#Contoh 4.1
inputuser = input("Masukkan suhu tubuh (derajat Celcius): ")
try:
    suhu = float(inputuser)
    if suhu >= 38:
        print("Anda demam")
    else:
        print("Anda tidak demam")
except ValueError:
    print("Input tidak valid! Masukkan angka suhu tubuh yang benar.")

#Contoh 4.2
inputuser = input("Masukkan suatu bilangan: ")
try:
    bilangan = int(inputuser)
    if bilangan > 0:
        print("Positif")
    elif bilangan < 0:
        print("Negatif")
    elif bilangan == 0:
        print("Nol")
except ValueError:
    print("Input tidak valid! Masukkan bilangan bulat yang benar.")


#Contoh 4.3
try:
    a = int(input("Masukkan bilangan pertama: "))
    b = int(input("Masukkan bilangan kedua: "))
    c = int(input("Masukkan bilangan ketiga: "))

    if a > b and a > c:
        print("Terbesar:", a)
    elif b > a and b > c:
        print("Terbesar:", b)
    elif c > a and c > b:
        print("Terbesar:", c)
    else:
        print("Ada dua atau lebih bilangan yang sama besar.")

except ValueError:
    print("Input tidak valid! Semua input harus berupa bilangan bulat.")
