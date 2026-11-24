# Lab 8 — Repetition (while and do-while) Hands-on Workbook (20 Tasks)

**Module:** 4300COMP Introduction to Programming · **Language:** Java

## How to use this lab

This lab has **20 hands-on tasks** on Lecture 8: `while` loops, the four ways of controlling a loop (counter, sentinel, flag, end-of-file), `do...while`, input validation, infinite loops and off-by-one errors. **All three official Tutorial 8 tasks and the supplementary task are included** (Tasks 3, 15, 16, 17, 18 and 19), marked "official".

**Learning outcomes:** MLO1 (loops and basic algorithms: totals, counting, maximum, minimum), MLO3 (Tasks 15–20 turn written specifications into working programs).

**Setup:** create a Java project called **Lab08** in Eclipse. Untick *Create module-info.java*. Make one class per task and tick `public static void main(String[] args)` when you create it. Programs that read files expect the file in the **project folder** (the folder that contains `src`), as in Lab 5.

**Rules for this lab:**

1. **Predict before you run.** For every "predict" task, write your answer down first. Being wrong and finding out why is how you learn tracing.
2. **Trace with a table.** When a loop surprises you, draw a trace table: one row per iteration, one column per variable, plus a column for the condition.
3. **Initialise, test, update.** Before you run any loop, point at the three parts. If you cannot find all three, the loop is probably wrong.
4. **If a program freezes,** it is almost certainly an infinite loop. Press the red square **Terminate** button on the Console view, then find the missing or wrong update.
5. Use the hints only after a real attempt. Hint 1 names the idea, hint 2 gives the next step.
6. Assume users type whole numbers when asked for whole numbers. Handling text typed by mistake needs exceptions, which come later.

**The tracker** at the end lets you tick off each task. The **answer key** is at the very end; every answer was compiled and run with Java 21 using javac on the command line (not Eclipse), with the inputs shown.

## Part A — Counter-controlled loops (Tasks 1–5)

### Task 1 — Your first while loop

**Class:** `Task01Counting` · **Goal:** write a counter loop and change each of its three parts.

1. Write a `while` loop that prints the numbers 1 to 10, one per line.
2. Label the three parts with comments: `// initialise`, `// test`, `// update`.
3. Change it so it prints 10 down to 1.
4. Change it so it prints `0 3 6 9 12 15 18` on **one** line.
5. Change it so it prints only the even numbers from 2 to 20 on one line, **without** using `%`.

- **Hint 1:** for one line, use `System.out.print(n + " ");` inside the loop and one `System.out.println();` after it.
- **Hint 2:** for counting down, the start value, the condition **and** the update all change.

### Task 2 — Predict the output

**Class:** `Task02Predict` · **Goal:** trace counter loops in your head.

Write your prediction for each snippet in the table **before** running anything. Then put all eight into one `main` method and check. Each snippet uses `System.out.print(... + " ")` unless it says `println`.

| | Code | Your prediction | Actual |
| --- | --- | --- | --- |
| a | `int n = 1; while (n <= 5) { print n; n = n + 1; }` | | |
| b | `int n = 10; while (n > 0) { print n; n = n - 3; }` | | |
| c | `int n = 5; while (n < 5) { print n; n = n + 1; }` | | |
| d | `int n = 1; while (n < 100) { print n; n = n * 2; }` | | |
| e | `int n = 0; int total = 0; while (n < 5) { total = total + n; n = n + 1; }` then `println(total)` | | |
| f | `int n = 20; while (n % 7 != 0) { n = n + 1; }` then `println(n)` | | |
| g | `int a = 1, b = 1; while (b < 50) { print b; int t = a + b; a = b; b = t; }` | | |
| h | `int n = 3; int count = 0; while (n != 1) { if (n % 2 == 0) { n = n / 2; } else { n = 3 * n + 1; } count = count + 1; }` then `println(count)` | | |

Score yourself out of 8 and record it in the tracker.

- **Hint 1:** for (c), check the condition **before** the first iteration.
- **Hint 2:** for (h), write each value of `n` in a row: 3, 10, …

### Task 3 — Official Tutorial 8, Task 1: trace While Loop 1

**Class:** `Task03Trace` · **Goal:** trace a loop with two changing variables.

**Without typing it in first,** describe the output of:

```java
int k = 9;
int i = -6;
while (i <= k) {
    i = i + 2;
    k = k - 1;
    System.out.printf("i + k = %d\n", i + k);
}
```

1. Copy and complete this trace table on paper:

| Iteration | `i <= k` tested | `i` after | `k` after | Printed |
| --- | --- | ---: | ---: | --- |
| 1 | −6 <= 9 → true | | | |
| 2 | | | | |
| … | | | | |

