# Latihan 11.2

data = ('Ignatius Harya Nugraha', '71251229', 'Yogyakarta, DIY')

print(f"Data:  {data}")
print()

nama, nim, alamat = data

print(f"NIM    :  {nim}")
print(f"NAMA   :  {nama}")
print(f"ALAMAT :  {alamat}")
print()

nim_tuple = tuple(nim)
print(f"NIM:  {nim_tuple}")
print()

nama_depan = nama.split()[0]
nama_depan_tuple = tuple(nama_depan)
print(f"NAMA DEPAN:  {nama_depan_tuple}")
print()

nama_terbalik = tuple(reversed(nama.split()))
print(f"NAMA TERBALIK:  {nama_terbalik}")
