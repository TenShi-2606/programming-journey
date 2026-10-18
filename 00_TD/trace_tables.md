# TD 01 — Pseudocode, Boolean Logic & Trace Tables

This file is for the **travaux dirigés (TD)** part of the UNCHK L1 algorithmics syllabus.

## 1. Variables and assignment

Pseudocode:

```text
a ← 4
b ← a + 3
a ← b * 2
AFFICHER a, b
```

Trace it one instruction at a time:

| Instruction | a | b |
|---|---:|---:|
| Start | — | — |
| a ← 4 | 4 | — |
| b ← a + 3 | 4 | 7 |
| a ← b * 2 | 14 | 7 |

Output: `14 7`. Assignment updates a variable; it is not an algebraic equality.

## 2. Conditions

```text
LIRE age
SI age >= 18 ALORS
    AFFICHER "majeur"
SINON
    AFFICHER "mineur"
FIN SI
```

Equivalent Python idea: `if age >= 18:` followed by an indented block, then `else:`.

## 3. Boolean operators

- `A ET B` is true only when both A and B are true.
- `A OU B` is true when at least one is true.
- `NON A` reverses A.

| A | B | A ET B | A OU B |
|---|---|---|---|
| False | False | False | False |
| False | True | False | True |
| True | False | False | True |
| True | True | True | True |

## 4. Practice — do the trace before running code

### Exercise A
```text
x ← 2
y ← 5
x ← x + y
y ← x - y
AFFICHER x, y
```
Write the value of `x` and `y` after every instruction.

### Exercise B
```text
n ← 9
SI n MOD 2 = 0 ALORS
    AFFICHER "pair"
SINON
    AFFICHER "impair"
FIN SI
```
Predict the output. Then repeat with `n ← 12`.

### Exercise C
Write pseudocode that reads three numbers and displays the largest. Consider ties.

### Exercise D
Write pseudocode that reads a score from 0 to 20 and displays "admis" if it is at least 10, otherwise "ajourné". Reject invalid scores.

## 5. Self-check
- Can I explain the difference between `=` in mathematics and assignment `←`?
- Can I trace a program without executing it?
- Can I evaluate AND, OR, and NOT?
- Can I explain why each branch of a condition is selected?

**Important:** try each exercise on paper before looking at or writing a solution.