2. How many lines are printed? What are `i` and `k` when the loop ends?
3. Then type it into Eclipse and verify your answer, as the tutorial asks.

- **Hint 1:** the printing happens **after** both updates in the same iteration.
- **Hint 2:** each iteration, `i` goes up by 2 and `k` goes down by 1, so the gap closes by 3.

### Task 4 — Sums (from the Tutorial 8 introduction)

**Class:** `Task04Sums` · **Goal:** use a running total.

1. Type in the tutorial's example that adds the numbers 0 to 99 and prints `The sum is = ...`. Predict the answer first.
2. Change it to add **1 to 100**.
3. Add a second loop that adds only the **even** numbers from 2 to 100.
4. Add a third loop that adds only the **odd** numbers from 1 to 99.
5. Check: what should the even sum plus the odd sum equal?

- **Hint 1:** for evens, start at 2 and add 2 each time.
- **Hint 2:** each loop needs its own `sum` reset to 0 (or a different variable).

### Task 5 — Times table

**Class:** `Task05TimesTable` · **Goal:** combine a counter loop with input and `printf`.

Ask the user which times table they want, then print 1 to 12 times it, neatly lined up:

```text
Which times table? 7
7 x  1 =   7
7 x  2 =  14
...
7 x 12 =  84
```

- **Hint 1:** `%2d` prints a whole number in a space 2 characters wide (Lecture 4).
- **Hint 2:** the counter goes from 1 to 12; the table number comes from `nextInt()`.

## Part B — Find and fix loop bugs (Tasks 6–10)

### Task 6 — Infinite loop clinic

**Class:** `Task06Infinite` · **Goal:** recognise and fix the four common causes of infinite loops.

Each loop below is meant to stop but does not. Run them **one at a time** (comment the others out), and be ready to press **Terminate**. For each: (a) explain why it never stops, (b) fix it.

```java
// Loop 1: should print 0 to 4
int i = 0;
while (i < 5) {
    System.out.println(i);
}

// Loop 2: should print 10 down to 1
int j = 10;
while (j > 0) {
    System.out.println(j);
    j = j + 1;
}

// Loop 3: should print 0 to 4
int k = 0;
while (k < 5); {
    System.out.println(k);
    k = k + 1;
}

// Loop 4: should stop when d reaches 1.0
double d = 0;
while (d != 1.0) {
    d = d + 0.1;
}
```

Extra questions:

1. Loop 3 compiles with no errors. Why does it print **nothing at all**?
2. Loop 2 is not truly infinite: it eventually stops. Using what you learned about `int` overflow in Lab 2, explain why. (Do not wait for it; it would print over 2 billion lines.)
3. For Loop 4, add a print inside the loop that shows `d` each time, but stop after 12 iterations by also counting. What value is printed where you expected `1.0`?

- **Hint 1:** look for: a missing update, an update in the wrong direction, a stray `;`, and `!=` with decimals.
- **Hint 2:** for Loop 4, change the condition to `d < 1.0` or use a counter.

### Task 7 — Off-by-one clinic

**Class:** `Task07OffByOne` · **Goal:** fix loops that run once too many or once too few.

Each loop runs, but gives the wrong result. Predict what it actually prints, run it, then fix it with the **smallest possible change**.

| Intention | Code |
| --- | --- |
| Print 1 to 10 | `int i = 1; while (i < 10) { print i; i = i + 1; }` |
| Print exactly 5 stars | `int i = 0; while (i <= 5) { print "*"; i = i + 1; }` |
| Count down 5 to 1, then print `Lift off!` | `int i = 5; while (i >= 0) { print i; i = i - 1; } println("Lift off!");` |

Then write one sentence explaining how to work out how many times a loop will run **without** running it.

- **Hint 1:** list the first and last value the body actually sees.
- **Hint 2:** for steps of 1, the number of iterations is last − first + 1.

### Task 8 — Sentinel sum, count and average

**Class:** `Task08SentinelStats` · **Goal:** extend the slide's sentinel loop.

1. Type the slide's program (read integers until `0`, print the sum). Test with `50 100 -30 0`. Expected: `The sum of the numbers is: 120`.
2. Extend it to also count how many numbers were entered (not counting the `0`) and print the average to 2 decimal places:

```text
Count: 3, sum: 120, average: 40.00
```

3. Test with just `0`. What happens to your average? Fix it so it prints `No numbers entered.` instead.

- **Hint 1:** `(double) sum / count` avoids integer division.
- **Hint 2:** test `count == 0` **before** dividing.

### Task 9 — Highest and lowest

**Class:** `Task09MaxMin` · **Goal:** find the maximum and minimum of an unknown number of values.

Read temperatures (whole numbers, can be negative) until the user enters `-999`. Print the highest and lowest.

