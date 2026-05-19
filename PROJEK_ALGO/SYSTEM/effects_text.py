import time
from termcolor import colored

def download_image_effect():
    while True:
        for i in range(6):
            titik = "." * i
            print(colored(f"\rMengunduh Foto, Tunggu Sebentar{titik}", "yellow"), end="")
            time.sleep(0.7)

        time.sleep(1.0)
        print("")

        for i in range(6):
            titik = "." * i
            print(colored(f"\rMenyimpan Ke Dalam Galeri{titik}", "yellow"), end="")
            time.sleep(0.7)

        time.sleep(1.0)
        print(colored("\nFoto Berhasil Di Unduh!", "green"))
        time.sleep(1.5)
        return
    
def edit_image_effect(response):
    while True:
        if not response:
            time.sleep(1.0)
            print(colored("Data Tidak Ditemukan!", "red"))
            time.sleep(1.5)
            return

        for i in range(6):
            titik = "." * i
            print(colored(f"\rMemperbarui Data, Tunggu Sebentar{titik}", "yellow"), end="")
            time.sleep(0.7)

        time.sleep(1.0)
        print(colored("\nData Berhasil Diperbarui!", "green"))
        time.sleep(1.5)
        return
    
def delete_image_effect(response):
    while True:
        if not response["found"]:
            time.sleep(1.0)
            print(colored(f"File {response["file_name"]} Tidak Ditemukan!", "red"))
            time.sleep(1.5)
            return

        for i in range(6):
            titik = "." * i
            print(colored(f"\rMenghapus Foto, Tunggu Sebentar{titik}", "yellow"), end="")
            time.sleep(0.7)

        time.sleep(1.0)
        print(colored("\nFoto Berhasil Dihapus!", "green"))
        time.sleep(1.5)
        return
    
def sorting_image_effect(by):
    while True:
        for i in range(6):
            titik = "." * i
            print(colored(f"\rMengurutkan foto berdasarkan {by}{titik}", "yellow"), end="")
            time.sleep(0.7)

        time.sleep(1.0)
        print(colored("\nData Berhasil Diurutkan!", "green"))
        time.sleep(1.5)
        return
    
def searching_image_effect(file_name, data:dict):
    while True:
        for i in range(6):
            titik = "." * i
            print(colored(f"\rMencari file {file_name}{titik}", "yellow"), end="")
            time.sleep(0.7)

        time.sleep(1.0)

        if not data["found"]:
            print(colored(f"\nFile {file_name} Tidak Ditemukan!", "red"), end="")
            time.sleep(1.5)
            return
        else:
            print(colored(f"\nFile {file_name} Ditemukan!", "green"), end="")
            print(colored(f"\nTanggal Ditambahkan: {data["date"]}"))
            time.sleep(3.0)
            return