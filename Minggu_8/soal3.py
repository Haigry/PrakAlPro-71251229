def hapus_spasi_berlebih(teks):
    hasil = ' '.join(teks.split())
    return hasil

teks1 = "saya    tidak   suka    memancing ikan"

print(hapus_spasi_berlebih(teks1))
