# Lab 6 — Selection (if-else) Hands-on Workbook (20 Tasks)

**Module:** 4300COMP Introduction to Programming · **Language:** Java

## How to use this lab

This lab has **20 hands-on tasks** on Lecture 6: relational operators, logical operators (`&&`, `||`, `!`), comparing Strings with `.equals()`, `if` and `if...else`, and the classic pitfalls. All three official Tutorial 6 exercises are included (marked **official**).

**Learning outcomes:** MLO1 throughout; MLO3 in Tasks 11–20 (turning rules in plain English into conditions).

**Setup:** make a project `Lab06` (untick module-info), one class per task with `main` ticked. Programs that read input need `import java.util.Scanner;` and `static Scanner console = new Scanner(System.in);`.

**How to test a program with conditions:** one test is never enough. For every condition, test:

1.  a value that is clearly **true**;

2.  a value that is clearly **false**;

3.  the **boundary** values exactly on the edge, and one either side (e.g. for `age >= 16`: 15, 16 and 17).

Record each test in a table: **input · expected output · actual output · pass/fail**. Fill in *expected* before you run.

**Rules**

1.  Type everything yourself. Predict first, then run.

2.  **Always use braces** `{ }` with `if` and `else`, even for one statement.

3.  Write the rule in plain English before writing the Java condition.

4.  Use hints in order; the answer key is at the end.

| Tasks | Focus                                                | Rough time     |
|-------|------------------------------------------------------|----------------|
| 1–5   | Conditions and operators (official Exercise 2)       | 10–15 min each |
| 6–10  | `if` and `if...else` (official Exercise 1)           | 10–15 min each |
| 11–15 | Rules from specifications (official Exercise 3)      | 15–20 min each |
| 16–20 | Larger programs, mini-project, assessment-style task | 20–30 min each |

Task 20 is practice only: it is not an official LJMU assessment and its checklist is not the official marking scheme.

## Tasks 1–5: Conditions and operators

### Task 1 — Relational predictions

**Class:** `Task01Relational` · **Goal:** predict `true`/`false` like the in-class test.

``` java
int x = 7, y = 12;
double p = 2.5;
char c = 'm';
```

| \#  | Expression    | Prediction |
|-----|---------------|------------|
| a   | `x < y`       |            |
| b   | `x == 7`      |            |
| c   | `y != 12`     |            |
| d   | `x * 2 > y`   |            |
| e   | `y / 5 == 2`  |            |
| f   | `y % 5 >= 2`  |            |
| g   | `p * 4 == 10` |            |
| h   | `p > x / 3`   |            |
| i   | `c > 'z'`     |            |
| j   | `c >= 'a'`    |            |
| k   | `'Z' < 'a'`   |            |
| l   | `'7' == 7`    |            |

Then print each one with `System.out.println("a: " + (x < y));` and mark yourself. Note: the brackets round the condition are needed inside `println`.

- **Hint 1:** arithmetic first (including integer division), then the comparison.

- **Hint 2:** `'7'` is a character with Unicode value 55, not the number 7.

### Task 2 — Evaluate by hand, then prove it (official Tutorial 6, Exercise 2)

**Class:** `Exercise2` · **Goal:** work out compound conditions, then check them in code.

``` java
int a = 10;
int b = 15;
double c = 13.2;
char d = 'D';
```

| \#  | Expression                                    | Your working | Result |
|-----|-----------------------------------------------|--------------|--------|
| 1   | `(b >= a + 2)`                                |              |        |
| 2   | `(15 > a) && (b < 21)`                        |              |        |
| 3   | `(a < b - 7) || (a + b == 42)`                |              |        |
| 4   | `(c / 2 < 10) || (d == 'd') && (a + b == 25)` |              |        |

1.  Work each one out **by hand**, showing every step.

2.  Write a program that uses an `if` for each expression and prints a message when it is true, e.g. `Expression 1 is true`.

3.  Extend it with `else` so it also prints a message when an expression is false.

4.  **Extra:** add brackets to expression 4 so that the `||` happens first. Does the result change?

