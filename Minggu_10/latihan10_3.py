def main():
    nama_file = input("Masukkan nama file teks: ")
    try:
        with open(nama_file, 'r', encoding='utf-8') as file:
            teks = file.read()
            for char in ".,!?;:'\"()[]{}":
                teks = teks.replace(char, ' ')

            kata_list = teks.lower().split()
            kata_unik = list(set(kata_list))
            kata_unik.sort()
            
            print(f"\nTotal kata yang unik: {len(kata_unik)}")
            print("Kata-kata unik dalam artikel:")
            for kata in kata_unik:
                print("-", kata)
                
    except:
        print(f"File '{nama_file}' tidak ditemukan.")

if __name__ == "__main__":
    main()
