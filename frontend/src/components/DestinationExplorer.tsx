import React, { useState, useEffect, useMemo, useCallback, useRef } from 'react';
import {
  Search, MapPin, Calendar, IndianRupee, Clock, ArrowRight,
  Filter, SortAsc, SortDesc, ChevronDown, X, Loader2, Eye
} from 'lucide-react';
import { Destination, StateItem, CategoryItem } from '../types';
import { api } from '../services/api';
import { DestinationDetailModal } from './DestinationDetailModal';

interface DestinationExplorerProps {
  destinations?: Destination[];
  onSelectDestination: (dest: Destination) => void;
}

const FALLBACK_IMAGE = 'https://images.unsplash.com/photo-1524492412937-b28074a5d7da?w=800&q=70';

const CATEGORY_BADGE: Record<string, string> = {
  Heritage: 'bg-amber-500/20 text-amber-300 border-amber-500/30',
  'Hill Station': 'bg-green-500/20 text-green-300 border-green-500/30',
  Beach: 'bg-blue-500/20 text-blue-300 border-blue-500/30',
  Wildlife: 'bg-orange-500/20 text-orange-300 border-orange-500/30',
  Spiritual: 'bg-purple-500/20 text-purple-300 border-purple-500/30',
  Adventure: 'bg-red-500/20 text-red-300 border-red-500/30',
  Nature: 'bg-emerald-500/20 text-emerald-300 border-emerald-500/30',
  Urban: 'bg-slate-500/20 text-slate-300 border-slate-500/30',
  Island: 'bg-cyan-500/20 text-cyan-300 border-cyan-500/30',
  Desert: 'bg-yellow-500/20 text-yellow-300 border-yellow-500/30',
};

function getCategoryBadgeStyle(category: string): string {
  for (const [key, style] of Object.entries(CATEGORY_BADGE)) {
    if (category.toLowerCase().includes(key.toLowerCase())) return style;
  }
  return 'bg-teal-500/20 text-teal-300 border-teal-500/30';
}

const SORT_OPTIONS = [
  { value: 'name_asc', label: 'A → Z' },
  { value: 'name_desc', label: 'Z → A' },
  { value: 'budget_asc', label: 'Budget: Low → High' },
  { value: 'budget_desc', label: 'Budget: High → Low' },
  { value: 'duration_asc', label: 'Duration: Short First' },
  { value: 'duration_desc', label: 'Duration: Long First' },
];

const PAGE_SIZE = 24;

