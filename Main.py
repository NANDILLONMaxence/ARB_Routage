from RoutingTable import insert_route, search_route, delete_route


# Création de la table de routage
root = None
root = insert_route(root, "192.168.1.0/24", "RT1")
root = insert_route(root, "10.0.0.0/8", "RT3")
root = insert_route(root, "172.16.0.0/16", "RT4")
root = insert_route(root, "172.18.0.0/16", "RT7")
root = insert_route(root, "192.168.3.0/24", "RT5")
root = insert_route(root, "192.168.2.0/24", "RT2")
root = insert_route(root, "172.17.0.0/16", "RT6")
root = insert_route(root, "192.168.4.0/24", "RT8")

# Recherche d'une route
route = search_route(root, "172.17.0.0/16")
if route:
    print(f"Route trouvée: {route.route_info}")
else:
    print("Route non trouvée")

# Suppression d'une route
root = delete_route(root, "192.168.3.0/24")

# Vérification de suppression
route = search_route(root, "192.168.3.0/24")
if route:
    print(f"Route trouvée: {route.route_info}")
else:
    print("Route non trouvée")