- **Hint 1:** in Java the minus sign is `-` (the tutorial sheet shows a long dash); the OR operator is two vertical bars `||` (Shift + backslash on a UK keyboard).

- **Hint 2:** `&&` is done before `||`.

### Task 3 — Build the truth tables

**Class:** `Task03TruthTable` · **Goal:** let Java prove the AND/OR/NOT rules.

Declare `boolean t = true, f = false;` and print this table, with every result **calculated** by Java:

``` text
A      B      A&&B   A||B   !A
true   true   true   true   false
true   false  false  true   false
false  true   false  true   true
false  false  false  false  true
```

Compare it with the truth table in the lecture notes.

- **Hint 1:** `printf("%-7b%-7b%-7b%-7b%b%n", t, t, t && t, t || t, !t);`

- **Hint 2:** `%b` formats a boolean; `-7` left-aligns it in 7 characters.

### Task 4 — Comparing Strings

**Class:** `Task04Strings` · **Goal:** see for yourself why `==` is wrong for Strings.

1.  Read a word from the user with `nextLine()`. Compare it with `"yes"` using `==` and print the result. Then compare with `"yes".equals(word)`. Type `yes`. Which is `true`?

2.  Add `"yes".equalsIgnoreCase(word)`. Try `YES`, `Yes`, `yes ` (with a space at the end) and `y`.

3.  Write an `if...else` that prints `Confirmed` if the user typed yes in any capitals, otherwise `Cancelled`.

Record each input and the three results in a table.

- **Hint 1:** text typed by the user is a new String object, so `==` says `false` even when the letters match.

- **Hint 2:** a trailing space is a real character: `"yes "` is not `"yes"`.

### Task 5 — English to Java

**Class:** `Task05Translate` · **Goal:** turn plain-English rules into conditions.

Write a Java condition for each. Assume suitable variables exist (e.g. `int age`, `double temp`, `String user`, `boolean isMember`).

1.  age is at least 18

2.  temp is below freezing (0)

3.  score is exactly 100

4.  age is between 13 and 19 inclusive (a teenager)

5.  age is under 5 or 65 and over

6.  the user is not a member

7.  the username is `admin`

8.  x is even

9.  x is a multiple of 3 but not of 9

10. the port is outside the range 0 to 65535

Test each condition in a small program with at least one true and one false value.

- **Hint 1:** “between” needs two comparisons joined with `&&`.

- **Hint 2:** “even” means the remainder after dividing by 2 is 0.

## Tasks 6–10: if and if...else

### Task 6 — Old enough to vote? (official Tutorial 6, Exercise 1)

**Class:** `Exercise1` · **Goal:** your first decision-making program.

1.  Read an age from the user. Using the operators from the lecture, decide whether they are old enough to vote in the UK (**16 or over**, as the tutorial states) and tell the user either way.

2.  Test with **25, 20, 16, 15**. Fill in a test table (input, expected, actual, pass/fail) before running.

3.  Extend the program to test whether the age is **between 16 and 20** (inclusive) and tell the user either way. Test again with 25, 20, 16, 15.

4.  Which of the four test values are boundary values? Which boundary value is missing from the tutorial’s list for part 3? Add it.

- **Hint 1:** part 1 is one `if...else` with `age >= 16`.

- **Hint 2:** part 3 needs `&&`: both `age >= 16` and `age <= 20`.

### Task 7 — Even or odd, and multiples

**Class:** `Task07EvenOdd` · **Goal:** use `%` in conditions.

Read a whole number. Then, as **three separate** decisions:

1.  print whether it is even or odd (`if...else`);

2.  print `It is a multiple of 5` only if it is (`if`, no else);

3.  print whether it is a multiple of both 3 and 4.

Test with 7, 10, 12, 15, 24, 0 and −6. Predict each before running.

- **Hint 1:** a number is even when `n % 2 == 0`.

- **Hint 2:** −6 % 2 is 0, so negative even numbers still work. What about −7 % 2?

### Task 8 — Pass or fail, tested properly

**Class:** `Task08PassFail` · **Goal:** write a condition and test its boundary.

