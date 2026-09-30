import { createContext, useContext, useState, useCallback } from 'react'

const AssessmentContext = createContext(null)

const STORAGE_KEY = 'prakruti_assessment_state'

function loadSaved() {
  try {
    const raw = sessionStorage.getItem(STORAGE_KEY)
    return raw ? JSON.parse(raw) : null
  } catch {
    return null
  }
}

function save(state) {
  try {
    sessionStorage.setItem(STORAGE_KEY, JSON.stringify(state))
  } catch { /* ignore */ }
}

export function AssessmentProvider({ children }) {
  const saved = loadSaved()

  const [questions, setQuestions] = useState(saved?.questions ?? [])
  const [currentIndex, setCurrentIndex] = useState(saved?.currentIndex ?? 0)
  const [answers, setAnswers] = useState(saved?.answers ?? {})   // { question_id: value }
  const [result, setResult] = useState(null)
  const [status, setStatus] = useState('idle') // idle | loading | submitting | done | error
  const [error, setError] = useState(null)

  const saveProgress = useCallback((patch) => {
    const next = { questions, currentIndex, answers, ...patch }
    save(next)
  }, [questions, currentIndex, answers])

  const setQuestionsData = useCallback((qs) => {
    setQuestions(qs)
    saveProgress({ questions: qs })
  }, [saveProgress])

  const answerQuestion = useCallback((questionId, value) => {
    setAnswers(prev => {
      const next = { ...prev, [questionId]: value }
      saveProgress({ answers: next })
      return next
    })
  }, [saveProgress])

  const goNext = useCallback(() => {
    setCurrentIndex(prev => {
      const next = prev + 1
      saveProgress({ currentIndex: next })
      return next
    })
  }, [saveProgress])

  const goPrev = useCallback(() => {
    setCurrentIndex(prev => {
      const next = Math.max(0, prev - 1)
      saveProgress({ currentIndex: next })
      return next
    })
  }, [saveProgress])

  const reset = useCallback(() => {
    sessionStorage.removeItem(STORAGE_KEY)
    setQuestions([])
    setCurrentIndex(0)
    setAnswers({})
    setResult(null)
    setStatus('idle')
    setError(null)
  }, [])

  return (
    <AssessmentContext.Provider value={{
      questions, setQuestionsData,
      currentIndex, goNext, goPrev,
      answers, answerQuestion,
      result, setResult,
      status, setStatus,
      error, setError,
      reset,
    }}>
      {children}
    </AssessmentContext.Provider>
  )
}

export function useAssessment() {
  const ctx = useContext(AssessmentContext)
  if (!ctx) throw new Error('useAssessment must be inside AssessmentProvider')
  return ctx
}
