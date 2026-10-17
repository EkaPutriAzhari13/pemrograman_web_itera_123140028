// Class untuk satu data pinjaman
class TaskItem {
  constructor({ id, nama, barang, nominal, tenggat, selesai = false }) {
    this.id = id ?? Date.now().toString();
    this.nama = nama;
    this.barang = barang;
    this.nominal = Number(nominal) || 0;
    this.tenggat = tenggat;
    this.selesai = selesai;
  }

  // dianggap terlambat kalau belum kembali dan tenggatnya sudah lewat
  get terlambat() {
    const hariIni = new Date().toLocaleDateString("en-CA"); // format YYYY-MM-DD
    return !this.selesai && this.tenggat < hariIni;
  }

  get status() {
    if (this.selesai) return "selesai";
    return this.terlambat ? "terlambat" : "belum";
  }
}

const KUNCI_STORAGE = "catatan-pinjaman";

// Class utama yang mengatur data dan tampilan
class DashboardApp {
  constructor() {
    this.daftar = this.muat();
    this.filterAktif = "semua";
    this.pasangEvent();
    this.render();
    this.ambilKutipan();
  }

  muat() {
    const data = JSON.parse(localStorage.getItem(KUNCI_STORAGE)) || [];
    return data.map((item) => new TaskItem(item));
  }

  simpan() {
    localStorage.setItem(KUNCI_STORAGE, JSON.stringify(this.daftar));
  }

  // ambil kutipan acak dari API
  async ambilKutipan() {
    const elemen = document.getElementById("kutipan");
    let teks = "Kutipan tidak bisa dimuat, cek koneksi internet.";
    try {
      const respon = await fetch("https://dummyjson.com/quotes/random");
      const { quote, author } = await respon.json();
      teks = `"${quote}" - ${author}`;
    } catch (error) {
      console.error(error);
    }
    elemen.textContent = teks;
  }

  hitungRingkasan() {
    const aktif = this.daftar.filter((item) => !item.selesai);
    const terlambat = this.daftar.filter((item) => item.terlambat);
    const totalUang = aktif.reduce((jumlah, item) => jumlah + item.nominal, 0);

    document.getElementById("total-aktif").textContent = aktif.length;
    document.getElementById("total-terlambat").textContent = terlambat.length;
    document.getElementById("total-uang").textContent = `Rp ${totalUang.toLocaleString("id-ID")}`;
  }

  ambilDataTampil() {
    return this.daftar.filter((item) => {
      if (this.filterAktif === "semua") return true;
      return item.status === this.filterAktif;
    });
  }

  render() {
    const wadah = document.getElementById("daftar");
    const tampil = this.ambilDataTampil();

    if (tampil.length === 0) {
      wadah.innerHTML = `<li class="kosong">Belum ada data.</li>`;
    } else {
      wadah.innerHTML = tampil
        .map((item) => {
          const { id, nama, barang, nominal, tenggat, status } = item;
          const uang = nominal > 0 ? ` - Rp ${nominal.toLocaleString("id-ID")}` : "";
          const label = {
            belum: "Belum kembali",
            terlambat: "Terlambat",
            selesai: "Sudah kembali",
          }[status];

          return `
            <li class="item ${status}">
              <h3>${barang}${uang}</h3>
              <p>Dipinjam oleh ${nama}, tenggat ${tenggat}</p>
              <span class="badge ${status}">${label}</span>
              <div class="aksi">
                <button data-aksi="selesai" data-id="${id}">
                  ${status === "selesai" ? "Batalkan" : "Tandai kembali"}
                </button>
                <button data-aksi="edit" data-id="${id}">Edit</button>
                <button class="hapus" data-aksi="hapus" data-id="${id}">Hapus</button>
              </div>
            </li>`;
        })
        .join("");
    }

    this.hitungRingkasan();
  }

  pasangEvent() {
    const form = document.getElementById("form-pinjaman");
    const tombolBatal = document.getElementById("tombol-batal");
    const wadah = document.getElementById("daftar");

    form.addEventListener("submit", (e) => {
      e.preventDefault();
      this.simpanForm();
    });

    tombolBatal.addEventListener("click", () => this.resetForm());

    // tombol filter
    document.querySelectorAll(".btn-filter").forEach((tombol) => {
      tombol.addEventListener("click", () => {
        document.querySelector(".btn-filter.aktif").classList.remove("aktif");
        tombol.classList.add("aktif");
        this.filterAktif = tombol.dataset.filter;
        this.render();
      });
    });

    // tombol di dalam daftar, cukup satu listener di wadahnya
    wadah.addEventListener("click", (e) => {
      const { aksi, id } = e.target.dataset;
      if (!aksi) return;

      if (aksi === "selesai") this.tandaiSelesai(id);
      if (aksi === "edit") this.isiFormEdit(id);
      if (aksi === "hapus") this.hapus(id);
    });
  }

  simpanForm() {
    const idEdit = document.getElementById("id-edit").value;
    const data = {
      nama: document.getElementById("nama").value.trim(),
      barang: document.getElementById("barang").value.trim(),
      nominal: Number(document.getElementById("nominal").value) || 0,
      tenggat: document.getElementById("tenggat").value,
    };

    if (idEdit) {
      // mode edit: ubah data yang sudah ada
      const item = this.daftar.find((i) => i.id === idEdit);
      Object.assign(item, data);
    } else {
      // mode tambah: buat data baru
      this.daftar.push(new TaskItem(data));
    }

    this.simpan();
    this.render();
    this.resetForm();
  }

  isiFormEdit(id) {
    const { nama, barang, nominal, tenggat } = this.daftar.find((i) => i.id === id);

    document.getElementById("id-edit").value = id;
    document.getElementById("nama").value = nama;
    document.getElementById("barang").value = barang;
    document.getElementById("nominal").value = nominal || "";
    document.getElementById("tenggat").value = tenggat;

    document.getElementById("judul-form").textContent = "Edit Pinjaman";
    document.getElementById("tombol-simpan").textContent = "Simpan Perubahan";
    document.getElementById("tombol-batal").hidden = false;
    document.getElementById("nama").focus();
  }

  resetForm() {
    document.getElementById("form-pinjaman").reset();
    document.getElementById("id-edit").value = "";
    document.getElementById("judul-form").textContent = "Tambah Pinjaman";
    document.getElementById("tombol-simpan").textContent = "Simpan";
    document.getElementById("tombol-batal").hidden = true;
  }

  tandaiSelesai(id) {
    const item = this.daftar.find((i) => i.id === id);
    item.selesai = !item.selesai;
    this.simpan();
    this.render();
  }

  hapus(id) {
    if (!confirm("Hapus data pinjaman ini?")) return;
    this.daftar = this.daftar.filter((i) => i.id !== id);
    this.simpan();
    this.render();
  }
}

const app = new DashboardApp();