The pass mark is **40** (make it a constant). Read a mark from 0 to 100 and print `Pass` or `Fail`. Then:

1.  Complete a test table with the values 0, 39, 40, 41, 100 and 75.

2.  Deliberately change `>=` to `>`. Which test catches the bug? This is why boundary tests matter.

3.  Change back, then add a second, **independent** check: if the mark is 70 or more, also print `Distinction-level mark`.

- **Hint 1:** `final int PASS_MARK = 40;`

- **Hint 2:** the Distinction check is a separate `if` after the `if...else`, not part of it.

### Task 9 — Bug hunt: eight broken conditions

**Goal:** recognise every pitfall from the lecture. Type each fragment inside `main`, predict, run, explain, fix.

| \#  | Code                                                                                                   | What goes wrong |
|-----|--------------------------------------------------------------------------------------------------------|-----------------|
| 1   | `int thing = 0; if (thing = 1) { }`                                                                    | ?               |
| 2   | `boolean ok = true; if (ok = false) { System.out.println("Off"); }`                                    | ?               |
| 3   | `int score = 50; char grade = 'C'; if (score > 70) grade = 'A'; System.out.println("The grade is A");` | ?               |
| 4   | `float hours = 20.0f; if (hours > 40.0f); { System.out.println("Too long!"); }`                        | ?               |
| 5   | `int x = 5; if (3 < x < 10) { }`                                                                       | ?               |
| 6   | `int x = 5; if (x => 3) { }`                                                                           | ?               |
| 7   | `String s = new String("yes"); if (s == "yes") { System.out.println("match"); }`                       | ?               |
| 8   | `int x = 5; if (x > 3) { } else (x < 3) { }`                                                           | ?               |

For each: compile error, runtime problem, or logic error? Write the corrected line.

- **Hint 1:** numbers 2, 3, 4 and 7 compile. They are the dangerous ones.

- **Hint 2:** `else` never has a condition.

### Task 10 — Trace the decisions

**Class:** `Task10Trace` · **Goal:** predict which blocks run (exam skill).

``` java
String out = "";
if (n > 10) { out += "A"; } else { out += "B"; }
if (n % 2 == 0) { out += "C"; }
if (n >= 15 && n <= 20) { out += "D"; } else { out += "E"; }
if (!(n == 10) || n > 100) { out += "F"; }
System.out.println(n + " -> " + out);
```

Predict the output for `n` = 3, 10, 15 and 20. Then run it four times (change `n` each time, or read it with Scanner) and mark yourself.

- **Hint 1:** four separate decisions, so up to four letters are added; `+=` joins Strings too.

- **Hint 2:** the last condition is true whenever `n` is not 10.

## Tasks 11–15: Rules from specifications

### Task 11 — Is the tour bus full? (official Tutorial 6, Exercise 3)

**Class:** `Exercise3` · **Goal:** turn a written rule into one combined condition.

A tour bus is **full** if it has either of these combinations on board:

- 60 seated, 2 wheelchair users and 15 standing, **or**

- 60 seated, 0 wheelchair users and 19 standing.

Read three integers (seated, wheelchair users, standing). Using a **single `if...else`**, print `The bus is full` or `The bus is not full`.

1.  Write the rule in plain English with AND/OR first.

2.  Test with: `60 2 15`, `60 0 19`, `60 1 15`, `59 2 15`, `60 0 18`.

3.  **Design question:** the tutorial lists exact combinations. What should happen with `60 2 19`, or `60 1 19`? Write a second version that treats the bus as full when the numbers **reach or exceed** a full combination, and compare the two versions’ results. Which matches the real-world meaning better? (If unsure which your tutor wants, ask: this is exactly the kind of ambiguity to clarify in a real brief.)

- **Hint 1:** structure: `(combination 1) || (combination 2)`, where each combination is three comparisons joined with `&&`.

- **Hint 2:** use brackets round each combination so the `&&`s and `||` are clearly grouped.

### Task 12 — Guessing game (lecture worked example)

**Class:** `GuessingGame` · **Goal:** build the lecture example yourself.

1.  Generate a random number from 0 to 10 with `Random` (`import java.util.Random;`, then `rand.nextInt(11)`).

