def is_prima(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prima_terdekat(n):
    kandidat = n - 1
    while kandidat >= 2:
        if is_prima(kandidat):
            return kandidat
        kandidat -= 1
    return None 

n = int(input("Masukkan nilai n: "))

hasil = prima_terdekat(n)

if hasil is not None:
    print(f"Prima terdekat < {n} adalah {hasil}")
else:
    print(f"Tidak ada bilangan prima yang kurang dari {n}")
