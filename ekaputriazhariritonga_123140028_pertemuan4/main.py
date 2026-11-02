# Cara impor 1: impor seluruh modul, fungsinya dipanggil dengan awalan nama modul
import math_operations

# Cara impor 2: impor fungsi tertentu saja, bisa dipanggil langsung
from math_operations import (
    luas_lingkaran,
    keliling_lingkaran,
    celsius_ke_fahrenheit,
    celsius_ke_kelvin,
)

print("=== Pengujian Modul math_operations ===")
print(f"Nilai konstanta PI = {math_operations.PI}")

# Persegi
print("\n[Persegi]")
for sisi in (4, 5.5):
    luas = math_operations.luas_persegi(sisi)
    keliling = math_operations.keliling_persegi(sisi)
    print(f"Sisi {sisi} -> luas = {luas:.2f} | keliling = {keliling:.2f}")

# Persegi panjang
print("\n[Persegi Panjang]")
for panjang, lebar in ((8, 5), (12, 7.5)):
    luas = math_operations.luas_persegi_panjang(panjang, lebar)
    keliling = math_operations.keliling_persegi_panjang(panjang, lebar)
    print(f"{panjang} x {lebar} -> luas = {luas:.2f} | keliling = {keliling:.2f}")

# Lingkaran
print("\n[Lingkaran]")
for jari_jari in (7, 10):
    luas = luas_lingkaran(jari_jari)
    keliling = keliling_lingkaran(jari_jari)
    print(f"Jari-jari {jari_jari} -> luas = {luas:.2f} | keliling = {keliling:.2f}")

# Konversi suhu
print("\n[Konversi Suhu]")
for celsius in (0, 37, 100):
    fahrenheit = celsius_ke_fahrenheit(celsius)
    kelvin = celsius_ke_kelvin(celsius)
    print(f"{celsius} C -> {fahrenheit:.2f} F | {kelvin:.2f} K")