# Day 2 Laboratory — Check First, Then Run

**Part I · Chapter 2 · Day 2** · 25 exercises · Goes with [Lecture 2](../Lectures/Lecture-02-How-Programming-Languages-Work.md)

## Before you start

**Today's one skill:** predicting what happens when you run a file. Python **checks the whole file first** (stage 1), then **runs it line by line** (stage 2). You will practise telling **syntax errors**, **runtime errors** and **logic errors** apart, and reading Python's error messages.

**You may use only:** `print("text")`, `print('text')` and `print()`, the same as Day 1. Every mistake in this lab is a mistake in a `print()` line.

### How to work

1. Save every exercise in `My-Solutions/Lab-02/`, one file each, named as the exercise says.
2. Keep a file called `predictions.md` in the same folder. For every exercise that says **predict**, write your prediction there **before** you run anything. Then write what really happened underneath.
3. **Type the broken code exactly as shown, mistakes included.** The mistakes are the point.
4. To run a file: `python3 ex01_all_good.py` (macOS/Linux) or `python ex01_all_good.py` (Windows).
5. The file path at the top of each error message will be different on your computer. That is normal. Ignore it.
6. Submit after each level for review.

### The three questions to ask every time

1. **Stage 1:** is the grammar correct on **every** line? If not, **nothing** will appear.
2. **Stage 2:** if the grammar is fine, which line (if any) uses a command name that does not exist? Everything **above** it will appear.
3. **Output:** is the output what was wanted? If not, it is a **logic error**.

### Levels

| Level | Exercises | What it is for |
| --- | --- | --- |
| 1 | 1–5 | Seeing the two stages for yourself |
| 2 | 6–10 | Predicting and classifying errors |
| 3 | 11–15 | Files with more than one mistake |
| 4 | 16–20 | Debugging and reading error messages |
| 5 | 21–25 | Realistic problems and your own puzzles |

---

## Level 1 — Seeing the two stages for yourself

### Exercise 1 — A file with no mistakes

**File:** `ex01_all_good.py`

```python
print("Line 1")
print("Line 2")
print("Line 3")
print("Line 4")
```

Run it. In `predictions.md`, write how many lines appeared and whether there was an error message. You will compare every other exercise with this one.

**Tests:** both stages passing.

---

### Exercise 2 — Missing bracket on the last line

**File:** `ex02_bracket_last.py`

Copy your Exercise 1 file, then delete the `)` from the **last** line only.

**Predict:** will `Line 1`, `Line 2` and `Line 3` appear? Then run it.

**Write down:** the last line of the error message, and the line number it gave.

**Hint:** Lecture 2, C.5. **Tests:** a syntax error stops everything.

---

### Exercise 3 — Misspelt `print` on the last line

**File:** `ex03_misspell_last.py`

Copy your Exercise 1 file, then change the last `print` to `Print`.

**Predict:** which lines will appear? Then run it.

**Question:** Exercises 2 and 3 both have one mistake on the last line. Why is the output so different?

**Hint:** Lecture 2, C.6. **Tests:** a runtime error stops at its line.

---

### Exercise 4 — Missing quote on the first line

**File:** `ex04_quote_first.py`

```python
print("Line 1)
print("Line 2")
print("Line 3")
print("Line 4")
```

**Predict,** then run. Compare the output with Exercise 2.

**Question:** does it make any difference to the output whether a syntax error is on the first line or the last line? Why?

**Tests:** stage 1 checks the whole file, wherever the mistake is.

---

### Exercise 5 — Misspelt `print` on the first line

**File:** `ex05_misspell_first.py`

```python
prnt("Line 1")
print("Line 2")
print("Line 3")
print("Line 4")
```

**Predict,** then run.

**Question:** this time no lines appeared, just like a syntax error. So how can you tell from the message that it was a **runtime** error and not a syntax error? (Look at the first word of the message.)

**Hint:** Lecture 2, C.6 table. **Tests:** recognising the two kinds of message.

---

## Level 2 — Predicting and classifying errors

### Exercise 6 — A syntax error in the middle

**File:** `ex06_syntax_middle.py`

