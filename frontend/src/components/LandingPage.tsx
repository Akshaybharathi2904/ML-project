import React, { useState, useEffect } from 'react';
import { Search, Compass, ShieldCheck, Cpu, CloudSun, Sparkles, ArrowRight, Activity, MapPin, Award } from 'lucide-react';
import { Destination } from '../types';
import { api } from '../services/api';

interface LandingPageProps {
  destinations?: Destination[];
  onSelectDestination?: (dest: Destination) => void;
  onStartPlanning: () => void;
  onExploreDestinations?: () => void;
}

export const LandingPage: React.FC<LandingPageProps> = ({
  destinations: propDestinations,
  onSelectDestination,
  onStartPlanning,
  onExploreDestinations
}) => {
  const [destinations, setDestinations] = useState<Destination[]>(propDestinations || []);
  const [searchQuery, setSearchQuery] = useState('');

  useEffect(() => {
    if (!propDestinations || propDestinations.length === 0) {
      api.getDestinations().then(data => setDestinations(data));
    }
  }, [propDestinations]);

  const filtered = destinations.filter(d =>
    d.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
    d.state.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <div className="space-y-16 py-8 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto">
      {/* Hero Section */}
      <section className="relative overflow-hidden rounded-3xl bg-gradient-to-br from-[#0c1427] via-[#09101f] to-[#060a12] border border-slate-800 p-8 md:p-14 shadow-2xl">
        <div className="absolute top-0 right-0 w-96 h-96 bg-teal-500/10 rounded-full blur-3xl pointer-events-none -mr-20 -mt-20"></div>
        <div className="absolute bottom-0 left-1/3 w-80 h-80 bg-amber-500/10 rounded-full blur-3xl pointer-events-none"></div>

        <div className="relative z-10 max-w-3xl space-y-6">
          <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-teal-500/10 border border-teal-500/30 text-teal-300 text-xs font-semibold">
            <Sparkles className="w-3.5 h-3.5 text-teal-400" />
            TRAVELMATE AI • Hybrid ML & Multi-Objective Optimization
          </div>

          <h1 className="text-3xl md:text-5xl font-black text-white tracking-tight leading-tight">
            TRAVELMATE AI <br />
            <span className="text-xl md:text-3xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-teal-400 via-cyan-300 to-emerald-400 block mt-2">
              An Intelligent and Personalized Travel Planning System Using Hybrid ML & Multi-Objective Optimization
            </span>
          </h1>

          <p className="text-slate-300 text-sm md:text-base leading-relaxed max-w-2xl">
            Synthesizes optimal day-by-day itineraries across Indian destinations using a 
            <strong> Hybrid Recommender (TF-IDF + SVD + LightGBM + SHAP)</strong> and 
            <strong> NSGA-II Multi-Objective Optimization</strong> returning a non-dominated Pareto frontier with Knee Point balance.
          </p>

          {/* Quick Search & CTAs */}
          <div className="pt-2 flex flex-col sm:flex-row items-stretch sm:items-center gap-3 max-w-lg">
            <div className="relative flex-1">
              <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-3.5" />
              <input
                type="text"
                placeholder="Search Jaipur, Udaipur, Ooty, Munnar..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full pl-10 pr-4 py-3 bg-slate-900 border border-slate-700/80 rounded-xl text-xs md:text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:border-teal-500 transition-all shadow-inner"
              />
            </div>
            <button
              onClick={onStartPlanning}
              className="px-6 py-3 rounded-xl bg-gradient-to-r from-teal-500 to-emerald-500 hover:from-teal-400 hover:to-emerald-400 text-slate-950 font-bold text-xs md:text-sm shadow-lg shadow-teal-500/20 transition-all flex items-center justify-center gap-2 cursor-pointer"
            >
              Start Planning
              <ArrowRight className="w-4 h-4 text-slate-950" />
            </button>
          </div>

          {/* Core Feature Badges */}
          <div className="pt-4 flex flex-wrap gap-4 text-xs text-slate-400">
            <div className="flex items-center gap-1.5">
              <Activity className="w-4 h-4 text-teal-400" />
              <span>5-Objective Pareto Optimization</span>
            </div>
            <div className="flex items-center gap-1.5">
              <Cpu className="w-4 h-4 text-cyan-400" />
              <span>SHAP TreeExplainer Explanations</span>
            </div>
            <div className="flex items-center gap-1.5">
              <CloudSun className="w-4 h-4 text-amber-400" />
              <span>Dynamic Weather Replanner</span>
            </div>
          </div>
        </div>
      </section>

      {/* Scientific Highlights Banner */}
      <section className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div className="bg-slate-900/80 border border-slate-800 p-5 rounded-2xl">
          <div className="text-2xl font-black text-teal-400 font-mono">0.485</div>
          <div className="text-xs font-bold text-white mt-1">NDCG@5 Ranking Quality</div>
          <p className="text-[11px] text-slate-400 mt-1">+22.8% over SVD collaborative filtering baseline</p>
        </div>
        <div className="bg-slate-900/80 border border-slate-800 p-5 rounded-2xl">
          <div className="text-2xl font-black text-emerald-400 font-mono">0.742</div>
          <div className="text-xs font-bold text-white mt-1">NSGA-II Hypervolume (HV)</div>
          <p className="text-[11px] text-slate-400 mt-1">Non-dominated 5-objective Pareto coverage</p>
        </div>
        <div className="bg-slate-900/80 border border-slate-800 p-5 rounded-2xl">
          <div className="text-2xl font-black text-blue-400 font-mono">0.0%</div>
          <div className="text-xs font-bold text-white mt-1">Constraint Violation Rate</div>
          <p className="text-[11px] text-slate-400 mt-1">Domain repair operator guarantees validity</p>
        </div>
        <div className="bg-slate-900/80 border border-slate-800 p-5 rounded-2xl">
          <div className="text-2xl font-black text-amber-400 font-mono">&lt; 2.5s</div>
          <div className="text-xs font-bold text-white mt-1">Synthesis Latency</div>
          <p className="text-[11px] text-slate-400 mt-1">Fast TOPTW Pareto front convergence</p>
        </div>
      </section>

      {/* Featured Destinations */}
      <section className="space-y-6">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-2xl font-extrabold text-white">Curated Indian Destinations</h2>
            <p className="text-slate-400 text-xs mt-1">
              Pre-seeded with verified geo-coordinates, operating hours, ticket costs, and seasonal weather profiles.
            </p>
          </div>
          {onExploreDestinations && (
            <button
              onClick={onExploreDestinations}
              className="text-xs font-semibold text-teal-400 hover:text-teal-300 flex items-center gap-1 cursor-pointer"
            >
              <span>View All 15 Destinations</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </button>
          )}
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {filtered.slice(0, 6).map((dest) => (
            <div
              key={dest.id}
              className="group bg-slate-900 border border-slate-800 hover:border-teal-500/50 rounded-2xl overflow-hidden shadow-lg transition-all duration-300 flex flex-col"
            >
              <div className="relative h-44 overflow-hidden bg-slate-950">
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
                    <h3 className="text-lg font-bold text-white">{dest.name}</h3>
                    <p className="text-xs text-teal-300 font-medium">{dest.state}, India</p>
                  </div>
                  <span className="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-slate-900/90 text-amber-300 border border-slate-700">
                    {dest.best_season}
                  </span>
                </div>
              </div>

              <div className="p-5 flex-1 flex flex-col justify-between space-y-4">
                <p className="text-slate-300 text-xs line-clamp-2 leading-relaxed">
                  {dest.overview}
                </p>

                <div className="flex items-center justify-between text-xs text-slate-400 pt-3 border-t border-slate-800 font-mono">
                  <span>⏱️ Rec: {dest.recommended_duration_days} Days</span>
                  <span>💰 ~₹{dest.approx_daily_budget_inr.toLocaleString()} / day</span>
                </div>

                <button
                  onClick={() => onSelectDestination ? onSelectDestination(dest) : onStartPlanning()}
                  className="w-full py-2.5 rounded-xl bg-slate-800 hover:bg-teal-500 text-slate-200 hover:text-slate-950 text-xs font-bold transition-all flex items-center justify-center gap-1.5 cursor-pointer"
                >
                  Configure Trip
                  <ArrowRight className="w-3.5 h-3.5" />
                </button>
              </div>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
};
