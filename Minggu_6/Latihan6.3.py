def hitung_ips(jumlah_mk):
    bobot = {'A': 4, 'B': 3, 'C': 2, 'D': 1}
    sks_per_mk = 3
    total_bobot = 0
    total_sks = 0

    for i in range(1, jumlah_mk + 1):
        nilai = input(f'Nilai MK {i}: ').upper()
        if nilai in bobot:
            total_bobot += bobot[nilai] * sks_per_mk
            total_sks   += sks_per_mk
        else:
            print('Nilai tidak valid, dilewati.')

    if total_sks > 0:
        return round(total_bobot / total_sks, 2)
    else:
        return 0

print('Program penghitung IPS Mahasiswa')
jumlah = int(input('Berapa jumlah mata kuliah? '))
ips = hitung_ips(jumlah)
print(f'Nilai IPS anda semester ini {ips}')
