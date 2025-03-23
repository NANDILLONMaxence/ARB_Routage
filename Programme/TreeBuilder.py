# Version: 1.0
# Subject: Construction de l'arbre binaire de routage
# Created by: NANDILLON Maxence

from BinTree import BinTree

# def build_tree():
#     """
#     Cette fonction crée un arbre binaire de routage avec des nœuds représentant des sous-réseaux IP et leurs routeurs associés.
#     Chaque nœud de l'arbre contient une adresse IP ou un sous-réseau et un nom de routeur. 
#     Elle retourne la racine de cet arbre.
    
#     :return: La racine de l'arbre binaire qui représente le réseau et ses routeurs.
#     """
#     # Création de la racine de l'arbre, représentant un réseau "192.168.1.0/24" et un routeur "RT1"
#     root = BinTree("192.168.1.0/24", "RT1",
#         # Le sous-arbre gauche représente le réseau "10.0.0.0/8" et le routeur "RT3"
#         left=BinTree("10.0.0.0/8", "RT3",
#             # Le sous-arbre gauche de RT3 représente le réseau "192.168.10.0/24" et le routeur "RT4"
#             left=BinTree("192.168.10.0/24", "RT4",
#                 # Sous-arbres de RT4
#                 left=BinTree("192.168.40.0/24", "RT8"),  # RT8 : réseau "192.168.40.0/24"
#                 right=BinTree("192.168.50.0/24", "RT9")  # RT9 : réseau "192.168.50.0/24"
#             ),
#             # Le sous-arbre droit de RT3 représente le réseau "192.168.20.0/24" et le routeur "RT5"
#             right=BinTree("192.168.20.0/24", "RT5",
#                 # Sous-arbres de RT5
#                 left=BinTree("172.18.0.0/16", "RT10"),  # RT10 : réseau "172.18.0.0/16"
#                 right=BinTree("192.168.60.0/24", "RT11")  # RT11 : réseau "192.168.60.0/24"
#             )
#         ),
#         # Le sous-arbre droit représente le réseau "172.16.0.0/16" et le routeur "RT2"
#         right=BinTree("172.16.0.0/16", "RT2",
#             # Sous-arbre gauche de RT2 représentant le réseau "172.17.0.0/16" et le routeur "RT6"
#             left=BinTree("172.17.0.0/16", "RT6"),
#             # Sous-arbre droit de RT2 représentant le réseau "192.168.30.0/24" et le routeur "RT7"
#             right=BinTree("192.168.30.0/24", "RT7")
#         )
#     )

#     # Retourner la racine de l'arbre, qui est le point de départ de l'arbre binaire de routage
#     return root

def build_tree():
    """
    Cette fonction crée un arbre binaire de routage avec des nœuds représentant des sous-réseaux IP et leurs routeurs associés.
    Chaque nœud de l'arbre contient une adresse IP ou un sous-réseau et un nom de routeur.
    Elle retourne la racine de cet arbre.
    """
    root = BinTree("192.168.1.0/24", "RT1",
        # Le sous-arbre gauche représente le réseau "10.0.0.0/8" et le routeur "RT3"
        left=BinTree("10.0.0.0/8", "RT3",
            # Le sous-arbre gauche de RT3 représente le réseau "192.168.10.0/24" et le routeur "RT4"
            left=BinTree("192.168.10.0/24", "RT4",
                # Sous-arbres de RT4
                left=BinTree("192.168.40.0/24", "RT8"),
                right=BinTree("192.168.50.0/24", "RT9")
            ),
            # Le sous-arbre droit de RT3 représente le réseau "192.168.20.0/24" et le routeur "RT5"
            right=BinTree("192.168.20.0/24", "RT5",
                # Sous-arbres de RT5
                left=BinTree("172.18.0.0/16", "RT10"),
                right=BinTree("192.168.60.0/24", "RT11")
            ),
            # Le sous-arbre gauche supplémentaire de RT3 représente le réseau "192.168.70.0/24" et le routeur "RT12"
            left_right=BinTree("192.168.70.0/24", "RT12",
                # Sous-arbres de RT12
                left=BinTree("192.168.80.0/24", "RT16"),
                right=BinTree("192.168.90.0/24", "RT17")
            ),
            # Le sous-arbre droit supplémentaire de RT3 représente le réseau "192.168.80.0/24" et le routeur "RT13"
            right_right=BinTree("192.168.85.0/24", "RT13")
        ),
        # Le sous-arbre droit représente le réseau "172.16.0.0/16" et le routeur "RT2"
        right=BinTree("172.16.0.0/16", "RT2",
            # Sous-arbre gauche de RT2 représentant le réseau "172.17.0.0/16" et le routeur "RT6"
            left=BinTree("172.17.0.0/16", "RT6",
                # Sous-arbres de RT6
                left=BinTree("172.18.20.0/24", "RT18"),
                right=BinTree("172.18.30.0/24", "RT19")
            ),
            # Sous-arbre droit de RT2 représentant le réseau "192.168.30.0/24" et le routeur "RT7"
            right=BinTree("192.168.30.0/24", "RT7",
                # Sous-arbres de RT7
                left=BinTree("192.168.45.0/24", "RT14"),
                right=BinTree("172.19.0.0/16", "RT15")
            ),
            # Le sous-arbre gauche supplémentaire de RT2 représente le réseau "172.20.0.0/16" et le routeur "RT20"
            left_left=BinTree("172.20.0.0/16", "RT20"),
            # Le sous-arbre droit supplémentaire de RT2 représente le réseau "172.21.0.0/16" et le routeur "RT21"
            right_right=BinTree("172.21.0.0/16", "RT21")
        )
    )

    # Retourner la racine de l'arbre, qui est le point de départ de l'arbre binaire de routage
    return root

