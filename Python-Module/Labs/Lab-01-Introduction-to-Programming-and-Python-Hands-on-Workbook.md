# Day 1 Laboratory — Introduction to Programming and Python

**Part I · Chapter 1 · Day 1** · 30 exercises · Goes with [Lecture 1](../Lectures/Lecture-01-Introduction-to-Programming-and-Python.md)

## Before you start

**What this lab covers:** running Python in the REPL and as scripts, `print()` with one or more values, `sep` and `end`, strings and quotes, escape sequences, triple quotes, string repetition with `*`, simple arithmetic inside `print()`, comments, and the three kinds of error.

**What it does not cover yet:** variables, `input()`, `if`, loops. **Do not use them**, even if you know them from Java. Every exercise can be solved with what the lecture taught. Working inside the limits is part of the training.

### Setup

1. Make sure `python3 --version` (macOS/Linux) or `py --version` (Windows) shows Python 3.
2. Work inside the `My-Solutions/Lab-01/` folder.
3. Create **one file per exercise**, named as the exercise says, for example `ex01_hello.py`.
4. Start every file with a two-line header comment:

   ```python
   # ex01_hello.py
   # Exercise 1: prints a greeting and my name.
   ```

5. Run each file from the terminal:

   ```bash
   cd Python-Module/My-Solutions/Lab-01
   python3 ex01_hello.py
   ```

### Rules that make this lab work

1. **Type every line yourself.** No copy and paste, not even from this lab.
2. **Predict, then run.** Where an exercise says *predict*, write your prediction as a comment in the file **before** running it.
3. **Match output exactly** where an exact output is given: same spelling, capitals, spaces and blank lines.
4. **Stuck?** Re-read the lecture section named in the hint, then ask for a hint. Solutions are released only after you have attempted an exercise.
5. **Submit for review** in batches (for example, after each level). An exercise is marked ✅ in `PROGRESS.md` only after review.

### Levels

| Level | Exercises | Purpose | Rough time |
| --- | --- | --- | --- |
| 1 | 1–6 | Basic understanding | 5–10 min each |
| 2 | 7–12 | Applying the concept | 10 min each |
| 3 | 13–18 | Combining operations | 10–15 min each |
| 4 | 19–24 | Problem-solving and debugging | 15–20 min each |
| 5 | 25–30 | Real-world applications and challenges | 20–45 min each |

---

## Level 1 — Basic understanding

### Exercise 1 — Hello, Python

**Level:** 1 · **File:** `ex01_hello.py`

**Problem:** write your first script.

**Requirements**

- Line 1 of output: `Hello, world!`
- Line 2 of output: `My name is <your name>.`
- Use two `print` statements.

**Expected output** (with your own name)

```text
Hello, world!
My name is Afaq.
```

**Then experiment:** run it three times. Change the text each time and save before running. What happens if you run without saving?

**Tests:** creating, saving and running a script. Basic `print()`.

---

### Exercise 2 — Exploring the REPL

**Level:** 1 · **File:** `ex02_repl_notes.py`

**Problem:** use the interactive shell and record what you find in a script.

**Requirements**

1. Open the REPL (`python3` or `py`). Type each of these and note what appears:
   - `7 + 3`
   - `"Hello"`
   - `print("Hello")`
   - `10 / 4`
   - `import this`
2. Exit the REPL.
3. In `ex02_repl_notes.py`, write a comment for each line you typed, recording what the REPL showed.
4. The script must then **print** three lines:
   - your Python version, typed as text (for example `Python version: 3.15.0`)
   - the result of `10 / 4`, calculated by Python
   - the first rule of "The Zen of Python" (the line after its title), typed as text

**Expected output** (example, your version may differ)

```text
Python version: 3.15.0
10 / 4 = 2.5
Beautiful is better than ugly.
```

**Think about:** why did `"Hello"` show quotes in the REPL but `print("Hello")` did not?

**Tests:** using the REPL, REPL versus script behaviour, getting the version.

---

### Exercise 3 — Three-line introduction

