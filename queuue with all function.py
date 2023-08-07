class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    
    def __init__(self):
        self.front = None
        self.rear = None
    def is_empty(self):
        return self.front is None
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    
    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return data
    
    def display(self):
        current = self.front
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
        print()
if __name__ == "__main__":
    queue = Queue()
    
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    
    print("Queue Elements: ")
    queue.display()
    
    print("Dequeue:",queue.dequeue())
    print("Queue elements after deletion")
    queue.display()
    
    