import React, { useState } from 'react';
import CompetitorCard from './CompetitorCard';
import { Search, Filter, SlidersHorizontal, ChevronRight, X, TrendingUp, Cpu } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import data from '../data/data.json';

const Dashboard = () => {
    const [selectedComp, setSelectedComp] = useState(null);
    const [search, setSearch] = useState('');

    const competitors = data.competitors.filter(c =>
        c.metadata.name.toLowerCase().includes(search.toLowerCase())
    );

    return (
        <div className="min-h-screen bg-apple-bg pt-20 pb-20 px-6 sm:px-10">
            {/* Header */}
            <nav className="fixed top-6 left-6 right-6 h-16 glass rounded-full z-50 px-6 flex items-center justify-between shadow-sm">
                <div className="flex items-center gap-3">
                    <div className="w-8 h-8 bg-apple-accent rounded-lg flex items-center justify-center">
                        <TrendingUp className="text-white w-5 h-5" />
                    </div>
                    <span className="font-bold text-lg tracking-tight">Competitor Intelligence</span>
                </div>

                <div className="hidden md:flex items-center bg-slate-100/50 rounded-full px-4 py-2 w-96 border border-slate-200/50 focus-within:bg-white focus-within:border-apple-accent/30 transition-all">
                    <Search className="w-4 h-4 text-slate-400 mr-2" />
                    <input
                        type="text"
                        placeholder="Search market leaders..."
                        className="bg-transparent border-none outline-none text-sm w-full"
                        value={search}
                        onChange={(e) => setSearch(e.target.value)}
                    />
                </div>

                <div className="flex items-center gap-3 text-slate-500 font-medium text-sm">
                    <button className="p-2 hover:bg-white rounded-full transition-colors">
                        <SlidersHorizontal className="w-5 h-5" />
                    </button>
                </div>
            </nav>

            {/* Main Content */}
            <div className="max-w-7xl mx-auto">
                <header className="mb-12 flex flex-col md:flex-row md:items-end justify-between gap-6">
                    <div>
                        <div className="flex items-center gap-2 text-apple-accent font-bold text-xs uppercase tracking-widest mb-3">
                            <span className="w-2 h-2 rounded-full bg-apple-accent animate-pulse" />
                            Live Autonomous Market Scan
                        </div>
                        <h1 className="text-4xl md:text-5xl font-bold text-apple-text tracking-tight mb-4">
                            AI Text-to-Speech
                        </h1>
                        <p className="text-slate-500 max-w-xl text-lg leading-relaxed">
                            Real-time competitive landscape analyzer tracking features, pricing, and maturity across the neural synthesis market.
                        </p>
                    </div>
                    <div className="flex gap-2">
                        <button className="px-5 py-2.5 bg-white border border-slate-200 rounded-xl text-sm font-semibold hover:border-apple-accent transition-colors">Compare All</button>
                        <button className="px-5 py-2.5 bg-apple-accent text-white rounded-xl text-sm font-semibold shadow-lg shadow-blue-500/25 hover:opacity-90 transition-opacity">Export Repo</button>
                    </div>
                </header>

                {/* Bento Grid */}
                <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
                    {competitors.map((comp) => (
                        <CompetitorCard
                            key={comp.metadata.homepage}
                            competitor={comp}
                            onClick={() => setSelectedComp(comp)}
                        />
                    ))}
                </div>
            </div>

            {/* Detail Overlay */}
            <AnimatePresence>
                {selectedComp && (
                    <div className="fixed inset-0 z-[100] flex items-center justify-center p-6">
                        <motion.div
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            exit={{ opacity: 0 }}
                            onClick={() => setSelectedComp(null)}
                            className="absolute inset-0 bg-slate-900/40 backdrop-blur-sm"
                        />
                        <motion.div
                            layoutId={`card-${selectedComp.metadata.name}`}
                            className="relative w-full max-w-4xl bg-white rounded-[32px] shadow-2xl overflow-hidden max-h-[90vh] flex flex-col"
                        >
                            <button
                                onClick={() => setSelectedComp(null)}
                                className="absolute top-6 right-6 p-2 bg-slate-100 hover:bg-slate-200 rounded-full z-10 transition-colors"
                            >
                                <X className="w-5 h-5 text-slate-500" />
                            </button>

                            <div className="p-10 overflow-y-auto">
                                <div className="flex items-center gap-4 mb-8">
                                    <div className="w-16 h-16 bg-slate-50 rounded-2xl flex items-center justify-center">
                                        <Cpu className="w-8 h-8 text-apple-accent" />
                                    </div>
                                    <div>
                                        <h2 className="text-3xl font-bold mb-1">{selectedComp.metadata.name}</h2>
                                        <p className="text-slate-400 font-medium">{selectedComp.metadata.homepage}</p>
                                    </div>
                                </div>

                                <div className="grid md:grid-cols-2 gap-10 mb-10">
                                    <div className="bg-slate-50 rounded-3xl p-8 border border-slate-100">
                                        <h4 className="text-sm font-bold text-slate-400 uppercase tracking-widest mb-6 border-b border-slate-200 pb-2">Analysis Stats</h4>
                                        <div className="space-y-6">
                                            {Object.entries(selectedComp.scores).map(([key, val]) => (
                                                <div key={key}>
                                                    <div className="flex justify-between text-sm font-bold mb-2 capitalize">
                                                        <span>{key} Score</span>
                                                        <span>{val}/10</span>
                                                    </div>
                                                    <div className="h-2 w-full bg-slate-200 rounded-full overflow-hidden">
                                                        <motion.div
                                                            initial={{ width: 0 }}
                                                            animate={{ width: `${val * 10}%` }}
                                                            className="h-full bg-apple-accent"
                                                        />
                                                    </div>
                                                </div>
                                            ))}
                                            {Object.keys(selectedComp.scores).length === 0 && (
                                                <p className="text-slate-400 italic text-sm">Waiting for Phase B scraping data...</p>
                                            )}
                                        </div>
                                    </div>

                                    <div className="bg-slate-50 rounded-3xl p-8 border border-slate-100">
                                        <h4 className="text-sm font-bold text-slate-400 uppercase tracking-widest mb-6 border-b border-slate-200 pb-2">Discovered Pages</h4>
                                        <div className="flex flex-wrap gap-2">
                                            {selectedComp.discovery.relevant_pages.length > 0 ? (
                                                selectedComp.discovery.relevant_pages.slice(0, 10).map((page, i) => (
                                                    <div key={i} className="px-3 py-1.5 bg-white border border-slate-200 rounded-lg text-xs font-semibold text-slate-600 truncate max-w-[200px]">
                                                        {page.split('/').pop() || 'index'}
                                                    </div>
                                                ))
                                            ) : (
                                                <p className="text-slate-400 italic text-sm">No internal pages identified yet.</p>
                                            )}
                                        </div>
                                    </div>
                                </div>

                                <div className="bg-emerald-50 rounded-3xl p-8 border border-emerald-100 flex items-center justify-between">
                                    <div>
                                        <h4 className="font-bold text-emerald-900 mb-1">Scraping Status</h4>
                                        <p className="text-emerald-700/80 text-sm font-medium">Auto-discovery complete. Data normalization pending Phase C.</p>
                                    </div>
                                    <button className="px-6 py-3 bg-emerald-600 text-white rounded-2xl font-bold shadow-lg shadow-emerald-600/20 hover:bg-emerald-700 transition-colors">Trigger Re-crawl</button>
                                </div>
                            </div>
                        </motion.div>
                    </div>
                )}
            </AnimatePresence>
        </div>
    );
};

export default Dashboard;
