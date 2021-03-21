import function

daftar_kontak = []
daftar_kontak.append({
    "Nama":"Muhammad Vikri",
    "No.Telepon":"089629170587"
})
daftar_kontak.append({
    "Nama":"Putri",
    "No.Telepon":"085885858493"
})
while True:
    print("Selamat Datang!")
    print("---Menu---")
    print("1.Daftar Kontak")
    print("2.Tambah Kontak")
    print("3.Keluar")


    Menu = input("Pilih Menu : ")

    if Menu == "3":
        break 
    elif Menu == "1":
        function.display_kontak(daftar_kontak)
    elif Menu == "2":
        kontak = function.new_kontak()
        daftar_kontak.append(kontak)
        print ("Kontak berhasil ditambahkan")
    elif Menu !="1,2,3":
        print ("Menu Tidak Tersedia")

print("Program Selesai, Sampai jumpa!")

    
