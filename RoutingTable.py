from BinTree import BinTree

def bfs_mark_unreachable(root, ip):
    """
    Marque le nœud spécifié et tous ses descendants comme non accessibles en utilisant un parcours en largeur (BFS).

    :param root: Racine de l'arbre.
    :param ip: Adresse IP du réseau en panne.
    :return: Un ensemble contenant les nœuds non accessibles.
    """
    unreachable = set()
    
    # File pour le parcours BFS
    queue = [root]
    
    while queue:
        current = queue.pop(0)  # Défilement (FIFO)
        
        if current.key == ip:
            # Ajouter tous les descendants du nœud en panne à l'ensemble
            queue.append(current)  # Ajouter lui-même pour traitement
            break  # On a trouvé le nœud en panne
    
    while queue:
        node = queue.pop(0)  # Retirer un nœud
        
        # Marquer le nœud comme inaccessible
        unreachable.add(node.key)

        # Ajouter ses enfants à la file pour marquer tous les descendants
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return unreachable

def search_prefix(root, ip, path=None, optimal_path=None):
    """Recherche en préfixe (pré-ordre)."""
    if path is None:
        path = []
    if optimal_path is None:
        optimal_path = []
    
    if root is None:
        return None, path, optimal_path

    # Ajouter le nœud actuel au chemin parcouru
    path.append(root.key)

    if root.key == ip:
        # Copier le chemin optimal
        optimal_path.extend(path)
        return root, path, optimal_path

    # Recherche dans le sous-arbre gauche
    left_result, _, left_optimal = search_prefix(root.left, ip, path, optimal_path)
    if left_result:
        return left_result, path, left_optimal

    # Recherche dans le sous-arbre droit
    right_result, _, right_optimal = search_prefix(root.right, ip, path, optimal_path)
    if right_result:
        return right_result, path, right_optimal

    return None, path, optimal_path

def search_infix(root, ip, path=None, optimal_path=None):
    """Recherche en infixe (in-ordre)."""
    if path is None:
        path = []
    if optimal_path is None:
        optimal_path = []

    if root is None:
        return None, path, optimal_path

    # Recherche dans le sous-arbre gauche
    left_result, _, left_optimal = search_infix(root.left, ip, path, optimal_path)
    if left_result:
        return left_result, path, left_optimal

    # Ajouter le nœud actuel au chemin parcouru
    path.append(root.key)

    if root.key == ip:
        optimal_path.extend(path)
        return root, path, optimal_path

    # Recherche dans le sous-arbre droit
    right_result, _, right_optimal = search_infix(root.right, ip, path, optimal_path)
    if right_result:
        return right_result, path, right_optimal

    return None, path, optimal_path

def search_suffix(root, ip, path=None, optimal_path=None):
    """Recherche en suffixe (post-ordre)."""
    if path is None:
        path = []
    if optimal_path is None:
        optimal_path = []

    if root is None:
        return None, path, optimal_path

    # Recherche dans le sous-arbre gauche
    left_result, _, left_optimal = search_suffix(root.left, ip, path, optimal_path)
    if left_result:
        return left_result, path, left_optimal

    # Recherche dans le sous-arbre droit
    right_result, _, right_optimal = search_suffix(root.right, ip, path, optimal_path)
    if right_result:
        return right_result, path, right_optimal

    # Ajouter le nœud actuel au chemin parcouru
    path.append(root.key)

    if root.key == ip:
        optimal_path.extend(path)
        return root, path, optimal_path

    return None, path, optimal_path


def find_fastest_search(root, ip):
    """
    Compare les trois méthodes de recherche et retourne la plus rapide.
    Si plusieurs méthodes ont le même temps d'exécution, choisit celle qui a parcouru le moins de nœuds.

    :param root: Racine de l'arbre.
    :param ip: Adresse IP à rechercher.
    :return: La méthode la plus rapide, le nœud trouvé, le chemin parcouru, et le chemin optimal.
    """
    methods = {
        "prefix": search_prefix,
        "infix": search_infix,
        "suffix": search_suffix,
    }
    
    fastest_method = None
    fastest_time = float('inf')  # Initialiser avec une valeur infinie
    fastest_result = None
    fastest_path = None
    fastest_optimal_path = None
    min_nodes_visited = float('inf')  # Initialiser avec une valeur infinie
    
    print("Comparaison des méthodes de recherche :")
    
    for method_name, method in methods.items():
        start_time = get_current_time()  # Début du chronomètre
        result, path, optimal_path = method(root, ip)
        elapsed_time = get_current_time() - start_time  # Temps écoulé
        
        # Nombre de nœuds parcourus
        nodes_visited = len(path)
        
        # Afficher le temps d'exécution et le nombre de nœuds parcourus
        print(f"Méthode {method_name} : {elapsed_time:.6f} secondes, {nodes_visited} nœuds parcourus")
        
        # Comparer d'abord le temps d'exécution, puis le nombre de nœuds parcourus
        if result and (elapsed_time < fastest_time or (elapsed_time == fastest_time and nodes_visited < min_nodes_visited)):
            fastest_method = method_name
            fastest_time = elapsed_time
            fastest_result = result
            fastest_path = path
            fastest_optimal_path = optimal_path
            min_nodes_visited = nodes_visited
    
    # Calculer le chemin depuis la racine après avoir trouvé le nœud
    if fastest_result:
        path_from_root = get_path_from_root(root, ip)
    else:
        path_from_root = []
    
    # Retourner uniquement quatre valeurs
    return fastest_method, fastest_result, fastest_path, path_from_root

