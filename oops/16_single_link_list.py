
class Node:
    def __init__(self, data):
        self.data = data      
        self.next = None     


class LinkedList:
    def __init__(self):
        self.head = None    

    def insert(self, value):
        new_node = Node(value)
        if self.head is None:             
            self.head = new_node
        else:
            current = self.head
            while current.next:           
                current = current.next
            current.next = new_node       

    def delete(self, value):
        current = self.head
        prev = None

        while current:
            if current.data == value:
                if prev is None:          
                    self.head = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
ll = LinkedList()
ll.insert(10)
ll.insert(20)

print("List after insertions:", ll.display()) 
ll.delete(10)
print("List after deleting 10:", ll.display()) 