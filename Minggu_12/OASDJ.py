# Cara membuat tuple
t1 = ('a', 'b', 'c', 'd', 'e')
t2 = 'a', 'b', 'c', 'd', 'e'  # tanpa kurung juga valid

# Tuple dengan satu elemen (perlu koma!)
t3 = ('a',)  # ini tuple
t4 = ('a')   # ini STRING, bukan tuple

# Tuple kosong
t5 = tuple()

# Membuat tuple dari string
t6 = tuple('Python')
print(t6)  # ('P', 'y', 't', 'h', 'o', 'n')

# Perbandingan tuple
print((0, 1, 2) < (0, 3, 4))          # True
print((0, 1, 2000000) < (0, 3, 4))    # True (cek elemen ke-2)
print(('a', 'b') < ('a', 'c'))        # True

# Mengurutkan list of tuples
data = [(3, 'tiga'), (1, 'satu'), (2, 'dua')]
data.sort()
print(data)  # [(1, 'satu'), (2, 'dua'), (3, 'tiga')]

# Urutan terbalik (descending)
data.sort(reverse=True)
print(data)  # [(3, 'tiga'), (2, 'dua'), (1, 'satu')]

# Concatenation
t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)  # (1, 2, 3, 4, 5, 6)

# Repetition
t4 = ('ha',) * 3
print(t4)  # ('ha', 'ha', 'ha')

# Membership
print(3 in t1)      # True
print(10 in t1)     # False

# Panjang tuple
print(len(t1))      # 3


t = ('a', 'b', 'c', 'd', 'e')

# Akses elemen
print(t[0])    # 'a'
print(t[-1])   # 'e'

# Slicing
print(t[1:3])  # ('b', 'c')
print(t[:2])   # ('a', 'b')
print(t[2:])   # ('c', 'd', 'e')

# Tuple immutable - tidak bisa diubah
# t[0] = 'A'  # ERROR: TypeError

# Tapi bisa diganti keseluruhan
t = ('A',) + t[1:]
print(t)  # ('A', 'b', 'c', 'd', 'e')

# Tuple assignment dasar
x, y = 10, 20
print(x)  # 10
print(y)  # 20

# Unpacking list/tuple
data = ['Alice', 25, 'Jakarta']
nama, umur, kota = data
print(nama)  # Alice

# Swap variabel (tanpa variabel temporary!)
a, b = 5, 10
a, b = b, a
print(a, b)  # 10 5

# Split dan assign
email = 'user@domain.com'
username, domain = email.split('@')
print(username)  # user
print(domain)    # domain.com


# Dictionary to list of tuples
d = {'a': 10, 'b': 1, 'c': 22}
t = list(d.items())
print(t)
# [('a', 10), ('b', 1), ('c', 22)]

# Urutkan berdasarkan key
t.sort()
print(t)
# [('a', 10), ('b', 1), ('c', 22)]


# Iterasi dictionary dengan tuple assignment
d = {'a': 10, 'b': 1, 'c': 22}

for key, val in d.items():
    print(f'{key}: {val}')
# a: 10
# c: 22
# b: 1


d = {'a': 10, 'b': 1, 'c': 22}

# Buat list (value, key)
lst = []
for key, val in d.items():
    lst.append((val, key))

# Sort descending
lst.sort(reverse=True)
print(lst)
# [(22, 'c'), (10, 'a'), (1, 'b')]

# Cetak hasil
for val, key in lst:
    print(f'{key}: {val}')
# c: 22
# a: 10
# b: 1