```text
Enter temperatures, -999 to finish: 12 -3 8 21 5 -999
Highest: 21, lowest: -3
```

1. Why is `-999` a sensible sentinel here, but `-1` or `0` would not be?
2. First try starting `max` and `min` at `0`. Test with `12 8 21 5 -999`. Which answer is wrong and why?
3. Fix it by starting both at the **first** value read.
4. Handle `-999` as the very first input: print `No temperatures entered.`

- **Hint 1:** the priming read gives you the first value; use it to set both `max` and `min`.
- **Hint 2:** inside the loop, two separate `if` statements (not `else if`) update `max` and `min`.

### Task 10 — Guessing game with a counter

**Class:** `Task10Guess` · **Goal:** combine a flag with a counter.

1. Type the slide's GuessingGame (flag-controlled). Add the `Scanner` and imports the slide leaves out.
2. While testing, replace the random number with a fixed one: `int secret = 37;`.
3. Change the range to 1–100 and the messages to `Too high.` and `Too low.`.
4. Count the guesses. When correct, print `Correct! You needed N guesses.` after the loop.
5. Test with `50`, `25`, `37`. Expected: `Too high.`, `Too low.`, then `Correct! You needed 3 guesses.`
6. Put the random number back: `ran.nextInt(100) + 1`. Why `+ 1`?
7. **Think:** if you always guess the middle of the remaining range, what is the most guesses you could ever need for 1–100?

- **Hint 1:** the counter increases on **every** guess, right after reading it.
- **Hint 2:** `nextInt(100)` gives 0–99.

## Part C — EOF loops and do...while (Tasks 11–14)

### Task 11 — Reading a file to the end

**Class:** `Task11LineNumbers` · **Goal:** use an EOF-controlled loop and see why sentinels in files are risky.

Create `prog.txt` in the project folder with exactly these five lines:

```text
This is a sample text file.
It contains some data.
This is the last line.
Really?
This is the last line.
```

1. Type the slide's ReadLines program. Run it. What is printed?
2. Change it to use `hasNextLine()` and print a line number before each line, then the total:

```text
1: This is a sample text file.
...
5: This is the last line.
Total lines: 5
```

3. Now write a **sentinel** version that reads lines until it reads `This is the last line.` (compare Strings with `.equals()`, Lecture 6). How many lines does it print? What does this tell you about using a "last line" sentinel in files?

- **Hint 1:** the line number is a counter that starts at 0 and goes up by 1 each iteration.
- **Hint 2:** the sentinel version needs a priming `nextLine()` before the loop.

### Task 12 — End of input from the keyboard

**Class:** `Task12EofSum` · **Goal:** use EOF with console input.

1. Type the slide's EofSum program. Run it, type `50 100 -30`, press Enter, then signal end of input: **Ctrl+Z** on Windows, **Ctrl+D** on macOS or Linux. Click inside the Console first. Expected: `The sum of the numbers is: 120`.
2. Write down what happened on your computer. If the key press did not work in Eclipse, note it and ask in your lab.
3. Why does this loop **not** need a priming read, when the sentinel loop in Task 8 does?

- **Hint 1:** `hasNext()` looks ahead without reading anything.

### Task 13 — do...while predictions

**Class:** `Task13DoWhile` · **Goal:** understand "at least once".

Predict, then run:

| | Code | Your prediction | Actual |
| --- | --- | --- | --- |
| a | `int i = 0; do { print i; i = i + 5; } while (i <= 20);` | | |
| b | Same as (a) but `int i = 21;` | | |
| c | `int i = 21; while (i <= 20) { print i; i = i + 5; }` | | |
| d | `int n = 3; do { print n; n = n - 1; } while (n > 0);` | | |
| e | `int n = 1; do { n = n * 3; } while (n < 50);` then `println(n)` | | |
| f | Same as (e) but `int n = 100;` | | |

Then: remove the semicolon after `while (i <= 20)` in (a). Write down the exact error message.

- **Hint 1:** in (b) and (f) the body runs once before the condition is ever tested.

### Task 14 — Input validation, two ways

**Class:** `Task14Validate` · **Goal:** compare `do...while` validation with a flag-controlled `while`.

1. Type the slide's do...while score validator (score must be 0–10). Test with `15`, `-2`, `7`.
2. The user is never told **why** they are being asked again. Write a second version using a flag-controlled `while` that prints, for example, `Error: 15 is not between 0 and 10. Try again.`
3. Test both with the same inputs and compare the output.
4. In one or two sentences: which version is better for the user, and which is shorter to write?
5. **Cyber security link:** name one real program where refusing out-of-range input matters (for example an age, a quantity, a port number) and what could go wrong without it.

