def cek_digit_belakang(a, b, c):
    digit_a = a % 10
    digit_b = b % 10
    digit_c = c % 10

    return (digit_a == digit_b) or (digit_b == digit_c) or (digit_a == digit_c)

a = int(input("Masukkan angka pertama : "))
b = int(input("Masukkan angka kedua   : "))
c = int(input("Masukkan angka ketiga  : "))

print(cek_digit_belakang(a, b, c))