**Level:** 1 · **File:** `ex03_introduction.py`

**Requirements:** print three lines: your name, your course, and your university. Use three `print` statements, with a comment above each one saying what it prints.

**Expected output** (example)

```text
Name: Afaq Ahmad
Course: BSc (Hons) Cyber Security
University: Liverpool John Moores University
```

**Tests:** sequence, comments, string literals.

---

### Exercise 4 — Blank lines and spacing

**Level:** 1 · **File:** `ex04_blank_lines.py`

**Requirements:** produce **exactly** this output, including the two blank lines, using `print()` for the blank lines. Do not use `\n` in this exercise.

```text
SECTION 1
Introduction

SECTION 2
Main content

SECTION 3
Summary
```

**Tests:** `print()` with no arguments, careful output matching.

---

### Exercise 5 — Quotes inside quotes

**Level:** 1 · **File:** `ex05_quotes.py`

**Problem:** print text that contains quote marks.

**Requirements:** produce these three lines. Print line 1 with double quotes on the outside, line 2 with single quotes on the outside, and line 3 **twice**, once each way, using escape sequences where needed.

```text
It's my first day of Python.
My lecturer said "type every line yourself".
It's called "Python" after Monty Python.
It's called "Python" after Monty Python.
```

**Hint:** lecture section C.7, *Strings and string literals* and *Escape sequences*.

**Tests:** choosing quote types, `\'` and `\"`.

---

### Exercise 6 — Fix the capitals

**Level:** 1 · **File:** `ex06_fix_case.py`

**Problem:** this program is broken. Type it exactly as shown first.

```python
print("Line A")
Print("Line B")
PRINT("Line C")
print("Line D")
```

**Requirements**

1. **Predict** (as a comment at the top): which lines will appear before the program stops, and what kind of error will it be?
2. Run it. Record the actual last line of the traceback in a comment.
3. Fix one line, run again, record the new error, then fix the other line.
4. The final file must print all four lines and keep your prediction and recorded errors as comments.

**Tests:** case sensitivity, runtime errors, reading a traceback, the run–fix–rerun cycle.

---

## Level 2 — Applying the concept

### Exercise 7 — Separators

**Level:** 2 · **File:** `ex07_separators.py`

**Problem:** build formatted values from separate pieces.

**Requirements:** each line must be printed with **one** `print` call that receives the parts as **separate arguments** and uses `sep`. For example, the date is `print("27", "11", "2026", sep=...)`.

```text
27/11/2026
18:43:00
192.168.1.10
www.ljmu.ac.uk
ERROR|auth|failed login
```

**Restriction:** none of your strings may contain `/`, `:`, `.` or `|`. Only `sep` may supply them.

**Tests:** `sep`, thinking about how output is assembled.

---

### Exercise 8 — Staying on one line

**Level:** 2 · **File:** `ex08_progress_bar.py`

**Requirements:** use **at least six** separate `print` calls to produce this **single** line:

```text
Scanning ports [######] done
```

Each `#` (or group of them) should come from its own `print` call, as if the scan were progressing.

**Then experiment:** what changes if you forget `end=""` on one of the middle calls? Record the answer in a comment.

**Tests:** `end`, the default newline.

---

### Exercise 9 — Python as a calculator

**Level:** 2 · **File:** `ex09_calculator.py`

**Requirements:** print these lines. The text before `=` must be a string, and the answer after `=` **must be calculated by Python**, not typed.

```text
12 + 30 = 42
100 - 58 = 42
6 * 7 = 42
84 / 2 = 42.0
```

**Question** (answer in a comment): why is the last answer `42.0` and not `42`?

**Tests:** strings versus expressions, mixing them in one `print`, the `/` operator.

---

### Exercise 10 — A table with tabs

**Level:** 2 · **File:** `ex10_device_table.py`

**Requirements:** print this table using `\t` to separate the columns. Use one `print` per row.

```text
Device	IP address
Router	192.168.1.1
Laptop	192.168.1.20
Phone	192.168.1.35
Printer	192.168.1.50
```

