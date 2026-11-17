import React, { useState, useEffect, useMemo, useRef } from 'react';
import { Compass, Calendar, IndianRupee, Users, Sliders, Star, Sparkles, CheckCircle2, ArrowLeft, Search, ChevronDown, X, MapPin } from 'lucide-react';
import { Destination, ItineraryResponse } from '../types';
import { api } from '../services/api';

interface TripCustomizerProps {
  destinations?: Destination[];
  initialDestination?: Destination | string | null;
  onItineraryGenerated: (data: ItineraryResponse) => void;
  onBack?: () => void;
}

const CATEGORIES = [
  { key: 'heritage', label: 'Heritage & Forts' },
  { key: 'nature', label: 'Nature & Scenic' },
  { key: 'temple', label: 'Spiritual & Temples' },
  { key: 'adventure', label: 'Adventure & Trails' },
  { key: 'food', label: 'Food & Cafes' },
  { key: 'shopping', label: 'Shopping & Bazaars' },
  { key: 'museum', label: 'Museums & Art' },
  { key: 'wildlife', label: 'Wildlife & Safari' }
];

const SEED_ATTRACTIONS = [
  { id: 'PLC_0001', name: 'City Palace' },
  { id: 'PLC_0002', name: 'Lake Pichola Boating' },
  { id: 'PLC_0003', name: 'Jagdish Temple' },
  { id: 'PLC_0004', name: 'Saheliyon Ki Bari' },
  { id: 'PLC_0005', name: 'Bagore Ki Haveli' },
];

