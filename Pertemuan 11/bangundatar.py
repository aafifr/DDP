# Modul Bangun Datar

# 1. Persegi
def persegi(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi
    print("Hasil luasnya persegi:", luas)
    print("Hasil kelilingnya persegi:", keliling)

# 2. Persegi Panjang
def persegi_panjang(panjang,lebar):
    luas = panjang*lebar
    keliling = panjang + lebar * 2
    print("Hasil luas persegi panjang:", luas)
    print("Hasil keliling persegi panjang:", keliling)

#  3. Segitiga
def segitiga(sisi,alas,tinggi):
    luas = 0.5 * alas * tinggi
    keliling = 3 * sisi
    print("Hasil luas segitiga:", luas)
    print("hasil keliling segitiga:", keliling)

# 4. Lingkaran
def lingkaran(r,diameter):
    luas = 22.7 * r * r
    keliling = 22.7 * diameter
    print("Hasil luas lingkaran:", luas)
    print("Hasil keliling lingkaran:", keliling)

# 5. Belah Ketupat
def belah_ketupat(d1,d2,sisi):
    luas = 0.5 * d1 * d2
    keliling = 4 * sisi
    print("Hasil luas belah ketupat:", luas)
    print("Hasil keliling belah ketupat:", keliling)

# 6. Jajargenjang
def jajar_genjang(alas,tinggi,sisi):
    luas = alas * tinggi
    keliling = 2 * (alas + sisi)
    print("Hasil luas jajargenjang:", luas)
    print("Hasil keliling jajargenjang:", keliling)

# Trapesium
def trapesium(tinggi,a,b,c,d):
    luas = 0.5 * tinggi
    keliling = a + b + c + d
    print("Hasil luas trapesium:", luas)
    print("Hasil keliling trapesium:", keliling)