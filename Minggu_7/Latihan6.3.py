tinggi = int(input("Masukkan tinggi: "))
lebar  = int(input("Masukkan lebar : "))

angka = 1
for baris in range(tinggi):
    isi_baris = []
    for kolom in range(lebar):
        isi_baris.append(str(angka))
        angka += 1
    print("\t".join(isi_baris))
