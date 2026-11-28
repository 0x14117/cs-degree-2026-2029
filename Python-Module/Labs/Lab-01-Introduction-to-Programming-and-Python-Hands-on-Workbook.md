# Day 1 Laboratory — Showing Text with `print()`

**Part I · Chapter 1 · Day 1** · 25 exercises · Goes with [Lecture 1](../Lectures/Lecture-01-Introduction-to-Programming-and-Python.md)

## Before you start

**Today's one skill:** showing text on the screen with `print()`.

**You may use only:**

- `print("some text")` with double quotes
- `print('some text')` with single quotes
- `print()` for a blank line

**Do not use** anything else, even if you have seen it online: no maths, no `+`, no `*`, no `sep` or `end`, no `\n`, no `#` comments, no `input()`. Every exercise can be done with the three things above. If you catch yourself using something else, rewrite it.

### How to work

1. Make the folder `My-Solutions/Lab-01/` if it does not exist. Save every exercise there as its own file, named as the exercise says.
2. Run each file from that folder:

   ```bash
   python3 ex01_hello.py      # macOS / Linux
   python ex01_hello.py       # Windows (or: py ex01_hello.py)
   ```

3. **Type everything yourself.** No copy and paste.
4. **Predict before you run.** Where an exercise says *predict*, write your prediction down first (on paper, or in a file called `predictions.md`).
5. **Match the target output exactly**: same spelling, capitals, spaces and blank lines.
6. **Stuck?** Re-read the lecture section in the hint, then ask for a hint. A full solution is only shown after you have tried.
7. **Submit after each level** for review. Exercises are only marked done after review.

### Levels

| Level | Exercises | What it is for |
| --- | --- | --- |
| 1 | 1–5 | Your first `print()` lines |
| 2 | 6–10 | Quotes, exact text and blank lines |
| 3 | 11–15 | Longer programs and lined-up layouts |
| 4 | 16–20 | Fixing mistakes and predicting output |
| 5 | 21–25 | Realistic screens and a final program |

---

## Level 1 — Your first `print()` lines

### Exercise 1 — Hello, world

**File:** `ex01_hello.py`

Write a program that shows exactly:

```text
Hello, world!
```

Then change it to show `Hello, Python!` and run it again. Then change it back.

**Hint:** Lecture 1, C.4. **Tests:** creating, saving and running a file.

---

### Exercise 2 — Your name

**File:** `ex02_my_name.py`

Write a program that shows your own name on one line, for example:

```text
Afaq Ahmad
```

**Tests:** one `print()` with your own text.

---

### Exercise 3 — Three facts

**File:** `ex03_three_facts.py`

Show three lines about yourself: your name, your course and your university.

**Example output**

```text
My name is Afaq Ahmad.
I study BSc Cyber Security.
I study at LJMU.
```

**Tests:** several `print()` lines run in order.

---

### Exercise 4 — Single quotes

**File:** `ex04_single_quotes.py`

Show the same three lines as Exercise 3, but this time use **single quotes** in every `print()`.

**Question:** is the output any different? Write your answer in `predictions.md`.

**Hint:** Lecture 1, C.7. **Tests:** both kinds of quote do the same job.

---

### Exercise 5 — A blank line

**File:** `ex05_blank_line.py`

Show exactly this, including the empty line in the middle:

```text
Good morning.

Time to code.
```

**Hint:** Lecture 1, C.9. **Tests:** `print()` with nothing inside.

---

## Level 2 — Quotes, exact text and blank lines

### Exercise 6 — Apostrophes

**File:** `ex06_apostrophes.py`

Show exactly:

```text
It's Monday.
I'm at university today.
Don't forget your student card.
```

**Hint:** each line contains a `'`, so which quotes must go on the outside? **Tests:** choosing the right quotes.

---

### Exercise 7 — Quotes inside the text

**File:** `ex07_quotes_inside.py`

Show exactly:

```text
My tutor said "practise every day".
The sign said "Lab 2 is closed".
```

**Hint:** Lecture 1, C.7 table. **Tests:** single quotes outside, double quotes inside.

---

### Exercise 8 — Capitals and spaces

**File:** `ex08_exact.py`

**Predict** what each line shows, then run it:

```python
print("python")
print("PYTHON")
print("PyThOn")
print("p y t h o n")
print("      python")
```

**Question:** the last line has spaces inside the quotes. Why is that allowed, when a space **before** `print` is not?

**Hint:** Lecture 1, C.8 and rule 5. **Tests:** text is shown exactly as typed.

---

### Exercise 9 — Spacing it out

**File:** `ex09_spacing.py`

Show exactly this. There are **two** empty lines between `Chapter 1` and `Chapter 2`:

