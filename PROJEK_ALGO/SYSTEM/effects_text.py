import time
from termcolor import colored

#Menampilkan animasi proses download gambar
def download_image_effect():
    """
    Fungsi menampilkan animasi download gambar
    """
    while True:

        #animasi proses mengunduh gambar
        for i in range(6):
            titik = "." * i #membuat efek titik bertambah
            print(colored(f"\rMengunduh Foto, Tunggu Sebentar{titik}", "yellow"), end="")
            time.sleep(0.7)

        time.sleep(1.0)
        print("")

        #animasi proses menyimpan gambar ke galeri
        for i in range(6):
            titik = "." * i
            print(colored(f"\rMenyimpan Ke Dalam Galeri{titik}", "yellow"), end="")
            time.sleep(0.7)


        time.sleep(1.0)

        #menampilkan pesan berhasil didownload
        print(colored("\nFoto Berhasil Di Unduh!", "green"))
        time.sleep(1.5)
        return
    

#menampilkan animasi proses edit gambar    
def edit_image_effect(response):
    """
    Fungsi menampilkan animasi edit gambar
    """
    while True:

        #jika data tidak ditemukan
        if not response:
            time.sleep(1.0)
            print(colored("Data Tidak Ditemukan!", "red"))
            time.sleep(1.5)
            return

        #animasi proses memperbarui data
        for i in range(6):
            titik = "." * i
            print(colored(f"\rMemperbarui Data, Tunggu Sebentar{titik}", "yellow"), end="")
            time.sleep(0.7)

        time.sleep(1.0)

        #menampilkan pesan berhasil update
        print(colored("\nData Berhasil Diperbarui!", "green"))
        time.sleep(1.5)
        return

#Menampilkan animasi proses menghapus gambar    
def delete_image_effect(response):
    """
    Fungsi menampilkan animasi menghapus gambar
    """
    while True:

        #jika file tidak ditemukann
        if not response["found"]:
            time.sleep(1.0)
            print(colored(f"File {response["file_name"]} Tidak Ditemukan!", "red"))
            time.sleep(1.5)
            return

        #animasi proses menghapus gambar
        for i in range(6):
            titik = "." * i
            print(colored(f"\rMenghapus Foto, Tunggu Sebentar{titik}", "yellow"), end="")
            time.sleep(0.7)

        time.sleep(1.0)

        #menampilkan pesan berhasil menghapus gambar
        print(colored("\nFoto Berhasil Dihapus!", "green"))
        time.sleep(1.5)
        return
    

#Menampilkan animasi proses sorting data gambar    
def sorting_image_effect(by):
    """
    Fungsi menampilkan animasi sorting gambar
    """
    while True:

        #animasi proses pengurutan data
        for i in range(6):
            titik = "." * i
            print(colored(f"\rMengurutkan foto berdasarkan {by}{titik}", "yellow"), end="")
            time.sleep(0.7)

        time.sleep(1.0)

        #menampilkan pesan berhasil sorting
        print(colored("\nData Berhasil Diurutkan!", "green"))
        time.sleep(1.5)
        return
    
#Menampilkan animasi proses pencarian gambar
def searching_image_effect(file_name, data:dict):
    """
    Fungsi menampilkan animasi pencarian gambar
    """
    while True:

        #animasi proses pencarian file
        for i in range(6):
            titik = "." * i
            print(colored(f"\rMencari file {file_name}{titik}", "yellow"), end="")
            time.sleep(0.7)

        time.sleep(1.0)

    #jika file tidak ditemukan
        if not data["found"]:
            print(colored(f"\nFile {file_name} Tidak Ditemukan!", "red"), end="")
            time.sleep(1.5)
            return
    #jika file ditemukan
        else:
            print(colored(f"\nFile {file_name} Ditemukan!", "green"), end="")
            print(colored(f"\nTanggal Ditambahkan: {data["date"]}"))
            time.sleep(3.0)
            return