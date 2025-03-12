class Queue:
    def __init__(self):
        """Initialise une file vide."""
        self.elements = []

    def enqueue(self, elt):
        """Ajoute un élément à la file (FIFO)."""
        self.elements.append(elt)  # Ajout en fin de liste

    def dequeue(self):
        """Retire et retourne l'élément en tête de la file."""
        if self.is_empty():
            return None
        return self.elements.pop(0)  # Retrait du premier élément (FIFO)

    def peek(self):
        """Retourne l'élément en tête de file sans le retirer."""
        if self.is_empty():
            return None
        return self.elements[0]

    def is_empty(self):
        """Vérifie si la file est vide."""
        return len(self.elements) == 0
