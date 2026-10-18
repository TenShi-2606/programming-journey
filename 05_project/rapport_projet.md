# Mini-projet commenté — The Three Doors

## 1. Présentation

**Type :** jeu textuel interactif en Python.  
**Objectif pédagogique :** réunir variables, entrées utilisateur, conditions, boucles, fonctions, structures de données et tests dans un petit programme exécutable.

Le joueur choisit une porte (rouge, bleue ou verte), puis une action liée à la scène. Chaque combinaison mène à une fin.

## 2. Algorithme général

```text
DEBUT
    AFFICHER le titre et la situation
    choix ← demander un choix valide parmi rouge, bleu, vert

    SI choix = rouge ALORS
        demander lire ou partir
        afficher la fin correspondante
    SINON SI choix = bleu ALORS
        demander nager ou revenir
        afficher la fin correspondante
    SINON
        demander explorer ou se reposer
        afficher la fin correspondante
    FIN SI

    AFFICHER le message de fin
FIN
```

## 3. Rôle des fonctions

- `ask_choice(prompt, choices)` : normalise la saisie avec `strip().lower()`, vérifie l'appartenance aux choix autorisés, puis recommence si l'entrée est invalide. La boucle se termine uniquement lorsqu'une réponse autorisée est donnée.
- `play()` : gère le scénario et les embranchements. Elle délègue la validation de saisie à `ask_choice`.
- `if __name__ == "__main__"` : lance le jeu uniquement quand le fichier est exécuté directement, pas lorsqu'il est importé par un autre module.

## 4. Structures et logique utilisées

| Notion | Utilisation dans le projet |
|---|---|
| Variable / chaîne | Conserver le choix du joueur |
| Entrée / sortie | `input()` et `print()` |
| Condition | Sélectionner la scène et la fin |
| Boucle `while` | Recommencer une saisie invalide |
| Fonction / paramètres | Réutiliser la validation pour plusieurs questions |
| Tuple | Fournir la liste ordonnée des choix autorisés |
| Ensemble (`set`) | Tester rapidement l'appartenance d'un choix |
| Validation | Refuser toute réponse non prévue |

## 5. Plan de tests manuels

| Test | Saisie | Résultat attendu |
|---|---|---|
| T1 | Porte : `yellow`, puis `red` | Refuse yellow et redemande la porte |
| T2 | `red`, puis `read` | Affiche la fin « The Curious Mind » |
| T3 | `blue`, puis `return` | Affiche la fin « The Patient » |
| T4 | `GREEN` | Accepte la saisie après conversion en minuscules |
| T5 | ` red ` | Accepte la saisie après suppression des espaces |
| T6 | Choix invalide à répétition | Continue à demander jusqu'à une réponse autorisée |

## 6. Limites et améliorations possibles

- Les scènes sont codées directement dans `play()`; un futur développement pourrait séparer les données narratives de la logique.
- Le jeu ne conserve pas encore un inventaire, un score ou un historique.
- On pourrait ajouter des tests automatisés pour la validation des choix.
- Le scénario est volontairement petit pour garder l'accent sur les bases algorithmiques.

## 7. Bilan à compléter après exécution

- [ ] Exécuter le jeu et effectuer les six tests.
- [ ] Expliquer le rôle de `while True` et pourquoi la fonction finit par retourner une réponse.
- [ ] Modifier une scène ou ajouter une fin sans casser les autres chemins.
- [ ] Noter les résultats observés et les éventuelles corrections.

**Note :** ce document décrit la conception attendue et les tests à effectuer. Ne pas déclarer les tests réussis avant de les avoir réellement exécutés.