- **Hint 1:** the flag is `boolean valid = false;` and the loop is `while (!valid)`.
- **Hint 2:** give `score` a starting value, or Java will complain it might not be initialised.

## Part D — Official tutorial tasks and integration (Tasks 15–20)

The grade table for Tasks 15–18 (official Tutorial 8, Task 2):

| Exam mark condition | Grade |
| --- | --- |
| mark ≥ 70 | A |
| 60 ≤ mark < 70 | B |
| 50 ≤ mark < 60 | C |
| mark < 50 | D |

### Task 15 — Official Tutorial 8, Task 2: six exam marks

**Class:** `Task15SixMarks` · **Goal:** a counter-controlled loop with selection inside.

Write a program that:

- accepts **six** exam marks (as percentages),
- converts each mark to its grade,
- outputs the number of students who got A, B and C grades separately. (Print D too; it costs one line and helps you check the counts add up to 6.)

**Test:** `72 65 48 55 90 61` → A: 2, B: 2, C: 1, D: 1.

**Plan first** in plain English or pseudocode: which variables do you need before the loop? What happens inside it? What is printed after it?

- **Hint 1:** you need four counters, all starting at 0, plus a loop counter for the six students.
- **Hint 2:** inside the loop, use an `if...else if...else` chain from the top grade down (Lecture 7), so each condition only needs one comparison.

### Task 16 — Official Tutorial 8, Task 3 (part 1): any number of students, sentinel

**Class:** `Task16GradesSentinel` · **Goal:** change a counter loop into a sentinel loop.

Classes rarely have exactly six students. Change Task 15 so the teacher types marks until they enter `-1`. Also print how many students were entered.

**Tests:**

| Input | Expected |
| --- | --- |
| `72 65 48 55 90 61 39 70 -1` | Students: 8, A: 3, B: 2, C: 1, D: 2 |
| `-1` | Students: 0, all counts 0 |

- **Hint 1:** use the priming-read pattern from Lecture 8, section 7.
- **Hint 2:** make `-1` a constant: `final int SENTINEL = -1;`.

### Task 17 — Official Tutorial 8, Task 3 (part 2): end-of-file

**Class:** `Task17GradesEOF` · **Goal:** the same job with an EOF-controlled loop.

Create `marks.txt` in the project folder:

```text
72 65 48 55
90 61 39 70
```

Read **all** marks until the end of the file and print the same summary as Task 16. Expected: Students: 8, A: 3, B: 2, C: 1, D: 2.

1. Does it matter that the marks are on two lines? Why not?
2. Add the word `absent` at the end of the file and run again. What happens with `hasNextInt()` as the condition? What would happen with `hasNext()` and `nextInt()`?
3. **Optional:** do the same with keyboard input and Ctrl+Z / Ctrl+D (as in Task 12).

- **Hint 1:** use `while (read.hasNextInt())` with `int mark = read.nextInt();` inside.
- **Hint 2:** don't forget `throws FileNotFoundException` on `main` and `read.close()` after the loop (Lecture 5).

### Task 18 — Official Tutorial 8, Task 3 (part 3): validate every mark

**Class:** `Task18GradesValidated` · **Goal:** use a `do...while` to make sure every mark entered is a valid percentage.

To avoid typing mistakes, extend Task 16 so that every mark must be between 0 and 100. If the teacher types something else, ask again for that mark. `-1` must still finish entry.

**Test:** `72 150 65 -5 48 -1` → the program asks again after `150` and after `-5`; final result Students: 3, A: 1, B: 1, C: 0, D: 1.

1. Write the condition for "invalid **and** not the sentinel" before you write any code.
2. **Improve it:** print `150 is not a valid percentage.` when a mark is rejected. Which loop style from Task 14 makes this easier?

- **Hint 1:** an inner `do...while` reads **one** valid mark (or the sentinel); the outer loop processes marks until the sentinel.
- **Hint 2:** the inner condition is `(mark < 0 || mark > 100) && mark != SENTINEL`.

### Task 19 — Official Tutorial 8, supplementary: largest factor of 3195

**Class:** `Task19LargestFactor` · **Goal:** use a loop to search for an answer.

The factors of a number are the numbers that divide into it exactly, including 1 and the number itself (the factors of 6 are 1, 2, 3 and 6). Write a program to find the **largest factor of 3195, excluding 3195 itself**.

1. First method: start at 3194 and count **down** until you find a number that divides 3195 exactly (`%` gives 0). How many iterations does it take?
2. Second method: find the **smallest** factor above 1 by counting **up** from 2, then divide 3195 by it. Why does this give the same answer much faster?
3. Make the number a constant so you can test other values. What does your program print for a prime number such as 13?

