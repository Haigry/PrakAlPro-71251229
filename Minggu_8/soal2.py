def hitung_frekuensi(kalimat, kata_cari):
    kalimat_lower = kalimat.lower()
    kata_lower = kata_cari.lower()
    
    kata_list = kalimat_lower.split()
    
    kata_bersih = []
    for kata in kata_list:
        bersih = ''.join([c for c in kata if c.isalpha()])
        kata_bersih.append(bersih)
    
    jumlah = kata_bersih.count(kata_lower)
    return jumlah

kalimat = "Saya mau makan. Makan itu wajib. Mau siang atau malam saya wajib makan"
kata = "makan"
hasil = hitung_frekuensi(kalimat, kata)
print(f"{kata} ada {hasil} buah")

kata2 = "mau"
hasil2 = hitung_frekuensi(kalimat, kata2)
print(f"{kata2} ada {hasil2} buah")

kata3 = "wajib"
hasil3 = hitung_frekuensi(kalimat, kata3)
print(f"{kata3} ada {hasil3} buah")