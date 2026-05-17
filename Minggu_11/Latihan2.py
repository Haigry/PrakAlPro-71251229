# Latihan 11.2

def petakan_dua_list(lista, listb):
    hasil = dict(zip(lista, listb))
    return hasil

if __name__ == "__main__":
    lista = ['red', 'green', 'blue']
    listb = ['#FF0000', '#008000', '#0000FF']

    print(f"Lista = {lista}")
    print(f"Listb = {listb}")

    hasil = petakan_dua_list(lista, listb)
    print(f"\nOutput:")
    print(hasil)
