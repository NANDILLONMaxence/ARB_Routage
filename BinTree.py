# Initialisation du module BinTree
class BinTree:
    def __init__(self, key, route_info, left=None, right=None):
        """
        Initialise un noeud de l'arbre binaire
        :param key: Clé du noeud (adresse IP).
        :param route_info: Information de routage associées
        :param left: Sous-arbre gauche.
        :param right: Sous-arbre droit.
        """
        self.key = key
        self.route_info = route_info
        self.left = None
        self.right = None
