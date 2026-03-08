# def namaFungsi(a,b):
#     hasil = a + b
#     return hasil
#     #atau dapat ditulis dengan fungsi yang diinginkan

# print(namaFungsi(1,2))

# def sapa(nama):
#     print("Halo,", nama, "! Selamat datang.")

# sapa("Budi")
# hasil = sapa("Budi")
# print(hasil)

# def tambah(a, b, c):
#     hasil = a + b + c
#     return hasil

# nilai1 = 70
# nilai2 = 85
# nilai3 = 55

# rata_rata = tambah(nilai1, nilai2, nilai3) / 3
# print(rata_rata)

# def hitung_belanja(belanja, diskon=0):
#     bayar = belanja - (belanja * diskon) / 100
#     return bayar

# print(hitung_belanja(100000))
# print(hitung_belanja(100000, 10))
# print(hitung_belanja(100000, 50))

# def cetak(a, b, c):
#     print("Nilai a:", a)
#     print("Nilai b:", b)
#     print("Nilai c:", c)
# #cara biasa harus urut
# cetak(20, 30, 40)

# #bisa acak asal ada argumen = berapa gitu
# cetak(b=30, c=40, a=20)

def tambah(a, b):
    hasil = a + b
    return hasil

print(tambah(10, 20))


tambah = lambda a, b: a + b

print(tambah(10, 20))