// Individual destination card
const DestinationCard: React.FC<{
  dest: Destination;
  onView: (d: Destination) => void;
  onSelect: (d: Destination) => void;
}> = ({ dest, onView, onSelect }) => {
  const [imgError, setImgError] = useState(false);
  const imageUrl = imgError || !dest.image_url ? FALLBACK_IMAGE : dest.image_url;
  const category = dest.destination_category || 'General';

  return (
    <div className="group bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden hover:border-teal-500/40 transition-all duration-300 hover:shadow-lg hover:shadow-teal-500/10 flex flex-col">
      {/* Image */}
      <div className="relative h-48 overflow-hidden">
        <img
          src={imageUrl}
          alt={dest.name}
          loading="lazy"
          onError={() => setImgError(true)}
          className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105"
        />
        <div className="absolute inset-0 bg-gradient-to-t from-slate-900/90 via-slate-900/20 to-transparent" />

        {/* Category badge */}
        <div className="absolute top-3 left-3">
          <span className={`text-xs px-2.5 py-1 rounded-full border font-medium ${getCategoryBadgeStyle(category)}`}>
            {category}
          </span>
        </div>

        {/* Photographer tag */}
        {dest.photographer_name && !imgError && (
          <div className="absolute bottom-2 right-2">
            <span className="text-xs text-slate-400 bg-black/50 px-1.5 py-0.5 rounded">
              © {dest.photographer_name}
            </span>
          </div>
        )}
      </div>

      {/* Content */}
      <div className="p-4 flex flex-col flex-1">
        <div className="flex items-start justify-between mb-1">
          <h3 className="text-base font-bold text-white leading-tight">{dest.name}</h3>
        </div>

        <div className="flex items-center gap-1.5 text-teal-400 text-xs mb-2">
          <MapPin className="w-3 h-3 flex-shrink-0" />
          <span>{dest.state}</span>
          {dest.is_union_territory && (
            <span className="text-xs px-1 rounded bg-teal-500/10 text-teal-400 border border-teal-500/20">UT</span>
          )}
        </div>

        <p className="text-slate-400 text-xs leading-relaxed mb-3 line-clamp-2 flex-1">
          {dest.overview || dest.description || 'A beautiful Indian destination.'}
        </p>

        {/* Stats row */}
        <div className="flex items-center gap-3 text-xs text-slate-500 mb-4">
          <span className="flex items-center gap-1">
            <IndianRupee className="w-3 h-3" />
            ₹{(dest.approx_daily_budget_inr || 3500).toLocaleString('en-IN')}/day
          </span>
          <span className="flex items-center gap-1">
            <Clock className="w-3 h-3" />
            {dest.recommended_duration_days || 3}d
          </span>
          {(dest.best_visiting_season || dest.best_season) && (
            <span className="flex items-center gap-1 truncate">
              <Calendar className="w-3 h-3 flex-shrink-0" />
              <span className="truncate">{(dest.best_visiting_season || dest.best_season)?.split(' ').slice(0, 3).join(' ')}</span>
            </span>
          )}
        </div>

        {/* Action buttons */}
        <div className="flex gap-2">
          <button
            onClick={() => onView(dest)}
            className="flex-1 flex items-center justify-center gap-1.5 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-medium transition border border-slate-700 hover:border-slate-600"
          >
            <Eye className="w-3.5 h-3.5" />
            View Details
          </button>
          <button
            onClick={() => onSelect(dest)}
            className="flex-1 flex items-center justify-center gap-1.5 py-2 rounded-lg bg-teal-500/10 hover:bg-teal-500/20 text-teal-400 text-xs font-medium transition border border-teal-500/20 hover:border-teal-500/40"
          >
            Plan Trip
            <ArrowRight className="w-3.5 h-3.5" />
          </button>
        </div>
      </div>
    </div>
  );
};

