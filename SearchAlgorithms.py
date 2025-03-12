from BinTree import BinTree

def search_prefix(root, ip, path=None, optimal_path=None):
    if path is None:
        path = []
    if optimal_path is None:
        optimal_path = []
    
    if root is None:
        return None, path, optimal_path

    path.append(root.key)

    if root.key == ip:
        optimal_path.extend(path)
        return root, path, optimal_path

    left_result, _, left_optimal = search_prefix(root.left, ip, path, optimal_path)
    if left_result:
        return left_result, path, left_optimal

    right_result, _, right_optimal = search_prefix(root.right, ip, path, optimal_path)
    if right_result:
        return right_result, path, right_optimal

    return None, path, optimal_path

def search_infix(root, ip, path=None, optimal_path=None):
    if path is None:
        path = []
    if optimal_path is None:
        optimal_path = []

    if root is None:
        return None, path, optimal_path

    left_result, _, left_optimal = search_infix(root.left, ip, path, optimal_path)
    if left_result:
        return left_result, path, left_optimal

    path.append(root.key)

    if root.key == ip:
        optimal_path.extend(path)
        return root, path, optimal_path

    right_result, _, right_optimal = search_infix(root.right, ip, path, optimal_path)
    if right_result:
        return right_result, path, right_optimal

    return None, path, optimal_path

def search_suffix(root, ip, path=None, optimal_path=None):
    if path is None:
        path = []
    if optimal_path is None:
        optimal_path = []

    if root is None:
        return None, path, optimal_path

    left_result, _, left_optimal = search_suffix(root.left, ip, path, optimal_path)
    if left_result:
        return left_result, path, left_optimal

    right_result, _, right_optimal = search_suffix(root.right, ip, path, optimal_path)
    if right_result:
        return right_result, path, right_optimal

    path.append(root.key)

    if root.key == ip:
        optimal_path.extend(path)
        return root, path, optimal_path

    return None, path, optimal_path

def find_fastest_search(root, ip, unreachable_nodes=None):
    from time import time

    if root is None:
        return None, None, [], [], "L'arbre de routage est vide."

    if unreachable_nodes is None:
        unreachable_nodes = set()

    methods = {
        "prefix": search_prefix,
        "infix": search_infix,
        "suffix": search_suffix,
    }

    fastest_method = None
    fastest_time = float('inf')
    fastest_result = None
    fastest_path = []
    fastest_optimal_path = []

    for method_name, method in methods.items():
        start_time = time()
        result, path, optimal_path = method(root, ip)
        elapsed_time = time() - start_time

        if result and elapsed_time < fastest_time:
            fastest_method = method_name
            fastest_time = elapsed_time
            fastest_result = result
            fastest_path = path
            fastest_optimal_path = optimal_path

    if fastest_result:
        path_from_root = get_path_from_root(root, ip)
        return fastest_method, fastest_result, fastest_path, path_from_root, None

    if ip in unreachable_nodes:
        return None, None, [], [], f"La route {ip} était présente mais a été supprimée ou est devenue inaccessible."

    return None, None, [], [], f"La route {ip} n'existe pas dans la table de routage."

def get_path_from_root(root, ip):
    def dfs(node, target_ip, path):
        if node is None:
            return None
        path.append(node.key)
        if node.key == target_ip:
            return path
        left_path = dfs(node.left, target_ip, path.copy())
        if left_path is not None:
            return left_path
        right_path = dfs(node.right, target_ip, path.copy())
        if right_path is not None:
            return right_path
        return None

    return dfs(root, ip, []) or []
