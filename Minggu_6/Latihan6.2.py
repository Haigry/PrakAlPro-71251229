def ganjil(bawah, atas):
    if bawah < atas:
        n = bawah + 1
        if n % 2 == 0:
            n += 1
        while n <= atas:
            print(n, end=', ')
            n += 2
    else:
        n = bawah if bawah % 2 != 0 else bawah - 1
        while n >= atas:
            print(n, end=', ')
            n -= 2

bawah = int(input('Masukkan batas bawah: '))
atas  = int(input('Masukkan batas atas: '))
ganjil(bawah, atas)
