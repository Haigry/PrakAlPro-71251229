def perkalian(a, b):
    hasil = 0
    penjumlahan = []
    for i in range(a):
        hasil += b
        penjumlahan.append(str(b))
    proses = ' + '.join(penjumlahan)
    print(f'{a} x {b} = {proses} = {hasil}')
    return hasil

a = int(input('Masukkan bilangan pertama: '))
b = int(input('Masukkan bilangan kedua: '))
perkalian(a, b)
