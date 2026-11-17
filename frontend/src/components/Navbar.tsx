import React from 'react';
import { Compass, Sparkles, MapPin, Sliders, BarChart3, Bot, Award, Layers, User } from 'lucide-react';

interface NavbarProps {
  currentView: 'landing' | 'explorer' | 'customize' | 'dashboard' | 'evaluation';
  onNavigate: (view: 'landing' | 'explorer' | 'customize' | 'dashboard' | 'evaluation') => void;
  onOpenCopilot: () => void;
  onOpenProfile?: () => void;
  hasItinerary?: boolean;
}

export const Navbar: React.FC<NavbarProps> = ({ 
  currentView, 
  onNavigate, 
  onOpenCopilot,
  onOpenProfile,
  hasItinerary 
}) => {
  return (
    <header className="sticky top-0 z-40 bg-[#060a12]/95 backdrop-blur-md border-b border-slate-800/80 px-4 sm:px-6 py-3 transition-all">
      <div className="max-w-7xl mx-auto flex items-center justify-between">
        {/* Brand */}
        <div 
          onClick={() => onNavigate('landing')}
          className="flex items-center gap-3 cursor-pointer group"
        >
          <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-teal-500 to-cyan-400 flex items-center justify-center shadow-lg shadow-teal-500/20 group-hover:scale-105 transition-transform">
            <Compass className="w-6 h-6 text-slate-950 stroke-[2.5]" />
          </div>
          <div>
            <div className="flex items-center gap-1.5">
              <span className="font-extrabold text-lg sm:text-xl tracking-tight text-white">TRAVELMATE <span className="text-teal-400">AI</span></span>
            </div>
            <p className="text-[10px] text-slate-400 tracking-wider uppercase font-semibold hidden sm:block">
              Hybrid ML & Multi-Objective Optimization
            </p>
          </div>
        </div>

        {/* Navigation Tabs */}
        <nav className="flex items-center gap-1 bg-slate-900/90 p-1.5 rounded-xl border border-slate-800/80">
          <button
            onClick={() => onNavigate('landing')}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition-all cursor-pointer ${
              currentView === 'landing' 
                ? 'bg-teal-500 text-slate-950 font-bold shadow-md' 
                : 'text-slate-300 hover:text-white hover:bg-slate-800'
            }`}
          >
            <Sparkles className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">Home</span>
          </button>

          <button
            onClick={() => onNavigate('explorer')}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition-all cursor-pointer ${
              currentView === 'explorer' 
                ? 'bg-teal-500 text-slate-950 font-bold shadow-md' 
                : 'text-slate-300 hover:text-white hover:bg-slate-800'
            }`}
          >
            <MapPin className="w-3.5 h-3.5" />
            <span>Destinations</span>
          </button>

          <button
            onClick={() => onNavigate('customize')}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition-all cursor-pointer ${
              currentView === 'customize' 
                ? 'bg-teal-500 text-slate-950 font-bold shadow-md' 
                : 'text-slate-300 hover:text-white hover:bg-slate-800'
            }`}
          >
            <Sliders className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">Planner</span>
          </button>

          <button
            onClick={() => onNavigate('evaluation')}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold transition-all cursor-pointer ${
              currentView === 'evaluation' 
                ? 'bg-teal-500 text-slate-950 font-bold shadow-md' 
                : 'text-slate-300 hover:text-white hover:bg-slate-800'
            }`}
          >
            <Award className="w-3.5 h-3.5" />
            <span>Evaluation</span>
          </button>
        </nav>

        {/* Right CTA */}
        <div className="flex items-center gap-2">
          {onOpenProfile && (
            <button
              onClick={onOpenProfile}
              className="flex items-center gap-1.5 bg-slate-900 hover:bg-slate-800 text-slate-300 hover:text-white border border-slate-700/80 px-3 py-1.5 rounded-xl text-xs font-bold transition shadow-sm cursor-pointer"
            >
              <User className="w-3.5 h-3.5 text-teal-400" />
              <span className="hidden sm:inline">Profile</span>
            </button>
          )}

          <button
            onClick={onOpenCopilot}
            className="flex items-center gap-1.5 bg-slate-900 hover:bg-slate-800 text-teal-400 border border-teal-500/30 px-3 py-1.5 rounded-xl text-xs font-bold transition shadow-sm cursor-pointer"
          >
            <Bot className="w-4 h-4 text-teal-400" />
            <span className="hidden sm:inline">AI Copilot</span>
          </button>
        </div>
      </div>
    </header>
  );
};
