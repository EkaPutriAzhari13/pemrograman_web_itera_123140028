// Latihan 3: array dan objek

const mahasiswa = [
  { nama: "Budi", nim: "123140001", jurusan: "Teknik Informatika", nilai: 85 },
  { nama: "Sari", nim: "123140002", jurusan: "Teknik Informatika", nilai: 92 },
  { nama: "Andi", nim: "123140003", jurusan: "Teknik Informatika", nilai: 70 },
  { nama: "Dewi", nim: "123140004", jurusan: "Teknik Informatika", nilai: 78 },
  { nama: "Rani", nim: "123140005", jurusan: "Teknik Informatika", nilai: 88 }
];

// tampilkan semua data
console.table(mahasiswa);

// cari nilai tertinggi
let tertinggi = mahasiswa[0];
for (let i = 1; i < mahasiswa.length; i++) {
  if (mahasiswa[i].nilai > tertinggi.nilai) {
    tertinggi = mahasiswa[i];
  }
}
console.log("Nilai tertinggi:", tertinggi.nama, tertinggi.nilai);

// rata-rata nilai
let total = 0;
for (const m of mahasiswa) {
  total += m.nilai;
}
const rataRata = total / mahasiswa.length;
console.log("Rata-rata:", rataRata);

// mahasiswa yang nilainya di atas rata-rata
const diAtasRata = mahasiswa.filter(function (m) {
  return m.nilai > rataRata;
});
console.log("Di atas rata-rata:", diAtasRata.map(m => m.nama));

// urutkan berdasarkan nama (A-Z)
const urutNama = [...mahasiswa].sort(function (a, b) {
  return a.nama.localeCompare(b.nama);
});
console.log("Urut nama:", urutNama.map(m => m.nama));

// tambah dan hapus data
mahasiswa.push({ nama: "Eka", nim: "123140028", jurusan: "Teknik Informatika", nilai: 90 });
console.log("Jumlah setelah tambah:", mahasiswa.length);
mahasiswa.pop();
console.log("Jumlah setelah hapus:", mahasiswa.length);