2.  Ask the user for a guess.

3.  Print `You guessed correctly!`, or say whether the guess was **below** or **above** the random number.

4.  **Test properly:** temporarily replace the random number with `int number = 7;` and test with guesses 5, 7 and 10. Then restore the random line.

5.  **Extra:** if the user enters a number outside 0–10, print `Out of range` instead.

- **Hint 1:** three outcomes → `if ... else if ... else`.

- **Hint 2:** the out-of-range check goes **first**: `if (guess < 0 || guess > 10)`.

### Task 13 — Login checker

**Class:** `Task13Login` · **Goal:** combine `&&` with `.equals()`.

Read a username and a password (both `nextLine()`). Access is granted only if the username is `admin` (exact case) **and** the password is `letmein`. Otherwise print `Access denied.`.

1.  Test: `admin`/`letmein`, `admin`/`LetMeIn`, `Admin`/`letmein`, `admin`/(empty), and `admin `/`letmein` (trailing space).

2.  Usernames are often not case-sensitive. Change the program so the **username** ignores case but the **password** does not. Retest.

3.  Explain why the program prints the same message whatever was wrong.

**Learning example only:** real systems never hard-code passwords in source code.

- **Hint 1:** `"admin".equalsIgnoreCase(user) && "letmein".equals(pass)`.

- **Hint 2:** telling an attacker which part was wrong halves their work.

### Task 14 — Online shop delivery rules

**Class:** `Task14Delivery` · **Goal:** apply two rules in the right order.

**Rules:**

1.  Students get 10% off the goods total.

2.  After any discount, orders of **£50.00 or more** get free delivery; otherwise delivery is £3.99.

Read the goods total (`double`) and whether the customer is a student (read `yes`/`no` and convert it to a `boolean` with `.equalsIgnoreCase`). Print the goods total after discount, the delivery charge and the amount to pay, all to 2 dp. Use constants.

| Goods | Student? | Expected to pay |
|-------|----------|-----------------|
| 60.00 | no       | 60.00           |
| 52.00 | yes      | 50.79           |
| 45.00 | no       | 48.99           |
| 50.00 | no       | 50.00           |
| 49.99 | no       | 53.98           |
| 55.50 | yes      | 53.94           |

Work out at least two rows by hand before running.

- **Hint 1:** first an `if` for the discount, then a separate `if...else` for delivery.

- **Hint 2:** `boolean isStudent = "yes".equalsIgnoreCase(answer);`

### Task 15 — Leap year

**Class:** `Task15LeapYear` · **Goal:** a classic compound condition.

The Gregorian calendar rule: a year is a leap year if it is divisible by 4 **and not** divisible by 100, **or** if it is divisible by 400.

1.  Read a year and print whether it is a leap year, using **one** `if...else`.

2.  Test: 2024, 1900, 2000, 2026, 2100. Predict each first.

3.  Rewrite the condition with different brackets: `y % 4 == 0 && (y % 100 != 0 || y % 400 == 0)`. Does it give the same results for all five? Explain.

- **Hint 1:** `(y % 4 == 0 && y % 100 != 0) || y % 400 == 0`.

- **Hint 2:** 1900 is divisible by 100 but not by 400, so it is **not** a leap year.

## Tasks 16–20: Larger programs

### Task 16 — Password policy checker

**Class:** `Task16Password` · **Goal:** check user input against security rules, one rule at a time.

Read a username and a proposed password. Print exactly **one** verdict, checking the rules **in this order**:

1.  shorter than 12 characters → `Too short`

2.  the same as the username (ignoring case) → `Same as username`

3.  contains the word `password` (any case) → `Contains the word password`

4.  otherwise → `Acceptable`

| Username     | Password            | Expected                   |
|--------------|---------------------|----------------------------|
| sam         | correcthorsebattery | Acceptable                 |
| sam         | short               | Too short                  |
| sam         | password1234        | Contains the word password |
| samarcher123 | SAMARCHER123        | Same as username           |
| sam         | Tr0ub4dor&3xyz      | Acceptable                 |

