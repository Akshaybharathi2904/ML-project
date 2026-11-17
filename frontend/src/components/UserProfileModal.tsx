import React, { useState, useEffect } from 'react';
import { 
  X, User, ShieldCheck, Heart, Star, Sliders, History, Calendar, 
  IndianRupee, Award, Clock, ArrowRight, Save, Trash2, CheckCircle2, 
  MapPin, RefreshCw, Sparkles, BookOpen
} from 'lucide-react';
import { api } from '../services/api';
import { UserProfile, SavedTripItem, UserRatingItem, ItineraryResponse } from '../types';

interface UserProfileModalProps {
  isOpen: boolean;
  onClose: () => void;
  currentTrip?: ItineraryResponse | null;
  onLoadTrip: (loaded: ItineraryResponse) => void;
}

const CATEGORIES = [
  { key: 'heritage', label: 'Heritage & Forts' },
  { key: 'nature', label: 'Nature & Scenic' },
  { key: 'temple', label: 'Spiritual & Temples' },
  { key: 'adventure', label: 'Adventure & Trails' },
  { key: 'food', label: 'Food & Culinary' },
  { key: 'shopping', label: 'Shopping & Bazaars' },
  { key: 'museum', label: 'Museums & Art' },
  { key: 'wildlife', label: 'Wildlife & Safari' }
];

