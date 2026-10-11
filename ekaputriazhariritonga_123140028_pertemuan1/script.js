// Data keranjang disimpan di array, dan ikut disimpan ke localStorage
let keranjang = [];
let kodePromo = "";

const form = document.getElementById("form-barang");
const inputNama = document.getElementById("nama");
const inputHarga = document.getElementById("harga");
const inputQty = document.getElementById("qty");
const inputBayar = document.getElementById("bayar");
const inputKode = document.getElementById("kode");

// ubah angka jadi format rupiah, contoh 15000 -> Rp 15.000
function rupiah(angka) {
  return "Rp " + angka.toLocaleString("id-ID");
}

function simpan() {
  localStorage.setItem("keranjang", JSON.stringify(keranjang));
}

function muat() {
  const data = localStorage.getItem("keranjang");
  if (data) {
    keranjang = JSON.parse(data);
  }
}

function tampilError(input, idError, pesan) {
  document.getElementById(idError).textContent = pesan;
  if (pesan) {
    input.classList.add("salah");
  } else {
    input.classList.remove("salah");
  }
}

function validasi() {
  let valid = true;

  const nama = inputNama.value.trim();
  const harga = Number(inputHarga.value);
  const qty = Number(inputQty.value);

  if (nama.length < 3) {
    tampilError(inputNama, "error-nama", "Nama barang minimal 3 karakter.");
    valid = false;
  } else {
    tampilError(inputNama, "error-nama", "");
  }

  if (inputHarga.value === "" || isNaN(harga) || harga < 500) {
    tampilError(inputHarga, "error-harga", "Harga harus berupa angka, minimal Rp 500.");
    valid = false;
  } else {
    tampilError(inputHarga, "error-harga", "");
  }

  if (inputQty.value === "" || !Number.isInteger(qty) || qty < 1) {
    tampilError(inputQty, "error-qty", "Jumlah harus bilangan bulat, minimal 1.");
    valid = false;
  } else {
    tampilError(inputQty, "error-qty", "");
  }

  return valid;
}

function hitungTotal() {
  let total = 0;
  for (let i = 0; i < keranjang.length; i++) {
    total += keranjang[i].harga * keranjang[i].qty;
  }
  return total;
}

function hitungDiskon(total) {
  // diskon 10% kalau belanja >= 50rb, atau pakai kode HEMAT10
  const pakaiKode = kodePromo.toUpperCase() === "HEMAT10";
  if (total >= 50000 || (pakaiKode && total > 0)) {
    return total * 0.1;
  }
  return 0;
}

function tampilKeranjang() {
  const tbody = document.getElementById("isi-keranjang");
  tbody.innerHTML = "";

  for (let i = 0; i < keranjang.length; i++) {
    const item = keranjang[i];
    const subtotal = item.harga * item.qty;

    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${i + 1}</td>
      <td></td>
      <td class="angka">${rupiah(item.harga)}</td>
      <td>${item.qty}</td>
      <td class="angka">${rupiah(subtotal)}</td>
      <td><button class="btn-hapus" data-index="${i}">Hapus</button></td>
    `;
    // nama diisi lewat textContent biar aman kalau ada karakter aneh
    tr.children[1].textContent = item.nama;
    tbody.appendChild(tr);
  }

  document.getElementById("kosong").style.display = keranjang.length === 0 ? "block" : "none";
}

function tampilHitungan() {
  const total = hitungTotal();
  const diskon = hitungDiskon(total);
  const totalAkhir = total - diskon;

  document.getElementById("total").textContent = rupiah(total);
  document.getElementById("diskon").textContent = rupiah(diskon);
  document.getElementById("total-akhir").textContent = rupiah(totalAkhir);

  const infoDiskon = document.getElementById("info-diskon");
  if (diskon > 0) {
    infoDiskon.textContent = "Diskon 10% didapat.";
    infoDiskon.className = "info hijau";
  } else if (kodePromo !== "" && kodePromo.toUpperCase() !== "HEMAT10") {
    infoDiskon.textContent = "Kode promo tidak dikenal.";
    infoDiskon.className = "info merah";
  } else {
    infoDiskon.textContent = "Belanja minimal Rp 50.000 dapat diskon 10%.";
    infoDiskon.className = "info";
  }

  // kembalian
  const infoBayar = document.getElementById("info-bayar");
  const bayar = Number(inputBayar.value);

  if (inputBayar.value === "" || totalAkhir === 0) {
    document.getElementById("kembalian").textContent = rupiah(0);
    infoBayar.textContent = "";
  } else if (bayar < totalAkhir) {
    document.getElementById("kembalian").textContent = rupiah(0);
    infoBayar.textContent = "Uang belum mencukupi, kurang " + rupiah(totalAkhir - bayar) + ".";
    infoBayar.className = "info merah";
  } else {
    document.getElementById("kembalian").textContent = rupiah(bayar - totalAkhir);
    infoBayar.textContent = "Pembayaran cukup.";
    infoBayar.className = "info hijau";
  }
}

function render() {
  tampilKeranjang();
  tampilHitungan();
}

form.addEventListener("submit", function (e) {
  e.preventDefault();

  if (!validasi()) {
    return;
  }

  keranjang.push({
    nama: inputNama.value.trim(),
    harga: Number(inputHarga.value),
    qty: Number(inputQty.value)
  });

  simpan();
  form.reset();
  inputNama.focus();
  render();
});

// tombol hapus di tabel
document.getElementById("isi-keranjang").addEventListener("click", function (e) {
  if (e.target.classList.contains("btn-hapus")) {
    const index = Number(e.target.dataset.index);
    keranjang.splice(index, 1);
    simpan();
    render();
  }
});

inputBayar.addEventListener("input", tampilHitungan);

inputKode.addEventListener("input", function () {
  kodePromo = inputKode.value.trim();
  tampilHitungan();
});

document.getElementById("btn-reset").addEventListener("click", function () {
  if (keranjang.length > 0 && !confirm("Kosongkan keranjang dan mulai transaksi baru?")) {
    return;
  }
  keranjang = [];
  kodePromo = "";
  inputKode.value = "";
  inputBayar.value = "";
  localStorage.removeItem("keranjang");
  render();
});

muat();
render();
