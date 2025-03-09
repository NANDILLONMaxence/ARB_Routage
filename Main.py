from RoutingTable import find_fastest_search, save_search_cache, load_search_cache, delete_route, bfs_mark_unreachable
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

# Spécifier un réseau en panne
network_down = "192.168.50.0/24"  # Réseau en panne
unreachable_nodes = bfs_mark_unreachable(root, network_down)

# Supprimer le réseau en panne et ses enfants
root = delete_route(root, network_down)


# Recherche d'une route
ip_to_search = "192.168.30.0/24"  # Réseau recherché par l'utilisateur

# Vérifier si la route est déjà dans le cache
cache = load_search_cache()
if ip_to_search in cache:
    print(f"Utilisation du cache pour {ip_to_search}")
    method = cache[ip_to_search]["method"]
    path = cache[ip_to_search]["path"]
    path_from_root = cache[ip_to_search]["path_from_root"]
    print(f"Méthode utilisée : {method}")
    print(f"Chemin parcouru : {path}")
    print(f"Chemin depuis la racine : {path_from_root}")
else:
    print(f"Recherche de {ip_to_search} avec les trois méthodes...")
    method, result, path, path_from_root = find_fastest_search(root, ip_to_search)  # Déballer quatre valeurs
    
    if result:
        print(f"Route trouvée : {result.route_info}")
        print(f"Méthode la plus rapide : {method}")
        print(f"Chemin parcouru : {path}")
        print(f"Chemin depuis la racine : {path_from_root}")
        
        # Enregistrer dans le cache
        save_search_cache(ip_to_search, method, path, path_from_root)
    else:
        print("Route non trouvée.")