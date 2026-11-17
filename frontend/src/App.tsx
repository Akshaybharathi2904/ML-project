import React, { useState, useEffect } from 'react';
import { Navbar } from './components/Navbar';
import { LandingPage } from './components/LandingPage';
import { DestinationExplorer } from './components/DestinationExplorer';
import { TripCustomizer } from './components/TripCustomizer';
import { ResultsDashboard } from './components/ResultsDashboard';
import { EvaluationPage } from './components/EvaluationPage';
import { TripCopilotModal } from './components/TripCopilotModal';
import { UserProfileModal } from './components/UserProfileModal';
import { Footer } from './components/Footer';
import { Destination, ItineraryResponse } from './types';
import { Sparkles } from 'lucide-react';

const DEFAULT_SAMPLE_ITINERARY: ItineraryResponse = {
  trip_id: 'TRIP-UDAIPUR-DEMO-01',
  destination: 'Udaipur',
  chosen_solution_index: 0,
  feasibility_score: 94.0,
  feasibility_breakdown: {
    time_feasibility: 96.0,
    budget_feasibility: 92.0,
    open_hours_feasibility: 100.0,
    pace_feasibility: 88.0
  },
  weather_summary: [
    {
      date: '2026-11-05',
      temp_min_c: 18.5,
      temp_max_c: 29.2,
      rain_probability_pct: 10.0,
      condition: 'Sunny and Clear',
      outdoor_suitability: 'Optimal (Comfortable)',
      suitability_score: 95.0,
      recommendation: 'Excellent weather for palace exploration and lake cruises.',
      data_source: 'Open-Meteo'
    },
    {
      date: '2026-11-06',
      temp_min_c: 19.0,
      temp_max_c: 28.5,
      rain_probability_pct: 15.0,
      condition: 'Partly Cloudy',
      outdoor_suitability: 'Optimal',
      suitability_score: 90.0,
      recommendation: 'Ideal conditions for heritage gardens and scenic hill viewpoints.',
      data_source: 'Open-Meteo'
    },
    {
      date: '2026-11-07',
      temp_min_c: 17.8,
      temp_max_c: 28.0,
      rain_probability_pct: 12.0,
      condition: 'Clear Blue Skies',
      outdoor_suitability: 'Optimal',
      suitability_score: 92.0,
      recommendation: 'Comfortable afternoon temperatures for bazaars and cultural havelis.',
      data_source: 'Open-Meteo'
    }
  ],
  solver_info: {
    algorithm: 'NSGA-II (TOPTW Multi-Objective)',
    generations: 30,
    population: 35,
    runtime_seconds: 2.14,
    total_pareto_front_solutions: 18,
    constraint_violation_rate: '0.0%'
  },
  data_source_labels: {
    recommender: 'Hybrid LightGBM Blender (TF-IDF + TruncatedSVD)',
    optimizer: 'NSGA-II with Domain Repair Operator',
    weather: 'Open-Meteo API (Cached)'
  },
  chosen_itinerary: {
    solution_index: 0,
    total_score: 4.82,
    total_cost_inr: 4350.0,
    total_travel_time_min: 75,
    category_diversity: 0.85,
    avg_crowd_level: 0.42,
    total_places: 7,
    is_knee_point: true,
    days: [
      {
        day_number: 1,
        date: '2026-11-05',
        total_travel_time_min: 25,
        total_visit_time_min: 240,
        total_cost_inr: 1650.0,
        feasibility: 96.0,
        stops: [
          {
            place_id: 'PLC_0001',
            place_name: 'City Palace Complex',
            category: 'heritage',
            city: 'Udaipur',
            lat: 24.5764,
            lon: 73.6835,
            arrival_time: '09:30',
            departure_time: '12:00',
            visit_duration_min: 150,
            travel_time_from_prev_min: 0,
            travel_distance_km: 0.0,
            cost_inr: 350.0,
            crowd_forecast: 0.65,
            disruption_risk: 'Low',
            is_indoor: true,
            personalization_score: 0.96,
            why_recommended: [
              'High preference match for Royal Heritage & Mewar architecture (96%).',
              'Collaborative filtering alignment with culturally focused travel profiles.',
              'Optimal morning slot avoiding peak afternoon tourist congestion.'
            ]
          },
          {
            place_id: 'PLC_0002',
            place_name: 'Lake Pichola Boating & Jagmandir',
            category: 'nature',
            city: 'Udaipur',
            lat: 24.5700,
            lon: 73.6780,
            arrival_time: '12:20',
            departure_time: '14:00',
            visit_duration_min: 100,
            travel_time_from_prev_min: 12,
            travel_distance_km: 1.8,
            cost_inr: 500.0,
            crowd_forecast: 0.55,
            disruption_risk: 'Low (Fair Weather)',
            is_indoor: false,
            personalization_score: 0.94,
            why_recommended: [
              'Top-ranked scenic attraction in Udaipur with high panoramic acclaim.',
              'Geographically contiguous to City Palace with minimal transit delay.',
              'Clear skies and calm water conditions forecasted by Open-Meteo.'
            ]
          },
          {
            place_id: 'PLC_0005',
            place_name: 'Bagore Ki Haveli Cultural Museum',
            category: 'museum',
            city: 'Udaipur',
            lat: 24.5790,
            lon: 73.6820,
            arrival_time: '15:30',
            departure_time: '17:30',
            visit_duration_min: 120,
            travel_time_from_prev_min: 10,
            travel_distance_km: 1.2,
            cost_inr: 150.0,
            crowd_forecast: 0.38,
            disruption_risk: 'Low (Indoor)',
            is_indoor: true,
            personalization_score: 0.89,
            why_recommended: [
              'Celebrated folk arts museum and evening Dharohar dance performances.',
              'Low entry fee adhering to configured budget constraints.',
              'High user review consensus (4.7/5.0) and rich artifact exhibits.'
            ]
          }
        ]
      },
      {
        day_number: 2,
        date: '2026-11-06',
        total_travel_time_min: 30,
        total_visit_time_min: 210,
        total_cost_inr: 1400.0,
        feasibility: 94.0,
        stops: [
          {
            place_id: 'PLC_0004',
            place_name: 'Saheliyon Ki Bari Royal Gardens',
            category: 'nature',
            city: 'Udaipur',
            lat: 24.6030,
            lon: 73.6870,
            arrival_time: '09:30',
            departure_time: '11:00',
            visit_duration_min: 90,
            travel_time_from_prev_min: 14,
            travel_distance_km: 3.5,
            cost_inr: 100.0,
            crowd_forecast: 0.32,
            disruption_risk: 'Low',
            is_indoor: false,
            personalization_score: 0.91,
            why_recommended: [
              'Historic marble fountains, lush lotus pools, and tranquil shaded paths.',
              'Morning visiting slot ensures pleasant ambient temperatures.',
              'High botanical diversity and relaxing unhurried pace.'
            ]
          },
          {
            place_id: 'PLC_0006',
            place_name: 'Monsoon Palace (Sajjangarh Fort)',
            category: 'heritage',
            city: 'Udaipur',
            lat: 24.5920,
            lon: 73.6400,
            arrival_time: '15:30',
            departure_time: '17:30',
            visit_duration_min: 120,
            travel_time_from_prev_min: 18,
            travel_distance_km: 7.2,
            cost_inr: 250.0,
            crowd_forecast: 0.60,
            disruption_risk: 'Low',
            is_indoor: false,
            personalization_score: 0.95,
            why_recommended: [
              'Hilltop fortress offering sunset panoramas over Udaipur lakes.',
              'Ranked as a premier landscape viewpoint by peer collaborative profiles.',
              'Timed perfectly to catch the golden hour horizon.'
            ]
          }
        ]
      },
      {
        day_number: 3,
        date: '2026-11-07',
        total_travel_time_min: 20,
        total_visit_time_min: 180,
        total_cost_inr: 1300.0,
        feasibility: 92.0,
        stops: [
          {
            place_id: 'PLC_0003',
            place_name: 'Jagdish Temple',
            category: 'temple',
            city: 'Udaipur',
            lat: 24.5795,
            lon: 73.6840,
            arrival_time: '09:00',
            departure_time: '10:30',
            visit_duration_min: 90,
            travel_time_from_prev_min: 8,
            travel_distance_km: 1.1,
            cost_inr: 0.0,
            crowd_forecast: 0.45,
            disruption_risk: 'Low',
            is_indoor: true,
            personalization_score: 0.88,
            why_recommended: [
              'Indo-Aryan architecture with intricately carved pillars and spiritual aura.',
              'Free community access providing maximum value on day budget.',
              'Convenient walking distance from Old City bazaars.'
            ]
          },
          {
            place_id: 'PLC_0008',
            place_name: 'Bada Bazaar & Hathi Pol Handicrafts',
            category: 'shopping',
            city: 'Udaipur',
            lat: 24.5820,
            lon: 73.6880,
            arrival_time: '11:00',
            departure_time: '13:00',
            visit_duration_min: 120,
            travel_time_from_prev_min: 6,
            travel_distance_km: 0.9,
            cost_inr: 500.0,
            crowd_forecast: 0.50,
            disruption_risk: 'Low',
            is_indoor: false,
            personalization_score: 0.86,
            why_recommended: [
              'Authentic Rajasthani mojris, bandhani textiles, and Pichwai paintings.',
              'High category diversity balancing heritage and cultural commerce.',
              'Local food stalls offering traditional kachoris and sweets nearby.'
            ]
          }
        ]
      }
    ]
  },
  pareto_solutions: [
    {
      solution_index: 0,
      total_score: 4.82,
      total_cost_inr: 4350.0,
      total_travel_time_min: 75,
      category_diversity: 0.85,
      avg_crowd_level: 0.42,
      total_places: 7,
      is_knee_point: true,
      days: []
    },
    {
      solution_index: 1,
      total_score: 4.20,
      total_cost_inr: 2950.0,
      total_travel_time_min: 60,
      category_diversity: 0.72,
      avg_crowd_level: 0.38,
      total_places: 5,
      is_knee_point: false,
      days: []
    },
    {
      solution_index: 2,
      total_score: 5.10,
      total_cost_inr: 6200.0,
      total_travel_time_min: 95,
      category_diversity: 0.92,
      avg_crowd_level: 0.55,
      total_places: 9,
      is_knee_point: false,
      days: []
    },
    {
      solution_index: 3,
      total_score: 4.65,
      total_cost_inr: 3800.0,
      total_travel_time_min: 80,
      category_diversity: 0.80,
      avg_crowd_level: 0.40,
      total_places: 6,
      is_knee_point: false,
      days: []
    }
  ]
};

