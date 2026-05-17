# Latihan 11.3
# Buatlah program untuk menghitung distribusi jam dalam satu hari dimana ada
# pesan yang diterima dari setiap email yang masuk. Gunakan file mbox-short.txt
# untuk sebagai datanya.

def hitung_distribusi_jam(nama_file):
    try:
        fhand = open(nama_file)
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak bisa dibuka!")
        return

    jam_counts = dict()
    for line in fhand:
        if not line.startswith('From '):
            continue
        words = line.split()
        # Format: From email weekday month day HH:MM:SS year
        if len(words) < 6:
            continue
        waktu = words[5]          # contoh: '09:14:16'
        jam = waktu.split(':')[0]  # ambil bagian jam saja
        jam_counts[jam] = jam_counts.get(jam, 0) + 1

    fhand.close()

    # Urutkan berdasarkan jam (sebagai list of tuples)
    lst = sorted(jam_counts.items())

    for jam, jumlah in lst:
        print(jam, jumlah)


if __name__ == "__main__":
    nama_file = input("Enter a file name: ")
    hitung_distribusi_jam(nama_file)
