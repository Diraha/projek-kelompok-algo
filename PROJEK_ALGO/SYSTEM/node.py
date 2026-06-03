from rich.table import Table #Menampilkan data dalam bentuk tabel di terminal
from rich import print as p #Membuat tampilan terminal lebih rapi dan bewarna
from history import Stack #Mengambil class Stack dari file riwayat.py, menyimpan riwayat foto yang sudah dihapus
from datetime import datetime
import json
import os
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel

class Node: #Class untuk membuat template node
    def __init__(self, data):
        self.data = data #Membuat variabel data
        self.next = None #Membuat variabel next untuk pointer ke node selanjutnya
        self.prev = None #Membuat variabel prev untuk pointer ke node sebelumnya

class DoubleLinkedList: #Class untuk menjalankan fitur CRUD(Create, Read, Update, Delete)
    def __init__(self):
        self.head = None
        self.tail = None
        self.load_from_file() #Saat program pertama kali dijalankan, data dari file txt dimasukkan kembali ke linked list
        self.stack = Stack() #Membuat objek stack untuk menyimpan riwayat foto yang dihapus

    def clear_console(self):
        """
        Method untuk membersihkan riwayat terminal
        """
        os.system("cls" if os.name == "nt" else "clear")

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
            with open("PROJEK_ALGO/DATABASE/data_image.json", mode="r", encoding="utf-8") as file:
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

        with open("PROJEK_ALGO/DATABASE/data_image.json", mode="w", encoding="utf-8") as file:
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
                return True

            temp = temp.next #Jika belum ditemukan, pindah ke node berikutnya

        return False
 
    def delete_photo(self, nama_file:str):
        """
        Method untuk menghapus foto dari Linked list
        """
        temp = self.head #Mulai mencari data dari head
        
        while temp: #Looping selama node masih ada
            if temp.data["nama_file"] == nama_file: #Jika data yang dicari ditemukan
                info_hapus = {"file_name": temp.data["nama_file"], "tanggal": temp.data["tanggal"]}
                self.stack.add_trash(info_hapus)

                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next

                if temp.next:
                    temp.next.prev = temp.prev
                else:
                    self.tail = temp.prev 
                
                return {"file_name": nama_file, "found": True}
            temp=temp.next
        return {"file_name": nama_file, "found": False}

    def display_table(self):
        """
        Method untuk menampilkan seluruh data foto dalam bentuk tabel
        """
        self.clear_console()

        table = Table(title="Gallery-HT")
        table.add_column("No", justify="center") #Menambahkan kolom nomor
        table.add_column("File Name") #Menambahkan kolom nama file
        table.add_column("Keterangan", justify="center")

        temp = self.head #Mulai baca data dari head
        
        nomor = 1 #Nomor awal tabel

        if self.is_empty(): #Jika Linked list kosong, tampilkan keterangan
            table.add_row("-", "Belum ada data foto", "-")
        else: #Jika ada data, tampilkan ke tabel
            while temp:
                table.add_row(str(nomor), f"{temp.data["nama_file"]:<127}", temp.data["tanggal"])
                temp = temp.next #Pindah ke node berikutnya
                nomor += 1 #Nomor bertambah
        p(table) #Menampilkan tabel ke terminal


    def display(self):
        """
        Method untuk menampilkan tabel foto dan pilihan user
        """
        self.display_table()

        print("\n[A]: Download Image                                                   [T]: Trash History                                                    [C]: Searching")
        print("[E]: Edit Image                                                       [S]: Display DBL Structure                                            [X]: Exit")
        print("[D]: Delete Image                                                     [R]: Sorting                                                          [I]: Gallery Information")

    def insertion_sort(self, by):
        """
        Method untuk mengurutkan data
        """

        if self.is_empty():
            print("Double Linked List masih kosong!")
            return
        if self.head.next is None: #Cek data kedua apkh kosong
            print("Hanya ada satu data tidak bisa diurutkan!")

        current = self.head.next #Mulai dari node kedua
        while current: 
            current_data = current.data #Simpan data sementara
            temp = current.prev #Mulai dari kiri karena cari posisi dari kiri

            while temp and temp.data[by] > current_data[by]: #Cek node nya masih ada gak
                temp.next.data = temp.data #Geser kanan
                temp = temp.prev
                if temp == None: #Kalau udah habis data jadi paling depan
                    self.head.data = current_data
                else: #Kalau masih ada data jadi setelah temp
                    temp.next.data = current_data
            
            current = current.next
        self.save_to_file()
    
    def display_dbl_vertical(self):
        """
        Menampilkan struktur Double Linked List dengan split terminal
        """
        if self.is_empty():
            print("Double Linked List Kosong!")
            return
        
        console = Console()

        # Panel kiri (Head -> Tail)
        next_text = "[bold green]HEAD[/bold green]\n |\n"

        temp = self.head
        while temp:
            next_text += f"[ {temp.data['nama_file']} ]\n"

            if temp.next:
                next_text += " |\n v\n"
            
            temp = temp.next
        next_text += " |\nNULL"

        # Panel Kanan (Tail -> Head)
        prev_text = "[bold cyan]TAIL[/bold cyan]\n |\n"

        temp = self.tail
        while temp:
            prev_text += f"[ {temp.data['nama_file']} ]\n"

            if temp.prev:
                prev_text += " ^\n |\n"

            temp = temp.prev
        prev_text += " |\nNULL"

        # Split Terminal
        layout = Layout()

        layout.split_row(
            Layout(
                Panel(
                    next_text,
                    title="NEXT POINTER (HEAD -> TAIL)",
                    border_style="green"
                ),
                name="left"
            ),
            Layout(
                Panel(
                    prev_text,
                    title="PREV POINTER (TAIL -> HEAD)",
                    border_style="cyan"
                ),
                name="right"
            )
        )

        console.print(layout)
        input("\nTekan Enter untuk kembali...")
        
    def binary_search(self, target:str):
        """
        Method untuk mencari foto berdasarkan file menggunakan Binary Search
        """

        self.insertion_sort("nama_file") #Memastikan data sudah terurut berdasarkan nama_file
        data_list = []
        temp = self.head #Ubah linked list menjadi list biasa untuk diakses berdasarkan index

        while temp:
            data_list.append(temp.data)
            temp = temp.next

        low = 0
        high = len(data_list) - 1

        while low <= high:
            mid = (low + high) // 2

            nama_tengah = data_list[mid]["nama_file"]

            #Jika ditemukan
            if nama_tengah == target:
                return {"date": data_list[mid]['tanggal'], "found": True}
            #Jika target lebih kecil
            elif target < nama_tengah:
                high = mid - 1
            #Jika target lebih besar
            else:
                low = mid + 1

        return {"found": False}
    
    def gallery_information(self):
        """
        Method untuk menampilkan informasi galeri
        """

        print("========== GALLERY INFO ==========\n")

        total = 0
        temp = self.head
        
        #menghitung jumlah foto pada galeri
        while temp:
            total += 1
            temp = temp.next

        print(f"Total Foto: {total}")

        #jika galeri kosong
        if self.head is None:
            print("Gallery Kosong")

        else:
            #menampilkan foto pertama dan terakhir
            print(f"Foto Pertama: {self.head.data['nama_file']}")
            print(f"Foto Terakhir: {self.tail.data['nama_file']}")
        print("\n========== GALLERY INFO ==========")

        input_user = input("Tekan Enter untuk Kembali...")
        input_user