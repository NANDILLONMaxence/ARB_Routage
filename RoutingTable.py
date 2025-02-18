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
        return root
    
    # Si l'adresse IP est plus petite que la clé actuelle, on cherche à gauche
    if root.key < ip:
        return search_route(root.left, ip)
    
    # Sinon on cherche à droite
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
    
    # Sinon, on cherche la route à supprimer

    # Si l'adresse IP est plus petite que la clé actuelle, on cherche à gauche
    if ip < root.key:
        root.left = delete_route(root.left, ip)

    # Sinon, on cherche à droite
    elif ip > root.key:
        root.right = delete_route(root.right, ip)

    #
    else:
        # Cas 1 




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