- **Hint 1:** this is a loop where the **condition** does the searching and the body only updates: `while (NUMBER % candidate != 0)`.
- **Hint 2:** the largest factor × the smallest factor (above 1) = the number.

### Task 20 — Assessment-style task: PIN entry with lockout

**Class:** `PinLockout` · **Goal:** combine a counter, a flag, `do...while` validation and selection in one program.

This is a practice task similar in skills to the module's application assessments. It is **not** an actual assessment question.

**Specification:**

1. The correct PIN is stored as a constant: `4821`. The maximum number of attempts is a constant: `3`.
2. The program asks: `Enter your 4-digit PIN: `.
3. If the input is not between 1000 and 9999, print `A PIN must have exactly 4 digits.` and ask again. A badly formatted PIN does **not** use up an attempt.
4. A correctly formatted but wrong PIN uses one attempt and prints `Incorrect PIN. N attempt(s) left.` (do not print this after the last attempt).
5. The program stops as soon as the PIN is correct, or after 3 wrong attempts.
6. At the end it prints either `Access granted after N attempt(s).` or `Card locked. Contact your bank.`

**Test plan** (fill in the Actual column):

| Test | Input | Expected | Actual |
| --- | --- | --- | --- |
| 1 Correct first time | `4821` | `Access granted after 1 attempt(s).` | |
| 2 Correct on the last attempt, with a format error | `1111`, `482`, `2222`, `4821` | two "Incorrect" messages, one "4 digits" message, then `Access granted after 3 attempt(s).` | |
| 3 Three wrong PINs | `1111`, `2222`, `3333` | `Incorrect PIN. 2 attempt(s) left.`, `... 1 attempt(s) left.`, `Card locked. Contact your bank.` | |
| 4 Boundary | `999`, `10000`, `1000`, ... | your choice: write it | |

**Plan first:** write the algorithm in plain English. Then identify which variable is the counter, which is the flag, and which loop does the validation.

**Learning note:** real systems never store a PIN or password as plain text in the code. This is a toy program for practising loops; in later modules you will see how real systems store secrets (for example, hashing).

- **Hint 1:** outer loop condition: `while (!unlocked && attempts < MAX_ATTEMPTS)`.
- **Hint 2:** the validation `do...while` goes **inside** the outer loop, before `attempts` is increased.

## Tracker

| Task | Done | Notes / score |
| --- | --- | --- |
| 1 First while loop | ☐ | |
| 2 Predict (out of 8) | ☐ | |
| 3 Official Task 1 trace | ☐ | |
| 4 Sums | ☐ | |
| 5 Times table | ☐ | |
| 6 Infinite loop clinic | ☐ | |
| 7 Off-by-one clinic | ☐ | |
| 8 Sentinel stats | ☐ | |
| 9 Highest and lowest | ☐ | |
| 10 Guessing game with counter | ☐ | |
| 11 Reading a file to the end | ☐ | |
| 12 EOF from the keyboard | ☐ | |
| 13 do...while predictions (out of 6) | ☐ | |
| 14 Validation two ways | ☐ | |
| 15 Official Task 2: six marks | ☐ | |
| 16 Official Task 3: sentinel | ☐ | |
| 17 Official Task 3: EOF | ☐ | |
| 18 Official Task 3: do-while validation | ☐ | |
| 19 Official supplementary: largest factor | ☐ | |
| 20 PIN lockout | ☐ | |

## Reflection

1. In your own words, what is the difference between `while` and `do...while`? Give one situation for each.
2. Which of the four control methods (counter, sentinel, flag, EOF) did you find hardest, and why?
3. What was the most useful bug you found today, and how did you find it?
4. Could you write Task 16 again tomorrow without looking at your code? If not, which part would you get stuck on?

## Answer key

All code was compiled and run with Java 21 (javac on the command line, not Eclipse). Outputs shown are the actual outputs for the inputs given. Your programs may differ and still be correct, as long as they meet the specification.

**Task 1.**

```java
int n = 1;                          // initialise
while (n <= 10) {                   // test
    System.out.println(n);
    n = n + 1;                      // update
}
```

Down: `n = 10; while (n >= 1) { ...; n = n - 1; }`. Steps of 3: `n = 0; while (n <= 18) { System.out.print(n + " "); n = n + 3; }`. Evens: `n = 2; while (n <= 20) { ...; n = n + 2; }`.

**Task 2.** a `1 2 3 4 5` · b `10 7 4 1` · c nothing (the condition is false at the first test) · d `1 2 4 8 16 32 64` · e `10` · f `21` · g `1 2 3 5 8 13 21 34` (Fibonacci numbers below 50) · h `7` (3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 is 7 steps).

**Task 3.**

