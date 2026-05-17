# Latihan 11.2
# Buatlah program dengan menggunakan tuple yang dapat melalukan proses
# seperti pada kasus 11.1, Gunakan data diri anda masing-masing dan lakukan
# perubahan supaya didapatkan output seperti contoh berikut ini.

# Ganti dengan data diri Anda
data = ('Ignatius Harya Nugraha', '71251229', 'Yogyakarta, DIY')

print(f"Data:  {data}")
print()

# Unpack tuple
nama, nim, alamat = data

print(f"NIM    :  {nim}")
print(f"NAMA   :  {nama}")
print(f"ALAMAT :  {alamat}")
print()

# NIM per digit sebagai tuple
nim_tuple = tuple(nim)
print(f"NIM:  {nim_tuple}")
print()

# Nama depan per karakter sebagai tuple
nama_depan = nama.split()[0]
nama_depan_tuple = tuple(nama_depan)
print(f"NAMA DEPAN:  {nama_depan_tuple}")
print()

# Nama terbalik (split by spasi, dibalik) sebagai tuple
nama_terbalik = tuple(reversed(nama.split()))
print(f"NAMA TERBALIK:  {nama_terbalik}")
