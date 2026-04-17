class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_trash(self, data):
        new_node = Node(data)

        if self.head:
            new_node.next = self.head

        self.head = new_node
        self.size += 1

        self.save_trash()

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        return print("NULL")
    
    def save_trash(self):
        temp = self.head

        while temp:
            with open("PROJEK_ALGO/data_sampah.txt", mode="a", encoding="utf-8") as file:
                file.write(f"{temp.data}\n")
                temp = temp.next

        return print("Selesai!")