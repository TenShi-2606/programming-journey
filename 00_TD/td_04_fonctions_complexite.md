# TD 04 — Fonctions, invariants et complexité

## Exercice A — Fonction et valeur de retour

Écrire une fonction `carre(n)` qui retourne le carré de n. Exemple : `carre(4) == 16`.

Correction Python :
```python
def carre(n: int) -> int:
    return n * n
```

La valeur retournée peut être réutilisée dans un calcul. `print` affiche une valeur mais ne remplace pas `return`.

## Exercice B — Portée locale

```python
def addition(a, b):
    resultat = a + b
    return resultat

print(addition(2, 3))
```

Affichage : 5. Les paramètres `a`, `b` et la variable `resultat` sont locaux à la fonction. Ils ne sont pas automatiquement disponibles hors de celle-ci.

## Exercice C — Invariant de somme

```python
total = 0
for i in range(1, n + 1):
    total += i
```

**Invariant :** après le traitement de i, `total` vaut la somme des entiers de 1 à i.  
**Initialisation :** avant la boucle, `total = 0`, ce qui correspond à une somme vide.  
**Conservation :** au tour i, on ajoute i à la somme précédente, ce qui produit la somme jusqu'à i.  
**Terminaison :** la boucle effectue un nombre fini d'itérations ; i avance de 1 jusqu'à n.

## Exercice D — Terminaison d'un while

```python
count = 5
while count > 0:
    count -= 1
```

La variable diminue de 1 à chaque tour et finit par atteindre 0. La condition `count > 0` devient alors fausse. Si la mise à jour était absente, la boucle ne terminerait pas.

## Exercice E — Complexité

| Algorithme | Idée | Complexité temporelle indicative |
|---|---|---|
| Accéder à un indice de liste | Accès direct | O(1) |
| Parcourir une liste | Un passage | O(n) |
| Recherche linéaire | Examiner au plus n éléments | O(n) |
| Recherche dichotomique | Diviser la zone de recherche par deux | O(log n) |
| Tri par sélection | Comparaisons imbriquées | O(n²) |

La complexité décrit l'évolution du travail quand la taille des données augmente ; elle ne prédit pas à elle seule un temps exact en secondes.
