def luas_segitiga():
    a = int(input("Masukkan Alas Segitiga: "))
    t = int(input("Masukkan Tinggi Segitiga: "))
    luas = a*t / 2
    print("Luas segitiga adalah:", luas)

luas_segitiga()

def luas_persegi_panjang():
    p = int(input("Masukkan panjang persegi: "))
    l = int(input("Masukkan lebar persegi: "))
    luas = p*l
    print("Luas persegi adalah: ",luas )

luas_persegi_panjang()

def luas_lingkaran():
    r = int(input("Masukkan jari-jari lingkaran: "))
    luas = 3,14 * r * r
    print("Luas lingkaran adalah: ",luas)

luas_lingkaran()