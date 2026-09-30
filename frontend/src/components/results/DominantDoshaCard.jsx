const DOSHA_META = {
  Vata:         { color: 'from-sky-50 to-blue-100',   accent: 'text-sky-700',   border: 'border-sky-200',   badge: 'bg-sky-100 text-sky-700' },
  Pitta:        { color: 'from-orange-50 to-red-100', accent: 'text-orange-700',border: 'border-orange-200',badge: 'bg-orange-100 text-orange-700' },
  Kapha:        { color: 'from-green-50 to-emerald-100', accent: 'text-emerald-700', border: 'border-emerald-200', badge: 'bg-emerald-100 text-emerald-700' },
}

function getMeta(dosha) {
  const base = dosha?.split('+')?.[0]
  const key = base ? base.charAt(0).toUpperCase() + base.slice(1) : 'Vata'
  return DOSHA_META[key] ?? DOSHA_META.Vata
}

export default function DominantDoshaCard({ prediction }) {
  const display = prediction
    ?.split('+')
    .map(d => d.charAt(0).toUpperCase() + d.slice(1))
    .join(' + ') ?? '—'

  const meta = getMeta(prediction)

  return (
    <div className={`rounded-2xl border ${meta.border} bg-gradient-to-br ${meta.color} p-6 text-center space-y-3 animate-fade-in`}>
      <p className="text-xs font-medium text-stone-500 uppercase tracking-widest">Your Dominant Prakruti</p>
      <h1 className={`text-4xl font-serif font-bold ${meta.accent}`}>{display}</h1>
      <span className={`inline-block text-xs font-medium px-3 py-1 rounded-full ${meta.badge}`}>
        Based on ML classification
      </span>
      <p className="text-xs text-stone-500 max-w-xs mx-auto pt-1">
        This result represents the output of the assessment methodology and is not a medical diagnosis.
      </p>
    </div>
  )
}
