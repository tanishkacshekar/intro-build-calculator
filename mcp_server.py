"""MCP server for the intelligent calculator course exercise.

Exposes a `solve_math_problem` tool over stdio. Tested two ways:
1. Manually, in MCP Inspector.
2. Programmatically, from intelligent_calculator.ipynb (the MCP client
   verification cells at the end of the notebook).
"""
import re

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("intro-calculator")

# Note: "one" is deliberately absent - phrases like "One person" do not
# name a quantity. It is counted only in the explicit form "one apple(s)".
WORD_NUMBERS = {
    "zero": 0, "two": 2, "three": 3, "four": 4, "five": 5,
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14,
    "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
    "nineteen": 19, "twenty": 20,
}


def _extract_numbers(text: str) -> list:
    numbers = [int(n) for n in re.findall(r"\d+", text)]
    numbers.extend(
        WORD_NUMBERS[w]
        for w in re.findall(r"[a-z]+", text.lower())
        if w in WORD_NUMBERS
    )
    if re.search(r"\bone\s+apples?\b", text, re.IGNORECASE):
        numbers.append(1)
    return numbers


@mcp.tool()
def solve_math_problem(problem: str) -> str:
    """Solve the course's simple addition word problems (e.g. "Five apples
    and ten more are put together. How many apples are there?") by adding
    the quantities mentioned in the problem."""
    numbers = _extract_numbers(problem)
    if len(numbers) < 2:
        return "I need at least two quantities to add."
    total = sum(numbers)
    item = "apples" if re.search(r"apple", problem, re.IGNORECASE) else "items"
    return f"The total is {total} {item}."


if __name__ == "__main__":
    mcp.run(transport="stdio")