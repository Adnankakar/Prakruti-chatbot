import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

const client = axios.create({
  baseURL: API_BASE_URL,
  timeout: 15000,
  headers: { 'Content-Type': 'application/json' },
})

/**
 * Fetch all 29 assessment questions from the backend.
 * Returns { total_questions, questions: [{id, feature, question, options}] }
 */
export async function getQuestions() {
  const { data } = await client.get('/api/questions')
  return data
}

/**
 * Submit completed answers and get the full assessment result.
 *
 * @param {Array<{question_id: number, value: string}>} answers
 * Returns { ml_prediction, vpk_percentages, recommendation, disclaimer }
 */
export async function submitAssessment(answers) {
  const { data } = await client.post('/api/assessment', { answers })
  return data
}

/**
 * Fetch recommendations for a specific dosha class.
 * @param {string} dosha
 */
export async function getRecommendations(dosha) {
  const encoded = encodeURIComponent(dosha)
  const { data } = await client.get(`/api/assessment/recommendations/${encoded}`)
  return data
}
