from BinTree import BinTree
from Queue import Queue
from SearchAlgorithms import find_fastest_search
from CacheManager import save_search_cache, load_search_cache

def bfs_mark_unreachable(root, ip):
    """
    Marque un réseau et tous ses sous-réseaux comme inaccessibles en utilisant un parcours BFS.
    """
    unreachable = set()
    queue = Queue()
    queue.enqueue(root)

    while not queue.is_empty():
        current = queue.dequeue()
        if current.key == ip:
            queue.enqueue(current)  # Ajouter pour marquer ses descendants
            break  # On a trouvé le nœud en panne

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
    """
    if root is None:
        return None
    if root.key == ip:
        return None  # Supprime complètement ce sous-arbre
    root.left = delete_route(root.left, ip)
    root.right = delete_route(root.right, ip)
    return root
