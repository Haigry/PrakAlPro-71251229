
print('='*50)
print('KALKULATOR BERAT BADAN IDEAL')
print('='*50)

tinggi = eval(input('Masukkan tinggi badan (dalam meter): '))
bmi_target = eval(input('Masukkan BMI yang diharapkan: '))

berat = bmi_target * (tinggi ** 2)

# Menampilkan hasil
print('\n' + '='*50)
print('HASIL PERHITUNGAN')
print('='*50)
print(f'Tinggi Badan     : {tinggi} meter')
print(f'BMI Target       : {bmi_target}')
print(f'Berat Badan Ideal: {berat:.2f} kg')
print('='*50)
