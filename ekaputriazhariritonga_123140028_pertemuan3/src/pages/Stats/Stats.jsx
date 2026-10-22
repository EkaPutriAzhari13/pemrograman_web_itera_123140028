import { useBooks } from '../../context/BookContext'
import useBookStats from '../../hooks/useBookStats'
import './Stats.css'

function Stats() {
  const { books } = useBooks()
  const stats = useBookStats(books)

  return (
    <div className="stats">
      <h2>Statistik Buku</h2>
      <ul>
        <li>Total buku: {stats.total}</li>
        <li>Milik: {stats.milik}</li>
        <li>Sedang dibaca: {stats.baca}</li>
        <li>Ingin dibeli: {stats.beli}</li>
      </ul>
    </div>
  )
}

export default Stats