export function App() {
  const urlParamView = new URLSearchParams(window.location.search).get('view') as any;
  const [currentView, setCurrentView] = useState<'landing' | 'explorer' | 'customize' | 'dashboard' | 'evaluation'>(
    urlParamView && ['landing', 'explorer', 'customize', 'dashboard', 'evaluation'].includes(urlParamView)
      ? urlParamView
      : 'landing'
  );
  const [selectedDestination, setSelectedDestination] = useState<Destination | null>(null);
  const [activeItinerary, setActiveItinerary] = useState<ItineraryResponse | null>(DEFAULT_SAMPLE_ITINERARY);
  const [isCopilotOpen, setIsCopilotOpen] = useState<boolean>(false);
  const [isProfileOpen, setIsProfileOpen] = useState<boolean>(false);

  // Handlers
  const handleStartPlanning = () => {
    setCurrentView('explorer');
  };

  const handleSelectDestination = (dest: Destination) => {
    setSelectedDestination(dest);
    setCurrentView('customize');
  };

  const handleItineraryGenerated = (data: ItineraryResponse) => {
    setActiveItinerary(data);
    setCurrentView('dashboard');
  };

  return (
    <div className="min-h-screen bg-[#060a12] text-slate-100 flex flex-col font-sans selection:bg-teal-500 selection:text-slate-950">
      {/* Top Navbar */}
      <Navbar
        currentView={currentView}
        onNavigate={view => setCurrentView(view as any)}
        onOpenCopilot={() => setIsCopilotOpen(true)}
        onOpenProfile={() => setIsProfileOpen(true)}
        hasItinerary={!!activeItinerary}
      />

      {/* Main View Router */}
      <main className="flex-1">
        {currentView === 'landing' && (
          <LandingPage
            onStartPlanning={handleStartPlanning}
            onExploreDestinations={() => setCurrentView('explorer')}
            onViewEvaluation={() => setCurrentView('evaluation')}
          />
        )}

        {currentView === 'explorer' && (
          <DestinationExplorer
            onSelectDestination={handleSelectDestination}
          />
        )}

        {currentView === 'customize' && (
          <TripCustomizer
            initialDestination={selectedDestination}
            onItineraryGenerated={handleItineraryGenerated}
            onBack={() => setCurrentView('explorer')}
          />
        )}

        {currentView === 'dashboard' && activeItinerary && (
          <ResultsDashboard
            itineraryData={activeItinerary}
            onUpdateItinerary={updated => setActiveItinerary(updated)}
            onBackToCustomize={() => setCurrentView('customize')}
            onOpenCopilot={() => setIsCopilotOpen(true)}
          />
        )}

        {currentView === 'evaluation' && (
          <EvaluationPage />
        )}
      </main>

      {/* Persistent Floating AI Copilot Trigger */}
      <button
        onClick={() => setIsCopilotOpen(true)}
        className="fixed bottom-6 right-6 z-40 bg-gradient-to-r from-teal-500 to-emerald-600 hover:from-teal-400 hover:to-emerald-500 text-slate-950 font-bold px-4 py-3 rounded-full shadow-2xl shadow-teal-500/30 flex items-center space-x-2.5 transition transform hover:scale-105 cursor-pointer border border-teal-300/30"
      >
        <Sparkles className="w-5 h-5 text-slate-950 fill-slate-950" />
        <span className="text-sm tracking-wide">Trip Copilot</span>
      </button>

      {/* Trip Copilot Modal */}
      <TripCopilotModal
        isOpen={isCopilotOpen}
        onClose={() => setIsCopilotOpen(false)}
        destination={selectedDestination?.name || activeItinerary?.destination || 'Udaipur'}
        tripId={activeItinerary?.trip_id}
        onApplyPlanChange={(updated) => {
          if (updated) {
            setActiveItinerary(updated);
            setCurrentView('dashboard');
          }
        }}
      />

      {/* User Profile & Travel History Modal */}
      <UserProfileModal
        isOpen={isProfileOpen}
        onClose={() => setIsProfileOpen(false)}
        currentTrip={activeItinerary}
        onLoadTrip={(loaded) => {
          setActiveItinerary(loaded);
          setCurrentView('dashboard');
        }}
      />

      {/* Footer */}
      <Footer />
    </div>
  );
}

export default App;
