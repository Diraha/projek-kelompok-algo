from pathlib import Path #Membuat path folder/file yang lebih aman
from rich.table import Table #Menampilkan data dalam bentuk tabel di terminal
from rich import print as p #Membuat tampilan terminal lebih rapi dan bewarna
from riwayat import Stack #Mengambil class Stack dari file riwayat.py, menyimpan riwayat foto yang sudah dihapus
from datetime import datetime
import os #Membersihkan layar terminal
import json

#BASE_DIR digunakan untuk mendapatkan lokasi folder utama project
#__file__ berarti lokasi file main.py
#parent.parent berarti naik dua folder dari SYSTEM/main.py ke PROJEK_ALGO/
BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_DIR = BASE_DIR / "DATABASE" #Menentukan lokasi folder DATABASE
DATA_IMAGE_PATH = DATABASE_DIR / "data_image.json" #Menentukan lokasi file data_image.json untuk menyimpan data foto

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

    ###################
    #HELPER
    ###################

    def is_empty(self):
        """
        Method untuk mengecek apakah Linked list kosong
        """
        return self.head is None
    
    def _now(self) -> str:
        """
        Waktu sekarang dalam format string
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    ###################
    #FUNCTION
    ###################
    
    def add_node(self, data:dict):
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

        try:
            with open(DATA_IMAGE_PATH, mode="r", encoding="utf-8") as file:
                content = file.read().strip()
                if not content: #Kalau File nya masih kosong
                    return
                records = json.loads(content)
                for record in records:
                    if "nama_file" in record:
                        if "tanggal" not in record:
                            record["tanggal"] = "Tidak diketahui"
                        self.add_node(record)
        except(json.JSONDecodeError, KeyError): #Kalau file rusak, mulai dari LL kosong
            print("Database rusak atau format tidak valid!")

    def save_to_file(self):
        """
        Method untuk menyimpan ulang seluruh isi Linked list ke file txt
        """
        records = []
        temp = self.head 

        while temp:
            records.append(temp.data)
            temp = temp.next
        with open(DATA_IMAGE_PATH, mode="w", encoding="utf-8") as file:
            json.dump(records, file, indent=4, ensure_ascii=False)

    def add_photo(self, nama_file:str):
        """
        Method untuk menambahkan foto baru
        """
        if not nama_file:
            print("Nama file tidak boleh kosong!") #Mengecek agar input tidak kosong
            return
        
        record = {
            "nama_file" : nama_file,
            "tanggal" : self._now()
        }
        
        self.add_node(record) #Menambahkan data ke Linked list
        self.save_to_file() #Menyimpan Linked list terbaru ke file txt
        print(f"Foto '{nama_file}' berhasil ditambahkan!")

    def update_photo(self, old_nama:str, new_nama:str):
        """
        Method untuk mengubah nama file foto
        """
        temp = self.head #Mencari data dari head

        while temp:
            #Jika data pada node sama dengan nama file yang dicari
            if temp.data["nama_file"] == old_nama:
                tanggal_edit = self._now()
                temp.data["nama_file"] = new_nama #Ganti nama data lama dengan data baru
                temp.data["tanggal"] = tanggal_edit #Memperbarui tanggal mjd tanggal baru
                self.save_to_file()
                print(f"Foto '{old_nama}' berhasil diubah menjadi '{new_data}'!")
                return

            temp = temp.next #Jika belum ditemukan, pindah ke node berikutnya

    def delete_photo(self, nama_file:str):
        """
        Method untuk menghapus foto dari Linked list
        """
        temp = self.head #Mulai mencari data dari head
        stack = Stack() #Membuat objek stack untuk menyimpan riwayat foto yang dihapus
        
        while temp: #Looping selama node masih ada
            if temp.data["nama_file"] == nama_file: #Jika data yang dicari ditemukan
                info_hapus = (f"{temp.data["nama_file"]} (ditambahkan: {temp.data["tanggal"]})")
                stack.add_trash(info_hapus)

                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next

                if temp.next :
                    temp.next.prev = temp.prev
                else:
                    self.tail = temp.prev 
                
                self.save_to_file()
                print(f"Foto {nama_file} berhasil dihapus")
                return
            temp=temp.next 
        print(f"gambar {nama_file} tidak ditemukan pada penyimpanan!")

    def display(self):
        """
        Method untuk menampilkan seluruh data foto dalam bentuk tabel
        """
        table = Table(title="Data Galeri Foto") #Membuat tabel dengan judul
        table.add_column("No", justify="center") #Menambahkan kolom nomor
        table.add_column("Nama File") #Menambahkan kolom nama file
        table.add_column("Tanggal", justify="center")

        temp = self.head #Mulai baca data dari head
        
        nomor = 1 #Nomor awal tabel

        if self.is_empty(): #Jika Linked list kosong, tampilkan keterangan
            table.add_row("-", "Belum ada data foto", "-")
        else: #Jika ada data, tampilkan ke tabel
            while temp:
                table.add_row(str(nomor), temp.data["nama_file"], temp.data.get("tanggal", "Tidak diketahui"))
                temp = temp.next #Pindah ke node berikutnya
                nomor += 1 #Nomor bertambah
        p(table) #Menampilkan tabel ke terminal

    def insertion_sort(self, by):
        """
        Method untuk mengurutkan data
        """

        if self.is_empty():
            print("Double Linked List masih kosong!")
            return
        if self.head.next is None:
            print("Hanya ada satu data tidak bisa diurutkan!")

        current = self.head.next
        while current:
            current_data = current.data
            temp = current.prev

            while temp and temp.data[by] > current_data[by]:
                temp.next.data = temp.data
                temp = temp.prev
                if temp == None:
                    self.head.data = current_data
                else:
                    temp.next.data = current_data
            
            current = current.next
        self.save_to_file()
    
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
    print("\n")
    print("=====================================")
    print("=         APLIKASI GALERI           =")
    print("= 1. Tambah Data Foto               =")
    print("= 2. Tampilkan Data Foto            =")
    print("= 3. Edit Data Foto                 =")
    print("= 4. Hapus Data Foto                =")
    print("= 5. Tampilkan Struktur DLL         =")
    print("= 6. Tampilkan Riwayat Hapus        =")
    print("= 7. Urutkan Foto                   =")
    print("= 8. Keluar                         =")
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
            dll.display()
            old_data = input("Masukkan Nama File yang Ingin Diedit: ").strip()
            new_data = input("Masukkan Nama File Baru: ").strip()
            dll.update_photo(old_data, new_data)
        
        elif choice == "4":
            dll.display()
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
            print("\nFoto dapat diurutkan berdasarkan:")
            print("1. Nama Foto (A-Z)")
            print("2. Tanggal")
            sort_choice = input("Masukkan Nomor Pengurutan yang Ingin Dilakukan(1/2): ").strip()
            if sort_choice == "1":
                by = "nama_file"
                dll.insertion_sort(by)
                dll.display()
            elif sort_choice =="2":
                by = "tanggal"
                dll.insertion_sort(by)
                dll.display()
            else:
                print("Pilihan tidak valid!")
        
        elif choice == "8":
            print("Program selesai. Terimakasih!")
            break
        
        else:
            print("Input Tidak Valid!")

        #Menanyakan apakah user ingin melanjutkan menggunakan aplikasi
        lanjut = input("\nLanjut menggunakan aplikasi? (klik 'y' untuk lanjut, klik apapun untuk keluar): ").strip().lower()

        if lanjut == "y":
            clear_screen() #Membersihkan layar sebelum menampilkan menu lagi
            continue
        else:
            print("Program selesai. Terimakasih!")
            break