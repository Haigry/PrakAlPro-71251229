# Program Perhitungan Gaji dan Pengeluaran Budi
# Liburan selama 5 minggu

print('='*60)
print('PROGRAM PERHITUNGAN GAJI DAN PENGELUARAN')
print('Liburan Semester (5 Minggu)')
print('='*60)

# INPUT dari pengguna
gaji_per_jam = eval(input('Gaji per jam yang diinginkan (Rp): '))
jam_per_minggu = eval(input('Jumlah jam kerja per minggu: '))
7
# KONSTANTA
MINGGU_KERJA = 5
PAJAK = 0.14         # 14%
BAJU_AKSESORIS = 0.10  # 10%
ALAT_TULIS = 0.01      # 1%
SEDEKAH = 0.25         # 25%
ANAK_YATIM = 0.30      # 30% dari sedekah
DHUAFA = 0.70          # 70% dari sedekah

# PERHITUNGAN
# 1. Pendapatan sebelum pajak
total_jam = jam_per_minggu * MINGGU_KERJA
pendapatan_kotor = gaji_per_jam * total_jam

# 2. Pajak dan pendapatan bersih
jumlah_pajak = pendapatan_kotor * PAJAK
pendapatan_bersih = pendapatan_kotor - jumlah_pajak

# 3. Pengeluaran untuk baju dan aksesoris
uang_baju = pendapatan_bersih * BAJU_AKSESORIS

# 4. Pengeluaran untuk alat tulis
uang_alat_tulis = pendapatan_bersih * ALAT_TULIS

# 5. Sisa uang setelah belanja
sisa_uang = pendapatan_bersih - uang_baju - uang_alat_tulis

# 6. Sedekah
total_sedekah = sisa_uang * SEDEKAH
sedekah_yatim = total_sedekah * ANAK_YATIM
sedekah_dhuafa = total_sedekah * DHUAFA

# 7. Sisa akhir
sisa_akhir = sisa_uang - total_sedekah

# OUTPUT
print('\n' + '='*60)
print('HASIL PERHITUNGAN')
print('='*60)
print(f'Total jam kerja: {total_jam} jam ({jam_per_minggu} jam/minggu × {MINGGU_KERJA} minggu)')
print()
print('PENDAPATAN:')
print(f'1. Pendapatan sebelum pajak  : Rp {pendapatan_kotor:,.2f}')
print(f'2. Pendapatan setelah pajak  : Rp {pendapatan_bersih:,.2f}')
print(f'   (Pajak 14% = Rp {jumlah_pajak:,.2f})')
print()
print('PENGELUARAN:')
print(f'3. Baju dan aksesoris (10%)  : Rp {uang_baju:,.2f}')
print(f'4. Alat tulis (1%)           : Rp {uang_alat_tulis:,.2f}')
print()
print('SEDEKAH:')
print(f'5. Total sedekah (25%)       : Rp {total_sedekah:,.2f}')
print(f'6. Untuk anak yatim (30%)    : Rp {sedekah_yatim:,.2f}')
print(f'7. Untuk kaum dhuafa (70%)   : Rp {sedekah_dhuafa:,.2f}')
print()
print(f'Sisa uang Budi akhir         : Rp {sisa_akhir:,.2f}')
print('='*60)
