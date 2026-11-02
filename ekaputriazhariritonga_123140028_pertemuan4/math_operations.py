# Konstanta
PI = 3.14159


def luas_persegi(sisi):
    """Menghitung luas persegi.

    Parameter:
        sisi : panjang sisi persegi
    Mengembalikan luas persegi (float).
    """
    return sisi * sisi


def keliling_persegi(sisi):
    """Menghitung keliling persegi.

    Parameter:
        sisi : panjang sisi persegi
    Mengembalikan keliling persegi (float).
    """
    return 4 * sisi


def luas_persegi_panjang(panjang, lebar):
    """Menghitung luas persegi panjang.

    Parameter:
        panjang : panjang persegi panjang
        lebar   : lebar persegi panjang
    Mengembalikan luas persegi panjang (float).
    """
    return panjang * lebar


def keliling_persegi_panjang(panjang, lebar):
    """Menghitung keliling persegi panjang.

    Parameter:
        panjang : panjang persegi panjang
        lebar   : lebar persegi panjang
    Mengembalikan keliling persegi panjang (float).
    """
    return 2 * (panjang + lebar)


def luas_lingkaran(jari_jari):
    """Menghitung luas lingkaran memakai konstanta PI.

    Parameter:
        jari_jari : jari-jari lingkaran
    Mengembalikan luas lingkaran (float).
    """
    return PI * jari_jari ** 2


def keliling_lingkaran(jari_jari):
    """Menghitung keliling lingkaran memakai konstanta PI.

    Parameter:
        jari_jari : jari-jari lingkaran
    Mengembalikan keliling lingkaran (float).
    """
    return 2 * PI * jari_jari


def celsius_ke_fahrenheit(celsius):
    """Mengonversi suhu dari Celsius ke Fahrenheit.

    Parameter:
        celsius : suhu dalam derajat Celsius
    Mengembalikan suhu dalam Fahrenheit (float).
    """
    return celsius * 9 / 5 + 32


def celsius_ke_kelvin(celsius):
    """Mengonversi suhu dari Celsius ke Kelvin.

    Parameter:
        celsius : suhu dalam derajat Celsius
    Mengembalikan suhu dalam Kelvin (float).
    """
    return celsius + 273.15