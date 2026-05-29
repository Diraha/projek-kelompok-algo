from rich.table import Table #Menampilkan riwayat dalam bentuk tabel
from rich import print as p #Agar tampilan terminal lebih rapi
import json
import os
import time
from termcolor import colored

class Node:
    """
    Class Stack menggunakan konsep Linked List untuk
    menyimpan riwayat gambar yang terhapus
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack: #Class untuk membuat template node linked list
    def __init__(self):
        self.head = None
        self.load_from_file()

    #menambahkan data ke stack
    def add_trash(self, value):
        new_node = Node(value)

        if self.head:
            new_node.next = self.head
        
        self.head = new_node

        self.save_to_file()

    #menyimpan data ke file json
    def save_to_file(self):
        data = [] #list kosong untuk menampung data stack

        current = self.head

        #loop selama node masih ada
        while current:
            data.append(current.value) #menambahkan value node ke list
            current = current.next #berpindah ke node berikutnya

        #membuka file JSON dalam node write
        with open("PROJEK_ALGO/DATABASE/data_sampah.json", mode="w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    #membaca data dari file JSON
    def load_from_file(self):
        try:
            #membuka file JSON
            with open("PROJEK_ALGO/DATABASE/data_sampah.json", "r") as file:
                data = json.load(file)
            
            #membalik data agar urutan stack tetap benar
            for item in reversed(data):
                #menambahkan data ke stack
                self.add_trash(item)

        #jika file tidak ditemukan
        except FileNotFoundError:
            print("Database Tidak Ditemukan!")

    #menghapus semua data trash
    def delete_trash():
        pass

    #menampilkan riwayat trash
    def display_trash(self):
        #membuat tabel Rich
        table = Table(title="Riwayat Gambar Terhapus")

        #membuat kolom tabel
        table.add_column("No")
        table.add_column("File Name")
        table.add_column("Date")

        num = 1 #nomor urut

        temp = self.head #variabel sementara untuk traversal

        #liip selama node masih ada
        while temp:
            #menambahkan baris ke tabel
            table.add_row(str(num), f"{temp.value['file_name']:<127}", temp.value["tanggal"])
            num += 1 #increment nomor
            temp = temp.next #pindah ke node berikutnya
        
        p(table) #menampilkan tabel menggunakan rich

        print("\n[D]: Clear Trash                                                   [S]: Display Stack Structure                                                     [B]: Back\n")

    #menampilkan struktur stack
    def display_stack_structure(self):
        current = self.head #variabel current untuk traversal
        
        while current: #selama loop node masih ada
            #tampilkan nama file dan arah pointer
            print(current.value["file_name"], end="-> ")
            current = current.next #pindah ke node berikutnya

#function display
def display():
    stack = Stack() #membuat object stack

    while True:
        os.system("cls" if os.name == "nt" else "clear") #membersihkan terminal

        stack.display_trash() #menampilkan riwayat trash

        input_user = input("Masukkan Pilihan Anda: ").strip().upper()

        #clear trash
        if input_user == "D":
            stack.delete_trash() #memanggil function delete_trash

        #tampilkan struktur stack
        elif input_user == "S":
            stack.display_stack_structure()
            break

        #kembali ke gallery
        elif input_user == "B":
            from main import gallery
            gallery()
            break

        #input tidak valid
        else:
            print(colored("Input Tidak Valid!", "red")) #menampilkan pesan error
            time.sleep(1.5)