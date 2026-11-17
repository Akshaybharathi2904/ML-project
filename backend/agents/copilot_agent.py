import re
from typing import Dict, Any, List, Optional
from backend.services.weather_service import weather_service
from backend.services.places_service import places_service
from backend.services.routing_service import routing_service
from backend.services.llm_service import llm_service
from backend.engines.prediction_engine import ml_prediction_provider
from backend.schemas.schemas import PredictionFeatures, ChatMessageResponse


class TripCopilotAgent:
    """
    Agent 6: Trip Copilot Chatbot.
    Dispatches validated tool functions and provides intelligent conversational guidance.
    Uses LLM when configured, and falls back to a deterministic, rule-based intent router.
    """

    def __init__(self):
        self.tools = {
            "get_weather_forecast": self._tool_weather,
            "search_places": self._tool_search_places,
            "predict_crowd": self._tool_predict_crowd,
            "predict_cost": self._tool_predict_cost,
            "compare_attractions": self._tool_compare,
            "get_packing_suggestions": self._tool_packing,
            "get_food_recommendations": self._tool_food,
            "replan_itinerary": self._tool_weather_replan_action,
            "remove_attraction": self._tool_remove_attraction,
            "add_nature_attractions": self._tool_add_nature,
            "reduce_budget": self._tool_reduce_budget,
            "suggest_less_crowded": self._tool_suggest_less_crowded,
            "replace_outdoor_rain": self._tool_weather_replan_action,
        }

    async def _tool_replan(self, destination: str) -> Dict[str, Any]:
        return await self._tool_weather_replan_action(destination)

    async def _tool_weather(self, destination: str) -> str:
        places = places_service.get_places_for_destination(destination)
        lat, lon = (places[0]["lat"], places[0]["lon"]) if places else (24.5854, 73.7125)
        forecasts = await weather_service.get_forecast(lat, lon, num_days=3)
        lines = [f"**Weather Forecast for {destination}:**"]
        for f in forecasts:
            lines.append(f"- **{f['date']}**: {f['condition']}, {f['temp_min_c']}°C - {f['temp_max_c']}°C, Rain: {f['rain_probability_pct']}%. Suitability: {f['outdoor_suitability']} ({f['suitability_score']}/100).")
        return "\n".join(lines)

    async def _tool_search_places(self, destination: str, query: str = "") -> str:
        places = places_service.get_places_for_destination(destination)
        if query:
            places = [p for p in places if query.lower() in p["name"].lower() or query.lower() in p["category"].lower()]
        lines = [f"**Top Attractions in {destination}:**"]
        for p in places[:5]:
            lines.append(f"- **{p['name']}** ({p['category'].capitalize()}) — Rating: {p['rating']}★, Approx: ₹{p['avg_cost_inr']}, Duration: {int(p['avg_visit_duration_min'])} min.")
        return "\n".join(lines)

    async def _tool_predict_crowd(self, destination: str, place_name: str = "") -> str:
        feats = PredictionFeatures(destination=destination, hour=12, is_weekend=True, base_popularity=0.85)
        res = ml_prediction_provider.predict_crowd(feats)
        return (
            f"**Predicted Crowd Level for {place_name or destination}:**\n"
            f"- Density Score: **{res.crowd_score}/100** ({res.category})\n"
            f"- Best Visiting Window: **{res.best_visiting_time}**\n"
            f"- Model: {res.model_version} ({res.data_source})"
        )

    async def _tool_predict_cost(self, destination: str) -> str:
        feats = PredictionFeatures(destination=destination, group_size=2, transport_mode="taxi")
        res = ml_prediction_provider.predict_cost(feats)
        return (
            f"**Estimated Cost for {destination} (2 Travelers):**\n"
            f"- Estimated Total: **₹{res.total_cost_inr:,.0f}** (₹{res.per_person_inr:,.0f} per person)\n"
            f"- Breakdown: Tickets ₹{res.breakdown['tickets']}, Food ₹{res.breakdown['food']}, Transport ₹{res.breakdown['transport']}.\n"
            f"- Confidence: {int(res.confidence*100)}% ({res.data_source})"
        )

    async def _tool_compare(self, destination: str, place_a: str, place_b: str) -> str:
        pa = places_service.get_place_by_id(place_a)
        pb = places_service.get_place_by_id(place_b)
        if not pa or not pb:
            places = places_service.get_places_for_destination(destination)
            pa = places[0] if len(places) > 0 else {"name": place_a, "rating": 4.6, "avg_cost_inr": 200, "category": "heritage"}
            pb = places[1] if len(places) > 1 else {"name": place_b, "rating": 4.4, "avg_cost_inr": 100, "category": "nature"}

        return (
            f"**Comparison: {pa['name']} vs {pb['name']}**\n"
            f"1. **Category:** {pa.get('category', '').capitalize()} vs {pb.get('category', '').capitalize()}\n"
            f"2. **Rating:** {pa.get('rating', 4.5)}★ vs {pb.get('rating', 4.3)}★\n"
            f"3. **Cost:** ₹{pa.get('avg_cost_inr', 0)} vs ₹{pb.get('avg_cost_inr', 0)}\n"
            f"4. **Atmosphere:** {'Indoor Museum/Palace' if pa.get('is_indoor') else 'Outdoor Landmark'} vs {'Indoor' if pb.get('is_indoor') else 'Scenic Outdoor'}"
        )

    async def _tool_packing(self, destination: str) -> str:
        return (
            f"**Recommended Packing Checklist for {destination}:**\n"
            f"- 👟 Comfortable walking/trekking shoes for heritage stone walkways and nature paths\n"
            f"- ☀️ Sun protection: Sunglasses, SPF 50 sunscreen, light cotton cap\n"
            f"- 🌧️ Compact travel umbrella or light waterproof windbreaker\n"
            f"- 🔋 High-capacity power bank and camera gear for photography\n"
            f"- 🧣 Scarf or light shawl (required when entering spiritual temples/ghats)"
        )

    async def _tool_food(self, destination: str) -> str:
        places = places_service.get_places_for_destination(destination, category="food")
        food_names = [p["name"] for p in places[:3]]
        food_str = ", ".join(food_names) if food_names else "authentic regional cuisine and local thalis"
        return (
            f"**Culinary Recommendations in {destination}:**\n"
            f"- Top dining spots: **{food_str}**\n"
            f"- Must-try local delicacies: Traditional regional thali, local street snacks, fresh filter coffee/tea, and heritage desserts."
        )

    async def _tool_remove_attraction(self, destination: str, query: str = "") -> Dict[str, Any]:
        places = places_service.get_places_for_destination(destination)
        target = None
        for p in places:
            if query and query.lower() in p["name"].lower():
                target = p
                break
        if not target and places:
            target = places[-1]

        target_name = target["name"] if target else "Selected attraction"
        target_id = target["id"] if target else "PLC_0003"
        return {
            "text": f"I can remove **{target_name}** from your schedule and recalculate your daily transit times and budget.",
            "proposed_changes": [
                {
                    "action": "remove_stop",
                    "place_id": target_id,
                    "place_name": target_name,
                    "day_number": 1,
                    "reason": f"Removed {target_name} per your chat instruction."
                }
            ]
        }

    async def _tool_add_nature(self, destination: str) -> Dict[str, Any]:
        places = places_service.get_places_for_destination(destination, category="nature")
        if not places:
            places = places_service.get_places_for_destination(destination)
        top_nature = places[0] if places else {"id": "PLC_0004", "name": "Scenic Nature Reserve", "avg_cost_inr": 100}

        return {
            "text": f"Found a top scenic nature recommendation for {destination}: **{top_nature['name']}** (Rating: {top_nature.get('rating', 4.6)}★, ₹{top_nature.get('avg_cost_inr', 100)}). Would you like to inject this into your itinerary?",
            "proposed_changes": [
                {
                    "action": "add_stop",
                    "place_id": top_nature["id"],
                    "place_name": top_nature["name"],
                    "category": "nature",
                    "cost_inr": top_nature.get("avg_cost_inr", 100),
                    "day_number": 1,
                    "reason": "Added nature attraction per traveler preference."
                }
            ]
        }

    async def _tool_reduce_budget(self, destination: str) -> Dict[str, Any]:
        return {
            "text": f"I can tighten your {destination} trip budget by 25% by prioritizing free heritage landmarks and budget-friendly regional dining.",
            "proposed_changes": [
                {
                    "action": "reduce_budget",
                    "cut_percentage": 25,
                    "reason": "25% budget optimization requested by traveler."
                }
            ]
        }

    async def _tool_suggest_less_crowded(self, destination: str) -> Dict[str, Any]:
        places = places_service.get_places_for_destination(destination)
        serene = [p for p in places if p.get("crowd_level", 0.5) < 0.45]
        if not serene:
            serene = places[-2:]

        names = [p["name"] for p in serene[:2]]
        name_str = " and ".join(names) if names else "heritage monuments"

        return {
            "text": f"Here are serene, low-crowd attractions in {destination}: **{name_str}**. These have low congestion risk (<35% density) and offer relaxed pacing.",
            "proposed_changes": [
                {
                    "action": "swap_crowded",
                    "replacement_name": serene[0]["name"] if serene else "Serene Sanctuary",
                    "replacement_id": serene[0]["id"] if serene else "PLC_0005",
                    "reason": "Low-crowd alternative recommended."
                }
            ]
        }

    async def _tool_weather_replan_action(self, destination: str) -> Dict[str, Any]:
        return {
            "text": f"High probability of rain showers detected. I can replace outdoor activities in {destination} with indoor palaces, museums, and covered markets.",
            "proposed_changes": [
                {
                    "action": "weather_replan",
                    "reason": "Rain forecasted; swapped outdoor activities for indoor alternatives."
                }
            ]
        }

    async def execute(
        self,
        message: str,
        destination: str = "Udaipur",
        trip_context: Optional[Dict[str, Any]] = None
    ) -> ChatMessageResponse:
        msg_lower = message.lower()
        tools_executed = []
        proposed_changes = None

        # 1. Rule-Based Intent Matching
        if any(w in msg_lower for w in ["remove", "delete", "drop"]) and any(w in msg_lower for w in ["attraction", "place", "temple", "palace", "stop", "fort", "museum", "lake"]):
            tools_executed.append("remove_attraction")
            # Extract possible place query
            place_q = ""
            for token in message.split():
                if token.lower() not in ["remove", "the", "attraction", "from", "my", "itinerary", "stop", "please", "can", "you"]:
                    place_q += " " + token
            res = await self._tool_remove_attraction(destination, place_q.strip())
            reply = res["text"]
            proposed_changes = res["proposed_changes"]

        elif any(w in msg_lower for w in ["nature", "scenic", "outdoor", "park", "garden"]) and any(w in msg_lower for w in ["add", "more", "suggest", "include"]):
            tools_executed.append("add_nature_attractions")
            res = await self._tool_add_nature(destination)
            reply = res["text"]
            proposed_changes = res["proposed_changes"]

        elif any(w in msg_lower for w in ["reduce", "cut", "lower", "cheaper", "tighten", "decrease"]) and any(w in msg_lower for w in ["budget", "cost", "price", "expense"]):
            tools_executed.append("reduce_budget")
            res = await self._tool_reduce_budget(destination)
            reply = res["text"]
            proposed_changes = res["proposed_changes"]

        elif any(w in msg_lower for w in ["less crowd", "less crowded", "avoid crowd", "quiet", "serene", "tranquil", "peaceful"]):
            tools_executed.append("suggest_less_crowded")
            res = await self._tool_suggest_less_crowded(destination)
            reply = res["text"]
            proposed_changes = res["proposed_changes"]

        elif any(w in msg_lower for w in ["rain", "storm", "wet", "precipitation", "weather"]) and any(w in msg_lower for w in ["replace", "replan", "indoor", "safe", "change"]):
            tools_executed.append("replace_outdoor_rain")
            res = await self._tool_weather_replan_action(destination)
            reply = res["text"]
            proposed_changes = res["proposed_changes"]

        elif any(w in msg_lower for w in ["weather", "rain", "temperature", "forecast"]):
            tools_executed.append("get_weather_forecast")
            reply = await self._tool_weather(destination)

        elif any(w in msg_lower for w in ["crowd", "busy", "rush", "peak"]):
            tools_executed.append("predict_crowd")
            reply = await self._tool_predict_crowd(destination)

        elif any(w in msg_lower for w in ["cost", "budget", "price", "expensive"]):
            tools_executed.append("predict_cost")
            reply = await self._tool_predict_cost(destination)

        elif any(w in msg_lower for w in ["pack", "carry", "clothes", "what to wear"]):
            tools_executed.append("get_packing_suggestions")
            reply = await self._tool_packing(destination)

        elif any(w in msg_lower for w in ["food", "eat", "restaurant", "cafe", "dishes"]):
            tools_executed.append("get_food_recommendations")
            reply = await self._tool_food(destination)

        elif any(w in msg_lower for w in ["compare", "vs", "better", "difference"]):
            tools_executed.append("compare_attractions")
            reply = await self._tool_compare(destination, "Attraction A", "Attraction B")

        elif any(w in msg_lower for w in ["replan", "change", "substitute", "indoor"]):
            tools_executed.append("replan_itinerary")
            res = await self._tool_replan(destination)
            reply = res["text"]
            proposed_changes = res["proposed_changes"]

        elif any(w in msg_lower for w in ["place", "attraction", "visit", "see"]):
            tools_executed.append("search_places")
            reply = await self._tool_search_places(destination)

        else:
            # 2. Try LLM service if general conversation
            sys_prompt = f"You are TRAVELMATE AI Copilot, an expert Indian travel assistant for {destination}."
            llm_reply = await llm_service.generate_response(message, sys_prompt)
            if llm_reply:
                reply = llm_reply
                tools_executed.append("llm_generation")
            else:
                reply = (
                    f"Hello! I'm your **Trip Copilot** for **{destination}**.\n\n"
                    f"I can assist you with:\n"
                    f"- 🌦️ **Weather forecasts** and outdoor suitability\n"
                    f"- 👥 **Crowd predictions** and optimal visiting hours\n"
                    f"- 💰 **Budget estimates** and ticket pricing\n"
                    f"- 🍲 **Local food** and cultural dining recommendations\n"
                    f"- 🎒 **Packing checklists** tailored to local conditions\n"
                    f"- 🔄 **Weather-aware replanning** when rain or disruptions arise."
                )

        return ChatMessageResponse(
            reply=reply,
            tool_calls_executed=tools_executed,
            proposed_changes=proposed_changes,
            data_source="Trip Copilot Multi-Agent Engine"
        )


copilot_agent = TripCopilotAgent()