def get_current_time():
    """
    Simule une fonction pour obtenir le temps actuel (en secondes).
    """
    # Cette fonction est une simulation, car nous ne pouvons pas utiliser `time.time()`.
    # Pour simplifier, nous utilisons un compteur manuel.
    if not hasattr(get_current_time, "counter"):
        get_current_time.counter = 0  # Initialiser le compteur à 0
    get_current_time.counter += 1  # Incrémenter le compteur à chaque appel
    return get_current_time.counter

def get_path_from_root(root, ip):
    """
    Retourne le chemin depuis la racine jusqu'au nœud recherché.

    :param root: Racine de l'arbre.
    :param ip: Adresse IP du nœud recherché.
    :return: Une liste contenant les clés des nœuds traversés (chemin depuis la racine).
    """
    def dfs(node, target_ip, path):
        if node is None:
            return None
        
        # Ajouter le nœud actuel au chemin
        path.append(node.key)
        
        # Si le nœud actuel correspond à l'IP recherchée
        if node.key == target_ip:
            return path
        
        # Rechercher dans le sous-arbre gauche
        left_path = dfs(node.left, target_ip, path.copy())
        if left_path is not None:
            return left_path
        
        # Rechercher dans le sous-arbre droit
        right_path = dfs(node.right, target_ip, path.copy())
        if right_path is not None:
            return right_path
        
        # Si le nœud n'est pas trouvé, retirer le nœud actuel du chemin
        path.pop()
        return None
    
    # Appeler la fonction DFS récursive
    result = dfs(root, ip, [])
    return result if result is not None else []

def save_search_cache(ip, method, path, path_from_root):
    """
    Sauvegarde la méthode de recherche la plus rapide et le chemin depuis la racine dans un fichier de cache.

    :param ip: Adresse IP recherchée.
    :param method: Méthode de recherche la plus rapide.
    :param path: Chemin parcouru par la méthode de recherche.
    :param path_from_root: Chemin depuis la racine jusqu'au nœud recherché.
    """
    cache = load_search_cache()  # Charge le cache existant
    cache[ip] = {
        "method": method,
        "path": path,
        "path_from_root": path_from_root  # Ajout du chemin depuis la racine
    }
    
    with open("search_cache.txt", "w") as file:
        for ip_key, data in cache.items():
            file.write(f"{ip_key}:{data['method']}:{','.join(data['path'])}:{','.join(data['path_from_root'])}\n")

def load_search_cache():
    """
    Charge la méthode de recherche la plus rapide et le chemin depuis la racine depuis le fichier de cache.

    :return: Un dictionnaire contenant le cache.
    """
    cache = {}
    try:
        with open("search_cache.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:  # Ignore les lignes vides
                    continue
                parts = line.split(":")
                if len(parts) == 4:  # Vérifie que la ligne a bien 4 parties
                    ip, method, path, path_from_root = parts
                    cache[ip] = {
                        "method": method,
                        "path": path.split(","),
                        "path_from_root": path_from_root.split(",")
                    }
                else:
                    print(f"Ligne mal formatée dans le cache : {line}")
    except FileNotFoundError:
        print("Fichier de cache non trouvé, création d'un nouveau cache.")
    return cache


def delete_route(root, ip):
    """
    Supprime un nœud et tous ses descendants dans l'arbre binaire.

    :param root: Racine de l'arbre.
    :param ip: Adresse IP du réseau à supprimer.
    :return: Nouvelle racine de l'arbre mise à jour.
    """
    if root is None:
        return None

    if root.key == ip:
        return None  # Supprime complètement le sous-arbre du nœud en panne
    
    # Parcours récursif
    root.left = delete_route(root.left, ip)
    root.right = delete_route(root.right, ip)

    return root


def min_value_node(node):
    """
    Trouver le noeud avec la valeur minimale.

    :param node: Noeud à partir duquel commencer la recherche.
    :return: Noeud avec la valeur minimale.
    """
    current = node
    while current.left is not None:
        current = current.left
    return current
