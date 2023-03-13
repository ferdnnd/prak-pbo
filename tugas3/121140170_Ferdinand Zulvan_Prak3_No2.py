class AkunBank:
    list_pelanggan = []

    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.__no_pelanggan = no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo
        self.list_pelanggan.append(self)

    def lihat_menu(self):
        print("Selamat datang di Bank Jago")
        print("Halo " + self.__nama_pelanggan + ", ingin melakukan apa?")
        print("1. Lihat saldo")
        print("2. Tarik tunai")
        print("3. Transfer saldo")
        print("4. Keluar")

    def lihat_saldo(self):
        print(self.__nama_pelanggan + " memiliki saldo Rp " + str(self.__jumlah_saldo))

    def tarik_tunai(self):
        print("Masukkan jumlah nominal yang ingin ditarik: ")
        tarikan = int(input())
        if tarikan > self.__jumlah_saldo:
            print("Nominal saldo yang Anda punya tidak cukup!")
        else:
            self.__jumlah_saldo -= tarikan
            print("Saldo berhasil ditarik!")

    def transfer(self):
        print("Masukkan nominal yang ingin ditransfer: ")
        nominal = int(input())
        print("Masukkan no rekening tujuan: ")
        no_rek_tujuan = int(input())
        found = False
        for p in self.list_pelanggan:
            if p.__no_pelanggan == no_rek_tujuan:
                p.__jumlah_saldo += nominal
                self.__jumlah_saldo -= nominal
                print("Transfer Rp " + str(nominal) + " ke " + p.__nama_pelanggan + " sukses!")
                found = True
                break
        if not found:
            print("No rekening tujuan tidak dikenal! Kembali ke menu utama.")

# Instansiasi 3 AkunBank
Akun1 = AkunBank(1234, "Ferdinand Zulvan Lindan", 5000000)
Akun2 = AkunBank(2345, "Ukraina", 6666666666)
Akun3 = AkunBank(3456, "Elon Musk", 9999999999)

# Simulasi penggunaan Akun1
Akun1.lihat_menu()
pilihan = int(input("Masukkan nomor input: "))
while pilihan != 4:
    if pilihan == 1:
        Akun1.lihat_saldo()
    elif pilihan == 2:
        Akun1.tarik_tunai()
    elif pilihan == 3:
        Akun1.transfer()
    else:
        print("Input tidak valid")
    Akun1.lihat_menu()
    pilihan = int(input("Masukkan nomor input: "))
print("Terima kasih telah menggunakan layanan kami.")