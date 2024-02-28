# Dictionary dalam dictionary untuk list penjualan Data Subhan's Store

# Data Awal
barang = {
    1: {'Nama': 'Pensil', 'Harga': 3000, 'Jumlah': 103},
    2: {'Nama': 'Buku', 'Harga': 20000, 'Jumlah': 132},
    3: {'Nama': 'Pulpen', 'Harga': 5000, 'Jumlah': 90},
    4: {'Nama': 'Sepatu', 'Harga': 150000, 'Jumlah': 86},
    5: {'Nama': 'Penghapus', 'Harga': 4000, 'Jumlah': 100},
    6: {'Nama': 'Penggaris', 'Harga': 6000, 'Jumlah': 84},
}

# Menampilkan menu opsi data penjualan dan meminta user untuk menginput pilihan menu
def subhanStore():
    while True:
        menuOption = int(input('''
    ================================== SELAMAT DATANG DI SUBHAN'S STORE ==================================
    Main Menu:
    1. Lihat Data Penjualan
    2. Tambah Data Penjualan
    3. Ubah Data Penjualan
    4. Hapus Data Penjualan
    5. Statistik Penjualan
    6. Keluar Program

    Masukkan Pilihan Menu yang ingin dijalankan (1-5): '''))
        
        if menuOption == 1:
            lihatData()
        elif menuOption == 2:
            tambahData()
        elif menuOption == 3:
            ubahData()
        elif menuOption == 4:
            hapusData()
        elif menuOption == 5:
            Statistik()
        elif menuOption == 6:
            break
        else:   
             print("\n\tMohon maaf, pilihan menu yang Anda masukkan tidak valid.") #--> Memunculkan tidak validnya data jika data yg diinput salah

#===============================================================FUNGSI CREATE DATA===================================================================================
# Untuk menambahkan data baru 
def tambahData():
    while True:
        subMenuOption = int(input('''
    Tambah Data Penjualan
    1. Tambah Data Baru 
    2. Kembali ke Menu Utama

    Pilih Sub-Menu: '''))

        if subMenuOption == 1:
            # Menginput primary key/unique column (ID) data yang ditambahkan
            idTambah = int(input('''
    Tambah Data Baru
    Masukkan Nomor ID data yang ingin ditambahkan: '''))

            
            if idTambah in barang:
                print("\n\tMaaf, Nomor ID data ({}) sudah ada.".format(idTambah))
            else:
                # Untuk menambahkan data penjualan ke dalam dictionary
                barang[idTambah] = {}
                # Menginput data penjualan baru
                print("\nTambah Data Penjualan Baru")
                namaBarang = input("\tMasukkan nama barang: ")
                hargaBarang = int(input("\tMasukkan harga barang: "))
                jumlahBarang = int(input("\tMasukkan jumlah barang terjual: "))

                simpanData = input("\tApakah Anda yakin ingin menyimpan data baru dengan Nomor ID: {}? " #--> Memunculkan apakah data akan disimpan
                                    .format(idTambah))

                if simpanData.lower() == "ya":
                    print("\n\tSukses, data berhasil ditambahkan.")
                    barang[idTambah]['Nama'] = namaBarang
                    barang[idTambah]['Harga'] = hargaBarang
                    barang[idTambah]['Jumlah'] = jumlahBarang
                else:
                    print("\n\tMaaf, data tidak berhasil ditambahkan.") 
        # Akan kembali ke menu utama
        elif subMenuOption == 2:
            break
        else:
            print("\n\tMaaf, pilihan sub-menu tidak valid.")

