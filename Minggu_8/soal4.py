def cari_panjang_pendek(kalimat):
    kata_list = kalimat.lower().split()
    
    terpendek = min(kata_list, key=len)
    terpanjang = max(kata_list, key=len)
    
    return terpendek, terpanjang

kalimat1 = "red snakes and a black frog in the pool"
pendek, panjang = cari_panjang_pendek(kalimat1)
print(f"Kalimat: {kalimat1}")
print(f"terpendek: {pendek}")
print(f"terpanjang: {panjang}")
