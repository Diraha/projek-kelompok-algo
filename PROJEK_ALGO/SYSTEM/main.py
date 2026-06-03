import os
from node import DoubleLinkedList
from history import display
from pyfiglet import Figlet
from termcolor import colored
from effects_text import edit_image_effect, delete_image_effect, sorting_image_effect, searching_image_effect, detail_image_effect
import time

def homescreen():
    """
    Function untuk menampilkan homescreen sistem
    """
    #mengambil lebar terminal agar tampilan rata tengah
    width = os.get_terminal_size().columns

    f = Figlet(font="small", width=width) #membuat objek figlet dengan font small
    print(colored(f.renderText(" " * 45 + "SELAMAT DATANG"), "white")) #menampilkan judul utama dengan warna putih
    print(colored(f.renderText(" " * 49 + "DI GALLERY-HT"), "magenta")) #menampilkan subjudul dengan warna magenta

    #menampilkan pilihan menu awal
    print(colored(" " * 54 + "Input [E] To Gallery | Input [D] To Image Download\n", "yellow"))

    prompt = "Silahkan Masukkan Pilihan Anda: "
    padding = (width - len(prompt)) // 2 #menegatur posisi prompt agar berada di tengah terminal
    user_choice = input(" " * padding + prompt).upper().strip() #menerima input user lalu mengubahnya menjadi huruf kapital dan menghapus spasi berlebih

    return user_choice #mengembalikan pilihan user


def gallery():
    """
    Function untuk menampilkan sistem menu
    """
    os.system("cls" if os.name == "nt" else "clear") #membersihkan terminal
    dll = DoubleLinkedList() #  Inisialisasi objek DoubleLinkedList

    while True: #Looping utama agar program terus berjalan sampai user pilih keluar
        dll.display()
        choice = input("Masukkan Pilihan Menu: ").strip().upper() #Meminta user memilih menu

        #menu edit foto        
        if choice == "E":
            os.system("cls" if os.name == "nt" else "clear") #membersihkan layar
            dll.display_table()
            old_data = input("Masukkan Nama File yang Ingin Diedit: ").strip() #meminta nama file lama
            new_data = input("Masukkan Nama File Baru: ").strip() #meminta nama file baru
            response = dll.update_photo(old_data, new_data) #memanggil method update photo
            edit_image_effect(response) #menampilkan efek edit

        #menu tambah/download foto
        elif choice == "A":
            #import function menu_download dari file g
            # download_image.py
            from download_image import menu_download
            menu_download() #menjalankan menu download
            return #keluar dari gallery
        
        #menu hapus foto
        elif choice == "D":
            os.system("cls" if os.name == "nt" else "clear") #membersihkan layar
            dll.display_table()
            input_user = input("Masukkan Nama File Yang Ingin Dihapus: ").strip() #Input user untuk menghapus data (ceritanya: gambar)
            response = dll.delete_photo(input_user) #Memanggil method delete_photo untuk menghapus data
            delete_image_effect(response) #menampilkan efek penghapusan
                
        #menu tampilkan data next & prev
        elif choice == "S":
            os.system("cls" if os.name == "nt" else "clear")
            dll.display_dbl_vertical()
        
        #menu history
        elif choice == "T":
            os.system("cls" if os.name == "nt" else "clear") #membersihkan layar
            display() #menampilkan history
            return #keluar dari gallery

        #menu sorting
        elif choice == "R":
            #loop untuk memilih metode sorting
            while True:
                os.system("cls" if os.name == "nt" else "clear") #membersihkan layar
                print("\nFoto dapat diurutkan berdasarkan:") #menampilkan pilihan sorting
                print("1. Nama File (A-Z)")
                print("2. Tanggal")

                #input pilihan sorting
                sort_choice = input("Masukkan Nomor Pengurutan yang Ingin Dilakukan(1/2): ").strip()

                #sorting berdasarkan nama file
                if sort_choice == "1":
                    by = "nama_file"
                    dll.insertion_sort(by)
                    sorting_image_effect(by) #menampilkan efek sorting
                    break
                #sorting berdasarkan tanggal
                elif sort_choice =="2":
                    by = "tanggal"
                    dll.insertion_sort(by)
                    sorting_image_effect(by) #menampilkan efek sorting
                    break
                #jika input tidak valid
                else:
                    print(colored("Pilihan tidak valid!", "red"))
                    time.sleep(1.5)
                
        #menu searching
        elif choice == "C":
            os.system("cls" if os.name == "nt" else "clear") #membersihkan layar
            dll.display_table()
            target = input("Masukkan nama foto yang dicari: ").strip() #input nama foto yang ingin dicari
            response = dll.binary_search(target) #melakukan binary search
            searching_image_effect(target, response) #menampilkan efek pencarian
            input("Tekan Enter untuk Kembali...")

        #menu informasi
        elif choice == "I":
            os.system("cls" if os.name == "nt" else "clear") #membersihkan layar
            dll.gallery_information()

        #menu detail foto
        elif choice == "V":
            dll.display_table()
            dll.detail_image()

        #menu exit
        elif choice == "X":
            os.system("cls" if os.name == "nt" else "clear") #membersihkan layar
            print("Program selesai. Terimakasih!") #menampilkan pesan keluar
            exit() #menghentikan program
                
        #jika input tidak valid
        else:
            print(colored("Input Tidak Valid!", "red")) #menampilkan pesan error
            time.sleep(1.5)


#program utama dijalankan jika file ini dieksekusi langsung
if __name__ == '__main__':
    #loop utama homescreen
    while True:
        os.system("cls" if os.name == "nt" else "clear")  #Membersihkan layar terminal saat program dimulai

        response = homescreen() #memanggil function homescreen

        #jika user memilih gallery
        if response == "E":
            gallery()
            break
        #jika user memilih download image
        elif response == "D":
            #import menu download dan jalankan menu download
            from download_image import menu_download
            menu_download()
            break
        #jika input tidak valid
        else:
            text = "Masukkan Inputan Yang Valid!" #tampilkan pesan eror
            padding = (os.get_terminal_size().columns - len(text)) // 2
            print(colored("\n" + " " * padding + text, "red"))
            time.sleep(1.5)