**Then experiment:** add a device called `Smart-TV-Lounge`. What happens to the alignment, and why? Can you fix it with a second `\t` on the other rows? Record what you find.

**Tests:** `\t`, how tab stops work.

---

### Exercise 11 — The backslash trap

**Level:** 2 · **File:** `ex11_backslash_trap.py`

**Problem:** Windows file paths contain backslashes, and backslashes start escape sequences.

**Requirements**

1. **Predict** the output of `print("C:\notes\today.txt")` and write it as a comment.
2. Add that line to your file and run it. Record what really appears, and explain it, in a comment.
3. Fix it so it prints exactly `C:\notes\today.txt`.
4. Now try `print("C:\Users\afaq")`. This one does not even run. Record the error type in a comment, then fix it.
5. The final file must print, correctly:

```text
C:\notes\today.txt
C:\Users\afaq
D:\backup\2026\november
```

**Tests:** escape sequences, `\\`, syntax errors caused by escapes.

---

### Exercise 12 — Comment this program

**Level:** 2 · **File:** `ex12_comment_it.py`

**Problem:** this program works but has no comments. Type it in.

```python
print("=" * 24)
print("  LAB BOOKING SYSTEM")
print("=" * 24)
print("Room:", "Byrom Street 1.23")
print("Date:", "Monday")
print("Old room:", "James Parsons 2.10")
print("Status:", "Confirmed")
print("=" * 24)
```

**Requirements**

1. Add a header comment (file name and purpose).
2. Add comments that explain **why** each section exists (title, details, footer), not ones that just repeat the code.
3. The "Old room" line is no longer wanted. **Comment it out** instead of deleting it.
4. Add one inline comment explaining why the divider uses `"=" * 24`.

**Tests:** writing useful comments, commenting out code.

---

## Level 3 — Combining operations

### Exercise 13 — Business card

**Level:** 3 · **File:** `ex13_business_card.py`

**Requirements:** print a business card for yourself, framed with a border.

- The top and bottom borders must be made with string repetition (`"*" * ...`), not typed out.
- At least four lines of details: name, course, email (invent one) and one interest.
- Use `\t` or spaces to indent the details inside the frame.

**Example**

```text
********************************
	AFAQ AHMAD
	Cyber Security Student
	afaq@example.com
	Interest: Linux and networks
********************************
```

**Challenge:** make the right-hand side of the frame line up too (`*` at both ends of every line). You will need to count characters.

**Tests:** string repetition, escapes, planning output layout.

---

### Exercise 14 — Shapes with repetition

**Level:** 3 · **File:** `ex14_shapes.py`

**Requirements:** using string repetition, and `+` to join two strings, print a right-angle triangle, then a blank line, then a centred pyramid.

```text
*
**
***
****
*****

    *
   ***
  *****
 *******
*********
```

**Restriction:** no string in your code may contain more than one `*` or more than one space. Repetition must do the work.

**Hint:** each pyramid row is some spaces followed by some stars. Work out the two numbers for each row on paper first. What pattern do you see?

**Tests:** `*` and `+` on strings, spotting a pattern (an early taste of algorithmic thinking).

---

### Exercise 15 — Same output, three ways

**Level:** 3 · **File:** `ex15_three_ways.py`

**Problem:** produce this block of output three separate times, each time a different way.

```text
Name: Ada Lovelace
Born: 1815
Known for: notes on the Analytical Engine
```

**Requirements**

- **Way 1:** three `print` calls.
- **Way 2:** **one** `print` call with **one** ordinary string, using `\n`. No triple quotes.
- **Way 3:** **one** `print` call with **three** separate string arguments and a `sep` value.
- Print a line of 20 dashes between each version.
- In a comment, say which way you think is most readable, and why.

**Tests:** `\n`, `sep`, recognising that one problem has many correct solutions.

---

### Exercise 16 — Unit converter (fixed values)

**Level:** 3 · **File:** `ex16_unit_converter.py`

