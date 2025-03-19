# Importation de la classe BinTree pour manipuler des arbres binaires
from BinTree import BinTree

def build_tree():
    """
    Cette fonction crée un arbre binaire de routage avec des nœuds représentant des sous-réseaux IP et leurs routeurs associés.
    Chaque nœud de l'arbre contient une adresse IP ou un sous-réseau et un nom de routeur. 
    Elle retourne la racine de cet arbre.
    
    :return: La racine de l'arbre binaire qui représente le réseau et ses routeurs.
    """
    # Création de la racine de l'arbre, représentant un réseau "192.168.1.0/24" et un routeur "RT1"
    root = BinTree("192.168.1.0/24", "RT1",
        # Le sous-arbre gauche représente le réseau "10.0.0.0/8" et le routeur "RT3"
        left=BinTree("10.0.0.0/8", "RT3",
            # Le sous-arbre gauche de RT3 représente le réseau "192.168.10.0/24" et le routeur "RT4"
            left=BinTree("192.168.10.0/24", "RT4",
                # Sous-arbres de RT4
                left=BinTree("192.168.40.0/24", "RT8"),  # RT8 : réseau "192.168.40.0/24"
                right=BinTree("192.168.50.0/24", "RT9")  # RT9 : réseau "192.168.50.0/24"
            ),
            # Le sous-arbre droit de RT3 représente le réseau "192.168.20.0/24" et le routeur "RT5"
            right=BinTree("192.168.20.0/24", "RT5",
                # Sous-arbres de RT5
                left=BinTree("172.18.0.0/16", "RT10"),  # RT10 : réseau "172.18.0.0/16"
                right=BinTree("192.168.60.0/24", "RT11")  # RT11 : réseau "192.168.60.0/24"
            )
        ),
        # Le sous-arbre droit représente le réseau "172.16.0.0/16" et le routeur "RT2"
        right=BinTree("172.16.0.0/16", "RT2",
            # Sous-arbre gauche de RT2 représentant le réseau "172.17.0.0/16" et le routeur "RT6"
            left=BinTree("172.17.0.0/16", "RT6"),
            # Sous-arbre droit de RT2 représentant le réseau "192.168.30.0/24" et le routeur "RT7"
            right=BinTree("192.168.30.0/24", "RT7")
        )
    )

    # Retourner la racine de l'arbre, qui est le point de départ de l'arbre binaire de routage
    return root
