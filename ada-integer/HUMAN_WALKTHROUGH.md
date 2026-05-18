# Ada Integer Representation – Human Walkthrough

## The Problem

Check if a string is a valid integer. Two valid formats:

1. **Decimal**: only digits 0-9, underscores ok as separators. Like `123_456`.
2. **Base notation**: `<base>#<digits>#` where:
   - base is a number from 2 to 16
   - digits are valid in that base (a-f or A-F for 10-15)
   - underscores allowed anywhere as separators
   - at least one actual digit must exist (not just underscores)

Examples:
```
"123_456_789"  -> True   (plain decimal)
"16#123abc#"   -> True   (base 16, digits 1,2,3,a,b,c all valid)
"10#123abc#"   -> False  (base 10, 'a' = 10, not valid in base 10)
"10#10#123ABC#"-> False  (second '#' is not a valid digit)
"10#0#"        -> True   (base 10, single digit 0)
"10##"         -> False  (no digits at all between the ##)
```

## Where to Edit

Only the `...` inside `solution()` in the starter file. The rest is given.
The `...` is between `base = 0` and `if base < 2 or base > 16`.
Your job: read the base number from the start of the string up to the first `#`.
After your code runs, `i` must be pointing AT the `#` character (the existing `i += 1` moves past it).

---

## Attempt 1 – split('#') but i is off by one

*"easiest thing is just split on # and grab the first chunk"*

**Edit the `...` to:**
```python
parts = line.split('#')
base = int(parts[0])
i = len(parts[0]) + 1   # thought: skip the base AND the '#'
```

**Two bugs immediately:**

**Bug 1** – `int('1_6')` crashes with ValueError if the base has underscores.
`"1_6#abc#"` splits to `['1_6', 'abc', '']`. `int('1_6')` → ValueError.

**Bug 2** – even if that worked, `i` is wrong.
The existing code already does `i += 1` after `...` to move past `#`.
So if I set `i = len(parts[0]) + 1` (already past `#`), then `i += 1` runs again,
putting i TWO spots past `#`. First digit of the number gets skipped.

For `"16#abc#"`, first digit `a` would be skipped. Wrong answer.

> *printed i before and after to debug, saw it was landing at 4 not 3*

---

## Attempt 2 – fix i offset and strip underscores, but still crashes on letters

*"ok two fixes: strip underscores before int(), and i should point AT '#' not past it"*

**Edit the `...` to:**
```python
hash_idx = line.find('#')
base_str = line[:hash_idx].replace('_', '')
base = int(base_str) if base_str else 0
i = hash_idx   # point AT '#', existing i+=1 moves past it correctly
```

**Still crashes.**
`"ab#xyz#"` is supposed to return False (invalid base), but instead:
`base_str = 'ab'`, `int('ab')` → ValueError. Crash instead of clean False.

> *"oh right, what if someone passes garbage in the base part. need to handle that"*

Thought about wrapping in try/except but felt messy. Looked at the digit loop below —
it goes character by character with `i`. Why not just do the same?

---

## Attempt 3 – loop char by char, same pattern as the rest of the code

*"stop being clever. just loop like the rest of the code does"*

**Edit the `...` to:**
```python
while line[i] != '#':
    if line[i] != '_':
        if not line[i].isdigit():
            return False
        base = base * 10 + int(line[i])
    i += 1
# when loop ends, line[i] is '#' -- exactly right for the existing i+=1
```

**Tested all examples manually:**

| input | what happens | result |
|-------|-------------|--------|
| `"123_456_789"` | last char not `#`, goes to else branch, all digits | True ✓ |
| `"16#123abc#"` | loop reads `1`,`6` → base=16, digits pass | True ✓ |
| `"10#123abc#"` | base=10, hits `a` in digit section, 10 < 10 is False | False ✓ |
| `"10#10#123ABC#"` | base=10, second `#` in digits → digit=-1 → False | False ✓ |
| `"10#0#"` | base=10, digit `0` valid | True ✓ |
| `"10##"` | base=10, no digits, atLeastOneDigit stays False | False ✓ |

All pass. Done.

---

## Why each mistake happened

| Attempt | Mistake | Why |
|---------|---------|-----|
| 1 | Used `split` and got `i` wrong | Grabbed a quick Python trick without thinking about what `i` meant in context |
| 1 | `int()` on string with underscore | Forgot underscores were a thing until it crashed |
| 2 | `int()` on letters crashes | Fixed underscores but didn't think about non-digit chars in base |
| 3 | Works | Stopped reaching for Python shortcuts, just copied the same loop pattern already in the code |

**The lesson:** when filling in missing code inside a function, match the style and pattern already there. The digit loop was already character-by-character. Doing the same for the base loop was the obvious move — just didn't see it until attempt 3.
