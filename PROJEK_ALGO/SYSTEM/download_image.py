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
    Fungsi untuk Menampilkan Daftar Gambar yang Bisa di Download
    """

    os.system("cls" if os.name == "nt" else "clear") #Membersihkan riwayat terminal sebelum menampilkan data

    num = 1 #Nomor urut untuk setiap gambar pada tabel

    table = Table(title="WELCOME TO PIN-HT")
    table.add_column("No", justify="center") #Menambahkan kolom nomor
    table.add_column("File Name") #Menambahkan kolom nama file
    table.add_column("Size", justify="center") #Menambahkan kolom ukuran file

    #Membaca data gambar dari file JSON
    with open("PROJEK_ALGO/DATABASE/data_download_image.json", "r") as file:
        data = json.load(file)

    #Menambahkan setiap data gambar ke dalam tabel
    for partOfData in data:
        table.add_row(str(num), f"{partOfData["file_name"]:<140}", partOfData["file_size"])
        num += 1 #Menambahkan nomor urut

    p(table) #Menampilkan tabel ke terminal

    #Menampilkan menu pilihan download
    print("\n[D]: Download Image                                                       [G]: Enter Gallery                                                        [X]: Exit\n")
    
    input_user = input("Masukkan Pilihan Anda: ").strip().upper()

    return input_user


def found_img():
    """
    Fungsi untuk mendownload gambar
    """
    dll = DoubleLinkedList()

    try:
        file_number = int(input("Masukkan Nomor File Gambar: "))
    except ValueError:
        print("Input Tidak Valid, Masukkan Nomor File Gambar!")

    #Mengubah nomor menjadi indeks list
    index = file_number - 1 #Agar sesuai dengan indeks yang ada pada data

    with open("PROJEK_ALGO/DATABASE/data_download_image.json", "r") as file:
        data = json.load(file)

    #Jika user input tidak sesuai dengan yang ada di dalam data
    if index < 0 or index >= len(data):
        print(colored("Nomor Gambar Tidak Valid di PIN-HT!", "red"))
        time.sleep(1.0) #Waktu untuk membaca pesan error
        return
    
    selected_data = data[index] #Mengambil data sesuai indeks
    file_name = selected_data["file_name"] #Mengambil nama file dari data yang dipilih
    file_size = selected_data["file_size"]
    dll.add_photo(file_name, file_size) #Menambahkan gambar ke galeri user
    download_image_effect()


def menu_download():
    """
    Fungsi untuk menampilkan menu di halaman download
    """
    while True:
        #Menampilkan daftar gambar dan mengambil pilihan user
        response = download_img()

        #Jika User Download Gambar
        if response == "D":
            found_img()
        #Jika User Kembali ke Galeri
        elif response == "G":
            from main import gallery
            gallery()
            break
        #Keluar dari Program
        elif response == "X":
            os.system("cls" if os.name == "nt" else "clear")
            print("Program Selesai, Terima Kasih!")
            exit()
        #Jika input tidak valid
        else:
            print(colored("Input Tidak Valid!", "red"))
            time.sleep(1.5)