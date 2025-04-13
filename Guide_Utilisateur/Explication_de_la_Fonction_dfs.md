### Explication de la Fonction `dfs` dans le Script

La fonction `dfs` (Depth-First Search, ou "parcours en profondeur") est utilisée dans le script pour **retrouver le chemin depuis la racine de l'arbre jusqu'à une adresse IP cible**. Elle est définie dans le fichier `SearchAlgorithms.py` et appelée par `get_path_from_root(root, ip)`.

---

#### **Signature de la Fonction**
```python
def dfs(node, target_ip, path):
    """
    Parcours en profondeur (DFS) pour trouver le chemin depuis la racine jusqu'à target_ip.
    
    :param node: Nœud actuel de l'arbre.
    :param target_ip: Adresse IP à rechercher.
    :param path: Liste accumulant le chemin parcouru.
    :return: Chemin complet (liste) si target_ip est trouvée, sinon None.
    """
```

---

#### **Fonctionnement Pas à Pas**
1. **Cas de base** :  
   - Si `node` est `None` (nœud vide), la fonction retourne `None`.  
   - Cela arrête la récursion sur une branche sans issue.

2. **Ajout du nœud actuel au chemin** :  
   - Le nœud courant (`node.key`) est ajouté à la liste `path`.  
   - Exemple :  
     ```python
     path = ["192.168.1.0/24"]  # Après avoir visité la racine.
     ```

3. **Vérification de la cible** :  
   - Si `node.key == target_ip`, on a trouvé la cible.  
   - La fonction retourne le `path` actuel, qui contient le chemin complet depuis la racine.  
     ```python
     if node.key == target_ip:
         return path  # Ex: ["192.168.1.0/24", "172.16.0.0/16", "192.168.30.0/24"]
     ```

4. **Appels récursifs** :  
   - La fonction explore d'abord le sous-arbre gauche (`node.left`), puis le droit (`node.right`).  
   - Une **copie** de `path` est passée pour éviter de modifier la liste originale dans les appels parallèles.  
     ```python
     left_path = dfs(node.left, target_ip, path.copy())  # Copie pour la branche gauche.
     right_path = dfs(node.right, target_ip, path.copy())  # Copie pour la branche droite.
     ```

5. **Retour du résultat** :  
   - Si la cible est trouvée à gauche, on retourne `left_path`.  
   - Sinon, on retourne `right_path`.  
   - Si rien n'est trouvé, on retourne `None`.

---

#### **Exemple avec l'Arbre du Projet**
- **Arbre utilisé** :
  ```
  RT1 (192.168.1.0/24)
  ├── RT3 (10.0.0.0/8)
  └── RT2 (172.16.0.0/16)
      └── RT7 (192.168.30.0/24)
  ```

- **Recherche de `192.168.30.0/24`** :
  1. `dfs(RT1, "192.168.30.0/24", [])`  
     - Ajoute `192.168.1.0/24` à `path`.
  2. Explore `RT2` (branche droite) :  
     - Ajoute `172.16.0.0/16` à `path`.
  3. Explore `RT7` (branche droite de RT2) :  
     - Ajoute `192.168.30.0/24` et retourne le chemin complet :  
       ```python
       ["192.168.1.0/24", "172.16.0.0/16", "192.168.30.0/24"]
       ```

---

#### **Utilité dans le Projet**
- **Affichage utilisateur** :  
  Le chemin retourné par `dfs` est affiché pour montrer comment la route a été trouvée.  
  Exemple :
  ```
  🌳 Chemin depuis la racine : ['192.168.1.0/24', '172.16.0.0/16', '192.168.30.0/24']
  ```

- **Différence avec `bfs_mark_unreachable`** :  
  - `dfs` est utilisé pour **trouver un chemin précis**.  
  - `bfs_mark_unreachable` (parcours en largeur) est utilisé pour **marquer tous les descendants d'une IP** comme inaccessibles.

---

#### **Points Clés**
- **Récursion** : La fonction s'appelle elle-même pour explorer chaque branche.  
- **Copie de `path`** : Nécessaire pour éviter que les branches gauche/droite ne se mélangent.  
- **Efficacité** : DFS est idéal pour retrouver un chemin dans un arbre, mais peut être moins efficace que BFS pour des arbres très déséquilibrés.

---

### Code Complet de `get_path_from_root`
```python
def get_path_from_root(root, ip):
    """Retourne le chemin depuis la racine jusqu'à l'IP cible en utilisant DFS."""
    def dfs(node, target_ip, path):
        if node is None:
            return None
        path.append(node.key)  # Ajoute le nœud actuel au chemin
        if node.key == target_ip:
            return path
        left_path = dfs(node.left, target_ip, path.copy())  # Branche gauche
        if left_path is not None:
            return left_path
        right_path = dfs(node.right, target_ip, path.copy())  # Branche droite
        if right_path is not None:
            return right_path
        return None

    return dfs(root, ip, []) or []  # Retourne [] si l'IP n'est pas trouvée
```

Cette fonction est essentielle pour comprendre comment le programme navigue dans l'arbre de routage !