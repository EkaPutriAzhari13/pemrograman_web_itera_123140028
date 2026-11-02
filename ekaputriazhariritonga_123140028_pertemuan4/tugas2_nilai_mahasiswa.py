def hitung_nilai_akhir(uts, uas, tugas):
    """Menghitung nilai akhir dengan bobot UTS 30%, UAS 40%, Tugas 30%.

    Parameter:
        uts   : nilai UTS
        uas   : nilai UAS
        tugas : nilai tugas
    Mengembalikan nilai akhir (float).
    """
    return 0.3 * uts + 0.4 * uas + 0.3 * tugas


def tentukan_grade(nilai_akhir):
    """Menentukan grade A sampai E dari nilai akhir.

    Parameter:
        nilai_akhir : nilai akhir mahasiswa (float)
    Mengembalikan huruf grade (str).
    """
    if nilai_akhir >= 80:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 60:
        return "C"
    elif nilai_akhir >= 50:
        return "D"
    else:
        return "E"


def tampilkan_tabel(daftar_mahasiswa):
    """Mencetak data mahasiswa dalam bentuk tabel di terminal.

    Parameter:
        daftar_mahasiswa : list of dict, setiap dict sudah memiliki
                           kunci 'nilai_akhir' dan 'grade'
    """
    garis = "-" * 56
    print(garis)
    print(f"{'No':<4}{'Nama':<20}{'NIM':<12}{'Nilai Akhir':>12}{'Grade':>8}")
    print(garis)
    for nomor, mhs in enumerate(daftar_mahasiswa, start=1):
        print(
            f"{nomor:<4}{mhs['nama']:<20}{mhs['nim']:<12}"
            f"{mhs['nilai_akhir']:>12.2f}{mhs['grade']:>8}"
        )
    print(garis)


# Data mahasiswa: list berisi dictionary
mahasiswa = [
    {"nama": "Atalie Salsabila", "nim": "123140027", "nilai_uts": 85, "nilai_uas": 90, "nilai_tugas": 88},
    {"nama": "Mulya Delani", "nim": "123140019", "nilai_uts": 70, "nilai_uas": 65, "nilai_tugas": 75},
    {"nama": "Nahli Saud Ramdani", "nim": "123140049", "nilai_uts": 90, "nilai_uas": 95, "nilai_tugas": 92},
    {"nama": "Muhammad Dzaky", "nim": "123140039", "nilai_uts": 55, "nilai_uas": 60, "nilai_tugas": 50},
    {"nama": "Gian Ivander", "nim": "123140040", "nilai_uts": 40, "nilai_uas": 45, "nilai_tugas": 60},
    {"nama": "Muharyan Syaifullah", "nim": "123140045", "nilai_uts": 75, "nilai_uas": 78, "nilai_tugas": 76},
]

# Hitung nilai akhir dan grade, simpan kembali ke dictionary masing-masing
for mhs in mahasiswa:
    mhs["nilai_akhir"] = hitung_nilai_akhir(
        mhs["nilai_uts"], mhs["nilai_uas"], mhs["nilai_tugas"]
    )
    mhs["grade"] = tentukan_grade(mhs["nilai_akhir"])

print("=== Data Nilai Mahasiswa ===")
tampilkan_tabel(mahasiswa)

# Cari nilai tertinggi dan terendah
tertinggi = max(mahasiswa, key=lambda m: m["nilai_akhir"])
terendah = min(mahasiswa, key=lambda m: m["nilai_akhir"])

print(f"\nNilai tertinggi : {tertinggi['nama']} ({tertinggi['nilai_akhir']:.2f}, grade {tertinggi['grade']})")
print(f"Nilai terendah  : {terendah['nama']} ({terendah['nilai_akhir']:.2f}, grade {terendah['grade']})")