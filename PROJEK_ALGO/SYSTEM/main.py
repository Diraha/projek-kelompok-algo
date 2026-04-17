from riwayat import Stack
from rich.table import Table
from rich import print as p
import os

class Node: #Class untuk membuat template node
    def __init__(self, data):
        self.data = data #Membuat variabel data
        self.next = None #Membuat variabel next untuk pointer ke node selanjutnya
        self.prev = None #Membuat variabel prev untuk pointer ke node sebelumnya

class DoubleLinkedList: #Class untuk menjalankan fitur CRUD(Create, Read, Update, Delete)
    def __init__(self):
        self.head = None
        self.tail = None

    def add_photo(self, data): #CREATE
        new_node = Node(data) #Inisialisasi node baru

        if not self.head: #Jika head node dan tail node belum ada, maka jadikan node yang baru dibuat sebagai mereka
            self.head = new_node
            self.tail = new_node
        else: #Jika head node dan tail node sudah ada, maka sambungkan pointer tail node ke node baru, lalu pindahkan tail node ke node selanjutnya
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.save_file() #Jalankan method simpan data ke dalam file

    def save_file(self): #SAVE FILE
        temp = self.head #Simpan head node ke dalam variabel baru

        while temp: #Looping data yang dimulai dari node
            with open("PROJEK_ALGO/DATABASE/data_image.txt", mode="a", encoding="utf-8") as file:
                file.write(f"{temp.data}\n") #Masukkan data yang ada pada node ke dalam file
                temp = temp.next #Perbarui variabel temp menjadi node berikutnya

        return print("Selesai!") #Jika sudah mencapai node terakhir, cetak kata selesai ke terminal

    def update(self, data_image):
        self.found = False
        with open("PROJEK_ALGO/DATABASE/data_image.txt", mode="r+", encoding="utf-8") as file:
            lines = file.readlines()

            file.seek(0) #Set posisi kursor kembali ke atas
            file.truncate() #Kosongkan file

            for line in lines:
                data = line.strip().split(",")
                if data[0] == data_image:
                    input_user = input("Masukkan Edit: ")
                    file.write(f"{input_user}\n")
                    self.found = True
                else:
                    file.write(f"{line}\n")

        if not self.found:
            print("File tidak ditemukan di dalam penyimpanan!")


    def delete_photo(self, data_image): #DELETE
        self.found = False
        
        with open("PROJEK_ALGO/DATABASE/data_image.txt", mode="r+", encoding="utf-8") as file:
            lines = file.readlines() #Ambil/baca semua isi file, lalu simpan ke dalam variabel

            file.seek(0) #Set posisi kursor kembali ke atas
            file.truncate() #Kosongkan file

            s = Stack() #Inisialisasi objek stack untuk menyimpan file yang terhapus

            for line in lines: #Looping satu satu isi variabel lines
                data = line.strip().split(",") #Setiap nilai, bersihkan dulu dari elemen lain

                if data[0] == data_image: #Jika data yang ingin dihapus ada di dalam file, maka:
                    s.add_trash(data_image) #Simpan ke dalam file data_sampah.txt
                    self.found = True
                else:
                    file.write(line) #Jika bukan, maka tulis kembali sisanya ke dalam file data_image.txt

        if not self.found:
            print("File tidak ditemukan pada penyimpanan!")
            return

    def display(self): #READ
        self.table = Table() #Inisialisasi objek Table
        self.table.add_column("Nama File") #Buat 1 kolom baru

        with open("PROJEK_ALGO/DATABASE/data_image.txt", mode="r", encoding="utf-8") as file:
            lines = file.readlines() #Ambil/baca semua isi file, lalu simpan ke dalam variabel

            for line in lines: #Looping setiap nilai yang ada di dalam variabel lines
                data = line.strip() #Setiap nilai, bersihkan dulu dari elemen lain
                self.table.add_row(data) #Tambahkan nilai sebagai baris baru di dalam tabel

        return p(self.table) #Cetak hasil tabel
    
    def disply_dbl_next(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        return print("NULL")

    def disply_dbl_prev(self):
        temp = self.tail

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev

        return print("NULL")

if __name__ == "__main__":
    os.system("cls")

    print("=====================================")
    print("= 1. Tambah Data                    =")
    print("= 2. Tampilkan Data                 =")
    print("= 3. Edit Data                      =")
    print("= 4. Hapus Data                     =")
    print("= 5. Tampilkan Struktur DBL         =")
    print("= 6. Tampilkan Riwayat              =")
    print("=====================================")

    dll = DoubleLinkedList() #Inisialisasi objek DoubleLinkedList
    
    choice = input("Pilih Menu (1-6): ").strip().lower()
    if choice == "1":
        input_user = input("Masukkan Nama File Gambar: ") #Input user untuk menambah data (ceritanya: gambar)
        dll.add_photo(input_user) #Memanggil method add_photo untuk memasukkan/menambah data
    elif choice == "2":
        dll.display() #Menampilkan daftar gambar dalam bentuk tabel
    elif choice == "3":
        input_user3 = input("Masukkan Nama File Yang Ingin Diedit: ")
        dll.update(input_user3)
    elif choice == "4":
        input_user2 = input("Masukkan Nama File Yang Ingin Dihapus: ") #Input user untuk menghapus data (ceritanya: gambar)
        dll.delete_photo(input_user2) #Memanggil method delete_photo untuk menghapus data
    elif choice == "5":
        dll.disply_dbl_next()
        dll.disply_dbl_prev()
    elif choice == "6":
        s = Stack()
        s.display_trash()
    else:
        print("Input Tidak Valid!")