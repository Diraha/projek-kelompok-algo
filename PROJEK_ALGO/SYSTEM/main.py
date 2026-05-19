import os
from node import DoubleLinkedList
from history import Stack
from pyfiglet import Figlet
from termcolor import colored
from effects_text import edit_image_effect, delete_image_effect, sorting_image_effect, searching_image_effect
import time
from download_image import menu_download

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
    user_choice = input(" " * padding + prompt).upper().strip() 

    return user_choice

def gallery():
    dll = DoubleLinkedList() #Inisialisasi objek DoubleLinkedList

    while True: #Looping utama agar program terus berjalan sampai user pilih keluar
        os.system("cls" if os.name == "nt" else "clear")
        dll.display()
        choice = input("Masukkan Pilihan Menu: ").strip().upper() #Meminta user memilih menu
                
        if choice == "E":
            os.system("cls" if os.name == "nt" else "clear")
            old_data = input("Masukkan Nama File yang Ingin Diedit: ").strip()
            new_data = input("Masukkan Nama File Baru: ").strip()
            response = dll.update_photo(old_data, new_data)
            edit_image_effect(response)
            os.system("cls" if os.name == "nt" else "clear")
            dll.display()

        elif choice == "A":
            menu_download()
                
        elif choice == "D":
            os.system("cls" if os.name == "nt" else "clear")
            input_user = input("Masukkan Nama File Yang Ingin Dihapus: ").strip() #Input user untuk menghapus data (ceritanya: gambar)
            dll.delete_photo(input_user) #Memanggil method delete_photo untuk menghapus data
            delete_image_effect()
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
            return

        elif choice == "R":
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                print("\nFoto dapat diurutkan berdasarkan:")
                print("1. Nama File (A-Z)")
                print("2. Tanggal")

                sort_choice = input("Masukkan Nomor Pengurutan yang Ingin Dilakukan(1/2): ").strip()

                if sort_choice == "1":
                    by = "nama_file"
                    dll.insertion_sort(by)
                    sorting_image_effect(by)
                    break

                elif sort_choice =="2":
                    by = "tanggal"
                    dll.insertion_sort(by)
                    sorting_image_effect(by)
                    break

                else:
                    print(colored("Pilihan tidak valid!", "red"))
                    time.sleep(1.5)

            os.system("cls" if os.name == "nt" else "clear")
            dll.display()
                
        elif choice == "C":
            os.system("cls" if os.name == "nt" else "clear")
            target = input("Masukkan nama foto yang dicari: ").strip()
            response = dll.binary_search(target)
            searching_image_effect(target, response)
            os.system("cls" if os.name == "nt" else "clear")
            dll.display()
                
        elif choice == "X":
            os.system("cls" if os.name == "nt" else "clear")
            print("Program selesai. Terimakasih!")
            exit()
                
        else:
            print(colored("Input Tidak Valid!", "red"))
            time.sleep(1.0)

if __name__ == '__main__':
    while True:
        os.system("cls" if os.name == "nt" else "clear")  #Membersihkan layar terminal saat program dimulai

        result = start()

        if result == "E":
            gallery()
            break
        elif result == "D":
            menu_download()
            break
        else:
            text = "Masukkan Inputan Yang Valid!"
            padding = (os.get_terminal_size().columns - len(text)) // 2
            print(colored("\n" + " " * padding + text, "red"))
            time.sleep(1.5)