```python
print("Checking system...")
print("Disk: OK")
print("Memory: OK")
print("Network: OK"
print("Firewall: OK")
print("All checks finished.")
```

**Predict** exactly what will appear. Run it. Then fix it and run again.

**Tests:** the position of a syntax error does not matter.

---

### Exercise 7 — A runtime error in the middle

**File:** `ex07_runtime_middle.py`

```python
print("Checking system...")
print("Disk: OK")
print("Memory: OK")
Print("Network: OK")
print("Firewall: OK")
print("All checks finished.")
```

**Predict** exactly which lines will appear. Run it.

**Question:** the program never printed `All checks finished.`. If this were a real system check, what would the user wrongly believe if they did not read the error?

**Tests:** the position of a runtime error decides how much runs.

---

### Exercise 8 — Sort the mistakes

**File:** `ex08_test.py` (you will reuse it)

Here are ten lines. For each one, **predict** in `predictions.md`: syntax error, runtime error, logic error, or no error at all. (For logic errors, imagine the intended text is the correct English.)

| # | Line |
| --- | --- |
| a | `print("Good morning")` |
| b | `print("Good morning"` |
| c | `Print("Good morning")` |
| d | `print("Good mornign")` |
| e | `print('Good morning")` |
| f | `prnt("Good morning")` |
| g | `print "Good morning"` |
| h | `print(Good morning)` |
| i | `PRINT("Good morning")` |
| j | `print("Good morning"))` |

Now test them **one at a time**: put one line in `ex08_test.py`, run it, write down the result, then replace it with the next line.

**Score yourself:** how many did you predict correctly, out of 10?

**Tests:** classifying errors.

---

### Exercise 9 — Read the message, find the mistake

**Files:** `ex09a.py`, `ex09b.py`, `ex09c.py`

Here are three real error messages, each from a different 3-line program.

**Message A**

```text
  File "ex09a.py", line 2
    print("Room 101 is free)
          ^
SyntaxError: unterminated string literal (detected at line 2)
```

**Message B**

```text
Room 101 is free
Traceback (most recent call last):
  File "ex09b.py", line 2, in <module>
    Prnt("Room 102 is busy")
    ^^^^
NameError: name 'Prnt' is not defined. Did you mean: 'print'?
```

**Message C**

```text
  File "ex09c.py", line 3
    print "Room 103 is free"
    ^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
```

For each message, write in `predictions.md`:

1. Is it a syntax error or a runtime error? How can you tell?
2. Which line has the mistake, and what is the mistake?
3. Did any lines run?

Then **recreate** each program: write a 3-line file that produces that exact message when run. (The file path in your message will be longer. That is fine.) Then fix each file.

**Tests:** reading error messages, working backwards from a message to code.

---

### Exercise 10 — Spelling inside and outside the quotes

**File:** `ex10_inside_outside.py`

```python
print("The command is called prnt")
print("Pyhton is easy to read")
print("WARNING: Pasword must be strong")
```

**Predict:** will there be an error? Run it.

Then change line 1 so the word `print` **outside** the quotes is misspelt as `prnt`. Predict, and run again.

**Question:** why does a spelling mistake inside the quotes cause no error, but one outside the quotes does? What kind of error are the misspellings inside the quotes? Fix all of them.

**Hint:** Lecture 2, Example 6. **Tests:** text versus command names.

---

## Level 3 — Files with more than one mistake

### Exercise 11 — Which mistake is reported first?

**File:** `ex11_two_mistakes.py`

```python
Print("Welcome")
print("Please wait")
print("Loading"
```

**Predict:** which line will the first error message point at, and why? Run it.

Fix **only** that line. **Predict** what happens next, then run again. Fix the other mistake and run a third time.

**Write down** the output of all three runs.

**Hint:** Lecture 2, C.8. **Tests:** syntax errors are reported before runtime errors.

---

### Exercise 12 — Three syntax errors

**File:** `ex12_three_syntax.py`

```python
print("Monday: Lecture")
print("Tuesday: Lab"
print("Wednesday: Study)
print("Thursday: Work")
print "Friday: Lecture"
```