export const UserProfileModal: React.FC<UserProfileModalProps> = ({
  isOpen,
  onClose,
  currentTrip,
  onLoadTrip
}) => {
  const [activeTab, setActiveTab] = useState<'profile' | 'history' | 'ratings'>('profile');
  const [usernameInput, setUsernameInput] = useState('Priya_Traveler');
  const [userProfile, setUserProfile] = useState<UserProfile>({
    user_id: 'USR_DEMO_01',
    username: 'Priya_Traveler',
    email: 'priya.traveler@travelmate.ai',
    budget_level: 'medium',
    pace_preference: 'moderate',
    preferences: {
      heritage: 0.85,
      nature: 0.90,
      temple: 0.50,
      adventure: 0.65,
      food: 0.75,
      shopping: 0.40,
      museum: 0.60,
      wildlife: 0.55
    }
  });

  const [savedTrips, setSavedTrips] = useState<SavedTripItem[]>([]);
  const [userRatings, setUserRatings] = useState<UserRatingItem[]>([]);
  const [selectedRatingPlace, setSelectedRatingPlace] = useState('PLC_0001');
  const [starCount, setStarCount] = useState(5);
  const [ratingFeedback, setRatingFeedback] = useState('Breathtaking lake views and intricate royal architecture.');
  const [statusMessage, setStatusMessage] = useState<string | null>(null);
  const [isSaving, setIsSaving] = useState(false);

  const showStatus = (msg: string) => {
    setStatusMessage(msg);
    setTimeout(() => setStatusMessage(null), 3500);
  };

  // Load profile & history on open
  useEffect(() => {
    if (isOpen) {
      loadHistory();
      loadRatings();
    }
  }, [isOpen]);

  const loadHistory = async () => {
    try {
      const trips = await api.getUserTripHistory(userProfile.user_id);
      setSavedTrips(trips);
    } catch (e) {
      console.warn('Could not load history:', e);
    }
  };

  const loadRatings = async () => {
    try {
      const ratings = await api.getUserRatings(userProfile.user_id);
      setUserRatings(ratings);
    } catch (e) {
      console.warn('Could not load ratings:', e);
    }
  };

  const handleLoginOrSwitch = async () => {
    if (!usernameInput.trim()) return;
    setIsSaving(true);
    try {
      const loggedIn = await api.loginUser(usernameInput.trim());
      setUserProfile(loggedIn);
      showStatus(`Logged in as ${loggedIn.username}! Profile synchronized.`);
      loadHistory();
      loadRatings();
    } catch (err: any) {
      showStatus('Login failed: ' + err.message);
    } finally {
      setIsSaving(false);
    }
  };

  const handleSavePreferences = async () => {
    setIsSaving(true);
    try {
      const updated = await api.updateUserProfile(userProfile.user_id, {
        budget_level: userProfile.budget_level,
        pace_preference: userProfile.pace_preference,
        preferences: userProfile.preferences
      });
      setUserProfile(prev => ({ ...prev, ...updated }));
      showStatus('Travel preferences updated! Recommendation models updated.');
    } catch (err: any) {
      showStatus('Save error: ' + err.message);
    } finally {
      setIsSaving(false);
    }
  };

  const handleSaveCurrentTrip = async () => {
    if (!currentTrip) return;
    setIsSaving(true);
    try {
      const res = await api.saveTripToHistory(
        userProfile.user_id,
        currentTrip.trip_id,
        `${currentTrip.destination} (${currentTrip.chosen_itinerary.days.length} Days)`
      );
      setSavedTrips(prev => [res, ...prev]);
      showStatus(`Trip to ${currentTrip.destination} saved to travel history!`);
    } catch (err: any) {
      showStatus('Save trip failed: ' + err.message);
    } finally {
      setIsSaving(false);
    }
  };

  const handleReuseTrip = async (tripId: string) => {
    try {
      const loaded = await api.reuseTrip(tripId);
      onLoadTrip(loaded);
      showStatus(`Loaded ${loaded.destination} trip!`);
      onClose();
    } catch (err: any) {
      showStatus('Could not load trip from database cache.');
    }
  };

  const handleSubmitRating = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await api.submitPlaceRating(
        userProfile.user_id,
        selectedRatingPlace,
        starCount,
        ratingFeedback
      );
      showStatus(`Recorded ${starCount}★ rating for ${selectedRatingPlace}! Feeds into SVD collaborative matrix.`);
      setRatingFeedback('');
      loadRatings();
    } catch (err: any) {
      showStatus('Rating submission failed: ' + err.message);
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 bg-black/70 backdrop-blur-sm animate-fadeIn">
      <div className="bg-[#0b1325] border border-slate-800 w-full max-w-3xl max-h-[90vh] rounded-3xl shadow-2xl flex flex-col overflow-hidden">
        
        {/* Header */}
        <div className="px-6 py-4 bg-slate-950/90 border-b border-slate-800 flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <div className="w-10 h-10 rounded-2xl bg-teal-500/15 border border-teal-500/30 flex items-center justify-center text-teal-400 font-bold">
              <User className="w-5 h-5" />
            </div>
            <div>
              <div className="flex items-center space-x-2">
                <h3 className="font-bold text-base text-white">Traveler Profile & History</h3>
                <span className="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-teal-500/15 text-teal-300 border border-teal-500/30">
                  TRAVELMATE AI
                </span>
              </div>
              <p className="text-xs text-slate-400">{userProfile.username} ({userProfile.user_id})</p>
            </div>
          </div>

          <button
            onClick={onClose}
            className="w-8 h-8 rounded-full bg-slate-900 hover:bg-slate-800 text-slate-400 hover:text-white flex items-center justify-center transition cursor-pointer"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Status notification toast */}
        {statusMessage && (
          <div className="bg-teal-500 text-slate-950 px-4 py-2.5 text-xs font-bold flex items-center justify-center space-x-2">
            <CheckCircle2 className="w-4 h-4" />
            <span>{statusMessage}</span>
          </div>
        )}

        {/* Tab Navigation */}
        <div className="flex items-center space-x-2 px-6 pt-3 border-b border-slate-800/80 bg-slate-950/40">
          <button
            onClick={() => setActiveTab('profile')}
            className={`px-4 py-2.5 text-xs font-bold transition flex items-center space-x-2 cursor-pointer border-b-2 ${
              activeTab === 'profile'
                ? 'border-teal-400 text-teal-300'
                : 'border-transparent text-slate-400 hover:text-white'
            }`}
          >
            <Sliders className="w-3.5 h-3.5" />
            <span>Preferences & Auth</span>
          </button>

          <button
            onClick={() => setActiveTab('history')}
            className={`px-4 py-2.5 text-xs font-bold transition flex items-center space-x-2 cursor-pointer border-b-2 ${
              activeTab === 'history'
                ? 'border-teal-400 text-teal-300'
                : 'border-transparent text-slate-400 hover:text-white'
            }`}
          >
            <History className="w-3.5 h-3.5" />
            <span>Travel History ({savedTrips.length})</span>
          </button>

          <button
            onClick={() => setActiveTab('ratings')}
            className={`px-4 py-2.5 text-xs font-bold transition flex items-center space-x-2 cursor-pointer border-b-2 ${
              activeTab === 'ratings'
                ? 'border-teal-400 text-teal-300'
                : 'border-transparent text-slate-400 hover:text-white'
            }`}
          >
            <Star className="w-3.5 h-3.5" />
            <span>Attraction Ratings ({userRatings.length})</span>
          </button>
        </div>

        {/* Content Body */}
        <div className="flex-1 overflow-y-auto p-6 space-y-6">
          
          {/* TAB 1: Profile & Preferences */}
          {activeTab === 'profile' && (
            <div className="space-y-6">
              {/* Login / Switch Account Bar */}
              <div className="bg-slate-900/90 border border-slate-800 p-4 rounded-2xl flex flex-col sm:flex-row items-center justify-between gap-3 text-xs">
                <div>
                  <span className="text-slate-400 block font-semibold">Active Traveler Identity</span>
                  <span className="text-white font-bold text-sm">{userProfile.username}</span>
                  <span className="text-slate-500 block">{userProfile.email}</span>
                </div>

                <div className="flex items-center gap-2 w-full sm:w-auto">
                  <input
                    type="text"
                    value={usernameInput}
                    onChange={(e) => setUsernameInput(e.target.value)}
                    placeholder="Switch username..."
                    className="bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-xs text-white focus:outline-none focus:border-teal-400 flex-1 sm:w-44"
                  />
                  <button
                    onClick={handleLoginOrSwitch}
                    disabled={isSaving}
                    className="bg-teal-500 hover:bg-teal-400 text-slate-950 font-bold px-3 py-2 rounded-xl text-xs transition cursor-pointer"
                  >
                    Switch
                  </button>
                </div>
              </div>

              {/* Standard Travel Parameters */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div className="space-y-1.5 text-xs">
                  <label className="font-bold text-slate-300 uppercase tracking-wider">Default Pace Preference</label>
                  <select
                    value={userProfile.pace_preference}
                    onChange={(e) => setUserProfile({ ...userProfile, pace_preference: e.target.value })}
                    className="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2.5 text-xs text-white focus:outline-none focus:border-teal-400"
                  >
                    <option value="relaxed">Relaxed (3 stops/day, leisurely)</option>
                    <option value="moderate">Moderate (4 stops/day, balanced)</option>
                    <option value="packed">Packed (5-6 stops/day, active exploration)</option>
                  </select>
                </div>

                <div className="space-y-1.5 text-xs">
                  <label className="font-bold text-slate-300 uppercase tracking-wider">Default Budget Level</label>
                  <select
                    value={userProfile.budget_level}
                    onChange={(e) => setUserProfile({ ...userProfile, budget_level: e.target.value })}
                    className="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2.5 text-xs text-white focus:outline-none focus:border-teal-400"
                  >
                    <option value="low">Economy / Budget Saver</option>
                    <option value="medium">Standard Comfort</option>
                    <option value="luxury">Luxury Heritage & Experiences</option>
                  </select>
                </div>
              </div>

              {/* Category Affinity Sliders */}
              <div className="space-y-3">
                <div className="flex justify-between items-center">
                  <h4 className="text-xs font-bold text-white uppercase tracking-wider flex items-center gap-1.5">
                    <Sliders className="w-3.5 h-3.5 text-teal-400" />
                    <span>Personal Category Interest Weights</span>
                  </h4>
                  <span className="text-[11px] text-slate-400">Used by TF-IDF & LightGBM ranking</span>
                </div>

                <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  {CATEGORIES.map(cat => {
                    const val = userProfile.preferences[cat.key] || 0.5;
                    return (
                      <div key={cat.key} className="bg-slate-950 p-3 rounded-xl border border-slate-800 space-y-1.5">
                        <div className="flex justify-between items-center text-xs">
                          <span className="text-slate-300 font-medium">{cat.label}</span>
                          <span className="text-teal-400 font-bold font-mono">{(val * 100).toFixed(0)}%</span>
                        </div>
                        <input
                          type="range"
                          min="0"
                          max="1"
                          step="0.05"
                          value={val}
                          onChange={(e) => {
                            const newPrefs = { ...userProfile.preferences, [cat.key]: parseFloat(e.target.value) };
                            setUserProfile({ ...userProfile, preferences: newPrefs });
                          }}
                          className="w-full accent-teal-400 bg-slate-900"
                        />
                      </div>
                    );
                  })}
                </div>
              </div>

              <div className="flex justify-end pt-2">
                <button
                  onClick={handleSavePreferences}
                  disabled={isSaving}
                  className="bg-gradient-to-r from-teal-500 to-emerald-500 hover:from-teal-400 hover:to-emerald-400 text-slate-950 font-bold px-5 py-2.5 rounded-xl text-xs flex items-center gap-2 cursor-pointer shadow-lg shadow-teal-500/20"
                >
                  <Save className="w-4 h-4 text-slate-950" />
                  <span>Save Preferences & Update Models</span>
                </button>
              </div>
            </div>
          )}

          {/* TAB 2: Travel History & Saved Trips */}
          {activeTab === 'history' && (
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <div>
                  <h4 className="font-bold text-white text-sm">Past Generated & Completed Trips</h4>
                  <p className="text-xs text-slate-400">View, reuse or edit previous itineraries synthesized by NSGA-II.</p>
                </div>

                {currentTrip && (
                  <button
                    onClick={handleSaveCurrentTrip}
                    disabled={isSaving}
                    className="bg-teal-500 hover:bg-teal-400 text-slate-950 font-bold px-3 py-2 rounded-xl text-xs flex items-center gap-1.5 cursor-pointer shadow-md"
                  >
                    <Save className="w-3.5 h-3.5" />
                    <span>Bookmark Active Trip</span>
                  </button>
                )}
              </div>

              {savedTrips.length > 0 ? (
                <div className="space-y-3">
                  {savedTrips.map((trip) => (
                    <div
                      key={trip.id}
                      className="bg-slate-900/90 border border-slate-800 hover:border-slate-700 p-4 rounded-2xl flex flex-col sm:flex-row sm:items-center justify-between gap-4 transition shadow-md"
                    >
                      <div className="space-y-1">
                        <div className="flex items-center space-x-2">
                          <h5 className="font-bold text-white text-sm">{trip.name}</h5>
                          <span className="px-2 py-0.5 rounded-full text-[10px] bg-teal-500/10 text-teal-400 border border-teal-500/20 font-semibold">
                            {trip.destination}
                          </span>
                        </div>
                        <p className="text-xs text-slate-400 flex items-center gap-3">
                          <span>📅 {trip.days_count} Days</span>
                          <span>💰 ₹{Math.round(trip.total_cost).toLocaleString()}</span>
                          <span>⭐ Feasibility: {trip.feasibility}%</span>
                        </p>
                        <p className="text-[11px] text-slate-500">Saved: {trip.saved_at}</p>
                      </div>

                      <div className="flex items-center space-x-2">
                        <button
                          onClick={() => handleReuseTrip(trip.trip_id)}
                          className="bg-slate-800 hover:bg-teal-500 hover:text-slate-950 text-slate-200 px-3 py-2 rounded-xl text-xs font-bold transition flex items-center gap-1.5 cursor-pointer"
                        >
                          <RefreshCw className="w-3 h-3" />
                          <span>Load & Reuse</span>
                        </button>
                      </div>
                    </div>
                  ))}
                </div>
              ) : (
                <div className="text-center py-10 text-slate-500 text-xs">
                  No saved trips yet. Generate an itinerary and click "Bookmark Active Trip" to save it here!
                </div>
              )}
            </div>
          )}

          {/* TAB 3: Visited Places & Feedback Ratings */}
          {activeTab === 'ratings' && (
            <div className="space-y-6">
              <div>
                <h4 className="font-bold text-white text-sm">Rate Visited Tourist Attractions</h4>
                <p className="text-xs text-slate-400">
                  Your feedback directly updates the TruncatedSVD collaborative filtering matrix factorizer, improving personalization accuracy for future trips.
                </p>
              </div>

              {/* Rating Form */}
              <form onSubmit={handleSubmitRating} className="bg-slate-900/90 border border-slate-800 p-4 rounded-2xl space-y-4">
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                  <div className="space-y-1.5 text-xs">
                    <label className="font-bold text-slate-300">Select Attraction</label>
                    <select
                      value={selectedRatingPlace}
                      onChange={(e) => setSelectedRatingPlace(e.target.value)}
                      className="w-full bg-slate-950 border border-slate-800 rounded-xl px-3 py-2.5 text-xs text-white focus:outline-none focus:border-teal-400"
                    >
                      <option value="PLC_0001">City Palace Complex (Udaipur)</option>
                      <option value="PLC_0002">Lake Pichola Boating & Jagmandir (Udaipur)</option>
                      <option value="PLC_0003">Jagdish Temple (Udaipur)</option>
                      <option value="PLC_0004">Saheliyon Ki Bari Royal Gardens (Udaipur)</option>
                      <option value="PLC_0005">Bagore Ki Haveli Cultural Museum (Udaipur)</option>
                      <option value="PLC_0006">Monsoon Palace Sajjangarh (Udaipur)</option>
                      <option value="PLC_0010">Amber Fort & Palace (Jaipur)</option>
                      <option value="PLC_0011">Hawa Mahal Palace of Winds (Jaipur)</option>
                      <option value="PLC_0012">Jantar Mantar Royal Observatory (Jaipur)</option>
                    </select>
                  </div>

                  <div className="space-y-1.5 text-xs">
                    <label className="font-bold text-slate-300">Star Rating</label>
                    <div className="flex items-center space-x-2 pt-1.5">
                      {[1, 2, 3, 4, 5].map((star) => (
                        <button
                          type="button"
                          key={star}
                          onClick={() => setStarCount(star)}
                          className={`text-xl transition cursor-pointer ${
                            star <= starCount ? 'text-amber-400 scale-110' : 'text-slate-700 hover:text-amber-200'
                          }`}
                        >
                          ★
                        </button>
                      ))}
                      <span className="text-amber-400 font-bold ml-2">{starCount}.0 / 5.0</span>
                    </div>
                  </div>
                </div>

                <div className="space-y-1.5 text-xs">
                  <label className="font-bold text-slate-300">Visitor Feedback / Review</label>
                  <input
                    type="text"
                    value={ratingFeedback}
                    onChange={(e) => setRatingFeedback(e.target.value)}
                    placeholder="Share visiting advice or feedback..."
                    className="w-full bg-slate-950 border border-slate-800 rounded-xl px-4 py-2.5 text-xs text-white focus:outline-none focus:border-teal-400"
                  />
                </div>

                <div className="flex justify-end">
                  <button
                    type="submit"
                    className="bg-teal-500 hover:bg-teal-400 text-slate-950 font-bold px-4 py-2 rounded-xl text-xs transition cursor-pointer flex items-center gap-1.5"
                  >
                    <Star className="w-3.5 h-3.5" />
                    <span>Submit Attraction Rating</span>
                  </button>
                </div>
              </form>

              {/* Previous Ratings Table */}
              <div className="space-y-2">
                <h5 className="font-bold text-xs text-slate-300 uppercase tracking-wider">Your Recorded Ratings</h5>
                {userRatings.length > 0 ? (
                  <div className="bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden">
                    <table className="w-full text-left text-xs text-slate-300">
                      <thead className="bg-slate-950 text-slate-400 text-[11px] uppercase">
                        <tr>
                          <th className="py-2.5 px-4">Place ID</th>
                          <th className="py-2.5 px-4">Rating</th>
                          <th className="py-2.5 px-4">Recorded Date</th>
                        </tr>
                      </thead>
                      <tbody className="divide-y divide-slate-800/60">
                        {userRatings.map((r, idx) => (
                          <tr key={idx} className="hover:bg-slate-800/30">
                            <td className="py-2.5 px-4 font-bold text-white">{r.place_id}</td>
                            <td className="py-2.5 px-4 text-amber-400 font-bold">★ {r.rating}</td>
                            <td className="py-2.5 px-4 text-slate-400">{r.timestamp ? r.timestamp.slice(0, 10) : 'Today'}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                ) : (
                  <p className="text-xs text-slate-500">No ratings submitted yet.</p>
                )}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
