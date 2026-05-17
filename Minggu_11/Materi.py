# Cara 1: Dictionary kosong menggunakan dict()
kamus = dict()

# Cara 2: Dictionary kosong menggunakan kurung kurawal
kamus2 = {}

# Cara 3: Dictionary dengan isi langsung (key:value)
mahasiswa = {
    'nim'   : '71251229',
    'nama'  : 'Ignatius Harya',
    'prodi' : 'Informatika',
    'ipk'   : 3.85
}

# Cara 4: Menggunakan dict() dengan keyword arguments
mobil = dict(merk='Toyota', tahun=2022, warna='Merah')

# Cara 5: Dari list of tuples
pasangan = [('a', 1), ('b', 2), ('c', 3)]


eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}

# Mengakses nilai dengan kunci
print(eng2sp['two'])           # Output: dos

# Mengakses nilai dengan .get() — aman dari KeyError
print(eng2sp.get('four'))      # Output: None
print(eng2sp.get('four', '-')) # Output: - (nilai default)

# Menambah item baru
eng2sp['four'] = 'cuatro'
print(eng2sp)

# Mengubah nilai yang sudah ada
eng2sp['one'] = 'UNO'
print(eng2sp['one'])           # Output: UNO

# Menghapus item dengan del
del eng2sp['four']
print(eng2sp)

# Menghapus item dengan .pop() — mengembalikan nilai yang dihapus
nilai = eng2sp.pop('three')
print(nilai)                   # Output: tres

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# .keys()   mengembalikan semua kunci
print(list(data.keys()))       # ['a', 'b', 'c', 'd']

# .values() mengembalikan semua nilai
print(list(data.values()))     # [1, 2, 3, 4]

# .items()  mengembalikan semua pasangan (key, value)
print(list(data.items()))
# [('a', 1), ('b', 2), ('c', 3), ('d', 4)]

# .update() menggabungkan/memperbarui dictionary
tambahan = {'e': 5, 'a': 99}  # 'a' akan ditimpa
data.update(tambahan)
print(data)   # {'a': 99, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# .clear()  mengosongkan dictionary
sementara = {'x': 1, 'y': 2}
sementara.clear()
print(sementara)              # {}

# .copy()   membuat salinan dangkal (shallow copy)
data2 = data.copy()
data2['a'] = 0                # tidak mempengaruhi data asli


fname = input('Masukkan nama file: ')
try:
    fhand = open(fname)
except:
    print('File tidak dapat dibuka:', fname)
    exit()

counts = dict()
for line in fhand:          # perulangan luar: tiap baris
    words = line.split()    # pecah baris jadi list kata
    for word in words:      # perulangan dalam: tiap kata
        counts[word] = counts.get(word, 0) + 1

print(counts)


counts = {'chuck': 1, 'annie': 42, 'jan': 100, 'bob': 7}

# Iterasi dengan kunci
for key in counts:
    print(key, counts[key])

# Iterasi key & value sekaligus dengan .items()
for key, value in counts.items():
    print(f'{key}: {value}')

# hanya tampilkan nilai > 10
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])

# Iterasi berurutan alfabet (sorted by key)
lst = list(counts.keys())
lst.sort()
for key in lst:
    print(key, counts[key])

# Iterasi berurutan berdasarkan nilai (sort by value) dari yang terbesar
for key in sorted(counts, key=counts.get, reverse=True):
    print(key, counts[key])

