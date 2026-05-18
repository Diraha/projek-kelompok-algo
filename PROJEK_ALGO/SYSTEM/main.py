import os
from node import DoubleLinkedList
from history import Stack
from pyfiglet import Figlet
from termcolor import colored
import json

def start():
    """
    Function untuk menampilkan homescreen aplikasi
    """
    width = os.get_terminal_size().columns

    f = Figlet(font="small", width=width)
    print(colored(f.renderText(" " * 45 + "SELAMAT DATANG"), "white"))
    print(colored(f.renderText(" " * 49 + "DI GALLERY-HT"), "magenta"))

    print(colored(" " * 54 + "Input [E] To Gallery | Input [D] To Image Download\n", "yellow"))

    prompt = "Silahkan Masukkan Pilihan Anda: "
    padding = (width - len(prompt)) // 2
    user_choice = input(" " * padding + prompt).lower().strip() 

    return user_choice

def show_gallery():
    with open("PROJEK_ALGO/DATABASE/data_image.json", "r") as file:
        data = json.load(file)

    num = 1

    for partOfData in data:
        print(f"{num} | {partOfData["nama_file"]:<40}{partOfData["tanggal"]:>10}")
        num += 1

#Bagian ini hanya dijalankan jika file main.py dijalankan langsung
if __name__ == "__main__":
    dll = DoubleLinkedList() #Inisialisasi objek DoubleLinkedList
    os.system("cls" if os.name == "nt" else "clear")  #Membersihkan layar terminal saat program dimulai

    start = start() #Menampilkan menu

    if start == "e":
        os.system("cls" if os.name == "nt" else "clear")
        dll.display()

        while True: #Looping utama agar program terus berjalan sampai user pilih keluar
            choice = input("Pilih Menu (1-9): ").strip().upper() #Meminta user memilih menu

            if choice == "A":
                os.system("cls" if os.name == "nt" else "clear")
                input_user = input("Masukkan Nama File Gambar: ").strip() #Input user untuk menambah data (ceritanya: gambar)
                dll.add_photo(input_user) #Memanggil method add_photo untuk memasukkan/menambah data
                os.system("cls" if os.name == "nt" else "clear")
                dll.display()
            
            elif choice == "E":
                os.system("cls" if os.name == "nt" else "clear")
                old_data = input("Masukkan Nama File yang Ingin Diedit: ").strip()
                new_data = input("Masukkan Nama File Baru: ").strip()
                dll.update_photo(old_data, new_data)
                os.system("cls" if os.name == "nt" else "clear")
                dll.display()
            
            elif choice == "D":
                os.system("cls" if os.name == "nt" else "clear")
                input_user = input("Masukkan Nama File Yang Ingin Dihapus: ").strip() #Input user untuk menghapus data (ceritanya: gambar)
                dll.delete_photo(input_user) #Memanggil method delete_photo untuk menghapus data
                os.system("cls" if os.name == "nt" else "clear")
                dll.display()
            
            elif choice == "S":
                print("\nData dari HEAD ke TAIL:")
                dll.disply_dll_next()

                print("\nData dari TAIL ke HEAD:")
                dll.disply_dll_prev()
            
            elif choice == "T":
                os.system("cls" if os.name == "nt" else "clear")
                stack = Stack()
                stack.display_trash()

            elif choice == "R":
                os.system("cls" if os.name == "nt" else "clear")
                print("\nFoto dapat diurutkan berdasarkan:")
                print("1. Nama Foto (A-Z)")
                print("2. Tanggal")

                sort_choice = input("Masukkan Nomor Pengurutan yang Ingin Dilakukan(1/2): ").strip()

                if sort_choice == "1":
                    by = "nama_file"
                    dll.insertion_sort(by)

                elif sort_choice =="2":
                    by = "tanggal"
                    dll.insertion_sort(by)

                else:
                    print("Pilihan tidak valid!")

                os.system("cls" if os.name == "nt" else "clear")
                dll.display()
            
            elif choice == "C":
                os.system("cls" if os.name == "nt" else "clear")
                target = input("Masukkan nama foto yang dicari: ").strip()
                dll.binary_search(target)
                os.system("cls" if os.name == "nt" else "clear")
                dll.display()
            
            elif choice == "X":
                os.system("cls" if os.name == "nt" else "clear")
                print("Program selesai. Terimakasih!")
                exit()
            
            else:
                print("Input Tidak Valid!")
                
    elif start == "p":
        print("Hallo!")

    else:
        print("Masukkan Inputan Yang Valid!")