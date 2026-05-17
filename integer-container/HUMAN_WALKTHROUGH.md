# Integer Container – Human Coding Walkthrough

This is a CodeSignal progressive Python problem (Level 1).

---

## The Problem (plain English)

You have one file: `main.py`. You write a `solution(queries)` function.

The function receives a list of queries. Each query is a 2-element list:
- `["ADD", "5"]` — add integer 5 to the container, return empty string `""`
- `["EXISTS", "5"]` — check if 5 is in the container, return `"true"` or `"false"`

The container starts empty.

**Example:**
```python
queries = [
    ["ADD", "1"],
    ["ADD", "2"],
    ["ADD", "5"],
    ["ADD", "2"],
    ["EXISTS", "2"],
    ["EXISTS", "5"],
    ["EXISTS", "1"],
    ["EXISTS", "4"],
    ["EXISTS", "3"],
    ["EXISTS", "0"]
]
# Output: ["", "", "", "", "true", "true", "true", "false", "false", "false"]
```

---

## Where to Edit

Only touch `main.py`. The starter file is just:
```python
# main.py  <-- THIS is the only file you edit
def solution(queries):
    pass
```

---

## Attempt 1 – Forgot that ADD also needs a return value

**What the human thinks:** *"Loop through queries, handle ADD and EXISTS. Simple."*

**Edit `main.py` to:**
```python
def solution(queries):
    container = []
    results = []
    for query in queries:
        if query[0] == "ADD":
            container.append(query[1])   # forgot to append anything to results!
        elif query[0] == "EXISTS":
            results.append("true" if query[1] in container else "false")
    return results
```

**Run it. Output:**
```
["true", "true", "true", "false", "false", "false"]
```

**What went wrong:** The problem says ADD should return an empty string `""`. The output array must have one entry per query, including ADD queries. Got 6 items instead of 10.

> *"Oh. ADD returns empty string. I need to append \"\" for each ADD too."*

---

## Attempt 2 – Type mismatch (stored int, checked string)

**What the human thinks:** *"I should convert to int since these are numbers. Let me do `int(query[1])` when adding."*

**Edit `main.py` to:**
```python
def solution(queries):
    container = []
    results = []
    for query in queries:
        if query[0] == "ADD":
            container.append(int(query[1]))   # stores as int
            results.append("")
        elif query[0] == "EXISTS":
            results.append("true" if query[1] in container else "false")  # checks as string!
    return results
```

**Run it. Output:**
```
["", "", "", "", "false", "false", "false", "false", "false", "false"]
```

**What went wrong:** Container has `[1, 2, 5, 2]` (integers). Checking `"5" in [1, 2, 5, 2]` — string `"5"` is **not equal** to integer `5` in Python. Every single EXISTS returns `"false"`.

> *"What?? I added 5, why does EXISTS 5 say false?... Oh. I stored int but checked string. Python doesn't auto-convert."*

---

## Attempt 3 – Python's True/False vs the string "true"/"false"

**What the human thinks:** *"Ok convert both sides to int. And I'll use a ternary for true/false."*

**Edit `main.py` to:**
```python
def solution(queries):
    container = []
    results = []
    for query in queries:
        if query[0] == "ADD":
            container.append(int(query[1]))
            results.append("")
        elif query[0] == "EXISTS":
            results.append(True if int(query[1]) in container else False)  # Python booleans!
    return results
```

**Run it locally, print the result:**
```
['', '', '', '', True, True, True, False, False, False]
```

**Looks fine to the human... but the test FAILS.**

**What went wrong:** The test expects the strings `"true"` and `"false"` (lowercase). Python's boolean values `True` and `False` are NOT the same as those strings. `True != "true"`. This is really easy to miss because they look almost identical when printed.

> *"Why is it failing?! It looks right... oh. It wants the STRING 'true' not Python's True. Case matters too — lowercase t."*

---

## Attempt 4 – Works

**What the human thinks:** *"Just put actual string quotes around true and false. And I'll use a set instead of a list since it's faster for lookups."*

**Edit `main.py` to:**
```python
def solution(queries):
    container = set()
    results = []
    for query in queries:
        if query[0] == "ADD":
            container.add(int(query[1]))
            results.append("")
        elif query[0] == "EXISTS":
            results.append("true" if int(query[1]) in container else "false")
    return results
```

**Run it. Output:**
```
["", "", "", "", "true", "true", "true", "false", "false", "false"]
```

**Correct!** All tests pass.

---

## Why each mistake happens to real humans

| Attempt | Mistake | Why it happens |
|---------|---------|----------------|
| 1 | Forgot `""` for ADD | Focused on the logic, missed that every query needs a result entry |
| 2 | Stored int, checked string | Converted one side but forgot the other — very common type mismatch |
| 3 | Used Python `True`/`False` not `"true"`/`"false"` | In Python you write `True` constantly — muscle memory overrides reading the spec |
| 4 | Works | Slowed down and re-read the expected output format exactly |

---

## Key takeaways

1. Check your output **format** — count of items, types of each item, exact string casing.
2. In Python, **`True` and `"true"` are completely different things** — don't let the similarity fool you.
3. If you convert a value on the ADD side, convert it the same way on the EXISTS side.
4. Use a `set` over a `list` for membership checks — `in` on a set is O(1), on a list is O(n).
