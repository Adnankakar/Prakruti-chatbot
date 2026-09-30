export default function ProgressBar({ current, total }) {
  const pct = Math.round(((current + 1) / total) * 100)

  return (
    <div className="space-y-1.5">
      <div className="flex justify-between text-xs text-stone-500">
        <span>Question {current + 1} of {total}</span>
        <span>{pct}%</span>
      </div>
      <div className="h-1.5 bg-stone-200 rounded-full overflow-hidden">
        <div
          className="h-full bg-brand-500 rounded-full transition-all duration-500 ease-out"
          style={{ width: `${pct}%` }}
          role="progressbar"
          aria-valuenow={pct}
          aria-valuemin={0}
          aria-valuemax={100}
          aria-label={`Assessment progress: ${pct}%`}
        />
      </div>
    </div>
  )
}
