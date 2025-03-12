class Stack:
    def __init__(self):
        """Initialise une pile vide."""
        self.elements = []

    def push(self, elt):
        """Ajoute un élément en haut de la pile."""
        self.elements.append(elt)

    def pop(self):
        """Retire et retourne l'élément en haut de la pile."""
        if self.is_empty():
            return None
        return self.elements.pop()

    def peek(self):
        """Retourne l'élément en haut de la pile sans le retirer."""
        if self.is_empty():
            return None
        return self.elements[-1]

    def is_empty(self):
        """Vérifie si la pile est vide."""
        return len(self.elements) == 0
