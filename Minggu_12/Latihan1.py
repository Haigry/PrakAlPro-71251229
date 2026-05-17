# Latihan 11.1
# Buatlah program untuk melakukan pengecekan apakah semua anggota yang ada
# didalam tuple sama.

def cek_semua_sama(t):
    return len(set(t)) == 1

if __name__ == "__main__":
    tA = (90, 90, 90, 90)
    print(f"tA= {tA}")
    print()
    print("Output")
    print(cek_semua_sama(tA))
