from pathlib import Path #Membuat path folder/file yang lebih aman
from rich.table import Table #Menampilkan data dalam bentuk tabel di terminal
from rich import print as p #Membuat tampilan terminal lebih rapi dan bewarna
from riwayat import Stack #Mengambil class Stack dari file riwayat.py, menyimpan riwayat foto yang sudah dihapus
import os #Membersihkan layar terminal

#BASE_DIR digunakan untuk mendapatkan lokasi folder utama project
#__file__ berarti lokasi file main.py
#parent.parent berarti naik dua folder dari SYSTEM/main.py ke PROJEK_ALGO/
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_DIR = BASE_DIR / "DATABASE" #Menentukan lokasi folder DATABASE
DATA_IMAGE_PATH = DATABASE_DIR / "data_image.txt" #Menentukan lokasi file data_image.txt untuk menyimpan data foto

class Node: #Class untuk membuat template node
    def __init__(self, data):
        self.data = data #Membuat variabel data
        self.next = None #Membuat variabel next untuk pointer ke node selanjutnya
        self.prev = None #Membuat variabel prev untuk pointer ke node sebelumnya

class DoubleLinkedList: #Class untuk menjalankan fitur CRUD(Create, Read, Update, Delete)
    def __init__(self):
        self.head = None
        self.tail = None
        DATABASE_DIR.mkdir(exist_ok=True) #Membuat folder DATABASE jika belum ada
        DATA_IMAGE_PATH.touch(exist_ok=True) #Membuat file data_image.txt jika belum ada
        self.load_from_file() #Saat program pertama kali dijalankan, data dari file txt dimasukkan kembali ke linked list

    def is_empty(self):
        """
        Method untuk mengecek apakah Linked list kosong
        """
        return self.head is None
    
    def add_node(self, data):
        """
        Method ini hanya menambahkan node ke Linked List tanpa langsung menyimpan data ke file
        """
        new_node = Node(data) #Membuat node baru yang berisi nama file foto

        #Jika Linked list kosong, maka node baru jadi head sekaligus tail
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        
        #Jika Linked list sudah memiliki data, node baru ditambahkan dibagian akhir
        else:
            self.tail.next = new_node #Node terakhir saat ini menunjuk ke node baru
            new_node.prev = self.tail #Node baru menunjuk balik ke tail lama
            self.tail = new_node #Tail dipindahkan ke node baru

    def load_from_file(self):
        """
        Method untuk mengambil data dari file data_image.txt lalu memasukkannya ke dalam Double Linked list
        """
        self.head = None #Mengosongkan linked list dulu
        self.tail = None

        with open(DATA_IMAGE_PATH, mode="r", encoding="utf-8") as file: #Membuka file data_image.txt dalam mode baca
            for line in file: #Membaca isi file baris perbaris
                data = line.strip() #Menghapus spasi atau enter diawal/akhir teks
                if data: #Jika data tidak kosong, masukkan ke linked list
                    self.add_node(data)

    def save_to_file(self):
        """
        Method untuk menyimpan ulang seluruh isi Linked list ke file txt
        """
        with open(DATA_IMAGE_PATH, mode="w", encoding="utf-8") as file: #Membuka file mode write
            temp = self.head #Membaca data dari head
            while temp: #Tulis datanya ke file selama node masih ada
                file.write(temp.data + "\n")
                temp = temp.next #Pindah ke node berikutnya

    def add_photo(self, data):
        """
        Method untuk menambahkan foto baru
        """
        if not data:
            print("Nama file tidak boleh kosong!") #Mengecek agar input tidak kosong
            return
        
        self.add_node(data) #Menambahkan data ke Linked list
        self.save_to_file() #Menyimpan Linked list terbaru ke file txt
        print(f"Foto '{data}' berhasil ditambahkan!")

    def update_photo(self, old_data, new_data):
        """
        Method untuk mengubah nama file foto
        """
        temp = self.head #Mencari data dari head

        while temp:
            #Jika data pada node sama dengan nama file yang dicari
            if temp.data == old_data:
                temp.data = new_data #Ganti data lama dengan data baru
                self.save_to_file()
                print(f"Foto '{old_data}' berhasil diubah menjadi '{new_data}'!")
                return

            temp = temp.next #Jika belum ditemukan, pindah ke node berikutnya

    def delete_photo(self, data_image):
        """
        Method untuk menghapus foto dari Linked list
        """
        temp = self.head #Mulai mencari data dari head
        stack = Stack() #Membuat objek stack untuk menyimpan riwayat foto yang dihapus
        
        while temp: #Looping selama node masih ada
            if temp.data == data_image: #Jika data yang dicari ditemukan
                stack.add_trash(temp.data)
                if temp.prev: #Jika node yang dihapus punya node sebelumnya, maka sambungkan ke node setelahnya
                    temp.prev.next = temp.next
                else: #Jika node yang dihapus adalah head, pindahkan head ke node berikutnya
                    self.head = temp.next

                if temp.next: #Jika node yang dihapus punya node setelahnya, sambungkan ke node sebelumnya
                    temp.next.prev = temp.prev
                else: #Jika node yang dihapus adalah tail, maka pindahkan tail ke node sebelumnya
                    self.tail = temp.prev
                
                self.save_to_file() #Simpan perubahan Linked list ke file txt
                print(f"Foto berhasil dihapus")
            else:
                print("File tidak ditemukan pada penyimpanan!") #Jika data tidak ditemykan
                return
            #jika belum ditemukan, lanjut ke node berikutnya
            temp = temp.next

    def display(self):
        """
        Method untuk menampilkan seluruh data foto dalam bentuk tabel
        """
        table = Table(title="Data Galeri Foto") #Membuat tabel dengan judul
        table.add_column("No", justify="center") #Menambahkan kolom nomor
        table.add_column("Nama File") #Menambahkan kolom nama file

        temp = self.head #Mulai baca data dari head
        
        nomor = 1 #Nomor awal tabel

        if self.is_empty(): #Jika Linked list kosong, tampilkan keterangan
            table.add_row("-", "Belum ada data foto")
        else: #Jika ada data, tampilkan ke tabel
            while temp:
                table.add_row(str(nomor), temp.data)
                temp = temp.next #Pindah ke node berikutnya
                nomor += 1 #Nomor bertambah
        p(table) #Menampilkan tabel ke terminal
    
    def disply_dll_next(self):
        """
        Method untuk menampilkan struktur Double Linked List dari depan ke belakang
        """
        temp = self.head #Mulai dari head

        if self.is_empty(): #Jika Linked list kosong
            print("Double Linked List masih kosong!")
            return
        
        #Menampilkan arah dari Head ke Tail
        print("HEAD", end=" <-> ")

        while temp: #Looping dari head ke tail
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("NULL")

    def disply_dll_prev(self):
        """
        Method untuk menampilkan struktur Double Linked List dari belakang ke depan
        """
        temp = self.tail #Mulai dari tail

        if self.is_empty(): #Jika Linked list kosong
            print("Double Linked List masih kosong!")
            return

        #Menampilkan arah dari Tail ke Head
        print("TAIL", end=" <-> ")

        while temp: #Looping dari tail ke head
            print(temp.data, end=" <-> ")
            temp = temp.prev

        print("NULL")

