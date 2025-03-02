class Stack:
    def __init__(self):
        self.elements = []

    def push(self, elt):
        self.elements.append(elt)

    def pop(self):
        return self.elements.pop()

    def peek(self):
        return self.elements[-1]

    def isempty(self):
        return len(self.elements) == 0