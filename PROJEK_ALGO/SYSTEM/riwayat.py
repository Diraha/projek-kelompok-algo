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

        self.save_trash() #Simpan hanya data baru ke file

    def display(self): #Fungsi untuk menampilkan isi stack
        temp = self.head #Mulai dari head

        while temp: #Iterasi selama node masih ada
            print(temp.data, end=" -> ")
            temp = temp.next #Pindah ke node berikutnya

        return print("NULL")
    
    def save_trash(self): #Fungsi untuk menyimpan data ke file
        temp = self.head

        while temp:
            with open("PROJEK_ALGO/DATABASE/data_sampah.txt", mode="a", encoding="utf-8") as file: #Buka file dalam mode append(tidak menghapus data lama)
                file.write(f"{temp.data}\n") #Tulis data baru ke file
                temp = temp.next

        return print("Selesai!") #Print konfirmasi