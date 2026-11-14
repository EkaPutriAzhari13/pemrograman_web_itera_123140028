from library_item import LibraryItem, Book, Magazine
from library import Library


def cetak_hasil_cari(hasil):
    """Menampilkan hasil pencarian berupa list item."""
    if not hasil:
        print(" Tidak ada item yang cocok.")
    for item in hasil:
        print(f" {item}")


perpustakaan = Library("Perpustakaan Kampus ITERA")

# 1. Menambahkan item (buku dan majalah)
print("=== 1. MENAMBAHKAN ITEM ===")
perpustakaan.tambah_item(Book("B001", "Laskar Pelangi", 2005, "Andrea Hirata", 529))
perpustakaan.tambah_item(Book("B002", "Bumi Manusia", 1980, "Pramoedya Ananta Toer", 535))
perpustakaan.tambah_item(Book("B003", "Algoritma dan Pemrograman", 2016, "Rinaldi Munir", 420))
perpustakaan.tambah_item(Magazine("M001", "National Geographic Indonesia", 2024, "Oktober 2024"))
perpustakaan.tambah_item(Magazine("M002", "Tempo", 2024, "November 2024"))
perpustakaan.tambah_item(Book("B001", "Buku Duplikat", 2020, "Anonim", 100))  # ID dobel, ditolak

# 2. Menampilkan katalog item yang tersedia
print("\n=== 2. KATALOG ITEM ===")
perpustakaan.tampilkan_tersedia()

# 3. Mencari item berdasarkan judul atau ID
print("\n=== 3. PENCARIAN ===")
print("Cari judul 'laskar':")
cetak_hasil_cari(perpustakaan.cari_by_judul("laskar"))
print("Cari judul 'tempo':")
cetak_hasil_cari(perpustakaan.cari_by_judul("tempo"))
print("Cari ID 'B002':")
cetak_hasil_cari([perpustakaan.cari_by_id("B002")])
print("Cari judul 'matematika':")
cetak_hasil_cari(perpustakaan.cari_by_judul("matematika"))

# 4. Status ketersediaan: pinjam dan kembalikan
print("\n=== 4. STATUS KETERSEDIAAN ===")
perpustakaan.pinjam_item("B001")
perpustakaan.pinjam_item("B001")  # sudah dipinjam
perpustakaan.pinjam_item("M002")
perpustakaan.tampilkan_semua()
perpustakaan.tampilkan_tersedia()
perpustakaan.kembalikan_item("B001")
perpustakaan.tampilkan_semua()

# 5. Polymorphism: method yang sama, hasil berbeda
print("\n=== 5. POLYMORPHISM (hitung_denda 4 hari) ===")
for id_item in ("B001", "M001"):
    item = perpustakaan.cari_by_id(id_item)
    print(f" {item.get_detail()}")
    print(f"   Denda 4 hari: Rp {item.hitung_denda(4):,}")

# 6. Bukti encapsulation dan abstract class
print("\n=== 6. BUKTI ENCAPSULATION & ABSTRACT CLASS ===")
buku = perpustakaan.cari_by_id("B001")

try:
    print(perpustakaan.__koleksi)
except AttributeError:
    print(" Akses langsung __koleksi gagal (private).")

try:
    buku.is_dipinjam = True
except AttributeError:
    print(" Mengubah is_dipinjam langsung gagal (property read-only).")

try:
    buku.judul = "   "
except ValueError as pesan:
    print(f" Setter judul menolak: {pesan}")

try:
    LibraryItem("X001", "Item Abstrak", 2024)
except TypeError:
    print(" LibraryItem tidak bisa dibuat langsung (abstract class).")