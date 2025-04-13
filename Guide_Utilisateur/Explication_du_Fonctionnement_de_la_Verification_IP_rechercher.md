### Explication du Fonctionnement de la Vérification d'IP dans le Programme

Le programme vérifie si une IP recherchée existe dans l'arbre de routage **avant** de marquer des nœuds comme inaccessibles (`unreachable_nodes`). Voici comment cela fonctionne étape par étape :

---

#### 1. **Initialisation de `unreachable_nodes`**
- Par défaut, `unreachable_nodes` est initialisé comme un ensemble vide (`set()`).  
- Il ne contient aucune IP au démarrage du programme.

---

#### 2. **Vérification de l'existence de l'IP**
La fonction `is_network_in_tree(root, ip)` est utilisée pour vérifier si l'IP recherchée existe dans l'arbre **avant toute suppression** :
```python
def is_network_in_tree(root, ip):
    """Vérifie si un réseau existe dans l'arbre avant suppression."""
    if root is None:
        return False
    if root.key == ip:
        return True
    return is_network_in_tree(root.left, ip) or is_network_in_tree(root.right, ip)
```
- Cette fonction parcourt récursivement l'arbre pour chercher l'IP.
- Si l'IP est trouvée, elle retourne `True` ; sinon, `False`.

---

#### 3. **Gestion des Routes Inaccessibles**
Si l'IP existe dans l'arbre :
- Le programme appelle `bfs_mark_unreachable(root, ip)` pour marquer l'IP et ses descendants comme inaccessibles.
- Ces IPs sont ajoutées à `unreachable_nodes`.
- Ensuite, `delete_route(root, ip)` supprime physiquement le sous-arbre correspondant.

```python
if is_network_in_tree(root, network_down):
    unreachable_nodes = bfs_mark_unreachable(root, network_down)  # Remplit unreachable_nodes
    root = delete_route(root, network_down)  # Supprime le sous-arbre
```

---

#### 4. **Recherche d'une IP**
Lors de la recherche (`find_fastest_search`), le programme :
1. Vérifie d'abord si l'IP est dans le cache.
2. Si elle n'est pas en cache, il utilise trois méthodes de parcours (préfixe, infixe, suffixe).
3. **Contrôle dans `unreachable_nodes`** :
   - Si l'IP est dans `unreachable_nodes`, cela signifie qu'elle a été supprimée et est inaccessible.
   - Sinon, il vérifie si elle existe dans l'arbre actuel.

```python
if ip in unreachable_nodes:
    return None, None, [], [], f"La route {ip} était présente mais a été supprimée."
```

---

### Exemple Concret
1. **Arbre initial** :
   ```
   RT1 (192.168.1.0/24)
   ├── RT3 (10.0.0.0/8)
   └── RT2 (172.16.0.0/16)
   ```

2. **Suppression de `10.0.0.0/8`** :
   - `is_network_in_tree(root, "10.0.0.0/8")` retourne `True`.
   - `unreachable_nodes` est rempli avec `{"10.0.0.0/8", ...}` (ses descendants).
   - Le sous-arbre est supprimé.

3. **Recherche de `10.0.0.0/8`** :
   - Le programme voit que `"10.0.0.0/8"` est dans `unreachable_nodes`.
   - Il renvoie : *"La route 10.0.0.0/8 était présente mais a été supprimée."*

---

### Pourquoi `unreachable_nodes` est vide au début ?
- Au démarrage, aucune route n'a encore été supprimée, donc `unreachable_nodes` est vide.
- Il se remplit **uniquement** lorsqu'une route est marquée comme inaccessible via `bfs_mark_unreachable()`.

---

### Résumé
- **Première vérification** : `is_network_in_tree()` garantit que l'IP existe avant suppression.
- **Deuxième vérification** : `unreachable_nodes` sert à éviter de rechercher des routes déjà supprimées.
- **Cache** : Optimise les recherches répétées pour les IPs valides.

Cette approche assure que le programme ne tente pas de supprimer ou de rechercher des routes inexistantes.