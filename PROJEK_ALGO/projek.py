from riwayat import Stack
from rich.table import Table
from rich import print as p

class Node: #Class untuk membuat template node
    def __init__(self, data):
        self.data = data #Membuat variabel data
        self.next = None #Membuat variabel next untuk pointer ke node selanjutnya
        self.prev = None #Membuat variabel prev untuk pointer ke node sebelumnya

class DoubleLinkedList: #Class untuk menjalankan fitur CRUD(Create, Read, Update, Delete)
    def __init__(self):
        self.head = None
        self.tail = None

    def add_photo(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.save_file()

    def save_file(self):
        temp = self.head

        while temp:
            with open("PROJEK_ALGO/data_image.txt", mode="a", encoding="utf-8") as file:
                file.write(f"{temp.data}\n")
                temp = temp.next

        return print("Selesai!")

    def delete_photo(self, data_image):
        with open("PROJEK_ALGO/data_image.txt", mode="r+", encoding="utf-8") as file:
            lines = file.readlines()

            file.seek(0)
            file.truncate()

            s = Stack()

            for line in lines:
                data = line.strip().split(",")

                if data[0] == data_image:
                    s.add_trash(data_image)
                else:
                    file.write(line)

    def display(self):
        self.table = Table()
        self.table.add_column("Nama File")

        with open("PROJEK_ALGO/data_image.txt", mode="r", encoding="utf-8") as file:
            lines = file.readlines()

            for line in lines:
                data = line.strip()
                self.table.add_row(data)

        return p(self.table)

dll = DoubleLinkedList()
# input_user = input("Masukkan Nama File Gambar: ")
# input_user2 = input("Masukkan Nama File Yang Ingin Dihapus: ")
# dll.add_photo(input_user)
# dll.delete_photo(input_user2)
dll.display()