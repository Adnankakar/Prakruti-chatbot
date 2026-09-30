export default function Button({
  children,
  onClick,
  disabled = false,
  variant = 'primary',
  type = 'button',
  className = '',
}) {
  const base = 'inline-flex items-center justify-center gap-2 rounded-xl px-6 py-3 font-medium transition-all duration-200 focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-500 focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50'

  const variants = {
    primary: 'bg-brand-600 text-white hover:bg-brand-700 active:bg-brand-800 shadow-sm hover:shadow-md',
    secondary: 'bg-white text-stone-700 border border-stone-200 hover:bg-stone-50 hover:border-stone-300 shadow-sm',
    ghost: 'text-stone-600 hover:bg-stone-100',
  }

  return (
    <button
      type={type}
      onClick={onClick}
      disabled={disabled}
      className={`${base} ${variants[variant]} ${className}`}
    >
      {children}
    </button>
  )
}
