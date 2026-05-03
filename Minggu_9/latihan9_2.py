def jalankan_kuis(nama_file):
    try:
        with open(nama_file, 'r') as f:
            soal_list = f.readlines()
    except FileNotFoundError:
        print(f"File '{nama_file}' tidak ditemukan.")
        return

    benar = 0
    salah = 0

    for baris in soal_list:
        baris = baris.strip()
        if not baris:
            continue

        # Format: pertanyaan || jawaban
        if '||' not in baris:
            continue

        bagian = baris.split('||')
        pertanyaan = bagian[0].strip()
        jawaban_benar = bagian[1].strip().lower()

        print(pertanyaan)
        jawaban_user = input("Jawab: ").strip().lower()

        if jawaban_user == jawaban_benar:
            print("Jawaban benar!")
            benar += 1
        else:
            print(f"Jawaban salah! Jawaban yang benar adalah: {bagian[1].strip()}")
            salah += 1

    print(f"\n=== Hasil Kuis ===")
    print(f"Benar : {benar}")
    print(f"Salah : {salah}")
    print(f"Total : {benar + salah}")

if __name__ == "__main__":
    nama_file = input("nama file1: ")
    jalankan_kuis(nama_file)
