from datetime import datetime

from pyramid.httpexceptions import HTTPBadRequest, HTTPNotFound
from pyramid.view import view_config

from ..models import Mahasiswa


def cari_mahasiswa(request):
    """Ambil mahasiswa berdasarkan id di URL. Hasilnya None kalau tidak ada."""
    id_mhs = request.matchdict['id']
    if id_mhs.isdigit():
        return request.dbsession.get(Mahasiswa, int(id_mhs))
    return None


def tidak_ditemukan(request):
    """Respon 404 berformat JSON.

    Dikembalikan dengan return (bukan raise), karena 404 yang di-raise akan
    ditangkap view notfound bawaan template dan berubah jadi halaman HTML.
    """
    return HTTPNotFound(json_body={
        'error': f"Mahasiswa dengan ID {request.matchdict['id']} tidak ditemukan"})


def baca_json(request):
    """Ambil body JSON dari request. Kalau bukan JSON object, kirim 400."""
    try:
        data = request.json_body
    except ValueError:
        raise HTTPBadRequest(json_body={'error': 'Body request harus berupa JSON yang valid'})
    if not isinstance(data, dict):
        raise HTTPBadRequest(json_body={'error': 'Body request harus berupa JSON object'})
    return data


def baca_tanggal(teks):
    """Ubah teks YYYY-MM-DD jadi tanggal. Teks kosong dianggap tidak ada tanggal."""
    if not teks:
        return None
    try:
        return datetime.strptime(str(teks), '%Y-%m-%d').date()
    except ValueError:
        raise HTTPBadRequest(json_body={
            'error': 'Format tanggal lahir tidak valid. Gunakan format YYYY-MM-DD'})


def cek_nim_unik(request, nim, id_sendiri=None):
    """Pastikan NIM belum dipakai mahasiswa lain."""
    lain = request.dbsession.query(Mahasiswa).filter_by(nim=nim).first()
    if lain is not None and lain.id != id_sendiri:
        raise HTTPBadRequest(json_body={'error': f'NIM {nim} sudah terdaftar'})


# 1. Lihat semua mahasiswa
@view_config(route_name='mahasiswa_list', renderer='json')
def mahasiswa_list(request):
    data = request.dbsession.query(Mahasiswa).order_by(Mahasiswa.id).all()
    return {'mahasiswas': [m.to_dict() for m in data]}


# 2. Lihat satu mahasiswa
@view_config(route_name='mahasiswa_detail', renderer='json')
def mahasiswa_detail(request):
    mahasiswa = cari_mahasiswa(request)
    if mahasiswa is None:
        return tidak_ditemukan(request)
    return {'mahasiswa': mahasiswa.to_dict()}


# 3. Tambah mahasiswa baru
@view_config(route_name='mahasiswa_add', renderer='json')
def mahasiswa_add(request):
    data = baca_json(request)

    # nim, nama, dan jurusan wajib diisi
    for field in ('nim', 'nama', 'jurusan'):
        if not data.get(field):
            raise HTTPBadRequest(json_body={'error': f'Field {field} wajib diisi!'})

    nim = str(data['nim'])
    cek_nim_unik(request, nim)

    mahasiswa = Mahasiswa(
        nim=nim,
        nama=data['nama'],
        jurusan=data['jurusan'],
        tanggal_lahir=baca_tanggal(data.get('tanggal_lahir')),
        alamat=data.get('alamat'),
    )
    request.dbsession.add(mahasiswa)
    request.dbsession.flush()  # supaya id langsung terisi

    return {'success': True, 'mahasiswa': mahasiswa.to_dict()}


# 4. Ubah data mahasiswa (hanya field yang dikirim yang diubah)
@view_config(route_name='mahasiswa_update', renderer='json')
def mahasiswa_update(request):
    mahasiswa = cari_mahasiswa(request)
    if mahasiswa is None:
        return tidak_ditemukan(request)
    data = baca_json(request)

    for field in ('nim', 'nama', 'jurusan'):
        if field in data:
            if not data[field]:
                raise HTTPBadRequest(json_body={'error': f'Field {field} tidak boleh kosong!'})
            if field == 'nim':
                cek_nim_unik(request, str(data['nim']), mahasiswa.id)
                mahasiswa.nim = str(data['nim'])
            else:
                setattr(mahasiswa, field, data[field])

    if 'alamat' in data:
        mahasiswa.alamat = data['alamat']
    if 'tanggal_lahir' in data:
        mahasiswa.tanggal_lahir = baca_tanggal(data['tanggal_lahir'])

    return {'success': True, 'mahasiswa': mahasiswa.to_dict()}


# 5. Hapus mahasiswa
@view_config(route_name='mahasiswa_delete', renderer='json')
def mahasiswa_delete(request):
    mahasiswa = cari_mahasiswa(request)
    if mahasiswa is None:
        return tidak_ditemukan(request)
    id_mhs = mahasiswa.id
    request.dbsession.delete(mahasiswa)
    return {'success': True,
            'message': f'Mahasiswa dengan ID {id_mhs} berhasil dihapus'}