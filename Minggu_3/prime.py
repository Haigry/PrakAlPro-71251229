# Program untuk mengecek apakah suatu bilangan adalah bilangan prima

def cek_prima(bilangan):
    if bilangan <= 1:
        return False
    if bilangan <= 3:
        return True
    if bilangan % 2 == 0 or bilangan % 3 == 0:
        return False
    i = 5
    while i * i <= bilangan:
        if bilangan % i == 0 or bilangan % (i + 2) == 0:
            return False
        i += 6
    return True

# Input dari pengguna
bilangan = int(input("Masukkan bilangan: "))

# Cek dan tampilkan hasil
if cek_prima(bilangan):
    print(f"{bilangan} adalah bilangan prima")
else:
    print(f"{bilangan} bukan bilangan prima")