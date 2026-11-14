from library_item import LibraryItem


class Library:
    """Mengelola koleksi item perpustakaan (buku, majalah, dan item lain).

    Koleksi disimpan di atribut private __koleksi berupa dictionary
    {id: item}, jadi hanya bisa diubah lewat method milik class ini.
    """

    def __init__(self, nama):
        self.nama = nama
        self.__koleksi = {}  # private: tidak bisa diakses langsung dari luar

    @property
    def jumlah_item(self):
        """Jumlah seluruh item di perpustakaan (hanya bisa dibaca)."""
        return len(self.__koleksi)

    def tambah_item(self, item):
        """Menambahkan item ke koleksi. Mengembalikan True kalau berhasil."""
        if not isinstance(item, LibraryItem):
            raise TypeError("Hanya objek LibraryItem yang boleh ditambahkan!")
        if item.item_id in self.__koleksi:
            print(f"Gagal: ID {item.item_id} sudah terdaftar.")
            return False
        self.__koleksi[item.item_id] = item
        print(f"Berhasil menambahkan: {item.judul}")
        return True

    def tampilkan_semua(self):
        """Menampilkan seluruh item beserta statusnya."""
        print(f"\n=== Seluruh Koleksi {self.nama} ({self.jumlah_item} item) ===")
        for item in self.__koleksi.values():
            print(f" {item}")

    def tampilkan_tersedia(self):
        """Menampilkan hanya item yang sedang tidak dipinjam."""
        tersedia = [item for item in self.__koleksi.values() if not item.is_dipinjam]
        print(f"\n=== Katalog Tersedia ({len(tersedia)} item) ===")
        for item in tersedia:
            # get_detail() dipanggil tanpa peduli item itu buku atau majalah
            print(f" [{item.item_id}] {item.get_detail()}")

    def cari_by_id(self, item_id):
        """Mencari satu item berdasarkan ID. Mengembalikan None kalau tidak ada."""
        return self.__koleksi.get(item_id)

    def cari_by_judul(self, kata_kunci):
        """Mencari item yang judulnya mengandung kata kunci (tidak peka huruf besar/kecil)."""
        kata_kunci = kata_kunci.lower()
        return [item for item in self.__koleksi.values()
                if kata_kunci in item.judul.lower()]

    def pinjam_item(self, item_id):
        """Meminjam item berdasarkan ID dan menampilkan hasilnya."""
        item = self.cari_by_id(item_id)
        if item is None:
            print(f"Item dengan ID {item_id} tidak ditemukan.")
        elif item.pinjam():
            print(f"'{item.judul}' berhasil dipinjam.")
        else:
            print(f"'{item.judul}' sedang dipinjam, belum bisa dipinjam lagi.")

    def kembalikan_item(self, item_id):
        """Mengembalikan item berdasarkan ID dan menampilkan hasilnya."""
        item = self.cari_by_id(item_id)
        if item is None:
            print(f"Item dengan ID {item_id} tidak ditemukan.")
        elif item.kembalikan():
            print(f"'{item.judul}' berhasil dikembalikan.")
        else:
            print(f"'{item.judul}' tidak sedang dipinjam.")