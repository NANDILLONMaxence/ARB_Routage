class Queue:
    def __init__(self):
        self.elements = []

    def enqueue(self, elt):
        self.elements.insert(0, elt)

    def dequeue(self):
        return self.elements.pop()

    def peek(self):
        return self.elements[-1]

    def isempty(self):
        return len(self.elements) == 0