# Lab 9 — Repetition (for Loop) Hands-on Workbook (20 Tasks)

**Module:** 4300COMP Introduction to Programming · **Language:** Java

## How to use this lab

This lab has **20 hands-on tasks** on Lecture 9: the `for` loop, converting between `for` and `while`, loop variable scope, off-by-one errors and patching, choosing the right loop, `break`, nested loops and debugging loops. **All official Tutorial 9 tasks and the supplementary task are included** (Tasks 4, 5, 13, 15, 16 and 17), marked "official".

**Learning outcomes:** MLO1 (loop constructs and algorithms), MLO2 (Eclipse debugger in Task 9; Oracle's `for` tutorial in Task 1), MLO3 (Tasks 13 and 16–20 turn specifications into programs).

**Setup:** create a Java project called **Lab09** in Eclipse. Untick *Create module-info.java*. Make one class per task and tick `public static void main(String[] args)`. Data files go in the **project folder** (the folder that contains `src`).

**Rules for this lab:**

1. **Predict before you run.** Write your answer first, then check.
2. **Name the three parts.** For every `for` loop, say aloud: "starts at…, runs while…, changes by…". Then work out how many times it runs.
3. **Fix the cause, not the symptom.** No patches (Lecture 9, section 8).
4. **For nested loops, think rows and columns:** the outer loop is usually the rows, the inner loop the columns.
5. If a program freezes, press the red **Terminate** button and check the condition and update.
6. Use the hints only after a real attempt.

The **tracker** is near the end, followed by the **answer key**. Every answer was compiled and run with Java 21 (javac on the command line, not Eclipse) with the inputs shown.

## Part A — Writing for loops (Tasks 1–5)

### Task 1 — First for loops

**Class:** `Task01ForLoops` · **Goal:** write `for` loops with different starts, conditions and updates.

1. Print `0 1 2 3 4 5 6 7 8 9` on one line with a `for` loop (Lecture 9, Program A).
2. Print `10 9 8 7 6 5 4 3 2 1` on one line.
3. Print the even numbers from 2 to 20 on one line, using `i += 2`.
4. Print `5 10 15 ... 100` on one line.
5. Rewrite Tutorial 8's sum of 0–99 as a `for` loop, exactly as Tutorial 9 shows, using `sum += i;`. Expected: `The sum is = 4950`.
6. Open Oracle's tutorial page [The for Statement](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/for.html) (linked from Tutorial 9). Find the example program on that page, predict its output, then type and run it.

- **Hint 1:** for counting down, all three parts change: start at 10, run while `i >= 1`, update with `i--`.
- **Hint 2:** for step 5, either start at 5 and add 5, or loop 1 to 20 and print `i * 5`.

### Task 2 — Predict the output

**Class:** `Task02Predict` · **Goal:** trace `for` loops in your head.

Predict each line, then put all ten in one `main` and check. "print" means `System.out.print(... + " ")`.

| | Code | Your prediction | Actual |
| --- | --- | --- | --- |
| a | `for (int i = 1; i <= 5; i++) { print i; }` | | |
| b | `for (int i = 10; i > 0; i -= 3) { print i; }` | | |
| c | `for (int i = 0; i < 0; i++) { print i; }` | | |
| d | `for (int i = 1; i < 50; i *= 3) { print i; }` | | |
| e | `int t = 0; for (int i = 1; i <= 4; i++) { t += i * i; }` then print `t` | | |
| f | `for (char c = 'a'; c < 'f'; c++) { System.out.print(c); }` | | |
| g | `int count = 0; for (int i = 0; i < 3; i++) { for (int j = 0; j < 4; j++) { count++; } }` then print `count` | | |
| h | `for (int i = 1; i <= 10; i++) { if (i % 4 == 0) { break; } print i; }` | | |
| i | `for (int i = 1; i <= 3; i++) { for (int j = 1; j <= i; j++) { System.out.print(j); } System.out.print(" "); }` | | |
| j | `int x = 0; for (int i = 0; i < 5; i++); { x++; }` then print `x` | | |

Score yourself out of 10.

- **Hint 1:** for (d), the update multiplies, so list the values: 1, 3, …
- **Hint 2:** for (j), look very carefully at the end of the header.

### Task 3 — for and while conversions

**Class:** `Task03Convert` · **Goal:** see that `for` and counter-controlled `while` are the same loop.

1. Convert to a `for` loop:

```java
int n = 1;
while (n <= 20) {
    System.out.print(n + " ");
    n = n + 3;
}
```

2. Convert to a `while` loop:

```java
for (int k = 100; k > 0; k = k / 2) {
    System.out.print(k + " ");
}
```

3. Convert to a `for` loop, and explain why the `for` version is safer if you later add code after the loop:

```java
int i = 0;
int total = 0;
while (i < 10) {
    total += i;
    i++;
}
System.out.println(total);
```

4. Run each pair and check they print exactly the same.

- **Hint 1:** use the pattern in Lecture 9, section 9: init → before the loop; condition → in `while (...)`; update → last line of the body.
- **Hint 2:** for question 3, think about where `i` exists after each version.

### Task 4 — Official Tutorial 9, Task 1 (part 1): a line of stars

**Class:** `Task04StarLine` · **Goal:** a `for` loop that runs a number of times chosen by the user.

Write a program that asks for a number and uses a `for` loop to display that many `*` on one line.

```text
How many stars? 5
*****
```

Then test with `1`, `0` and `20`. What happens with `0`, and why is that correct?

- **Hint 1:** the loop runs `n` times: `for (int i = 0; i < n; i++)`.
- **Hint 2:** use `print`, not `println`, inside the loop; one `println()` after it.

### Task 5 — Official Tutorial 9, Task 1 (part 2): the alphabet

**Class:** `Task05Letters` · **Goal:** use a `char` as the loop variable.

1. Print all the letters from `A` to `Z` on one line, using a `char` loop variable, as the tutorial asks.
2. Print them backwards, `Z` to `A`.
3. Print every other letter: `ACEGIKMOQSUWY`.
4. Print `a` to `e` with each letter's number code: `a=97 b=98 c=99 d=100 e=101`.
5. **Question:** why can `letter++` move from `'A'` to `'B'`?

- **Hint 1:** `for (char letter = 'A'; letter <= 'Z'; letter++)`.
- **Hint 2:** `(int) letter` gives the character's code (Lecture 2 casting, Lecture 6 character codes).

## Part B — Find and fix (Tasks 6–10)

### Task 6 — Braces, semicolons and scope clinic

**Class:** `Task06Clinic` · **Goal:** recognise four classic `for` mistakes.

For each snippet: predict, run, explain, fix.

```java
// Snippet 1: should print Hello and * five times each
int i;
for (i = 1; i <= 5; i++)
    System.out.println("Hello");
    System.out.println("*");

// Snippet 2: should print "in body" five times
for (int k = 0; k < 5; k++); {
    System.out.println("in body");
}

// Snippet 3: should print 0 to 4 and then the final counter value
for (int m = 0; m < 5; m++) {
    System.out.print(m + " ");
}
System.out.println(m);

// Snippet 4: should print 0 to 4
for (int n = 0, n < 5, n++) {
    System.out.print(n + " ");
}
```

Also: type this line with **curly quotes** copied from a word processor or the slides, `System.out.println(“ “ + i);`, and write down the error message. Then fix it with straight quotes.

- **Hint 1:** snippets 3 and 4 do not compile; read the error messages. Snippets 1 and 2 compile but behave wrongly.
- **Hint 2:** for snippet 3, declare `m` before the loop.

### Task 7 — Off by one in a file, and why not to patch

**Class:** `Task07OffByOne` · **Goal:** reproduce and properly fix the slide's off-by-one bug.

Create `numbers.txt` in the project folder containing: `54 40 90 68 75`

1. Type the slide's loop `for (int i = 0; i <= 5; i++)` that reads and prints each number. Run it. Copy the exception name and the line number from the error.
2. How many times does the loop run? Which value of `i` causes the crash?
3. Fix it **two different ways** by changing only the loop header.
4. Type the "patched" version with `if (i != 5)` from the slides. It works, so why is it poor practice? Give two reasons.
5. **Better still:** which loop from Lecture 8 would read **all** the numbers without you knowing how many there are?

- **Hint 1:** `i` takes the values 0, 1, 2, 3, 4, 5.
- **Hint 2:** for question 5, think `hasNextInt()`.

### Task 8 — Loop bug hunt (8 bugs)

**Class:** `Task08Buggy` · **Goal:** fix compile errors and logic errors in loops.

The program below should print: the numbers 1 to 10; `Sum: 15` (1+2+3+4+5); a countdown `5 4 3 2 1`; three rows of four stars; three lines `k loop`; and finally `3`. It contains **8 bugs**. Find and fix them all. Compile errors first, then run and fix the logic errors.

```java
public class Task08Buggy {
    public static void main(String[] args) {
        for (int i = 1, i <= 10, i++) {
            System.out.print(i + " ");
        }
        System.out.println();
        int sum;
        for (int i = 1; i < 5; i++) {
            sum = sum + i;
        }
        System.out.println("Sum: " + sum);
        for (int i = 5; i >= 1; i++) {
            System.out.print(i + " ");
        }
        System.out.println();
        for (int i = 0; i < 3; i++) {
            for (int i = 0; i < 4; i++) {
                System.out.print("*");
            }
            System.out.println()
        }
        for (int k = 0; k < 3; k++); {
            System.out.println("k loop");
        }
        System.out.println(k);
    }
}
```

Record each bug in a table: line, what was wrong, compile or logic error, fix.

**Warning:** one of the logic bugs makes the program print for a very long time. Be ready to press **Terminate**.

- **Hint 1:** javac reports only 4 errors at first; more appear once you fix those.
- **Hint 2:** look for: commas, an uninitialised total, `<` vs `<=`, an update going the wrong way, a reused name, a missing `;`, a stray `;`, and scope.

### Task 9 — Debug the Fibonacci loop by hand and with tools

**Class:** `Task09Fibonacci` · **Goal:** practise the three debugging methods from the slides.

```java
int a = 0;
int b = 1;
for (int i = 2; i < 10; i++) {
    int c = a + b;
    a = b;
    b = c;
}
System.out.println(b);
```

1. **By hand:** copy and complete a trace table with columns `i`, `a`, `b`, `c` (values after each iteration). What is printed?
2. **With prints:** add `System.out.println("i=" + i + " a=" + a + " b=" + b + " c=" + c);` as the last line of the body. Does the output match your table?
3. **With Eclipse:** remove the print. Put a breakpoint on `int c = a + b;`, run as **Debug**, and press **Step Over** repeatedly. Watch the Variables view. Write one sentence on which method you found clearest.
4. Change the loop so the program prints the **20th** Fibonacci number. What is it?

- **Hint 1:** with `a = 0, b = 1` before the loop and `i` starting at 2, `b` ends up as the Fibonacci number with position equal to the last value of `i`.
- **Hint 2:** change `i < 10` to `i <= 20`.

### Task 10 — Logic errors the compiler cannot see

**Class:** `Task10Logic` · **Goal:** use the slide's debugging tips (reversed inequality, `&&` vs `||`) and print statements.

Each loop compiles and runs but gives the wrong answer. Find the bug using prints or a trace table, then fix it.

1. Should print `10 9 8 7 6 5 4 3 2 1`:

```java
for (int i = 10; i < 1; i--) {
    System.out.print(i + " ");
}
```

2. Should add up every number from 1 to 100 that is divisible by 3 **or** by 5 (correct answer: 2418):

```java
int total = 0;
for (int i = 1; i <= 100; i++) {
    if (i % 3 == 0 && i % 5 == 0) {
        total += i;
    }
}
System.out.println(total);
```

3. Should print 13! (13 factorial = 13 × 12 × … × 1 = 6,227,020,800):

```java
int f = 1;
for (int i = 1; i <= 13; i++) {
    f *= i;
}
System.out.println("13! = " + f);
```

For each: what does it actually print, what is the cause, and what is the fix?

- **Hint 1:** (1) is a reversed inequality, (2) is `&&` in place of `||`.
- **Hint 2:** for (3), compare the answer with the largest value an `int` can hold (Lab 2), and use `long`.

## Part C — Building with for, break and nesting (Tasks 11–15)

### Task 11 — Sum and average of n numbers

**Class:** `Task11SumAverage` · **Goal:** extend the slide's five-number program.

1. Type the slide's program that reads five numbers and prints the sum and the `int` average. Test with `10 20 30 40 47`. Why is the average 29 and not 29.4?
2. Add a line that prints the exact average.
3. Change the program so it first asks **how many numbers** the user will enter, then reads that many. Print the sum and the average to 2 decimal places.
4. Test with `4` then `10 20 30 45` (expected sum 105, average 26.25), and with `0`. Make sure `0` does not crash or print nonsense.
5. Why is a `for` loop the right choice here, even though you don't know the count when you write the program?

- **Hint 1:** the loop runs `n` times, where `n` is read before the loop.
- **Hint 2:** check `n > 0` before dividing.

### Task 12 — break: where it goes and what it tests

**Class:** `Task12Break` · **Goal:** use `break` and see why its condition and placement matter.

1. Type the slide's BreakSum program (read up to 5 numbers from `numbers.txt`, stop when `sum > 100`). Expected output: `54 40 90`.
2. Create `hundred.txt` containing `60 40 10 5 5`. Run the program on it (change the file name). What is printed, and what is the sum?
3. The slide describes this as "stop if the sum **reaches** 100". Change the condition to match that description. Run again on `hundred.txt`. What changes?
4. Back on `numbers.txt`, move the `if (...) { break; }` so it comes **before** the `System.out.print(...)` line (but after the sum is updated). What is printed now, and why?
5. In one sentence: what does `break` skip?

- **Hint 1:** "reaches 100" means "is 100 or more".
- **Hint 2:** `break` leaves the loop immediately; nothing after it in that iteration runs.

### Task 13 — Official Tutorial 9, Task 2: largest of up to ten numbers

**Class:** `Task13Largest` · **Goal:** a `for` loop with a maximum count, a `break`, and a running maximum.

Using a `for` loop, read **at most ten** positive numbers from the user and display the largest. If the user enters a negative number at any point, the loop must **stop immediately** and print the result as normal.

**Test 1 (from the tutorial):** inputs `1`, `30`, `128`, `60`, `100`, `-1` → `You entered 5 numbers, the largest of which was 128.`

Make your own test plan with at least these cases and run them all:

| Test | Input | Expected |
| --- | --- | --- |
| Tutorial example | `1 30 128 60 100 -1` | 5 numbers, largest 128 |
| Ten numbers, no negative | `5 9 2 7 1 3 8 4 6 10` (then anything) | 10 numbers, largest 10; the 11th value is never read |
| Negative first | `-4` | a sensible message, not "largest 0" |
| Zero | `0 0 -1` | decide: is 0 "positive"? Write down your decision |

- **Hint 1:** the loop header is `for (int i = 0; i < 10; i++)`; inside, read, then `if (number < 0) { break; }`.
- **Hint 2:** count the numbers yourself (do not use `i` after the loop: it no longer exists). Set the largest from the first number accepted.

### Task 14 — Nested shapes

**Class:** `Task14Shapes` · **Goal:** control rows and columns with nested loops.

1. Ask the user for a width and height and print a solid rectangle of `*` (e.g. width 6, height 3).
2. Type the slide's star pyramid. Look closely at the output: why does it not match the picture on the slide (`*`, `**`, …)? Fix it.
3. Print the triangle upside down: 5 stars, then 4, … then 1.
4. Print a **hollow** square of size 5: stars on the border, spaces inside.

```text
*****
*   *
*   *
*   *
*****
```

5. For each shape, write in one sentence what the outer loop controls and what the inner loop controls.

- **Hint 1:** for the upside-down triangle, count the outer loop down: `for (int r = 5; r >= 1; r--)`.
- **Hint 2:** for the hollow square, print `*` when the row is first or last, **or** the column is first or last; otherwise print a space.

### Task 15 — Official Tutorial 9, Task 3 (part 1): number rows

**Class:** `Task15NumberRows` · **Goal:** nested `for` loops where the inner count depends on the outer counter.

Using nested `for` loops, print five rows: the number 1 once in the first row, 2 twice in the second, and so on.

```text
1
22
333
4444
55555
```

Then: change it so each row counts up instead (`1`, `12`, `123`, `1234`, `12345`). What one thing changed?

- **Hint 1:** the outer loop is the row number 1–5; the inner loop runs `row` times.
- **Hint 2:** the first version prints the outer variable; the second prints the inner one.

## Part D — Official tasks and integration (Tasks 16–20)

### Task 16 — Official Tutorial 9, Task 3 (part 2): chessboard

**Class:** `Task16Chessboard` · **Goal:** nested loops plus a condition per cell.

Using nested `for` loops, print an 8-by-8 chessboard. Filled squares (`#`) and unfilled squares (space) alternate and are never next to each other:

```text
# # # # 
 # # # #
# # # # 
 # # # #
# # # # 
 # # # #
# # # # 
 # # # #
```

(Each row is 8 characters. Rows starting with `#` end with a space.)

1. Plan it: for row `r` and column `c` (both starting at 0), when is a square filled? Fill in a 3×3 table of `r + c` values to find the pattern.
2. Make the board size a constant and test with 4 and 10.

- **Hint 1:** look at whether `r + c` is even or odd.
- **Hint 2:** `if ((row + col) % 2 == 0)` prints `#`, `else` prints a space.

### Task 17 — Official Tutorial 9, supplementary: number pyramid

**Class:** `Task17NumberPyramid` · **Goal:** two inner loops per row (spaces, then digits).

Using nested `for` loops, print:

```text
    1
   222
  33333
 4444444
555555555
```

1. Fill in a table first: for row 1–5, how many leading spaces? How many digits?
2. Find a formula for each in terms of the row number and the total number of rows.
3. Make the number of rows a constant. What happens if you set it to 9? To 10?

- **Hint 1:** spaces: 4, 3, 2, 1, 0. Digits: 1, 3, 5, 7, 9.
- **Hint 2:** spaces = `ROWS - row`; digits = `2 * row - 1`.

### Task 18 — Multiplication grid with headings

**Class:** `Task18Grid` · **Goal:** a neat, labelled table built with nested loops and `printf`.

Print a 10×10 multiplication table with a heading row and a heading column:

```text
   |   1   2   3   4   5   6   7   8   9  10
---+----------------------------------------
 1 |   1   2   3   4   5   6   7   8   9  10
 2 |   2   4   6   8  10  12  14  16  18  20
...
10 |  10  20  30  40  50  60  70  80  90 100
```

1. Which parts need a loop on their own (not nested), and which need nested loops?
2. Make the size a constant and test with 5 and 12. What breaks at 12, and how do you fix the column width?

- **Hint 1:** the heading row is one loop over the columns; the dashed line is another; the body is nested.
- **Hint 2:** `%4d` prints a number 4 characters wide; `%2d |` prints the row label.

### Task 19 — Mini-project: how long would it take to guess a PIN?

**Class:** `Task19PinKeyspace` · **Goal:** use nested loops to search every possibility, and see why PIN length and lockouts matter.

This is a toy experiment to understand **brute force** (trying every possible value) on a number you choose yourself. It does not attack anything real.

**Specification:**

1. Store a secret 3-digit code as a constant, e.g. `final int SECRET = 739;`.
2. Use **three nested `for` loops**, one per digit (each 0–9), to build every guess from `000` to `999` in order: `guess = d1 * 100 + d2 * 10 + d3`.
3. Count the guesses. When the guess equals the secret, stop **all three** loops and print `Found 739 after 740 guesses.`
4. Then print a table of how many combinations there are for PINs of 1 to 8 digits, using a `for` loop that multiplies by 10 each time and `%,d` to add thousands separators:

```text
1-digit PIN: 10 combinations
...
8-digit PIN: 100,000,000 combinations
```

**Questions:**

1. `break` only leaves the innermost loop. How did you stop all three? (Use a `boolean` flag, as in Lecture 8.)
2. What is the worst case for a 3-digit code? Which secret gives it?
3. If an attacker could try one guess per second, how long is the worst case for a 4-digit PIN? For a 6-digit PIN? (Work it out in hours and days.)
4. Lab 8 Task 20 locked a card after 3 wrong attempts. Out of 10,000 4-digit PINs, what is the chance of guessing correctly within 3 tries? Explain in two sentences why lockouts matter so much.
5. Why does the combinations table need a `long` once you go past 9 digits?

- **Hint 1:** after the innermost loop, check the flag and `break` again; do the same after the middle loop.
- **Hint 2:** combinations for `n` digits = 10ⁿ; worst case = all of them.

### Task 20 — Assessment-style task: exam results report from a file

**Class:** `ResultsReport` · **Goal:** combine file input, a `for` loop over a known number of records, validation, selection and formatted output.

This is a practice task similar in skills to the module's application assessments. It is **not** an actual assessment question.

**Input file** `results.txt`. The first value is how many student records follow; each record is a name (one word) and a mark:

```text
6
Priya 72
Tom 48
Aisha 91
Leo 150
Maya 64
Ben 55
```

**Specification:**

1. Read the number of records first, then use a `for` loop to read exactly that many records.
2. For each record, print a line in a neat table: name (left-aligned, 10 wide), mark (5 wide), grade (6 wide), using the Lab 8 grade boundaries (A ≥ 70, B 60–69, C 50–59, D < 50).
3. A mark outside 0–100 is **invalid**: print `INVALID` in the grade column and leave it out of all totals.
4. After the table print: how many valid marks out of the total; the count of each grade; the average of the valid marks to 1 decimal place; the top mark and who got it.

**Expected output for the file above:**

```text
Name        Mark  Grade
Priya         72      A
Tom           48      D
Aisha         91      A
Leo          150 INVALID
Maya          64      B
Ben           55      C

Valid marks: 5 of 6
A: 2  B: 1  C: 1  D: 1
Average: 66.0
Top mark: 91 (Aisha)
```

**Test plan** (fill in Actual):

| Test | Change to `results.txt` | Expected | Actual |
| --- | --- | --- | --- |
| 1 | As above | As above | |
| 2 | All marks valid | `Valid marks: 6 of 6` | |
| 3 | Boundary marks 0, 49, 50, 69, 70, 100 | D, D, C, B, A, A | |
| 4 | Every mark invalid | No average or top mark line; no crash | |
| 5 | First line says 6 but only 5 records | What happens? Note it for Lecture 13 (exceptions) | |

**Plan first:** write the algorithm in plain English. Which loop type, and why? Which variables must exist before the loop?

- **Hint 1:** `read.next()` reads the one-word name; `read.nextInt()` reads the mark (Lecture 5).
- **Hint 2:** formats: `"%-10s %5d %6s%n"` for each row; `%-10s` means left-aligned in 10 characters.

## Tracker

| Task | Done | Notes / score |
| --- | --- | --- |
| 1 First for loops | ☐ | |
| 2 Predict (out of 10) | ☐ | |
| 3 for/while conversions | ☐ | |
| 4 Official Task 1: star line | ☐ | |
| 5 Official Task 1: alphabet | ☐ | |
| 6 Braces, semicolons, scope | ☐ | |
| 7 Off by one in a file | ☐ | |
| 8 Bug hunt (out of 8) | ☐ | |
| 9 Fibonacci debugging | ☐ | |
| 10 Logic errors | ☐ | |
| 11 Sum and average of n | ☐ | |
| 12 break placement | ☐ | |
| 13 Official Task 2: largest | ☐ | |
| 14 Nested shapes | ☐ | |
| 15 Official Task 3: number rows | ☐ | |
| 16 Official Task 3: chessboard | ☐ | |
| 17 Official supplementary: pyramid | ☐ | |
| 18 Multiplication grid | ☐ | |
| 19 PIN keyspace mini-project | ☐ | |
| 20 Results report | ☐ | |

## Reflection

1. Explain, as if to a friend, the order in which the three parts of a `for` loop run.
2. When would you choose `for`, `while` and `do...while`? Give one example of each from this lab or Lab 8.
3. What did Task 7 teach you about patching code?
4. Which nested-loop task was hardest, and what finally made it click?
5. What did Task 19 change about how you think about PIN length and lockouts?

## Answer key

All code was compiled and run with Java 21 (javac on the command line, not Eclipse). Outputs shown are actual outputs for the inputs given. Your code may differ and still be correct if it meets the specification.

**Task 1.** (2) `for (int i = 10; i >= 1; i--)`. (3) `for (int i = 2; i <= 20; i += 2)`. (4) `for (int i = 5; i <= 100; i += 5)`. (5):

```java
int sum = 0;
for (int i = 0; i < 100; i++) {
    sum += i;
}
System.out.println("The sum is = " + sum);   // The sum is = 4950
```

**Task 2.** a `1 2 3 4 5` · b `10 7 4 1` · c nothing · d `1 3 9 27` · e `30` (1+4+9+16) · f `abcde` · g `12` · h `1 2 3` · i `1 12 123` · j `1` (the `;` makes an empty loop, so the block runs once). All verified.

**Task 3.** (1) `for (int n = 1; n <= 20; n = n + 3)` prints `1 4 7 10 13 16 19`. (2) `int k = 100; while (k > 0) { System.out.print(k + " "); k = k / 2; }` prints `100 50 25 12 6 3 1`. (3) `int total = 0; for (int i = 0; i < 10; i++) { total += i; }` prints `45`. In the `for` version `i` disappears after the loop, so later code cannot accidentally use or change it.

**Task 4.**

```java
import java.util.Scanner;

public class StarLine {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        System.out.print("How many stars? ");
        int n = console.nextInt();
        for (int i = 0; i < n; i++) {
            System.out.print("*");
        }
        System.out.println();
        console.close();
    }
}
```

Input `5` → `*****`. Input `0` → an empty line: the condition `0 < 0` is false at the start, so the loop runs zero times, which is exactly right for "zero stars".

**Task 5.**

```java
public class Letters {
    public static void main(String[] args) {
        for (char letter = 'A'; letter <= 'Z'; letter++) {
            System.out.print(letter);
        }
        System.out.println();
        for (char letter = 'Z'; letter >= 'A'; letter--) {      // backwards
            System.out.print(letter);
        }
        System.out.println();
        for (char letter = 'A'; letter <= 'Z'; letter += 2) {   // every other letter
            System.out.print(letter);
        }
        System.out.println();
        for (char letter = 'a'; letter <= 'e'; letter++) {      // lower case with codes
            System.out.print(letter + "=" + (int) letter + " ");
        }
        System.out.println();
    }
}
```

Output (verified):

```text
ABCDEFGHIJKLMNOPQRSTUVWXYZ
ZYXWVUTSRQPONMLKJIHGFEDCBA
ACEGIKMOQSUWY
a=97 b=98 c=99 d=100 e=101
```

`letter++` works because a `char` is stored as a number (its UTF-16 code); `'A'` is 65 and `'B'` is 66.

**Task 6.** Snippet 1 prints `Hello` five times and `*` once; add braces. Snippet 2 prints `in body` once; remove the `;`. Snippet 3: `error: cannot find symbol` for `m`; declare `int m;` before the loop and use `for (m = 0; ...)`, which then prints `0 1 2 3 4 5`. Snippet 4: `error: ';' expected`; use semicolons. Curly quotes: `error: illegal character: '“'`. All verified.

**Task 7.** (1) `54 40 90 68 75 Exception in thread "main" java.util.NoSuchElementException`. (2) Six times; the crash happens when `i` is 5 (the sixth read). (3) `for (int i = 0; i < 5; i++)` or `for (int i = 1; i <= 5; i++)` (both verified). (4) The patch hides the real mistake instead of fixing it, wastes an iteration, makes the code harder to read, and is easy to break when the loop is changed later. (5) An EOF-controlled `while (read.hasNextInt())` loop.

**Task 8.** The 8 bugs: (1) commas in the first header → semicolons; (2) `int sum;` not initialised → `int sum = 0;`; (3) `i < 5` adds only 1–4 (sum 10) → `i <= 5`; (4) countdown uses `i++` so `i` grows instead of shrinking (prints for billions of iterations until overflow) → `i--`; (5) inner loop reuses `i` → `j`; (6) missing `;` after `System.out.println()`; (7) stray `;` after the `k` loop header → remove; (8) `k` used after the loop → declare `int k;` before it and use `for (k = 0; ...)`. First compile shows only 4 errors (verified). Fixed output (verified):

```text
1 2 3 4 5 6 7 8 9 10
Sum: 15
5 4 3 2 1
****
****
****
k loop
k loop
k loop
3
```

**Task 9.** Trace as in Lecture 9, section 13; the program prints `34`. The debug prints match the table row by row (verified). The 20th Fibonacci number is `6765` (verified with `i <= 20`).

**Task 10.** (1) Prints nothing: `10 < 1` is false at the start (reversed inequality). Fix: `i >= 1`. (2) Prints `315` (only multiples of 15) instead of `2418`. Fix: `||`. (3) Prints `13! = 1932053504`: the true value is larger than the biggest `int` (2,147,483,647), so it overflows. Fix: `long f = 1;`. All verified.

**Task 11.**

```java
import java.util.Scanner;

public class SumAverageN {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        System.out.print("How many numbers? ");
        int n = console.nextInt();
        int sum = 0;
        for (int i = 1; i <= n; i++) {
            System.out.print("Number " + i + ": ");
            sum = sum + console.nextInt();
        }
        System.out.println();
        if (n > 0) {
            System.out.printf("Sum: %d, average: %.2f%n", sum, (double) sum / n);
        } else {
            System.out.println("No numbers to average.");
        }
        console.close();
    }
}
```

`4` then `10 20 30 45` → `Sum: 105, average: 26.25`. `0` → `No numbers to average.` (verified). The slide version gives 29 because `sum / 5` is integer division. A `for` loop fits because the program knows the count (`n`) before the loop starts.

**Task 12.** (1) `54 40 90`, sum 184. (2) With `> 100` on `hundred.txt`: `60 40 10`, sum 110. (3) With `>= 100`: `60 40`, sum 100: it now stops as soon as the sum reaches exactly 100. (4) With the `break` before the print on `numbers.txt`: `54 40` (sum 184): the third number is added but never printed, because `break` skips the rest of that iteration. (5) `break` skips everything after it in the current iteration, the update expression, and all remaining iterations. All verified.

**Task 13.**

```java
import java.util.Scanner;

public class LargestPositive {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        final int MAX_NUMBERS = 10;
        int count = 0;
        int largest = 0;
        for (int i = 0; i < MAX_NUMBERS; i++) {
            int number = console.nextInt();
            if (number < 0) {
                break;                       // negative: stop immediately
            }
            count++;
            if (count == 1 || number > largest) {
                largest = number;
            }
        }
        if (count == 0) {
            System.out.println("You entered no positive numbers.");
        } else {
            System.out.println("You entered " + count + " numbers, the largest of which was " + largest + ".");
        }
        console.close();
    }
}
```

Verified results: tutorial example → `You entered 5 numbers, the largest of which was 128.`; ten numbers then `99` → `You entered 10 numbers, the largest of which was 10.` (the 99 is never read); `-4` → `You entered no positive numbers.`; `0 0 -1` → `You entered 2 numbers, the largest of which was 0.` The tutorial says "positive" but only says to stop on a **negative**, so this answer accepts 0. If you decide 0 is not positive, add a check and write your decision in your notes; it is worth asking your tutor.

**Task 14.** Rectangle: outer loop over `height` rows, inner over `width` columns. The slide pyramid prints `" *"`, so every star has a space before it (verified); print `"*"` instead. Upside down: `for (int r = 5; r >= 1; r--) { for (int c = 1; c <= r; c++) { ... } }`. Hollow square:

```java
final int SIZE = 5;
for (int r = 1; r <= SIZE; r++) {
    for (int c = 1; c <= SIZE; c++) {
        if (r == 1 || r == SIZE || c == 1 || c == SIZE) {
            System.out.print("*");
        } else {
            System.out.print(" ");
        }
    }
    System.out.println();
}
```

**Task 15.**

```java
public class NumberRows {
    public static void main(String[] args) {
        for (int row = 1; row <= 5; row++) {
            for (int col = 1; col <= row; col++) {
                System.out.print(row);
            }
            System.out.println();
        }
    }
}
```

Output verified as in the task. For `1`, `12`, `123`, … print `col` instead of `row`.

**Task 16.**

```java
public class Chessboard {
    public static void main(String[] args) {
        final int SIZE = 8;
        for (int row = 0; row < SIZE; row++) {
            for (int col = 0; col < SIZE; col++) {
                if ((row + col) % 2 == 0) {
                    System.out.print("#");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }
    }
}
```

Output verified to match the tutorial's pattern exactly (8 characters per row). A square is filled when `row + col` is even.

**Task 17.**

```java
public class NumberPyramid {
    public static void main(String[] args) {
        final int ROWS = 5;
        for (int row = 1; row <= ROWS; row++) {
            for (int s = 1; s <= ROWS - row; s++) {      // leading spaces
                System.out.print(" ");
            }
            for (int d = 1; d <= 2 * row - 1; d++) {     // 1, 3, 5, 7, 9 digits
                System.out.print(row);
            }
            System.out.println();
        }
    }
}
```

Output verified. With 9 rows it still works; with 10 rows the last row prints `10` nineteen times (two characters each), so the pyramid loses its shape.

**Task 18.**

```java
public class MultiplicationGrid {
    public static void main(String[] args) {
        final int SIZE = 10;
        System.out.print("   |");
        for (int col = 1; col <= SIZE; col++) {
            System.out.printf("%4d", col);
        }
        System.out.println();
        System.out.print("---+");
        for (int col = 1; col <= SIZE; col++) {
            System.out.print("----");
        }
        System.out.println();
        for (int row = 1; row <= SIZE; row++) {
            System.out.printf("%2d |", row);
            for (int col = 1; col <= SIZE; col++) {
                System.out.printf("%4d", row * col);
            }
            System.out.println();
        }
    }
}
```

Output verified as in the task. At size 12 the numbers still fit in `%4d` (largest 144), so the grid stays aligned. It breaks at size 32, where 32 × 32 = 1024 needs 4 digits with no space left between columns; widen to `%5d`.

**Task 19.**

```java
public class PinKeyspace {
    public static void main(String[] args) {
        final int SECRET = 739;                  // a 3-digit "PIN" for the experiment
        int guesses = 0;
        boolean found = false;

        for (int d1 = 0; d1 <= 9; d1++) {
            for (int d2 = 0; d2 <= 9; d2++) {
                for (int d3 = 0; d3 <= 9; d3++) {
                    guesses++;
                    int guess = d1 * 100 + d2 * 10 + d3;
                    if (guess == SECRET) {
                        found = true;
                        break;                   // leaves only the innermost loop
                    }
                }
                if (found) {
                    break;
                }
            }
            if (found) {
                break;
            }
        }
        System.out.println("Found " + SECRET + " after " + guesses + " guesses.");

        // How big is the search space for longer PINs?
        long combinations = 1;
        for (int digits = 1; digits <= 8; digits++) {
            combinations = combinations * 10;
            System.out.printf("%d-digit PIN: %,d combinations%n", digits, combinations);
        }
    }
}
```

Output (verified): `Found 739 after 740 guesses.` then the table from 10 to 100,000,000. Answers: (2) worst case 1,000 guesses, for secret `999`. (3) 4 digits: 10,000 seconds ≈ 2.8 hours; 6 digits: 1,000,000 seconds ≈ 11.6 days. (4) 3 in 10,000, i.e. 0.03%: a lockout turns an attack that is certain to succeed within hours into one that almost always fails. (5) An `int` holds up to about 2.1 billion, so 10 digits (10,000,000,000) would overflow.

**Task 20.**

```java
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Scanner;

public class ResultsReport {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner read = new Scanner(new FileReader("results.txt"));
        int students = read.nextInt();                 // first value: how many records follow

        int valid = 0, total = 0;
        int countA = 0, countB = 0, countC = 0, countD = 0;
        int best = -1;
        String bestName = "";

        System.out.printf("%-10s %5s %6s%n", "Name", "Mark", "Grade");
        for (int i = 1; i <= students; i++) {
            String name = read.next();
            int mark = read.nextInt();
            if (mark < 0 || mark > 100) {
                System.out.printf("%-10s %5d %6s%n", name, mark, "INVALID");
            } else {
                String grade;
                if (mark >= 70) {
                    grade = "A";
                    countA++;
                } else if (mark >= 60) {
                    grade = "B";
                    countB++;
                } else if (mark >= 50) {
                    grade = "C";
                    countC++;
                } else {
                    grade = "D";
                    countD++;
                }
                System.out.printf("%-10s %5d %6s%n", name, mark, grade);
                valid++;
                total = total + mark;
                if (mark > best) {
                    best = mark;
                    bestName = name;
                }
            }
        }
        read.close();

        System.out.println();
        System.out.println("Valid marks: " + valid + " of " + students);
        System.out.println("A: " + countA + "  B: " + countB + "  C: " + countC + "  D: " + countD);
        if (valid > 0) {
            System.out.printf("Average: %.1f%n", (double) total / valid);
            System.out.println("Top mark: " + best + " (" + bestName + ")");
        }
    }
}
```

Test 1 output verified to match the expected output exactly. A `for` loop fits because the file says in advance how many records there are. Test 5: the program crashes with `NoSuchElementException` when it tries to read the missing record; handling that gracefully needs exceptions, later in the module.

**Next:** Lecture 10. The slides say arrays come next, where `for` loops and avoiding off-by-one errors are essential.
