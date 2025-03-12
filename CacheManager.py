def save_search_cache(ip, method, path, path_from_root):
    cache = load_search_cache()
    cache[ip] = {
        "method": method,
        "path": path,
        "path_from_root": path_from_root
    }

    with open("search_cache.txt", "w") as file:
        for ip_key, data in cache.items():
            file.write(f"{ip_key}:{data['method']}:{','.join(data['path'])}:{','.join(data['path_from_root'])}\n")

def load_search_cache():
    cache = {}
    try:
        with open("search_cache.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(":")
                if len(parts) == 4:
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
