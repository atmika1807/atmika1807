# Lucky Numbers – Human Coding Walkthrough

This is a CodeSignal filesystem problem. There are two files:
- `luckyNumberPrinter.js` – already written, you cannot change it
- `luckyChecker.js` – you have to write the `isLucky` function inside it

---

## The Problem (plain English)

Print numbers 1 to 100. But if a number is "lucky", print `Lucky!` instead.

A number is **lucky** if:
- it is **divisible by 7** (like 7, 14, 21...)
- OR it **contains the digit 7** (like 7, 17, 27, 70, 71, 72...)

Expected output (first 20 lines):
```
1
2
3
4
5
6
Lucky!    <- 7 (divisible by 7 AND contains 7)
8
9
10
11
12
13
Lucky!    <- 14 (divisible by 7)
15
16
Lucky!    <- 17 (contains digit 7)
18
19
20
```

---

## Where to Edit

Only touch `luckyChecker.js`. The file is basically empty:
```js
// luckyChecker.js  <-- THIS is the file you edit every attempt
const isLucky = (x) => {
    // TODO: fill this in
};

module.exports = { isLucky };
```

---

## Attempt 1 – The "that should be enough" mistake

**What the human thinks:** *"Lucky means divisible by 7, right? Let me just do that."*

**Edit `luckyChecker.js` to:**
```js
const isLucky = (x) => {
    return x % 7 === 0;
};

module.exports = { isLucky };
```

**Run it. Output looks like:**
```
1
2
3
4
5
6
Lucky!   <- 7 ✓
8
...
16
17       <- WRONG, should be Lucky!
```

**What went wrong:** Read the problem description again... "*divisible by 7 OR contains the digit 7*".
Missed the second condition entirely. Classic skim-reading mistake.

---

## Attempt 2 – The type error mistake

**What the human thinks:** *"Ok I just need to also check if the number has a 7 in it. I'll use `.includes('7')`.*"

**Edit `luckyChecker.js` to:**
```js
const isLucky = (x) => {
    return x % 7 === 0 || x.includes('7');
};

module.exports = { isLucky };
```

**Run it. Crashes immediately:**
```
TypeError: x.includes is not a function
```

**What went wrong:** `x` is a **number**. Numbers don't have `.includes()`. Only strings do.
You have to convert `x` to a string first before calling string methods on it.

---

## Attempt 3 – The off-by-one mistake (the sneaky one)

**What the human thinks:** *"Oh right, convert to string first. I'll use `indexOf` to find the '7' character."*

**Edit `luckyChecker.js` to:**
```js
const isLucky = (x) => {
    return x % 7 === 0 || String(x).indexOf('7') > 0;
};

module.exports = { isLucky };
```

**Run it. Output looks mostly right but...**
```
...
70       <- WRONG, should be Lucky! (wait, 70 % 7 = 0, it passes)
71       <- WRONG, should be Lucky!
72       <- WRONG, should be Lucky!
73       <- WRONG, should be Lucky!
...
```

**What went wrong:** `indexOf` returns the **position** of the character.
- For `71`, `String(71).indexOf('7')` returns **0** (it's the first character)
- `0 > 0` is **false** → not detected as lucky
- Should be `>= 0`, not `> 0`!

`indexOf` returns -1 when the character is **not found**, so the correct check is `>= 0`.
Using `> 0` accidentally excludes numbers that **start with** 7.

---

## Attempt 4 – The fix that actually works

**What the human thinks:** *"Ugh, I'll just use `.includes()` like I did before, just remember to convert to string first."*

**Edit `luckyChecker.js` to:**
```js
const isLucky = (x) => {
    return x % 7 === 0 || x.toString().includes('7');
};

module.exports = { isLucky };
```

**Run it. Output is correct!**
```
1
2
3
4
5
6
Lucky!   <- 7  ✓
8
9
10
11
12
13
Lucky!   <- 14 ✓
15
16
Lucky!   <- 17 ✓
18
19
20
...
```

---

## Why each mistake happens to real humans

| Attempt | Mistake | Why it happens |
|---------|---------|----------------|
| 1 | Forgot second condition | Skimmed the problem, brain filled in the obvious part and moved on |
| 2 | Called `.includes()` on a number | Muscle memory — you write `.includes()` all the time on strings, forgot to check what type `x` is |
| 3 | Used `indexOf > 0` instead of `>= 0` | Confused "found" with "found after position 0" — a very common off-by-one on indexOf |
| 4 | Works | Switched to `.includes()` which reads as plain English and avoids the index confusion |

---

## Key takeaways

1. Read the **full** problem description before writing any code.
2. Always check the **type** of your variables before calling methods on them.
3. `indexOf` returns `-1` for not found, `0` or higher for found — **not** `0` for not found.
4. `.includes()` is cleaner than `indexOf >= 0` for this exact reason.
