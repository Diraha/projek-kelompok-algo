from rich.table import Table
from rich import print as p

class Node: #Class untuk membuat template node linked list
    def __init__(self, data):
        self.data = data #Membuat variabel data
        self.next = None #Membuat variabel next untuk pointer ke node selanjutnya

class Stack: #Class stack menggunakan linked list
    def __init__(self):
        
        self.head = None #Head stack (node paling atas)
        self.size = 0 #Menyimpan jumlah elemen stack

    def add_trash(self, data): #Fungsi untuk menambahkan data ke stack (push)
        new_node = Node(data) #Membuat node baru dengan data yang diberikan

        if self.head:
            new_node.next = self.head #Node baru menunjuk ke head lama

        self.head = new_node #Head sekarang menjadi node baru (data terbaru di atas)
        self.size += 1 #Ukuran stack bertambah satu

        with open("PROJEK_ALGO/DATABASE/data_sampah.txt", mode="a", encoding="utf-8") as file:
            file.write(f"{data}\n") #Jalankan method simpan data ke dalam file

    def display(self): #Fungsi untuk menampilkan isi stack
        temp = self.head #Mulai dari head

        while temp: #Iterasi selama node masih ada
            print(temp.data, end=" -> ")
            temp = temp.next #Pindah ke node berikutnya

        return print("NULL")
        
    def display_trash(self):
        self.table = Table() #Inisialisasi objek Table
        self.table.add_column("Nama File") #Buat 1 kolom baru

        with open("PROJEK_ALGO/DATABASE/data_sampah.txt", mode="r", encoding="utf-8") as file:
            lines = file.readlines() #Ambil/baca semua isi file, lalu simpan ke dalam variabel

            for line in lines: #Looping setiap nilai yang ada di dalam variabel lines
                data = line.strip() #Setiap nilai, bersihkan dulu dari elemen lain
                self.table.add_row(data) #Tambahkan nilai sebagai baris baru di dalam tabel

        return p(self.table) #Cetak hasil tabel