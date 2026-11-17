import React, { useState } from 'react';
import {
  X, MapPin, Calendar, IndianRupee, Clock, Camera, ExternalLink,
  Navigation, Star, Tag, ChevronRight, Compass, Info
} from 'lucide-react';
import { Destination } from '../types';

interface DestinationDetailModalProps {
  destination: Destination;
  onClose: () => void;
  onSelectDestination: (dest: Destination) => void;
}

const FALLBACK_IMAGE = 'https://images.unsplash.com/photo-1524492412937-b28074a5d7da?w=1200&q=80';

const CATEGORY_COLORS: Record<string, string> = {
  'Heritage': 'bg-amber-500/20 text-amber-300 border-amber-500/30',
  'Hill Station': 'bg-green-500/20 text-green-300 border-green-500/30',
  'Beach': 'bg-blue-500/20 text-blue-300 border-blue-500/30',
  'Wildlife': 'bg-orange-500/20 text-orange-300 border-orange-500/30',
  'Spiritual': 'bg-purple-500/20 text-purple-300 border-purple-500/30',
  'Adventure': 'bg-red-500/20 text-red-300 border-red-500/30',
  'Nature': 'bg-emerald-500/20 text-emerald-300 border-emerald-500/30',
  'Urban': 'bg-slate-500/20 text-slate-300 border-slate-500/30',
  'Island': 'bg-cyan-500/20 text-cyan-300 border-cyan-500/30',
  'Desert': 'bg-yellow-500/20 text-yellow-300 border-yellow-500/30',
};

function getCategoryStyle(category: string): string {
  for (const [key, style] of Object.entries(CATEGORY_COLORS)) {
    if (category.toLowerCase().includes(key.toLowerCase())) return style;
  }
  return 'bg-teal-500/20 text-teal-300 border-teal-500/30';
}

