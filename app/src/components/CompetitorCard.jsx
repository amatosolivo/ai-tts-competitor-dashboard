import React from 'react';
import { ExternalLink, TrendingUp, DollarSign, Cpu } from 'lucide-react';
import { motion } from 'framer-motion';

const CompetitorCard = ({ competitor, onClick }) => {
    const { metadata, scores, pricing, capabilities } = competitor;

    return (
        <motion.div
            layoutId={`card-${metadata.name}`}
            onClick={onClick}
            className="bento-card group flex flex-col justify-between"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            whileHover={{ y: -5, scale: 1.01 }}
        >
            <div>
                <div className="flex justify-between items-start mb-4">
                    <div className="bg-slate-50 p-3 rounded-2xl group-hover:bg-apple-accent/5 transition-colors">
                        <Cpu className="w-6 h-6 text-slate-400 group-hover:text-apple-accent transition-colors" />
                    </div>
                    <span className={`text-[10px] font-bold uppercase tracking-wider px-2 py-1 rounded-full ${metadata.status === 'discovery_complete' ? 'bg-emerald-50 text-emerald-600' : 'bg-amber-50 text-amber-600'
                        }`}>
                        {metadata.status.replace('_', ' ')}
                    </span>
                </div>

                <h3 className="text-xl font-bold text-apple-text mb-1">{metadata.name}</h3>
                <p className="text-sm text-slate-500 mb-6 truncate">{metadata.homepage}</p>

                <div className="space-y-4">
                    <div>
                        <div className="flex justify-between text-xs font-medium text-slate-400 mb-1.5">
                            <span>Innovation</span>
                            <span>{scores.innovation || 0}/10</span>
                        </div>
                        <div className="h-1.5 w-full bg-slate-100 rounded-full overflow-hidden">
                            <motion.div
                                initial={{ width: 0 }}
                                animate={{ width: `${(scores.innovation || 0) * 10}%` }}
                                className="h-full bg-apple-accent rounded-full"
                            />
                        </div>
                    </div>

                    <div>
                        <div className="flex justify-between text-xs font-medium text-slate-400 mb-1.5">
                            <span>Affordability</span>
                            <span>{scores.affordability || 0}/10</span>
                        </div>
                        <div className="h-1.5 w-full bg-slate-100 rounded-full overflow-hidden">
                            <motion.div
                                initial={{ width: 0 }}
                                animate={{ width: `${(scores.affordability || 0) * 10}%` }}
                                className="h-full bg-emerald-500 rounded-full"
                            />
                        </div>
                    </div>
                </div>
            </div>

            <div className="mt-8 pt-4 border-t border-slate-50 flex items-center justify-between text-slate-400 group-hover:text-apple-accent transition-colors">
                <span className="text-xs font-medium">View Analysis</span>
                <ExternalLink className="w-4 h-4" />
            </div>
        </motion.div>
    );
};

export default CompetitorCard;