**Predict:** how many times will you need to run the file to find all three mistakes?

Run it, fix **only** the line reported, and run again. Keep a table in `predictions.md`:

| Run | Line reported | Error message (last line) | What I fixed |
| --- | --- | --- | --- |
| 1 | | | |

Keep going until the program works.

**Question:** did Python report all three mistakes at once? Did it report them in line order?

**Tests:** one syntax error at a time.

---

### Exercise 13 — Two runtime errors

**File:** `ex13_two_runtime.py`

```python
print("Step 1")
Print("Step 2")
print("Step 3")
print("Step 4")
prnt("Step 5")
print("Step 6")
```

**Predict** the output of the first run. Run it. Fix the first mistake, **predict** the second run, and run again. Fix the second mistake and run a third time.

**Question:** in the first run, did Python know about the mistake on line 5? Why not?

**Tests:** stage 2 stops at the first runtime error it reaches.

---

### Exercise 14 — Make it fail at a chosen line

**File:** `ex14_fail_at_line5.py`

Write a 6-line program of your own that, when run, shows **exactly the first four lines** of output and then a runtime error that points at **line 5**.

Then explain in `predictions.md` why lines 5 and 6 did not appear.

**Tests:** using your understanding to design behaviour.

---

### Exercise 15 — Make it show nothing

**File:** `ex15_show_nothing.py`

Write a 6-line program where lines 1 to 5 are perfect `print()` lines, but running it shows **no output at all**, only an error message pointing at **line 6**.

Then write **two different** versions of line 6 that both cause this (save the second version as `ex15_show_nothing_v2.py`).

**Question:** could you make lines 1 to 5 show nothing using a misspelt `print` on line 6? Why or why not?

**Tests:** using stage 1 deliberately.

---

## Level 4 — Debugging and reading error messages

### Exercise 16 — Fix the welcome screen

**File:** `ex16_welcome_fix.py`

This program has **four** mistakes: two syntax errors, one runtime error and one logic error (a spelling mistake inside the quotes).

```python
print("==============================")
print("   NORTHGATE SYSTEMS"
print("==============================")
print()
Print("Welcome, authorised user.")
print("Your last login was yesterday.)
print()
print("Remember to lock your screan.")
print("==============================")
```

**Target output**

```text
==============================
   NORTHGATE SYSTEMS
==============================

Welcome, authorised user.
Your last login was yesterday.

Remember to lock your screen.
==============================
```

**Before running**, list all four mistakes in `predictions.md`, and say which kind each one is and in what order Python will report them. Then run and fix them one at a time, checking your predicted order.

**Question:** which mistake did Python never report? How did you find it?

**Tests:** using the two stages to debug a realistic program.

---

### Exercise 17 — Prediction sheet

**Files:** `ex17a.py` to `ex17e.py`

For each mini program, **write down the exact output** (or "no output", and the kind of error) **before** you type it. Then type and run each one, and mark your predictions right or wrong.

**A**

```python
print("Red")
print("Green")
print("Blue")
```

**B**

```python
print("Red")
print("Green"
print("Blue")
```

**C**

```python
print("Red")
Print("Green")
print("Blue")
```

**D**

```python
print()
print("Red")
prnt()
print("Blue")
```

**E**

```python
Print("Red")
print("Green")
print("Blue)
```

**Score:** out of 5.

**Tests:** fast, accurate prediction.

---

### Exercise 18 — Logic error hunt

**File:** `ex18_logic_hunt.py`

This program runs with **no error at all**, but it is wrong in **six** places compared with the target. Type it exactly, run it, and compare its output with the target line by line. Then fix it.

```python
print("LIBRARY NOTICE")
print()
print("The libary is open from 9am to 5pm.")
print("Please keep noise to a minimum.")
print("Food is allowed in the computer room.")
print("Return books by Firday.")
print()
print("Thank you")
print("LIBRARY NOTICE")
```

**Target output**

```text
LIBRARY NOTICE

The library is open from 9am to 8pm.
Please keep noise to a minimum.
Food is NOT allowed in the computer room.
Return books by Friday.

Thank you!
```

**Write down** each of the six differences you found.

