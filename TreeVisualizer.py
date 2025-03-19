def print_tree(root, searched_node=None, prefix="", is_left=True):
    """
    Affiche l'arbre binaire de manière hiérarchique en utilisant des symboles pour représenter la structure de l'arbre.
    - 🔍 Le nœud recherché est affiché en bleu.

    :param root: La racine de l'arbre binaire.
    :param searched_node: L'adresse IP du nœud recherché. Si ce nœud est trouvé, il sera affiché en bleu.
    :param prefix: Le préfixe pour structurer l'affichage (utilisé pour les niveaux de l'arbre).
    :param is_left: Un indicateur pour savoir si le nœud actuel est à gauche dans l'arbre. Cela permet de formater correctement l'affichage.
    """
    
    # Vérifier si le nœud actuel est vide (None), ce qui signifie qu'il n'y a rien à afficher.
    if root is None:
        return

    # 🎨 Définir des couleurs pour l'affichage dans le terminal.
    color_white = "\033[37m"  # Blanc : couleur pour les nœuds non recherchés
    color_blue = "\033[94m"   # Bleu : couleur pour le nœud recherché
    color_reset = "\033[0m"   # Réinitialiser la couleur après chaque nœud

    # Vérifier si le nœud actuel est celui que nous recherchons.
    if searched_node and root.key == searched_node:
        # Si c'est le nœud recherché, on l'affiche en bleu.
        node_label = f"{color_blue}{root.key}{color_reset}"
    else:
        # Sinon, on l'affiche en blanc (couleur par défaut).
        node_label = f"{color_white}{root.key}{color_reset}"

    # Affichage du nœud avec son préfixe (structure de l'arbre).
    # Le préfixe change en fonction de l'emplacement du nœud (gauche ou droite).
    print(prefix + ("├── " if is_left else "└── ") + node_label)

    # Préparer le préfixe pour les sous-arbres (gauche et droite).
    # Cela permet de maintenir la structure visuelle correcte pour l'affichage hiérarchique.
    new_prefix = prefix + ("│   " if is_left else "    ")

    # Affichage récursif des sous-arbres gauche et droit.
    # On applique la fonction de manière récursive pour chaque sous-arbre.
    # La fonction s'appelle elle-même pour les enfants gauche et droit (left et right).
    # `True` pour la gauche (car un sous-arbre gauche commence avec un symbole spécifique),
    # `False` pour la droite (un autre symbole).
    print_tree(root.left, searched_node, new_prefix, True)
    print_tree(root.right, searched_node, new_prefix, False)
