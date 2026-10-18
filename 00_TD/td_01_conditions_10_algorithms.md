# TD 01 — Dix algorithmes conditionnels à tracer

**Consigne du syllabus :** tracer manuellement dix algorithmes conditionnels. Pour chaque cas, noter les variables, évaluer les conditions dans l'ordre et écrire exactement l'affichage.

## Partie A — Énoncés

### 1. Signe d'un nombre
```text
LIRE n
SI n > 0 ALORS
    AFFICHER "positif"
SINON SI n < 0 ALORS
    AFFICHER "negatif"
SINON
    AFFICHER "zero"
FIN SI
```
Tester avec 7, -3 et 0.

### 2. Pair ou impair
```text
LIRE n
SI n MOD 2 = 0 ALORS
    AFFICHER "pair"
SINON
    AFFICHER "impair"
FIN SI
```
Tester avec 8 et 11.

### 3. Majorité
```text
LIRE age
SI age >= 18 ALORS
    AFFICHER "majeur"
SINON
    AFFICHER "mineur"
FIN SI
```
Tester avec 17 et 18.

### 4. Admissibilité selon deux critères
```text
LIRE age, autorisation
SI age >= 18 ET autorisation = VRAI ALORS
    AFFICHER "autorise"
SINON
    AFFICHER "refuse"
FIN SI
```
Tester avec (20, vrai), (17, vrai) et (20, faux).

### 5. Intervalle inclusif
```text
LIRE n
SI n >= 10 ET n <= 20 ALORS
    AFFICHER "dans intervalle"
SINON
    AFFICHER "hors intervalle"
FIN SI
```
Tester avec 9, 10, 20 et 21.

### 6. Note valide puis résultat
```text
LIRE note
SI note < 0 OU note > 20 ALORS
    AFFICHER "invalide"
SINON SI note >= 10 ALORS
    AFFICHER "admis"
SINON
    AFFICHER "ajourne"
FIN SI
```
Tester avec -1, 9, 10 et 21.

### 7. Maximum de deux nombres
```text
LIRE a, b
SI a >= b ALORS
    AFFICHER a
SINON
    AFFICHER b
FIN SI
```
Tester avec (4, 9), (9, 4) et (5, 5).

### 8. Tarif selon l'âge
```text
LIRE age
SI age < 12 ALORS
    AFFICHER "enfant"
SINON SI age < 18 ALORS
    AFFICHER "junior"
SINON
    AFFICHER "adulte"
FIN SI
```
Tester avec 11, 12, 17 et 18. Les branches sont évaluées de haut en bas.

### 9. Divisibilité par 3
```text
LIRE n
SI n MOD 3 = 0 ALORS
    AFFICHER "multiple de 3"
SINON
    AFFICHER "non multiple de 3"
FIN SI
```
Tester avec 12 et 14.

### 10. Réduction conditionnelle
```text
LIRE prix
SI prix >= 10000 ALORS
    prix ← prix * 0.9
FIN SI
AFFICHER prix
```
Tester avec 9000 et 12000. Une réduction de 10 % revient à multiplier le prix par 0,9.

## Partie B — Corrigé rapide

| N° | Entrée | Affichage / valeur finale |
|---:|---|---|
| 1 | 7, -3, 0 | positif ; negatif ; zero |
| 2 | 8, 11 | pair ; impair |
| 3 | 17, 18 | mineur ; majeur |
| 4 | (20,vrai), (17,vrai), (20,faux) | autorise ; refuse ; refuse |
| 5 | 9, 10, 20, 21 | hors ; dans ; dans ; hors |
| 6 | -1, 9, 10, 21 | invalide ; ajourne ; admis ; invalide |
| 7 | (4,9), (9,4), (5,5) | 9 ; 9 ; 5 |
| 8 | 11, 12, 17, 18 | enfant ; junior ; junior ; adulte |
| 9 | 12, 14 | multiple de 3 ; non multiple de 3 |
| 10 | 9000, 12000 | 9000 ; 10800 |

## Auto-contrôle

- [ ] J'ai tracé les dix algorithmes avant de lire le corrigé.
- [ ] J'ai testé les limites (par exemple 10 et 20 dans un intervalle).
- [ ] Je peux expliquer pourquoi l'ordre des conditions compte.
- [ ] J'ai comparé mes prédictions aux résultats d'une implémentation Python.
