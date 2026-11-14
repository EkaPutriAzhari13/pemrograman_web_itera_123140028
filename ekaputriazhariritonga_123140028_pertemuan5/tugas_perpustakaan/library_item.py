from abc import ABC, abstractmethod


class LibraryItem(ABC):
    """Class dasar (abstract) untuk semua item perpustakaan.

    Class ini tidak bisa dibuat objeknya secara langsung. Setiap subclass
    wajib mengisi method abstract get_detail() dan hitung_denda().
    """

    def __init__(self, item_id, judul, tahun_terbit):
        self._item_id = item_id            # protected: boleh dipakai subclass
        self._tahun_terbit = tahun_terbit  # protected
        self.judul = judul                 # lewat setter, jadi ikut divalidasi
        self.__dipinjam = False            # private: hanya diubah lewat pinjam()/kembalikan()

    @property
    def item_id(self):
        """ID item (hanya bisa dibaca)."""
        return self._item_id

    @property
    def judul(self):
        """Judul item."""
        return self._judul

    @judul.setter
    def judul(self, judul_baru):
        """Mengubah judul. Judul tidak boleh kosong."""
        if not judul_baru or not judul_baru.strip():
            raise ValueError("Judul tidak boleh kosong!")
        self._judul = judul_baru.strip()

    @property
    def is_dipinjam(self):
        """Status pinjam: True kalau sedang dipinjam (hanya bisa dibaca)."""
        return self.__dipinjam

    def pinjam(self):
        """Meminjam item. Mengembalikan True kalau berhasil, False kalau sudah dipinjam."""
        if self.__dipinjam:
            return False
        self.__dipinjam = True
        return True

    def kembalikan(self):
        """Mengembalikan item. Mengembalikan True kalau berhasil, False kalau tidak sedang dipinjam."""
        if not self.__dipinjam:
            return False
        self.__dipinjam = False
        return True

    @abstractmethod
    def get_detail(self):
        """Mengembalikan teks detail item. Diisi oleh subclass."""
        pass

    @abstractmethod
    def hitung_denda(self, hari_terlambat):
        """Menghitung denda keterlambatan. Diisi oleh subclass."""
        pass

    def __str__(self):
        status = "Dipinjam" if self.__dipinjam else "Tersedia"
        return f"[{self._item_id}] {self._judul} - {status}"


class Book(LibraryItem):
    """Buku. Denda keterlambatan Rp 1.000 per hari."""

    DENDA_PER_HARI = 1000

    def __init__(self, item_id, judul, tahun_terbit, penulis, jumlah_halaman):
        super().__init__(item_id, judul, tahun_terbit)
        self.penulis = penulis
        self.jumlah_halaman = jumlah_halaman

    def get_detail(self):
        """Detail buku: judul, penulis, halaman, dan tahun terbit."""
        return (f"Buku | {self._judul} | Penulis: {self.penulis} | "
                f"{self.jumlah_halaman} halaman | Terbit {self._tahun_terbit}")

    def hitung_denda(self, hari_terlambat):
        """Denda buku = hari terlambat x Rp 1.000 (0 kalau tidak terlambat)."""
        return max(0, hari_terlambat) * self.DENDA_PER_HARI


class Magazine(LibraryItem):
    """Majalah. Denda keterlambatan Rp 500 per hari."""

    DENDA_PER_HARI = 500

    def __init__(self, item_id, judul, tahun_terbit, edisi):
        super().__init__(item_id, judul, tahun_terbit)
        self.edisi = edisi

    def get_detail(self):
        """Detail majalah: judul, edisi, dan tahun terbit."""
        return f"Majalah | {self._judul} | Edisi: {self.edisi} | Terbit {self._tahun_terbit}"

    def hitung_denda(self, hari_terlambat):
        """Denda majalah = hari terlambat x Rp 500 (0 kalau tidak terlambat)."""
        return max(0, hari_terlambat) * self.DENDA_PER_HARI