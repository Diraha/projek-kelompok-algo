from rich.table import Table #Menampilkan riwayat dalam bentuk tabel
from rich import print as p #Agar tampilan terminal lebih rapi
import json

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack: #Class untuk membuat template node linked list
    def __init__(self):
        self.head = None

    def add_trash(self, value):
        new_node = Node(value)

        if self.head:
            new_node.next = self.head
        
        self.head = new_node

        self.save_to_file()

    def save_to_file(self):
        data = []

        current = self.head

        while current:
            data.append(current.value)
            current = current.next

        with open("PROJEK_ALGO/DATABASE/data_sampah.json", mode="w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    def display_trash(self):
        table = Table(title="Riwayat Gambar Terhapus")
        table.add_column("No")
        table.add_column("File Name")
        table.add_column("Date")

        num = 1

        temp = self.head

        while temp:
            table.add_row(str(num), f"{temp.value["file_name"]:<127}", temp.value["tanggal"])
            num += 1
            temp = temp.next
        
        p(table)