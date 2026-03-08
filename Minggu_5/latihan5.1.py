def cek_angka(a, b, c):
    semua_beda = (a != b) and (b != c) and (a != c)

    ada_jumlah = (a + b == c) or (a + c == b) or (b + c == a)

    if semua_beda and ada_jumlah:
        hasil = True ,"Semua kondisi terpenuhi"
        return hasil
    elif not semua_beda and not ada_jumlah:
        hasil = False ,"Tidak semua kondisi terpenuhi"
        return hasil
    elif not semua_beda:
        hasil = False ,"Ada angka yang sama"
        return hasil
    else:
        hasil = False ,"Jumlahnya tidak sesuai"
        return hasil

a = int(input("Masukkan bilangan pertama: "))
b = int(input("Masukkan bilangan kedua: "))
c = int(input("Masukkan bilangan ketiga: "))

print(cek_angka(a, b, c))
