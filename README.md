# Projet : Optimisation du routage des paquets (ARB_routage)

## Description du projet

Ce projet a été réalisé dans le cadre du cours d'**Algorithmique Avancée avec Python** à l'ESGI. L'objectif principal est de modéliser une architecture réseau en utilisant des **arbres binaires** pour structurer une table de routage et d'optimiser le routage des paquets en trouvant le chemin le plus efficace entre les routeurs. Le projet implémente des algorithmes de parcours d'arbres tels que le **parcours en profondeur (DFS)** et le **parcours en largeur (BFS)** pour trouver le chemin optimal.

## Fonctionnalités

- **Représentation du réseau** : Chaque nœud de l'arbre représente un routeur, et les branches représentent les connexions entre les routeurs.
- **Algorithme de routage** : Utilisation de DFS et BFS pour trouver le chemin optimal vers une destination.
- **Simulation d'envoi de paquets** : Simulation de l'envoi de paquets en suivant le chemin optimal calculé.
- **Gestion des routes obstruées** : Gestion des cas où une route est obstruée et proposition d'une alternative.
- **Extension avec ABR** : Utilisation d'un arbre binaire de recherche pour optimiser la recherche des routes et leur coût.

## Structure du projet

Le projet est organisé en plusieurs modules Python :

- **BinTree.py** : Implémentation de la classe `BinTree` pour représenter les nœuds de l'arbre binaire.
- **Queue.py** : Implémentation d'une file d'attente (Queue) pour gérer les paquets en attente d'envoi.
- **RouteManager.py** : Gestion des routes et des algorithmes de routage.
- **SearchAlgorithms.py** : Implémentation des algorithmes de recherche (DFS, BFS, etc.).
- **PacketSender.py** : Simulation de l'envoi de paquets.
- **TreeVisualizer.py** : Visualisation de l'arbre de routage.
- **CacheManager.py** : Gestion du cache pour stocker les résultats de recherche.
- **Main.py** : Programme principal qui orchestre l'exécution du projet.

## Installation

Pour exécuter ce projet, vous devez avoir Python installé sur votre machine. Suivez les étapes suivantes :

1. Clonez ce dépôt GitHub :
   ```bash
   git clone https://github.com/votre-utilisateur/ARB_routage.git
   ```
2. Accédez au répertoire du projet :
   ```bash
   cd ARB_routage/programme
   ```
3. Exécutez le programme principal :
   ```bash
   python Main.py
   ```

## Utilisation

Le programme principal (`Main.py`) vous guidera à travers les différentes étapes du projet :

1. **Construction de l'arbre de routage** : L'arbre de routage est construit automatiquement à partir des données fournies.
2. **Recherche de routes** : Vous pouvez rechercher une route spécifique en entrant une adresse IP.
3. **Simulation d'envoi de paquets** : Vous pouvez simuler l'envoi d'un paquet en suivant le chemin optimal calculé.
4. **Visualisation de l'arbre** : L'arbre de routage est affiché dans le terminal avec des couleurs pour indiquer les nœuds recherchés.

## Outils utilisés

- **Python** : Langage de programmation principal.
- **Miro** : Pour la gestion des tâches et la création de diagrammes.
- **Mermaid** : Pour les diagrammes de flux et d'UML.
- **Copilote** : Pour les commentaires et descriptions dans le code.

## Difficultés rencontrées

 - **Gestion des parcours d’arbres** : La mise en place des algorithmes de parcours en profondeur (DFS) et en largeur (BFS) a été complexe, notamment en raison de la nécessité de gérer les nœuds et les branches de manière distincte.
 - **Optimisation du routage** : Déterminer le chemin optimal avec le coût le plus faible, sans utiliser la bibliothèque time. Cela m'aurait permis de mesurer le temps de recherche de chaque méthode afin de sélectionner la plus rapide, plutôt que de choisir celle ayant parcouru le moins de nœuds pour atteindre le réseau cible. Cela nécessité des recherches approfondies et des tests multiples.
 - **Gestion des routes obstruées avec alternative** : La gestion des cas où une route est obstruée et la proposition d’une alternative ont posé des problèmes de logique et de mise en œuvre.

## Perspectives d'amélioration

- **Automatisation des tests** : Implémenter des tests automatisés pour vérifier l'efficacité des algorithmes de routage.
- **Extension avec d'autres algorithmes** : Explorer d'autres algorithmes de routage pour améliorer les performances.

## Licence

Ce projet est sous licence MIT. Pour plus d'informations, consultez le fichier [LICENSE](LICENSE).

---
