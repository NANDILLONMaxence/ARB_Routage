# Version: 1.0
# Subject: Fonction d'envoi de paquet
# Created by: NANDILLON Maxence

def send_packet( ip, path_from_root):
    """
    Simule l'envoi d'un paquet en utilisant un chemin prédéfini et une latence aléatoire dans un range de 1 à 29 ms.
    La latence est choisie de manière "aléatoire" à chaque saut sans utiliser de librairie externe.
    
    :param ip: Adresse IP de destination.
    :param path_from_root: Chemin depuis la racine jusqu'à la destination.
    """
    if not path_from_root:
        print(f"❌ Aucun chemin trouvé pour {ip}.")
        return

    print(f"\n📦 Envoi du paquet vers {ip}...")
    total_latency = 0

    # Parcourir chaque saut dans le chemin de la racine à la destination
    for i in range(len(path_from_root) - 1):
        current_node = path_from_root[i]
        next_node = path_from_root[i + 1]
        
        # Choisir une latence aléatoire dans le range de 1 à 29
        latency = (hash(f"{current_node}{next_node}{i}") % 29) + 1  # hash pour générer une valeur "aléatoire"
        
        total_latency += latency
        print(f"  🚚 Paquet en transit de {current_node} à {next_node} (latence: {latency} ms)")

    print(f"✅ Paquet arrivé à destination {ip} en {total_latency} ms.")