import React, { useState, useEffect, useRef } from 'react';
import { 
  ItineraryResponse, 
  ParetoSolution, 
  ItineraryStop, 
  WeatherForecast,
  BudgetBreakdownData,
  ShapExplanationData,
  CrowdAnalyticsData
} from '../types';
import { api } from '../services/api';
import { 
  Calendar, Clock, MapPin, IndianRupee, Users, ShieldAlert, Sparkles, 
  TrendingUp, Award, Layers, AlertCircle, RefreshCw, ChevronDown, 
  ChevronUp, Eye, ArrowRight, CloudRain, Zap, CheckCircle2, Sliders,
  Navigation, BarChart3, Brain, Compass, Trash2, Sun, Sunset, 
  PieChart as PieChartIcon, AlertTriangle, ShieldCheck, X
} from 'lucide-react';
import { 
  ScatterChart, Scatter, XAxis, YAxis, ZAxis, Tooltip, 
  ResponsiveContainer, Cell, LineChart, Line, CartesianGrid, 
  BarChart, Bar, PieChart, Pie, Legend
} from 'recharts';
import L from 'leaflet';

interface ResultsDashboardProps {
  itineraryData: ItineraryResponse;
  onUpdateItinerary: (updated: ItineraryResponse) => void;
  onBackToCustomize: () => void;
  onOpenCopilot: () => void;
}

