import { useState, useEffect } from 'react'
import PropTypes from 'prop-types'
import './BookForm.css'

const emptyForm = { title: '', author: '', status: 'milik' }

function BookForm({ onSubmit, initialData, onCancel }) {
  const [form, setForm] = useState(initialData || emptyForm)
  const [errors, setErrors] = useState({})

  useEffect(() => {
    setForm(initialData || emptyForm)
    setErrors({})
  }, [initialData])

  const handleChange = (e) => {
    const { name, value } = e.target
    setForm((prev) => ({ ...prev, [name]: value }))
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    const newErrors = {}
    if (!form.title.trim()) newErrors.title = 'Judul wajib diisi'
    if (!form.author.trim()) newErrors.author = 'Penulis wajib diisi'
    setErrors(newErrors)
    if (Object.keys(newErrors).length > 0) return

    onSubmit({
      title: form.title.trim(),
      author: form.author.trim(),
      status: form.status,
    })
    if (!initialData) setForm(emptyForm)
  }

  return (
    <form onSubmit={handleSubmit} noValidate className="book-form">
      <div>
        <label htmlFor="title">Judul</label>
        <input
          id="title"
          name="title"
          value={form.title}
          onChange={handleChange}
          className={errors.title ? 'input-error' : ''}
        />
        {errors.title && <p className="error-text">{errors.title}</p>}
      </div>

      <div>
        <label htmlFor="author">Penulis</label>
        <input
          id="author"
          name="author"
          value={form.author}
          onChange={handleChange}
          className={errors.author ? 'input-error' : ''}
        />
        {errors.author && <p className="error-text">{errors.author}</p>}
      </div>

      <div>
        <label htmlFor="status">Status</label>
        <select id="status" name="status" value={form.status} onChange={handleChange}>
          <option value="milik">Milik</option>
          <option value="baca">Sedang Dibaca</option>
          <option value="beli">Ingin Dibeli</option>
        </select>
      </div>

      <div className="actions">
        <button type="submit">{initialData ? 'Simpan Perubahan' : 'Tambah Buku'}</button>
        {initialData && (
          <button type="button" className="btn-cancel" onClick={onCancel}>
            Batal
          </button>
        )}
      </div>
    </form>
  )
}

BookForm.propTypes = {
  onSubmit: PropTypes.func.isRequired,
  initialData: PropTypes.shape({
    id: PropTypes.number,
    title: PropTypes.string,
    author: PropTypes.string,
    status: PropTypes.string,
  }),
  onCancel: PropTypes.func,
}

export default BookForm