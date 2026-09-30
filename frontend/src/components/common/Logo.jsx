export default function Logo({ size = 'md' }) {
  const sizes = {
    sm: 'text-lg',
    md: 'text-2xl',
    lg: 'text-3xl',
  }
  return (
    <span className={`font-serif font-bold text-brand-700 tracking-wide ${sizes[size]}`}>
      Prakruti
    </span>
  )
}
