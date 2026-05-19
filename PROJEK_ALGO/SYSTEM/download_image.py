from rich.table import Table
from rich import print as p
import json
import os
from node import DoubleLinkedList
from termcolor import colored
import time
from effects_text import download_image_effect

def download_img():
    """
    Fungsi Untuk Menampilkan Daftar Gambar
    """

    os.system("cls" if os.name == "nt" else "clear")

    num = 1

    table = Table(title="WELCOME TO PIN-HT")
    table.add_column("No", justify="center") #Menambahkan kolom nomor
    table.add_column("File Name") #Menambahkan kolom nama file
    table.add_column("Size", justify="center")

    with open("PROJEK_ALGO/DATABASE/data_download_image.json", "r") as file:
        data = json.load(file)

    for partOfData in data:
        table.add_row(str(num), f"{partOfData["file_name"]:<140}", partOfData["file_size"])
        num += 1

    p(table)

    print("\n[D]: Download Image                                                       [G]: Enter Gallery                                                        [X]: Exit\n")
    
    input_user = input("Masukkan Pilihan Anda: ").strip().upper()

    return input_user

def found_img():
    dll = DoubleLinkedList()

    file_name = input("Masukkan Nama File Gambar: ").strip().lower()

    with open("PROJEK_ALGO/DATABASE/data_download_image.json", "r") as file:
        data = json.load(file)

    for i in data:
        if file_name == i["file_name"]:
            dll.add_photo(file_name)
            download_image_effect()
            return

    print(colored("Gambar Tidak Tersedia di PIN-HT", "red"))
    time.sleep(1.0)
    return

def menu_download():
    while True:
        response = download_img()

        if response == "D":
            found_img()
        elif response == "G":
            from main import gallery
            gallery()
            break
        elif response == "X":
            os.system("cls" if os.name == "nt" else "clear")
            print("Program Selesai, Terima Kasih!")
            exit()
        else:
            print(colored("Input Tidak Valid!", "red"))
            time.sleep(1.5)