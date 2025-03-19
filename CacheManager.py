
def save_search_cache(ip, method, path, path_from_root):
    """
    Sauvegarde les informations de recherche dans un fichier cache.
    
    Paramètres :
        ip (str) : Adresse IP de l'utilisateur.
        method (str) : Méthode HTTP utilisée (GET, POST, etc.).
        path (list) : Liste des chemins liés à la recherche.
        path_from_root (list) : Liste des chemins relatifs à la racine.
    """
    # Charger les données existantes du cache
    cache = load_search_cache()
    
    # Mettre à jour le cache avec la nouvelle entrée
    cache[ip] = {
        "method": method,
        "path": path,
        "path_from_root": path_from_root
    }
    
    # Écrire le cache mis à jour dans le fichier
    with open("search_cache.txt", "w") as file:
        for ip_key, data in cache.items():
            file.write(f"{ip_key}:{data['method']}:{','.join(data['path'])}:{','.join(data['path_from_root'])}\n")

def load_search_cache():
    """
    Charge les données de recherche à partir du fichier cache.
    
    Retourne :
        dict : Un dictionnaire contenant les informations du cache.
    """
    cache = {}
    try:
        # Ouvrir le fichier cache en mode lecture
        with open("search_cache.txt", "r") as file:
            for line in file:
                line = line.strip()  # Supprimer les espaces ou retours à la ligne
                if not line:
                    continue  # Ignorer les lignes vides
                
                parts = line.split(":")  # Séparer les éléments de la ligne
                
                if len(parts) == 4:
                    ip, method, path, path_from_root = parts
                    cache[ip] = {
                        "method": method,
                        "path": path.split(","),  # Transformer la chaîne en liste
                        "path_from_root": path_from_root.split(",")
                    }
                else:
                    print(f"Ligne mal formatée dans le cache : {line}")
    except FileNotFoundError:
        print("Fichier de cache non trouvé, création d'un nouveau cache.")
    
    return cache
