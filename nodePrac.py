class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None  # Head (first node)

    def append(self, data):
        """Adds a new node to the end of the list."""
        new_node = Node(data)
        
        if not self.head:  # If list is empty, set head
            self.head = new_node
            return
        
        last = self.head
        while last.next:  # Traverse to the last node
            last = last.next
        
        last.next = new_node  # Link last node to new node

    def display(self):
        """Prints all nodes in the linked list."""
        current = self.head
        while current:
            print(current.data, end=" -> ")  # Print node data
            current = current.next
        print("None")  # Indicate end of list

# Testing the Linked List
ll = LinkedList()
ll.append("Alice")
ll.append("Bob")
ll.append("Charlie")

ll.display()  # Output: Alice -> Bob -> Charlie -> None
