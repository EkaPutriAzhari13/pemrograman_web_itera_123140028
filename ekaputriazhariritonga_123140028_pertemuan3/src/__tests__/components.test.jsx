import { describe, it, expect, vi } from 'vitest'
import { render, screen, fireEvent } from '@testing-library/react'
import BookForm from '../components/BookForm/BookForm'
import BookList from '../components/BookList/BookList'
import BookFilter from '../components/BookFilter/BookFilter'

describe('BookForm', () => {
  it('menampilkan pesan error saat form kosong disubmit', () => {
    const onSubmit = vi.fn()
    render(<BookForm onSubmit={onSubmit} />)

    fireEvent.click(screen.getByText('Tambah Buku'))

    expect(screen.getByText('Judul wajib diisi')).toBeInTheDocument()
    expect(screen.getByText('Penulis wajib diisi')).toBeInTheDocument()
    expect(onSubmit).not.toHaveBeenCalled()
  })

  it('memanggil onSubmit dengan data yang valid', () => {
    const onSubmit = vi.fn()
    render(<BookForm onSubmit={onSubmit} />)

    fireEvent.change(screen.getByLabelText('Judul'), {
      target: { value: 'Laskar Pelangi' },
    })
    fireEvent.change(screen.getByLabelText('Penulis'), {
      target: { value: 'Andrea Hirata' },
    })
    fireEvent.click(screen.getByText('Tambah Buku'))

    expect(onSubmit).toHaveBeenCalledWith({
      title: 'Laskar Pelangi',
      author: 'Andrea Hirata',
      status: 'milik',
    })
  })
})

describe('BookList', () => {
  it('menampilkan pesan kosong jika tidak ada buku', () => {
    render(<BookList books={[]} onEdit={() => {}} onDelete={() => {}} />)
    expect(screen.getByText('Belum ada buku.')).toBeInTheDocument()
  })

  it('menampilkan daftar buku dan memanggil onDelete', () => {
    const onDelete = vi.fn()
    const books = [{ id: 1, title: 'Bumi', author: 'Tere Liye', status: 'baca' }]
    render(<BookList books={books} onEdit={() => {}} onDelete={onDelete} />)

    expect(screen.getByText('Bumi')).toBeInTheDocument()
    fireEvent.click(screen.getByText('Hapus'))
    expect(onDelete).toHaveBeenCalledWith(1)
  })
})

describe('BookFilter', () => {
  it('memanggil onSearchChange saat mengetik di kolom pencarian', () => {
    const onSearchChange = vi.fn()
    render(
      <BookFilter
        status="semua"
        onStatusChange={() => {}}
        search=""
        onSearchChange={onSearchChange}
      />
    )

    fireEvent.change(screen.getByPlaceholderText('Cari judul atau penulis...'), {
      target: { value: 'react' },
    })
    expect(onSearchChange).toHaveBeenCalledWith('react')
  })
})