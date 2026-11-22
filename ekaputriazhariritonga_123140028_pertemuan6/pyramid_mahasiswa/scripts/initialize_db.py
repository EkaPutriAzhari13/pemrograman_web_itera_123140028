import argparse
import sys
from datetime import date

from pyramid.paster import bootstrap, setup_logging
from sqlalchemy.exc import OperationalError

from .. import models


def setup_models(dbsession):
    """
    Masukkan data awal (seeding) ke database.

    Data hanya ditambahkan kalau belum ada, jadi aman dijalankan berulang kali.
    """
    data_mahasiswa = [
        {
            'nim': '123',
            'nama': 'putri salsabila',
            'jurusan': 'Teknik Informatika',
            'tanggal_lahir': date(2000, 5, 15),
            'alamat': 'Jl. Merdeka No. 123, Bandung',
        },
        {
            'nim': '54321',
            'nama': 'Siti aisyah',
            'jurusan': 'Sistem Informasi',
            'tanggal_lahir': date(2001, 8, 22),
            'alamat': 'Jl. Mawar No. 45, Jakarta',
        },
    ]

    for data in data_mahasiswa:
        sudah_ada = dbsession.query(models.Mahasiswa).filter_by(nim=data['nim']).first()
        if sudah_ada is None:
            dbsession.add(models.Mahasiswa(**data))

    data_matakuliah = [
        {'kode_mk': 'IF2110', 'nama_mk': 'Pemrograman Web', 'sks': 3, 'semester': 3},
        {'kode_mk': 'IF3140', 'nama_mk': 'Basis Data', 'sks': 4, 'semester': 5},
        {'kode_mk': 'IF2120', 'nama_mk': 'Struktur Data', 'sks': 3, 'semester': 3},
    ]

    for data in data_matakuliah:
        sudah_ada = dbsession.query(models.Matakuliah).filter_by(kode_mk=data['kode_mk']).first()
        if sudah_ada is None:
            dbsession.add(models.Matakuliah(**data))


def parse_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'config_uri',
        help='Configuration file, e.g., development.ini',
    )
    return parser.parse_args(argv[1:])


def main(argv=sys.argv):
    args = parse_args(argv)
    setup_logging(args.config_uri)
    env = bootstrap(args.config_uri)

    try:
        with env['request'].tm:
            dbsession = env['request'].dbsession
            setup_models(dbsession)
        print('Seeding selesai.')
    except OperationalError:
        print('''
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to initialize your database tables with `alembic`.
    Check your README.txt for description and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.
            ''')


if __name__ == '__main__':
    main()