**Problem:** 1 mile is exactly 1.609344 km. Print a small conversion table where **every converted value is calculated by Python**.

**Expected output**

```text
--- Distance converter ---
1 mile = 1.609344 km
5 miles = 8.04672 km
Marathon (26.2 miles) = 42.1648128 km
10 km = 6.2137119223733395 miles
```

**Hint:** km → miles means dividing by 1.609344.

**Question** (comment): the last answer has a lot of decimal places. Is that a bug in your program? What would a real user prefer to see? (You will learn to fix this in Chapter 8.)

**Tests:** arithmetic expressions inside `print`, multiplication versus division, critically reading output.

---

### Exercise 17 — Receipt, version 2

**Level:** 3 · **File:** `ex17_receipt_v2.py`

**Problem:** extend the lecture's receipt (Demo 12) to three items.

**Requirements**

- Items: Coffee £2.40, Sandwich £3.75, Cookie £1.20.
- A title, dividers made with repetition, one line per item, and a total **calculated by Python** from the three prices.
- Run it and look **very** closely at the total.

**What you should discover:** the total is not displayed as `7.35`. In a comment, record exactly what it shows. This is not a bug in your code. It is how computers store decimal numbers, and Chapter 7 explains why. For now, write down what you think a customer would think if they saw it, and why this matters in real software (banking, for example).

**Tests:** combining every output feature so far, noticing surprising output, floating-point awareness.

---

### Exercise 18 — Prediction drill

**Level:** 3 · **File:** `ex18_predict.py`

**Problem:** type these lines in exactly. **Before running**, write your predicted output for each one as a comment directly above it. Show spaces as `·` in your prediction if that helps.

```python
print("A", "B", sep="")
print("A", "B", sep="", end="")
print("C")
print("1", "2", "3", sep=" > ")
print("x", "y", sep="\n", end="\n\n")
print("done")
print("[", "OK", "]")
print("[", "OK", "]", sep="")
print("Total:", 3 + 4, "items")
print("3 + 4", "=", 3 + 4)
```

Then run it. For every prediction that was wrong, add a comment: **what you predicted, what happened, and why.**

**Tests:** precise mental model of `sep`, `end` and expressions. This is the habit of predicting output.

---

## Level 4 — Problem-solving and debugging

### Exercise 19 — Fix the syntax errors

**Level:** 4 · **File:** `ex19_fix_syntax.py`

**Problem:** this program contains **five** syntax errors. Type it in exactly as shown, errors included.

```python
# Student welcome message
print("Welcome to LJMU"
print('Your course: Cyber Security")
print("Building: "Byrom Street"")
 print("Induction week starts on Monday")
print "Good luck!"
```

**Requirements**

1. Run it. Python reports **only one** syntax error at a time. Record that error message as a comment.
2. Fix **only** that error and run again. Repeat until it works.
3. Number your comments so the file ends up with a log of all five errors and each fix.
4. Final output:

```text
Welcome to LJMU
Your course: Cyber Security
Building: "Byrom Street"
Induction week starts on Monday
Good luck!
```

**Watch out:** the first error Python reports may **not** be the first mistake in the file. Python reads the file in stages, and some mistakes (like a broken string) are caught in an earlier stage than others (like a missing bracket). Record the order in which Python actually reports them.

**Questions** (comments): why does Python show one syntax error at a time? Why does even `Welcome to LJMU` never print until every error is fixed?

**Tests:** reading `SyntaxError` and `IndentationError` messages, fixing systematically.

---

### Exercise 20 — The great error experiment

**Level:** 4 · **Files:** `ex20a_runtime.py` and `ex20b_syntax.py`

**Problem:** prove for yourself the difference between runtime and syntax errors.

**Requirements**

