# Version: 1.0
# Subject: Programme principal pour la découverte réseaux et la simulation de routage de paquets.
# Created by: NANDILLON Maxence

from RouteManager import bfs_mark_unreachable, delete_route
from SearchAlgorithms import find_fastest_search, get_path_from_root, bfs_search
from CacheManager import save_search_cache, load_search_cache
from TreeVisualizer import print_tree
from TreeBuilder import build_tree
from PacketSender import send_packet

def is_network_in_tree(root, ip):
    """Vérifie si un réseau existe dans l'arbre avant suppression.
    
    :param root: Racine de l'arbre de routage.
    :param ip: Adresse IP du réseau à vérifier.
    :return: True si le réseau est présent, False sinon.
    """
    if root is None:
        return False
    if root.key == ip:
        return True
    return is_network_in_tree(root.left, ip) or is_network_in_tree(root.right, ip)

def handle_network_down(root):
    """Gère la suppression d'un réseau injoignable.
    
    :param root: Racine de l'arbre de routage.
    :return: L'arbre de routage mis à jour et la liste des nœuds inaccessibles.
    """
    network_down = input("Entrez le réseau en panne (ex: 192.168.50.0/24) : ").strip()
    if is_network_in_tree(root, network_down):
        unreachable_nodes = bfs_mark_unreachable(root, network_down)
        root = delete_route(root, network_down)
        print(f"\n✅ Le réseau {network_down} et ses descendants ont été supprimés.")
    else:
        print(f"\n⚠️ Attention : Le réseau {network_down} n'existe pas dans la table de routage.")
        unreachable_nodes = set()
    return root, unreachable_nodes

def search_route(root, unreachable_nodes):
    """Recherche une route dans l'arbre.

    :param root: Racine de l'arbre de routage.
    :param unreachable_nodes: Liste des nœuds inaccessibles.
    :return: La méthode de recherche la plus rapide, le nœud trouvé, le chemin parcouru, le chemin optimal depuis la racine, et un message d'erreur.
    """
    ip_to_search = input("Entrez le réseau à rechercher (ex: 192.168.30.0/24) : ").strip()
    cache = load_search_cache()

    if ip_to_search in cache:
        print(f"Utilisation du cache pour {ip_to_search}")
        method = cache[ip_to_search]["method"]
        path = cache[ip_to_search]["path"]
        path_from_root = cache[ip_to_search]["path_from_root"]
    else:
        print(f"\n🔎 Recherche de {ip_to_search} avec les trois méthodes...")
        method, result, path, path_from_root, failure_reason = find_fastest_search(root, ip_to_search, unreachable_nodes)
        if result:
            save_search_cache(ip_to_search, method, path, path_from_root)
        else:
            print(f"\n❌ Route non trouvée. Raison : {failure_reason}")
            return None  # Retourner None si la route n'est pas trouvée

    print(f"\n✅ Route trouvée via {method}")
    print(f"\n📍 Chemin parcouru : {path}")
    print(f"\n🌳 Chemin depuis la racine : {path_from_root}")

    return ip_to_search  # Retourner l'adresse IP recherchée

def handle_packet_sending(root):
    """Gère l'envoi d'un paquet si demandé.
    :param root: Racine de l'arbre de routage.
    """
    send_packet_option = input("\nVoulez-vous envoyer un paquet ? (oui/non) : ").strip().lower()
    if send_packet_option == "oui" or send_packet_option == "yes" or send_packet_option == "o" or send_packet_option == "y":
        ip_to_send = input("Entrez l'adresse du réseau à joindre : ").strip()
        cache = load_search_cache()

        if ip_to_send in cache:
            path_from_root = cache[ip_to_send]["path_from_root"]
            send_packet(ip_to_send, path_from_root)
        else:
            print(f"\n🔎 Recherche de {ip_to_send} avec la méthode BFS...")
            result, path, optimal_path = bfs_search(root, ip_to_send)
            if result:
                path_from_root = get_path_from_root(root, ip_to_send)
                send_packet(ip_to_send, path_from_root)
                save_search_cache(ip_to_send, "bfs", path, path_from_root)
            else:
                print(f"\n❌ Route non trouvée pour {ip_to_send}.")

def main():
    """Fonction principale qui orchestre le programme."""
    root = build_tree()

    print("\n🌳 Aperçu de l'arbre du réseau initial :\n")
    print_tree(root)

    root, unreachable_nodes = handle_network_down(root)
    # Appeler search_route pour obtenir l'adresse IP recherchée
    ip_to_search = search_route(root, unreachable_nodes)

    # Afficher l'arbre après suppression avec le nœud recherché en bleu
    print("\n🌳 Aperçu de l'arbre de routage après suppression :\n")
    if ip_to_search:  # Vérifier si une adresse IP a été recherchée
        print_tree(root, ip_to_search)  # Afficher l'arbre avec le nœud recherché en bleu
    else:
        print_tree(root)  # Afficher l'arbre normalement si aucune recherche n'a été effectuée

    handle_packet_sending(root)

if __name__ == "__main__":
    main()