class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current is None:
            return
        prev.next = current.next
        current = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Example usage
linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

linked_list.prepend(0)

linked_list.insert_after_node(linked_list.head.next, 1.5)

linked_list.display()  # Output: 0 1 1.5 2 3 4

linked_list.delete_node(1.5)

linked_list.display()  # Output: 0 1 2 3 4