1. In `ex20a_runtime.py`, write six `print` statements labelled `Step 1` to `Step 6`. Make **Step 4** a `NameError` by misspelling `print` as `prnt`.
2. In `ex20b_syntax.py`, write the same six statements, but this time make **Step 4** a syntax error by leaving off its closing bracket.
3. **Predict** for each file which steps will print. Write your predictions as comments, then run both.
4. In a comment at the bottom of `ex20b_syntax.py`, explain the difference in what happened, using the words **compile**, **bytecode** and **run**.

**Tests:** the compile-then-run model of Python from lecture section C.4.

---

### Exercise 21 — Text plus number

**Level:** 4 · **File:** `ex21_type_error.py`

**Problem:** this line fails:

```python
print("Total devices: " + 7)
```

**Requirements**

1. Run it and record the error type and message in a comment.
2. Explain in your own words, in a comment, what `concatenate`, `str` and `int` mean in the message.
3. Write **two different** corrected versions that both print `Total devices: 7`.
4. Write a third line that prints `Total devices: 7` where the `7` is **calculated** as `4 + 3`. Which of your two fixes works for this, and why does the other one not?

**Tests:** `TypeError`, `+` on strings versus numbers, choosing the right fix.

---

### Exercise 22 — The wrong average

**Level:** 4 · **File:** `ex22_average.py`

**Problem:** a student wants the average of their three marks: 64, 71 and 58. Their program is:

```python
print("Average mark:", 64 + 71 + 58 / 3)
```

**Requirements**

1. Work out the correct average **by hand** first (to two decimal places). Write it in a comment.
2. Run the program. Write what it actually printed in a comment.
3. What kind of error is this: syntax, runtime or logic? Explain how you know.
4. Explain what Python actually calculated. (Hint: which operation happens first in normal maths?)
5. Fix it so it prints the right average.

**Tests:** spotting logic errors by checking against an expected answer, operator order (a preview of Chapter 11).

---

### Exercise 23 — Trace table

**Level:** 4 · **File:** `ex23_trace.py`

**Problem:** read this program **without running it**.

```python
print("Start", end=" | ")
print("A", "B", sep="-", end=" | ")
print()
print("Two\tTabs\there")
print("=" * 3 + ">", "Go")
# print("Hidden")
print("End", end="!\n")
```

**Requirements**

1. In a comment block at the top of your file, build a trace table with the columns **Line**, **What happens** and **Output after this line**.
2. Write the complete predicted output.
3. Then type the program below your comments and run it. Mark each line of your trace ✓ (correct) or ✗ (wrong) and explain each ✗.

**Tests:** tracing execution step by step, which is the core skill for reading any program.

---

### Exercise 24 — From algorithm to program

**Level:** 4 · **File:** `ex24_algorithm.py`

**Problem:** programming starts with precise steps. Here is a vague algorithm for resetting a forgotten password:

```text
1. Go to the website.
2. Reset your password.
3. Log in.
```

**Requirements**

1. In comments, list **at least three** questions a literal-minded computer (or a confused new user) would ask about these steps.
2. Rewrite the algorithm, in comments, as **at least eight** precise numbered steps that answer those questions.
3. Write a program that prints your improved algorithm as a neat, numbered help page, with a title and dividers made by repetition.

**Example start of output**

```text
====================================
  HOW TO RESET YOUR PASSWORD
====================================
Step 1: Open a web browser.
Step 2: ...
```

**Tests:** decomposition, precision, thinking like a programmer (lecture section C.1).

---

## Level 5 — Real-world applications and challenges

### Exercise 25 — Linux boot screen

**Level:** 5 · **File:** `ex25_boot_screen.py`

**Problem:** simulate the start-up messages of a Linux server.

**Requirements**

- An ASCII-art banner made with triple quotes, showing a server name you invent.
- At least eight service lines, in the form `[  OK  ] Started <service>.`
- At least one `[FAILED]` line, followed by an indented hint line starting with `\t`.
- One line printed piece by piece with `end=""`, for example `Checking disks.....done`.
- A summary line where the number of services is **calculated**, for example `Services started: 8 of 9`, with 8 and 9 written as sums such as `5 + 3`.

**Example extract**

