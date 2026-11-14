# intro-build-calculator

An intelligent calculator built with LangChain and Groq (Llama) as part of the
intro "build a calculator" course exercise.

**Public repository.** The default branch `main` carries the latest executed
notebook, `intelligent_calculator.ipynb`, with all saved outputs.

The agent answers natural-language math word problems by calling tools:

- `add(a, b)` — integer addition
- `tree_distance(crown_angle, crown_height)` — horizontal distance to a tree
  from the angle of elevation and crown height

## Files

- `intelligent_calculator.ipynb` — the notebook, committed after a full run
  (code cells carry their saved outputs and execution counts)
- `mcp_server.py` — MCP server exposing the `solve_math_problem` tool over
  stdio (also written by the notebook's `%%writefile` cell)

## Verification (all visible in the notebook's saved outputs)

- **Tool-call tests:** `add` (5+10 → 15, 7+8 → 15), `tree_distance`
  (~17.32 metres), and the missing-angle case where the agent asks for the
  elevation angle instead of guessing.
- **LangSmith:** tracing for project `intro-build-calculator`; the run query
  lists `intro_apples`, `intro_tree`, `intro_missing_angle` — all `success`.
- **MCP:** `mcp_server.py` was tested manually in MCP Inspector and verified
  programmatically in the notebook — an MCP client launches the server over
  stdio, lists its tools, calls `solve_math_problem` on both apple problems,
  and prints `Check: PASS` twice.
- **ChatGPT MCP tunnel:** unavailable (HTTP 401) — documented honestly in the
  notebook.
