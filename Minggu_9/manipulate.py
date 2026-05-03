import re

def CountWisnu(userinp):
    try:
        handle = open(userinp)
        isi = handle.read()
        d = re.findall('Wisnu', isi)
        print(len(d))
        print(d)
    except:
        print("File Tidak Ada Prof")

if __name__ == "__main__":
    userinp = str(input())
    CountWisnu(userinp)