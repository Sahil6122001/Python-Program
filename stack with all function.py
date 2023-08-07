class Stack:
    def __init__(self,size):
        self.stack=[]
        self.top = -1
        self.size = size
        
    def is_empty(self):
        return self.top ==-1
    def is_full(self):
        return self.top == self.size-1
    
    def push(self, data):
        if self.is_full():
            print("Stack is full")
        else:
            self.stack.append(data)
            self.top +=1
    def pop(self):
        if self.is_empty():
            print("stack is empty")
            return None
        data = self.stack.pop()
        self.top -=1
        return data
    def display(self):
        if self.is_empty():
            print("stack is empty")
        else:
            print("stack elements")
            for i in range(self.top,-1,-1):
                print(self.stack[i])

if __name__ == "__main__":
    ssize = int(input("Enter the size of stack:- "))
    my_stack = Stack(ssize)
    
    while True:
        print("\nChoose an option:")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")

        choice = int(input("Choice:- "))

        if choice == 1:
            element = int(input("Enter the element to push: "))
            my_stack.push(element)
        elif choice == 2:
            pop_item = my_stack.pop()
            if pop_item is not None:
                print("Popped Item:", pop_item)
        elif choice == 3:
            my_stack.display()
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please try again.")