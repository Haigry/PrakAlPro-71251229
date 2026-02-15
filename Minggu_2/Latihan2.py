# Program Menghitung Fungsi f(x) = 2x^3 + 2x + 15/x
# Input: nilai x (bilangan bulat)
# Output: hasil f(x)

print('='*50)
print('KALKULATOR FUNGSI f(x) = 2x³ + 2x + 15/x')
print('='*50)

# Input nilai x dari pengguna
x = eval(input('Masukkan nilai x (bilangan bulat): '))

# Cek apakah x = 0 (karena tidak bisa dibagi 0)
if x == 0:
    print('Error: x tidak boleh 0 (pembagian dengan 0)')
else:
    # Menghitung setiap komponen fungsi
    komponen1 = 2 * (x ** 3)  # 2x^3
    komponen2 = 2 * x          # 2x
    komponen3 = 15 / x         # 15/x
    
    # Menghitung hasil akhir
    hasil = komponen1 + komponen2 + komponen3
    
    # Menampilkan hasil
    print('\n' + '='*50)
    print('HASIL PERHITUNGAN')
    print('='*50)
    print(f'Nilai x          : {x}')
    print(f'2x³              : {komponen1}')
    print(f'2x               : {komponen2}')
    print(f'15/x             : {komponen3:.2f}')
    print('-'*50)
    print(f'f({x}) = 2({x})³ + 2({x}) + 15/{x}')
    print(f'f({x}) = {hasil:.2f}')
    print('='*50)
