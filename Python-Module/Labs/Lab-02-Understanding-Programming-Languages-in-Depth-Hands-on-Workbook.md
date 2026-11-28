# Day 2 Laboratory — Understanding Programming Languages in Depth

**Part I · Chapter 2 · Day 2** · 30 exercises · Goes with [Lecture 2](../Lectures/Lecture-02-Understanding-Programming-Languages-in-Depth.md)

## Before you start

**What this lab covers:** asking Python about itself with `sys` and `platform`, disassembling code with `dis`, reading stack-machine bytecode, constant folding, `compile()` and `exec()`, the tokenizer and AST tools, `.pyc` files and `__pycache__`, compile-time versus run-time errors, comparing Python with Java and C, and the security consequences of bytecode.

**What you may use:** everything from Day 1 (`print()`, strings, `sep`, `end`, escape sequences, `*` repetition, arithmetic, comments), plus today's new tools: `import`, `dis.dis()`, `compile()`, `exec()`, `sys` and `platform` values, and the terminal commands `-m dis`, `-m tokenize`, `-m ast`, `-m py_compile`, `-m timeit`, `-c` and `-B`.

**What it does not cover yet:** variables, `input()`, `if`, loops, functions. **Do not use them.** Every exercise can be solved without them.

**Prerequisite:** the Day 1 lab. If you have not yet submitted Lab 1 for review, do that first. Today's exercises assume you are comfortable with `print()`.

### Setup

1. Check your version: `python3 --version` (macOS/Linux) or `py --version` (Windows). **Write it down.** Many outputs today depend on it.
2. Work inside the `My-Solutions/Lab-02/` folder. One file per exercise, named as the exercise says.
3. Start every file with the two-line header comment, as on Day 1:

   ```python
   # ex01_which_python.py
   # Exercise 1: prints facts about the Python interpreter running this file.
   ```

4. Run files from that folder:

   ```bash
   cd Python-Module/My-Solutions/Lab-02
   python3 ex01_which_python.py
   ```

   On Windows, replace `python3` with `py` everywhere in this lab.

5. **Java (Exercises 16 and 23):** you have Java from 4300COMP. Check with `javac -version`.
6. **C (Exercise 17):** you need `gcc`. On Linux or WSL: `gcc --version`. On macOS, running `gcc` offers to install the command-line tools. On Windows without WSL, use an LJMU lab machine or the alternative route given in the exercise.

### Rules that make this lab work

1. **Type every line yourself.** No copy and paste, including the listings in this lab.
2. **Predict, then run.** Where an exercise says *predict*, write your prediction as a comment **before** running.
3. **Your bytecode may differ.** The listings in this lab come from Python 3.13. On 3.14 or newer, some instruction names differ (see Lecture 2, C.5). When that happens, write down the difference as a comment. That is part of the learning, not a failure.
4. **Ignore the left-hand line numbers when comparing listings.** Your files start with header comments, so your code is on different lines. Compare the instructions.
5. **Stuck?** Re-read the lecture section in the hint, then ask for a hint. Solutions are released only after you have attempted an exercise.
6. **Submit in batches** (after each level). An exercise is marked ✅ in `PROGRESS.md` only after review.

### Levels

| Level | Exercises | Purpose | Rough time |
| --- | --- | --- | --- |
| 1 | 1–6 | Basic understanding | 5–10 min each |
| 2 | 7–12 | Applying the concept | 10–15 min each |
| 3 | 13–18 | Combining operations | 15–20 min each |
| 4 | 19–24 | Problem-solving and debugging | 15–25 min each |
| 5 | 25–30 | Real-world applications and challenges | 20–45 min each |

---

## Level 1 — Basic understanding

### Exercise 1 — Which Python am I?

**Level:** 1 · **File:** `ex01_which_python.py`

**Problem:** write a script that reports on the interpreter that is running it.

**Requirements**

- Import `sys` and `platform` at the top, one per line.
- Print a heading line `INTERPRETER REPORT`, then a line of 30 `=` characters made with `*`.
- Print these five facts, each with a label: the full version (`sys.version`), the implementation name (`platform.python_implementation()`), the C compiler CPython was built with (`platform.python_compiler()`), the cache tag (`sys.implementation.cache_tag`) and the path of the Python program (`sys.executable`).
- Line the values up neatly using spaces or `\t`.

**Example output** (yours will show your own values)

```text
INTERPRETER REPORT
==============================
Version:         3.13.18 (main, Oct 26 2026, 14:08:19) [Clang 23.1.3 ]
Implementation:  CPython
Built with:      Clang 23.1.3
Cache tag:       cpython-313
Program:         /usr/local/bin/python3
```

**Then:** add a comment at the bottom explaining in one sentence what "Built with" tells you about how your interpreter itself was made.

**Hint:** Lecture 2, Demo 1. Values like `sys.version` have no brackets; functions like `platform.python_compiler()` do.

**Tests:** `import`, the dot notation, the idea that CPython is a compiled C program.

---

### Exercise 2 — First disassembly, annotated

**Level:** 1 · **File:** `ex02_first_dis.py`

**Problem:** disassemble one line of code and explain every instruction.

**Requirements**

- Use `dis.dis()` to disassemble the code `print("Hello, bytecode")`. Remember the code must be **a string**.
- Run it. Then, **below** the `dis.dis(...)` line, add one comment line per instruction in your output, explaining what it does in your own words. Use the word *stack* at least twice.

**Expected output** (Python 3.13)

```text
  0           RESUME                   0

  1           LOAD_NAME                0 (print)
              PUSH_NULL
              LOAD_CONST               0 ('Hello, bytecode')
              CALL                     1
              RETURN_VALUE
```