```text
[  OK  ] Started Network Manager.
[  OK  ] Started OpenSSH server daemon.
[FAILED] Failed to start Apache web server.
	See 'systemctl status apache2' for details.
Checking disks.....done
```

**Tests:** everything from Day 1, combined into a realistic output. Planning a larger program.

---

### Exercise 26 — Security alert banner

**Level:** 5 · **File:** `ex26_security_alert.py`

**Problem:** the IT security team wants a terminal message warning students about a phishing email.

**Requirements**

- A bordered header with the word `SECURITY ALERT`, made with repetition.
- A short description of the (fictional) phishing email: sender, subject line in quotes, and what it asks for.
- A numbered list of at least four "What you should do" steps.
- A line with a fake reporting address and a Windows path to a guidance document, printed correctly with backslashes.
- At least one line using `sep` and one using `end`.
- A footer.
- Clear header and section comments in your code.

**Tests:** quotes, escapes, layout, writing output for a real audience.

---

### Exercise 27 — Weekly timetable

**Level:** 5 · **File:** `ex27_timetable.py`

**Requirements**

- Print a Monday-to-Friday timetable (real or invented) as a table with columns **Day**, **Time** and **Activity**, aligned with `\t`.
- Include at least seven rows, a header row and a divider under the header.
- At the end, print `Total study hours:` with a value **calculated** from your timetable (for example `3 + 2 + 4`).
- Print `Average per day:` calculated as total divided by 5.

**Tests:** tables, tab alignment with uneven text lengths, calculations inside `print`.

---

### Exercise 28 — Network inventory report

**Level:** 5 · **File:** `ex28_network_report.py`

**Problem:** a lab network has two subnets. Produce an inventory report.

**Requirements**

- Title block with the report date built with `sep` (as in Exercise 7).
- **Subnet A** section: at least four devices with hostname, IP address and role, tab-aligned.
- **Subnet B** section: at least three devices in the same layout.
- A summary that prints the device count of each subnet and the **calculated** total.
- A "Notes" section written as a single triple-quoted string over at least three lines.
- Use the private address ranges `192.168.x.x` or `10.x.x.x` only.

**Tests:** structuring a longer program into sections, consistent layout.

---

### Exercise 29 — A `--help` screen

**Level:** 5 · **File:** `ex29_help_screen.py`

**Problem:** command-line tools print a help screen when run with `--help`. Recreate one for an imaginary tool called `logcheck`.

**Expected shape** (exact contents are up to you)

```text
Usage: logcheck [OPTIONS] FILE

Scan a log file for failed login attempts.

Options:
  -h, --help          Show this message and exit.
  -v, --verbose       Show every matching line.
  -o, --output PATH   Save the report to PATH.
  -n, --top N         Show the N most frequent IP addresses.

Examples:
  logcheck /var/log/auth.log
  logcheck -n 5 -o report.txt "C:\logs\security.log"
```

**Requirements**

- At least four options and two examples.
- The options must line up in columns.
- At least one example containing a Windows path and quotes, printed correctly.
- Use at least two different techniques from today (for example triple quotes for one section, separate `print`s for another), and say in a comment why you chose each.

**Tests:** precise text layout, escapes inside realistic content, professional conventions.

---

### Exercise 30 — Capstone: "About me" program

**Level:** 5 · **File:** `ex30_capstone.py`

**Problem:** write a complete, well-organised program that introduces you and your learning plan. This is the Day 1 mini-project.

**Requirements**

Your program must:

1. Produce **at least 25 lines** of output.
2. Start with a header comment: file name, author, date and a one-sentence description.
3. Be divided into **at least four sections** (for example: banner, about me, my modules, my Python plan, footer), each with a section comment.
4. Use **every** one of these at least once, and label each with a comment such as `# uses: sep`:
   - `print()` for a blank line
   - several arguments in one `print`
   - `sep`
   - `end`
   - `\n`
   - `\t`
   - an escaped quote (`\"` or `\'`)
   - `\\`
   - a triple-quoted string
   - string repetition
   - string joining with `+`
   - at least **three** calculations, such as weeks remaining in the semester, hours of Python per week, or days until a deadline
