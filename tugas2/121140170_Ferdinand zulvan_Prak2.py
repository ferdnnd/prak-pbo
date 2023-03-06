class Ferdinand:
    def __init__(self, nama, nim, kls, sks):
        self.nama = nama
        self.nim = nim
        self.kls = kls
        self.sks = sks
    
    def info(self):
        print("Mahasiswa dengan nama ", self.nama, "dengan nim", self.nim, "mengikuti kelas PBO ", self.kls, "dengan", self.sks, "sks")
        
# Membuat object dari class Mobil
p1 = Ferdinand("joni", "12112312", "RB", "3")
p2 = Ferdinand("joko", "12112170", "RA", "2")

# Memanggil method info untuk menampilkan informasi mobil
p1.info()
p2.info()