**API exploration (MLO2):** `length()` you met in Lab 2. For rule 3, look up `contains` and `toLowerCase` in the [String documentation](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) and work out how to combine them.

**Learning note:** length is the single most useful password rule. Real policies also check passwords against lists of known leaked passwords.

- **Hint 1:** one verdict from several rules → `if ... else if ... else if ... else`.

- **Hint 2:** `password.toLowerCase().contains("password")`.

### Task 17 — Security alert from a log file (builds on Lab 5)

**Class:** `Task17LogAlert` · **Goal:** combine file input with a decision.

Reuse Lab 5 Task 15 (`access.txt`: server name; then username, successful logins, failed logins). Add a decision: if the failure rate is **more than 20%**, add the line `ALERT: possible password guessing` to `security_report.txt`; otherwise add `Status: normal`.

Test with `sam 120 6` (4.76%, normal) and `bob 12 48` (80%, alert). Then design the boundary test: what numbers give **exactly** 20%, and what should happen?

- **Hint 1:** use a constant `ALERT_THRESHOLD = 20.0`.

- **Hint 2:** 8 failures out of 40 total is exactly 20%.

### Task 18 — Network port classifier

**Class:** `Task18Ports` · **Goal:** ranges and an invalid-input check (cyber context).

TCP/UDP ports run from 0 to 65535. Port numbers are commonly grouped as: **well-known** 0–1023 (e.g. 22 SSH, 443 HTTPS), **registered** 1024–49151, **dynamic/private** 49152–65535.

Read a port number and print its group, or `Invalid port` if it is outside 0–65535.

Test every boundary: −1, 0, 22, 443, 1023, 1024, 8080, 49151, 49152, 65535, 65536.

- **Hint 1:** check for invalid first: `if (port < 0 || port > 65535)`.

- **Hint 2:** in an `else if` chain, each later test can assume the earlier ones were false, so `else if (port <= 1023)` is enough.

### Task 19 — Mini-project: cash machine (ATM) withdrawal

**Class:** `Task19ATM` · **Goal:** several decisions working together, in the right order.

**Rules:** the account balance is £250.00; the correct PIN is 4321; the daily limit is £300; the machine only has £10 notes. All fixed values must be constants.

1.  Ask for the PIN. If it is wrong, print `Incorrect PIN. Card retained.` and do nothing else.

2.  Otherwise ask for an amount (whole pounds). Reject it with a clear message if it is zero/negative or not a multiple of 10, if it is over the daily limit, or if it is more than the balance.

3.  Otherwise subtract it and print `Please take £<amount>. New balance: £<balance>` (2 dp).

**Test plan** (complete expected results first):

| PIN  | Amount | Expected                  |
|------|--------|---------------------------|
| 1111 | —      | Incorrect PIN             |
| 4321 | 50     | Take £50, balance £200.00 |
| 4321 | 55     | Not a multiple of 10      |
| 4321 | 400    | Over daily limit          |
| 4321 | 260    | Insufficient funds        |
| 4321 | 250    | Take £250, balance £0.00  |
| 4321 | 0      | Rejected                  |

- **Hint 1:** the amount checks go **inside** the PIN’s `else` block, so a wrong PIN never reaches them.

- **Hint 2:** order matters: a £400 request should say “daily limit”, not “insufficient funds”.

### Task 20 — Assessment-style practice: cinema ticket pricer

**Class:** `Task20Cinema` · **Time limit:** 30 minutes, no hints.

Practice only: not an official LJMU assessment, and the checklist is not the official marking scheme.

**Specification:** read the customer’s name, the day (e.g. `Tue`), whether they are a student (`yes`/`no`), their age, and the number of tickets. Price **one** ticket by these rules, in this order:

1.  Under 12: Child, £5.00.

2.  Otherwise 65 or over: Senior, £6.50.

3.  Otherwise a student: Student, 20% off the adult price.

4.  Otherwise: Adult, £9.50.

5.  Then, on **Tuesdays** (any capitals), every ticket is £1.00 cheaper.

Print one line with `printf`: `Sam: 2 x Adult ticket @ £9.50 = £19.00`. All prices and rates must be constants. Read text before numbers to avoid the `nextLine()` trap.

