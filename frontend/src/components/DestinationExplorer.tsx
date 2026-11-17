import React, { useState, useEffect } from 'react';
import { Search, MapPin, Calendar, IndianRupee, Clock, ArrowRight } from 'lucide-react';
import { Destination } from '../types';
import { api } from '../services/api';

interface DestinationExplorerProps {
  destinations?: Destination[];
  onSelectDestination: (dest: Destination) => void;
}

export const DestinationExplorer: React.FC<DestinationExplorerProps> = ({
  destinations: propDestinations,
  onSelectDestination
}) => {
  const [destinations, setDestinations] = useState<Destination[]>(propDestinations || []);
  const [query, setQuery] = useState('');
  const [selectedState, setSelectedState] = useState<string>('all');
  const [loading, setLoading] = useState<boolean>(!propDestinations || propDestinations.length === 0);

  useEffect(() => {
    if (!propDestinations || propDestinations.length === 0) {
      setLoading(true);
      api.getDestinations().then(data => {
        setDestinations(data);
        setLoading(false);
      }).catch(err => {
        console.error(err);
        setLoading(false);
      });
    }
  }, [propDestinations]);

  const states = ['all', ...Array.from(new Set(destinations.map(d => d.state)))];

  const filtered = destinations.filter(d => {
    const matchesQuery = d.name.toLowerCase().includes(query.toLowerCase()) ||
                         d.state.toLowerCase().includes(query.toLowerCase()) ||
                         d.overview.toLowerCase().includes(query.toLowerCase());
    const matchesState = selectedState === 'all' || d.state === selectedState;
    return matchesQuery && matchesState;
  });

  return (
    <div className="space-y-8 py-8 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto">
      {/* Header */}
      <div className="space-y-2">
        <h1 className="text-3xl font-extrabold text-white">Destination Explorer</h1>
        <p className="text-slate-400 text-sm">
          Discover curated Indian destinations with live weather tracking, verified attractions, and estimated budget ranges.
        </p>
      </div>

      {/* Filter and Search Bar */}
      <div className="flex flex-col md:flex-row gap-4">
        <div className="relative flex-1">
          <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-3.5" />
          <input
            type="text"
            placeholder="Search by city, state, or keywords..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            className="w-full pl-10 pr-4 py-3 bg-slate-900 border border-slate-800 rounded-xl text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:border-teal-500 transition-all shadow-inner"
          />
        </div>

        {/* State Filter Pills */}
        <div className="flex items-center gap-2 overflow-x-auto pb-2 md:pb-0">
          {states.map(st => (
            <button
              key={st}
              onClick={() => setSelectedState(st)}
              className={`px-3.5 py-2 rounded-xl text-xs font-semibold whitespace-nowrap transition-all capitalize cursor-pointer ${
                selectedState === st
                  ? 'bg-teal-500 text-slate-950 font-bold shadow-lg shadow-teal-500/20'
                  : 'bg-slate-900 border border-slate-800 text-slate-400 hover:text-slate-200'
              }`}
            >
              {st}
            </button>
          ))}
        </div>
      </div>

      {/* Grid of Destinations */}
      {loading ? (
        <div className="py-20 text-center text-slate-400 text-sm animate-pulse">
          Loading curated Indian destinations...
        </div>
      ) : filtered.length === 0 ? (
        <div className="py-20 text-center text-slate-500 text-sm">
          No destinations found matching your criteria. Try another search.
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filtered.map(dest => (
            <div
              key={dest.id}
              className="bg-slate-900 border border-slate-800 hover:border-slate-700 rounded-2xl overflow-hidden shadow-lg flex flex-col justify-between transition-all group"
            >
              <div>
                <div className="relative h-48 overflow-hidden bg-slate-950">
                  <img
                    src={dest.image_url || 'https://images.unsplash.com/photo-1599661046289-e31897846e41?w=800'}
                    alt={dest.name}
                    className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
                    onError={(e: any) => {
                      e.target.src = 'https://images.unsplash.com/photo-1599661046289-e31897846e41?w=800';
                    }}
                  />
                  <div className="absolute inset-0 bg-gradient-to-t from-slate-950 via-slate-950/20 to-transparent"></div>
                  <div className="absolute bottom-3 left-4 right-4 flex items-center justify-between">
                    <div>
                      <h3 className="text-xl font-black text-white">{dest.name}</h3>
                      <div className="flex items-center gap-1 text-teal-300 text-xs">
                        <MapPin className="w-3.5 h-3.5" />
                        <span>{dest.state}, India</span>
                      </div>
                    </div>
                  </div>
                </div>

                <div className="p-5 space-y-4">
                  <p className="text-slate-300 text-xs leading-relaxed line-clamp-3">
                    {dest.overview}
                  </p>

                  <div className="space-y-1.5 text-xs text-slate-400 pt-2 border-t border-slate-800">
                    <div className="flex items-center gap-1.5">
                      <Calendar className="w-3.5 h-3.5 text-teal-400" />
                      <span>Best Season: <b>{dest.best_season}</b></span>
                    </div>
                    <div className="flex items-center gap-1.5">
                      <Clock className="w-3.5 h-3.5 text-amber-400" />
                      <span>Recommended Duration: <b>{dest.recommended_duration_days} Days</b></span>
                    </div>
                    <div className="flex items-center gap-1.5">
                      <IndianRupee className="w-3.5 h-3.5 text-emerald-400" />
                      <span>Est. Budget: <b>₹{dest.approx_daily_budget_inr.toLocaleString()} / day</b></span>
                    </div>
                  </div>
                </div>
              </div>

              <div className="p-5 pt-0">
                <button
                  onClick={() => onSelectDestination(dest)}
                  className="w-full py-3 rounded-xl bg-teal-500 hover:bg-teal-400 text-slate-950 font-bold text-xs transition-all flex items-center justify-center gap-2 cursor-pointer shadow-md shadow-teal-500/20"
                >
                  <span>Plan Trip to {dest.name}</span>
                  <ArrowRight className="w-4 h-4 text-slate-950" />
                </button>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};