```text
Chapter 1
Programs are lists of instructions.


Chapter 2
Python runs them from top to bottom.
```

**Tests:** using several `print()` lines for blank space.

---

### Exercise 10 — Punctuation

**File:** `ex10_punctuation.py`

Show exactly:

```text
Wait... what?!
Cost: £5 (cash only)
Email: student@ljmu.ac.uk
50% done -> keep going!
```

**Question:** did Python change any of the symbols? Why not?

**Tests:** any character inside quotes is just text.

---

## Level 3 — Longer programs and lined-up layouts

### Exercise 11 — Address label

**File:** `ex11_address_label.py`

Show a parcel address label (use a made-up address):

```text
TO:
Mr A. Student
12 Example Street
Liverpool
L1 1AA
United Kingdom
```

**Tests:** a longer sequence of `print()` lines.

---

### Exercise 12 — Café menu

**File:** `ex12_menu.py`

Show this menu. Use **spaces inside the quotes** to line up the prices:

```text
CAMPUS CAFE MENU

Tea          £1.20
Coffee       £2.50
Sandwich     £3.75
Soup         £3.10
```

**Hint:** count the characters. Each price starts in the same column. **Tests:** lining up text with spaces.

---

### Exercise 13 — Weekly timetable

**File:** `ex13_timetable.py`

Show your university week. Use your real days (Monday, Tuesday and Friday) or make one up. Line up the second column with spaces:

```text
MY WEEK
-------
Monday      University
Tuesday     University
Wednesday   Study and work
Thursday    Study and work
Friday      University
```

**Tests:** headings, underlines and lined-up columns.

---

### Exercise 14 — A box

**File:** `ex14_box.py`

Draw this box exactly. Every line is **20 characters** wide:

```text
+------------------+
|                  |
|   CYBER LAB 1    |
|                  |
+------------------+
```

**Then experiment:** delete one space from the middle line and run it. What happens to the right-hand side? Put the space back.

**Hint:** Lecture 1, C.10 and Example 6. **Tests:** counting characters.

---

### Exercise 15 — The tea algorithm

**File:** `ex15_tea.py`

Show the full tea algorithm from Lecture 1, C.1, as a numbered list with a title and a blank line after the title:

```text
HOW TO MAKE TEA

1. Boil the kettle.
2. Put a tea bag in the cup.
3. Pour the water into the cup.
4. Wait 3 minutes.
5. Take out the tea bag.
```

**Then:** add **two more steps** of your own at the end (for example, adding milk), so the algorithm is more exact.

**Tests:** turning an algorithm into a program.

---

## Level 4 — Fixing mistakes and predicting output

### Exercise 16 — Fix the broken lines

**File:** `ex16_fix_me.py`

Each line below has **one** mistake. Type all six into your file **with the mistakes**, then run it and read the error. Fix **only the line the error points at**, run again, and repeat until the program works.

```python
Print("Line one")
print("Line two"
print("Line three)
print('Line four")
print(Line five)
print "Line six"
```

**Target output**

```text
Line one
Line two
Line three
Line four
Line five
Line six
```

**Write down** each error message you saw, and what fixed it, in `predictions.md`.

**Notice:** the errors will **not** come in order from line 1 to line 6, and some lines are reported before line 1 is. That is normal. Write down the order you saw. Day 2 explains why it happens.

**Hint:** Lecture 1, section G. **Tests:** recognising and fixing the common mistakes.

---

### Exercise 17 — Wrong quotes

**File:** `ex17_wrong_quotes.py`

These two lines are broken. **Predict** why, then fix each one in **two different ways**: once by changing the outer quotes, and once by rewording the text so the problem character is not needed.

```python
print('I can't come today.')
print("Press "Enter" to continue.")
```

**Tests:** understanding why matching quotes matter.

---

### Exercise 18 — Put it in order

**File:** `ex18_order.py`

This program logs into a computer, but the steps are mixed up. Type it, run it, then **move the lines** so the steps come out in the correct order. Do not change any text.

```python
print("4. Open your files")
print("2. Type your username")
print("1. Switch on the computer")
print("5. Log out when finished")
print("3. Type your password")
```

**Question:** Python gave no error message. Why not? Was the program "wrong"?

**Hint:** Lecture 1, C.2 and Example 7. **Tests:** sequence.

---

### Exercise 19 — Predict the output

**File:** `ex19_predict.py`

**Before typing anything**, write down exactly what this program will show, including blank lines:

```python
print("A")
print()
print("B")
print("C")
print()
print()
print("  D")
```

Then type it, run it and compare. How many lines of output were there in total, counting blank ones?

**Tests:** reading code and predicting output.

---

### Exercise 20 — Copy the target

