class Queue:
    def __init__(self):
        """
        Initialise une file vide.
        """
        self.elements = []

    def enqueue(self, elt):
        """
        Ajoute un élément à la file (FIFO).
        
        Paramètres :
            elt : Élément à ajouter à la file.
        """
        self.elements.append(elt)  # Ajout en fin de liste

    def dequeue(self):
        """
        Retire et retourne l'élément en tête de la file.
        
        Retourne :
            L'élément retiré ou None si la file est vide.
        """
        if self.is_empty():
            return None
        return self.elements.pop(0)  # Retrait du premier élément (FIFO)

    def peek(self):
        """
        Retourne l'élément en tête de file sans le retirer.
        
        Retourne :
            L'élément en tête ou None si la file est vide.
        """
        if self.is_empty():
            return None
        return self.elements[0]

    def is_empty(self):
        """
        Vérifie si la file est vide.
        
        Retourne :
            bool : True si la file est vide, sinon False.
        """
        return len(self.elements) == 0