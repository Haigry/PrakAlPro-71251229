def faktorial(num):
    hasil = 1
    for i in range(1, num + 1):
        hasil *= i
    return hasil

n = int(input("Masukkan nilai n: "))

for baris in range(n, 0, -1):
    fak = faktorial(baris)

    deret = " ".join(str(i) for i in range(baris, 0, -1))

    print(f"{fak} {deret}")
