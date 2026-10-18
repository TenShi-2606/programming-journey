# My Programming Journey 💻

I'm preparing for **L1 Application Development at UNCHK (Université Numérique Cheikh Hamidou Kane)**. This repository documents the pre-entry algorithmics programme: course concepts, TD tracing, executable TP scripts, tests, and a mini-project.

## Repository map

| Path | Purpose |
|---|---|
| `00_TD/trace_tables.md` | Variables, assignment, Boolean logic, and hand-tracing |
| `00_TD/corrections_td_01.md` | Worked reference answers for TD 01 |
| `00_TD/td_02_boucles.md` | Loops, counters, accumulators, and modulo |
| `00_TD/td_03_structures.md` | Lists, matrices, linear/binary search, and sorting |
| `00_TD/td_04_fonctions_complexite.md` | Functions, invariants, termination, and complexity |
| `01_fundamentals/conditions.py` | Variables, types, conditions, Boolean expressions, score validation |
| `02_loops/loops.py` | Sums, factorials, multiplication tables, and a terminating while loop |
| `03_data_structures/search_sort.py` | Lists, matrices, linear/binary search, selection sort, bubble sort |
| `04_functions/modularity.py` | Functions, parameters, return values, scope, and prime testing |
| `05_project/` | The Three Doors — a commented text adventure with input validation |
| `06_TP/input_validation.py` | Practical input validation and conditional classification |
| `06_TP/measure_search.py` | Empirical timing comparison of linear and binary search |
| `07_tests/test_algorithms.py` | Automated regression tests for the core examples |

## Run the work

Run commands from the repository root with Python 3:

```bash
python3 01_fundamentals/conditions.py
python3 02_loops/loops.py
python3 03_data_structures/search_sort.py
python3 04_functions/modularity.py
python3 05_project/text_adventure.py
python3 06_TP/input_validation.py
python3 06_TP/measure_search.py
python3 -m unittest discover -s 07_tests -v
```

The input-validation TP expects a number from 0 to 20. The search-timing TP prints measured times for increasing list sizes; results vary by computer and Python version.

## Learning workflow

For each TD or TP:
1. Read the problem and write a prediction / trace.
2. Run the relevant code.
3. Compare the output with the prediction.
4. Explain the algorithm and its stopping condition.
5. Test edge cases and make one independent change.

## Programme coverage

- [x] Variables, assignment, conditions, Boolean logic, and modulo examples
- [x] Repetition with `for` and `while`, sums, factorial, and stopping conditions
- [x] Lists/matrices, linear and binary search, selection sort and bubble sort
- [x] Functions, parameters, return values, and local scope
- [x] TD files for tracing, structures, invariants, termination, and basic complexity
- [x] Executable TP scripts for validation and empirical search timing
- [x] Interactive text mini-project with manual test plan
- [x] Automated regression tests added
- [ ] Run every script and the test suite on the local machine
- [ ] Complete a personal explanation / oral walkthrough of each section
- [ ] Record and discuss timing measurements and complexity observations

**Status:** the repository now contains a broad first pass across the topics in the supplied pre-entry syllabus. The code and written reference answers are preparation materials; local execution, test results, and the student's own explanations remain to be verified.
