export default function AnswerOption({ option, selected, onSelect }) {
  return (
    <button
      type="button"
      role="radio"
      aria-checked={selected}
      onClick={() => onSelect(option.value)}
      className={`
        w-full text-left px-5 py-4 rounded-xl border transition-all duration-200
        focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-500 focus-visible:ring-offset-1
        ${selected
          ? 'border-brand-500 bg-brand-50 text-brand-800 shadow-sm'
          : 'border-stone-200 bg-white text-stone-700 hover:border-brand-300 hover:bg-brand-50/40'
        }
      `}
    >
      <div className="flex items-center gap-3">
        <div className={`
          w-4 h-4 rounded-full border-2 shrink-0 transition-colors duration-200
          ${selected ? 'border-brand-500 bg-brand-500' : 'border-stone-300'}
        `}>
          {selected && (
            <div className="w-full h-full rounded-full flex items-center justify-center">
              <div className="w-1.5 h-1.5 rounded-full bg-white" />
            </div>
          )}
        </div>
        <span className="text-sm font-medium leading-snug">{option.label}</span>
      </div>
    </button>
  )
}