export const TripCustomizer: React.FC<TripCustomizerProps> = ({
  destinations: propDestinations,
  initialDestination,
  onItineraryGenerated,
  onBack
}) => {
  const initDestName = typeof initialDestination === 'string' 
    ? initialDestination 
    : initialDestination?.name || 'Udaipur';

  const [destinations, setDestinations] = useState<Destination[]>(propDestinations || []);
  const [destination, setDestination] = useState<string>(initDestName);
  const [startDate, setStartDate] = useState('2026-11-05');
  const [numDays, setNumDays] = useState(3);
  const [budget, setBudget] = useState(15000);
  const [pace, setPace] = useState<'relaxed' | 'moderate' | 'packed'>('moderate');
  const [transport, setTransport] = useState('taxi');
  const [travelers, setTravelers] = useState(2);
  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  // Searchable destination dropdown state
  const [destSearch, setDestSearch] = useState('');
  const [showDestDropdown, setShowDestDropdown] = useState(false);
  const destDropdownRef = useRef<HTMLDivElement>(null);

  // Interest Sliders (0.0 to 1.0)
  const [interests, setInterests] = useState<Record<string, number>>({
    heritage: 0.8,
    nature: 0.9,
    temple: 0.5,
    adventure: 0.6,
    food: 0.7,
    shopping: 0.4,
    museum: 0.6,
    wildlife: 0.5
  });

  // Seed Ratings for Collaborative Filtering Cold-Start Handling
  const [seedRatings, setSeedRatings] = useState<Record<string, number>>({
    'PLC_0001': 5,
    'PLC_0002': 4
  });

  const [progressStep, setProgressStep] = useState(0);

  useEffect(() => {
    if (!propDestinations || propDestinations.length === 0) {
      api.getDestinations().then(data => setDestinations(data));
    }
  }, [propDestinations]);

  useEffect(() => {
    if (initialDestination) {
      const name = typeof initialDestination === 'string' ? initialDestination : initialDestination.name;
      setDestination(name);
    }
  }, [initialDestination]);

  // Close destination dropdown on outside click
  useEffect(() => {
    const handler = (e: MouseEvent) => {
      if (destDropdownRef.current && !destDropdownRef.current.contains(e.target as Node)) {
        setShowDestDropdown(false);
      }
    };
    document.addEventListener('mousedown', handler);
    return () => document.removeEventListener('mousedown', handler);
  }, []);

  const PROGRESS_MESSAGES = [
    "Understanding your travel request...",
    "Retrieving destination geospatial graph...",
    "Analyzing Open-Meteo weather suitability...",
    "Scoring attractions via LightGBM Hybrid Recommender...",
    "Executing NSGA-II Multi-Objective Itinerary Optimization...",
    "Extracting Pareto optimal trade-offs & Knee Point...",
    "Finalizing day-by-day scheduled itinerary!"
  ];

  const handleInterestChange = (cat: string, val: number) => {
    setInterests(prev => ({ ...prev, [cat]: val }));
  };

  const handleSeedRating = (placeId: string, rating: number) => {
    setSeedRatings(prev => ({ ...prev, [placeId]: rating }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    setErrorMessage(null);

    const payload = {
      destination,
      start_date: startDate,
      num_days: numDays,
      budget_inr: budget,
      pace,
      transport,
      travelers_count: travelers,
      interests,
      seed_ratings: seedRatings
    };

    let step = 0;
    const interval = setInterval(() => {
      step = (step + 1) % PROGRESS_MESSAGES.length;
      setProgressStep(step);
    }, 600);

    try {
      const result = await api.generateItinerary(payload);
      onItineraryGenerated(result);
    } catch (err: any) {
      console.error(err);
      setErrorMessage(err.message || 'Failed to synthesize itinerary. Please try again.');
    } finally {
      clearInterval(interval);
      setIsLoading(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto py-8 px-4 sm:px-6">
      <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6 md:p-10 shadow-2xl space-y-8">
        
        {/* Header */}
        <div className="flex items-center justify-between">
          <div>
            <div className="flex items-center space-x-2">
              {onBack && (
                <button
                  type="button"
                  onClick={onBack}
                  className="mr-2 text-slate-400 hover:text-white transition"
                >
                  <ArrowLeft className="w-5 h-5" />
                </button>
              )}
              <h1 className="text-2xl sm:text-3xl font-extrabold text-white flex items-center gap-3">
                <Compass className="w-7 h-7 text-teal-400" />
                <span>Trip Customization Engine</span>
              </h1>
            </div>
            <p className="text-slate-400 text-xs sm:text-sm mt-1">
              Configure parameters, category preferences, and budget caps to guide the NSGA-II multi-objective optimizer.
            </p>
          </div>
        </div>

        {errorMessage && (
          <div className="p-4 rounded-xl bg-red-500/10 border border-red-500/30 text-red-400 text-xs">
            {errorMessage}
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-8">
          {/* Main Parameters */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Destination – Searchable Dropdown */}
            <div className="space-y-2">
              <label className="text-xs font-bold text-slate-300 uppercase tracking-wider">Destination</label>
              <div className="relative" ref={destDropdownRef}>
                <button
                  type="button"
                  onClick={() => setShowDestDropdown(v => !v)}
                  className="w-full flex items-center justify-between bg-slate-950 border border-slate-800 rounded-xl px-4 py-3 text-sm text-white focus:outline-none focus:border-teal-500 hover:border-slate-700 transition"
                >
                  <span className="flex items-center gap-2">
                    <MapPin className="w-4 h-4 text-teal-400 flex-shrink-0" />
                    {destination || 'Select destination...'}
                  </span>
                  <ChevronDown className={`w-4 h-4 text-slate-400 transition-transform ${showDestDropdown ? 'rotate-180' : ''}`} />
                </button>
                {showDestDropdown && (
                  <div className="absolute top-full left-0 right-0 mt-1 z-50 bg-slate-900 border border-slate-700 rounded-xl shadow-2xl">
                    {/* Search input */}
                    <div className="p-2 border-b border-slate-800">
                      <div className="relative">
                        <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-3.5 h-3.5 text-slate-400 pointer-events-none" />
                        <input
                          type="text"
                          value={destSearch}
                          onChange={e => setDestSearch(e.target.value)}
                          placeholder="Search destinations or states..."
                          className="w-full bg-slate-950 border border-slate-800 rounded-lg pl-9 pr-8 py-2 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-teal-500"
                          autoFocus
                        />
                        {destSearch && (
                          <button onClick={() => setDestSearch('')} className="absolute right-2 top-1/2 -translate-y-1/2 text-slate-500 hover:text-white">
                            <X className="w-3 h-3" />
                          </button>
                        )}
                      </div>
                    </div>
                    {/* Options */}
                    <div className="max-h-60 overflow-y-auto">
                      {(() => {
                        const q = destSearch.toLowerCase();
                        const filtered = destinations.filter(d =>
                          !q ||
                          d.name.toLowerCase().includes(q) ||
                          d.state.toLowerCase().includes(q)
                        );
                        // Group by state
                        const grouped: Record<string, Destination[]> = {};
                        filtered.forEach(d => {
                          const s = d.state;
                          if (!grouped[s]) grouped[s] = [];
                          grouped[s].push(d);
                        });
                        const sortedStates = Object.keys(grouped).sort();
                        if (filtered.length === 0) {
                          return <p className="text-center text-slate-500 text-xs py-6">No destinations found.</p>;
                        }
                        return sortedStates.map(state => (
                          <div key={state}>
                            <div className="sticky top-0 bg-slate-900/95 px-4 py-1.5 text-xs font-bold text-slate-500 uppercase tracking-wider border-b border-slate-800/50">
                              {state}
                            </div>
                            {grouped[state].map(d => (
                              <button
                                key={d.id || d.name}
                                type="button"
                                onClick={() => {
                                  setDestination(d.name);
                                  setShowDestDropdown(false);
                                  setDestSearch('');
                                }}
                                className={`w-full text-left px-4 py-2.5 text-sm flex items-center justify-between hover:bg-slate-800 transition ${destination === d.name ? 'text-teal-400 bg-teal-500/5' : 'text-slate-300'}`}
                              >
                                <span>{d.name}</span>
                                {destination === d.name && <CheckCircle2 className="w-3.5 h-3.5 text-teal-400" />}
                              </button>
                            ))}
                          </div>
                        ));
                      })()}
                    </div>
                  </div>
                )}
              </div>
            </div>

            {/* Start Date */}
            <div className="space-y-2">
              <label className="text-xs font-bold text-slate-300 uppercase tracking-wider">Start Date</label>
              <input
                type="date"
                value={startDate}
                onChange={(e) => setStartDate(e.target.value)}
                className="w-full bg-slate-950 border border-slate-800 rounded-xl px-4 py-3 text-sm text-white focus:outline-none focus:border-teal-500"
              />
            </div>

            {/* Days & Budget */}
            <div className="space-y-2">
              <div className="flex justify-between items-center">
                <label className="text-xs font-bold text-slate-300 uppercase tracking-wider">Duration</label>
                <span className="text-teal-400 font-bold text-sm">{numDays} Days</span>
              </div>
              <input
                type="range"
                min="1"
                max="7"
                value={numDays}
                onChange={(e) => setNumDays(Number(e.target.value))}
                className="w-full accent-teal-400 bg-slate-950"
              />
            </div>

            <div className="space-y-2">
              <div className="flex justify-between items-center">
                <label className="text-xs font-bold text-slate-300 uppercase tracking-wider">Total Trip Budget</label>
                <span className="text-emerald-400 font-bold text-sm">₹{budget.toLocaleString()}</span>
              </div>
              <input
                type="range"
                min="3000"
                max="60000"
                step="1000"
                value={budget}
                onChange={(e) => setBudget(Number(e.target.value))}
                className="w-full accent-emerald-400 bg-slate-950"
              />
            </div>

            {/* Pace & Transport */}
            <div className="space-y-2">
              <label className="text-xs font-bold text-slate-300 uppercase tracking-wider">Travel Pace</label>
              <div className="grid grid-cols-3 gap-2">
                {(['relaxed', 'moderate', 'packed'] as const).map(p => (
                  <button
                    type="button"
                    key={p}
                    onClick={() => setPace(p)}
                    className={`py-2.5 rounded-xl text-xs font-bold capitalize transition-all cursor-pointer ${
                      pace === p
                        ? 'bg-teal-500 text-slate-950 shadow-md shadow-teal-500/20'
                        : 'bg-slate-950 border border-slate-800 text-slate-400 hover:text-slate-200'
                    }`}
                  >
                    {p}
                  </button>
                ))}
              </div>
            </div>

            <div className="space-y-2">
              <label className="text-xs font-bold text-slate-300 uppercase tracking-wider">Transport Mode</label>
              <select
                value={transport}
                onChange={(e) => setTransport(e.target.value)}
                className="w-full bg-slate-950 border border-slate-800 rounded-xl px-4 py-3 text-sm text-white focus:outline-none focus:border-teal-500"
              >
                <option value="taxi">Private Taxi / Cab (Flexible)</option>
                <option value="auto">Auto Rickshaw (Local City)</option>
                <option value="walking">Walk & Public Transit</option>
              </select>
            </div>
          </div>

          {/* Interests & Weights */}
          <div className="space-y-4 pt-4 border-t border-slate-800">
            <div>
              <h3 className="text-base font-bold text-white flex items-center gap-2">
                <Sliders className="w-4 h-4 text-teal-400" />
                <span>Interests & Activity Preferences</span>
              </h3>
              <p className="text-xs text-slate-400 mt-1">
                Content-based TF-IDF features dynamically adapt based on these slider weights (0 to 100%).
              </p>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
              {CATEGORIES.map(cat => (
                <div key={cat.key} className="bg-slate-950 border border-slate-800/80 p-3.5 rounded-2xl space-y-2">
                  <div className="flex justify-between items-center text-xs">
                    <span className="font-semibold text-slate-200">{cat.label}</span>
                    <span className="text-teal-400 font-bold">{Math.round((interests[cat.key] || 0) * 100)}%</span>
                  </div>
                  <input
                    type="range"
                    min="0"
                    max="1"
                    step="0.05"
                    value={interests[cat.key] || 0}
                    onChange={(e) => handleInterestChange(cat.key, parseFloat(e.target.value))}
                    className="w-full accent-teal-400 bg-slate-900"
                  />
                </div>
              ))}
            </div>
          </div>

          {/* Collaborative Seed Ratings */}
          <div className="space-y-3 pt-4 border-t border-slate-800">
            <div className="flex items-center justify-between">
              <div>
                <h3 className="text-base font-bold text-white flex items-center gap-2">
                  <Star className="w-4 h-4 text-amber-400" />
                  <span>Seed Ratings (Cold-Start Resolution)</span>
                </h3>
                <p className="text-xs text-slate-400 mt-1">
                  Rate places you've visited to enable SVD matrix factorization collaborative folding-in.
                </p>
              </div>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-3">
              {SEED_ATTRACTIONS.map(item => (
                <div key={item.id} className="bg-slate-950 border border-slate-800/80 p-3 rounded-xl flex items-center justify-between">
                  <span className="text-xs text-slate-300 font-medium truncate max-w-[140px]">{item.name}</span>
                  <div className="flex gap-1">
                    {[1, 2, 3, 4, 5].map(star => (
                      <button
                        type="button"
                        key={star}
                        onClick={() => handleSeedRating(item.id, star)}
                        className={`text-xs cursor-pointer ${
                          (seedRatings[item.id] || 0) >= star ? 'text-amber-400' : 'text-slate-600 hover:text-amber-300'
                        }`}
                      >
                        ★
                      </button>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Submit Button & Progress State */}
          <div className="pt-4">
            {isLoading ? (
              <div className="bg-slate-950 border border-teal-500/30 p-5 rounded-2xl space-y-3 text-center animate-pulse">
                <div className="inline-block w-8 h-8 border-4 border-teal-500 border-t-transparent rounded-full animate-spin"></div>
                <p className="text-sm font-bold text-teal-300">{PROGRESS_MESSAGES[progressStep]}</p>
                <div className="w-full bg-slate-900 h-1.5 rounded-full overflow-hidden">
                  <div
                    className="bg-gradient-to-r from-teal-500 to-amber-400 h-full transition-all duration-300"
                    style={{ width: `${((progressStep + 1) / PROGRESS_MESSAGES.length) * 100}%` }}
                  ></div>
                </div>
              </div>
            ) : (
              <button
                type="submit"
                className="w-full py-4 rounded-2xl bg-gradient-to-r from-teal-500 via-cyan-400 to-emerald-400 text-slate-950 font-black text-base shadow-xl shadow-teal-500/20 hover:opacity-95 transition-all transform hover:-translate-y-0.5 flex items-center justify-center gap-2 cursor-pointer"
              >
                <Sparkles className="w-5 h-5 text-slate-950" />
                <span>Synthesize Optimal Itinerary (NSGA-II Engine)</span>
              </button>
            )}
          </div>
        </form>
      </div>
    </div>
  );
};
