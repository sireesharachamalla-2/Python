
class Queue:
    def __init__(self):
        self.queue = []

    def queues(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)  
        return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print(self.queue) 
q = Queue()

q.queues(10)
q.queues(20)
q.display()       
removed = q.dequeue()
print("Dequeued:", removed)  
q.display() 
