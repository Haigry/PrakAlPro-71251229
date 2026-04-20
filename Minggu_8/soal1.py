def cek_anagram(kata1, kata2):
    kata1 = kata1.lower().replace(" ", "")
    kata2 = kata2.lower().replace(" ", "")

    return sorted(kata1) == sorted(kata2)

kata1 = input("Masukkan kata pertama: ")
kata2 = input("Masukkan kata kedua: ")
if cek_anagram(kata1, kata2):
    print(f'"{kata1}" adalah anagram dari "{kata2}"')
else:
    print(f'"{kata1}" BUKAN anagram dari "{kata2}"')
