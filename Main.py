# Description: Programme principal pour la découverte reseaux et la simulation de routage de paquets.
from RouteManager import bfs_mark_unreachable, delete_route
from SearchAlgorithms import find_fastest_search, get_path_from_root, bfs_search
from CacheManager import save_search_cache, load_search_cache
from TreeVisualizer import print_tree
from TreeBuilder import build_tree
from PacketSender import send_packet

# Construction de l'arbre binaire
root = build_tree()

# Vérifier si le réseau est dans l'arbre AVANT de le marquer comme inaccessible
def is_network_in_tree(root, ip):
    """
    Vérifie si un réseau existe dans l'arbre avant suppression.
    
    Paramètres :
        root (Node) : Racine de l'arbre binaire.
        ip (str) : Adresse IP du réseau.
    
    Retourne :
        bool : True si le réseau est présent, sinon False.
    """
    if root is None:
        return False
    if root.key == ip:
        return True
    return is_network_in_tree(root.left, ip) or is_network_in_tree(root.right, ip)

# Afficher l'arbre initial
print("\n🌳 Aperçu de l'arbre du réseau initial :\n")
print_tree(root)

# Demander à l'utilisateur d'entrer le réseau en panne
network_down = input("Entrez le réseau en panne (ex: 192.168.50.0/24) : ").strip()

# Vérifier si le réseau existe AVANT suppression
if is_network_in_tree(root, network_down):
    unreachable_nodes = bfs_mark_unreachable(root, network_down)
    root = delete_route(root, network_down)
    print(f"✅ Le réseau {network_down} et ses descendants ont été supprimés.")
else:
    print(f"⚠️ Attention : Le réseau {network_down} n'existe pas dans la table de routage.")
    unreachable_nodes = set()

# Rechercher la route après la suppression
ip_to_search = input("Entrez le réseau à rechercher (ex: 192.168.30.0/24) : ").strip()

# Afficher l'arbre après suppression avec le nœud recherché en bleu
print("\n🌳 Aperçu de l'arbre de routage après suppression :\n")
print_tree(root, ip_to_search)

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

# Demander à l'utilisateur s'il souhaite envoyer un paquet
send_packet_option = input("\nVoulez-vous envoyer un paquet ? (oui/non) : ").strip().lower()

if send_packet_option == "oui":
    ip_to_send = input("Entrez l'adresse du réseau à joindre : ").strip()
    cache = load_search_cache()

    if ip_to_send in cache:
        print(f"Utilisation du cache pour {ip_to_send}")
        path_from_root = cache[ip_to_send]["path_from_root"]
        send_packet(ip_to_send, path_from_root)
    else:
        print(f"🔎 Recherche de {ip_to_send} avec la méthode BFS...")
        result, path, optimal_path = bfs_search(root, ip_to_send)  # Utiliser BFS ici
        if result:
            path_from_root = get_path_from_root(root, ip_to_send)
            send_packet(ip_to_send, path_from_root)
            # Enregistrer dans le cache
            save_search_cache(ip_to_send, "bfs", path, path_from_root)  # Méthode BFS
        else:
            print(f"❌ Route non trouvée pour {ip_to_send}.")
