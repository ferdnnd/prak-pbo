username_benar = "admin"
password_benar = "12345"

batas_percobaan = 3

percobaan = 0

while percobaan < batas_percobaan:
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    

    if username == username_benar and password == password_benar:
        print("Login berhasil!")
        break
    else:
        print("Username atau password salah. Silakan coba lagi.")
        percobaan += 1

if percobaan == batas_percobaan:
    print("Batas percobaan login telah tercapai. Akun diblokir.")