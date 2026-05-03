def tiga_terbaik(data):
    data_urut = sorted(data, reverse=True)
    return data_urut[:3]

if __name__ == "__main__":
    angka = [10, 5, 8, 20, 20, 4, 30, 25, 30]
    hasil = tiga_terbaik(angka)
    print(f"Data awal: {angka}")
    print(f"3 Bilangan terbaik: {hasil}")