| Iteration | `i <= k` tested | `i` after | `k` after | Printed |
| --- | --- | ---: | ---: | --- |
| 1 | −6 <= 9 true | −4 | 8 | `i + k = 4` |
| 2 | −4 <= 8 true | −2 | 7 | `i + k = 5` |
| 3 | −2 <= 7 true | 0 | 6 | `i + k = 6` |
| 4 | 0 <= 6 true | 2 | 5 | `i + k = 7` |
| 5 | 2 <= 5 true | 4 | 4 | `i + k = 8` |
| 6 | 4 <= 4 true | 6 | 3 | `i + k = 9` |
| – | 6 <= 3 **false** | | | loop ends |

Six lines, `i + k = 4` up to `i + k = 9`. At the end `i` is 6 and `k` is 3. (Each iteration `i + k` grows by 1 because `i` gains 2 and `k` loses 1.)

**Task 4.** 0 to 99: `4950`. 1 to 100: `5050`. Evens 2–100: `2550`. Odds 1–99: `2500`. 2550 + 2500 = 5050, the sum of 1 to 100.

**Task 5.**

```java
import java.util.Scanner;

public class TimesTable {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        System.out.print("Which times table? ");
        int table = console.nextInt();
        int i = 1;
        while (i <= 12) {
            System.out.printf("%d x %2d = %3d\n", table, i, table * i);
            i = i + 1;
        }
        console.close();
    }
}
```

**Task 6.** Loop 1: no update; add `i = i + 1;`. Loop 2: the update goes the wrong way; use `j = j - 1;`. Loop 3: the `;` after `while (k < 5)` is an empty body, so the loop tests `k < 5` forever and never reaches the block; remove the `;` (verified: it compiles, then hangs with no output). Loop 4: `d` never equals exactly 1.0; use `while (d < 1.0)`.

Extra 2: `j` keeps growing until it passes the largest `int` (2,147,483,647) and overflows to −2,147,483,648, which makes `j > 0` false. Verified: 2,147,483,638 iterations. Extra 3: after ten additions `d` is `0.9999999999999999`, then `1.0999999999999999`, so it skips past 1.0.

**Task 7.** Prints `1 2 3 4 5 6 7 8 9` → fix `i <= 10`. Prints `******` (6 stars) → fix `i < 5`. Prints `5 4 3 2 1 0 Lift off!` → fix `i >= 1` (or `i > 0`). Rule: find the first and last values the body sees; for steps of 1 the count is last − first + 1.

**Task 8.**

```java
import java.util.Scanner;

public class SentinelStats {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        System.out.print("Enter a sequence of integers terminated by 0: ");
        int sum = 0;
        int count = 0;
        int current = console.nextInt();
        while (current != 0) {
            sum = sum + current;
            count = count + 1;
            current = console.nextInt();
        }
        if (count == 0) {
            System.out.println("No numbers entered.");
        } else {
            System.out.printf("Count: %d, sum: %d, average: %.2f\n", count, sum, (double) sum / count);
        }
        console.close();
    }
}
```

Input `50 100 -30 0` → `Count: 3, sum: 120, average: 40.00`. Input `0` → `No numbers entered.` Without the check, `(double) sum / count` with `count` 0 would print `NaN` (0.0 divided by 0); with plain `int` division it would throw `ArithmeticException: / by zero`.

**Task 9.**

```java
import java.util.Scanner;

public class MaxMin {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        final int SENTINEL = -999;
        System.out.print("Enter temperatures, -999 to finish: ");
        int temp = console.nextInt();
        if (temp == SENTINEL) {
            System.out.println("No temperatures entered.");
        } else {
            int max = temp;     // the first value is both the biggest and smallest so far
            int min = temp;
            while (temp != SENTINEL) {
                if (temp > max) {
                    max = temp;
                }
                if (temp < min) {
                    min = temp;
                }
                temp = console.nextInt();
            }
            System.out.println("Highest: " + max + ", lowest: " + min);
        }
        console.close();
    }
}
```

`12 -3 8 21 5 -999` → `Highest: 21, lowest: -3`. `-999` → `No temperatures entered.` Question 1: −1 and 0 are real temperatures; −999 never is. Question 2: starting `min` at 0 with all-positive temperatures gives lowest 0, which was never entered.

**Task 10.**

```java
import java.util.Random;
import java.util.Scanner;

public class GuessCounter {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        Random ran = new Random();
        int secret = ran.nextInt(100) + 1;   // 1 to 100
        // int secret = 37;                  // use a fixed value while testing
        int guesses = 0;
        boolean found = false;
        while (!found) {
            System.out.print("Guess (1-100): ");
            int guess = console.nextInt();
            guesses = guesses + 1;
            if (guess > secret) {
                System.out.println("Too high.");
            } else if (guess < secret) {
                System.out.println("Too low.");
            } else {
                found = true;
            }
        }
        System.out.println("Correct! You needed " + guesses + " guesses.");
        console.close();
    }
}
```

