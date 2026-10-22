import { describe, it, expect, beforeEach } from 'vitest'
import { renderHook, act } from '@testing-library/react'
import useLocalStorage from '../hooks/useLocalStorage'
import useBookStats from '../hooks/useBookStats'

describe('useLocalStorage', () => {
  beforeEach(() => {
    localStorage.clear()
  })

  it('menyimpan nilai ke localStorage', () => {
    const { result } = renderHook(() => useLocalStorage('books', []))

    act(() => {
      result.current[1]([{ id: 1, title: 'A' }])
    })

    expect(JSON.parse(localStorage.getItem('books'))).toEqual([{ id: 1, title: 'A' }])
  })
})

describe('useBookStats', () => {
  it('menghitung jumlah buku per status', () => {
    const books = [
      { id: 1, status: 'milik' },
      { id: 2, status: 'baca' },
      { id: 3, status: 'baca' },
      { id: 4, status: 'beli' },
    ]
    const { result } = renderHook(() => useBookStats(books))

    expect(result.current).toEqual({ total: 4, milik: 1, baca: 2, beli: 1 })
  })
})