from typing import Dict, Any, List, Optional
import json
import httpx
from backend.config import settings


class LLMService:
    """LLM wrapper supporting Google Gemini, Groq, and a rule-based intent router fallback."""

    def __init__(self):
        self.gemini_key = settings.GEMINI_API_KEY
        self.groq_key = settings.GROQ_API_KEY

    async def generate_response(self, prompt: str, system_prompt: str = "") -> Optional[str]:
        # 1. Try Gemini API if key is provided
        if self.gemini_key:
            try:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={self.gemini_key}"
                payload = {
                    "contents": [{"parts": [{"text": f"{system_prompt}\n\n{prompt}"}]}]
                }
                async with httpx.AsyncClient(timeout=8.0) as client:
                    resp = await client.post(url, json=payload)
                    if resp.status_code == 200:
                        data = resp.json()
                        candidates = data.get("candidates", [])
                        if candidates:
                            text = candidates[0].get("content", {}).get("parts", [{}])[0].get("text", "")
                            if text:
                                return text
            except Exception:
                pass

        # 2. Try Groq if key is provided
        if self.groq_key:
            try:
                url = "https://api.groq.com/openai/v1/chat/completions"
                payload = {
                    "model": "llama-3.3-70b-versatile",
                    "messages": [
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": prompt}
                    ]
                }
                async with httpx.AsyncClient(timeout=8.0) as client:
                    resp = await client.post(
                        url,
                        json=payload,
                        headers={"Authorization": f"Bearer {self.groq_key}"}
                    )
                    if resp.status_code == 200:
                        return resp.json()["choices"][0]["message"]["content"]
            except Exception:
                pass

        # If no key, returns None to trigger rule-based router
        return None


llm_service = LLMService()

