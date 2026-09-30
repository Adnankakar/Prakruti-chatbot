import { ShieldAlert } from 'lucide-react'

export default function ResultDisclaimer() {
  return (
    <div className="flex gap-3 rounded-xl border border-amber-200 bg-amber-50 p-4">
      <ShieldAlert className="shrink-0 text-amber-600 mt-0.5" size={18} />
      <p className="text-sm text-amber-800 leading-relaxed">
        This assessment is for educational and wellness self-reflection purposes only.
        It is not a medical diagnosis and does not replace consultation with a qualified
        healthcare professional.
      </p>
    </div>
  )
}
