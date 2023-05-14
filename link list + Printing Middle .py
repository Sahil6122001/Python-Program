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
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
    
    def printMiddle(self):
        slow_ptr = self.head
        fast_ptr = self.head
        if self.head is not None:
            while(fast_ptr is not None and 
                  fast_ptr.next is not None):
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
            print("The middle element is",slow_ptr.data)
            

linked_list = LinkedList()

while True:
    element = input("Enter an element of the linked list (or enter 'q' to stop): ")
    if element == 'q':
        break
    linked_list.append(int(element))

linked_list.print_list()
linked_list.printMiddle()
