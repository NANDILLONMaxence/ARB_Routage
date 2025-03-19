# Importation de la bibliothèque Queue pour utiliser une file d'attente
from Queue import Queue

# Fonction de recherche de type "prefix" (on explore d'abord la gauche, puis la droite)
def search_prefix(root, ip, path=None, optimal_path=None):
    # Initialiser les chemins si aucun n'est passé en argument
    if path is None:
        path = []
    if optimal_path is None:
        optimal_path = []
    
    # Si l'arbre est vide, on retourne rien
    if root is None:
        return None, path, optimal_path

    # Ajouter le nœud actuel au chemin
    path.append(root.key)

    # Si le nœud actuel contient l'IP recherchée, on retourne ce nœud et son chemin
    if root.key == ip:
        optimal_path.extend(path)
        return root, path, optimal_path

    # Recherche à gauche dans l'arbre
    left_result, _, left_optimal = search_prefix(root.left, ip, path, optimal_path)
    if left_result:
        return left_result, path, left_optimal

    # Recherche à droite dans l'arbre
    right_result, _, right_optimal = search_prefix(root.right, ip, path, optimal_path)
    if right_result:
        return right_result, path, right_optimal

    # Si l'IP n'a pas été trouvée, on retourne les chemins parcourus
    return None, path, optimal_path

# Fonction de recherche de type "infix" (on explore gauche, puis le nœud, puis droite)
def search_infix(root, ip, path=None, optimal_path=None):
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

    # Ajouter le nœud actuel au chemin
    path.append(root.key)

    # Si le nœud contient l'IP recherchée, on retourne ce nœud et son chemin
    if root.key == ip:
        optimal_path.extend(path)
        return root, path, optimal_path

    # Recherche dans le sous-arbre droit
    right_result, _, right_optimal = search_infix(root.right, ip, path, optimal_path)
    if right_result:
        return right_result, path, right_optimal

    return None, path, optimal_path

# Fonction de recherche de type "suffix" (on explore gauche, puis droite, puis le nœud)
def search_suffix(root, ip, path=None, optimal_path=None):
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

    # Ajouter le nœud actuel au chemin
    path.append(root.key)

    # Si le nœud contient l'IP recherchée, on retourne ce nœud et son chemin
    if root.key == ip:
        optimal_path.extend(path)
        return root, path, optimal_path

    return None, path, optimal_path

# Fonction de recherche en largeur (BFS) pour trouver un nœud
def bfs_search(root, ip):
    """
    Recherche un nœud dans l'arbre en utilisant un parcours en largeur (BFS).
    
    :param root: Racine de l'arbre.
    :param ip: Adresse IP à rechercher.
    :return: Le nœud trouvé, le chemin parcouru, et le chemin optimal depuis la racine.
    """
    if root is None:
        return None, [], []  # Si l'arbre est vide, on retourne une réponse vide

    # On utilise une file d'attente pour gérer les nœuds à explorer
    queue = Queue()
    queue.enqueue((root, [root.key]))  # Ajouter la racine avec son chemin (seulement la racine)

    while not queue.is_empty():
        current_node, path = queue.dequeue()  # Récupérer un nœud et son chemin

        # Si on trouve l'IP dans ce nœud, on retourne ce nœud et le chemin
        if current_node.key == ip:
            return current_node, path, path

        # Ajouter les nœuds enfants à la file d'attente
        if current_node.left:
            queue.enqueue((current_node.left, path + [current_node.left.key]))
        if current_node.right:
            queue.enqueue((current_node.right, path + [current_node.right.key]))

    return None, [], []  # Si l'IP n'est pas trouvée dans l'arbre, on retourne rien

# Fonction pour trouver la méthode de recherche la plus rapide
def find_fastest_search(root, ip, unreachable_nodes=None):
    if root is None:
        return None, None, [], [], "L'arbre de routage est vide."

    if unreachable_nodes is None:
        unreachable_nodes = set()

    # Vérifier si l'IP est dans les nœuds inaccessibles
    if ip in unreachable_nodes:
        return None, None, [], [], f"La route {ip} était présente mais est inaccessible."

    # Liste des méthodes de recherche disponibles
    methods = {
        "prefix": search_prefix,
        "infix": search_infix,
        "suffix": search_suffix,
    }

    fastest_method = None
    fastest_result = None
    fastest_path = []
    fastest_optimal_path = []

    print("Comparaison des méthodes de recherche :")

    # Tester chaque méthode pour trouver la plus rapide
    for method_name, method in methods.items():
        result, path, optimal_path = method(root, ip)

        # Afficher le nombre de nœuds parcourus par chaque méthode
        print(f"Méthode {method_name} : {len(path)} nœuds parcourus")

        # Si une méthode trouve l'IP et qu'elle est plus rapide, on la garde
        if result and (fastest_result is None or len(path) < len(fastest_path)):
            fastest_method = method_name
            fastest_result = result
            fastest_path = path
            fastest_optimal_path = optimal_path

    # Si une méthode a trouvé l'IP, retourner la méthode la plus rapide
    if fastest_result:
        path_from_root = get_path_from_root(root, ip)
        return fastest_method, fastest_result, fastest_path, path_from_root, None

    return None, None, [], [], f"La route {ip} n'existe pas dans la table de routage."

# Fonction pour obtenir le chemin de la racine à un nœud spécifique
def get_path_from_root(root, ip):
    def dfs(node, target_ip, path):
        if node is None:
            return None
        path.append(node.key)  # Ajouter le nœud actuel au chemin
        if node.key == target_ip:
            return path  # Si l'IP est trouvée, on retourne le chemin
        # Recherche dans le sous-arbre gauche
        left_path = dfs(node.left, target_ip, path.copy())
        if left_path is not None:
            return left_path
        # Recherche dans le sous-arbre droit
        right_path = dfs(node.right, target_ip, path.copy())
        if right_path is not None:
            return right_path
        return None

    return dfs(root, ip, []) or []  # Si l'IP n'est pas trouvée, on retourne un chemin vide
