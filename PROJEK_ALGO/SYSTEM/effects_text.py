import time
from termcolor import colored

def download_photo_effect():
    while True:
        for i in range(6):
            titik = "." * i
            print(colored(f"\rMengunduh Foto, Tunggu Sebentar{titik}", "yellow"), end="")
            time.sleep(1.5)

        time.sleep(1.5)
        print(colored("\nSelesai!", "yellow"))
        time.sleep(1.5)
        return
    
def edit_photo_effect():
    while True:
        for i in range(6):
            titik = "." * i
            print(colored(f"\rMemperbarui Data, Tunggu Sebentar{titik}", "yellow"), end="")
            time.sleep(1.5)

        time.sleep(1.5)
        print(colored("\nSelesai!", "yellow"))
        time.sleep(1.5)
        return
    
def delete_photo_effect():
    while True:
        for i in range(6):
            titik = "." * i
            print(colored(f"\rMenghapus Foto, Tunggu Sebentar{titik}", "yellow"), end="")
            time.sleep(1.5)

        time.sleep(1.5)
        print(colored("\nSelesai!", "yellow"))
        time.sleep(1.5)
        return
    
def sorting_photo_effect(by):
    while True:
        for i in range(6):
            titik = "." * i
            print(colored(f"\rMengurutkan foto berdasarkan {by}{titik}", "yellow"), end="")
            time.sleep(1.5)

        time.sleep(1.5)
        print(colored("\nSelesai!", "yellow"))
        time.sleep(1.5)
        return
    
def searching_photo_effect(file_name):
    while True:
        for i in range(6):
            titik = "." * i
            print(colored(f"\rMencari file {file_name}{titik}", "yellow"), end="")
            time.sleep(1.5)

        time.sleep(1.5)
        print(colored("\nSelesai!", "yellow"))
        time.sleep(1.5)
        return