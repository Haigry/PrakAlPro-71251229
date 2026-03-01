try:
    bilangan = int(input("Masukkan suatu bilangan: "))
    hasil = "Positif" if bilangan > 0 else ("Negatif" if bilangan < 0 else "Nol")
    print(hasil)
except ValueError:
    print("Input tidak valid! Masukkan bilangan bulat.")
