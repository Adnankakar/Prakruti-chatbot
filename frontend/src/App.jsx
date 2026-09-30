import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { AssessmentProvider } from './context/AssessmentContext'
import Home from './pages/Home'
import Assessment from './pages/Assessment'
import Result from './pages/Result'

export default function App() {
  return (
    <BrowserRouter>
      <AssessmentProvider>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/assessment" element={<Assessment />} />
          <Route path="/result" element={<Result />} />
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </AssessmentProvider>
    </BrowserRouter>
  )
}
