import { useEffect, useCallback } from 'react'
import { useNavigate } from 'react-router-dom'
import { ChevronLeft, ChevronRight, CheckCircle } from 'lucide-react'
import Logo from '../components/common/Logo'
import Button from '../components/common/Button'
import ProgressBar from '../components/assessment/ProgressBar'
import QuestionCard from '../components/assessment/QuestionCard'
import LoadingScreen from '../components/common/LoadingScreen'
import ErrorState from '../components/common/ErrorState'
import Disclaimer from '../components/common/Disclaimer'
import { useAssessment } from '../context/AssessmentContext'
import { getQuestions, submitAssessment } from '../services/api'

export default function Assessment() {
  const navigate = useNavigate()
  const {
    questions, setQuestionsData,
    currentIndex, goNext, goPrev,
    answers, answerQuestion,
    setResult, status, setStatus,
    error, setError,
  } = useAssessment()

  const currentQuestion = questions[currentIndex]
  const selectedValue = currentQuestion ? answers[currentQuestion.id] : undefined
  const isLast = currentIndex === questions.length - 1
  const canContinue = !!selectedValue

  // Load questions on mount if not already loaded
  useEffect(() => {
    if (questions.length > 0) return
    setStatus('loading')
    getQuestions()
      .then(data => {
        setQuestionsData(data.questions)
        setStatus('idle')
      })
      .catch(err => {
        console.error('Failed to load questions:', err)
        setError('Unable to load the assessment. Please check your connection and try again.')
        setStatus('error')
      })
  }, []) // eslint-disable-line react-hooks/exhaustive-deps

  const handleSelect = useCallback((value) => {
    if (!currentQuestion) return
    answerQuestion(currentQuestion.id, value)
  }, [currentQuestion, answerQuestion])

  const handleContinue = useCallback(() => {
    if (!canContinue) return
    if (isLast) {
      handleSubmit()
    } else {
      goNext()
    }
  }, [canContinue, isLast, goNext]) // eslint-disable-line react-hooks/exhaustive-deps

  async function handleSubmit() {
    setStatus('submitting')
    const payload = questions.map(q => ({
      question_id: q.id,
      value: answers[q.id],
    }))
    try {
      const result = await submitAssessment(payload)
      setResult(result)
      navigate('/result')
    } catch (err) {
      console.error('Submission failed:', err)
      const msg = err?.response?.data?.detail || "We couldn't submit your assessment. Your answers have not been lost."
      setError(msg)
      setStatus('error')
    }
  }

  if (status === 'submitting') return <LoadingScreen />

  if (status === 'loading') {
    return (
      <div className="min-h-screen bg-surface flex items-center justify-center">
        <div className="text-center space-y-3 animate-fade-in">
          <div className="flex justify-center gap-2">
            {[0, 1, 2].map(i => (
              <div key={i} className="w-2.5 h-2.5 rounded-full bg-brand-400 animate-pulse-soft"
                style={{ animationDelay: `${i * 0.2}s` }} />
            ))}
          </div>
          <p className="text-sm text-stone-500">Loading assessment…</p>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-surface flex flex-col">
      {/* Header */}
      <header className="border-b border-stone-200 bg-white/80 backdrop-blur-sm sticky top-0 z-10">
        <div className="max-w-2xl mx-auto px-6 py-4 flex items-center justify-between gap-4">
          <Logo size="sm" />
          {questions.length > 0 && (
            <span className="text-sm text-stone-500">
              {currentIndex + 1} / {questions.length}
            </span>
          )}
        </div>
      </header>

      <main className="flex-1 max-w-2xl mx-auto w-full px-6 py-8">
        {status === 'error' ? (
          <ErrorState
            message={error}
            onRetry={() => { setStatus('idle'); setError(null) }}
            retryLabel={questions.length === 0 ? 'Retry' : 'Try Submitting Again'}
          />
        ) : (
          <div className="space-y-8">
            {/* Progress */}
            {questions.length > 0 && (
              <ProgressBar current={currentIndex} total={questions.length} />
            )}

            {/* Question */}
            {currentQuestion && (
              <div key={currentQuestion.id}>
                <QuestionCard
                  question={currentQuestion}
                  selectedValue={selectedValue}
                  onSelect={handleSelect}
                />
              </div>
            )}

            {/* Navigation */}
            {currentQuestion && (
              <div className="flex items-center justify-between gap-3 pt-2">
                <Button
                  variant="secondary"
                  onClick={goPrev}
                  disabled={currentIndex === 0}
                >
                  <ChevronLeft size={16} />
                  Previous
                </Button>

                <Button
                  onClick={handleContinue}
                  disabled={!canContinue}
                >
                  {isLast ? (
                    <>
                      <CheckCircle size={16} />
                      Complete Assessment
                    </>
                  ) : (
                    <>
                      Continue
                      <ChevronRight size={16} />
                    </>
                  )}
                </Button>
              </div>
            )}

            {/* Compact disclaimer at bottom */}
            <div className="pt-4">
              <Disclaimer compact />
            </div>
          </div>
        )}
      </main>
    </div>
  )
}
