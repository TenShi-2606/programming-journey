# TD 02 — Boucles, compteurs et accumulateurs

**Objectif :** savoir tracer une boucle à la main avant d'exécuter le programme.  
**Méthode :** pour chaque tour, noter la valeur de la variable, vérifier la condition, puis noter l'action et la nouvelle valeur.

## 1. Exemple corrigé — boucle for

```python
total = 0
for i in range(1, 4):
    total = total + i
print(total)
```

| Tour | i | total avant | total après |
|---:|---:|---:|---:|
| Départ | — | — | 0 |
| 1 | 1 | 0 | 1 |
| 2 | 2 | 1 | 3 |
| 3 | 3 | 3 | 6 |

**Résultat :** 6. L'accumulateur conserve sa valeur d'un tour au suivant. La borne de fin de range est exclue.

## 2. Exercice A — prédire l'affichage

Sans exécuter le code, écris les nombres affichés dans l'ordre.

```python
for i in range(2, 7):
    print(i)
```

**Ma réponse :** à compléter.

## 3. Exercice B — boucle while

```python
count = 5
while count > 0:
    print(count)
    count = count - 2
```

Complète la trace :

| Tour | count au test | count > 0 ? | Affichage | Nouvelle valeur |
|---:|---:|---|---:|---:|
| 1 | 5 | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |

**Règle à retenir :** la condition du while décide si on continue ; l'instruction qui modifie count détermine dans quelle direction il évolue.

## 4. Exercice C — pair ou impair avec modulo

L'opérateur % donne le reste de la division entière. Par exemple, 5 % 2 vaut 1, car 5 = 2 × 2 + 1.

```python
number = 7
if number % 2 == 0:
    print("Pair")
else:
    print("Impair")
```

**Ma prédiction :** à compléter.  
**Explication avec mes mots :** à compléter.

## 5. Exercice D — somme des nombres pairs

```python
total = 0
for i in range(1, 6):
    if i % 2 == 0:
        total = total + i
print(total)
```

1. Valeurs de i parcourues : à compléter.
2. Valeurs ajoutées à total : à compléter.
3. Résultat final : à compléter.

## 6. Auto-évaluation

- [ ] Je sais que range(debut, fin) exclut fin.
- [ ] Je sais suivre la valeur d'un accumulateur.
- [ ] Je sais expliquer la condition d'un while et son instruction de mise à jour.
- [ ] Je sais utiliser % 2 pour reconnaître les nombres pairs et impairs.
- [ ] J'ai répondu aux exercices sans copier la correction.
- [ ] J'ai ensuite exécuté le code et comparé les résultats.

**Statut :** exercices en cours. Les réponses personnelles seront ajoutées après vérification.