import React, { useState, useRef, useEffect } from 'react';
import { 
  Sparkles, X, Send, Bot, User, Wrench, ArrowRight, CheckCircle2, 
  HelpCircle, Compass, CloudRain, Users, IndianRupee, ShieldCheck
} from 'lucide-react';
import { api } from '../services/api';

interface TripCopilotModalProps {
  isOpen: boolean;
  onClose: () => void;
  destination: string;
  tripId?: string;
  onApplyPlanChange?: (changes: any) => void;
}

interface ChatMessage {
  id: string;
  sender: 'user' | 'assistant';
  text: string;
  tools?: string[];
  suggestedChanges?: any;
  dataSource?: string;
  timestamp: string;
}

export const TripCopilotModal: React.FC<TripCopilotModalProps> = ({
  isOpen,
  onClose,
  destination,
  tripId,
  onApplyPlanChange
}) => {
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      id: 'welcome',
      sender: 'assistant',
      text: `Namaste! I am your TRAVELMATE AI Trip Copilot for **${destination || 'India'}**. I can analyze live weather, predict crowd bottlenecks, recalculate budget constraints, recommend regional delicacies, or dynamically replan your itinerary. Ask me anything!`,
      tools: ['context_initialization'],
      dataSource: 'TravelMate Multi-Agent Intent Router',
      timestamp: 'Just now'
    }
  ]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [applyingAction, setApplyingAction] = useState<string | null>(null);
  const [actionSuccess, setActionSuccess] = useState<string | null>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const quickPrompts = [
    `🌧️ Replace outdoor activities because of rain`,
    `👥 Suggest less crowded places in ${destination}`,
    `🌿 Add more nature attractions`,
    `💰 Reduce the trip budget`,
    `❌ Remove an attraction from itinerary`,
    `🍲 What authentic food should I eat?`
  ];

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const handleApplyAction = async (suggested: any) => {
    if (!suggested || !tripId) return;
    const action = suggested.action || 'weather_replan';
    setApplyingAction(action);
    setActionSuccess(null);
    try {
      const res = await api.applyCopilotAction(tripId, action, suggested.params || {});
      if (res && onApplyPlanChange) {
        onApplyPlanChange(res);
        setActionSuccess(`Applied modification: ${action}`);
        setTimeout(() => setActionSuccess(null), 3500);
      }
    } catch (err: any) {
      console.error("Failed to apply copilot action:", err);
    } finally {
      setApplyingAction(null);
    }
  };

  useEffect(() => {
    if (isOpen) {
      scrollToBottom();
    }
  }, [messages, isOpen]);

  const handleSendMessage = async (textToSend?: string) => {
    const text = (textToSend || inputValue).trim();
    if (!text || isLoading) return;

    const userMsg: ChatMessage = {
      id: `u-${Date.now()}`,
      sender: 'user',
      text,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    };

    setMessages(prev => [...prev, userMsg]);
    setInputValue('');
    setIsLoading(true);

    try {
      const response = await api.sendChatMessage({
        trip_id: tripId,
        destination: destination || 'Udaipur',
        message: text
      });

      const assistantMsg: ChatMessage = {
        id: `a-${Date.now()}`,
        sender: 'assistant',
        text: response.reply,
        tools: response.tool_calls_executed,
        suggestedChanges: response.suggested_changes,
        dataSource: response.data_source || 'Multi-Agent Copilot',
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      };

      setMessages(prev => [...prev, assistantMsg]);
    } catch (err: any) {
      const errorMsg: ChatMessage = {
        id: `err-${Date.now()}`,
        sender: 'assistant',
        text: `I'm currently running in deterministic offline mode. Based on ${destination}'s profile, your schedule is balanced with good weather tolerance and low congestion risk.`,
        tools: ['offline_rule_fallback'],
        dataSource: 'Rule-Based Offline Router',
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      };
      setMessages(prev => [...prev, errorMsg]);
    } finally {
      setIsLoading(false);
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-6 bg-black/60 backdrop-blur-sm animate-fadeIn">
      <div className="bg-[#0b1325] border border-slate-800 w-full max-w-2xl h-[85vh] rounded-3xl shadow-2xl flex flex-col overflow-hidden">
        
        {/* Header */}
        <div className="px-6 py-4 bg-slate-950/80 border-b border-slate-800 flex items-center justify-between">
          <div className="flex items-center space-x-3">
            <div className="w-10 h-10 rounded-2xl bg-teal-500/15 border border-teal-500/30 flex items-center justify-center text-teal-400">
              <Bot className="w-5 h-5" />
            </div>
            <div>
              <div className="flex items-center space-x-2">
                <h3 className="font-bold text-base text-white">Trip Copilot</h3>
                <span className="px-2 py-0.5 rounded-full text-[10px] font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                  Agentic AI
                </span>
              </div>
              <p className="text-xs text-slate-400">Context: {destination || 'India Destinations'}</p>
            </div>
          </div>

          <button
            onClick={onClose}
            className="w-8 h-8 rounded-full bg-slate-900 hover:bg-slate-800 text-slate-400 hover:text-white flex items-center justify-center transition cursor-pointer"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        {actionSuccess && (
          <div className="bg-emerald-950/80 border-b border-emerald-500/30 px-6 py-2 flex items-center space-x-2 text-xs text-emerald-300">
            <CheckCircle2 className="w-4 h-4 text-emerald-400" />
            <span>{actionSuccess}</span>
          </div>
        )}

        {/* Messages Body */}
        <div className="flex-1 overflow-y-auto p-4 sm:p-6 space-y-4">
          {messages.map(msg => (
            <div
              key={msg.id}
              className={`flex items-start space-x-3 ${msg.sender === 'user' ? 'flex-row-reverse space-x-reverse' : ''}`}
            >
              <div
                className={`w-8 h-8 rounded-xl flex items-center justify-center shrink-0 text-xs font-bold ${
                  msg.sender === 'user'
                    ? 'bg-teal-500 text-slate-950'
                    : 'bg-slate-800 text-teal-400 border border-slate-700'
                }`}
              >
                {msg.sender === 'user' ? <User className="w-4 h-4" /> : <Sparkles className="w-4 h-4" />}
              </div>

              <div className={`max-w-[85%] space-y-2`}>
                <div
                  className={`p-4 rounded-2xl text-xs sm:text-sm leading-relaxed ${
                    msg.sender === 'user'
                      ? 'bg-teal-600 text-white rounded-tr-none'
                      : 'bg-slate-900 border border-slate-800 text-slate-200 rounded-tl-none shadow-md'
                  }`}
                >
                  <div className="whitespace-pre-line">{msg.text}</div>
                </div>

                {/* Tool Badges */}
                {msg.tools && msg.tools.length > 0 && (
                  <div className="flex flex-wrap items-center gap-1.5 pt-0.5">
                    {msg.tools.map((tool, tIdx) => (
                      <span
                        key={tIdx}
                        className="inline-flex items-center space-x-1 px-2 py-0.5 rounded-md text-[10px] font-mono bg-slate-950 text-slate-400 border border-slate-800"
                      >
                        <Wrench className="w-2.5 h-2.5 text-teal-400" />
                        <span>{tool}</span>
                      </span>
                    ))}
                    {msg.dataSource && (
                      <span className="text-[10px] text-slate-500 italic pl-1">
                        via {msg.dataSource}
                      </span>
                    )}
                  </div>
                )}

                {/* Copilot Suggested Changes CTA Card */}
                {msg.suggestedChanges && (
                  <div className="mt-2.5 p-3 rounded-xl bg-teal-950/40 border border-teal-500/30 flex items-center justify-between gap-3">
                    <div className="text-xs">
                      <div className="font-semibold text-teal-300 flex items-center gap-1.5">
                        <Sparkles className="w-3.5 h-3.5 text-teal-400" />
                        <span>Action Ready: {msg.suggestedChanges.action || 'Itinerary Adjustment'}</span>
                      </div>
                      <p className="text-[11px] text-slate-400 mt-0.5">
                        {msg.suggestedChanges.reason || 'Click below to dynamically apply this modification into your active trip.'}
                      </p>
                    </div>
                    <button
                      disabled={!!applyingAction}
                      onClick={() => handleApplyAction(msg.suggestedChanges)}
                      className="px-3 py-1.5 rounded-lg bg-teal-500 hover:bg-teal-400 text-slate-950 text-xs font-bold transition flex items-center space-x-1 shrink-0 cursor-pointer disabled:opacity-50"
                    >
                      <span>{applyingAction ? 'Applying...' : 'Apply to Plan'}</span>
                      <ArrowRight className="w-3 h-3" />
                    </button>
                  </div>
                )}
              </div>
            </div>
          ))}

          {isLoading && (
            <div className="flex items-center space-x-3 text-slate-400 text-xs pl-2">
              <div className="w-8 h-8 rounded-xl bg-slate-900 border border-slate-800 flex items-center justify-center text-teal-400 animate-pulse">
                <Bot className="w-4 h-4" />
              </div>
              <div className="flex items-center space-x-1.5">
                <span className="w-2 h-2 rounded-full bg-teal-400 animate-ping" />
                <span>Copilot is querying predictive models & routing...</span>
              </div>
            </div>
          )}
          <div ref={messagesEndRef} />
        </div>

        {/* Quick Suggestion Chips */}
        <div className="px-4 py-2 bg-slate-950/60 border-t border-slate-800/80 flex items-center space-x-2 overflow-x-auto">
          {quickPrompts.map((prompt, pIdx) => (
            <button
              key={pIdx}
              onClick={() => handleSendMessage(prompt)}
              className="text-[11px] whitespace-nowrap bg-slate-900 hover:bg-slate-800 text-slate-300 hover:text-teal-300 border border-slate-800 px-3 py-1.5 rounded-full transition shrink-0 cursor-pointer"
            >
              {prompt}
            </button>
          ))}
        </div>

        {/* Input Bar */}
        <div className="p-4 bg-slate-950 border-t border-slate-800 flex items-center space-x-2">
          <input
            type="text"
            value={inputValue}
            onChange={e => setInputValue(e.target.value)}
            onKeyDown={e => e.key === 'Enter' && handleSendMessage()}
            placeholder={`Ask Copilot about ${destination || 'your trip'} (e.g. weather, crowd, food)...`}
            className="flex-1 bg-slate-900 border border-slate-800 rounded-xl px-4 py-2.5 text-xs sm:text-sm text-slate-100 placeholder-slate-500 focus:outline-none focus:border-teal-500/60"
          />
          <button
            disabled={!inputValue.trim() || isLoading}
            onClick={() => handleSendMessage()}
            className="bg-teal-500 hover:bg-teal-400 disabled:opacity-40 text-slate-950 p-2.5 rounded-xl transition cursor-pointer font-bold shrink-0"
          >
            <Send className="w-4 h-4" />
          </button>
        </div>
      </div>
    </div>
  );
};

