// Latihan 1: variabel dan kondisional

// data diri
const nama = "Eka Putri Azhari Ritonga";
let umur = 20;
const kotaAsal = "Medan";
console.log(nama + ", " + umur + " tahun, asal " + kotaAsal);

// cek kelulusan, syaratnya nilai >= 70
function cekKelulusan(nilai) {
  if (nilai >= 70) {
    return "Lulus";
  } else {
    return "Tidak lulus";
  }
}
console.log("Nilai 85:", cekKelulusan(85));
console.log("Nilai 60:", cekKelulusan(60));

// kategori umur
function kategoriUmur(umur) {
  if (umur < 12) {
    return "Anak";
  } else if (umur <= 17) {
    return "Remaja";
  } else if (umur <= 59) {
    return "Dewasa";
  } else {
    return "Lansia";
  }
}
console.log("Umur 8:", kategoriUmur(8));
console.log("Umur 15:", kategoriUmur(15));
console.log("Umur 30:", kategoriUmur(30));
console.log("Umur 65:", kategoriUmur(65));

// konversi angka hari ke nama hari (bahasa Inggris)
function namaHari(angka) {
  switch (angka) {
    case 1: return "Monday";
    case 2: return "Tuesday";
    case 3: return "Wednesday";
    case 4: return "Thursday";
    case 5: return "Friday";
    case 6: return "Saturday";
    case 7: return "Sunday";
    default: return "Angka harus 1 sampai 7";
  }
}
console.log("Hari ke-3:", namaHari(3));
console.log("Hari ke-9:", namaHari(9));

// grade pakai ternary
const nilai = 78;
const grade = nilai >= 80 ? "A" : nilai >= 70 ? "B" : "C";
console.log("Nilai " + nilai + " grade " + grade);