export const DestinationExplorer: React.FC<DestinationExplorerProps> = ({
  destinations: propDestinations,
  onSelectDestination
}) => {
  const [allDestinations, setAllDestinations] = useState<Destination[]>(propDestinations || []);
  const [states, setStates] = useState<StateItem[]>([]);
  const [categories, setCategories] = useState<CategoryItem[]>([]);
  const [loading, setLoading] = useState(!propDestinations || propDestinations.length === 0);

  // Filter state
  const [query, setQuery] = useState('');
  const [selectedState, setSelectedState] = useState('all');
  const [selectedCategory, setSelectedCategory] = useState('all');
  const [sortBy, setSortBy] = useState('name_asc');
  const [page, setPage] = useState(1);
  const [showStateDropdown, setShowStateDropdown] = useState(false);
  const [showSortDropdown, setShowSortDropdown] = useState(false);

  // Modal
  const [modalDest, setModalDest] = useState<Destination | null>(null);

  const stateDropdownRef = useRef<HTMLDivElement>(null);
  const sortDropdownRef = useRef<HTMLDivElement>(null);

  // Load data
  useEffect(() => {
    if (!propDestinations || propDestinations.length === 0) {
      setLoading(true);
      Promise.all([
        api.getDestinations('', '', '', 'name_asc'),
        api.getDestinationStates(),
        api.getDestinationCategories()
      ]).then(([dests, sts, cats]) => {
        setAllDestinations(dests);
        setStates(sts);
        setCategories(cats);
        setLoading(false);
      }).catch(() => setLoading(false));
    } else {
      // Build states/categories from prop data
      const stateMap: Record<string, number> = {};
      const catMap: Record<string, number> = {};
      propDestinations.forEach(d => {
        stateMap[d.state] = (stateMap[d.state] || 0) + 1;
        const cat = d.destination_category || 'General';
        catMap[cat] = (catMap[cat] || 0) + 1;
      });
      setStates(Object.entries(stateMap).sort().map(([s, c]) => ({ state: s, is_union_territory: false, destination_count: c })));
      setCategories(Object.entries(catMap).sort((a, b) => b[1] - a[1]).map(([c, n]) => ({ category: c, destination_count: n })));
    }
  }, [propDestinations]);

  // Close dropdowns on outside click
  useEffect(() => {
    const handler = (e: MouseEvent) => {
      if (stateDropdownRef.current && !stateDropdownRef.current.contains(e.target as Node)) {
        setShowStateDropdown(false);
      }
      if (sortDropdownRef.current && !sortDropdownRef.current.contains(e.target as Node)) {
        setShowSortDropdown(false);
      }
    };
    document.addEventListener('mousedown', handler);
    return () => document.removeEventListener('mousedown', handler);
  }, []);

  // Reset page on filter change
  useEffect(() => { setPage(1); }, [query, selectedState, selectedCategory, sortBy]);

  // Client-side filter + sort
  const filtered = useMemo(() => {
    const qn = query.toLowerCase();
    let result = allDestinations.filter(d => {
      if (qn) {
        const inName = d.name.toLowerCase().includes(qn);
        const inState = d.state.toLowerCase().includes(qn);
        const inOverview = (d.overview || '').toLowerCase().includes(qn);
        const inAttr = (d.popular_attractions || []).some(a => a.toLowerCase().includes(qn));
        const inCat = (d.destination_category || '').toLowerCase().includes(qn);
        if (!inName && !inState && !inOverview && !inAttr && !inCat) return false;
      }
      if (selectedState !== 'all' && d.state !== selectedState) return false;
      if (selectedCategory !== 'all') {
        const dc = (d.destination_category || '').toLowerCase();
        if (!dc.includes(selectedCategory.toLowerCase())) return false;
      }
      return true;
    });

    switch (sortBy) {
      case 'name_asc': result.sort((a, b) => a.name.localeCompare(b.name)); break;
      case 'name_desc': result.sort((a, b) => b.name.localeCompare(a.name)); break;
      case 'budget_asc': result.sort((a, b) => (a.approx_daily_budget_inr || 0) - (b.approx_daily_budget_inr || 0)); break;
      case 'budget_desc': result.sort((a, b) => (b.approx_daily_budget_inr || 0) - (a.approx_daily_budget_inr || 0)); break;
      case 'duration_asc': result.sort((a, b) => (a.recommended_duration_days || 0) - (b.recommended_duration_days || 0)); break;
      case 'duration_desc': result.sort((a, b) => (b.recommended_duration_days || 0) - (a.recommended_duration_days || 0)); break;
    }
    return result;
  }, [allDestinations, query, selectedState, selectedCategory, sortBy]);

  const totalPages = Math.ceil(filtered.length / PAGE_SIZE);
  const paginated = filtered.slice((page - 1) * PAGE_SIZE, page * PAGE_SIZE);

  const clearFilters = () => {
    setQuery('');
    setSelectedState('all');
    setSelectedCategory('all');
    setSortBy('name_asc');
  };

  const hasFilters = query || selectedState !== 'all' || selectedCategory !== 'all';
  const selectedStateName = selectedState === 'all' ? 'All States & UTs' : selectedState;
  const selectedSortLabel = SORT_OPTIONS.find(s => s.value === sortBy)?.label || 'A → Z';

  return (
    <div className="space-y-6 py-8 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto">
      {/* Header */}
      <div className="space-y-1">
        <h1 className="text-3xl font-extrabold text-white">Destination Explorer</h1>
        <p className="text-slate-400 text-sm">
          Discover <span className="text-teal-400 font-semibold">{allDestinations.length}</span> verified Indian destinations across all 28 states and 8 Union Territories.
        </p>
      </div>

      {/* Search + Filters Bar */}
      <div className="space-y-3">
        {/* Search input */}
        <div className="relative">
          <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400 pointer-events-none" />
          <input
            type="text"
            value={query}
            onChange={e => setQuery(e.target.value)}
            placeholder="Search destinations, states, attractions..."
            className="w-full bg-slate-900 border border-slate-700 rounded-xl pl-11 pr-10 py-3 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-teal-500 transition"
          />
          {query && (
            <button onClick={() => setQuery('')} className="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-white">
              <X className="w-4 h-4" />
            </button>
          )}
        </div>

        {/* Filter row */}
        <div className="flex flex-wrap gap-2 items-center">
          {/* State dropdown */}
          <div className="relative" ref={stateDropdownRef}>
            <button
              onClick={() => { setShowStateDropdown(v => !v); setShowSortDropdown(false); }}
              className={`flex items-center gap-2 px-4 py-2 rounded-xl text-sm border transition ${
                selectedState !== 'all'
                  ? 'bg-teal-500/10 border-teal-500/40 text-teal-300'
                  : 'bg-slate-900 border-slate-700 text-slate-300 hover:border-slate-600'
              }`}
            >
              <MapPin className="w-3.5 h-3.5" />
              <span className="max-w-[140px] truncate">{selectedStateName}</span>
              <ChevronDown className={`w-3.5 h-3.5 transition-transform ${showStateDropdown ? 'rotate-180' : ''}`} />
            </button>
            {showStateDropdown && (
              <div className="absolute top-full left-0 mt-1 z-30 bg-slate-900 border border-slate-700 rounded-xl shadow-xl max-h-72 overflow-y-auto min-w-[220px]">
                <button
                  onClick={() => { setSelectedState('all'); setShowStateDropdown(false); }}
                  className={`w-full text-left px-4 py-2.5 text-sm flex items-center justify-between hover:bg-slate-800 transition ${selectedState === 'all' ? 'text-teal-400' : 'text-slate-300'}`}
                >
                  All States & UTs
                  <span className="text-xs text-slate-500">{allDestinations.length}</span>
                </button>
                <div className="border-t border-slate-800 my-1" />
                {states.map(s => (
                  <button
                    key={s.state}
                    onClick={() => { setSelectedState(s.state); setShowStateDropdown(false); }}
                    className={`w-full text-left px-4 py-2 text-sm flex items-center justify-between hover:bg-slate-800 transition ${selectedState === s.state ? 'text-teal-400' : 'text-slate-300'}`}
                  >
                    <span className="flex items-center gap-2">
                      {s.state}
                      {s.is_union_territory && <span className="text-xs text-teal-500/70">UT</span>}
                    </span>
                    <span className="text-xs text-slate-500">{s.destination_count}</span>
                  </button>
                ))}
              </div>
            )}
          </div>

          {/* Category filter pills */}
          <div className="flex flex-wrap gap-1.5">
            <button
              onClick={() => setSelectedCategory('all')}
              className={`px-3 py-1.5 rounded-full text-xs font-medium border transition ${
                selectedCategory === 'all'
                  ? 'bg-teal-500/20 border-teal-500/40 text-teal-300'
                  : 'bg-slate-900 border-slate-700 text-slate-400 hover:border-slate-600'
              }`}
            >
              All
            </button>
            {categories.slice(0, 8).map(c => (
              <button
                key={c.category}
                onClick={() => setSelectedCategory(selectedCategory === c.category ? 'all' : c.category)}
                className={`px-3 py-1.5 rounded-full text-xs font-medium border transition ${
                  selectedCategory === c.category
                    ? getCategoryBadgeStyle(c.category)
                    : 'bg-slate-900 border-slate-700 text-slate-400 hover:border-slate-600'
                }`}
              >
                {c.category} <span className="opacity-60">({c.destination_count})</span>
              </button>
            ))}
          </div>

          {/* Sort */}
          <div className="relative ml-auto" ref={sortDropdownRef}>
            <button
              onClick={() => { setShowSortDropdown(v => !v); setShowStateDropdown(false); }}
              className="flex items-center gap-2 px-4 py-2 rounded-xl text-sm bg-slate-900 border border-slate-700 text-slate-300 hover:border-slate-600 transition"
            >
              <SortAsc className="w-3.5 h-3.5" />
              {selectedSortLabel}
              <ChevronDown className={`w-3.5 h-3.5 transition-transform ${showSortDropdown ? 'rotate-180' : ''}`} />
            </button>
            {showSortDropdown && (
              <div className="absolute top-full right-0 mt-1 z-30 bg-slate-900 border border-slate-700 rounded-xl shadow-xl min-w-[200px]">
                {SORT_OPTIONS.map(opt => (
                  <button
                    key={opt.value}
                    onClick={() => { setSortBy(opt.value); setShowSortDropdown(false); }}
                    className={`w-full text-left px-4 py-2.5 text-sm hover:bg-slate-800 transition ${sortBy === opt.value ? 'text-teal-400' : 'text-slate-300'}`}
                  >
                    {opt.label}
                  </button>
                ))}
              </div>
            )}
          </div>

          {/* Clear filters */}
          {hasFilters && (
            <button
              onClick={clearFilters}
              className="flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs text-red-400 border border-red-500/20 hover:bg-red-500/10 transition"
            >
              <X className="w-3.5 h-3.5" />
              Clear
            </button>
          )}
        </div>
      </div>

      {/* Results summary */}
      <div className="flex items-center justify-between text-xs text-slate-500">
        <span>
          Showing <span className="text-slate-300 font-medium">{paginated.length}</span> of <span className="text-slate-300 font-medium">{filtered.length}</span> destinations
          {selectedState !== 'all' && <> in <span className="text-teal-400">{selectedState}</span></>}
          {selectedCategory !== 'all' && <> · Category: <span className="text-teal-400">{selectedCategory}</span></>}
        </span>
      </div>

      {/* Loading */}
      {loading && (
        <div className="flex flex-col items-center justify-center py-20">
          <Loader2 className="w-8 h-8 text-teal-400 animate-spin mb-3" />
          <p className="text-slate-400 text-sm">Loading destinations across India...</p>
        </div>
      )}

      {/* Grid */}
      {!loading && paginated.length > 0 && (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-5">
          {paginated.map(dest => (
            <DestinationCard
              key={dest.id || dest.destination_id || dest.name}
              dest={dest}
              onView={setModalDest}
              onSelect={onSelectDestination}
            />
          ))}
        </div>
      )}

      {/* Empty state */}
      {!loading && paginated.length === 0 && (
        <div className="text-center py-20">
          <div className="text-5xl mb-4">🗺️</div>
          <h3 className="text-lg font-bold text-slate-300 mb-2">No destinations found</h3>
          <p className="text-slate-500 text-sm mb-4">Try a different search term or clear your filters.</p>
          <button onClick={clearFilters} className="px-4 py-2 rounded-lg bg-teal-500/10 border border-teal-500/20 text-teal-400 text-sm hover:bg-teal-500/20 transition">
            Clear Filters
          </button>
        </div>
      )}

      {/* Pagination */}
      {!loading && totalPages > 1 && (
        <div className="flex items-center justify-center gap-2 pt-4">
          <button
            onClick={() => setPage(p => Math.max(1, p - 1))}
            disabled={page === 1}
            className="px-4 py-2 rounded-lg text-sm bg-slate-900 border border-slate-700 text-slate-300 disabled:opacity-40 hover:border-slate-600 transition"
          >
            Previous
          </button>
          <div className="flex gap-1">
            {Array.from({ length: Math.min(5, totalPages) }, (_, i) => {
              const p = page <= 3 ? i + 1 : page - 2 + i;
              if (p < 1 || p > totalPages) return null;
              return (
                <button
                  key={p}
                  onClick={() => setPage(p)}
                  className={`w-9 h-9 rounded-lg text-sm transition ${
                    p === page
                      ? 'bg-teal-500 text-black font-bold'
                      : 'bg-slate-900 border border-slate-700 text-slate-300 hover:border-slate-600'
                  }`}
                >
                  {p}
                </button>
              );
            })}
          </div>
          <button
            onClick={() => setPage(p => Math.min(totalPages, p + 1))}
            disabled={page === totalPages}
            className="px-4 py-2 rounded-lg text-sm bg-slate-900 border border-slate-700 text-slate-300 disabled:opacity-40 hover:border-slate-600 transition"
          >
            Next
          </button>
        </div>
      )}

      {/* Detail Modal */}
      {modalDest && (
        <DestinationDetailModal
          destination={modalDest}
          onClose={() => setModalDest(null)}
          onSelectDestination={onSelectDestination}
        />
      )}
    </div>
  );
};
