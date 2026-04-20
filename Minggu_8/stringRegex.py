namasaya = "Antonius Rachmat C"
temansaya1 = "Yuan Lukito"
temansaya2 = 'Laurentius Kuncoro'
temansaya3 = "Matahari" + 'Bakti'

print(temansaya3)         # MatahariiBakti
print(namasaya[0])        # 'A'
print(namasaya[9])        # 'R'
print(temansaya1[1])      # 'u'

huruf = temansaya2[0]
print(huruf)              # 'L'

kalimat = "cerita rakyat"
awal = 0
akhir = 6
print(kalimat[awal:akhir])          # cerita
print(kalimat[7:len(kalimat)])       # rakyat
print(kalimat[:5])                  # cerit
print(kalimat[5:])                  # a rakyat
print(kalimat[:])                   # cerita rakyat
print(kalimat[::-1])                # taykar atirc (dibalik)

kalimat = "indonesia jaya"
i = 0
while i < len(kalimat):
    print(kalimat[i], end='')
    i += 1

kalimat = "indonesia jaya"
for kal in kalimat:
    print(kal, end='')

kalimat = "saya mau makan"
data = "saya"
print(data in kalimat)         # True
print("mau" in kalimat)       # True
print("dia" in kalimat)       # False

# Perbandingan string
if "saya" > "dia":
    print("Ya")               # Ya
if "dua" == "dua":
    print("Sama")             # Sama

kalimat = "universitas kristen duta wacana yogyakarta"
print(len(kalimat))              # output 42

terakhir = kalimat[len(kalimat)-1]
print(terakhir)                  # output 'a'

terakhir_versi2 = kalimat[-1]
print(terakhir_versi2)           # output 'a'
terakhir2 = kalimat[-2]
print(terakhir2)                 # output 't'

kata1 = "saya"
kata2 = "makan"
kata3 = kata1 + " " + kata2
print(kata3)                     # saya makan

kata4 = "ulang "
print(kata4 * 4)                 # ulang ulang ulang ulang
