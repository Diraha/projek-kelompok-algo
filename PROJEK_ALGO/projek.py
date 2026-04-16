from riwayat import Stack

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
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
            with open("data_image.txt", mode="a", encoding="utf-8") as file:
                file.write(f"{temp.data}\n")
                temp = temp.next

        return print("Selesai!")

    def display_next(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        return print("NULL")

    def display_previous(self):
        temp = self.tail

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev

        return print("NULL")

    def delete_photo(self, data):
        s = Stack()
        s.add_trash(data)

dll = DoubleLinkedList()
input_user = input("Masukkan Nama File Gambar: ")
input_user2 = input("Masukkan Nama File Yang Ingin Dihapus: ")
dll.add_photo(input_user)
dll.delete_photo(input_user2)

print("hai")