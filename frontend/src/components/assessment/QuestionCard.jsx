import AnswerOption from './AnswerOption'

export default function QuestionCard({ question, selectedValue, onSelect }) {
  return (
    <div className="animate-slide-up space-y-4">
      {/* Category badge */}
      {question.feature && (
        <span className="inline-block text-xs font-medium text-brand-600 bg-brand-100 px-3 py-1 rounded-full">
          {question.feature}
        </span>
      )}

      {/* Question text */}
      <h2 className="text-xl font-serif text-stone-800 leading-snug">
        {question.question}
      </h2>

      {/* Answer options */}
      <div
        className="space-y-2.5 pt-1"
        role="radiogroup"
        aria-label={question.question}
      >
        {question.options.map(opt => (
          <AnswerOption
            key={opt.value}
            option={opt}
            selected={selectedValue === opt.value}
            onSelect={onSelect}
          />
        ))}
      </div>
    </div>
  )
}
