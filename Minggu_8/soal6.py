import re
import random
import string

teks = """Berikut adalah daftar email dan nama pengguna dari mailing list:
anton@mail.com dimiliki oleh antonius
budi@gmail.co.id dimiliki oleh budi anwari
slamet@getnada.com dimiliki oleh slamet slumut
matahari@tokopedia.com dimiliki oleh toko matahari"""

emails = re.findall(r'[\w.]+@[\w.]+', teks)

print("Hasil:")
for email in emails:
    username = email.split('@')[0]
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    print(f"{email} username: {username} , password: {password}")
