import { createContext, useContext } from 'react'
import PropTypes from 'prop-types'
import useLocalStorage from '../hooks/useLocalStorage'

const BookContext = createContext(null)

export function BookProvider({ children }) {
  const [books, setBooks] = useLocalStorage('books', [])

  const addBook = (book) => {
    setBooks((prev) => [...prev, { ...book, id: Date.now() }])
  }

  const updateBook = (id, updated) => {
    setBooks((prev) => prev.map((b) => (b.id === id ? { ...b, ...updated } : b)))
  }

  const deleteBook = (id) => {
    setBooks((prev) => prev.filter((b) => b.id !== id))
  }

  return (
    <BookContext.Provider value={{ books, addBook, updateBook, deleteBook }}>
      {children}
    </BookContext.Provider>
  )
}

BookProvider.propTypes = {
  children: PropTypes.node.isRequired,
}

export function useBooks() {
  const context = useContext(BookContext)
  if (!context) throw new Error('useBooks harus dipakai di dalam BookProvider')
  return context
}