#===============================================================FUNGSI READ DATA===================================================================================
# Untuk menampilkan data secara keseluruhan dan salah satu data
def lihatData():
    garis = '=' * 60 

    while True:
        subMenuOption = int(input('''
    Lihat Data Penjualan
    1. Tampilkan Seluruh Data Penjualan 
    2. Cari Data Penjualan Berdasarkan Nomor ID
    3. Kembali ke Menu Utama

    Masukkan Pilihan Sub-Menu: '''))

        if subMenuOption == 1:
            if not barang:
                # Menampilkan tidak adanya data penjualan
                print("\n\tMaaf, tidak ada data penjualan yang dapat ditampilkan.")
            else: 
                totalPenjualan = 0      #--> menampilkan kolom "Total" pada setiap baris
                
                print("""
    Tampilkan Seluruh Data Penjualan
    {}
    {:>2} | {:<15} | {:<10} | {:<6} | {}
    {}""".format(garis, "No", "Nama Barang", "Harga", "Jumlah", "Total", garis))

                for i in barang:
                    total = barang[i]['Harga'] * barang[i]['Jumlah'] #--> harga barang dikalikan dengan jumlah barang
                    totalPenjualan += total     
                    print("\t{:>2} | {:<15} | Rp. {:<6} | {:<6} | Rp. {}".format
                          (i, barang[i]['Nama'], barang[i]['Harga'], barang[i]['Jumlah'], total))
        # Menginput primary key/unique column (ID) data yang ditambahkan
        elif subMenuOption == 2:
            idCari = int(input('''
    Cari Data Berdasarkan Nomor ID
    Masukkan Nomor ID data yang ingin dicari: '''))
            # Untuk mencari (ID)  
            if idCari not in barang.keys():
                print("\n\tMaaf, Nomor ID data ({}) tidak ditemukan.".format(idCari))
            else:
                total = barang[idCari]['Harga'] * barang[idCari]['Jumlah']
                print("""
    Tampilkan Data Penjualan Berdasarkan Nomor ID: {}
    {}
    {} | {:<15} | {:<10} | {:<6} | {}
    {}
    {:>2} | {:<15} | Rp. {:<6} | {:<6} | Rp. {}
    {}""".format(idCari, garis, "No", "Nama Barang", "Harga", "Jumlah", "Total", garis, idCari,
                 barang[idCari]['Nama'], barang[idCari]['Harga'], barang[idCari]['Jumlah'], total, garis))
        # Akan kembali ke menu utama
        elif subMenuOption == 3:
            break
        else:
            print("\n\tMaaf, pilihan sub-menu tidak valid.")

#===============================================================FUNGSI UPDATE DATA===================================================================================
# Untuk mengubah data sesuai nomor barang 
def ubahData():
    garis = '=' * 60

    while True:
        subMenuOption = int(input('''
    Ubah Data Penjualan
     1. Ubah Data
     2. Kembali ke Menu Utama

    Masukkan Pilihan Sub-Menu: '''))
        
        if subMenuOption == 1:
            # Menginput primary key/unique column (ID) data yang ingin dihapus
            idUbah = int(input('''
    Ubah Data Penjualan
    Masukkan Nomor ID data yang ingin diubah: '''))
            
            if idUbah not in barang.keys():
                print("\n\tMaaf, Nomor ID data ({}) tidak ditemukan.".format(idUbah))
            else :
                total = barang[idUbah]['Harga'] * barang[idUbah]['Jumlah']
                print("""
    Tampilkan Data Penjualan Berdasarkan Nomor ID: {}
    {}
    {} | {:<15} | {:<10} | {:<6} | {}
    {}
    {:>2} | {:<15} | Rp. {:<6} | {:<6} | Rp. {}
    {}""".format(idUbah, garis, "No", "Nama Barang", "Harga", "Jumlah", "Total", garis, idUbah,
                 barang[idUbah]['Nama'], barang[idUbah]['Harga'], barang[idUbah]['Jumlah'],
                 total, garis))
                print("\n\tUbah Data Penjualan Untuk Nomor ID: {}".format(idUbah))
                # Menginput kolom yang akan diubah
                ubahNama = input("\tApakah Anda ingin mengganti nama barang? ")

                if ubahNama.lower() == "ya":
                    namaBarang = input("\tMasukkan nama barang: ")
                else:
                    namaBarang = barang[idUbah]['Nama']

                ubahHarga = input("\tApakah Anda ingin mengganti harga barang? ")

                if ubahHarga.lower() == "ya":
                    hargaBarang = int(input("\tMasukkan harga barang: "))
                else:
                    hargaBarang = barang[idUbah]['Harga']
                ubahJumlah = input("\tApakah Anda ingin mengganti jumlah barang terjual? ")

                if ubahJumlah.lower() == "ya":
                    jumlahBarang = int(input("\tMasukkan jumlah barang terjual: "))
                else:
                    jumlahBarang = barang[idUbah]['Jumlah']

                print("\n\tSukses, data berhasil diubah.")
                barang[idUbah]['Nama'] = namaBarang
                barang[idUbah]['Harga'] = hargaBarang
                barang[idUbah]['Jumlah'] = jumlahBarang
        # Akan kembali ke menu utama
        elif subMenuOption == 2:
            break
        else:
            print("\n\tMaaf, pilihan sub-menu tidak valid.")