5. Contain one commented-out line, with a comment explaining why it is switched off.
6. Run with **no errors**, and contain **no logic errors**. Check every calculation by hand and write the hand-worked answer in a comment next to it.

**Self-check before submitting**

- [ ] 25+ lines of output
- [ ] Header comment complete
- [ ] Four or more commented sections
- [ ] Every feature in the list used and labelled
- [ ] Three or more calculations, each hand-checked in a comment
- [ ] One commented-out line, with a reason
- [ ] Output is tidy and aligned
- [ ] No variables, `input()`, `if` or loops (they are not taught yet)

**Tests:** everything in Chapter 1, plus planning, organisation and self-checking.

---

## Extension (optional, for fast finishers)

These are not required, but they stretch you.

- **E1.** Find out what `\a` does in a string. Try it in your terminal. Does it work everywhere?
- **E2.** In the REPL, type `help(print)`. Read it, and find one setting of `print` the lecture did not mention. What do you think it does? (Press `q` to quit the help screen.)
- **E3.** Make Exercise 14's pyramid twice as tall (ten rows). Did you have to think about each row separately, or did you spot a rule? Write the rule in plain English. Loops (Chapter 22) will let Python apply it for you.
- **E4.** Research one Python tool used in cybersecurity (Scapy, Volatility or Impacket) and print a five-line summary of what it does. Use the official project page as your source and include its link in the output.

---

## Submitting for review

When you finish a level, say **"Review Day 1, Level N"** and share your files (paste them, or commit and push them to this repository). For each exercise you will get:

- ✅ pass, or 🔁 revise
- syntax, logic or style issues, with **why** they matter
- an improved or alternative solution, **after** you have attempted it
- a short note on what to practise

Reference solutions go in `Reference-Solutions/Lab-01/` only after review.

## Progress tracker

Copy this into `PROGRESS.md` as you go, or tick it here.

| # | Exercise | Attempted | Reviewed |
| --- | --- | --- | --- |
| 1 | Hello, Python | ⬜ | ⬜ |
| 2 | Exploring the REPL | ⬜ | ⬜ |
| 3 | Three-line introduction | ⬜ | ⬜ |
| 4 | Blank lines and spacing | ⬜ | ⬜ |
| 5 | Quotes inside quotes | ⬜ | ⬜ |
| 6 | Fix the capitals | ⬜ | ⬜ |
| 7 | Separators | ⬜ | ⬜ |
| 8 | Staying on one line | ⬜ | ⬜ |
| 9 | Python as a calculator | ⬜ | ⬜ |
| 10 | A table with tabs | ⬜ | ⬜ |
| 11 | The backslash trap | ⬜ | ⬜ |
| 12 | Comment this program | ⬜ | ⬜ |
| 13 | Business card | ⬜ | ⬜ |
| 14 | Shapes with repetition | ⬜ | ⬜ |
| 15 | Same output, three ways | ⬜ | ⬜ |
| 16 | Unit converter | ⬜ | ⬜ |
| 17 | Receipt, version 2 | ⬜ | ⬜ |
| 18 | Prediction drill | ⬜ | ⬜ |
| 19 | Fix the syntax errors | ⬜ | ⬜ |
| 20 | The great error experiment | ⬜ | ⬜ |
| 21 | Text plus number | ⬜ | ⬜ |
| 22 | The wrong average | ⬜ | ⬜ |
| 23 | Trace table | ⬜ | ⬜ |
| 24 | From algorithm to program | ⬜ | ⬜ |
| 25 | Linux boot screen | ⬜ | ⬜ |
| 26 | Security alert banner | ⬜ | ⬜ |
| 27 | Weekly timetable | ⬜ | ⬜ |
| 28 | Network inventory report | ⬜ | ⬜ |
| 29 | A `--help` screen | ⬜ | ⬜ |
| 30 | Capstone: "About me" program | ⬜ | ⬜ |
