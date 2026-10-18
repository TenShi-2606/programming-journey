# TD 03 — Tableaux, recherche et tri

## Objectifs
- Tracer les indices et valeurs d'une liste.
- Distinguer recherche linéaire et recherche dichotomique.
- Comprendre le rôle d'un tableau trié.
- Comparer les tris par sélection et à bulles.

## Exercice A — Parcours d'une liste

Liste : `[8, 3, 6, 1, 5]`

1. Écrire les indices Python de chaque valeur.
2. Donner l'état de la variable `total` après chaque tour pour l'algorithme qui additionne tous les éléments.
3. Déterminer le maximum sans utiliser la fonction intégrée `max`.

Pseudo-code pour la somme :
```text
total ← 0
POUR chaque valeur v du tableau
    total ← total + v
FIN POUR
AFFICHER total
```

**Résultats de contrôle :** indices 0 à 4 ; somme = 23 ; maximum = 8.

## Exercice B — Recherche linéaire

Chercher 6 dans `[8, 3, 6, 1, 5]`.

| Comparaison | Valeur observée | Résultat |
|---:|---:|---|
| 1 | 8 | différente de 6 |
| 2 | 3 | différente de 6 |
| 3 | 6 | trouvé |

Avec des indices commençant à zéro, la fonction renvoie **2**. En recherche linéaire, on examine les éléments dans l'ordre jusqu'à trouver la cible ou atteindre la fin.

## Exercice C — Recherche dichotomique

Chercher 6 dans le tableau trié `[1, 3, 5, 6, 8]`.

1. Indices de départ : gauche = 0, droite = 4.
2. Milieu = (0 + 4) // 2 = 2 ; valeur = 5. Comme 5 < 6, déplacer gauche à 3.
3. Milieu = (3 + 4) // 2 = 3 ; valeur = 6 : cible trouvée à l'indice 3.

**Condition essentielle :** le tableau doit être trié dans l'ordre attendu. Sinon, éliminer une moitié peut éliminer la cible.

## Exercice D — Tri par sélection

Trier `[4, 2, 3, 1]`.

- Passe 1 : chercher le minimum de toute la liste (1), échanger avec la première valeur → `[1, 2, 3, 4]`.
- Passe 2 : le minimum de la partie restante est 2 ; aucun changement.
- Passe 3 : le minimum de la partie restante est 3 ; aucun changement.

Résultat : `[1, 2, 3, 4]`.

## Exercice E — Matrice

Pour `[[1, 2, 3], [4, 5, 6]]`, la somme de tous les éléments vaut **21**.

## Complexité — premier aperçu

- Recherche linéaire : au plus n éléments examinés, temps O(n).
- Recherche dichotomique : intervalle divisé par deux à chaque étape, temps O(log n).
- Tris par sélection et à bulles : temps O(n²) dans le cas général.