#===============================================================FUNGSI DELETE DATA===================================================================================
# Untuk menghapus salah satu data sesuai nomor nama barang
def hapusData():
    while True:
        subMenuOption = int(input('''
    Hapus Data Penjualan
    1. Hapus Data
    2. Kembali ke Menu Utama

    Masukkan Pilihan Sub-Menu: '''))
        
        if subMenuOption == 1:
            # Menginput primary key/unique column (ID) data yang ingin dihapus
            idDelete = int(input('''
    Hapus Data Penjualan
    Masukkan Nomor ID data yang ingin dihapus: '''))

            if idDelete not in barang.keys():
                print("\n\tMaaf, Nomor ID data ({}) tidak ditemukan.".format(idDelete))
            else:     
                hapusData = input("\n\tApakah Anda yakin ingin menghapus data dengan Nomor ID: {}? "
                                   .format(idDelete))
                if hapusData.lower() == "ya":
                    print("\n\tSukses, data berhasil dihapus.")
                    del barang[idDelete]
                else:
                    print("\n\tMaaf, data tidak berhasil dihapus.")
        # Akan kembali ke menu utama
        elif subMenuOption == 2:
            break
        else:
            print("\n\tMaaf, pilihan sub-menu tidak valid.")

#===============================================================FUNGSI STATISTIK DATA===================================================================================
# Untuk melihat data penjualan terbanyak dan dat penjualan terkecil
def Statistik():
    while True:
        subMenuOption = int(input('''
    Statistik Penjualan
    1. Lihat Penjualan Terbanyak
    2. Lihat Penjualan Terkecil
    3. Kembali ke Menu Utama

    Masukkan Pilihan Sub-Menu: '''))

        if subMenuOption == 1:
            lihatPenjualanTerbanyak()
        elif subMenuOption == 2:
            lihatPenjualanTerkecil()
        elif subMenuOption == 3:    #--> # Akan kembali ke menu utama
            break
        else:
            print("\n\tMaaf, pilihan sub-menu tidak valid.")

def lihatPenjualanTerbanyak():
    if not barang:
        print("\n\tMaaf, tidak ada data penjualan yang dapat ditampilkan.")
    else:
        sorted_barang = sorted(barang.items(), key=lambda x: x[1]['Jumlah'], reverse=True)
        
        print("\nPenjualan Terbanyak:")
        print("=" * 40)
        print("Nama Barang: {}".format(sorted_barang[0][1]['Nama']))
        print("Jumlah Terjual: {}".format(sorted_barang[0][1]['Jumlah']))
        print("=" * 40)


def lihatPenjualanTerkecil():
    if not barang:
        print("\n\tMaaf, tidak ada data penjualan yang dapat ditampilkan.")
    else:
        sorted_barang = sorted(barang.items(), key=lambda x: x[1]['Jumlah'])
        
        print("\nPenjualan Terkecil:")
        print("=" * 40)
        print("Nama Barang: {}".format(sorted_barang[0][1]['Nama']))
        print("Jumlah Terjual: {}".format(sorted_barang[0][1]['Jumlah']))
        print("=" * 40)



subhanStore()
