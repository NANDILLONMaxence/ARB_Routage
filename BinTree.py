class BinTree:
    def __init__(self, key, route_info, left=None, right=None):
        """
        Initialise un nœud de l'arbre binaire.

        Un arbre binaire est une structure où chaque nœud a au maximum deux enfants : un à gauche et un à droite.
        Cette classe permet de créer un nœud qui représente une adresse IP et ses informations de routage associées.

        :param key: Clé du nœud (adresse IP).
            - Cette clé représente une adresse IP qui identifie le nœud dans l'arbre.
            - Par exemple, une clé peut être "192.168.1.0/24" pour une plage d'adresses.
        
        :param route_info: Information de routage associée à ce nœud.
            - Cette information contient des détails sur le routage associés à l'adresse IP. Cela peut être un nom de routeur, une description ou d'autres informations pertinentes pour la table de routage.
        
        :param left: Sous-arbre gauche.
            - Ce paramètre représente le sous-arbre gauche du nœud. Un sous-arbre gauche est un autre nœud qui est lié à celui-ci.
            - Si le nœud n'a pas d'enfant gauche, ce paramètre est `None`.
        
        :param right: Sous-arbre droit.
            - Comme pour le sous-arbre gauche, ce paramètre représente l'enfant droit du nœud.
            - Si le nœud n'a pas d'enfant droit, ce paramètre est aussi `None`.
        """
        
        # Attribuer la clé (adresse IP) du nœud
        self.key = key
        
        # Attribuer les informations de routage à ce nœud
        self.route_info = route_info
        
        # Attribuer le sous-arbre gauche (enfant gauche)
        self.left = left
        
        # Attribuer le sous-arbre droit (enfant droit)
        self.right = right
