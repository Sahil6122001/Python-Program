class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        
    def printMiddle(self):
        slow_ptr = self.head
        fast_ptr = self.head
        if self.head is not None:
            while(fast_ptr is not None and 
                  fast_ptr.next is not None):
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
            print("The middle element is",slow_ptr.data)
            
llist = LinkedList()
llist.push(2)
llist.push(4)
llist.push(6)
llist.push(8)
llist.push(10)
llist.push(12)
llist.push(14)
llist.push(16)
llist.push(18)
llist.push(20)
llist.printMiddle()
