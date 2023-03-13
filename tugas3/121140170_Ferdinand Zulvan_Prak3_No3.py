class Mahasiswa:
    
    # variabel kelas (public)
    jumlah_mahasiswa = 0
    
    def __init__(self, nama, nim, ipk):
        # variabel instance (protected)
        self._nama = nama
        self._nim = nim
        self._ipk = ipk
        # variabel instance (private)
        self.__sks = 0
        
        # tambahkan 1 setiap kali instance dibuat
        Mahasiswa.jumlah_mahasiswa += 1
        
    # metode instance (public)
    def display_data(self):
        print("Nama:", self._nama)
        print("NIM:", self._nim)
        print("IPK:", self._ipk)
        
    # metode instance (protected)
    def _hitung_sks(self, matkul):
        sks = matkul['sks']
        self.__sks += sks
        
    # metode instance (private)
    def __check_sks(self, max_sks):
        if self.__sks > max_sks:
            print("Jumlah SKS melebihi batas!")
        else:
            print("Jumlah SKS masih dalam batas.")
            
    # metode instance (public) yang menggunakan metode protected dan private
    def ambil_matkul(self, matkul, max_sks):
        self._hitung_sks(matkul)
        self.__check_sks(max_sks)