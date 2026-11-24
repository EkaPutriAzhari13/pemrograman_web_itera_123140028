# Pertemuan 6 – RESTful API Pyramid (Mahasiswa & Matakuliah)

## Identitas Praktikan

| | |
|---|---|
| **Nama Lengkap** | Eka Putri Azhari Ritonga |
| **NIM** | 123140028 |
| **Kelas Praktikum** | PAW RA |

## Deskripsi Aplikasi

Aplikasi ini adalah RESTful API yang dibuat dengan **Pyramid Framework** dan database **PostgreSQL**. Isinya dua modul:

- **Manajemen Mahasiswa**: CRUD data mahasiswa (`nim`, `nama`, `jurusan`, `tanggal_lahir`, `alamat`).
- **Manajemen Matakuliah**: CRUD data mata kuliah (`kode_mk`, `nama_mk`, `sks`, `semester`).

Teknologi yang dipakai:

- **SQLAlchemy ORM** untuk model data
- **Alembic** untuk migrasi database
- **URL Dispatch** dengan predikat `request_method` untuk routing
- **View** yang mengembalikan respons JSON

Validasi input:

- Field wajib harus diisi. Kalau tidak lengkap, API mengembalikan `400 Bad Request`.
- `kode_mk` dan `nim` harus unik.
- `sks` dan `semester` harus bilangan bulat lebih dari 0.
- Data yang tidak ditemukan mengembalikan `404 Not Found`.

## Struktur Direktori

```
ekaputriazhariritonga_123140028_pertemuan6/
├── development.ini
├── production.ini
├── setup.py
├── README.md
├── test_api.sh
├── screenshots/
├── .gitignore
└── pyramid_mahasiswa/
    ├── __init__.py
    ├── routes.py
    ├── alembic/
    │   ├── env.py
    │   └── versions/
    │       ├── 20261122_b9ddeb4c2c4f.py   # create mahasiswa table
    │       └── 20261122_071a786621a5.py   # create matakuliah table
    ├── models/
    │   ├── __init__.py
    │   ├── meta.py
    │   ├── mahasiswa.py
    │   └── matakuliah.py
    ├── scripts/
    │   ├── __init__.py
    │   └── initialize_db.py
    └── views/
        ├── __init__.py
        ├── default.py
        ├── mahasiswa.py
        └── matakuliah.py
```

## Instalasi & Menjalankan Aplikasi

### 1. Siapkan database PostgreSQL

```sql
CREATE USER pyramid_user WITH PASSWORD 'pyramid_pass';
CREATE DATABASE pyramid_mahasiswa OWNER pyramid_user;
```

Konfigurasi koneksi ada di `development.ini`:

```ini
sqlalchemy.url = postgresql+psycopg2://pyramid_user:pyramid_pass@localhost:5432/pyramid_mahasiswa
```

### 2. Buat virtual environment & install dependensi

```bash
cd ekaputriazhariritonga_123140028_pertemuan6
python -m venv venv

# Linux / macOS
source venv/bin/activate
# Windows
venv\Scripts\activate

pip install --upgrade pip setuptools
pip install -e ".[testing]"
pip install psycopg2-binary
```

### 3. Jalankan migrasi database

```bash
alembic -c development.ini upgrade head
```

### 4. Isi data awal (seeding)

```bash
initialize_pyramid_mahasiswa_db development.ini
```

Perintah ini mengisi 2 data mahasiswa dan 3 data mata kuliah awal: IF2110 Pemrograman Web, IF3140 Basis Data, dan IF2120 Struktur Data.

### 5. Jalankan server

```bash
pserve development.ini --reload
```

Server berjalan di `http://localhost:6543`.

## Daftar Endpoint

### Mahasiswa

| Method | Endpoint | Keterangan |
|---|---|---|
| GET | `/api/mahasiswa` | Menampilkan semua mahasiswa |
| GET | `/api/mahasiswa/{id}` | Detail mahasiswa (404 jika tidak ada) |
| POST | `/api/mahasiswa` | Tambah mahasiswa (wajib: `nim`, `nama`, `jurusan`) |
| PUT | `/api/mahasiswa/{id}` | Ubah data mahasiswa |
| DELETE | `/api/mahasiswa/{id}` | Hapus mahasiswa |

### Matakuliah

| Method | Endpoint | Keterangan |
|---|---|---|
| GET | `/api/matakuliah` | Menampilkan semua mata kuliah |
| GET | `/api/matakuliah/{id}` | Detail mata kuliah (404 jika tidak ada) |
| POST | `/api/matakuliah` | Tambah mata kuliah (wajib: `kode_mk`, `nama_mk`, `sks`, `semester`) |
| PUT | `/api/matakuliah/{id}` | Ubah data mata kuliah |
| DELETE | `/api/matakuliah/{id}` | Hapus mata kuliah |

## Pengujian API (cURL)

### Mahasiswa

```bash
# GET semua mahasiswa
curl http://localhost:6543/api/mahasiswa

# GET detail mahasiswa
curl http://localhost:6543/api/mahasiswa/1

# POST tambah mahasiswa
curl -X POST http://localhost:6543/api/mahasiswa \
  -H "Content-Type: application/json" \
  -d '{"nim": "123140028", "nama": "Eka Putri Azhari Ritonga", "jurusan": "Teknik Informatika", "tanggal_lahir": "2005-01-01", "alamat": "Lampung"}'

# PUT ubah mahasiswa
curl -X PUT http://localhost:6543/api/mahasiswa/1 \
  -H "Content-Type: application/json" \
  -d '{"alamat": "Jl. Terusan Ryacudu, Lampung Selatan"}'

# DELETE hapus mahasiswa
curl -X DELETE http://localhost:6543/api/mahasiswa/2
```

### Matakuliah

```bash
# GET semua mata kuliah
curl http://localhost:6543/api/matakuliah

# GET detail mata kuliah
curl http://localhost:6543/api/matakuliah/1

# GET mata kuliah yang tidak ada (404)
curl -i http://localhost:6543/api/matakuliah/99

# POST tambah mata kuliah
curl -X POST http://localhost:6543/api/matakuliah \
  -H "Content-Type: application/json" \
  -d '{"kode_mk": "IF3028", "nama_mk": "Pengembangan Aplikasi Web", "sks": 3, "semester": 5}'

# POST data tidak lengkap (400)
curl -i -X POST http://localhost:6543/api/matakuliah \
  -H "Content-Type: application/json" \
  -d '{"kode_mk": "IF9999"}'

# PUT ubah mata kuliah
curl -X PUT http://localhost:6543/api/matakuliah/1 \
  -H "Content-Type: application/json" \
  -d '{"sks": 4}'

# DELETE hapus mata kuliah
curl -X DELETE http://localhost:6543/api/matakuliah/3
```

## Screenshot Hasil Pengujian

Semua endpoint diuji sekaligus dengan skrip [`test_api.sh`](test_api.sh), yang menjalankan perintah cURL untuk setiap endpoint secara berurutan. Status code tiap respons ditampilkan di akhir baris, misalnya `[200]`, `[400]`, `[404]`.

```bash
# terminal 1
pserve development.ini

# terminal 2 (Git Bash)
bash test_api.sh
```

### Endpoint Mahasiswa

GET all, GET by id, POST, PUT, DELETE:

![Hasil pengujian endpoint Mahasiswa](screenshots/test_mahasiswa.png)

### Endpoint Matakuliah

GET all, GET by id, GET 404, POST, POST 400, PUT, DELETE:

![Hasil pengujian endpoint Matakuliah](screenshots/test_matakuliah.png)