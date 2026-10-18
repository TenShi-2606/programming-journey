# TD 02 — Corrigé de référence
## Boucles, compteurs, accumulateurs et modulo

## Exercice A — range

Code : `for i in range(2, 7): print(i)`

Affichage :
```text
2
3
4
5
6
```

La borne 7 est exclue.

## Exercice B — while avec décrémentation

```python
count = 5
while count > 0:
    print(count)
    count = count - 2
```

| Test | count au test | Condition | Affichage | Après décrémentation |
|---:|---:|---|---:|---:|
| 1 | 5 | vrai | 5 | 3 |
| 2 | 3 | vrai | 3 | 1 |
| 3 | 1 | vrai | 1 | -1 |
| 4 | -1 | faux | — | arrêt |

Affichage : 5, 3, 1. La condition est évaluée avant chaque tour.

## Exercice C — modulo

Pour `number = 7`, `7 % 2 = 1`. Le reste n'est pas zéro, donc le test `number % 2 == 0` est faux et le programme affiche `Impair`.

Le modulo donne le reste de la division entière : `5 % 2 == 1`, car `5 = 2 × 2 + 1`. Pour des entiers divisés par 2, le reste vaut 0 pour un nombre pair et 1 pour un nombre impair.

## Exercice D — somme des nombres pairs

```python
total = 0
for i in range(1, 6):
    if i % 2 == 0:
        total = total + i
print(total)
```

Les valeurs de `i` sont 1, 2, 3, 4, 5. Seules 2 et 4 sont ajoutées.

| i | Reste i % 2 | Ajout ? | total après |
|---:|---:|---|---:|
| Départ | — | — | 0 |
| 1 | 1 | non | 0 |
| 2 | 0 | oui | 2 |
| 3 | 1 | non | 2 |
| 4 | 0 | oui | 6 |
| 5 | 1 | non | 6 |

Résultat final : **6**.

## Exemple complémentaire — somme de 1 à n

Pour `n = 5`, l'accumulateur évolue ainsi : 0 → 1 → 3 → 6 → 10 → 15. Résultat : 15.

## Exemple complémentaire — factorielle

`5! = 1 × 2 × 3 × 4 × 5 = 120`. On initialise le produit à 1, car multiplier par 0 donnerait toujours 0.

## Invariant et terminaison

Dans une boucle qui calcule une somme, l'invariant est que `total` contient la somme de toutes les valeurs déjà parcourues. Pour terminer un `while`, la variable de contrôle doit évoluer de manière à rendre la condition fausse. Une mise à jour absente ou dans la mauvaise direction peut créer une boucle infinie.
