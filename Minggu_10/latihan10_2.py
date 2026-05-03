def main():
    bilangan = []
    while True:
        inp = input("Masukkan bilangan (atau ketik 'done' untuk berhenti): ")
        if inp.lower() == 'done':
            break
        try:
            num = float(inp)
            bilangan.append(num)
        except ValueError:
            print("Input tidak valid, silakan masukkan bilangan atau 'done'.")
    
    if len(bilangan) > 0:
        rata = sum(bilangan) / len(bilangan)
        print(f"\nList bilangan yang dimasukkan: {bilangan}")
        print(f"Rata-rata: {rata}")
    else:
        print("Tidak ada bilangan yang dimasukkan.")

if __name__ == "__main__":
    main()
