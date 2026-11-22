from pyramid.httpexceptions import HTTPBadRequest, HTTPNotFound
from pyramid.view import view_config

from ..models import Matakuliah
from .mahasiswa import baca_json


def cari_matakuliah(request):
    """Ambil mata kuliah berdasarkan id di URL. Hasilnya None kalau tidak ada."""
    id_mk = request.matchdict['id']
    if id_mk.isdigit():
        return request.dbsession.get(Matakuliah, int(id_mk))
    return None


def tidak_ditemukan(request):
    """Respon 404 berformat JSON (di-return, bukan di-raise, supaya tidak
    ditangkap view notfound bawaan template)."""
    return HTTPNotFound(json_body={
        'error': f"Matakuliah dengan ID {request.matchdict['id']} tidak ditemukan"})


def cek_angka_positif(nilai, nama_field):
    """Pastikan nilai berupa bilangan bulat lebih dari 0 (untuk sks dan semester)."""
    if isinstance(nilai, str) and nilai.strip().isdigit():
        nilai = int(nilai)
    if isinstance(nilai, bool) or not isinstance(nilai, int) or nilai <= 0:
        raise HTTPBadRequest(json_body={
            'error': f'Field {nama_field} harus berupa bilangan bulat lebih dari 0'})
    return nilai


def cek_kode_unik(request, kode_mk, id_sendiri=None):
    """Pastikan kode mata kuliah belum dipakai mata kuliah lain."""
    lain = request.dbsession.query(Matakuliah).filter_by(kode_mk=kode_mk).first()
    if lain is not None and lain.id != id_sendiri:
        raise HTTPBadRequest(json_body={'error': f'Kode {kode_mk} sudah terdaftar'})


# 1. Lihat semua mata kuliah
@view_config(route_name='matakuliah_list', renderer='json')
def matakuliah_list(request):
    data = request.dbsession.query(Matakuliah).order_by(Matakuliah.id).all()
    return {'matakuliahs': [mk.to_dict() for mk in data]}


# 2. Lihat satu mata kuliah
@view_config(route_name='matakuliah_detail', renderer='json')
def matakuliah_detail(request):
    matakuliah = cari_matakuliah(request)
    if matakuliah is None:
        return tidak_ditemukan(request)
    return {'matakuliah': matakuliah.to_dict()}


# 3. Tambah mata kuliah baru
@view_config(route_name='matakuliah_add', renderer='json')
def matakuliah_add(request):
    data = baca_json(request)

    # keempat field wajib diisi
    for field in ('kode_mk', 'nama_mk', 'sks', 'semester'):
        if data.get(field) in (None, ''):
            raise HTTPBadRequest(json_body={'error': f'Field {field} wajib diisi!'})

    sks = cek_angka_positif(data['sks'], 'sks')
    semester = cek_angka_positif(data['semester'], 'semester')
    kode_mk = str(data['kode_mk'])
    cek_kode_unik(request, kode_mk)

    matakuliah = Matakuliah(
        kode_mk=kode_mk,
        nama_mk=data['nama_mk'],
        sks=sks,
        semester=semester,
    )
    request.dbsession.add(matakuliah)
    request.dbsession.flush()  # supaya id langsung terisi

    return {'success': True, 'matakuliah': matakuliah.to_dict()}


# 4. Ubah data mata kuliah (hanya field yang dikirim yang diubah)
@view_config(route_name='matakuliah_update', renderer='json')
def matakuliah_update(request):
    matakuliah = cari_matakuliah(request)
    if matakuliah is None:
        return tidak_ditemukan(request)
    data = baca_json(request)

    for field in ('kode_mk', 'nama_mk'):
        if field in data:
            if not data[field]:
                raise HTTPBadRequest(json_body={'error': f'Field {field} tidak boleh kosong!'})
            if field == 'kode_mk':
                cek_kode_unik(request, str(data['kode_mk']), matakuliah.id)
                matakuliah.kode_mk = str(data['kode_mk'])
            else:
                matakuliah.nama_mk = data['nama_mk']

    if 'sks' in data:
        matakuliah.sks = cek_angka_positif(data['sks'], 'sks')
    if 'semester' in data:
        matakuliah.semester = cek_angka_positif(data['semester'], 'semester')

    return {'success': True, 'matakuliah': matakuliah.to_dict()}


# 5. Hapus mata kuliah
@view_config(route_name='matakuliah_delete', renderer='json')
def matakuliah_delete(request):
    matakuliah = cari_matakuliah(request)
    if matakuliah is None:
        return tidak_ditemukan(request)
    id_mk = matakuliah.id
    request.dbsession.delete(matakuliah)
    return {'success': True,
            'message': f'Matakuliah dengan ID {id_mk} berhasil dihapus'}