**Test cases (verified):**

| Name | Day | Student | Age | Tickets | Expected line                        |
|------|-----|---------|-----|---------|--------------------------------------|
| Sam | Fri | no      | 30  | 2       | `2 x Adult ticket @ £9.50 = £19.00`  |
| Sam | Tue | yes     | 20  | 1       | `1 x Student ticket @ £6.60 = £6.60` |
| Sam  | Sat | no      | 8   | 3       | `3 x Child ticket @ £5.00 = £15.00`  |
| Jo   | tue | no      | 70  | 2       | `2 x Senior ticket @ £5.50 = £11.00` |
| Ali  | Mon | yes     | 12  | 1       | `1 x Student ticket @ £7.60 = £7.60` |
| Bo   | Mon | no      | 64  | 1       | `1 x Adult ticket @ £9.50 = £9.50`   |

**Self-check (practice only)**

- All six tests pass, including the boundaries 12 and 64/65

- Rules applied in the stated order with an `else if` chain

- Tuesday check ignores capitals and uses `.equalsIgnoreCase`

- Constants for every price and rate

- No `nextLine()` bug; braces on every `if`/`else`

- Output formatted exactly with `printf`

Send me your code when done and I will review it against the checklist.

## Progress tracker and reflection

Tick a task when every test in your table passes **and** you could explain every condition.

- Task 1 — Relational predictions (score: \_\_/12)

- Task 2 — Compound conditions (official Exercise 2)

- Task 3 — Truth tables

- Task 4 — Comparing Strings

- Task 5 — English to Java

- Task 6 — Voting age (official Exercise 1)

- Task 7 — Even/odd and multiples

- Task 8 — Pass/fail with boundary tests

- Task 9 — Bug hunt (8 pitfalls)

- Task 10 — Trace the decisions

- Task 11 — Tour bus (official Exercise 3)

- Task 12 — Guessing game

- Task 13 — Login checker

- Task 14 — Delivery rules

- Task 15 — Leap year

- Task 16 — Password policy

- Task 17 — Log alert from file

- Task 18 — Port classifier

- Task 19 — ATM withdrawal

- Task 20 — Cinema ticket pricer

**Reflection (send me your answers)**

1.  What is the difference between `=` and `==`? Why does `if (ok = false)` still compile?

2.  Why must Strings be compared with `.equals()`?

3.  When do you use two separate `if`s, and when one `if...else`?

4.  What is a boundary value? Give the boundary values you tested in Task 8 and Task 18.

5.  In Task 11, which interpretation of “full” did you choose, and why?

6.  Which pitfall from Task 9 do you think you are most likely to make?

## Answer key

Use only after a real attempt. All programs and results were compiled and run with Java 21 (`javac`), with test input piped in, not inside Eclipse.

**Task 1.** a true · b true · c false · d true (14 \> 12) · e true (12/5 = 2) · f true (12%5 = 2) · g true · h true (7/3 = 2) · i false · j true · k true (90 \< 97) · l false (55 ≠ 7).

**Task 2.**

| \#  | Working                                                | Result |
|-----|--------------------------------------------------------|--------|
| 1   | 15 \>= 12                                              | true   |
| 2   | true && true                                           | true   |
| 3   | (10 \< 8) \|\| (25 == 42) → false \|\| false           | false  |
| 4   | (6.6 \< 10) \|\| ((false) && (true)) → true \|\| false | true   |

Extra: `((c / 2 < 10) || (d == 'd')) && (a + b == 25)` is also `true` here (`true && true`), so the result doesn’t change for these values — but the meaning does: with `a + b` ≠ 25 the two versions would differ.

``` java
if (b >= a + 2) {
    System.out.println("Expression 1 is true");
} else {
    System.out.println("Expression 1 is false");
}
// ...same pattern for expressions 2 to 4
```

**Task 3.** Header `printf("%-7s%-7s%-7s%-7s%s%n", "A", "B", "A&&B", "A||B", "!A")`, then four rows like `printf("%-7b%-7b%-7b%-7b%b%n", t, f, t && f, t || f, !t)`. Output matches the task exactly.