**Question:** Python did not help you at all here. What did you use instead?

**Tests:** finding logic errors by comparing output.

---

### Exercise 19 — Explain it in your own words

**File:** `ex19_explain.py`

Write a program that **prints** your own explanation of how Python runs a file. It must show at least 12 lines, with a title, and must explain:

- what happens in stage 1 and what happens in stage 2,
- why a syntax error means no output,
- why a runtime error means some output,
- what a logic error is,
- one tip for reading error messages.

The program itself must, of course, have no errors.

**Tests:** explaining the concept clearly (and Day 1 printing skills).

---

### Exercise 20 — Match the message to the code

**File:** `ex20_test.py` (you will reuse it)

Match each line of code (1–6) with the error message it causes (A–F). Write your matches in `predictions.md` **before** testing.

| # | Code |
| --- | --- |
| 1 | `print("Hi"` |
| 2 | `Print("Hi")` |
| 3 | `print("Hi)` |
| 4 | `print("Hi"))` |
| 5 | `print "Hi"` |
| 6 | `print(Hi)` |

| Letter | Last line of the error message |
| --- | --- |
| A | `SyntaxError: unmatched ')'` |
| B | `NameError: name 'Hi' is not defined` |
| C | `SyntaxError: '(' was never closed` |
| D | `SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?` |
| E | `NameError: name 'Print' is not defined. Did you mean: 'print'?` |
| F | `SyntaxError: unterminated string literal (detected at line 1)` |

Then test each line on its own in `ex20_test.py` and check your matches.

**Question:** lines 2 and 6 both give a `NameError`. What do they have in common? (Hint: what does Python think `Hi` is, when it has no quotes?)

**Tests:** linking each mistake to its message.

---

## Level 5 — Realistic problems and your own puzzles

### Exercise 21 — The broken lab notice

**File:** `ex21_lab_notice.py`

This 14-line notice has **six** mistakes: three syntax errors, one runtime error and two logic errors (spelling inside quotes).

```python
print("**********************************")
print("*        CYBER LAB RULES         *")
print("**********************************")
print()
print("1. Log in with your own account.")
print("2. Never share your pasword."
print("3. Lock your screen when you leave.")
Print("4. Report anything suspicious.")
print("5. No food or drink near computers.)
print("6. Only use authorised tools.")
print "7. Save your work to your own drive."
print()
print("Thank you for keeping the lab safe")
print("**********************************")
```

**Target output**

```text
**********************************
*        CYBER LAB RULES         *
**********************************

1. Log in with your own account.
2. Never share your password.
3. Lock your screen when you leave.
4. Report anything suspicious.
5. No food or drink near computers.
6. Only use authorised tools.
7. Save your work to your own drive.

Thank you for keeping the lab safe.
**********************************
```

**Before running**, predict how many runs it will take to get rid of every error message, and in what order the errors will be reported. Then fix it, keeping a table of each run as in Exercise 12.

**Tests:** systematic debugging of a longer program.

---

### Exercise 22 — What actually happened?

**Files:** `ex22_backup.py`, `ex22_report.py`

Imagine each `print()` line below is a real step of a backup program. Type it exactly:

```python
print("Backup started")
print("Step 1: Copied documents")
print("Step 2: Copied photos")
Print("Step 3: Copied emails")
print("Step 4: Copied settings")
print("Backup finished")
```

Run it. Then write `ex22_report.py`, which **prints** a short incident report:

```text
INCIDENT REPORT: backup program
-------------------------------
Steps that completed:   ...
Step that failed:       ...
Steps that never ran:   ...
Kind of error:          ...
Cause:                  ...
Fix:                    ...
```

Fill in each `...` yourself.

**Question:** in a real backup program, why would it be dangerous to assume the backup worked just because it started?

**Tests:** working out exactly what ran before a runtime error.

---

### Exercise 23 — Prediction challenge

**Files:** `ex23a.py` to `ex23e.py`

Harder this time. Predict the **exact** output of each, including blank lines and error messages (just the last line of each message). Then test.

**A**

```python
print()
print()
print("Done")
```

**B**