With `secret = 37` and inputs `50`, `25`, `37`: `Too high.`, `Too low.`, `Correct! You needed 3 guesses.` (verified). `+ 1` shifts 0–99 to 1–100. Question 7: 7 guesses, because halving 100 possibilities reaches 1 after 7 halvings (2⁷ = 128 ≥ 100).

**Task 11.**

```java
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Scanner;

public class LineNumbers {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner read = new Scanner(new FileReader("prog.txt"));
        int lineNumber = 0;
        while (read.hasNextLine()) {
            String line = read.nextLine();
            lineNumber = lineNumber + 1;
            System.out.println(lineNumber + ": " + line);
        }
        read.close();
        System.out.println("Total lines: " + lineNumber);
    }
}
```

The slide version prints all five lines. The line-numbered version prints `1:` to `5:` and `Total lines: 5`. Sentinel version:

```java
String line = read.nextLine();
while (!line.equals("This is the last line.")) {
    System.out.println(line);
    line = read.nextLine();
}
```

It prints only the first **two** lines and stops at line 3, missing `Really?` and line 5 (verified). A "last line" marker fails as soon as the same text appears in the data; EOF control avoids this.

**Task 12.** With input `50 100 -30` and end of input: `The sum of the numbers is: 120` (verified with input supplied from a file, not with the key press). No priming read is needed because `hasNext()` checks for more input without consuming it, so the test can come first and the read inside the body.

**Task 13.** a `0 5 10 15 20` · b `21` · c nothing · d `3 2 1` · e `81` · f `300` (the body runs once: 100 × 3, then `300 < 50` is false). Missing semicolon: `error: ';' expected`.

**Task 14.** Version 1 repeats the prompt three times then prints `You entered a valid score: 7`. Version 2 (flag) prints:

```text
Enter a score between 0 and 10: Error: 15 is not between 0 and 10. Try again.
Enter a score between 0 and 10: Error: -2 is not between 0 and 10. Try again.
Enter a score between 0 and 10: You entered a valid score: 7
```

The flag version is better for the user; the `do...while` is shorter. Code for both is in Lecture 8, section 10. Example for question 5: a shop that accepts a negative quantity could give a refund instead of charging.

**Task 15.**

```java
import java.util.Scanner;

public class SixMarks {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        int countA = 0, countB = 0, countC = 0, countD = 0;
        int student = 1;
        while (student <= 6) {
            System.out.print("Mark for student " + student + ": ");
            int mark = console.nextInt();
            if (mark >= 70) {
                countA = countA + 1;
            } else if (mark >= 60) {
                countB = countB + 1;
            } else if (mark >= 50) {
                countC = countC + 1;
            } else {
                countD = countD + 1;
            }
            student = student + 1;
        }
        System.out.println();
        System.out.println("A grades: " + countA);
        System.out.println("B grades: " + countB);
        System.out.println("C grades: " + countC);
        System.out.println("D grades: " + countD);
        console.close();
    }
}
```

Input `72 65 48 55 90 61` → A 2, B 2, C 1, D 1 (verified).

**Task 16.**

```java
import java.util.Scanner;

public class GradesSentinel {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        final int SENTINEL = -1;
        int countA = 0, countB = 0, countC = 0, countD = 0;
        System.out.print("Enter a mark (-1 to finish): ");
        int mark = console.nextInt();
        while (mark != SENTINEL) {
            if (mark >= 70) {
                countA = countA + 1;
            } else if (mark >= 60) {
                countB = countB + 1;
            } else if (mark >= 50) {
                countC = countC + 1;
            } else {
                countD = countD + 1;
            }
            System.out.print("Enter a mark (-1 to finish): ");
            mark = console.nextInt();
        }
        int students = countA + countB + countC + countD;
        System.out.println();
        System.out.println("Students: " + students);
        System.out.println("A: " + countA + "  B: " + countB + "  C: " + countC + "  D: " + countD);
        console.close();
    }
}
```

Both tests give the expected results (verified).

**Task 17.**

```java
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Scanner;

public class GradesEOF {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner read = new Scanner(new FileReader("marks.txt"));
        int countA = 0, countB = 0, countC = 0, countD = 0;
        while (read.hasNextInt()) {
            int mark = read.nextInt();
            if (mark >= 70) {
                countA = countA + 1;
            } else if (mark >= 60) {
                countB = countB + 1;
            } else if (mark >= 50) {
                countC = countC + 1;
            } else {
                countD = countD + 1;
            }
        }
        read.close();
        int students = countA + countB + countC + countD;
        System.out.println("Students: " + students);
        System.out.println("A: " + countA + "  B: " + countB + "  C: " + countC + "  D: " + countD);
    }
}
```

