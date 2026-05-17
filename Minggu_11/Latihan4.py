# Latihan 11.4

def hitung_domain(nama_file):
    try:
        fhand = open(nama_file)
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak bisa dibuka!")
        return

    domain_counts = dict()
    for line in fhand:
        if not line.startswith('From:'):
            continue
        words = line.split()
        if len(words) < 2:
            continue
        email = words[1]
        if '@' in email:
            domain = email.split('@')[1]
            domain_counts[domain] = domain_counts.get(domain, 0) + 1

    fhand.close()
    print(domain_counts)


if __name__ == "__main__":
    nama_file2 = input("Masukkan nama file: ")
    hitung_domain(nama_file2)