**Question to answer in a comment:** the text `Hello, bytecode` does not appear as a line of output on its own. Why not?

**Hint:** Lecture 2, C.5. Quotes inside quotes: `dis.dis('print("...")')`.

**Tests:** using `dis`, reading the stack machine.

---

### Exercise 3 — Language profile table

**Level:** 1 · **File:** `ex03_language_table.py`

**Problem:** print a table classifying six languages.

**Requirements**

- Columns: `Language`, `Translation`, `Typing`, `Memory`.
- Rows: Python (CPython), Java, C, JavaScript, Rust, Bash.
- Use `\t` between columns. Use `-` repeated with `*` for a line under the header.
- For Rust and Bash, you will need to apply the lecture's categories yourself: Rust is compiled ahead of time and statically typed, and it manages memory with ownership rules. Bash is read and run line by line by the shell.

**Example of the first rows**

```text
Language        Translation             Typing              Memory
----------------------------------------------------------------------
Python          bytecode + VM           dynamic, strong     automatic (GC)
Java            bytecode + VM + JIT     static, strong      automatic (GC)
```

**Then experiment:** your columns probably do not line up perfectly with tabs. Try two tabs in places, or spaces. Which gives the neatest result? Note it in a comment.

**Hint:** Lecture 2, C.2 "Putting it together".

**Tests:** the classification vocabulary, formatted output.

---

### Exercise 4 — Three ways to run one line

**Level:** 1 · **File:** `ex04_three_ways.py`

**Problem:** run the same line of Python as a script, from the command line with `-c`, and in the REPL.

**Requirements**

1. Write a script whose only code is `print("Same code, three ways")`. Run it.
2. Run the same line with `-c`:
   - macOS/Linux: `python3 -c 'print("Same code, three ways")'`
   - Windows: `py -c "print('Same code, three ways')"`
3. Run it in the REPL.
4. In the REPL, also type just `"Same code, three ways"` with no `print()`. Note what is different.
5. Add a comment block to your script recording each exact command you typed and the output you saw.

**Questions to answer in comments**

- In all three cases, did the code go through the compiler? (Think about the pipeline.)
- Why did the REPL show quotes in step 4 but not in step 3?

**Hint:** Lecture 1, C.6; Lecture 2, C.4.

**Tests:** knowing the ways to start Python, and that all of them compile before running.

---

### Exercise 5 — The `None` surprise

**Level:** 1 · **File:** `ex05_none_surprise.py`

**Problem:** reproduce, explain and fix a common mistake.

**Requirements**

1. Write `print(dis.dis("7 * 6"))` (with the import). **Predict** the output in a comment, then run it.
2. Below it, add a second line, `print(print("Hi"))`. Predict, then run.
3. Write a comment explaining where each `None` comes from.
4. Create a fixed version below a comment `# FIXED VERSION`: disassemble `7 * 6` with no `None`, and print `Hi` once with no `None`.

**Expected output of your fixed lines** (Python 3.13)

```text
  0           RESUME                   0

  1           RETURN_CONST             0 (42)
Hi
```

**Hint:** Lecture 2, Demo 6. What does a function hand back when it has finished printing?

**Tests:** understanding that `print()` and `dis.dis()` return `None`.

---

### Exercise 6 — Compiled but never run

**Level:** 1 · **File:** `ex06_compiled_not_run.py`

**Problem:** prove that compiling code does not run it.

**Requirements**

1. Print the heading `Disassembling three dangerous-looking lines`.
2. Disassemble each of these, with a printed label before each one:
   - `print(missing_name)`
   - `print("Port " + 22)`
   - `print(5 / 0)`
3. Print `All three compiled. None of them ran.` at the end.
4. The program must finish with **no error**.
5. Then add, as the very last line, `exec(compile("print(5 / 0)", "<test>", "exec"))`. Run again, and record what changed in a comment.

**Questions to answer in comments**

- Which error would each of the three lines cause if it were run?
- In the `5 / 0` listing, find the instruction that would do the division. Why did the compiler not fold `5 / 0` into an answer?

**Hint:** Lecture 2, Demo 3 and C.6.

**Tests:** separating compile time from run time.

---

## Level 2 — Applying the concept

### Exercise 7 — Constant folding detective

**Level:** 2 · **File:** `ex07_folding.py`

**Problem:** find out which expressions the compiler works out in advance.

**Requirements**

- At the top, write a comment for each expression below predicting **FOLDED** or **NOT FOLDED**, and, if folded, the value you expect.
- Then disassemble all six, with a printed label before each:

| # | Expression |
| --- | --- |
| a | `365 * 24` |
| b | `"Log" + "in"` |
| c | `"*" * 40` |
| d | `"*" * 4097` |
| e | `2 ** 10` |
| f | `10 / 0` |

- After running, add a comment for each saying whether your prediction was right.

**Questions to answer in comments**

- Why is folding useful? Think about a line inside a program that runs a million times.
- Why does CPython refuse to fold (d)? Why must it refuse to fold (f)?

**Hint:** Lecture 2, Demo 4. A folded result shows up as one constant (`RETURN_CONST`, `LOAD_CONST` or `LOAD_SMALL_INT`, depending on your version). An unfolded one shows `BINARY_OP`.

**Tests:** constant folding, reading `dis` output.

---

### Exercise 8 — Compile and run by hand

**Level:** 2 · **File:** `ex08_compile_exec.py`

**Problem:** do the compile step and the run step yourself.

**Requirements**