**File:** `ex20_copy_target.py`

Write a program that shows **exactly** this. Look carefully at the capitals, spaces and blank lines:

```text
  WARNING

Do NOT share your password.
  Not with friends.
  Not with "IT support" on the phone.

Stay safe online.
```

**Tests:** precision. Every character must match.

---

## Level 5 — Realistic screens and a final program

### Exercise 21 — Login screen

**File:** `ex21_login_screen.py`

Make a text login screen for a made-up company, **Northgate Systems**. It must have a border at the top and bottom, the company name, a blank line, two lines `Username:` and `Password:`, a blank line, and a warning line. For example:

```text
==================================
        NORTHGATE SYSTEMS
==================================

Username:
Password:

Authorised users only.
==================================
```

You cannot type into it yet (that comes in Chapter 10). Today you are only designing what it looks like.

**Tests:** planning a screen layout.

---

### Exercise 22 — Security alert banner

**File:** `ex22_alert.py`

Show a security alert box like this, with every line the same width:

```text
**************************************
*                                    *
*   SECURITY ALERT                   *
*   Unusual login from new device    *
*   Time: 02:14                      *
*                                    *
**************************************
```

**Hint:** count the width of the top line first, then make every other line match it. **Tests:** careful alignment.

---

### Exercise 23 — Computer start-up messages

**File:** `ex23_boot.py`

When a Linux computer starts, it shows lines like these. Make a program that shows at least **eight** start-up lines in this style:

```text
[  OK  ] Started Network Manager.
[  OK  ] Started Firewall.
[  OK  ] Reached target Login Prompts.
[FAILED] Failed to start Printer Service.
```

Include at least one `[FAILED]` line, then a blank line, then `Welcome to Ubuntu`.

**Tests:** consistent formatting over a longer program.

---

### Exercise 24 — A help screen

**File:** `ex24_help.py`

Command-line tools show a help screen when you ask for help. Make one for a made-up tool called `logscan`:

```text
logscan - search log files for problems

Usage:
  logscan FILE
  logscan --help

Options:
  --failed     show failed logins only
  --today      show today's entries only
  --help       show this help message

Example:
  logscan auth.log --failed
```

Keep the option descriptions lined up.

**Tests:** a realistic, neatly laid-out program.

---

### Exercise 25 — Final program: about me

**File:** `ex25_about_me.py`

Write a program that introduces you. It must:

- start with a title inside a box (at least 3 lines),
- have **three** sections with headings: `ABOUT ME`, `MY COURSE` and `MY GOALS`, each followed by an underline made of `-` characters,
- have at least two lines under each heading,
- use at least one line with an apostrophe and one with double quotes in the text,
- have a blank line between sections,
- end with a closing border line,
- be at least **20 lines** of output.

**Tests:** everything from today in one program.

---

## Submitting for review

When you finish a level, say **"Review Day 1, Level N"** and share your files (paste them, or push them to the repository). For each exercise you get:

- ✅ pass, or 🔁 try again
- what is wrong and **why**
- a model answer, but only after you have tried

## Progress tracker

| # | Exercise | Attempted | Reviewed |
| --- | --- | --- | --- |
| 1 | Hello, world | ⬜ | ⬜ |
| 2 | Your name | ⬜ | ⬜ |
| 3 | Three facts | ⬜ | ⬜ |
| 4 | Single quotes | ⬜ | ⬜ |
| 5 | A blank line | ⬜ | ⬜ |
| 6 | Apostrophes | ⬜ | ⬜ |
| 7 | Quotes inside the text | ⬜ | ⬜ |
| 8 | Capitals and spaces | ⬜ | ⬜ |
| 9 | Spacing it out | ⬜ | ⬜ |
| 10 | Punctuation | ⬜ | ⬜ |
| 11 | Address label | ⬜ | ⬜ |
| 12 | Café menu | ⬜ | ⬜ |
| 13 | Weekly timetable | ⬜ | ⬜ |
| 14 | A box | ⬜ | ⬜ |
| 15 | The tea algorithm | ⬜ | ⬜ |
| 16 | Fix the broken lines | ⬜ | ⬜ |
| 17 | Wrong quotes | ⬜ | ⬜ |
| 18 | Put it in order | ⬜ | ⬜ |
| 19 | Predict the output | ⬜ | ⬜ |
| 20 | Copy the target | ⬜ | ⬜ |
| 21 | Login screen | ⬜ | ⬜ |
| 22 | Security alert banner | ⬜ | ⬜ |
| 23 | Computer start-up messages | ⬜ | ⬜ |
| 24 | A help screen | ⬜ | ⬜ |
| 25 | Final program: about me | ⬜ | ⬜ |
