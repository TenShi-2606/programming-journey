# Mini-project: The Three Doors

## Objective
Build a small interactive text adventure using the fundamentals in the UNCHK L1 algorithmics syllabus.

## Concepts used
- Variables and strings
- Conditions (`if / elif / else`)
- Loops for input validation
- Functions and parameters
- Tuples and sets for allowed choices
- Branching narrative and test cases

## Run it
From the repository root:

```bash
python3 05_project/text_adventure.py
```

## Manual test plan
1. Enter an invalid door such as `yellow`: the game should ask again.
2. Choose `red`, then `read`: the Curious Mind ending should appear.
3. Choose `blue`, then `return`: the Patient ending should appear.
4. Try uppercase input such as `GREEN`: it should be accepted because input is normalized.
5. Try entering spaces before a choice: surrounding whitespace should be ignored.

## Possible improvements
- Add a score or inventory.
- Add more rooms and endings.
- Store choices in a data structure.
- Separate story data from the game logic.
- Add automated tests.

This is a first learning project, not a finished commercial game. The next step is to explain each function and make at least one independent modification.
