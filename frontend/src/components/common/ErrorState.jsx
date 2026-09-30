import { AlertCircle } from 'lucide-react'
import Button from './Button'

export default function ErrorState({ message, onRetry, retryLabel = 'Try Again' }) {
  return (
    <div className="flex flex-col items-center gap-4 py-12 text-center animate-fade-in">
      <div className="w-12 h-12 rounded-full bg-red-50 flex items-center justify-center">
        <AlertCircle className="text-red-500" size={24} />
      </div>
      <div>
        <p className="font-medium text-stone-800 mb-1">Something went wrong</p>
        <p className="text-sm text-stone-500 max-w-sm">{message}</p>
      </div>
      {onRetry && (
        <Button onClick={onRetry} variant="secondary">
          {retryLabel}
        </Button>
      )}
    </div>
  )
}