1. Using `exec(compile(...))`, run three separate pieces of code, each with its own label (the second argument to `compile()`): `"<first>"`, `"<second>"` and `"<third>"`:
   - `print("Compiled at run time")`
   - `print("A", "B", "C", sep=" -> ")`
   - `print("Total:", 19 + 23)`
2. Put a normal `print("--- next ---")` between them.
3. Finally, add a fourth `exec(compile(...))` whose code is broken: `print("Oops"` (missing bracket), labelled `"<fourth>"`.

**Expected output** (up to the error)

```text
Compiled at run time
--- next ---
A -> B -> C
--- next ---
Total: 42
--- next ---
```

followed by a traceback ending in `SyntaxError: '(' was never closed`.

**Questions to answer in comments**

- The file contains a syntax error, yet three pieces of code ran. Explain why, using the words *compile time* and *run time*.
- Find the label `<fourth>` in the traceback. What is the label for?

**Hint:** Lecture 2, Demo 5. Remember to use single quotes around code that contains double quotes.

**Tests:** `compile()`, `exec()`, nested calls, two levels of compile time.

---

### Exercise 9 — Make and run a `.pyc`

**Level:** 2 · **File:** `ex09_greet.py`

**Problem:** create a bytecode file deliberately and run it without its source.

**Requirements**

1. Write `ex09_greet.py`, which prints two lines: `Hello from bytecode` and `I was compiled before I ran`.
2. Compile it without running it: `python3 -m py_compile ex09_greet.py`. Did anything print?
3. List the new `__pycache__` folder (`ls __pycache__` or `dir __pycache__`). Write the exact filename in a comment and label each part of it.
4. Run the `.pyc` directly, for example `python3 __pycache__/ex09_greet.cpython-313.pyc` (use your own filename).
5. Rename `ex09_greet.py` to `ex09_greet_hidden.py`, run the `.pyc` again, then rename it back.

**Questions to answer in comments**

- What does step 5 prove?
- Why does this matter for anyone who thinks shipping only `.pyc` files keeps their code private?

**Hint:** Lecture 2, C.7.

**Tests:** `py_compile`, cache tags, running bytecode without source.

---

### Exercise 10 — Importing caches, running does not

**Level:** 2 · **Files:** `ex10_main.py`, `ex10_helper.py`

**Problem:** find out exactly when Python writes a `.pyc` file.

**Requirements**

- `ex10_helper.py` prints `helper loaded`.
- `ex10_main.py` prints `main: start`, then imports `ex10_helper` (write `import ex10_helper`, with no `.py`), then prints `main: end`.
- Do this experiment **in order**, and record the result of each step in a comment in `ex10_main.py`:
  1. Delete `__pycache__` if it exists. Run `python3 -B ex10_main.py`. Is there a `__pycache__` now?
  2. Run `python3 ex10_main.py`. What is in `__pycache__` now? Is there a `.pyc` for `ex10_main`?
  3. Run it again. Did the output change?
  4. Edit `ex10_helper.py` to print `helper loaded (version 2)`, then run `ex10_main.py` again. What happened, and how did Python know the cache was out of date?

**Expected output of step 2**

```text
main: start
helper loaded
main: end
```