export const DestinationDetailModal: React.FC<DestinationDetailModalProps> = ({
  destination,
  onClose,
  onSelectDestination
}) => {
  const [imgError, setImgError] = useState(false);
  const imageUrl = imgError || !destination.image_url ? FALLBACK_IMAGE : destination.image_url;
  const category = destination.destination_category || 'General';
  const catStyle = getCategoryStyle(category);

  const handlePlanTrip = () => {
    onSelectDestination(destination);
    onClose();
  };

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-sm"
      onClick={(e) => { if (e.target === e.currentTarget) onClose(); }}
    >
      <div className="relative bg-slate-900 border border-slate-700 rounded-2xl max-w-3xl w-full max-h-[90vh] overflow-y-auto shadow-2xl">
        {/* Close Button */}
        <button
          onClick={onClose}
          className="absolute top-4 right-4 z-10 p-2 rounded-full bg-black/50 text-white hover:bg-black/80 transition"
        >
          <X className="w-5 h-5" />
        </button>

        {/* Hero Image */}
        <div className="relative h-72 overflow-hidden rounded-t-2xl">
          <img
            src={imageUrl}
            alt={destination.name}
            onError={() => setImgError(true)}
            className="w-full h-full object-cover"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-slate-900 via-slate-900/40 to-transparent" />

          {/* Photographer Attribution */}
          {destination.photographer_name && !imgError && (
            <div className="absolute bottom-3 right-3">
              <a
                href={destination.photographer_profile_url || '#'}
                target="_blank"
                rel="noopener noreferrer"
                className="flex items-center gap-1.5 px-2 py-1 rounded-full bg-black/60 text-xs text-slate-300 hover:text-white transition"
              >
                <Camera className="w-3 h-3" />
                <span>{destination.photographer_name}</span>
                {destination.image_source && (
                  <span className="text-slate-400">/ {destination.image_source}</span>
                )}
              </a>
            </div>
          )}

          {/* Title overlay */}
          <div className="absolute bottom-0 left-0 right-0 p-6">
            <div className="flex items-start justify-between">
              <div>
                <h2 className="text-3xl font-extrabold text-white mb-1">{destination.name}</h2>
                <div className="flex items-center gap-2 text-slate-300">
                  <MapPin className="w-4 h-4 text-teal-400 flex-shrink-0" />
                  <span className="text-sm">{destination.state}</span>
                  {destination.is_union_territory && (
                    <span className="text-xs px-1.5 py-0.5 rounded bg-teal-500/20 text-teal-300 border border-teal-500/30">UT</span>
                  )}
                </div>
              </div>
              <span className={`text-xs px-3 py-1 rounded-full border font-medium ${catStyle}`}>
                {category}
              </span>
            </div>
          </div>
        </div>

        {/* Content */}
        <div className="p-6 space-y-6">
          {/* Overview */}
          <div>
            <div className="flex items-center gap-2 mb-2">
              <Info className="w-4 h-4 text-teal-400" />
              <h3 className="text-sm font-bold text-slate-300 uppercase tracking-wider">Overview</h3>
            </div>
            <p className="text-slate-300 text-sm leading-relaxed">
              {destination.overview || destination.description || 'A beautiful destination in India.'}
            </p>
          </div>

          {/* Quick Stats */}
          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
            <div className="bg-slate-800/60 border border-slate-700 rounded-xl p-3 text-center">
              <Calendar className="w-5 h-5 text-teal-400 mx-auto mb-1" />
              <p className="text-xs text-slate-400 mb-0.5">Best Season</p>
              <p className="text-xs font-semibold text-white leading-tight">
                {destination.best_visiting_season || destination.best_season || 'Oct – Mar'}
              </p>
            </div>
            <div className="bg-slate-800/60 border border-slate-700 rounded-xl p-3 text-center">
              <IndianRupee className="w-5 h-5 text-teal-400 mx-auto mb-1" />
              <p className="text-xs text-slate-400 mb-0.5">Daily Budget</p>
              <p className="text-xs font-semibold text-white">
                ₹{destination.approx_daily_budget_inr?.toLocaleString('en-IN') || '—'}
              </p>
            </div>
            <div className="bg-slate-800/60 border border-slate-700 rounded-xl p-3 text-center">
              <Clock className="w-5 h-5 text-teal-400 mx-auto mb-1" />
              <p className="text-xs text-slate-400 mb-0.5">Duration</p>
              <p className="text-xs font-semibold text-white">
                {destination.recommended_duration_days || 3} Days
              </p>
            </div>
            <div className="bg-slate-800/60 border border-slate-700 rounded-xl p-3 text-center">
              <Navigation className="w-5 h-5 text-teal-400 mx-auto mb-1" />
              <p className="text-xs text-slate-400 mb-0.5">Coordinates</p>
              <p className="text-xs font-semibold text-white">
                {destination.lat?.toFixed(2)}°N, {destination.lon?.toFixed(2)}°E
              </p>
            </div>
          </div>

          {/* Popular Attractions */}
          {destination.popular_attractions && destination.popular_attractions.length > 0 && (
            <div>
              <div className="flex items-center gap-2 mb-3">
                <Star className="w-4 h-4 text-teal-400" />
                <h3 className="text-sm font-bold text-slate-300 uppercase tracking-wider">Popular Attractions</h3>
              </div>
              <div className="flex flex-wrap gap-2">
                {destination.popular_attractions.map((attr, i) => (
                  <span key={i} className="text-xs px-3 py-1.5 rounded-full bg-slate-800 border border-slate-700 text-slate-300 hover:border-teal-500/50 transition">
                    {attr}
                  </span>
                ))}
              </div>
            </div>
          )}

          {/* Nearby Places */}
          {destination.nearby_places && destination.nearby_places.length > 0 && (
            <div>
              <div className="flex items-center gap-2 mb-3">
                <MapPin className="w-4 h-4 text-teal-400" />
                <h3 className="text-sm font-bold text-slate-300 uppercase tracking-wider">Nearby Places</h3>
              </div>
              <div className="flex flex-wrap gap-2">
                {destination.nearby_places.map((place, i) => (
                  <span key={i} className="text-xs px-3 py-1.5 rounded-full bg-slate-800/80 border border-slate-700/80 text-slate-400">
                    {place}
                  </span>
                ))}
              </div>
            </div>
          )}

          {/* Recommended Activities */}
          {destination.recommended_activities && destination.recommended_activities.length > 0 && (
            <div>
              <div className="flex items-center gap-2 mb-3">
                <Tag className="w-4 h-4 text-teal-400" />
                <h3 className="text-sm font-bold text-slate-300 uppercase tracking-wider">Recommended Activities</h3>
              </div>
              <div className="flex flex-wrap gap-2">
                {destination.recommended_activities.map((act, i) => (
                  <span key={i} className="text-xs px-3 py-1.5 rounded-full bg-teal-500/10 border border-teal-500/20 text-teal-300">
                    {act}
                  </span>
                ))}
              </div>
            </div>
          )}

          {/* Map Link */}
          <div className="bg-slate-800/40 border border-slate-700/60 rounded-xl p-4 flex items-center justify-between">
            <div className="flex items-center gap-3">
              <Compass className="w-5 h-5 text-teal-400" />
              <div>
                <p className="text-sm font-medium text-white">View on Google Maps</p>
                <p className="text-xs text-slate-400">{destination.lat?.toFixed(4)}°N, {destination.lon?.toFixed(4)}°E</p>
              </div>
            </div>
            <a
              href={`https://maps.google.com/?q=${destination.lat},${destination.lon}`}
              target="_blank"
              rel="noopener noreferrer"
              className="flex items-center gap-1.5 text-xs text-teal-400 hover:text-teal-300 transition"
            >
              Open <ExternalLink className="w-3.5 h-3.5" />
            </a>
          </div>

          {/* Image License Attribution */}
          {destination.image_license && !imgError && (
            <p className="text-xs text-slate-500 text-center">
              Photo license: {destination.image_license}
              {destination.image_source_page && (
                <> · <a href={destination.image_source_page} target="_blank" rel="noopener noreferrer" className="underline hover:text-slate-400">Source</a></>
              )}
            </p>
          )}

          {/* CTA Button */}
          <button
            onClick={handlePlanTrip}
            className="w-full flex items-center justify-center gap-2 py-4 rounded-xl bg-teal-500 hover:bg-teal-400 text-black font-bold text-sm transition-all duration-200 hover:scale-[1.01] shadow-lg shadow-teal-500/20"
          >
            <Compass className="w-5 h-5" />
            Plan Trip with TravelMate AI
            <ChevronRight className="w-5 h-5" />
          </button>
        </div>
      </div>
    </div>
  );
};
