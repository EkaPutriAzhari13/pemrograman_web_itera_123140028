import PropTypes from 'prop-types'
import './BookList.css'

const statusLabel = {
  milik: 'Milik',
  baca: 'Sedang Dibaca',
  beli: 'Ingin Dibeli',
}

function BookList({ books, onEdit, onDelete }) {
  if (books.length === 0) {
    return <p>Belum ada buku.</p>
  }

  return (
    <ul className="book-list">
      {books.map((book) => (
        <li key={book.id} className="book-item">
          <div className="book-info">
            <strong>{book.title}</strong>
            <small>{book.author}</small>
            <span className={`badge ${book.status}`}>{statusLabel[book.status]}</span>
          </div>
          <div className="book-actions">
            <button onClick={() => onEdit(book)}>Edit</button>
            <button className="btn-delete" onClick={() => onDelete(book.id)}>
              Hapus
            </button>
          </div>
        </li>
      ))}
    </ul>
  )
}

BookList.propTypes = {
  books: PropTypes.arrayOf(
    PropTypes.shape({
      id: PropTypes.number.isRequired,
      title: PropTypes.string.isRequired,
      author: PropTypes.string.isRequired,
      status: PropTypes.string.isRequired,
    })
  ).isRequired,
  onEdit: PropTypes.func.isRequired,
  onDelete: PropTypes.func.isRequired,
}

export default BookList