`Students: 8` and `A: 3  B: 2  C: 1  D: 2` (verified). Line breaks do not matter because `nextInt()` reads tokens separated by any whitespace. With `absent` at the end, `hasNextInt()` returns false there, so the loop stops quietly; with `hasNext()` and `nextInt()` the program would crash with `InputMismatchException` on `absent`.

**Task 18.**

```java
import java.util.Scanner;

public class GradesValidated {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        final int SENTINEL = -1;
        int countA = 0, countB = 0, countC = 0, countD = 0;
        int mark;
        do {
            // read ONE valid mark (0-100) or the sentinel
            do {
                System.out.print("Enter a mark 0-100 (-1 to finish): ");
                mark = console.nextInt();
            } while ((mark < 0 || mark > 100) && mark != SENTINEL);

            if (mark != SENTINEL) {
                if (mark >= 70) {
                    countA = countA + 1;
                } else if (mark >= 60) {
                    countB = countB + 1;
                } else if (mark >= 50) {
                    countC = countC + 1;
                } else {
                    countD = countD + 1;
                }
            }
        } while (mark != SENTINEL);
        System.out.println();
        System.out.println("Students: " + (countA + countB + countC + countD));
        System.out.println("A: " + countA + "  B: " + countB + "  C: " + countC + "  D: " + countD);
        console.close();
    }
}
```

Input `72 150 65 -5 48 -1` → six prompts (two repeats), then `Students: 3` and `A: 1  B: 1  C: 0  D: 1` (verified). A loop inside a loop like this is called a **nested** loop; Lecture 9 covers nesting properly. For the error message, a flag-controlled `while` (Task 14) is easier.

**Task 19.**

```java
public class LargestFactor {
    public static void main(String[] args) {
        final int NUMBER = 3195;
        int candidate = NUMBER - 1;              // the number itself is excluded
        while (NUMBER % candidate != 0) {        // stop at the first exact divisor
            candidate = candidate - 1;
        }
        System.out.println("Largest factor of " + NUMBER + " (excluding itself): " + candidate);

        // Faster idea: find the SMALLEST factor above 1, then divide
        int smallest = 2;
        while (NUMBER % smallest != 0) {
            smallest = smallest + 1;
        }
        System.out.println("Check: " + NUMBER + " / " + smallest + " = " + (NUMBER / smallest));
    }
}
```

Output (verified): `Largest factor of 3195 (excluding itself): 1065` and `Check: 3195 / 3 = 1065`. Counting down takes 3194 − 1065 = 2129 iterations (the body runs 2129 times); counting up takes 1 (from 2 to 3). For a prime such as 13 both methods give 1 (counting down reaches 1, which divides everything; counting up reaches 13 itself).

**Task 20.**

```java
import java.util.Scanner;

public class PinLockout {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        final int CORRECT_PIN = 4821;      // learning example only: never hard-code real secrets
        final int MAX_ATTEMPTS = 3;

        int attempts = 0;
        boolean unlocked = false;

        while (!unlocked && attempts < MAX_ATTEMPTS) {
            int pin;
            do {                                         // format check: does NOT use an attempt
                System.out.print("Enter your 4-digit PIN: ");
                pin = console.nextInt();
                if (pin < 1000 || pin > 9999) {
                    System.out.println("A PIN must have exactly 4 digits.");
                }
            } while (pin < 1000 || pin > 9999);

            attempts = attempts + 1;                     // a real attempt
            if (pin == CORRECT_PIN) {
                unlocked = true;
            } else {
                int left = MAX_ATTEMPTS - attempts;
                if (left > 0) {
                    System.out.println("Incorrect PIN. " + left + " attempt(s) left.");
                }
            }
        }

        if (unlocked) {
            System.out.println("Access granted after " + attempts + " attempt(s).");
        } else {
            System.out.println("Card locked. Contact your bank.");
        }
        console.close();
    }
}
```

Test 2 output (verified):

```text
Enter your 4-digit PIN: Incorrect PIN. 2 attempt(s) left.
Enter your 4-digit PIN: A PIN must have exactly 4 digits.
Enter your 4-digit PIN: Incorrect PIN. 1 attempt(s) left.
Enter your 4-digit PIN: Access granted after 3 attempt(s).
```

Test 3 output (verified): two "Incorrect" lines, then `Card locked. Contact your bank.` Note: a PIN that starts with 0 (such as `0482`) is read by `nextInt()` as 482 and rejected. That is a limit of storing a PIN as an `int`; storing it as a `String` would fix it, but needs String methods beyond this lab.

**Next:** Lecture 9 — the `for` loop, choosing the right loop, nested control structures and debugging loops.
