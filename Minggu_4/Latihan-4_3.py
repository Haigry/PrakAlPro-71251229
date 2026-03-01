try:
    bulan = int(input("Masukkan bulan (1-12): "))

    if bulan < 1 or bulan > 12:
        print("Bulan yang Anda masukkan tidak valid.")
        print("Masukkan nomor bulan antara 1 sampai 12.")
    elif bulan == 2:
        print("Jumlah hari: 29")
    elif bulan > 2 and bulan % 2 == 0:
        print("Jumlah hari: 30")
    else:
        print("Jumlah hari: 31")

except ValueError:
    print("Input tidak valid! Masukkan angka nomor bulan (1-12).")
