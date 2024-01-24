def anggota():
    print("\n===================================================================================")
    print("\t\t\t   PROJECT AKHIR KONSEP PEMROGRAMAN  ")
    print("\t\t\t   Aplikasi Pemesanan Tiket Bioskop     ")
    print("=====================================================================================\n")
    print("\n------------------------------------------------------------------------------------")
    print("\t\t\t   ||     Kelompok ALGORITMA & PEMROGRAMAN    ||   ")
    print("--------------------------------------------------------------------------------------")
    print("\t\t 1. Mohammad Haekal                        (2307421045) ")
    print("\t\t 2. Rafi Forza Prasetyo                    (2307421036) ")
    print("\t\t 3. Hansha Natalegawa                      (2307421054) ")
    print("\t\t 4. Farrel Arya Putra                      (2307421045) ")
    print("\t\t 5. Valenzky Tesalonika Pangaribuan        (2307421045) ")
    print("\t\t 6. Shanazsiva Nasra                       (2307421045) ")
    print("\t\t 7. Muhammad Irfadillah                    (2307421048) ")
    print(input("tekan [enter] untuk melanjutkan Aplikasi"))


def hari():
    print ("\n")
    print ("====================================================================================")
    print ("\t\t\t   SELAMAT DATANG PARA PENONTON")
    print ("\t\t\t\t     XXI")
    print ("=====================================================================================\n")
    print ("-------------------------------------------------------------------------------------")
    print ("|| \t\t\t              Hari \t\t\t            Harga  ||")
    print ("=====================================================================================")
    print ("|| A.\t\t\t              SENIN\t\t\t            25.000 ||")
    print ("|| B.\t\t\t              SELASA\t\t\t            25.000 ||")
    print ("|| C.\t\t\t              RABU\t\t\t            30.000 ||")
    print ("|| D.\t\t\t              KAMIS\t\t\t            30.000 ||")
    print ("|| E.\t\t\t              JUMAT\t\t\t            35.000 ||")
    print ("|| F.\t\t\t              SABTU\t\t\t            40.000 ||")
    print ("|| G.\t\t\t              MINGGU\t\t\t            40.000 ||")

def namafilm():
   
    print ("-------------------------------------------------------------------------------------")
    print ("|| Kode\t\t\t\t\t\t\t\t             Judul ||")
    print ("=====================================================================================")
    print ("|| BDJ\t\t\t\t\t\t                 13 Bom Di Jakarta ||")
    print ("|| ACK\t\t\t\t\t\t                      Anchika 1995 ||")
    print ("|| AQM\t\t\t\t\t\t                           Aquaman ||")
    print ("|| SSN\t\t\t\t\t\t                    Sehidup Semati ||")
    print ("|| CTU\t\t\t\t\t\t                      Siksa Neraka ||")
    print ("-------------------------------------------------------------------------------------")
    print ("=============================   LAYAR        BIOSKOP   ==============================")
    print ("||        E1     E2     E3     E4     E5     E6     E7     E8     E9     E10       ||")
    print ("||        D1     D2     D3     D4     D5     D6     D7     D8     D9     D10       ||")
    print ("||        C1     C2     C3     C4     C5     C6     C7     C8     C9     C10       ||")
    print ("||        B1     B2     B3     B4     B5     B6     B7     B8     B9     B10       ||")
    print ("||        A1     A2     A3     A4     A5     A6     A7     A8     A9     A10       ||")
    print ("-------------------------------------------------------------------------------------")
    print ("=============================            WAKTU         ==============================")
    print ("-------------------------------------------------------------------------------------")
    print ("||        A.                          10.00-12.00                                  ||")
    print ("||        B.                          12.00-14.00                                  ||")
    print ("||        C.                          14.00-16.00                                  ||")
    print ("||        D.                          16.00-18.00                                  ||")
    print ("||        E.                          18.00-20.00                                  ||")
    print ("-------------------------------------------------------------------------------------")
    print ("=========================      SILAHKAN BUAT PESANAN       ==========================")
    
