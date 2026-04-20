import re
from datetime import datetime

def proses_tanggal(teks):
    pola = r'\d{4}-\d{2}-\d{2}'
        
    tanggal_list = re.findall(pola, teks)
        
    hari_ini = datetime.today()
        
    for tgl_str in tanggal_list:
        tgl = datetime.strptime(tgl_str, '%Y-%m-%d')
            
        selisih = abs((hari_ini - tgl).days)
            
        tgl_baru = tgl.strftime('%d-%m-%Y')
        print(f"{tgl_str} -> {tgl_baru}, selisih {selisih} hari")

teks = """Pada tanggal 1945-08-17 Indonesia merdeka.
Pangeran Diponegoro (TL: 1785-11-11),
Pattimura (TL: 1783-06-08) dan
Ki Hajar Dewantara (1889-05-02)."""

proses_tanggal(teks)
