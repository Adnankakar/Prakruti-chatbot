import { Utensils, Sun, Sparkles } from 'lucide-react'

const SECTIONS = [
  { key: 'description', label: null, icon: null },
  { key: 'diet',        label: 'Food & Nutrition',   icon: Utensils },
  { key: 'lifestyle',   label: 'Lifestyle',           icon: Sun      },
  { key: 'wellness_tips', label: 'Wellness Tips',     icon: Sparkles },
]

export default function RecommendationSection({ recommendation }) {
  if (!recommendation) return null

  return (
    <div className="space-y-4 animate-fade-in">
      <h3 className="font-serif text-lg text-stone-800">General Wellness Recommendations</h3>
      <p className="text-xs text-stone-400">
        General Ayurvedic lifestyle guidance for educational purposes. Not medical advice.
      </p>

      {/* Description */}
      {recommendation.description && (
        <div className="rounded-xl bg-stone-50 border border-stone-200 p-4">
          <p className="text-sm text-stone-700 leading-relaxed">{recommendation.description}</p>
        </div>
      )}

      {/* Diet / Lifestyle / Wellness Tips */}
      {SECTIONS.filter(s => s.label).map(({ key, label, icon: Icon }) => {
        const items = recommendation[key]
        if (!items?.length) return null
        return (
          <div key={key} className="rounded-xl border border-stone-200 bg-white p-5 space-y-3">
            <div className="flex items-center gap-2">
              {Icon && <Icon size={16} className="text-brand-600" />}
              <h4 className="font-medium text-stone-800 text-sm">{label}</h4>
            </div>
            <ul className="space-y-2">
              {items.map((item, i) => (
                <li key={i} className="flex gap-2 text-sm text-stone-600 leading-relaxed">
                  <span className="text-brand-400 mt-0.5">•</span>
                  <span>{item}</span>
                </li>
              ))}
            </ul>
          </div>
        )
      })}
    </div>
  )
}
