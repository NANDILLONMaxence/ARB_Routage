from RouteManager import bfs_mark_unreachable, delete_route
from SearchAlgorithms import find_fastest_search
from CacheManager import save_search_cache, load_search_cache
from BinTree import BinTree

# Construction de l'arbre binaire
root = BinTree("192.168.1.0/24", "RT1",
    left=BinTree("10.0.0.0/8", "RT3",
        left=BinTree("192.168.10.0/24", "RT4",
            left=BinTree("192.168.40.0/24", "RT8"),
            right=BinTree("192.168.50.0/24", "RT9")
        ),
        right=BinTree("192.168.20.0/24", "RT5",
            left=BinTree("172.18.0.0/16", "RT10"),
            right=BinTree("192.168.60.0/24", "RT11")
        )
    ),
    right=BinTree("172.16.0.0/16", "RT2",
        left=BinTree("172.17.0.0/16", "RT6"),
        right=BinTree("192.168.30.0/24", "RT7")
    )
)

# Vérifier si le réseau est dans l'arbre AVANT de le marquer comme inaccessible
def is_network_in_tree(root, ip):
    """Vérifie si un réseau existe dans l'arbre avant suppression."""
    if root is None:
        return False
    if root.key == ip:
        return True
    return is_network_in_tree(root.left, ip) or is_network_in_tree(root.right, ip)

# Demander à l'utilisateur d'entrer le réseau en panne
network_down = input("Entrez le réseau en panne (ex: 192.168.50.0/24) : ").strip()

# Vérifier si le réseau existe AVANT suppression
if is_network_in_tree(root, network_down):
    unreachable_nodes = bfs_mark_unreachable(root, network_down)
    root = delete_route(root, network_down)
    print(f"✅ Le réseau {network_down} et ses descendants ont été supprimés.")
else:
    print(f"⚠️ Attention : Le réseau {network_down} n'existe pas dans la table de routage.")
    unreachable_nodes = set()  # Aucune suppression n'a eu lieu

# Demander à l'utilisateur d'entrer le réseau à rechercher
ip_to_search = input("Entrez le réseau à rechercher (ex: 192.168.30.0/24) : ").strip()

# Vérifier si la route est déjà en cache
cache = load_search_cache()
if ip_to_search in cache:
    print(f"Utilisation du cache pour {ip_to_search}")
    method = cache[ip_to_search]["method"]
    path = cache[ip_to_search]["path"]
    path_from_root = cache[ip_to_search]["path_from_root"]
    print(f"🔍 Méthode utilisée : {method}")
    print(f"📍 Chemin parcouru : {path}")
    print(f"🌳 Chemin depuis la racine : {path_from_root}")
else:
    print(f"🔎 Recherche de {ip_to_search} avec les trois méthodes...")
    method, result, path, path_from_root, failure_reason = find_fastest_search(root, ip_to_search, unreachable_nodes)

    if result:
        print(f"✅ Route trouvée : {result.route_info}")
        print(f"🚀 Méthode la plus rapide : {method}")
        print(f"📍 Chemin parcouru : {path}")
        print(f"🌳 Chemin depuis la racine : {path_from_root}")
        
        # Enregistrer dans le cache
        save_search_cache(ip_to_search, method, path, path_from_root)
    else:
        print(f"❌ Route non trouvée. Raison : {failure_reason}")
