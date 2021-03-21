def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print ("Daftar Kontak:")
        print(f"Nama : {kontak['Nama']}")
        print(f"No.Telepon : {kontak['No.Telepon']}")

def new_kontak():
    Nama = input ("Nama : ")
    Telepon = input ("No.Telepon : ")
    kontak = {
        "Nama" : Nama,
        "No.Telepon" : Telepon
    }
    return kontak 