```python
print("One")
print("Two")
print("Three")
print("Four"
```

**C**

```python
print("One")
prnt("Two")
Print("Three")
print("Four")
```

**D**

```python
print("Line with a 'single' quote")
print('Line with a "double" quote')
print('Line with an apostrophe: it's')
```

**E**

```python
PRINT("Start")
print("Middle")
print("End"))
```

**Score:** out of 5. For each one you got wrong, write one sentence explaining what you misunderstood.

**Tests:** prediction with tricky cases.

---

### Exercise 24 — Make puzzles for a classmate

**Files:** `ex24_puzzle_syntax.py`, `ex24_puzzle_runtime.py`, `ex24_puzzle_logic.py`, `ex24_answers.py`

Write three puzzle programs of 5 to 8 lines each:

1. One with a **syntax error** hidden somewhere other than the first or last line.
2. One with a **runtime error** that lets **at least three** lines run first.
3. One with **two logic errors** and no error message.

Then write `ex24_answers.py`, which **prints** the answer to each puzzle: the kind of error, the line, what the output would be and how to fix it.

Check your puzzles really behave the way your answers say, by running them.

**Tests:** understanding the concept well enough to teach it.

---

### Exercise 25 — Final program: the error guide

**File:** `ex25_error_guide.py`

Write a program that prints a neat, well-laid-out **guide to Python errors** for a beginner. It must:

- have a title inside a box,
- have a section for each of the three kinds of error, with a heading and an underline,
- in each section, say **when** it is found (stage 1, stage 2 or never), **whether any output appears**, and give **one example line of code** that causes it (shown as text inside your `print()`, so your program does not break),
- end with the debugging checklist from Lecture 2, section D, in your own words,
- be at least **30 lines** of output,
- run with **no errors**.

**Tip:** to show an example of broken code as text, put it inside quotes. For example, to display `print("Hi"`, write `print('Example: print("Hi"')`. Think carefully about which quotes go on the outside.

**Tests:** everything from today, explained and displayed with Day 1 skills.

---

## Submitting for review

When you finish a level, say **"Review Day 2, Level N"** and share your files and your `predictions.md`. For each exercise you get:

- ✅ pass, or 🔁 try again
- what is wrong and **why**
- a model answer, but only after you have tried

## Progress tracker

| # | Exercise | Attempted | Reviewed |
| --- | --- | --- | --- |
| 1 | A file with no mistakes | ⬜ | ⬜ |
| 2 | Missing bracket on the last line | ⬜ | ⬜ |
| 3 | Misspelt `print` on the last line | ⬜ | ⬜ |
| 4 | Missing quote on the first line | ⬜ | ⬜ |
| 5 | Misspelt `print` on the first line | ⬜ | ⬜ |
| 6 | A syntax error in the middle | ⬜ | ⬜ |
| 7 | A runtime error in the middle | ⬜ | ⬜ |
| 8 | Sort the mistakes | ⬜ | ⬜ |
| 9 | Read the message, find the mistake | ⬜ | ⬜ |
| 10 | Spelling inside and outside the quotes | ⬜ | ⬜ |
| 11 | Which mistake is reported first? | ⬜ | ⬜ |
| 12 | Three syntax errors | ⬜ | ⬜ |
| 13 | Two runtime errors | ⬜ | ⬜ |
| 14 | Make it fail at a chosen line | ⬜ | ⬜ |
| 15 | Make it show nothing | ⬜ | ⬜ |
| 16 | Fix the welcome screen | ⬜ | ⬜ |
| 17 | Prediction sheet | ⬜ | ⬜ |
| 18 | Logic error hunt | ⬜ | ⬜ |
| 19 | Explain it in your own words | ⬜ | ⬜ |
| 20 | Match the message to the code | ⬜ | ⬜ |
| 21 | The broken lab notice | ⬜ | ⬜ |
| 22 | What actually happened? | ⬜ | ⬜ |
| 23 | Prediction challenge | ⬜ | ⬜ |
| 24 | Make puzzles for a classmate | ⬜ | ⬜ |
| 25 | Final program: the error guide | ⬜ | ⬜ |