**Task 4.** For `yes`: `==` false, `equals` true, `equalsIgnoreCase` true. `YES`/`Yes`: only `equalsIgnoreCase` true. `yes ` (trailing space) and `y`: all false.

**Task 5.** 1 `age >= 18` · 2 `temp < 0` · 3 `score == 100` · 4 `age >= 13 && age <= 19` · 5 `age < 5 || age >= 65` · 6 `!isMember` · 7 `"admin".equals(user)` · 8 `x % 2 == 0` · 9 `x % 3 == 0 && x % 9 != 0` · 10 `port < 0 || port > 65535`.

**Task 6.**

``` java
if (age >= 16) {
    System.out.println("You are old enough to vote in the UK.");
} else {
    System.out.println("You are not old enough to vote in the UK.");
}
if (age >= 16 && age <= 20) {
    System.out.println("Your age is between 16 and 20.");
} else {
    System.out.println("Your age is not between 16 and 20.");
}
```

| Age | Vote? | 16–20? |
|-----|-------|--------|
| 25  | yes   | no     |
| 20  | yes   | yes    |
| 16  | yes   | yes    |
| 15  | no    | no     |

Boundary values: 16 and 15 (part 1); 16, 15 and 20 (part 3). Missing: **21**, just above the upper boundary.

**Task 7.** (even? / multiple of 5? / multiple of 3 and 4?) 7: no/no/no · 10: yes/yes/no · 12: yes/no/yes · 15: no/yes/no · 24: yes/no/yes · 0: yes/yes/yes · −6: yes/no/no. −7 % 2 is −1, which is not 0, so it is correctly reported as odd.

**Task 8.** 0 Fail · 39 Fail · 40 Pass · 41 Pass · 100 Pass · 75 Pass. With `>` instead of `>=`, only the **40** test fails (says Fail). Distinction check: a separate `if (mark >= 70)` after the `if...else`.

**Task 9.**

| \#  | Kind                                                | Fix                                |
|-----|-----------------------------------------------------|------------------------------------|
| 1   | compile: int cannot be converted to boolean         | `thing == 1`                       |
| 2   | logic: compiles, assigns false, block never runs    | `if (!ok)`                         |
| 3   | logic: prints “The grade is A” for 50               | braces round both statements       |
| 4   | logic: prints “Too long!” for 20                    | remove the `;` after the condition |
| 5   | compile: bad operand types for binary operator '\<' | `x > 3 && x < 10`                  |
| 6   | compile: illegal start of expression                | `x >= 3`                           |
| 7   | logic: prints nothing although the text matches     | `s.equals("yes")`                  |
| 8   | compile: not a statement                            | `else if (x < 3)` or plain `else`  |

**Task 10.** 3 → `BEF` · 10 → `BCE` · 15 → `ADF` · 20 → `ACDF`.

**Task 11.**

``` java
if ((seated == 60 && wheelchair == 2 && standing == 15)
        || (seated == 60 && wheelchair == 0 && standing == 19)) {
    System.out.println("The bus is full");
} else {
    System.out.println("The bus is not full");
}
```

Exact version: full for `60 2 15` and `60 0 19`; not full for `60 1 15`, `59 2 15`, `60 0 18`, and also for `60 2 19` and `60 1 19`. An “at least” version, `(seated >= 60 && wheelchair >= 2 && standing >= 15) || (seated >= 60 && standing >= 19)`, also reports `60 2 19` and `60 1 19` as full (verified). The exact version follows the tutorial wording literally; ask your tutor which they intend.

**Task 12.** See Lecture 6 notes, Program A. Out-of-range check: `if (guess < 0 || guess > 10) { ... } else if (guess == number) { ... } else if (guess < number) { ... } else { ... }`.

**Task 13.** Only `admin`/`letmein` is granted (verified); the rest are denied, including the trailing-space username. Part 2: `"admin".equalsIgnoreCase(user) && "letmein".equals(pass)` then also grants `Admin`/`letmein`.

**Task 14.** Expected totals in the task table were verified.