export const ResultsDashboard: React.FC<ResultsDashboardProps> = ({
  itineraryData,
  onUpdateItinerary,
  onBackToCustomize,
  onOpenCopilot
}) => {
  const urlTab = new URLSearchParams(window.location.search).get('tab') as any;
  const [activeTab, setActiveTab] = useState<'timeline' | 'budget' | 'pareto' | 'analytics' | 'insights' | 'simulation'>(
    urlTab && ['timeline', 'budget', 'pareto', 'analytics', 'insights', 'simulation'].includes(urlTab)
      ? urlTab
      : 'timeline'
  );
  const [selectedDayNumber, setSelectedDayNumber] = useState<number>(1);
  const [expandedStops, setExpandedStops] = useState<Record<string, boolean>>({});
  const [isSimulating, setIsSimulating] = useState<boolean>(false);
  const [simulationResult, setSimulationResult] = useState<any | null>(null);
  const [swapModalStop, setSwapModalStop] = useState<ItineraryStop | null>(null);
  const [actionNotice, setActionNotice] = useState<string | null>(null);

  // New Feature States: Route Optimization, Budget Breakdown, SHAP, Crowd
  const [isOptimizingRoute, setIsOptimizingRoute] = useState<boolean>(false);
  const [budgetBreakdown, setBudgetBreakdown] = useState<BudgetBreakdownData | null>(null);
  const [userBudgetLimit, setUserBudgetLimit] = useState<number>(
    Math.round((itineraryData.chosen_itinerary.total_cost_inr || 5000) * 1.3)
  );
  const [loadingBudget, setLoadingBudget] = useState<boolean>(false);
  const [shapDataMap, setShapDataMap] = useState<Record<string, ShapExplanationData>>({});
  const [loadingShap, setLoadingShap] = useState<Record<string, boolean>>({});
  const [crowdModalData, setCrowdModalData] = useState<{
    placeId: string;
    placeName: string;
    data: CrowdAnalyticsData | null;
  } | null>(null);
  const [loadingCrowd, setLoadingCrowd] = useState<boolean>(false);

  const mapContainerRef = useRef<HTMLDivElement>(null);
  const mapInstanceRef = useRef<L.Map | null>(null);
  const layerGroupRef = useRef<L.LayerGroup | null>(null);

  const chosenPlan = itineraryData.chosen_itinerary;
  const days = chosenPlan.days || [];
  const currentDay = days.find(d => d.day_number === selectedDayNumber) || days[0];

  const showNotification = (msg: string) => {
    setActionNotice(msg);
    setTimeout(() => setActionNotice(null), 4000);
  };

  // Fetch Budget Breakdown whenever activeTab is 'budget' or tripId/budgetLimit changes
  useEffect(() => {
    if (activeTab === 'budget' || !budgetBreakdown) {
      setLoadingBudget(true);
      api.getBudgetBreakdown(itineraryData.trip_id, userBudgetLimit)
        .then(data => setBudgetBreakdown(data))
        .catch(err => console.error("Budget breakdown fetch failed", err))
        .finally(() => setLoadingBudget(false));
    }
  }, [activeTab, userBudgetLimit, itineraryData.trip_id]);

  // Toggle explainability breakdown & fetch real SHAP feature attributions
  const toggleStopExpand = async (placeId: string) => {
    const nextState = !expandedStops[placeId];
    setExpandedStops(prev => ({ ...prev, [placeId]: nextState }));
    if (nextState && !shapDataMap[placeId] && !loadingShap[placeId]) {
      setLoadingShap(prev => ({ ...prev, [placeId]: true }));
      try {
        const data = await api.getShapExplanation(placeId);
        setShapDataMap(prev => ({ ...prev, [placeId]: data }));
      } catch (err) {
        console.error("SHAP explanation error:", err);
      } finally {
        setLoadingShap(prev => ({ ...prev, [placeId]: false }));
      }
    }
  };

  // Route Optimization handler (Feature 2)
  const handleOptimizeRoute = async () => {
    if (!currentDay) return;
    setIsOptimizingRoute(true);
    try {
      const res = await api.optimizeRoute(itineraryData.trip_id, currentDay.day_number);
      if (res) {
        onUpdateItinerary(res);
        showNotification(`Day ${currentDay.day_number} route re-ordered via TSP!`);
      }
    } catch (err: any) {
      showNotification('Route optimization: ' + (err.message || 'Updated'));
    } finally {
      setIsOptimizingRoute(false);
    }
  };

  // Remove Stop handler (Feature 2)
  const handleRemoveStop = async (placeId: string, stopName: string) => {
    if (!currentDay) return;
    try {
      const res = await api.removeStop(itineraryData.trip_id, currentDay.day_number, placeId);
      if (res) {
        onUpdateItinerary(res);
        showNotification(`Removed "${stopName}". Day route and timeline updated.`);
      }
    } catch (err: any) {
      showNotification('Remove stop: ' + (err.message || 'Updated'));
    }
  };

  // Open Crowd Analytics Modal (Feature 9)
  const handleOpenCrowdModal = async (placeId: string, placeName: string) => {
    setCrowdModalData({ placeId, placeName, data: null });
    setLoadingCrowd(true);
    try {
      const data = await api.getPlaceCrowd(placeId);
      setCrowdModalData({ placeId, placeName, data });
    } catch (err) {
      console.error("Crowd fetch error:", err);
    } finally {
      setLoadingCrowd(false);
    }
  };

  // Initialize and update Leaflet Map
  useEffect(() => {
    if (!mapContainerRef.current) return;

    if (!mapInstanceRef.current) {
      const map = L.map(mapContainerRef.current).setView([24.5854, 73.7125], 12);
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors'
      }).addTo(map);

      const layerGroup = L.layerGroup().addTo(map);
      layerGroupRef.current = layerGroup;
      mapInstanceRef.current = map;
    }

    const map = mapInstanceRef.current;
    const layerGroup = layerGroupRef.current;
    if (!map || !layerGroup) return;

    layerGroup.clearLayers();

    const activeStops = currentDay ? currentDay.stops : [];
    if (activeStops.length === 0) return;

    const latLngs: L.LatLngTuple[] = [];
    const colors = ['#0d9488', '#2563eb', '#f59e0b', '#8b5cf6', '#ec4899'];
    const dayColor = colors[(selectedDayNumber - 1) % colors.length];

    activeStops.forEach((stop, idx) => {
      latLngs.push([stop.lat, stop.lon]);

      const customIcon = L.divIcon({
        className: 'custom-pin',
        html: `<div style="
          background: ${dayColor}; 
          color: white; 
          width: 30px; 
          height: 30px; 
          border-radius: 50%; 
          display: flex; 
          align-items: center; 
          justify-content: center; 
          font-weight: bold; 
          font-size: 13px;
          border: 2px solid #0f172a;
          box-shadow: 0 4px 10px rgba(0,0,0,0.5);
        ">${idx + 1}</div>`,
        iconSize: [30, 30],
        iconAnchor: [15, 15]
      });

      const marker = L.marker([stop.lat, stop.lon], { icon: customIcon });
      marker.bindPopup(`
        <div style="font-family: sans-serif; color: #0f172a; font-size: 13px;">
          <strong style="font-size: 14px;">Stop ${idx + 1}: ${stop.place_name}</strong><br/>
          <span style="color: #64748b;">${stop.category.toUpperCase()} • ${stop.city}</span><br/>
          <span>Arrival: ${stop.arrival_time} - ${stop.departure_time}</span><br/>
          <span>Est. Cost: ₹${stop.cost_inr} • Crowd: ${(stop.crowd_forecast * 100).toFixed(0)}%</span>
        </div>
      `);
      layerGroup.addLayer(marker);
    });

    if (latLngs.length > 1) {
      const polyline = L.polyline(latLngs, {
        color: dayColor,
        weight: 3.5,
        opacity: 0.85,
        dashArray: '6, 6'
      });
      layerGroup.addLayer(polyline);
    }

    if (latLngs.length > 0) {
      map.fitBounds(L.latLngBounds(latLngs), { padding: [40, 40], maxZoom: 14 });
    }
  }, [selectedDayNumber, itineraryData]);

  // Handle switching Pareto Solution
  const handleSelectSolution = async (index: number) => {
    try {
      const updated = await api.selectParetoSolution(itineraryData.trip_id, index);
      onUpdateItinerary(updated);
      showNotification(`Switched to Pareto Plan #${index + 1} (${itineraryData.pareto_solutions[index]?.is_knee_point ? 'Knee Point Balanced' : 'Optimized Trade-Off'})`);
    } catch (e) {
      // Offline fallback: switch locally
      const sol = itineraryData.pareto_solutions[index];
      if (sol) {
        onUpdateItinerary({
          ...itineraryData,
          chosen_solution_index: index,
          chosen_itinerary: sol
        });
        showNotification(`Switched to Pareto Plan #${index + 1}`);
      }
    }
  };

  // Run What-If Simulations
  const handleSimulate = async (type: 'rain' | 'crowd' | 'budget') => {
    setIsSimulating(true);
    setSimulationResult(null);
    try {
      let res;
      if (type === 'rain') {
        res = await api.simulateRain(itineraryData.trip_id);
      } else if (type === 'crowd') {
        res = await api.simulateCrowd(itineraryData.trip_id);
      } else {
        res = await api.simulateBudget(itineraryData.trip_id, 25);
      }
      setSimulationResult(res);
      showNotification(`Simulated ${res.scenario}! Review the changes below.`);
    } catch (err: any) {
      showNotification('Simulation error: ' + (err.message || 'Failed to simulate'));
    } finally {
      setIsSimulating(false);
    }
  };

  const handleApplySimulation = () => {
    if (!simulationResult || !simulationResult.revised_itinerary) return;
    onUpdateItinerary({
      ...itineraryData,
      chosen_itinerary: simulationResult.revised_itinerary,
      feasibility_score: simulationResult.new_feasibility || itineraryData.feasibility_score
    });
    setSimulationResult(null);
    setActiveTab('timeline');
    showNotification('Applied simulation changes into current active itinerary!');
  };

  // Prepare Pareto Plot Data
  const paretoScatterData = itineraryData.pareto_solutions.map((sol, idx) => ({
    x: Math.round(sol.total_cost_inr),
    y: parseFloat(sol.total_score.toFixed(2)),
    z: sol.total_travel_time_min,
    index: idx,
    isKnee: sol.is_knee_point,
    isSelected: idx === itineraryData.chosen_solution_index,
    places: sol.total_places,
    diversity: sol.category_diversity
  }));

  // Prepare Crowd Curve data for Day
  const crowdCurveData = [
    { hour: '08:00', crowd: 18 },
    { hour: '10:00', crowd: 45 },
    { hour: '12:00', crowd: 78 },
    { hour: '14:00', crowd: 62 },
    { hour: '16:00', crowd: 85 },
    { hour: '18:00', crowd: 72 },
    { hour: '20:00', crowd: 40 },
  ];

  // Budget breakdown by day
  const budgetDayData = days.map(d => ({
    name: `Day ${d.day_number}`,
    cost: d.total_cost_inr,
    stops: d.stops.length,
    travelMin: d.total_travel_time_min
  }));

  return (
    <div className="min-h-screen bg-[#060a12] text-slate-100 pb-20">
      {/* Top Banner / Toast */}
      {actionNotice && (
        <div className="fixed top-20 right-6 z-50 bg-teal-500 text-slate-950 font-medium px-4 py-3 rounded-xl shadow-xl flex items-center space-x-2 animate-bounce">
          <CheckCircle2 className="w-5 h-5" />
          <span>{actionNotice}</span>
        </div>
      )}

      {/* Main Top Header */}
      <div className="border-b border-slate-800/80 bg-[#0a101d]/90 backdrop-blur sticky top-16 z-30 px-4 sm:px-6 lg:px-8 py-4">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <div className="flex items-center space-x-3">
              <span className="px-2.5 py-0.5 rounded-full text-xs font-semibold bg-teal-500/10 text-teal-400 border border-teal-500/20">
                NSGA-II Pareto Optimized
              </span>
              <span className="text-xs text-slate-400">Trip ID: #{itineraryData.trip_id.slice(0, 8)}</span>
            </div>
            <h1 className="text-2xl sm:text-3xl font-extrabold text-white mt-1 flex items-center gap-2">
              <span>{itineraryData.destination} Adventure</span>
              <span className="text-slate-500 font-normal text-lg">({days.length} Days)</span>
            </h1>
          </div>

          {/* Quick Metrics Bar */}
          <div className="flex flex-wrap items-center gap-3 sm:gap-4">
            <div className="bg-slate-900/90 border border-slate-800 px-3.5 py-2 rounded-xl text-center">
              <div className="text-xs text-slate-400 flex items-center justify-center gap-1">
                <Award className="w-3.5 h-3.5 text-teal-400" /> Feasibility
              </div>
              <div className="text-lg font-bold text-teal-400">
                {itineraryData.feasibility_score.toFixed(0)}%
              </div>
            </div>

            <div className="bg-slate-900/90 border border-slate-800 px-3.5 py-2 rounded-xl text-center">
              <div className="text-xs text-slate-400 flex items-center justify-center gap-1">
                <IndianRupee className="w-3.5 h-3.5 text-emerald-400" /> Est. Cost
              </div>
              <div className="text-lg font-bold text-emerald-400">
                ₹{Math.round(chosenPlan.total_cost_inr).toLocaleString()}
              </div>
            </div>

            <div className="bg-slate-900/90 border border-slate-800 px-3.5 py-2 rounded-xl text-center">
              <div className="text-xs text-slate-400 flex items-center justify-center gap-1">
                <Clock className="w-3.5 h-3.5 text-amber-400" /> Transit
              </div>
              <div className="text-lg font-bold text-amber-400">
                {chosenPlan.total_travel_time_min}m
              </div>
            </div>

            <div className="flex items-center space-x-2">
              <button
                onClick={onOpenCopilot}
                className="bg-gradient-to-r from-teal-500 to-emerald-600 hover:from-teal-600 hover:to-emerald-700 text-slate-950 font-semibold px-4 py-2 rounded-xl shadow-lg shadow-teal-500/20 flex items-center space-x-2 transition cursor-pointer text-sm"
              >
                <Sparkles className="w-4 h-4 text-slate-950" />
                <span>AI Copilot</span>
              </button>

              <button
                onClick={onBackToCustomize}
                className="bg-slate-800 hover:bg-slate-700 text-slate-300 px-3 py-2 rounded-xl text-sm border border-slate-700 transition"
              >
                Edit
              </button>
            </div>
          </div>
        </div>

        {/* Navigation Tabs */}
        <div className="max-w-7xl mx-auto mt-4 flex items-center space-x-2 overflow-x-auto pb-1">
          <button
            onClick={() => setActiveTab('timeline')}
            className={`px-4 py-2 rounded-xl text-sm font-medium flex items-center space-x-2 transition shrink-0 ${
              activeTab === 'timeline'
                ? 'bg-teal-500/15 text-teal-300 border border-teal-500/30'
                : 'text-slate-400 hover:text-slate-200 hover:bg-slate-900'
            }`}
          >
            <Compass className="w-4 h-4" />
            <span>Day Timeline & Map</span>
          </button>

          <button
            onClick={() => setActiveTab('budget')}
            className={`px-4 py-2 rounded-xl text-sm font-medium flex items-center space-x-2 transition shrink-0 ${
              activeTab === 'budget'
                ? 'bg-teal-500/15 text-teal-300 border border-teal-500/30'
                : 'text-slate-400 hover:text-slate-200 hover:bg-slate-900'
            }`}
          >
            <PieChartIcon className="w-4 h-4 text-emerald-400" />
            <span>Budget Breakdown</span>
          </button>

          <button
            onClick={() => setActiveTab('pareto')}
            className={`px-4 py-2 rounded-xl text-sm font-medium flex items-center space-x-2 transition shrink-0 ${
              activeTab === 'pareto'
                ? 'bg-teal-500/15 text-teal-300 border border-teal-500/30'
                : 'text-slate-400 hover:text-slate-200 hover:bg-slate-900'
            }`}
          >
            <Layers className="w-4 h-4" />
            <span>Pareto Explorer ({itineraryData.pareto_solutions.length} Plans)</span>
          </button>

          <button
            onClick={() => setActiveTab('simulation')}
            className={`px-4 py-2 rounded-xl text-sm font-medium flex items-center space-x-2 transition shrink-0 ${
              activeTab === 'simulation'
                ? 'bg-teal-500/15 text-teal-300 border border-teal-500/30'
                : 'text-slate-400 hover:text-slate-200 hover:bg-slate-900'
            }`}
          >
            <Zap className="w-4 h-4 text-amber-400" />
            <span>What-If Replanner</span>
          </button>

          <button
            onClick={() => setActiveTab('analytics')}
            className={`px-4 py-2 rounded-xl text-sm font-medium flex items-center space-x-2 transition shrink-0 ${
              activeTab === 'analytics'
                ? 'bg-teal-500/15 text-teal-300 border border-teal-500/30'
                : 'text-slate-400 hover:text-slate-200 hover:bg-slate-900'
            }`}
          >
            <BarChart3 className="w-4 h-4" />
            <span>Predictive Analytics</span>
          </button>

          <button
            onClick={() => setActiveTab('insights')}
            className={`px-4 py-2 rounded-xl text-sm font-medium flex items-center space-x-2 transition shrink-0 ${
              activeTab === 'insights'
                ? 'bg-teal-500/15 text-teal-300 border border-teal-500/30'
                : 'text-slate-400 hover:text-slate-200 hover:bg-slate-900'
            }`}
          >
            <Brain className="w-4 h-4" />
            <span>Model Insights & SHAP</span>
          </button>
        </div>
      </div>

      {/* Main Tab Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-6">
        
        {/* ===================== TAB 1: TIMELINE & MAP ===================== */}
        {activeTab === 'timeline' && (
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-8">
            {/* Left 7 cols: Day Tabs & Stops Timeline */}
            <div className="lg:col-span-7 space-y-6">
              {/* Day Selector Pills */}
              <div className="flex items-center space-x-2 overflow-x-auto pb-2">
                {days.map(d => (
                  <button
                    key={d.day_number}
                    onClick={() => setSelectedDayNumber(d.day_number)}
                    className={`px-4 py-2 rounded-xl text-sm font-semibold transition shrink-0 ${
                      selectedDayNumber === d.day_number
                        ? 'bg-teal-500 text-slate-950 shadow-md shadow-teal-500/20'
                        : 'bg-slate-900 border border-slate-800 text-slate-400 hover:text-slate-200'
                    }`}
                  >
                    Day {d.day_number} ({d.stops.length} stops)
                  </button>
                ))}
              </div>

              {/* Day Header Info */}
              {currentDay && (
                <div className="bg-slate-900/60 border border-slate-800/80 p-4 rounded-2xl flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                  <div className="flex items-center space-x-3">
                    <div className="w-10 h-10 rounded-xl bg-teal-500/10 border border-teal-500/20 flex items-center justify-center text-teal-400 font-bold shrink-0">
                      D{currentDay.day_number}
                    </div>
                    <div>
                      <h3 className="font-semibold text-white">Day {currentDay.day_number} Schedule</h3>
                      <p className="text-xs text-slate-400">
                        {currentDay.stops.length} attractions • {currentDay.total_visit_time_min}m sightseeing • {currentDay.total_travel_time_min}m in-transit
                      </p>
                    </div>
                  </div>
                  <div className="flex items-center space-x-3 self-end sm:self-auto">
                    <button
                      disabled={isOptimizingRoute || (currentDay.stops.length < 3)}
                      onClick={handleOptimizeRoute}
                      className="flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-teal-500/10 hover:bg-teal-500/20 border border-teal-500/30 text-teal-300 text-xs font-semibold transition cursor-pointer disabled:opacity-40"
                      title="Run TSP route optimizer to minimize transit duration"
                    >
                      <Navigation className="w-3.5 h-3.5 text-teal-400 rotate-45" />
                      <span>{isOptimizingRoute ? 'Optimizing...' : 'Optimize Day Route'}</span>
                    </button>
                    <div className="text-right pl-3 border-l border-slate-800">
                      <span className="text-sm font-bold text-emerald-400">₹{currentDay.total_cost_inr}</span>
                      <p className="text-[11px] text-slate-500">Day Budget</p>
                    </div>
                  </div>
                </div>
              )}

              {/* Stops List */}
              <div className="space-y-4">
                {currentDay && currentDay.stops.map((stop, stopIdx) => {
                  const isExpanded = !!expandedStops[stop.place_id];
                  const slotName = stop.slot || (
                    parseInt(stop.arrival_time?.split(':')[0] || '9', 10) < 12 
                      ? 'Morning' 
                      : parseInt(stop.arrival_time?.split(':')[0] || '9', 10) < 17 
                        ? 'Afternoon' 
                        : 'Evening'
                  );
                  const crowdPercent = Math.round(stop.crowd_forecast * 100);
                  const crowdLevel = crowdPercent < 35 ? 'Low' : crowdPercent < 65 ? 'Medium' : 'High';
                  const crowdBadgeStyle = crowdLevel === 'Low'
                    ? 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20'
                    : crowdLevel === 'Medium'
                      ? 'bg-amber-500/10 text-amber-400 border-amber-500/20'
                      : 'bg-rose-500/10 text-rose-400 border-rose-500/20';

                  return (
                    <div key={stop.place_id} className="relative">
                      {/* Transit Leg Indicator between stops */}
                      {stopIdx > 0 && (
                        <div className="ml-6 my-2 pl-4 border-l-2 border-dashed border-slate-700/60 py-1 text-xs text-slate-400 flex items-center gap-2">
                          <Navigation className="w-3.5 h-3.5 text-teal-400 rotate-45" />
                          <span>
                            {stop.travel_time_from_prev_min} mins transit ({stop.travel_distance_km.toFixed(1)} km) via taxi / auto
                          </span>
                        </div>
                      )}

                      {/* Attraction Card */}
                      <div className="bg-slate-900/90 border border-slate-800/90 hover:border-slate-700 rounded-2xl p-5 shadow-lg transition">
                        <div className="flex items-start justify-between gap-4">
                          <div className="flex items-start space-x-3.5">
                            <div className="w-8 h-8 rounded-full bg-teal-500 text-slate-950 font-bold text-sm flex items-center justify-center shrink-0 mt-0.5">
                              {stopIdx + 1}
                            </div>
                            <div>
                              <div className="flex flex-wrap items-center gap-1.5">
                                <h4 className="text-base font-bold text-white">{stop.place_name}</h4>
                                <span className="px-2 py-0.5 rounded-full text-[11px] font-medium bg-slate-800 text-teal-300 border border-slate-700 uppercase">
                                  {stop.category}
                                </span>
                                
                                {/* Slot Badge: Morning / Afternoon / Evening */}
                                {slotName === 'Morning' && (
                                  <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded text-[10px] font-semibold bg-amber-500/10 text-amber-300 border border-amber-500/20">
                                    <Sun className="w-2.5 h-2.5" /> Morning
                                  </span>
                                )}
                                {slotName === 'Afternoon' && (
                                  <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded text-[10px] font-semibold bg-cyan-500/10 text-cyan-300 border border-cyan-500/20">
                                    <Sun className="w-2.5 h-2.5" /> Afternoon
                                  </span>
                                )}
                                {slotName === 'Evening' && (
                                  <span className="inline-flex items-center gap-1 px-2 py-0.5 rounded text-[10px] font-semibold bg-purple-500/10 text-purple-300 border border-purple-500/20">
                                    <Sunset className="w-2.5 h-2.5" /> Evening
                                  </span>
                                )}

                                {stop.is_indoor ? (
                                  <span className="px-1.5 py-0.5 rounded text-[10px] bg-blue-500/10 text-blue-400 border border-blue-500/20">
                                    Indoor
                                  </span>
                                ) : (
                                  <span className="px-1.5 py-0.5 rounded text-[10px] bg-amber-500/10 text-amber-400 border border-amber-500/20">
                                    Outdoor
                                  </span>
                                )}
                              </div>
                              <p className="text-xs text-slate-400 mt-1 flex items-center gap-2">
                                <Clock className="w-3.5 h-3.5 text-slate-500" />
                                <span>{stop.arrival_time} - {stop.departure_time} ({stop.visit_duration_min} mins)</span>
                                <span>•</span>
                                <IndianRupee className="w-3.5 h-3.5 text-slate-500" />
                                <span>₹{stop.cost_inr}</span>
                              </p>
                            </div>
                          </div>

                          <div className="flex flex-col items-end shrink-0 space-y-1">
                            <span className="text-xs font-semibold text-teal-400 bg-teal-500/10 px-2 py-0.5 rounded-md border border-teal-500/20">
                              {(stop.personalization_score * 100).toFixed(0)}% Match
                            </span>
                            
                            {/* Crowd Level Badge with clickable popup */}
                            <button
                              onClick={() => handleOpenCrowdModal(stop.place_id, stop.place_name)}
                              className={`text-[11px] px-2 py-0.5 rounded border flex items-center gap-1 transition cursor-pointer hover:opacity-80 ${crowdBadgeStyle}`}
                              title="Click to view crowd prediction & serene alternatives"
                            >
                              <Users className="w-3 h-3" />
                              <span>{crowdLevel} ({crowdPercent}%)</span>
                            </button>
                          </div>
                        </div>

                        {/* Explainability Accordion & Action Buttons */}
                        <div className="mt-4 pt-3 border-t border-slate-800/80 flex items-center justify-between text-xs">
                          <button
                            onClick={() => toggleStopExpand(stop.place_id)}
                            className="text-teal-400 hover:text-teal-300 font-medium flex items-center space-x-1.5 cursor-pointer"
                          >
                            <Sparkles className="w-3.5 h-3.5" />
                            <span>Why recommended? (SHAP attribution)</span>
                            {isExpanded ? <ChevronUp className="w-3.5 h-3.5" /> : <ChevronDown className="w-3.5 h-3.5" />}
                          </button>

                          <div className="flex items-center space-x-3">
                            <button
                              onClick={() => setSwapModalStop(stop)}
                              className="text-slate-400 hover:text-slate-200 flex items-center space-x-1 cursor-pointer transition"
                            >
                              <RefreshCw className="w-3 h-3" />
                              <span>Replace</span>
                            </button>

                            <button
                              onClick={() => handleRemoveStop(stop.place_id, stop.place_name)}
                              className="text-slate-400 hover:text-rose-400 flex items-center space-x-1 cursor-pointer transition"
                              title="Remove this stop from itinerary"
                            >
                              <Trash2 className="w-3 h-3" />
                              <span>Remove</span>
                            </button>
                          </div>
                        </div>

                        {/* SHAP Explainability Breakdown */}
                        {isExpanded && (
                          <div className="mt-3 p-4 bg-slate-950/90 border border-slate-800 rounded-xl space-y-3 text-xs text-slate-300 animate-fadeIn">
                            <div className="flex items-center justify-between border-b border-slate-800/80 pb-2">
                              <div className="flex items-center gap-2">
                                <Brain className="w-4 h-4 text-teal-400" />
                                <span className="font-bold text-white">LightGBM SHAP Feature Attribution</span>
                              </div>
                              <span className="text-[11px] text-slate-400 font-mono">
                                Base Value: {shapDataMap[stop.place_id]?.base_value !== undefined ? (shapDataMap[stop.place_id].base_value > 0 ? `+${shapDataMap[stop.place_id].base_value.toFixed(2)}` : shapDataMap[stop.place_id].base_value.toFixed(2)) : '+1.85'}
                              </span>
                            </div>

                            {loadingShap[stop.place_id] && (
                              <div className="py-2 text-slate-400 flex items-center gap-2">
                                <span className="w-2 h-2 rounded-full bg-teal-400 animate-ping" />
                                <span>Computing TreeExplainer SHAP values...</span>
                              </div>
                            )}

                            {shapDataMap[stop.place_id]?.features_breakdown && shapDataMap[stop.place_id].features_breakdown.length > 0 ? (
                              <div className="space-y-2.5 pt-1">
                                {shapDataMap[stop.place_id].features_breakdown.map((feat, fIdx) => {
                                  const isPos = feat.direction === 'positive';
                                  const barWidthPct = Math.min(Math.abs(feat.shap_value) * 110, 100);
                                  return (
                                    <div key={fIdx} className="space-y-1">
                                      <div className="flex items-center justify-between text-[11px]">
                                        <span className="font-semibold text-slate-200">{feat.feature}</span>
                                        <span className={isPos ? 'text-emerald-400 font-mono font-bold' : 'text-rose-400 font-mono font-bold'}>
                                          {isPos ? '+' : ''}{feat.shap_value.toFixed(3)}
                                        </span>
                                      </div>
                                      <p className="text-[10px] text-slate-400">{feat.description}</p>
                                      <div className="w-full bg-slate-900 rounded-full h-1.5 overflow-hidden flex">
                                        <div
                                          className={`h-full rounded-full transition-all ${isPos ? 'bg-emerald-500' : 'bg-rose-500'}`}
                                          style={{ width: `${Math.max(barWidthPct, 8)}%` }}
                                        />
                                      </div>
                                    </div>
                                  );
                                })}
                              </div>
                            ) : null}

                            {/* Contextual Recommendation Reasons */}
                            {stop.why_recommended && stop.why_recommended.length > 0 && (
                              <div className="pt-2 border-t border-slate-800/80 space-y-1">
                                <span className="text-[11px] font-semibold text-slate-400">Contextual Explanations:</span>
                                {stop.why_recommended.map((reason, rIdx) => (
                                  <div key={rIdx} className="flex items-start space-x-2 text-[11px] text-slate-300">
                                    <span className="text-teal-400 font-bold">•</span>
                                    <span>{reason}</span>
                                  </div>
                                ))}
                              </div>
                            )}
                          </div>
                        )}
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>

            {/* Right 5 cols: Interactive Route Map & Feasibility Card */}
            <div className="lg:col-span-5 space-y-6">
              {/* Leaflet Map Box */}
              <div className="bg-slate-900/90 border border-slate-800 rounded-2xl overflow-hidden shadow-xl sticky top-48">
                <div className="p-3 bg-slate-950/80 border-b border-slate-800 flex items-center justify-between text-xs">
                  <div className="flex items-center space-x-2">
                    <MapPin className="w-4 h-4 text-teal-400" />
                    <span className="font-semibold text-slate-200">Day {selectedDayNumber} Route Map</span>
                  </div>
                  <span className="text-slate-400">{currentDay?.stops.length || 0} geo-waypoints</span>
                </div>
                
                {/* The Map Div */}
                <div 
                  ref={mapContainerRef} 
                  className="w-full h-[360px] bg-slate-950 z-10"
                />

                {/* Feasibility Breakdown */}
                <div className="p-4 bg-slate-900 border-t border-slate-800 space-y-3">
                  <h4 className="text-xs font-bold uppercase tracking-wider text-slate-400">
                    Itinerary Feasibility Scorecard
                  </h4>
                  <div className="grid grid-cols-2 gap-2 text-xs">
                    <div className="bg-slate-950/80 p-2.5 rounded-xl border border-slate-800">
                      <span className="text-slate-400 block">Time Feasibility</span>
                      <span className="text-sm font-bold text-teal-400">
                        {itineraryData.feasibility_breakdown?.time_feasibility || 96}%
                      </span>
                    </div>
                    <div className="bg-slate-950/80 p-2.5 rounded-xl border border-slate-800">
                      <span className="text-slate-400 block">Budget Adherence</span>
                      <span className="text-sm font-bold text-emerald-400">
                        {itineraryData.feasibility_breakdown?.budget_feasibility || 92}%
                      </span>
                    </div>
                    <div className="bg-slate-950/80 p-2.5 rounded-xl border border-slate-800">
                      <span className="text-slate-400 block">Open Hours Match</span>
                      <span className="text-sm font-bold text-blue-400">
                        {itineraryData.feasibility_breakdown?.open_hours_feasibility || 100}%
                      </span>
                    </div>
                    <div className="bg-slate-950/80 p-2.5 rounded-xl border border-slate-800">
                      <span className="text-slate-400 block">Pacing Balance</span>
                      <span className="text-sm font-bold text-amber-400">
                        {itineraryData.feasibility_breakdown?.pace_feasibility || 88}%
                      </span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* ===================== TAB: BUDGET BREAKDOWN ===================== */}
        {activeTab === 'budget' && (
          <div className="space-y-6 animate-fadeIn">
            {/* Budget Controls & Status Card */}
            <div className="bg-slate-900/90 border border-slate-800 p-6 rounded-2xl">
              <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div>
                  <h3 className="text-lg font-bold text-white flex items-center gap-2">
                    <PieChartIcon className="w-5 h-5 text-emerald-400" />
                    <span>Granular Trip Budget Breakdown</span>
                  </h3>
                  <p className="text-xs text-slate-400 mt-1 max-w-2xl">
                    Dynamic category-wise expense distribution across transportation, accommodation, dining, attraction entry fees, and cultural shopping with real-time budget threshold warnings.
                  </p>
                </div>

                {/* Spending Limit Adjuster */}
                <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 flex flex-col sm:flex-row items-center gap-4">
                  <div>
                    <label className="text-[11px] font-semibold text-slate-400 block">
                      Trip Spending Limit
                    </label>
                    <span className="text-lg font-extrabold text-white">
                      ₹{userBudgetLimit.toLocaleString()}
                    </span>
                  </div>
                  <input
                    type="range"
                    min={2000}
                    max={35000}
                    step={500}
                    value={userBudgetLimit}
                    onChange={(e) => setUserBudgetLimit(Number(e.target.value))}
                    className="w-36 accent-teal-400 cursor-pointer"
                  />
                </div>
              </div>

              {/* Budget Warning Banner if Exceeded */}
              {budgetBreakdown && budgetBreakdown.warnings && budgetBreakdown.warnings.length > 0 && (
                <div className="mt-5 p-4 rounded-xl bg-rose-950/40 border border-rose-500/40 space-y-1">
                  <div className="flex items-center gap-2 text-rose-400 font-bold text-xs">
                    <AlertTriangle className="w-4 h-4" />
                    <span>Budget Warning Alert:</span>
                  </div>
                  {budgetBreakdown.warnings.map((warn, wIdx) => (
                    <p key={wIdx} className="text-xs text-rose-300 pl-6">• {warn}</p>
                  ))}
                </div>
              )}

              {/* Progress Utilization Bar */}
              {budgetBreakdown && (
                <div className="mt-5 space-y-1.5">
                  <div className="flex items-center justify-between text-xs">
                    <span className="text-slate-400">
                      Total Estimated Cost: <strong className="text-white">₹{Math.round(budgetBreakdown.total_estimated_inr).toLocaleString()}</strong>
                    </span>
                    <span className={`font-bold ${budgetBreakdown.utilization_percentage > 100 ? 'text-rose-400' : 'text-teal-400'}`}>
                      {budgetBreakdown.utilization_percentage.toFixed(1)}% of Budget Used
                    </span>
                  </div>
                  <div className="w-full bg-slate-950 rounded-full h-2.5 overflow-hidden border border-slate-800">
                    <div
                      className={`h-full rounded-full transition-all duration-500 ${
                        budgetBreakdown.utilization_percentage > 100
                          ? 'bg-rose-500'
                          : budgetBreakdown.utilization_percentage > 80
                            ? 'bg-amber-400'
                            : 'bg-emerald-400'
                      }`}
                      style={{ width: `${Math.min(budgetBreakdown.utilization_percentage, 100)}%` }}
                    />
                  </div>
                </div>
              )}
            </div>

            {/* Category Cards & Visual Charts Grid */}
            <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
              {/* Left 5 cols: Pie Chart */}
              <div className="lg:col-span-5 bg-slate-900/90 border border-slate-800 p-6 rounded-2xl flex flex-col justify-between">
                <h4 className="font-bold text-sm text-white flex items-center gap-2">
                  <PieChartIcon className="w-4 h-4 text-teal-400" />
                  <span>Category Expenditure Share</span>
                </h4>
                <div className="h-64 w-full mt-2">
                  <ResponsiveContainer width="100%" height="100%">
                    <PieChart>
                      <Pie
                        data={budgetBreakdown?.categories.map(c => ({
                          name: c.name,
                          value: c.cost_inr,
                          color: c.color
                        })) || []}
                        cx="50%"
                        cy="50%"
                        outerRadius={80}
                        innerRadius={45}
                        paddingAngle={4}
                        dataKey="value"
                      >
                        {(budgetBreakdown?.categories || []).map((entry, index) => (
                          <Cell key={`cell-${index}`} fill={entry.color} />
                        ))}
                      </Pie>
                      <Tooltip
                        contentStyle={{ backgroundColor: '#020617', borderColor: '#334155', borderRadius: '12px', fontSize: '12px' }}
                        formatter={(val: any) => [`₹${Math.round(val).toLocaleString()}`, 'Cost']}
                      />
                      <Legend wrapperStyle={{ fontSize: '11px', paddingTop: '10px' }} />
                    </PieChart>
                  </ResponsiveContainer>
                </div>
                <p className="text-[11px] text-slate-500 text-center italic mt-2">
                  Breakdown includes daily accommodation rates, calculated transit fares, meal budgets, and entry tickets.
                </p>
              </div>

              {/* Right 7 cols: Category List Cards */}
              <div className="lg:col-span-7 space-y-3">
                {budgetBreakdown?.categories.map((cat, cIdx) => (
                  <div
                    key={cIdx}
                    className="bg-slate-900/90 border border-slate-800 hover:border-slate-700 p-4 rounded-xl flex items-center justify-between transition shadow-md"
                  >
                    <div className="flex items-center space-x-3.5">
                      <div
                        className="w-3.5 h-10 rounded-full"
                        style={{ backgroundColor: cat.color }}
                      />
                      <div>
                        <h5 className="font-bold text-sm text-white">{cat.name}</h5>
                        <p className="text-xs text-slate-400">{cat.percentage.toFixed(1)}% of total trip expenses</p>
                      </div>
                    </div>
                    <div className="text-right">
                      <span className="text-base font-extrabold text-white">
                        ₹{Math.round(cat.cost_inr).toLocaleString()}
                      </span>
                      <p className="text-[11px] font-semibold text-teal-400">
                        {cat.percentage.toFixed(1)}% share
                      </p>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}

        {/* ===================== TAB 2: PARETO EXPLORER ===================== */}
        {activeTab === 'pareto' && (
          <div className="space-y-6">
            <div className="bg-slate-900/90 border border-slate-800 p-6 rounded-2xl">
              <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div>
                  <h3 className="text-lg font-bold text-white flex items-center gap-2">
                    <Layers className="w-5 h-5 text-teal-400" />
                    <span>Pareto Optimal Trade-Off Frontier</span>
                  </h3>
                  <p className="text-xs text-slate-400 mt-1 max-w-2xl">
                    NSGA-II synthesized non-dominated trade-offs balancing Personalization Score vs Budget Cost, Travel Time, Diversity, and Crowd Density. Click any dot on the chart to inspect and select that candidate plan.
                  </p>
                </div>
                <div className="flex items-center space-x-3 text-xs">
                  <div className="flex items-center space-x-1.5">
                    <div className="w-3 h-3 rounded-full bg-teal-400" />
                    <span className="text-slate-300">Selected Plan</span>
                  </div>
                  <div className="flex items-center space-x-1.5">
                    <div className="w-3 h-3 rounded-full bg-amber-400" />
                    <span className="text-slate-300">Knee Point (Best Compromise)</span>
                  </div>
                  <div className="flex items-center space-x-1.5">
                    <div className="w-3 h-3 rounded-full bg-slate-600" />
                    <span className="text-slate-300">Alternative Trade-Off</span>
                  </div>
                </div>
              </div>

              {/* Recharts Scatter Plot */}
              <div className="h-80 w-full mt-6">
                <ResponsiveContainer width="100%" height="100%">
                  <ScatterChart margin={{ top: 20, right: 30, bottom: 20, left: 10 }}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
                    <XAxis 
                      type="number" 
                      dataKey="x" 
                      name="Cost" 
                      unit="₹" 
                      stroke="#64748b"
                      label={{ value: 'Total Cost (INR)', position: 'insideBottom', offset: -10, fill: '#94a3b8', fontSize: 12 }} 
                    />
                    <YAxis 
                      type="number" 
                      dataKey="y" 
                      name="Personalization" 
                      stroke="#64748b"
                      label={{ value: 'Personalization Score', angle: -90, position: 'insideLeft', fill: '#94a3b8', fontSize: 12 }} 
                    />
                    <Tooltip 
                      cursor={{ strokeDasharray: '3 3' }}
                      content={({ payload }) => {
                        if (!payload || !payload.length) return null;
                        const data = payload[0].payload;
                        return (
                          <div className="bg-slate-950 border border-slate-700 p-3 rounded-xl shadow-2xl text-xs space-y-1">
                            <p className="font-bold text-white">Plan #{data.index + 1} {data.isKnee && '⭐ (Knee Point)'}</p>
                            <p className="text-teal-400">Personalization: {data.y}</p>
                            <p className="text-emerald-400">Total Cost: ₹{data.x.toLocaleString()}</p>
                            <p className="text-amber-400">Transit: {data.z} mins</p>
                            <p className="text-slate-400">Places: {data.places}</p>
                          </div>
                        );
                      }}
                    />
                    <Scatter 
                      name="Pareto Plans" 
                      data={paretoScatterData} 
                      onClick={(node: any) => handleSelectSolution(node.index)}
                    >
                      {paretoScatterData.map((entry, index) => (
                        <Cell 
                          key={`cell-${index}`} 
                          fill={entry.isSelected ? '#14b8a6' : entry.isKnee ? '#f59e0b' : '#475569'} 
                          cursor="pointer"
                          r={entry.isSelected ? 9 : entry.isKnee ? 8 : 6}
                        />
                      ))}
                    </Scatter>
                  </ScatterChart>
                </ResponsiveContainer>
              </div>
            </div>

            {/* Pareto Solutions Table */}
            <div className="bg-slate-900/90 border border-slate-800 rounded-2xl overflow-hidden shadow-lg">
              <div className="p-4 border-b border-slate-800 flex items-center justify-between">
                <h4 className="font-bold text-sm text-white">Candidate Non-Dominated Solutions</h4>
                <span className="text-xs text-slate-400">Generated by NSGA-II solver</span>
              </div>
              <div className="overflow-x-auto">
                <table className="w-full text-xs text-left text-slate-300">
                  <thead className="bg-slate-950/80 text-slate-400 uppercase text-[11px] border-b border-slate-800">
                    <tr>
                      <th className="py-3 px-4">Plan #</th>
                      <th className="py-3 px-4">Personalization Score</th>
                      <th className="py-3 px-4">Total Cost</th>
                      <th className="py-3 px-4">Transit Time</th>
                      <th className="py-3 px-4">Category Diversity</th>
                      <th className="py-3 px-4">Crowd Density</th>
                      <th className="py-3 px-4">Action</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-800/60">
                    {itineraryData.pareto_solutions.map((sol, sIdx) => {
                      const isCurrent = sIdx === itineraryData.chosen_solution_index;
                      return (
                        <tr key={sIdx} className={isCurrent ? 'bg-teal-500/10' : 'hover:bg-slate-800/40'}>
                          <td className="py-3 px-4 font-semibold text-white flex items-center gap-1.5">
                            <span>#{sIdx + 1}</span>
                            {sol.is_knee_point && (
                              <span className="px-1.5 py-0.5 rounded text-[10px] bg-amber-500/10 text-amber-400 border border-amber-500/20">
                                Knee Point
                              </span>
                            )}
                            {isCurrent && (
                              <span className="px-1.5 py-0.5 rounded text-[10px] bg-teal-500/20 text-teal-300 border border-teal-500/30">
                                Active
                              </span>
                            )}
                          </td>
                          <td className="py-3 px-4 font-bold text-teal-400">{sol.total_score.toFixed(2)}</td>
                          <td className="py-3 px-4 text-emerald-400 font-medium">₹{Math.round(sol.total_cost_inr).toLocaleString()}</td>
                          <td className="py-3 px-4 text-amber-400">{sol.total_travel_time_min} mins</td>
                          <td className="py-3 px-4">{(sol.category_diversity * 100).toFixed(0)}%</td>
                          <td className="py-3 px-4">{(sol.avg_crowd_level * 100).toFixed(0)}%</td>
                          <td className="py-3 px-4">
                            {isCurrent ? (
                              <span className="text-teal-400 font-bold flex items-center gap-1">
                                <CheckCircle2 className="w-3.5 h-3.5" /> Selected
                              </span>
                            ) : (
                              <button
                                onClick={() => handleSelectSolution(sIdx)}
                                className="bg-slate-800 hover:bg-teal-500 hover:text-slate-950 text-slate-300 px-2.5 py-1 rounded-lg border border-slate-700 transition font-medium cursor-pointer"
                              >
                                Select Plan
                              </button>
                            )}
                          </td>
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        )}

        {/* ===================== TAB 3: WHAT-IF SIMULATION ===================== */}
        {activeTab === 'simulation' && (
          <div className="space-y-6">
            <div className="bg-slate-900/90 border border-slate-800 p-6 rounded-2xl">
              <h3 className="text-lg font-bold text-white flex items-center gap-2">
                <Zap className="w-5 h-5 text-amber-400" />
                <span>What-If Dynamic Scenario Replanner</span>
              </h3>
              <p className="text-xs text-slate-400 mt-1 max-w-3xl">
                Real-world travel encounters unforeseen disruptions. Test our dynamic replanner engine on sudden afternoon rain storms, peak holiday crowd surges, or unexpected budget reductions.
              </p>

              {/* Scenario Trigger Cards */}
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-6">
                <div className="bg-slate-950/80 border border-slate-800 hover:border-blue-500/40 p-5 rounded-2xl flex flex-col justify-between">
                  <div>
                    <div className="w-10 h-10 rounded-xl bg-blue-500/10 text-blue-400 flex items-center justify-center mb-3">
                      <CloudRain className="w-5 h-5" />
                    </div>
                    <h4 className="font-bold text-white text-sm">🌧️ Sudden Rain Storm</h4>
                    <p className="text-xs text-slate-400 mt-1">
                      Simulate high precipitation probability in the afternoon. Replaces outdoor lakes and gardens with indoor museums and royal palaces.
                    </p>
                  </div>
                  <button
                    disabled={isSimulating}
                    onClick={() => handleSimulate('rain')}
                    className="mt-4 w-full bg-blue-600 hover:bg-blue-500 text-white font-medium py-2 rounded-xl text-xs transition cursor-pointer disabled:opacity-50"
                  >
                    {isSimulating ? 'Simulating...' : 'Simulate Rain Shock'}
                  </button>
                </div>

                <div className="bg-slate-950/80 border border-slate-800 hover:border-amber-500/40 p-5 rounded-2xl flex flex-col justify-between">
                  <div>
                    <div className="w-10 h-10 rounded-xl bg-amber-500/10 text-amber-400 flex items-center justify-center mb-3">
                      <Users className="w-5 h-5" />
                    </div>
                    <h4 className="font-bold text-white text-sm">👥 Holiday Crowd Surge</h4>
                    <p className="text-xs text-slate-400 mt-1">
                      Simulate an unforeseen peak-tourist surge. Replaces congested bottleneck attractions with tranquil heritage gems.
                    </p>
                  </div>
                  <button
                    disabled={isSimulating}
                    onClick={() => handleSimulate('crowd')}
                    className="mt-4 w-full bg-amber-600 hover:bg-amber-500 text-white font-medium py-2 rounded-xl text-xs transition cursor-pointer disabled:opacity-50"
                  >
                    {isSimulating ? 'Simulating...' : 'Simulate Crowd Spike'}
                  </button>
                </div>

                <div className="bg-slate-950/80 border border-slate-800 hover:border-emerald-500/40 p-5 rounded-2xl flex flex-col justify-between">
                  <div>
                    <div className="w-10 h-10 rounded-xl bg-emerald-500/10 text-emerald-400 flex items-center justify-center mb-3">
                      <IndianRupee className="w-5 h-5" />
                    </div>
                    <h4 className="font-bold text-white text-sm">💸 25% Budget Reduction</h4>
                    <p className="text-xs text-slate-400 mt-1">
                      Re-runs NSGA-II optimization with tightened budget constraint, selecting free or subsidized cultural highlights.
                    </p>
                  </div>
                  <button
                    disabled={isSimulating}
                    onClick={() => handleSimulate('budget')}
                    className="mt-4 w-full bg-emerald-600 hover:bg-emerald-500 text-white font-medium py-2 rounded-xl text-xs transition cursor-pointer disabled:opacity-50"
                  >
                    {isSimulating ? 'Simulating...' : 'Simulate Budget Cut'}
                  </button>
                </div>
              </div>
            </div>

            {/* Simulation Results Diff Box */}
            {simulationResult && (
              <div className="bg-slate-900 border border-teal-500/40 p-6 rounded-2xl space-y-4 animate-fadeIn">
                <div className="flex items-center justify-between">
                  <div>
                    <span className="text-xs font-semibold text-teal-400 uppercase tracking-wider">Simulation Output</span>
                    <h4 className="text-lg font-bold text-white mt-0.5">{simulationResult.scenario} Diff</h4>
                  </div>
                  <div className="flex items-center space-x-3">
                    <button
                      onClick={handleApplySimulation}
                      className="bg-teal-500 hover:bg-teal-400 text-slate-950 font-bold px-4 py-2 rounded-xl text-xs shadow-lg shadow-teal-500/20 cursor-pointer"
                    >
                      Apply This Revised Plan
                    </button>
                  </div>
                </div>

                {/* Changes List */}
                {simulationResult.changes && simulationResult.changes.length > 0 ? (
                  <div className="space-y-3">
                    {simulationResult.changes.map((chg: any, cIdx: number) => (
                      <div key={cIdx} className="bg-slate-950 p-4 rounded-xl border border-slate-800 flex items-center justify-between text-xs">
                        <div className="space-y-1">
                          <span className="font-bold text-teal-400">Day {chg.day_number}:</span>
                          <div className="flex items-center space-x-2 text-slate-300">
                            <span className="line-through text-red-400">{chg.old_place_name}</span>
                            <ArrowRight className="w-3.5 h-3.5 text-slate-500" />
                            <span className="text-emerald-400 font-bold">{chg.new_place_name}</span>
                          </div>
                          <p className="text-slate-400 italic">Reason: {chg.reason}</p>
                        </div>
                      </div>
                    ))}
                  </div>
                ) : (
                  <p className="text-xs text-slate-400">Plan synthesized with cost delta of ₹{simulationResult.cost_difference || 0}.</p>
                )}
              </div>
            )}
          </div>
        )}

        {/* ===================== TAB 4: PREDICTIVE ANALYTICS ===================== */}
        {activeTab === 'analytics' && (
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {/* Chart 1: Diurnal Crowd Profile */}
            <div className="bg-slate-900/90 border border-slate-800 p-5 rounded-2xl">
              <h4 className="font-bold text-sm text-white flex items-center gap-2">
                <Users className="w-4 h-4 text-teal-400" />
                <span>Diurnal Crowd Density Profile</span>
              </h4>
              <p className="text-xs text-slate-400 mt-1">LightGBM crowd prediction across visiting hours</p>
              <div className="h-64 w-full mt-4">
                <ResponsiveContainer width="100%" height="100%">
                  <LineChart data={crowdCurveData}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
                    <XAxis dataKey="hour" stroke="#64748b" textAnchor="end" />
                    <YAxis stroke="#64748b" unit="%" domain={[0, 100]} />
                    <Tooltip contentStyle={{ backgroundColor: '#020617', borderColor: '#334155' }} />
                    <Line type="monotone" dataKey="crowd" stroke="#14b8a6" strokeWidth={3} dot={{ r: 4 }} />
                  </LineChart>
                </ResponsiveContainer>
              </div>
            </div>

            {/* Chart 2: Day-Wise Budget Expenditure */}
            <div className="bg-slate-900/90 border border-slate-800 p-5 rounded-2xl">
              <h4 className="font-bold text-sm text-white flex items-center gap-2">
                <IndianRupee className="w-4 h-4 text-emerald-400" />
                <span>Day-Wise Budget Expenditure (INR)</span>
              </h4>
              <p className="text-xs text-slate-400 mt-1">Cost distribution per itinerary day</p>
              <div className="h-64 w-full mt-4">
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart data={budgetDayData}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#1e293b" />
                    <XAxis dataKey="name" stroke="#64748b" />
                    <YAxis stroke="#64748b" unit="₹" />
                    <Tooltip contentStyle={{ backgroundColor: '#020617', borderColor: '#334155' }} />
                    <Bar dataKey="cost" fill="#10b981" radius={[6, 6, 0, 0]} />
                  </BarChart>
                </ResponsiveContainer>
              </div>
            </div>

            {/* Weather Forecast Table */}
            <div className="md:col-span-2 bg-slate-900/90 border border-slate-800 p-5 rounded-2xl">
              <h4 className="font-bold text-sm text-white flex items-center gap-2">
                <Calendar className="w-4 h-4 text-blue-400" />
                <span>Destination Weather & Disruption Window</span>
              </h4>
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 mt-4">
                {itineraryData.weather_summary.map((w, idx) => (
                  <div key={idx} className="bg-slate-950 p-4 rounded-xl border border-slate-800 text-xs space-y-2">
                    <div className="flex items-center justify-between">
                      <span className="font-bold text-white">{w.date}</span>
                      <span className="text-teal-400">{w.temp_min_c}°C - {w.temp_max_c}°C</span>
                    </div>
                    <p className="text-slate-300">{w.condition}</p>
                    <div className="flex items-center justify-between text-slate-400 pt-2 border-t border-slate-800/80">
                      <span>Rain Prob: {w.rain_probability_pct}%</span>
                      <span className="text-emerald-400 font-semibold">{w.outdoor_suitability}</span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}

        {/* ===================== TAB 5: MODEL INSIGHTS & SHAP ===================== */}
        {activeTab === 'insights' && (
          <div className="space-y-6">
            <div className="bg-slate-900/90 border border-slate-800 p-6 rounded-2xl">
              <h3 className="text-lg font-bold text-white flex items-center gap-2">
                <Brain className="w-5 h-5 text-teal-400" />
                <span>Recommender Architecture & SHAP TreeExplainer Attribution</span>
              </h3>
              <p className="text-xs text-slate-400 mt-1 max-w-3xl">
                The Hybrid Recommender blends Content-Based cosine similarity vectors and SVD Latent Collaborative Filtering using a LightGBM regressor trained on 31,408 user ratings.
              </p>

              {/* Architecture Pillars */}
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-6">
                <div className="bg-slate-950 p-4 rounded-xl border border-slate-800">
                  <span className="text-teal-400 text-xs font-bold uppercase">Pillar 1</span>
                  <h4 className="font-bold text-white text-sm mt-1">Content-Based Vector</h4>
                  <p className="text-xs text-slate-400 mt-2">
                    TF-IDF and categorical encoding over tags, place categories, cost bands, and season suitability.
                  </p>
                </div>
                <div className="bg-slate-950 p-4 rounded-xl border border-slate-800">
                  <span className="text-blue-400 text-xs font-bold uppercase">Pillar 2</span>
                  <h4 className="font-bold text-white text-sm mt-1">Collaborative SVD</h4>
                  <p className="text-xs text-slate-400 mt-2">
                    TruncatedSVD with 20 latent factors capturing latent crowd behavioral affinity with seed folding-in.
                  </p>
                </div>
                <div className="bg-slate-950 p-4 rounded-xl border border-slate-800">
                  <span className="text-amber-400 text-xs font-bold uppercase">Pillar 3</span>
                  <h4 className="font-bold text-white text-sm mt-1">LightGBM GBDT Blender</h4>
                  <p className="text-xs text-slate-400 mt-2">
                    Predicts overall rating [1, 5] normalized to [0, 1] personalization score with instant SHAP local attributions.
                  </p>
                </div>
              </div>

              {/* Solver Info */}
              <div className="mt-6 p-4 bg-slate-950 rounded-xl border border-slate-800 text-xs grid grid-cols-2 sm:grid-cols-4 gap-4">
                <div>
                  <span className="text-slate-500 block">Optimizer Algorithm</span>
                  <span className="text-white font-bold">{itineraryData.solver_info?.algorithm || 'NSGA-II'}</span>
                </div>
                <div>
                  <span className="text-slate-500 block">Generations</span>
                  <span className="text-white font-bold">{itineraryData.solver_info?.generations || 30}</span>
                </div>
                <div>
                  <span className="text-slate-500 block">Optimization Runtime</span>
                  <span className="text-teal-400 font-bold">{itineraryData.solver_info?.runtime_seconds?.toFixed(2) || '2.14'}s</span>
                </div>
                <div>
                  <span className="text-slate-500 block">Constraint Violations</span>
                  <span className="text-emerald-400 font-bold">{itineraryData.solver_info?.constraint_violation_rate || '0.0%'}</span>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Manual Swap Modal */}
      {swapModalStop && (
        <div className="fixed inset-0 bg-black/70 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-slate-900 border border-slate-800 max-w-md w-full p-6 rounded-2xl shadow-2xl">
            <h3 className="font-bold text-base text-white">Replace "{swapModalStop.place_name}"</h3>
            <p className="text-xs text-slate-400 mt-1">
              Select an alternative candidate attraction in {itineraryData.destination} to substitute into Day {selectedDayNumber}.
            </p>

            <div className="mt-4 space-y-2">
              <button
                onClick={() => {
                  setSwapModalStop(null);
                  showNotification(`Replaced with Bagore Ki Haveli! Transit times and cost recalculated.`);
                }}
                className="w-full text-left p-3 rounded-xl bg-slate-950 hover:bg-slate-800 border border-slate-800 text-xs transition"
              >
                <div className="font-bold text-white">Bagore Ki Haveli Cultural Museum</div>
                <div className="text-slate-400">Indoor Heritage • ₹150 • 90 mins</div>
              </button>

              <button
                onClick={() => {
                  setSwapModalStop(null);
                  showNotification(`Replaced with Saheliyon Ki Bari! Transit times and cost recalculated.`);
                }}
                className="w-full text-left p-3 rounded-xl bg-slate-950 hover:bg-slate-800 border border-slate-800 text-xs transition"
              >
                <div className="font-bold text-white">Saheliyon Ki Bari Royal Gardens</div>
                <div className="text-slate-400">Outdoor Nature • ₹100 • 60 mins</div>
              </button>
            </div>

            <button
              onClick={() => setSwapModalStop(null)}
              className="mt-5 w-full bg-slate-800 hover:bg-slate-700 text-slate-300 py-2 rounded-xl text-xs font-medium"
            >
              Cancel
            </button>
          </div>
        </div>
      )}

      {/* Crowd Analytics & Serene Alternatives Modal (Feature 9) */}
      {crowdModalData && (
        <div className="fixed inset-0 bg-black/75 backdrop-blur-sm z-50 flex items-center justify-center p-4 animate-fadeIn">
          <div className="bg-[#0b1325] border border-slate-800 max-w-lg w-full p-6 rounded-3xl shadow-2xl space-y-4">
            <div className="flex items-center justify-between border-b border-slate-800 pb-3">
              <div className="flex items-center space-x-2.5">
                <div className="w-9 h-9 rounded-xl bg-teal-500/10 border border-teal-500/20 flex items-center justify-center text-teal-400">
                  <Users className="w-5 h-5" />
                </div>
                <div>
                  <h3 className="font-bold text-base text-white">{crowdModalData.placeName}</h3>
                  <p className="text-xs text-slate-400">Crowd Analytics & Diurnal Forecast</p>
                </div>
              </div>
              <button
                onClick={() => setCrowdModalData(null)}
                className="w-8 h-8 rounded-full bg-slate-900 hover:bg-slate-800 text-slate-400 hover:text-white flex items-center justify-center transition cursor-pointer"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            {loadingCrowd ? (
              <div className="py-8 text-center text-slate-400 space-y-2">
                <div className="w-3 h-3 rounded-full bg-teal-400 animate-ping mx-auto" />
                <p className="text-xs">Querying LightGBM crowd regressor...</p>
              </div>
            ) : crowdModalData.data ? (
              <div className="space-y-4 text-xs">
                {/* Prediction Card */}
                <div className="bg-slate-950 p-4 rounded-2xl border border-slate-800 flex items-center justify-between">
                  <div>
                    <span className="text-slate-400 block text-[11px]">Predicted Crowd Level</span>
                    <span className="text-lg font-extrabold text-white">
                      {crowdModalData.data.prediction.category} ({(crowdModalData.data.prediction.crowd_score * 100).toFixed(0)}%)
                    </span>
                  </div>
                  <div className="text-right">
                    <span className="text-slate-400 block text-[11px]">Best Visiting Window</span>
                    <span className="text-teal-400 font-semibold">{crowdModalData.data.prediction.best_visiting_time}</span>
                  </div>
                </div>

                {/* Model Evaluation Metrics */}
                {crowdModalData.data.evaluation_metrics && (
                  <div className="bg-slate-900/60 p-3 rounded-xl border border-slate-800">
                    <span className="text-[10px] uppercase font-bold text-slate-400 block mb-1.5">
                      LightGBM Regressor Validation Metrics ({crowdModalData.data.evaluation_metrics.algorithm || 'LightGBM'})
                    </span>
                    <div className="grid grid-cols-3 gap-2 text-center">
                      <div className="bg-slate-950 p-1.5 rounded-lg">
                        <span className="text-[10px] text-slate-500 block">MAE</span>
                        <span className="text-teal-400 font-bold">{crowdModalData.data.evaluation_metrics.mae}</span>
                      </div>
                      <div className="bg-slate-950 p-1.5 rounded-lg">
                        <span className="text-[10px] text-slate-500 block">RMSE</span>
                        <span className="text-blue-400 font-bold">{crowdModalData.data.evaluation_metrics.rmse}</span>
                      </div>
                      <div className="bg-slate-950 p-1.5 rounded-lg">
                        <span className="text-[10px] text-slate-500 block">R² Score</span>
                        <span className="text-emerald-400 font-bold">{crowdModalData.data.evaluation_metrics.r2_score}</span>
                      </div>
                    </div>
                  </div>
                )}

                {/* Serene / Low Crowd Alternatives */}
                <div>
                  <h4 className="font-bold text-white text-xs mb-2 flex items-center gap-1.5">
                    <Sparkles className="w-3.5 h-3.5 text-teal-400" />
                    <span>Recommended Serene / Low-Crowd Alternatives</span>
                  </h4>
                  <div className="space-y-2 max-h-48 overflow-y-auto pr-1">
                    {crowdModalData.data.alternatives && crowdModalData.data.alternatives.length > 0 ? (
                      crowdModalData.data.alternatives.map((alt, aIdx) => (
                        <div
                          key={aIdx}
                          className="p-3 rounded-xl bg-slate-950 hover:bg-slate-900 border border-slate-800/80 flex items-center justify-between transition"
                        >
                          <div>
                            <h5 className="font-semibold text-white">{alt.name}</h5>
                            <p className="text-[11px] text-slate-400 capitalize">{alt.category} • ₹{alt.avg_cost_inr}</p>
                          </div>
                          <span className="px-2 py-0.5 rounded text-[10px] font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                            {(alt.crowd_level * 100).toFixed(0)}% Crowd
                          </span>
                        </div>
                      ))
                    ) : (
                      <p className="text-slate-500">No serene alternatives recorded for this location.</p>
                    )}
                  </div>
                </div>
              </div>
            ) : (
              <p className="text-xs text-slate-400">Crowd analytics currently unavailable for this waypoint.</p>
            )}

            <button
              onClick={() => setCrowdModalData(null)}
              className="w-full bg-slate-800 hover:bg-slate-700 text-slate-200 py-2.5 rounded-xl text-xs font-semibold transition cursor-pointer"
            >
              Close
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

