
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        return self.stack

s = Stack()
s.push(10)
s.push(20)
print("Stack after pushes:", s.display())
popped = s.pop()
print("Popped element:", popped)
print("Stack now:", s.display())
