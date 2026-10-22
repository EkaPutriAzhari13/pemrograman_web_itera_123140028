import { useState } from 'react'
import { useBooks } from '../../context/BookContext'
import BookForm from '../../components/BookForm/BookForm'
import BookList from '../../components/BookList/BookList'
import BookFilter from '../../components/BookFilter/BookFilter'
import './Home.css'

function Home() {
  const { books, addBook, updateBook, deleteBook } = useBooks()
  const [status, setStatus] = useState('semua')
  const [search, setSearch] = useState('')
  const [editingBook, setEditingBook] = useState(null)

  const filteredBooks = books.filter((book) => {
    const matchStatus = status === 'semua' || book.status === status
    const keyword = search.toLowerCase()
    const matchSearch =
      book.title.toLowerCase().includes(keyword) ||
      book.author.toLowerCase().includes(keyword)
    return matchStatus && matchSearch
  })

  const handleSubmit = (data) => {
    if (editingBook) {
      updateBook(editingBook.id, data)
      setEditingBook(null)
    } else {
      addBook(data)
    }
  }

  return (
    <div className="home">
      <h2>{editingBook ? 'Edit Buku' : 'Tambah Buku'}</h2>
      <BookForm
        onSubmit={handleSubmit}
        initialData={editingBook}
        onCancel={() => setEditingBook(null)}
      />

      <h2>Daftar Buku</h2>
      <BookFilter
        status={status}
        onStatusChange={setStatus}
        search={search}
        onSearchChange={setSearch}
      />
      <BookList books={filteredBooks} onEdit={setEditingBook} onDelete={deleteBook} />
    </div>
  )
}

export default Home