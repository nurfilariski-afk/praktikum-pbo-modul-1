class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):
        return self.panjang * self.lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)


# Membuat objek
persegi_panjang_1 = PersegiPanjang(10, 5)
persegi_panjang_2 = PersegiPanjang(8, 3)

# Menampilkan hasil
print("Persegi Panjang 1")
print("Panjang  :", persegi_panjang_1.panjang)
print("Lebar    :", persegi_panjang_1.lebar)
print("Luas     :", persegi_panjang_1.hitung_luas())
print("Keliling :", persegi_panjang_1.hitung_keliling())

print()

print("Persegi Panjang 2")
print("Panjang  :", persegi_panjang_2.panjang)
print("Lebar    :", persegi_panjang_2.lebar)
print("Luas     :", persegi_panjang_2.hitung_luas())
print("Keliling :", persegi_panjang_2.hitung_keliling())