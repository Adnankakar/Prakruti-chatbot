const BARS = [
  { key: 'vata',  label: 'Vata',  color: 'bg-sky-400',     text: 'text-sky-700'  },
  { key: 'pitta', label: 'Pitta', color: 'bg-orange-400',   text: 'text-orange-700' },
  { key: 'kapha', label: 'Kapha', color: 'bg-emerald-400',  text: 'text-emerald-700' },
]

export default function DoshaChart({ vpk }) {
  return (
    <div className="rounded-2xl border border-stone-200 bg-white p-6 space-y-4 animate-fade-in">
      <div className="flex items-center justify-between">
        <h3 className="font-serif text-lg text-stone-800">Dosha Composition</h3>
        <p className="text-xs text-stone-400">Rule-based scoring</p>
      </div>

      <div className="space-y-4">
        {BARS.map(({ key, label, color, text }) => {
          const pct = vpk?.[key] ?? 0
          return (
            <div key={key} className="space-y-1.5">
              <div className="flex justify-between text-sm">
                <span className={`font-medium ${text}`}>{label}</span>
                <span className="text-stone-600 font-medium">{pct}%</span>
              </div>
              <div className="h-3 bg-stone-100 rounded-full overflow-hidden">
                <div
                  className={`h-full ${color} rounded-full transition-all duration-700 ease-out`}
                  style={{ width: `${pct}%` }}
                  role="progressbar"
                  aria-valuenow={pct}
                  aria-valuemin={0}
                  aria-valuemax={100}
                  aria-label={`${label}: ${pct}%`}
                />
              </div>
            </div>
          )
        })}
      </div>

      <p className="text-xs text-stone-400 pt-1">
        Percentages are derived from rule-based Ayurvedic scoring, independent of ML classification.
      </p>
    </div>
  )
}
