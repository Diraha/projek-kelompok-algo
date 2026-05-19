from rich.table import Table #Menampilkan riwayat dalam bentuk tabel
from rich import print as p #Agar tampilan terminal lebih rapi
import json
import os
import time
from termcolor import colored

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack: #Class untuk membuat template node linked list
    def __init__(self):
        self.head = None
        self.load_from_file()

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

    def load_from_file(self):
        try:
            with open("PROJEK_ALGO/DATABASE/data_sampah.json", "r") as file:
                data = json.load(file)

            for item in reversed(data):
                self.add_trash(item)
        except FileNotFoundError:
            print("Database Tidak Ditemukan!")

    def delete_trash():
        pass

    def display_trash(self):
        table = Table(title="Riwayat Gambar Terhapus")
        table.add_column("No")
        table.add_column("File Name")
        table.add_column("Date")

        num = 1

        temp = self.head

        while temp:
            table.add_row(str(num), f"{temp.value['file_name']:<127}", temp.value["tanggal"])
            num += 1
            temp = temp.next
        
        p(table)

        print("\n[D]: Clear Trash                                                   [S]: Display Stack Structure                                                     [B]: Back\n")

    def display_stack_structure(self):
        current = self.head
        
        while current:
            print(current.value["file_name"], end="-> ")
            current = current.next

def display():
    stack = Stack()

    while True:
        os.system("cls" if os.name == "nt" else "clear")

        stack.display_trash()

        input_user = input("Masukkan Pilihan Anda: ").strip().upper()

        if input_user == "D":
            stack.delete_trash()
        elif input_user == "S":
            stack.display_stack_structure()
            break
        elif input_user == "B":
            from main import gallery
            gallery()
            break
        else:
            print(colored("Input Tidak Valid!", "red"))
            time.sleep(1.5)