class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node3=Node("Eugeo")
node2=Node("Alice")
node1=Node("Ahnaf")
node1.next = node2
node2.next = node3

print(node1.data)
print(node1.next.data)
print(node1.next.next.data)
# print(node1)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def appendN(self, data):
        #"""Adds a new node to the end of the list."""
        new_node = Node(data)
        
        if not self.head: 
            self.head = new_node
            return
        
        last = self.head
        while last.next:  
            last = last.next
        
        last.next = new_node  

    def display(self):
        # """Prints all nodes in the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")  # Print node data
            current = current.next
        print("None")  # Indicate end of list

# Testing the Linked List
ll=linkedlist()
ll.appendN("Alice")
ll.appendN("Bob")
ll.appendN("Charlie")

ll.display()  # Output: Alice -> Bob -> Charlie -> None
