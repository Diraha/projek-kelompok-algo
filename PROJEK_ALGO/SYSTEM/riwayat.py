from pathlib import Path #Mengatur path file dan folder
from rich.table import Table #Menampilkan riwayat dalam bentuk tabel
from rich import print as p #Agar tampilan terminal lebih rapi

#BASE_DIR digunakan untuk mendapatkan lokasi folder utama project
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_DIR = BASE_DIR / "DATABASE" #Menentukan lokasi folder DATABASE
DATA_TRASH_PATH = DATABASE_DIR / "data_sampah.txt" #Menentukan lokasi file data_image.txt untuk menyimpan data foto

class Stack: #Class untuk membuat template node linked list
    def __init__(self):
        DATABASE_DIR.mkdir(exist_ok=True) #Membuat folder DATABASE jika belum ada
        DATA_TRASH_PATH.touch(exist_ok=True) #Membuat file data_sampah.txt jika belum ada

    def add_trash(self, data):
        """
        Method untuk menambahkan data foto yang dihapus ke file riwayat
        """
        with open(DATA_TRASH_PATH, mode="a", encoding="utf-8") as file: #Membuka file dalam mode append
            file.write(data + "\n")

    def display_trash(self):
        """
        Method untuk menampilkan semua riwayat foto yang sudah dihapus
        """
        table = Table(title="Riwayat Foto Terhapus") #Membuat tabel untuk menampilkan data riwayat
        table.add_column("No", justify="center") #Menambahkan kolom nomor
        table.add_column("Nama File Terhapus") #Menambahkan kolom nama file yang terhapus

        with open(DATA_TRASH_PATH, mode="r", encoding="utf-8") as file: #Membuka file data_sampah.txt dalam mode baca
            lines = [line.strip() for line in file if line.strip()] #Membaca semua baris dan menghapus enter/spasi kosong

            if not lines: #Jika belum ada data yang dihapus
                table.add_row("-", "Belum ada riwayat hapus")
            else: #Jika ada riwayat, tampilkan data dari yang terbaru
                #reversed agar data terakhir ditampilkan paling atas sesuai konsep stak LIFO
                for index, data in enumerate(reversed(lines), start=1):
                    table.add_row(str(index), data)
            
            p(table) #Menampilkan tabel ke terminal