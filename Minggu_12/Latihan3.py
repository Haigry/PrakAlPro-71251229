# Latihan 11.3

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
        if len(words) < 6:
            continue
        waktu = words[5]
        jam = waktu.split(':')[0]
        jam_counts[jam] = jam_counts.get(jam, 0) + 1

    fhand.close()

    lst = sorted(jam_counts.items())

    for jam, jumlah in lst:
        print(jam, jumlah)


if __name__ == "__main__":
    nama_file = input("Enter a file name: ")
    hitung_distribusi_jam(nama_file)
