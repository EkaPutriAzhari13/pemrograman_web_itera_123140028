import PropTypes from 'prop-types'
import './BookFilter.css'

function BookFilter({ status, onStatusChange, search, onSearchChange }) {
  return (
    <div className="book-filter">
      <input
        type="text"
        placeholder="Cari judul atau penulis..."
        value={search}
        onChange={(e) => onSearchChange(e.target.value)}
      />
      <select value={status} onChange={(e) => onStatusChange(e.target.value)}>
        <option value="semua">Semua</option>
        <option value="milik">Milik</option>
        <option value="baca">Sedang Dibaca</option>
        <option value="beli">Ingin Dibeli</option>
      </select>
    </div>
  )
}

BookFilter.propTypes = {
  status: PropTypes.string.isRequired,
  onStatusChange: PropTypes.func.isRequired,
  search: PropTypes.string.isRequired,
  onSearchChange: PropTypes.func.isRequired,
}

export default BookFilter