def hitung_bmi(berat, tinggi):
    """Menghitung BMI.

    Parameter:
        berat  : berat badan dalam kilogram (kg)
        tinggi : tinggi badan dalam meter (m)
    Mengembalikan nilai BMI (float).
    """
    return berat / (tinggi * tinggi)


def tentukan_kategori(bmi):
    """Menentukan kategori berat badan berdasarkan nilai BMI.

    Parameter:
        bmi : nilai BMI (float)
    Mengembalikan nama kategori (str).
    """
    if bmi < 18.5:
        return "Berat badan kurang"
    elif bmi < 25:
        return "Berat badan normal"
    elif bmi < 30:
        return "Berat badan berlebih"
    else:
        return "Obesitas"


print("=== Program Penghitung BMI ===")
berat_badan = float(input("Masukkan berat badan (kg): "))
tinggi_badan = float(input("Masukkan tinggi badan (m): "))

bmi = hitung_bmi(berat_badan, tinggi_badan)
kategori = tentukan_kategori(bmi)

print(f"\nBMI      : {bmi:.2f}")
print(f"Kategori : {kategori}")