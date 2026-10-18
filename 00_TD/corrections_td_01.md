# TD 01 — Corrigé de référence
## Pseudo-code, affectation, conditions et logique booléenne

> À utiliser pour vérifier le travail après une première tentative. Le corrigé sert aussi de support d'explication.

## Exercice A — Affectations successives

Pseudo-code :
```text
x ← 2
y ← 5
x ← x + y
y ← x - y
AFFICHER x, y
```

| Instruction | x | y | Explication |
|---|---:|---:|---|
| Départ | — | — | Variables non initialisées |
| x ← 2 | 2 | — | x reçoit 2 |
| y ← 5 | 2 | 5 | y reçoit 5 |
| x ← x + y | 7 | 5 | x reçoit l'ancienne valeur de x + y |
| y ← x - y | 7 | 2 | y reçoit 7 - 5 |

**Affichage :** `7 2`.

## Exercice B — Parité

Pour n = 9, `9 MOD 2 = 1`, donc le test `n MOD 2 = 0` est faux : afficher **impair**.  
Pour n = 12, `12 MOD 2 = 0`, donc le test est vrai : afficher **pair**.

## Exercice C — Maximum de trois nombres

```text
LIRE a, b, c
max ← a
SI b > max ALORS
    max ← b
FIN SI
SI c > max ALORS
    max ← c
FIN SI
AFFICHER max
```

Les comparaisons strictes suffisent pour trouver la valeur maximale, même en cas d'égalité. Si on doit aussi indiquer la position du maximum, il faut définir la règle de gestion des égalités.

## Exercice D — Validation d'une note

```text
LIRE note
SI note < 0 OU note > 20 ALORS
    AFFICHER "Note invalide"
SINON SI note >= 10 ALORS
    AFFICHER "admis"
SINON
    AFFICHER "ajourné"
FIN SI
```

La validation de l'intervalle doit être faite avant la décision d'admission.

## Vérifications essentielles

- Une affectation remplace la valeur d'une variable.
- `ET` exige que les deux conditions soient vraies.
- `OU` exige qu'au moins une condition soit vraie.
- Une condition `SINON` est exécutée si les branches précédentes ne sont pas sélectionnées.
