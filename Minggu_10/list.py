
# Perubahan di dalam fungsi MEMENGARUHI list asli
def ubah(data):
    data[0] = 'anton'

data = ['a', 'b', 'c']
ubah(data)
print(data)   # ['anton', 'b', 'c']  ← list asli berubah!

# Fungsi yang mengembalikan list baru (tanpa mengubah asli)
def hapus_pertama(data):
    return data[1:]    # slice = buat list baru

data = ['anton', 'b', 'c']
baru = hapus_pertama(data)
print(baru)   # ['b', 'c']
print(data)   # ['anton', 'b', 'c']  ← asli tidak berubah

# Jika ingin asli berubah, simpan hasilnya
data = hapus_pertama(data)
print(data)   # ['b', 'c']