``` java
if (isStudent) {
    goods = goods - goods * STUDENT_DISCOUNT;
}
if (goods >= FREE_DELIVERY_THRESHOLD) {
    delivery = 0;
} else {
    delivery = DELIVERY_CHARGE;
}
```

**Task 15.** 2024 leap · 1900 not · 2000 leap · 2026 not · 2100 not. The rewritten condition gives the same five results: both say “divisible by 4, and either not by 100 or by 400”.

**Task 16.**

``` java
if (password.length() < 12) {
    System.out.println("Too short");
} else if (password.equalsIgnoreCase(username)) {
    System.out.println("Same as username");
} else if (password.toLowerCase().contains("password")) {
    System.out.println("Contains the word password");
} else {
    System.out.println("Acceptable");
}
```

All five test rows verified.

**Task 17.** Add after the existing report lines:

``` java
if (failPct > ALERT_THRESHOLD) {
    out.println("ALERT: possible password guessing");
} else {
    out.println("Status: normal");
}
```

`sam 120 6` → normal; `bob 12 48` → alert; boundary `eve 32 8` (exactly 20.00%) → normal, because the rule says *more than* 20%.

**Task 18.**

``` java
if (port < 0 || port > 65535) {
    System.out.println("Invalid port");
} else if (port <= 1023) {
    System.out.println("Well-known port");
} else if (port <= 49151) {
    System.out.println("Registered port");
} else {
    System.out.println("Dynamic/private port");
}
```

−1 and 65536 invalid; 0, 22, 443, 1023 well-known; 1024, 8080, 49151 registered; 49152, 65535 dynamic/private.

**Task 19.** One model answer (all seven test rows verified):

``` java
final int CORRECT_PIN = 4321;
final double DAILY_LIMIT = 300.00;
final int NOTE = 10;
double balance = 250.00;

System.out.print("Enter PIN: ");
int pin = console.nextInt();
if (pin != CORRECT_PIN) {
    System.out.println("Incorrect PIN. Card retained.");
} else {
    System.out.print("Amount to withdraw: ");
    int amount = console.nextInt();
    if (amount <= 0 || amount % NOTE != 0) {
        System.out.println("Amount must be a positive multiple of 10.");
    } else if (amount > DAILY_LIMIT) {
        System.out.println("Amount exceeds the daily limit of £300.00.");
    } else if (amount > balance) {
        System.out.println("Insufficient funds.");
    } else {
        balance = balance - amount;
        System.out.printf("Please take £%d. New balance: £%.2f%n", amount, balance);
    }
}
```

**Task 20.** One model answer (all six test rows verified):

``` java
import java.util.Scanner;

/* Task 20 model answer: cinema ticket pricer. */
public class Task20Cinema {
    static Scanner console = new Scanner(System.in);

    public static void main(String[] args) {
        final double ADULT = 9.50, CHILD = 5.00, SENIOR = 6.50;
        final double STUDENT_DISCOUNT = 0.20, TUESDAY_REDUCTION = 1.00;

        // Text input first, then numbers
        System.out.print("Name: ");
        String name = console.nextLine();
        System.out.print("Day (e.g. Tue): ");
        String day = console.nextLine();
        System.out.print("Student (yes/no): ");
        boolean student = "yes".equalsIgnoreCase(console.nextLine());
        System.out.print("Age: ");
        int age = console.nextInt();
        System.out.print("Number of tickets: ");
        int qty = console.nextInt();

        // Price one ticket, rules in order
        double price;
        String band;
        if (age < 12) {
            price = CHILD;
            band = "Child";
        } else if (age >= 65) {
            price = SENIOR;
            band = "Senior";
        } else if (student) {
            price = ADULT - ADULT * STUDENT_DISCOUNT;
            band = "Student";
        } else {
            price = ADULT;
            band = "Adult";
        }
        if ("Tue".equalsIgnoreCase(day)) {
            price = price - TUESDAY_REDUCTION;
        }

        System.out.printf("%s: %d x %s ticket @ £%.2f = £%.2f%n", name, qty, band, price, price * qty);
    }
}
```