def clear_screen():
    """
    Function untuk membersihkan layar terminal
    """
    #Jika sistem operasi Windows, gunakan cls
    #Jika bukan windows, gunakan clear
    os.system("cls" if os.name == "nt" else "clear") 

def show_menu():
    """
    Function untuk menampilkan menu utama aplikasi
    """
    print("=====================================")
    print("=         APLIKASI GALERI           =")
    print("= 1. Tambah Data Foto               =")
    print("= 2. Tampilkan Data Foto            =")
    print("= 3. Edit Data Foto                 =")
    print("= 4. Hapus Data Foto                =")
    print("= 5. Tampilkan Struktur DLL         =")
    print("= 6. Tampilkan Riwayat Hapus        =")
    print("= 7. Keluar                         =")
    print("=====================================")

#Bagian ini hanya dijalankan jika file main.py dijalankan langsung
if __name__ == "__main__":
    dll = DoubleLinkedList() #Inisialisasi objek DoubleLinkedList
    clear_screen() #Membersihkan layar terminal saat program dimulai

    while True: #Looping utama agar program terus berjalan sampai user pilih keluar
        show_menu() #Menampilkan menu

        choice = input("Pilih Menu (1-7): ").strip() #Meminta user memilih menu

        if choice == "1":
            input_user = input("Masukkan Nama File Gambar: ").strip() #Input user untuk menambah data (ceritanya: gambar)
            dll.add_photo(input_user) #Memanggil method add_photo untuk memasukkan/menambah data
        
        elif choice == "2":
            dll.display() #Menampilkan daftar gambar dalam bentuk tabel
        
        elif choice == "3":
            old_data = input("Masukkan Nama File yang Ingin Diedit: ").strip()
            new_data = input("Masukkan Nama File Baru: ").strip()
            dll.update_photo(old_data, new_data)
        
        elif choice == "4":
            input_user = input("Masukkan Nama File Yang Ingin Dihapus: ").strip() #Input user untuk menghapus data (ceritanya: gambar)
            dll.delete_photo(input_user) #Memanggil method delete_photo untuk menghapus data
        
        elif choice == "5":
            print("\nData dari HEAD ke TAIL:")
            dll.disply_dll_next()

            print("\nData dari TAIL ke HEAD:")
            dll.disply_dll_prev()
        
        elif choice == "6":
            stack = Stack()
            stack.display_trash()
        
        elif choice == "7":
            print("Program selesai. Terimakasih!")
            break
        
        else:
            print("Input Tidak Valid!")

        #Menanyakan apakah user ingin melanjutkan menggunakan aplikasi
        lanjut = input("\nLanjut menggunakan aplikasi? (y/n): ").strip().lower()

        if lanjut == "n":
            print("Program selesai. Terimakasih!")
            break

        clear_screen() #Membersihkan layar sebelum menampilkan menu lagi