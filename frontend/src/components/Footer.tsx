import React from 'react';
import { ShieldCheck, Info, Heart, Compass, Cpu, Database } from 'lucide-react';

export const Footer: React.FC = () => {
  return (
    <footer className="border-t border-slate-800/80 bg-[#040810] text-slate-400 py-10 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto space-y-6">
        
        {/* Synthetic Data Disclaimer Banner */}
        <div className="bg-slate-900/60 border border-slate-800 rounded-2xl p-4 flex flex-col sm:flex-row sm:items-center justify-between gap-3 text-xs">
          <div className="flex items-start sm:items-center space-x-3">
            <span className="p-1.5 rounded-lg bg-amber-500/10 text-amber-400 border border-amber-500/20 shrink-0">
              <Info className="w-4 h-4" />
            </span>
            <p className="text-slate-300">
              <strong className="text-white">Academic Integrity Notice:</strong> All place metrics, user profiles, and rating matrices are generated as a high-fidelity <strong>SYNTHETIC</strong> benchmark (300 places, 1,000 users, 31,408 ratings) designed for reproducible research. Real data can be connected via <code className="text-teal-300 bg-slate-950 px-1 py-0.5 rounded">data/real_data_adapter.py</code>.
            </p>
          </div>
          <div className="shrink-0 flex items-center space-x-2 text-[11px] text-teal-400 font-mono">
            <span>Deterministic Seed: 42</span>
          </div>
        </div>

        {/* Footer Links & Credits */}
        <div className="flex flex-col md:flex-row items-center justify-between gap-4 text-xs pt-4 border-t border-slate-800/50">
          <div className="flex items-center space-x-2">
            <div className="w-6 h-6 rounded-lg bg-teal-500 flex items-center justify-center font-bold text-slate-950 text-xs">
              <Compass className="w-4 h-4 text-slate-950" />
            </div>
            <span className="font-bold text-white tracking-wide">TRAVELMATE AI</span>
            <span className="text-slate-500 hidden sm:inline">| An Intelligent and Personalized Travel Planning System Using Hybrid ML & Multi-Objective Optimization</span>
          </div>

          <div className="flex items-center space-x-6 text-slate-400">
            <span>FastAPI + PyMoo (NSGA-II)</span>
            <span>LightGBM + SVD + SHAP</span>
            <span>React + TypeScript + Tailwind</span>
          </div>

          <p className="text-slate-500 text-center md:text-right">
            Engineered with hybrid ML & multi-objective optimization.
          </p>
        </div>
      </div>
    </footer>
  );
};

