# Latihan 11.3


def hitung_email(nama_file):
    try:
        fhand = open(nama_file)
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak bisa dibuka!")
        return

    counts = dict()
    for line in fhand:
        # Baris From: diikuti alamat email: "From: email@domain.com"
        if not line.startswith('From:'):
            continue
        words = line.split()
        if len(words) < 2:
            continue
        email = words[1]
        counts[email] = counts.get(email, 0) + 1

    fhand.close()
    print(counts)

if __name__ == "__main__":
    nama_file = input("Masukkan nama file : ")
    hitung_email(nama_file)