def tiket():
    
    try:
        hari = input("masukkan hari(a/b/c/d/e/f/g): ")
        film = input("masukkan kode film: ")
        jam = input("masukkan jam tayang: ")
    
        if hari.lower() == "a" :
            nama="senin"
            harga = 25000
        elif hari.lower() == "b":
            nama="selasa"
            harga = 25000
        elif hari.lower() == "c" :
            nama="rabu"
            harga = 30000
        elif hari.lower() == "d":
            nama="kamis"
            harga = 30000
        elif hari.lower() == "e":
            nama="jumat"
            harga = 35000
        elif hari.lower() == "f":
            nama="sabtu"
            harga = 40000
        elif hari.lower() == "g" :
            nama="minggu"
            harga = 40000
        else:
            print("pilihan anda salah")
            
    
        if film.lower() == "bdj" :
            judul = "13 Bom Di Jakarta"
        elif film.lower() == "ack" :
            judul = "Anchika 1995"
        elif film.lower() == "aqm":
            judul = "Aquaman"
        elif film.lower() == "ssn":
            judul = "Sehidup Semati"
        elif film.lower() == "ctu" :
            judul = "Siksa Neraka"
        else:
            print("pilihan anda salah")
            
        n = int(input("masukkan banyak tiket: "))
        kursi_list = []
        for i in range(1,n+1):
            print("\ntiket ke-",i)
            kursi = (input("masukkan kode kursi: "))
            kursi_list.append(kursi)
            
       
        hari = harga
        hari = nama
        total = n * int(harga)
        print("total yang dibayar: ", total)
        
        bayar = input ("masukkan jumlah uang pembayaran: ")
        kembalian = int(bayar) - int(total)
        
        if kembalian < 0:
            print("\nPEMBAYARAN ANDA BELUM CUKUP, HARAP MASUKKAN ULANG")
            print("--------------------------------------------------")
            bayar = input ("masukkan jumlah uang pembayaran:")
            kembalian = int(bayar) - int(total)
            
        list_film = ["bdj","BDJ","ACK","ack","aqm","AQM","ssn","SSN","CTU","ctu"]
        list_kursi = ["A1","A2","A3","A4","A5","A6","A8","A9","A10","B1","B2","B3","B4",
                      "B5","B6","B7","B8","B9","B10","C1","C2","C3","C4","C5","C6","C7",
                      "C8","C9","C10","D1","D2","D3","D4","D5","D6","D7","D8","D9","D10",
                      "E1","E2","E3","E4","E5","E6","E7","E8","E9","E10"]
        list_jam = ["10.00-12.00","12.00-14.00","14.00-16.00","16.00-18.00","18.00-20.00"]
        
        formatted_seats = ", ".join(kursi)

        teks = "=========================================\n\t TIKET BIOSKOP\n=========================================\n\tKUBU DALAM XXI\n=========================================\nfilm: {} \nhari: {}\njam: {} \njumlah tiket: {}\nkode kursi: {}\ntotal: {}\n=========================================\nbayar: {}\nkembalian: {}\n=========================================\n".format(judul, nama, jam, n, ", ".join(kursi_list), total, bayar, kembalian)
        
        if film in list_film and kursi in list_kursi and jam in list_jam:
            file = open("tiket.txt","a")
            file.write(teks)
            file.close()
            print(input("\ntekan [enter] untuk mencetak tiket"))
            cetak()
        else:
            salah()
        
            
    except ValueError:
        print("\nmasukkan nomor")
            
        
def cetak():
    print ("=====================================================================================")
    print ("\t\t\t\t KUBU DALAM XXI")
    print ("=====================================================================================")
    print ("\t\t\t\t CETAK TIKET")
    print ("\t\t\ttiket telah dicetak ambil di file txt")
    print ("\t\t\t\tterimakasi")
    
    print ("-------------------------------------------------------------------------------------")
    print ("========================           selamat menonton         =========================")    
    
def salah():
    print ("=====================================================================================")
    print ("\t\t\t\t KUBU DALAM XXI")
    
    print ("=====================================================================================")
    print ("\t\t\t\t TIKET TIDAK DAPAT DICETAK")
    
    print ("-------------------------------------------------------------------------------------")
    print ("==================           MAAF ATAS KETIDAKNYAMANANNYA         ===================")    

    
    
anggota()
hari()
namafilm()
tiket()

class Menu:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

class Pemesanan:
    def __init__(self):
        self.pesanan = []

    def tambah_pesanan(self, menu, jumlah):
        total_harga = menu.harga * jumlah
        self.pesanan.append({"menu": menu.nama, "jumlah": jumlah, "total_harga": total_harga})

    def tampilkan_pesanan(self):
        if not self.pesanan:
            print("Belum ada pesanan.")
            return

        menu_list = []
        print("Pesanan:")
        for item in self.pesanan:
            print(f"{item['menu']} - {item['jumlah']} pcs - Rp {item['total_harga']}")
            menu_list.append(item['menu'])

        total_biaya = sum(item['total_harga'] for item in self.pesanan)
        print(f"Total biaya: Rp {total_biaya}")

        bayar1 = input("masukkan jumlah uang pembayaran: ")
        kembalian1 = int(bayar1) - total_biaya

        if kembalian1 < 0:
            print("\nPEMBAYARAN ANDA BELUM CUKUP, HARAP MASUKKAN ULANG")
            print("--------------------------------------------------")
            bayar1 = input("masukkan jumlah uang pembayaran:")
            kembalian1 = int(bayar1) - total_biaya

        teks = "=========================================\n\tMENU MAKAN\n=========================================\n\tCINEMA XXI\n=========================================\nMenu:\n {} \ntotal: {}\n=========================================\nbayar: {}\nkembalian: {}\n=========================================\n".format("\n ".join(menu_list), total_biaya, bayar1, kembalian1)

        file = open("menu.txt", "a")
        file.write(teks)
        file.close()
        print(input("\ntekan [enter] untuk mencetak tiket"))
        print("berhasil dicetak")


def menu_bioskop():
    print("\n=======================           MENU MAKANAN XII         ========================")
    print("Daftar Menu Bioskop:")
    for i, menu in enumerate(menu_list, start=1):
        print(f"{i}. {menu.nama} - Rp {menu.harga}")


def pesan_makanan():
    pemesanan_user = Pemesanan()

    while True:
        menu_bioskop()
        pilihan = input("Pilih menu XII (1-5) atau ketik 'selesai' jika tidak memesan: ")

        if pilihan.lower() == 'selesai':
            break

        try:
            pilihan_menu = int(pilihan)
            if 1 <= pilihan_menu <= 5:
                jumlah = int(input("Masukkan jumlah pesanan: "))
                pemesanan_user.tambah_pesanan(menu_list[pilihan_menu - 1], jumlah)

            else:
                print("Pilihan tidak valid. Silakan pilih 1-5.")
        except ValueError:
            print("Masukkan angka yang valid.")

    print("\nPesanan Anda:")
    pemesanan_user.tampilkan_pesanan()


# Daftar menu dan harga
menu_list = [
    Menu("Popcorn", 25000),
    Menu("Minuman", 15000),
    Menu("Hot Dog", 20000),
    Menu("Nachos", 18000),
    Menu("Es Krim", 12000),
]

if __name__ == "__main__":
    pesan_makanan()