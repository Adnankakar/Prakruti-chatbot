export default function LoadingScreen() {
  return (
    <div className="min-h-screen bg-surface flex items-center justify-center">
      <div className="text-center animate-fade-in space-y-6 max-w-sm mx-auto px-6">
        <div className="flex justify-center gap-2">
          {[0, 1, 2].map(i => (
            <div
              key={i}
              className="w-3 h-3 rounded-full bg-brand-400 animate-pulse-soft"
              style={{ animationDelay: `${i * 0.25}s` }}
            />
          ))}
        </div>
        <div className="space-y-2">
          <h2 className="text-xl font-serif text-stone-800">Analysing Your Responses</h2>
          <p className="text-sm text-stone-500">Preparing your assessment result…</p>
        </div>
        <p className="text-xs text-stone-400">
          Your responses are being processed by the assessment system.
        </p>
      </div>
    </div>
  )
}
