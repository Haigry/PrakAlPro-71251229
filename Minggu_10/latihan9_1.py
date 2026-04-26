def bandingkan_file(file1, file2):
    try:
        with open(file1, 'r') as f1:
            baris1 = f1.readlines()
    except FileNotFoundError:
        print(f"File '{file1}' tidak ditemukan.")
        return

    try:
        with open(file2, 'r') as f2:
            baris2 = f2.readlines()
    except FileNotFoundError:
        print(f"File '{file2}' tidak ditemukan.")
        return

    # Samakan panjang kedua list
    max_baris = max(len(baris1), len(baris2))
    ada_perbedaan = False

    for i in range(max_baris):
        b1 = baris1[i].rstrip('\n') if i < len(baris1) else "<tidak ada baris>"
        b2 = baris2[i].rstrip('\n') if i < len(baris2) else "<tidak ada baris>"

        if b1 != b2:
            ada_perbedaan = True
            print(f"Baris {i + 1}:")
            print(f"  File 1 : {b1}")
            print(f"  File 2 : {b2}")

    if not ada_perbedaan:
        print("Kedua file identik, tidak ada perbedaan.")

if __name__ == "__main__":
    nama_file1 = input("nama file1: ")
    nama_file2 = input("nama file2: ")
    bandingkan_file(nama_file1, nama_file2)
