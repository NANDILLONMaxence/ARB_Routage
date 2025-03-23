# Version: 1.0
# Subject: Gestionnaire de route
# Created by: NANDILLON Maxence

from Queue import Queue

def bfs_mark_unreachable(root, ip):
    """
    Marque un réseau et tous ses sous-réseaux comme inaccessibles en utilisant un parcours BFS.
    
    Paramètres :
        root (Node) : Racine de l'arbre binaire de routage.
        ip (str) : Adresse IP du réseau à marquer comme inaccessible.
    
    Retourne :
        set : Ensemble des adresses IP des réseaux inaccessibles.
    """
    unreachable = set()
    queue = Queue()
    queue.enqueue(root)

    # Recherche du nœud correspondant à l'adresse IP donnée
    while not queue.is_empty():
        current = queue.dequeue()
        if current.key == ip:
            queue.enqueue(current)  # Ajouter pour marquer ses descendants
            break  # On a trouvé le nœud en panne

    # Marquer tous les sous-réseaux comme inaccessibles
    while not queue.is_empty():
        node = queue.dequeue()
        unreachable.add(node.key)
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)

    return unreachable


def delete_route(root, ip):
    """
    Supprime un réseau et ses sous-réseaux de l'arbre de routage.
    
    Paramètres :
        root (Node) : Racine de l'arbre binaire de routage.
        ip (str) : Adresse IP du réseau à supprimer.
    
    Retourne :
        Node : Nouvelle racine de l'arbre après suppression.
    """
    if root is None:
        return None
    if root.key == ip:
        return None  # Supprime complètement ce sous-arbre
    root.left = delete_route(root.left, ip)
    root.right = delete_route(root.right, ip)
    return root
