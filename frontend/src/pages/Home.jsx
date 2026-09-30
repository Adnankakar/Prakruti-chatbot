import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { Leaf, Brain, Activity, ChevronRight, ShieldAlert } from 'lucide-react'
import Logo from '../components/common/Logo'
import Button from '../components/common/Button'
import { useAssessment } from '../context/AssessmentContext'

const DOSHAS = [
  {
    name: 'Vata',
    color: 'bg-sky-50 border-sky-200',
    accent: 'text-sky-700',
    dot: 'bg-sky-400',
    desc: 'Associated with movement, creativity, and lightness.',
  },
  {
    name: 'Pitta',
    color: 'bg-orange-50 border-orange-200',
    accent: 'text-orange-700',
    dot: 'bg-orange-400',
    desc: 'Associated with transformation, focus, and intensity.',
  },
  {
    name: 'Kapha',
    color: 'bg-emerald-50 border-emerald-200',
    accent: 'text-emerald-700',
    dot: 'bg-emerald-400',
    desc: 'Associated with stability, endurance, and nourishment.',
  },
]

const HOW_IT_WORKS = [
  { icon: Brain,    text: '29 structured questions about your physical and lifestyle characteristics.' },
  { icon: Activity, text: 'A machine learning model classifies your dominant Prakruti.' },
  { icon: Leaf,     text: 'Receive general wellness guidance aligned with your constitution.' },
]

export default function Home() {
  const navigate = useNavigate()
  const { reset } = useAssessment()
  const [agreed, setAgreed] = useState(false)

  function handleStart() {
    reset()
    navigate('/assessment')
  }

  return (
    <div className="min-h-screen bg-surface">
      {/* Header */}
      <header className="border-b border-stone-200 bg-white/80 backdrop-blur-sm sticky top-0 z-10">
        <div className="max-w-3xl mx-auto px-6 py-4">
          <Logo />
        </div>
      </header>

      <main className="max-w-2xl mx-auto px-6 py-12 space-y-12 animate-fade-in">
        {/* Hero */}
        <div className="text-center space-y-4">
          <div className="inline-flex items-center gap-2 bg-brand-100 text-brand-700 text-xs font-medium px-3 py-1.5 rounded-full">
            <Leaf size={12} />
            AI-Assisted Ayurvedic Self-Assessment
          </div>
          <h1 className="text-4xl sm:text-5xl font-serif text-stone-900 leading-tight">
            Understand Your<br />
            <span className="text-brand-600">Prakruti</span>
          </h1>
          <p className="text-stone-500 text-lg leading-relaxed max-w-lg mx-auto">
            A structured self-assessment guided by Ayurvedic principles and machine learning.
            Complete in around 5–10 minutes.
          </p>
          <p className="text-sm text-stone-400">29 questions · Guided · Educational</p>
        </div>

        {/* Dosha cards */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
          {DOSHAS.map(d => (
            <div key={d.name} className={`rounded-2xl border p-5 ${d.color}`}>
              <div className="flex items-center gap-2 mb-2">
                <div className={`w-2.5 h-2.5 rounded-full ${d.dot}`} />
                <span className={`font-serif font-semibold ${d.accent}`}>{d.name}</span>
              </div>
              <p className="text-sm text-stone-600 leading-relaxed">{d.desc}</p>
            </div>
          ))}
        </div>

        {/* How it works */}
        <div className="rounded-2xl border border-stone-200 bg-white p-6 space-y-4">
          <h2 className="font-serif text-xl text-stone-800">How It Works</h2>
          <div className="space-y-4">
            {HOW_IT_WORKS.map(({ icon: Icon, text }, i) => (
              <div key={i} className="flex gap-3 items-start">
                <div className="w-7 h-7 rounded-lg bg-brand-100 flex items-center justify-center shrink-0 mt-0.5">
                  <Icon size={14} className="text-brand-600" />
                </div>
                <p className="text-sm text-stone-600 leading-relaxed">{text}</p>
              </div>
            ))}
          </div>
        </div>

        {/* Disclaimer + CTA */}
        <div className="rounded-2xl border border-stone-200 bg-white p-6 space-y-5">
          <h2 className="font-serif text-xl text-stone-800">Before You Begin</h2>

          <div className="flex gap-3 rounded-xl bg-amber-50 border border-amber-200 p-4">
            <ShieldAlert className="shrink-0 text-amber-600 mt-0.5" size={18} />
            <p className="text-sm text-amber-800 leading-relaxed">
              This assessment is for educational and wellness self-reflection purposes only.
              It is not a medical diagnosis and does not replace consultation with a qualified
              healthcare professional.
            </p>
          </div>

          <label className="flex items-start gap-3 cursor-pointer group">
            <input
              type="checkbox"
              checked={agreed}
              onChange={e => setAgreed(e.target.checked)}
              className="mt-0.5 w-4 h-4 rounded accent-brand-600 cursor-pointer"
            />
            <span className="text-sm text-stone-600 leading-relaxed group-hover:text-stone-800 transition-colors">
              I understand that this is a wellness self-assessment and not a medical diagnosis,
              and I want to continue.
            </span>
          </label>

          <Button
            onClick={handleStart}
            disabled={!agreed}
            className="w-full"
          >
            Start Assessment
            <ChevronRight size={16} />
          </Button>
        </div>
      </main>

      <footer className="text-center py-8 text-xs text-stone-400">
        Prakruti Self-Assessment · Final Year Engineering Project · Educational Use Only
      </footer>
    </div>
  )
}
