from BinTree import BinTree

 
def insert_route(root, ip, route_info):
    """
    Insérer une route dans la table de routage (arbre binaire).

    :param root: Racine de l'arbre binaire.
    :param ip: Adresse IP de la route à rechercher.
    :param route_info: Information de routage associées à la route.
    :return: Racine de l'arbre binaire mise à jour.
    """
    if root is None:
        return BinTree(ip, route_info)
    
    # Si l'adresse IP est plus petite que la clé actuelle, on va à gauche
    if ip < root.key:
        root.left = insert_route(root.left, ip, route_info)
    
    # Sinon, on va à droite
    else:
        root.right = insert_route(root.right, ip, route_info)

    return root


def search_route(root, ip):
    """
    Recherche une route dans la table de routage (arbre binaire).

    :param root: Racine de l'arbre binaire.
    :param ip: Adresse IP de la route à rechercher.
    :return: Le noeud contenant la route, ou None si non trouvée.
    """

    # Si l'arbre est vide ou si la clé est égale à l'adresse IP recherchée on retourne la racine.
    if root is None or root.key == ip:
        print(f"Visité : {root.key if root else 'None'}")
        return root
    
    print(f"Visité : {root.key}")
    # Si l'adresse IP est plus petite que la clé actuelle, on cherche à gauche
    if ip < root.key:
        return search_route(root.left, ip)
    
    # Sinon, on cherche à droite
    return search_route(root.right, ip)

def delete_route(root, ip):
    """
    Supprimer une route de la table de routage.

    :param root: Racine de l'arbre binaire.
    :param ip: Adresse IP de la route à supprimer.
    :return: Racine de l'arbre binaire mise à jour.
    """
    # Si l'arbre est vide, on retourne la racine. 
    if root is None:
        return root
    
    # Si l'adresse IP est inférieure à la clé du nœud actuel, on va à gauche
    if ip < root.key:
        root.left = delete_route(root.left, ip)

    # Si l'adresse IP est supérieure, on va à droite
    elif ip > root.key:
        root.right = delete_route(root.right, ip)

    # Si on a trouvé le nœud à supprimer
    else:
        # Cas 1 : Le nœud n'a pas d'enfant à gauche
        if root.left is None:
            return root.right
        
        # Cas 2 : Le nœud n'a pas d'enfant à droite
        elif root.right is None:
            return root.left
        
        # Cas 3 : Le nœud a deux enfants
        else:
            # On trouve le successeur (le plus petit nœud dans le sous-arbre droit)
            temp = min_value_node(root.right)

            # On remplace la clé et les informations de routage
            root.key = temp.key
            root.route_info = temp.route_info

            # On supprime le successeur
            root.right = delete_route(root.right, temp.key)
    
    return root

def min_value_node(node):
    """
    Trouver le noeud avec la valeur minimale

    :param node: Noeud à partir duquel commencer la recherche
    :return: Noeud avec la valeur minimale
    """
    current = node
    while current.left is not None:
        current = current.left
    return current

