class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp is None:
            return
        prev.next = temp.next
        temp = None

    def delete_at_beginning(self):
        if self.head:
            curr = self.head
            self.head = curr.next
            curr = None
        else:
            print("nothing in list")

    def search(self, key):
        curr = self.head
        prev = None
        index = 0
        while curr:
            if curr.data == key:
                print("Found at index:", index)
                return
            prev = curr
            curr = curr.next
            index += 1
        print("Not found in the linked list")

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")


# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)
    linked_list.insert_at_end(4)
    linked_list.insert_at_end(5)

    linked_list.print_list()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> None

    linked_list.insert_at_beginning(0)
    linked_list.print_list()  # Output: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None

    linked_list.delete_at_beginning()
    linked_list.print_list()  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> None

    linked_list.delete(3)
    linked_list.print_list()  # Output: 1 -> 2 -> 4 -> 5 -> None

    print(linked_list.search(3))  # Output: False
    print(linked_list.search(4))  # Output: True
