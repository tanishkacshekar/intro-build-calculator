# intro-build-calculator

An intelligent calculator built with LangChain and Groq (Llama) as part of the
intro "build a calculator" course exercise.

The agent answers natural-language math word problems by calling tools:

- `add(a, b)` — integer addition
- `tree_distance(crown_angle, crown_height)` — horizontal distance to a tree
  from the angle of elevation and crown height

## Notebook

`intelligent_calculator.ipynb` is committed **after a full run** — every code
cell has its saved output and execution count (1–16), including:

- tool-call tests (`add`, `tree_distance`) with results
- three solved problems: apples, tree height, and the missing-angle case
  (which correctly asks for the elevation angle instead of guessing)
- LangSmith tracing setup for project `intro-build-calculator`
- a LangSmith run query listing the traced runs:
  `intro_apples`, `intro_tree`, `intro_missing_angle` (all `success`)