**Hint:** Lecture 2, Demo 8 and C.7 (the header stores the source file's time and size).

**Tests:** import caching, `-B`, cache freshness checks.

---

### Exercise 11 — The magic number

**Level:** 2 · **File:** `ex11_magic.py`

**Problem:** connect your interpreter to the first bytes of its `.pyc` files.

**Requirements**

1. Print your Python version (`sys.version`) and cache tag (`sys.implementation.cache_tag`).
2. Print the magic number your interpreter writes into `.pyc` files. Use this tool line, which you will fully understand in Part IV:

   ```python
   import importlib.util
   print("Magic number:", importlib.util.MAGIC_NUMBER)
   ```

3. Show the raw bytes of the `.pyc` you made in Exercise 9. Use this tool line from Lecture 2, Demo 12 (with your own filename):

   ```python
   print(open("__pycache__/ex09_greet.cpython-313.pyc", "rb").read())
   ```

4. In a comment, copy the first 4 bytes of the file and check they match the magic number.

**Expected output** (the start of it, on Python 3.13)

```text
Version: 3.13.18 (main, Oct 26 2026, 14:08:19) [Clang 23.1.3 ]
Cache tag: cpython-313
Magic number: b'\xf3\r\r\n'
b'\xf3\r\r\n\x00\x00\x00\x00...
```

**Questions to answer in comments**

- Can you spot the two strings from your `ex09_greet.py` inside the bytes?
- Why does every Python version need a different magic number?

**Tests:** the `.pyc` header, version-specific bytecode.

---

### Exercise 12 — Disassemble a whole program

**Level:** 2 · **File:** `ex12_receipt_dis.py`

**Problem:** disassemble the Day 1 receipt program and summarise what you find.

**Requirements**

1. Run `python3 -m dis ../../Examples/Lecture-01/ex12_receipt.py` (from your `Lab-02` folder).
2. Count, by hand, how many times each of these appears: `LOAD_NAME`, `LOAD_CONST`, `CALL`, `POP_TOP`.
3. Write `ex12_receipt_dis.py`, which prints a short report like the one below, with your real counts:

```text
BYTECODE REPORT: ex12_receipt.py
==============================
print statements in source:   ?
LOAD_NAME instructions:       ?
LOAD_CONST instructions:      ?
CALL instructions:            ?
POP_TOP instructions:         ?
```

**Questions to answer in comments**

- Why is the number of `CALL` instructions equal to the number of `print()` calls?
- The source has `"=" * 30` four times. How does it appear in the bytecode, and why does the bytecode reuse the same constant number each time?
- The source has `2.50 + 3.75`. What did the compiler store instead?

**Hint:** Lecture 2, C.5 (whole files end each line with `POP_TOP`).

**Tests:** reading a full listing, connecting source lines to instructions.

---

## Level 3 — Combining operations

### Exercise 13 — The pipeline, stage by stage

**Level:** 3 · **Files:** `ex13_target.py`, `ex13_pipeline_report.py`

**Problem:** follow one program through every stage of CPython's pipeline.

**Requirements**

1. `ex13_target.py` contains your header comment and one line: `print("Login", "failed", sep=" -> ", end="!\n")`.
2. Run all four on it, saving what you see: the script itself, `python3 -m tokenize`, `python3 -m ast` and `python3 -m dis`.
3. `ex13_pipeline_report.py` prints a report with one section per stage, for example:

```text
STAGE 2 - TOKENIZER
  Number of tokens (excluding ENCODING and ENDMARKER): ?
  Kinds of token seen: ...
STAGE 3 - PARSER (AST)
  Top node inside the module body: ...
  Number of keyword arguments: ...
STAGE 4 - COMPILER (BYTECODE)
  Call instruction used: ...
  Keyword names tuple: ...
STAGE 6 - RUN
  Output: ...
```

**Questions to answer in comments**

- Where did the quote marks go between the tokens and the AST?
- Why is there no stage 5 section? (What is a code object, and why can you not see it directly with these tools?)

**Hint:** Lecture 2, C.4 and Demo 7.

**Tests:** the full pipeline and its tools.

---

### Exercise 14 — What the compiler throws away

**Level:** 3 · **File:** `ex14_comments.py`

**Problem:** prove that comments cost nothing at run time.

**Requirements**

1. Write a file with **five** comment lines, one blank line and **one** line of code: `print("Comments are free")`.
2. Run `-m tokenize`, `-m ast` and `-m dis` on it.
3. Make a second version, `ex14_no_comments.py`, with the same code line and no comments.
4. Compare the `dis` output of both files.
5. Add a comment block to `ex14_comments.py` answering the questions below.

**Questions**

- At which stage do the comments stop existing?
- Is the bytecode of the two files identical? If anything differs, what is it, and why?
- A classmate says: "I delete my comments to make my program faster." Reply to them in two sentences.

**Hint:** compare the source line numbers in the two `dis` listings.

**Tests:** tokens versus AST, why comments are always worth writing.

---

### Exercise 15 — Same output, different bytecode

**Level:** 3 · **File:** `ex15_same_output.py`

**Problem:** three lines print the same text. Do they compile to the same bytecode?

**Requirements**

- Disassemble each of these, with a label before each:
  - (a) `print("A-B-C")`
  - (b) `print("A", "B", "C", sep="-")`
  - (c) `print("A" + "-" + "B" + "-" + "C")`
- **Predict** first: which will produce the fewest instructions?
- Then run each one for real with `exec(compile(...))` to confirm they all print `A-B-C`.

**Questions to answer in comments**

- Count the instructions for each. Which are identical, and why?
- Which version does the most work at **run time**? Which does the most work at **compile time**?
- Which would you write in a real program? Readability counts. Give a reason.

**Hint:** constant folding works on string `+` too.

**Tests:** linking source style to bytecode, compile time versus run time work.

---

### Exercise 16 — Java bytecode versus Python bytecode

**Level:** 3 · **Files:** `Hello.java`, `ex16_hello.py`, `ex16_compare.py`

**Problem:** compare the two stack machines you now know.

**Requirements**

1. Write `Hello.java` printing `Hello from Java` (Lecture 2, Demo 10). Compile with `javac Hello.java`, run with `java Hello`, and disassemble with `javap -c Hello`.
2. Write `ex16_hello.py` printing `Hello from Python`, and disassemble it with `python3 -m dis ex16_hello.py`.
3. Write `ex16_compare.py`, which prints a comparison table:

```text
                    JAVA                    PYTHON (CPython)
Compile command     javac Hello.java        (automatic)
Bytecode file       Hello.class             only if imported (.pyc)
View bytecode       javap -c Hello          python3 -m dis file.py
Push the function   getstatic ...           LOAD_NAME print
Push the text       ...                     ...
Call it             ...                     ...
```

Fill in every `...` from your own outputs. Add at least two more rows of your own (for example: type checking, JIT).

**Questions to answer in comments**

- Both are stack machines. What evidence in the listings shows this?
- `javap` shows a method called `Hello()` you never wrote. What is it?

**Tests:** comparing two bytecode VMs, using knowledge from 4300COMP.

---

### Exercise 17 — A true native compile

**Level:** 3 · **Files:** `hello.c`, `ex17_native.py`

**Problem:** see the difference between native code and bytecode for yourself.

**Requirements (main route, with `gcc`)**

1. Write `hello.c` (Lecture 2, Demo 11). Compile with `gcc hello.c -o hello.out`, then run `./hello.out`.
2. Run `file hello.out` (Linux/macOS/WSL) and note what it says.
3. Find the file sizes of `hello.c`, `hello.out` and a `.pyc` from Exercise 9 (`ls -l`).
4. Try to show `hello.out`'s bytecode with Python: `python3 -m dis hello.out`. What happens, and why?
5. Write `ex17_native.py`, which prints a short report of your findings: what `file` said, the three sizes, and one sentence explaining the result of step 4.

**Alternative route (no `gcc` available):** skip steps 1–4. Instead, use the `file` output and explanation in Lecture 2, Demo 11, and write `ex17_native.py` as a report explaining what *would* happen in each step and why. Say in the report that you used the alternative route.

**Questions to answer in comments**

- Could you copy `hello.out` to a Windows laptop and run it? Could you copy a `.py`? A `.pyc`?
- Why is `hello.out` so much bigger than `hello.c`?

**Tests:** AOT compilation, native code, portability.

---

### Exercise 18 — Version detective

**Level:** 3 · **File:** `ex18_versions.py`

**Problem:** bytecode changes between Python versions. Identify which version produced each listing.

These two listings were both produced by `dis.dis("10 * 6")`:

**Listing X**

```text
  0           RESUME                   0

  1           LOAD_SMALL_INT          60
              RETURN_VALUE
```

**Listing Y**

```text
  0           RESUME                   0

  1           RETURN_CONST             0 (60)
```

**Requirements**

1. Disassemble `10 * 6` and `10 * 600` on your own Python.
2. Using Lecture 2, C.5, decide which listing came from Python 3.13 and which from Python 3.14 or newer.
3. Write `ex18_versions.py`, which prints:
   - your Python version,
   - which listing (X or Y) your output matches, or neither,
   - which version produced X and which produced Y,
   - one sentence on what is **the same** in both listings.
4. Windows users: run `py -0`. If you have more than one Python installed, run the disassembly on each (for example `py -3.13 ex18_versions.py`) and include both results.

**Questions to answer in comments**

- On 3.14 or newer, `10 * 600` does not use `LOAD_SMALL_INT`. Find out what it uses. Why might "small" integers get a special instruction?
- Did the meaning of `10 * 6` change between versions? What does this tell you about the difference between the language and its implementation?

**Tests:** implementation details versus language rules.

---

## Level 4 — Problem-solving and debugging

### Exercise 19 — Compile time or run time?

**Level:** 4 · **Files:** `ex19a.py` to `ex19i.py`, `ex19_results.py`

**Problem:** for each snippet, decide when (if ever) the mistake is caught.

| File | Code (put this after the header comment) |
| --- | --- |
| `ex19a.py` | `print("Welcome)` |
| `ex19b.py` | `print("Welcome"` |
| `ex19c.py` | `Print("Welcome")` |
| `ex19d.py` | `print("Port " + 22)` |
| `ex19e.py` | `print(10 / 0)` |
| `ex19f.py` | `return "done"` |
| `ex19g.py` | `    print("indented")` (four spaces at the start) |
| `ex19h.py` | `print("Total:", 3 + 4 * 2)` |
| `ex19i.py` | `print("Area of a 3 by 4 rectangle:", 3 + 4)` |

**Requirements**

1. **Before testing anything**, write your predictions in a comment at the top of `ex19_results.py`. For each file, say: *compile time*, *run time* or *never caught*, and the error name you expect.
2. Test each file in **two steps**:
   - `python3 -m py_compile ex19a.py` (if this shows an error, it is a compile-time error)
   - `python3 ex19a.py` (only if step 1 was silent)
3. Write `ex19_results.py` to print a results table:

```text
File     When caught      Error
ex19a    compile time     SyntaxError (unterminated string literal)
...
```

4. Below the table, print your score: how many predictions were right out of 9.

**Questions to answer in comments**

- Two files produce no error message at all. Are they both correct programs?
- Which compile-time error is found by the compiler rather than by the tokenizer or parser?

**Hint:** Lecture 2, C.6 table.

**Tests:** predicting error stages, using `py_compile` as a checker.

---

### Exercise 20 — Fix it before it runs

**Level:** 4 · **File:** `ex20_service_status.py`

**Problem:** this program contains three syntax errors, one runtime error and one logic error. Use the compiler to find the syntax errors **without running the program**.

Type it exactly as shown, mistakes included:

```python
# ex20_service_status.py
# Prints a service status report. Contains several deliberate mistakes.
print("Service status report)
print("SSH", "running", sep=": ")
print("HTTP" "stopped", sep=": ")
    print("FTP", "disabled", sep=": ")
print("Checked at", "09:00"
prnt("End of report")
```

**Requirements**

1. Run `python3 -m py_compile ex20_service_status.py`. Fix **only** the error it reports. Repeat until it is silent. Keep a record in a comment: round number, line, error message, your fix. (One round's message starts with `Sorry:`. That is just how `py_compile` prints that kind of error.)
2. Only when `py_compile` is silent, run the program. Fix the runtime error.
3. Look carefully at the output. One line is wrong but caused no error at all. Find it and fix it.

**Target output after all fixes**

```text
Service status report
SSH: running
HTTP: stopped
FTP: disabled
Checked at 09:00
End of report
```

**Questions to answer in comments**

- How many rounds of `py_compile` did you need? Why does the compiler report only one syntax error at a time?
- Why did `py_compile` never complain about `prnt`?
- Explain exactly why `"HTTP" "stopped"` is not a syntax error. (Try `print("HTTP" "stopped")` in the REPL.)

**Tests:** systematic debugging, and the limits of what a compiler can catch.

---

### Exercise 21 — Reverse engineer: mystery A

**Level:** 4 · **File:** `ex21_mystery_a.py`

**Problem:** here is the bytecode of a mystery program (Python 3.13, `python3 -m dis`). Rebuild the source code.

```text
  0           RESUME                   0

  1           LOAD_NAME                0 (print)
              PUSH_NULL
              LOAD_CONST               0 ('System check')
              CALL                     1
              POP_TOP

  2           LOAD_NAME                0 (print)
              PUSH_NULL
              LOAD_CONST               1 ('Disk')
              LOAD_CONST               2 ('OK')
              LOAD_CONST               3 (' ... ')
              LOAD_CONST               4 (('sep',))
              CALL_KW                  3
              POP_TOP

  3           LOAD_NAME                0 (print)
              PUSH_NULL
              LOAD_CONST               5 (3600)
              LOAD_CONST               6 ('seconds in an hour')
              CALL                     2
              POP_TOP
              RETURN_CONST             7 (None)
```

**Requirements**

1. **Before writing any code**, predict the program's output in a comment.
2. Write `ex21_mystery_a.py` so that `python3 -m dis` on it gives the same instructions (ignore the line numbers on the left).
3. For constant 5, there is more than one possible source. Write it as a calculation that the compiler would fold into `3600`, and explain in a comment why you cannot tell from the bytecode alone which calculation (or plain number) the author typed.
4. Run your program and check your predicted output.

**Tests:** reading bytecode backwards, constant folding, keyword arguments.

---

### Exercise 22 — Reverse engineer: mystery B

**Level:** 4 · **File:** `ex22_mystery_b.py`

**Problem:** a harder listing (Python 3.13). Rebuild the source code.

```text
  0           RESUME                   0

  1           LOAD_NAME                0 (print)
              PUSH_NULL
              LOAD_CONST               0 ('==============================')
              CALL                     1
              POP_TOP

  2           LOAD_NAME                0 (print)
              PUSH_NULL
              LOAD_CONST               1 ('ALERT\tLevel')
              LOAD_CONST               2 (3)
              LOAD_CONST               3 ('!\n')
              LOAD_CONST               4 (('end',))
              CALL_KW                  3
              POP_TOP

  3           LOAD_NAME                0 (print)
              PUSH_NULL
              LOAD_CONST               5 ('Source:')
              LOAD_CONST               6 ('10.0.0.5')
              LOAD_CONST               7 ('Port:')
              LOAD_CONST               8 (22)
              CALL                     4
              POP_TOP

  4           LOAD_NAME                0 (print)
              PUSH_NULL
              LOAD_CONST               0 ('==============================')
              CALL                     1
              POP_TOP
              RETURN_CONST             9 (None)
```

**Requirements**

1. Predict the **exact** output first, including where the tab and the `!` appear.
2. Rebuild the source. Use `*` for the line of `=` characters (count them).
3. Verify with `python3 -m dis` and by running it.

**Questions to answer in comments**

- Line 4 uses `LOAD_CONST 0`, the same constant as line 1. What does that tell you about how the compiler stores constants?
- `CALL 4` on line 3 has no keyword names tuple. What `sep` and `end` values does that `print()` call use?
- `3` and `22` have no quotes in the listing, but `'10.0.0.5'` does. What does that tell you about their types?

**Tests:** escape sequences in bytecode, constant reuse, default arguments.

---

### Exercise 23 — Java refuses, Python runs

**Level:** 4 · **Files:** `Broken.java`, `ex23_broken.py`, `Fixed.java`, `ex23_fixed.py`

**Problem:** make the same mistake in both languages and compare when it is caught.

**Requirements**

1. `Broken.java`: print `Step 1`, `Step 2` and `Step 3` with `System.out.println`, but misspell the third one as `System.out.prinltn`. Try `javac Broken.java`.
2. `ex23_broken.py`: print the same three lines, misspelling the third `print` as `pirnt`. Run `python3 -m py_compile ex23_broken.py`, then run the script.
3. Record both complete error outputs in a comment in `ex23_broken.py`.
4. Make fixed copies, `Fixed.java` (the class name must change to `Fixed`) and `ex23_fixed.py`, and run both.

**Questions to answer in comments**

- How many lines of output did each broken program produce before failing? Why?
- Which language's approach would you prefer for a program that controls a door lock? For a quick script that renames files? Give a reason for each.
- Python's error message suggested a fix. What did it suggest, and how do you think it worked that out?

**Hint:** Lecture 2, C.6 "Why Java catches more" and Demo 9.

**Tests:** static versus dynamic checking.

---

### Exercise 24 — Trace the stack

**Level:** 4 · **File:** `ex24_stack_trace.py`

**Problem:** run the stack machine by hand.

**Requirements**

1. Disassemble `print("Total:", 3 * 4)`. Python 3.13 gives:

   ```text
     0           RESUME                   0

     1           LOAD_NAME                0 (print)
                 PUSH_NULL
                 LOAD_CONST               0 ('Total:')
                 LOAD_CONST               1 (12)
                 CALL                     2
                 RETURN_VALUE
   ```

2. In comments, write an execution trace table like the one in Lecture 2, C.5: step, instruction, stack afterwards, visible effect.
3. Now **without running anything**, write the bytecode you expect for `print("Hi", "there", sep="_")` as a comment, then a trace table for it.
4. Check your expected bytecode with `dis.dis()` in the file. Mark any line you got wrong, and correct it.
5. Finally, run both lines with `exec(compile(...))` and check the visible effects in your tables.

**Questions to answer in comments**

- Why is there no instruction that multiplies 3 by 4?
- After `CALL`, how many items are on the stack, and what is the item?

**Tests:** stack machine reasoning, predicting compiler output.

---

## Level 5 — Real-world applications and challenges

### Exercise 25 — Secrets in bytecode

**Level:** 5 · **Files:** `ex25_fake_config.py`, `ex25_finding.py`

**Problem:** prove that compiling does not hide a secret, then write it up like a security finding.

> Use only the **fake** values below. Never put a real password in any file in this repository.

**Requirements**

1. `ex25_fake_config.py` prints two lines:
   - `Database user: lab_admin`
   - `Database password: FAKE-Passw0rd-For-Lab-Only`
2. Compile it with `python3 -m py_compile ex25_fake_config.py`.
3. Move the source somewhere else (or rename it) so only the `.pyc` remains in `Lab-02`.
4. Recover the secret **from the `.pyc` alone**, in two ways:
   - by printing the raw bytes (the tool line from Lecture 2, Demo 12),
   - by running the `.pyc` directly.
5. Put the source file back.
6. Write `ex25_finding.py`, which prints a short security finding in this format:

```text
============================================================
FINDING: Hard-coded credential recoverable from bytecode
============================================================
Severity:        ...
Affected file:   ...
Evidence:        ...
How recovered:   ...
Impact:          ...
Recommendation:  ...
============================================================
```

Fill in each field yourself. Choose a severity (Low, Medium, High or Critical) and justify it in a comment.

**Questions to answer in comments**

- Would compiling the program to a native `.exe` instead have fixed the problem? Why or why not?
- Where should a real password be kept instead? (You may answer "I do not know yet". This is covered in Part V and Part IX.)

**Tests:** applying today's ideas to a real security problem, and professional reporting.

---

### Exercise 26 — Triage without running

**Level:** 5 · **File:** `ex26_triage.py`

**Problem:** a colleague found an unknown script on a lab machine. You are not allowed to run it. All you have is its disassembly (Python 3.13):

```text
  0           RESUME                   0

  1           LOAD_NAME                0 (print)
              PUSH_NULL
              LOAD_CONST               0 ('Connecting to 203.0.113.5 ...')
              CALL                     1
              POP_TOP

  2           LOAD_NAME                0 (print)
              PUSH_NULL
              LOAD_CONST               1 ('Uploading files')
              LOAD_CONST               2 ('... ')
              LOAD_CONST               3 (('end',))
              CALL_KW                  2
              POP_TOP

  3           LOAD_NAME                0 (print)
              PUSH_NULL
              LOAD_CONST               4 ('done')
              CALL                     1
              POP_TOP

  4           LOAD_NAME                1 (Print)
              PUSH_NULL
              LOAD_CONST               5 ('Connection closed')
              CALL                     1
              POP_TOP
              RETURN_CONST             6 (None)
```

**Requirements**

Write `ex26_triage.py`, which prints a triage report answering:

1. **What names does the code use?** List every name loaded with `LOAD_NAME`.
2. **Does it import anything?** (What instruction would you expect to see if it did? Disassemble `import socket` yourself to find out.)
3. **Does it actually connect to 203.0.113.5 or upload anything?** Justify your answer from the bytecode, not from the text it prints.
4. **Will it run to the end?** If not, which source line fails, with which error, and why?
5. **Exact output before it stops.** Pay attention to `end`.
6. **Verdict:** in one sentence, is this script dangerous, misleading, or harmless?

**Finally:** rebuild the source as `ex26_rebuilt.py` and run **your own** rebuilt copy to confirm answers 4 and 5. Running your own copy is fine. The rule was never to run the unknown original.

**Questions to answer in comments**

- What is the difference between what a program *says* it does and what it *does*? Why should an analyst trust the instructions over the messages?
- `203.0.113.5` is in a range reserved for documentation (TEST-NET-3). Why do examples and labs use such addresses?

**Tests:** safe static analysis, reading names and constants, spotting a runtime error before it happens.

---

### Exercise 27 — Compile-time work is free at run time

**Level:** 5 · **File:** `ex27_timing_report.py`

**Problem:** measure the effect of constant folding with `timeit`, a standard tool for timing small pieces of code.

**Requirements**

1. Run each of these in the terminal. `timeit` runs the code millions of times and reports the best average time per run.

   ```bash
   python3 -m timeit '"=" * 20'
   python3 -m timeit '"=" * 5000'
   python3 -m timeit '60 * 60 * 24'
   python3 -m timeit '"Cyber" + "Security"'
   ```

   On Windows PowerShell, use `py -m timeit "'=' * 20"` and so on (swap the quote styles).

2. For each one, record the time per loop, and check in `dis` whether it was folded.
3. Write `ex27_timing_report.py`, which prints a table: expression, folded (yes/no), time per loop, and a final conclusion line.

**Example of the format** (the times here are made up; use your own)

```text
Expression               Folded?   Time per loop
"=" * 20                 yes       ?? nsec
...
Conclusion: ...
```

**Questions to answer in comments**

- The folded expressions all take roughly the same tiny time. Why? (What is the VM actually doing for them?)
- Times vary between runs and between computers. Why does `timeit` report the *best* of several runs?

**Tests:** connecting compiler behaviour to measured performance.

---

### Exercise 28 — Pick the right translation model

**Level:** 5 · **File:** `ex28_language_picker.py`

**Problem:** for each scenario, recommend a translation model and a language, and justify it.

| # | Scenario |
| --- | --- |
| 1 | Firmware for a cheap home router with very little memory |
| 2 | A ten-line script to search today's authentication log for failed logins |
| 3 | An interactive feature on a web page, running inside the user's browser |
| 4 | A large banking system, run on servers for years, where speed matters after start-up |
| 5 | A tool given to a hundred analysts who use Windows, macOS and Linux |
| 6 | A program that must catch as many mistakes as possible before it ever runs |

**Requirements**

- Print one block per scenario: the scenario, your recommended **translation model** (AOT native, bytecode + VM, JIT, or interpreted), an example **language**, and a **reason** that uses at least one idea from the lecture (speed, portability, compile-time checking, memory, start-up time).
- End with a printed paragraph on why there is no single "best" language.

**Tests:** applying the classification to real decisions.

---

### Exercise 29 — Pipeline poster

**Level:** 5 · **File:** `ex29_pipeline_poster.py`

**Problem:** create a text "poster" explaining CPython's pipeline to a first-year student who missed today's lecture.

**Requirements**

- Use one example line of code, chosen by you, and show what it looks like at every stage.
- For each of the six stages: its name, what goes in, what comes out, the command that shows it (if there is one), and one kind of error caught there (if any).
- Use boxes and arrows drawn with characters (`+`, `-`, `|`, `v`), with `*` repetition for long lines.
- At least 30 lines of output, and readable in an 80-character-wide terminal.
- Mark clearly where compile time ends and run time begins.

**Tip:** run `-m tokenize`, `-m ast` and `-m dis` on your chosen line first, and copy short real fragments onto your poster by typing them.

**Tests:** explaining the full model in your own words, formatted output.

---

### Exercise 30 — Capstone: under the hood

**Level:** 5 · **File:** `ex30_under_the_hood.py`

**Problem:** one program that demonstrates today's main ideas, then a self-investigation of that program.

**Requirements**

The program prints five numbered sections, each with a heading and a line of `-`:

1. **This interpreter:** implementation, version, C compiler, cache tag.
2. **Compile, then run:** uses `exec(compile(...))` to run one line of your choice, with a custom label, and prints a sentence explaining the two steps.
3. **Constant folding:** disassembles one expression that is folded and one that is not, with a sentence after each.
4. **Four languages compared:** a small table of Python, Java, C and JavaScript (translation model and typing).
5. **What I learned today:** three sentences in your own words.

Then, the investigation (answers as comments at the bottom of the file):

- Run `python3 -m dis ex30_under_the_hood.py`. What is the **first** source line that has any instructions, and why not line 1?
- How many `CALL` or `CALL_KW` instructions does your program contain? Does that match the number of calls you wrote?
- Find a constant that is shown folded in the listing of your own file.
- Run `python3 -m py_compile ex30_under_the_hood.py` and run the resulting `.pyc`. Does the output match running the `.py`?

**Tests:** everything from today, in one program.

---

## Extension (optional, for fast finishers)

- **E1.** Run `python3 -m dis --help` and read the options. Try `-C` (show cache entries) on one of your files. What changed? (Some options depend on your version.)
- **E2.** Read the first section of the `dis` module documentation (https://docs.python.org/3/library/dis.html). Find the sentence that warns bytecode can change between versions. Print it as a quotation, with the link, in `extE2_dis_warning.py`.
- **E3.** Read the summary of PEP 659, the specialising adaptive interpreter (https://peps.python.org/pep-0659/). In `extE3_pep659.py`, print five lines explaining it in your own words.
- **E4.** Write a 3-line C program with a missing semicolon. Compare `gcc`'s error message with Python's `SyntaxError`. Which is clearer for a beginner?

---

## Submitting for review

When you finish a level, say **"Review Day 2, Level N"** and share your files (paste them, or commit and push them to this repository). Include your Python version, because today's outputs depend on it. For each exercise you will get:

- ✅ pass, or 🔁 revise
- syntax, logic or style issues, with **why** they matter
- an improved or alternative solution, **after** you have attempted it
- a short note on what to practise

Reference solutions go in `Reference-Solutions/Lab-02/` only after review.

## Progress tracker

| # | Exercise | Attempted | Reviewed |
| --- | --- | --- | --- |
| 1 | Which Python am I? | ⬜ | ⬜ |
| 2 | First disassembly, annotated | ⬜ | ⬜ |
| 3 | Language profile table | ⬜ | ⬜ |
| 4 | Three ways to run one line | ⬜ | ⬜ |
| 5 | The `None` surprise | ⬜ | ⬜ |
| 6 | Compiled but never run | ⬜ | ⬜ |
| 7 | Constant folding detective | ⬜ | ⬜ |
| 8 | Compile and run by hand | ⬜ | ⬜ |
| 9 | Make and run a `.pyc` | ⬜ | ⬜ |
| 10 | Importing caches, running does not | ⬜ | ⬜ |
| 11 | The magic number | ⬜ | ⬜ |
| 12 | Disassemble a whole program | ⬜ | ⬜ |
| 13 | The pipeline, stage by stage | ⬜ | ⬜ |
| 14 | What the compiler throws away | ⬜ | ⬜ |
| 15 | Same output, different bytecode | ⬜ | ⬜ |
| 16 | Java bytecode versus Python bytecode | ⬜ | ⬜ |
| 17 | A true native compile | ⬜ | ⬜ |
| 18 | Version detective | ⬜ | ⬜ |
| 19 | Compile time or run time? | ⬜ | ⬜ |
| 20 | Fix it before it runs | ⬜ | ⬜ |
| 21 | Reverse engineer: mystery A | ⬜ | ⬜ |
| 22 | Reverse engineer: mystery B | ⬜ | ⬜ |
| 23 | Java refuses, Python runs | ⬜ | ⬜ |
| 24 | Trace the stack | ⬜ | ⬜ |
| 25 | Secrets in bytecode | ⬜ | ⬜ |
| 26 | Triage without running | ⬜ | ⬜ |
| 27 | Compile-time work is free at run time | ⬜ | ⬜ |
| 28 | Pick the right translation model | ⬜ | ⬜ |
| 29 | Pipeline poster | ⬜ | ⬜ |
| 30 | Capstone: under the hood | ⬜ | ⬜ |
