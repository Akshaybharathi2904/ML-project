import { Destination, Place, WeatherForecast, ItineraryResponse, EvaluationData, StateItem, CategoryItem } from '../types';

const API_BASE = 'http://localhost:8000/api';

export const api = {
  async getDestinations(query: string = '', state: string = '', category: string = '', sort_by: string = 'name_asc'): Promise<Destination[]> {
    try {
      const params = new URLSearchParams({ q: query, state, category, sort_by, limit: '500' });
      const res = await fetch(`${API_BASE}/destinations/search?${params.toString()}`);
      if (res.ok) {
        const json = await res.json();
        // New search endpoint returns { destinations, total, ... }
        const data = json.data;
        if (data && Array.isArray(data.destinations)) return data.destinations;
        if (Array.isArray(data)) return data;
        return [];
      }
    } catch (e) {
      console.warn('API error, falling back to mock destination data:', e);
    }
    // Fallback destinations
    return [
      {
        id: 'udaipur',
        name: 'Udaipur',
        state: 'Rajasthan',
        lat: 24.5854,
        lon: 73.7125,
        best_season: 'October to March',
        approx_daily_budget_inr: 4200,
        recommended_duration_days: 3,
        overview: 'City of Lakes steeped in royal Mewar Rajput palaces and serene waters.',
        image_url: 'https://images.unsplash.com/photo-1599661046289-e31897846e41?w=800'
      },
      {
        id: 'jaipur',
        name: 'Jaipur',
        state: 'Rajasthan',
        lat: 26.9124,
        lon: 75.7873,
        best_season: 'October to March',
        approx_daily_budget_inr: 3800,
        recommended_duration_days: 3,
        overview: 'The Pink City celebrated for grand forts, palaces, and vibrant bazaars.',
        image_url: 'https://images.unsplash.com/photo-1477587458883-47145ed94245?w=800'
      },
      {
        id: 'ooty',
        name: 'Ooty',
        state: 'Tamil Nadu',
        lat: 11.4102,
        lon: 76.6950,
        best_season: 'October to June',
        approx_daily_budget_inr: 3500,
        recommended_duration_days: 3,
        overview: 'Queen of Nilgiri Hill Stations famous for tea estates and toy train.',
        image_url: 'https://images.unsplash.com/photo-1589308078059-be1415eab4c3?w=800'
      },
      {
        id: 'munnar',
        name: 'Munnar',
        state: 'Kerala',
        lat: 10.0889,
        lon: 77.0595,
        best_season: 'September to May',
        approx_daily_budget_inr: 3800,
        recommended_duration_days: 3,
        overview: 'Idyllic hill retreat wrapped in sprawling emerald tea plantations.',
        image_url: 'https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?w=800'
      },
      {
        id: 'goa',
        name: 'Goa',
        state: 'Goa',
        lat: 15.2993,
        lon: 74.1240,
        best_season: 'November to February',
        approx_daily_budget_inr: 4500,
        recommended_duration_days: 4,
        overview: 'Sun-soaked coastal paradise famed for beaches, heritage, and nightlife.',
        image_url: 'https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?w=800'
      },
      {
        id: 'varanasi',
        name: 'Varanasi',
        state: 'Uttar Pradesh',
        lat: 25.3176,
        lon: 82.9739,
        best_season: 'October to March',
        approx_daily_budget_inr: 2800,
        recommended_duration_days: 3,
        overview: 'One of the world oldest living cities and sacred spiritual capital.',
        image_url: 'https://images.unsplash.com/photo-1561361513-2d000a50f0dc?w=800'
      }
    ];
  },

  async getDestinationStates(): Promise<StateItem[]> {
    try {
      const res = await fetch(`${API_BASE}/destinations/states`);
      if (res.ok) {
        const json = await res.json();
        return json.data || [];
      }
    } catch (e) {
      console.warn('Failed to load destination states:', e);
    }
    return [];
  },

  async getDestinationCategories(): Promise<CategoryItem[]> {
    try {
      const res = await fetch(`${API_BASE}/destinations/categories`);
      if (res.ok) {
        const json = await res.json();
        return json.data || [];
      }
    } catch (e) {
      console.warn('Failed to load destination categories:', e);
    }
    return [];
  },

  async getDestinationById(id: string): Promise<Destination | null> {
    try {
      const res = await fetch(`${API_BASE}/destinations/${encodeURIComponent(id)}`);
      if (res.ok) {
        const json = await res.json();
        return json.data || null;
      }
    } catch (e) {
      console.warn('Failed to load destination details:', e);
    }
    return null;
  },

  async getPopularDestinations(limit: number = 20): Promise<Destination[]> {
    try {
      const res = await fetch(`${API_BASE}/destinations/popular?limit=${limit}`);
      if (res.ok) {
        const json = await res.json();
        return json.data || [];
      }
    } catch (e) {
      console.warn('Failed to load popular destinations:', e);
    }
    return [];
  },

  async generateItinerary(payload: any): Promise<ItineraryResponse> {
    const res = await fetch(`${API_BASE}/itinerary/generate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    if (!res.ok) {
      throw new Error(`Failed to synthesize itinerary: ${res.statusText}`);
    }
    const json = await res.json();
    return json.data;
  },

  async selectParetoSolution(tripId: string, solutionIndex: number): Promise<ItineraryResponse> {
    const res = await fetch(`${API_BASE}/itinerary/select-solution`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ trip_id: tripId, solution_index: solutionIndex })
    });
    if (!res.ok) throw new Error('Failed to select solution');
    const json = await res.json();
    return json.data;
  },

  async replanItinerary(payload: any): Promise<any> {
    const res = await fetch(`${API_BASE}/itinerary/replan`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    if (!res.ok) throw new Error('Failed to replan');
    const json = await res.json();
    return json.data;
  },

  async swapActivity(payload: { trip_id: string; day_number: number; old_place_id: string; new_place_id: string }): Promise<any> {
    const res = await fetch(`${API_BASE}/itinerary/swap`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    if (!res.ok) throw new Error('Failed to swap');
    const json = await res.json();
    return json.data;
  },

  async sendChatMessage(payload: { trip_id?: string; destination: string; message: string }): Promise<any> {
    const res = await fetch(`${API_BASE}/chat`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    if (!res.ok) throw new Error('Chat request failed');
    const json = await res.json();
    return json.data;
  },

  async simulateRain(tripId: string): Promise<any> {
    const res = await fetch(`${API_BASE}/simulation/rain`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ trip_id: tripId })
    });
    if (!res.ok) throw new Error('Simulation failed');
    const json = await res.json();
    return json.data;
  },

  async simulateCrowd(tripId: string): Promise<any> {
    const res = await fetch(`${API_BASE}/simulation/crowd`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ trip_id: tripId })
    });
    if (!res.ok) throw new Error('Simulation failed');
    const json = await res.json();
    return json.data;
  },

  async simulateBudget(tripId: string, cutPercentage: number): Promise<any> {
    const res = await fetch(`${API_BASE}/simulation/budget`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ trip_id: tripId, cut_percentage: cutPercentage })
    });
    if (!res.ok) throw new Error('Simulation failed');
    const json = await res.json();
    return json.data;
  },

  async getEvaluationSummary(): Promise<EvaluationData> {
    try {
      const res = await fetch(`${API_BASE}/evaluation/summary`);
      if (res.ok) {
        const json = await res.json();
        return json.data;
      }
    } catch (e) {
      console.warn('Evaluation summary fetch error:', e);
    }
    return {
      recommender_ablation: [],
      optimizer_benchmarks: [],
      end_to_end_satisfaction: [],
      predictor_models: {}
    };
  },

  async getShapExplanation(placeId: string, destination: string = 'Udaipur') {
    const res = await fetch(`${API_BASE}/recommend/explain/${placeId}?destination=${encodeURIComponent(destination)}`);
    if (!res.ok) throw new Error('Failed to fetch SHAP explanation');
    const json = await res.json();
    return json.data;
  },

  async optimizeRoute(tripId: string, dayNumber: number): Promise<ItineraryResponse> {
    const res = await fetch(`${API_BASE}/itinerary/optimize-route`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ trip_id: tripId, day_number: dayNumber })
    });
    if (!res.ok) throw new Error('Route optimization failed');
    const json = await res.json();
    return json.data;
  },

  async removeStop(tripId: string, dayNumber: number, placeId: string): Promise<ItineraryResponse> {
    const res = await fetch(`${API_BASE}/itinerary/remove-stop`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ trip_id: tripId, day_number: dayNumber, place_id: placeId })
    });
    if (!res.ok) throw new Error('Failed to remove stop');
    const json = await res.json();
    return json.data;
  },

  async getBudgetBreakdown(tripId: string, budgetCap?: number) {
    const url = budgetCap ? `${API_BASE}/itinerary/${tripId}/budget-breakdown?budget_cap=${budgetCap}` : `${API_BASE}/itinerary/${tripId}/budget-breakdown`;
    const res = await fetch(url);
    if (!res.ok) throw new Error('Failed to retrieve budget breakdown');
    const json = await res.json();
    return json.data;
  },

  async applyCopilotAction(tripId: string, action: string, parameters: any = {}): Promise<ItineraryResponse> {
    const res = await fetch(`${API_BASE}/chat/apply-action`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ trip_id: tripId, action, parameters })
    });
    if (!res.ok) throw new Error('Failed to execute Copilot action');
    const json = await res.json();
    return json.data;
  },

  async getPlaceCrowd(placeId: string, destination: string = 'Udaipur', hour: number = 12) {
    const res = await fetch(`${API_BASE}/predictions/crowd/place/${placeId}?destination=${encodeURIComponent(destination)}&hour=${hour}`);
    if (!res.ok) throw new Error('Failed to load crowd analytics');
    const json = await res.json();
    return json.data;
  },

  async loginUser(username: string) {
    const res = await fetch(`${API_BASE}/users/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username })
    });
    if (!res.ok) throw new Error('Failed to login user');
    const json = await res.json();
    return json.data;
  },

  async getUserProfile(userId: string) {
    const res = await fetch(`${API_BASE}/users/profile/${userId}`);
    if (!res.ok) throw new Error('Failed to get user profile');
    const json = await res.json();
    return json.data;
  },

  async updateUserProfile(userId: string, data: any) {
    const res = await fetch(`${API_BASE}/users/profile/${userId}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    if (!res.ok) throw new Error('Failed to update user profile');
    const json = await res.json();
    return json.data;
  },

  async submitPlaceRating(userId: string, placeId: string, rating: number, feedback: string = '') {
    const res = await fetch(`${API_BASE}/users/ratings`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ user_id: userId, place_id: placeId, rating, feedback })
    });
    if (!res.ok) throw new Error('Failed to submit rating');
    const json = await res.json();
    return json.data;
  },

  async getUserRatings(userId: string) {
    const res = await fetch(`${API_BASE}/users/ratings/${userId}`);
    if (!res.ok) return [];
    const json = await res.json();
    return json.data || [];
  },

  async getUserTripHistory(userId: string) {
    const res = await fetch(`${API_BASE}/users/history/${userId}`);
    if (!res.ok) return [];
    const json = await res.json();
    return json.data || [];
  },

  async saveTripToHistory(userId: string, tripId: string, name?: string) {
    const res = await fetch(`${API_BASE}/users/trips/save`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ user_id: userId, trip_id: tripId, name })
    });
    if (!res.ok) throw new Error('Failed to save trip');
    const json = await res.json();
    return json.data;
  },

  async reuseTrip(tripId: string): Promise<ItineraryResponse> {
    const res = await fetch(`${API_BASE}/users/trips/reuse`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ trip_id: tripId })
    });
    if (!res.ok) throw new Error('Failed to reuse trip');
    const json = await res.json();
    return json.data;
  }
};

