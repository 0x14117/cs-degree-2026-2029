# Lab 7 — Multiple Selection and switch Hands-on Workbook (20 Tasks)

**Module:** 4300COMP Introduction to Programming · **Language:** Java

## How to use this lab

This lab has **20 hands-on tasks** on Lecture 7: choosing between many paths with separate `if`s, nested `if`s and `if...else if...else` chains; comparing decimals with `Math.abs`; and the `switch` statement with `case`, `break`, `default` and fall-through. All three official Tutorial 7 exercises and the supplementary exercise are included (marked **official**), plus the tutorial’s airport-label examples.

**Learning outcomes:** MLO1 throughout; MLO2 in Task 4 (`Math.abs`); MLO3 in Tasks 11–20.

**Setup:** project `Lab07` (untick module-info), one class per task with `main` ticked. Input programs need the Scanner lines; file programs need `throws FileNotFoundException` and the data file in the project root.

**Tutorial 7’s style rules (follow them in every task):**

1.  Indent to show the structure.

2.  Put a **comment above every condition** saying what it is meant to check. Conditions are where most logic errors are made, and the comment lets a reader spot a mismatch.

3.  Choose the construct that is clearest to someone reading the code for the first time.

**Test tables:** for every multi-way decision, test **one value in each branch** plus **every boundary**. Record input · expected · actual · pass/fail, and fill in *expected* before running.

| Tasks | Focus                                               | Rough time     |
|-------|-----------------------------------------------------|----------------|
| 1–5   | Multiple selection with `if`                        | 10–15 min each |
| 6–10  | `switch` and fall-through                           | 10–15 min each |
| 11–15 | Official exercises, menu, file + `if`               | 15–25 min each |
| 16–20 | Larger programs, refactoring, assessment-style task | 20–30 min each |

Task 20 is practice only: it is not an official LJMU assessment and its checklist is not the official marking scheme.

## Tasks 1–5: Multiple selection with if

### Task 1 — Separate ifs versus a chain

**Class:** `Task01IfsVsChain` · **Goal:** see how many blocks each structure can run.

``` java
int v = 80;
String s = "";
if (v > 50) { s += "A"; }
if (v > 70) { s += "B"; }
if (v > 90) { s += "C"; }
System.out.println("Separate: " + s);
```

1.  Predict the output for `v` = 40, 60, 80 and 95. Run and check.

2.  Rewrite the three tests as one `if ... else if ... else if` chain. Predict and run for the same four values.

3.  Fill in: “Separate ifs can run \_\_\_\_ blocks; a chain runs at most \_\_\_\_.”

4.  Reverse the order of the chain (test `v > 90` first). Now what happens? Which order is correct if you want the **highest** matching band?

- **Hint 1:** in a chain, the first true condition wins and the rest are skipped.

- **Hint 2:** with `> 50` first, 95 never reaches the `> 90` test.

### Task 2 — Untangle the nested interest rates

**Class:** `Task02Interest` · **Goal:** turn nested `if...else` into a readable chain.

1.  Type the lecture’s **nested** version (four levels of braces) that sets `interestRate` from `balance` (0.05 for ≥ 50000, 0.04 for ≥ 25000, 0.03 for ≥ 10000, otherwise 0.01). Read `balance` from the user.

2.  Rewrite it as an `if...else if...else` chain in a second class.

3.  Run **both** with the same test table: 60000, 50000, 49999.99, 25000, 24999.99, 10000, 9999.99, 0. They must agree on every row.

4.  Print the rate as a percentage with `printf("%.0f%%%n", interestRate * 100)`.

- **Hint 1:** each `else { if (...)` becomes `else if (...)`.

- **Hint 2:** the boundary rows (50000, 25000, 10000) catch `>` used by mistake instead of `>=`.

### Task 3 — Fix the wrongly ordered chain

**Class:** `Task03Degree` · **Goal:** understand why order matters.

UK degree classifications commonly use these bands: 70+ First, 60–69 2:1, 50–59 2:2, 40–49 Third, below 40 Fail. This code compiles but is wrong:

``` java
if (mark >= 40) {
    result = "Third";
} else if (mark >= 50) {
    result = "2:2";
} else if (mark >= 60) {
    result = "2:1";
} else if (mark >= 70) {
    result = "First";
} else {
    result = "Fail";
}
```

1.  Predict, then run, for 85, 65, 45 and 39. Which results are wrong?

2.  Fix it **only by reordering** the tests.

3.  Test every boundary: 70, 69, 60, 59, 50, 49, 40, 39, plus 85.

4.  Add a comment above each condition saying which band it catches.

- **Hint 1:** test the **highest** band first when using `>=`.

- **Hint 2:** the broken version gives “Third” for everything from 40 upwards.

### Task 4 — Comparing decimals safely (MLO2)

**Class:** `Task04Decimals` · **Goal:** reproduce the lecture’s rounding error and fix it.

1.  Type `RoundingError` from the lecture: `y = 3.0/7.0 + 2.0/7.0 + 2.0/7.0` compared with `x = 1.0` using `==`. Record the output.

2.  Type `RoundingFix` using `Math.abs(x - y) < 0.000001`. Make the tolerance a constant `TOLERANCE`.

3.  Try two more: `0.1 * 3` against `0.3`, and adding `0.1` ten times against `1.0`. Print each value and both comparisons.

4.  Look up `Math.abs` in the [Math class documentation](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Math.html). How many versions of `abs` are there, and for which types?

- **Hint 1:** print the actual value first: you will see why `==` fails.

- **Hint 2:** `Math.abs` is `static`, so you call it on the class name: `Math.abs(...)`, no object or import needed.

### Task 5 — Airport case labels: two if designs (from Tutorial 7)

**Class:** `Task05Labels` · **Goal:** compare a nested design with a complex-condition design.

Cases are labelled by weight:

| Weight          | Label       |
|-----------------|-------------|
| 1, 2, 3         | A           |
| 4               | B           |
| 5               | C           |
| any other value | Not allowed |

1.  Implement Tutorial 7’s **nested** version: an outer `if (weight > 0)` containing a chain (`< 4`, `== 4`, `== 5`, else), with an outer `else` for zero/negative.

2.  Implement the **complex-condition** version: `if ((weight > 0) && (weight < 4))`, then `else if (weight == 4)`, `else if (weight == 5)`, `else`.

3.  Test both with −1, 0, 1, 3, 4, 5, 6. They must agree.

4.  The tutorial notes the complex version can’t tell an overweight case from a **negative** weight (a possible scale fault). Add an `else if` so negative weights print `Scale error` while 6+ still prints `Not allowed`.

- **Hint 1:** in Java the OR operator is `||` (the sheet shows a special bar character).

- **Hint 2:** the new test `weight < 0` must come before the final `else`.

## Tasks 6–10: switch and fall-through

### Task 6 — Grade messages with switch

**Class:** `Task06GradeSwitch` · **Goal:** your first switch.

1.  Type the lecture example: `char grade = 'B';` and a switch with cases `'A'`, `'B'`, `'C'`, each printing a message and `break`, and a `default` printing `The grade is invalid.`

2.  Change it to read the grade from the user: `char grade = console.next().charAt(0);` (`charAt(0)` takes the first character of the word typed).

3.  Make lower-case letters work too, **without** repeating the messages: group `case 'A': case 'a':` together.

4.  Test with `A`, `b`, `C`, `d` and `F`.

- **Hint 1:** a case with no statements falls through to the next case’s statements. That is how grouping works.

- **Hint 2:** `charAt` is a String method; you will see more String methods later.

### Task 7 — Fall-through investigation

**Class:** `Task07FallThrough` · **Goal:** predict exactly what a switch without breaks does.

Type the lecture’s broken grade switch (cases 0, 1, 2 grouped for F, then 3 → C, 4 → B, 5 → A, then `default` → Invalid score, with **no** `break`s).

1.  Before running, write the full output for every score from 0 to 7 in a table.

2.  Run each score and mark your predictions.

3.  Add the missing `break`s so each score prints exactly one line. Which case does **not** need a break, and why?

4.  Re-run 0 to 7 and confirm.

- **Hint 1:** execution starts at the matching case and keeps going down until a `break` or the closing `}`.

- **Hint 2:** a score of 7 matches nothing, so only `default` runs.

### Task 8 — Airport labels with switch, and deliberate fall-through (from Tutorial 7)

**Class:** `Task08LabelSwitch` · **Goal:** use fall-through on purpose.

1.  Rewrite Task 5’s labelling with a `switch (weight)`: `case 1: case 2: case 3:` → A, `case 4:` → B, `case 5:` → C, `default:` → Not allowed. Test −1 to 6.

2.  Tutorial 7 then changes the A labels: weight 1 → `**A`, weight 2 → `*A`, weight 3 → `A`. Build a `String label = "";` and use **deliberate fall-through**: `case 1:` adds `*`, `case 2:` adds `*`, `case 3:` adds `A` then `break`.

3.  Trace weight 1 by hand: which cases’ statements run?

4.  Where would you put a check for negative weights in the switch version? (The tutorial suggests inside `default`.) Add it.

- **Hint 1:** `label = label + "*";` (or `label += "*";`).

- **Hint 2:** inside `default:` you can use an ordinary `if (weight < 0) { ... } else { ... }`.

### Task 9 — Day of the week

**Class:** `Task09Days` · **Goal:** a switch that produces a value, plus grouping.

Read a number 1–7 (1 = Monday). Use one switch to set `String dayName`, and a second switch with grouped cases to set `String kind` to `weekday` or `weekend`. Print `Saturday is a weekend day.` Any other number prints `Invalid day`.

Test 1, 5, 6, 7, 0 and 8.

**Extra:** rewrite the first switch as a **switch expression** (`String dayName = switch (day) { case 1 -> "Monday"; ... default -> "Invalid day"; };`). The module focuses on the traditional form; this is for comparison only.

- **Hint 1:** `case 1: case 2: case 3: case 4: case 5: kind = "weekday"; break;`

- **Hint 2:** Java insists a variable has a value before use; `default` makes sure it always does.

### Task 10 — Bug hunt: eight switch mistakes

**Goal:** recognise every switch error. Type each inside `main`, read the message (javac shown), fix it.

| \#  | Code                                                                                                       | Message or behaviour                                     |
|-----|------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|
| 1   | `double gpa = 4.2; switch (gpa) { case 4.2: break; }`                                                      | `selector type double is not allowed`                    |
| 2   | `int option = 1; switch (option) { case 1: break; case 1: break; }`                                        | `duplicate case label`                                   |
| 3   | `char quitOption = 'q'; char input = 'q'; switch (input) { case quitOption: break; }`                      | `constant expression required`                           |
| 4   | `boolean ok = true; switch (ok) { case true: break; }`                                                     | `selector type boolean is not allowed`                   |
| 5   | `int x = 75; switch (x) { case x >= 70: break; }`                                                          | `incompatible types: boolean cannot be converted to int` |
| 6   | `String s = "A"; switch (s) { case 'A': break; }`                                                          | `incompatible types: char cannot be converted to String` |
| 7   | `int x = 5; switch (x) { case 1 System.out.println("one"); break; }`                                       | `: or -> expected`                                       |
| 8   | `int x = 2; switch (x) { case 2: System.out.println("two"); case 3: System.out.println("three"); break; }` | compiles; prints two **and** three                       |

For number 3, give **two** fixes (hint: one uses `final`, one uses a literal). For number 5, what construct should be used instead?

- **Hint 1:** a switch matches exact constant values; it cannot test ranges.

- **Hint 2:** `'A'` is a `char`; `"A"` is a `String`.

## Tasks 11–15: Official exercises, menu and file processing

Tasks 11–13 build **one** program in three stages, exactly as Tutorial 7 does. Keep a copy of each stage.

### Task 11 — Ticket price by age (official Tutorial 7, Exercise 1)

**Class:** `Exercise1`

1.  Read an age from the keyboard and print the ticket price:

| Age                       | Price |
|---------------------------|-------|
| under 16                  | £5    |
| 16 through 64 (inclusive) | £10   |
| over 64                   | £5    |

2.  **Question from the tutorial:** what is the best selection construct and structure here? Try writing it two ways — a three-branch `if...else if...else`, and a two-branch `if...else` using `||` — and decide which is clearer. Could a `switch` do it? Why not?

3.  Test: 15, 16, 40, 64, 65, 0. Print prices with `printf("£%.2f")`.

- **Hint 1:** two of the bands give the same price, so `(age < 16 || age > 64)` covers both.

- **Hint 2:** a switch cannot test ranges like “under 16”.

### Task 12 — Student discounts (official Tutorial 7, Exercise 2)

**Class:** `Exercise2` (a copy of Exercise 1)

1.  Also ask whether the user is a student (read `yes`/`no`). Apply these discounts to the age-based price:

| Age / student             | Discount |
|---------------------------|----------|
| student and 16 through 64 | −10%     |
| student and over 64       | −20%     |

2.  **Did your code check whether someone under 16 tried to claim to be a student?** If not, add a check that prints an error message. (The tutorial says students must be “over 16” but the table starts at 16; this workbook treats **16 or over** as allowed. Ask your tutor if unsure.)

3.  **Rewrite** the program so it first tests the student status (printing the error if needed), works out the discount, and then prints the result. Is this approach more or less efficient/readable? Write two sentences.

4.  Test: 30 non-student (£10.00), 30 student (£9.00), 70 student (£4.00), 12 student (error), 16 student (£9.00), 65 non-student (£5.00).

- **Hint 1:** make the prices and discounts constants.

- **Hint 2:** `price = price - price * STUDENT_DISCOUNT;`

### Task 13 — Birthday month codes with switch (official Tutorial 7, Exercise 3)

**Class:** `Exercise3` (a copy of Exercise 2)

1.  Also ask for the **current month** and the user’s **birth month** (use `Jan`, `Feb` ... `Dec`). If they match, the ticket is **free**, and instead of a price the ticket shows a code from this table, chosen with a `switch` on the month:

| Month | Code | Month | Code |
|-------|------|-------|------|
| Jan   | Q1.1 | Jul   | Q3.1 |
| Feb   | Q1.2 | Aug   | Q3.2 |
| Mar   | Q1.3 | Sep   | Q3.3 |
| Apr   | Q2.1 | Oct   | Q4.1 |
| May   | Q2.2 | Nov   | Q4.2 |
| Jun   | Q2.3 | Dec   | Q4.3 |

2.  **Question:** what is the advantage of a switch here?

3.  Write a **nested if** (or `else if` chain) that could replace the switch. Compare the two for readability.

4.  Test: Oct/Oct → `Q4.1`; Feb/Feb → `Q1.2`; Oct/Mar → normal price; `oct`/`Oct` → what happens, and why?

- **Hint 1:** read the months with `nextLine()` (after the age, clear the newline first).

- **Hint 2:** a String switch is case-sensitive, like `.equals()`.

### Task 14 — Interactive menu that survives bad input

**Class:** `Task14Menu` · **Goal:** the lecture’s menu, improved.

1.  Build the lecture’s menu (1 Update Roles, 2 Assign Workers, 3 Release Bees) with `nextInt()` and an `int` switch, plus a `default` for unknown options. Test 1, 3, 9 and `abc`. What does `abc` do?

2.  Improve it: read the choice with `nextLine()` and switch on the **String** (`case "1":` ...). Test again with 1, 3, 9, `abc` and an empty line.

3.  Add a fourth option, `q` or `Q`, that prints `Goodbye`.

**Security thinking:** every program that takes input must handle input it doesn’t expect. Version 2 does that without crashing.

- **Hint 1:** `case "q": case "Q":` groups both letters.

- **Hint 2:** an empty line is the String `""`, which simply goes to `default`.

### Task 15 — PayCalculator: file input plus if (lecture worked example)

**Class:** `PayCalculator` · **Goal:** combine Lecture 5 files with selection.

`wages.txt` (project root):

``` text
Keir
15.0 8 true
Rachel
13.0 8 false
```

Schema: name (line), then pay rate (decimal), hours (whole number) and bonus (`true`/`false`). If bonus is `true`, add 10% to the wage.

1.  Read both records (no loops yet: repeat the reading code) and print `Keir worked 8 hours for £132.0` and `Rachel worked 8 hours for £104.0`.

2.  Change the output to `printf` with 2 dp.

3.  Add a third record of your own and check it by hand.

- **Hint 1:** after `nextBoolean()`, call `nextLine()` to finish the line before reading the next name.

- **Hint 2:** `if (bonus1) { wage1 = wage1 + wage1 * BONUS_RATE; }` — no `== true` needed.

## Tasks 16–20: Larger programs

### Task 16 — Four-function calculator

**Class:** `Task16Calculator` · **Goal:** switch on a `char`, with an `if` inside one case.

Read a number, an operator and a second number typed on one line, e.g. `7 / 2`. Use `console.nextDouble()`, `console.next().charAt(0)`, `console.nextDouble()`.

- `+`, `-`, `*` and `%` print the result.

- `x` should also mean multiply (group it with `*`).

- `/` prints the result, **unless** the second number is 0: then print `Error: cannot divide by zero`.

- Anything else prints `Unknown operator: ^` (showing the character).

Test: `7 + 3`, `7 - 3`, `7 * 3`, `7 x 3`, `7 / 2`, `7 / 0`, `7 % 3`, `7 ^ 3`.

- **Hint 1:** the divide-by-zero check is an `if...else` **inside** `case '/':`, followed by `break`.

- **Hint 2:** comparing with exactly `0` is fine here because the user typed it; the tolerance rule is for **calculated** decimals.

### Task 17 — HTTP status code explainer

**Class:** `Task17Http` · **Goal:** combine a switch (exact values) with an `if` chain (ranges).

Web servers answer every request with a status code. Read a code and print its meaning:

- Exact codes via `switch`: 200 OK, 301 Moved Permanently, 403 Forbidden, 404 Not Found, 500 Internal Server Error.

- Any other code, in the `default` section, by range: 100–199 Informational, 200–299 Success, 300–399 Redirection, 400–499 Client error, 500–599 Server error, otherwise `Invalid status code`.

Test: 200, 301, 403, 404, 500, 204, 418, 302, 503, 99, 600.

**Cyber link:** in web server logs, many 403/404 responses from one address can be a sign of someone probing for hidden pages.

- **Hint 1:** this shows why both constructs exist: switch for exact values, `if` for ranges.

- **Hint 2:** put the whole range chain inside `default:`.

### Task 18 — Refactor for readability (official supplementary exercise)

**Class:** `Task18Refactor` · **Goal:** answer Tutorial 7’s supplementary question: could your programs be made clearer with a different construct?

This code works but is hard to read:

``` java
if (option == 1) {
    System.out.println("Start scan");
} else {
    if (option == 2) {
        System.out.println("Stop scan");
    } else {
        if (option == 3) {
            System.out.println("Show report");
        } else {
            if (option == 4) {
                System.out.println("Exit");
            } else {
                System.out.println("Unknown option");
            }
        }
    }
}
```

1.  Rewrite it as an `else if` chain. Then rewrite it as a `switch`. Test all three versions with 1, 2, 3, 4 and 7; the output must be identical.

2.  Which version would you want to maintain? Why?

3.  Look back at **Lab 6 Task 18** (port classifier) and **Lab 6 Task 20** (cinema pricer). For each, decide whether a `switch` would make it clearer, and explain why or why not in one sentence.

- **Hint 1:** one variable compared with exact values → switch.

- **Hint 2:** ranges (port numbers, ages) → stay with an `if` chain.

### Task 19 — Mini-project: security incident triage from a file

**Class:** `Task19Triage` · **Goal:** file input + `if` chain + `switch` + file output.

`incident.txt` schema: incident ID (line 1); then a type code (one letter), severity (1–5) and hours the incident has been open (line 2).

``` text
INC-1042
P 2 3
```

**Priority rules (in order):** severity 4 or more, **or** open more than 48 hours → `P1 Critical`; severity exactly 3 → `P2 High`; otherwise `P3 Normal`.

**Category and team (switch on the type code):**

| Code  | Category            | Team                       |
|-------|---------------------|----------------------------|
| M     | Malware             | Endpoint Security          |
| P     | Phishing            | Email Security             |
| D     | DDoS                | Network Operations         |
| U     | Unauthorised access | Identity and Access        |
| other | Unknown             | Security Operations Centre |

Write `triage_report.txt`:

``` text
Incident:  INC-1042
Category:  Phishing
Severity:  2 (open 3 h)
Priority:  P3 Normal
Assign to: Email Security
```

Test with five files: `P 2 3`, `M 5 1`, `U 2 72`, `D 3 10`, `X 1 1`. Write the expected priority and team for each before running. Use constants for 4 and 48.

- **Hint 1:** read the code with `in.next().charAt(0)`.

- **Hint 2:** `U 2 72` is P1 because of the hours, not the severity.

### Task 20 — Assessment-style practice: coffee shop till

**Class:** `Task20Coffee` · **Time limit:** 30 minutes, no hints.

Practice only: not an official LJMU assessment, and the checklist is not the official marking scheme.

**Specification:**

1.  Show a menu and read the choice as text: 1 Espresso £2.20, 2 Latte £3.10, 3 Tea £1.80. Any other choice prints `Invalid drink choice.` and nothing else.

2.  Read the size as a letter (S/M/L, either case): Small +£0.00, Medium +£0.40, Large +£0.80. Any other letter prints `Invalid size.`

3.  Read whether the customer has a loyalty card (yes/no): loyalty customers get 10% off the subtotal.

4.  Read the quantity; it must be at least 1, otherwise print `Quantity must be at least 1.`

5.  Print the receipt with `printf`:

``` text
2 x Large Latte @ £3.90
Subtotal: £7.80
Discount: £0.78
Total:    £7.02
```

**Required:** at least one `switch` on a String, one `switch` on a `char` with grouped cases, an `if...else if` chain, constants for every price, a comment above every condition, and no `nextLine()` bugs.

**Test cases (verified):** `2 L yes 2` → £7.02 · `1 S no 1` → £2.20 · `3 m no 3` → £6.60 · `4 S no 1` → invalid drink · `2 X no 1` → invalid size · `2 M yes 0` → quantity error.

**Self-check (practice only)**

- All six tests give exactly the expected output

- String switch for the drink, char switch with grouped cases for the size

- Invalid input handled without crashing for drink and size

- Constants for every price and the discount

- A comment above every condition (Tutorial 7 rule)

- Money printed to 2 dp

Send me your code when done and I will review it against the checklist.

## Progress tracker and reflection

Tick a task when every row of your test table passes **and** every condition has a comment.

- Task 1 — Separate ifs versus a chain

- Task 2 — Untangle nested interest rates

- Task 3 — Fix the wrongly ordered chain

- Task 4 — Comparing decimals

- Task 5 — Airport labels with if

- Task 6 — Grade switch

- Task 7 — Fall-through investigation

- Task 8 — Airport labels with switch

- Task 9 — Day of the week

- Task 10 — Switch bug hunt

- Task 11 — Ticket price by age (official Exercise 1)

- Task 12 — Student discounts (official Exercise 2)

- Task 13 — Birthday codes (official Exercise 3)

- Task 14 — Robust menu

- Task 15 — PayCalculator

- Task 16 — Calculator

- Task 17 — HTTP status codes

- Task 18 — Refactor (official supplementary)

- Task 19 — Incident triage

- Task 20 — Coffee shop till

**Reflection (send me your answers)**

1.  When do separate `if`s make sense, and when must you use a chain?

2.  Why does the order of conditions in an `else if` chain matter? Use Task 3 as your example.

3.  Explain fall-through. When is it a bug and when is it useful?

4.  Give two things a `switch` cannot do that an `if` chain can.

5.  Why should you never compare calculated doubles with `==`?

6.  Your answers to the Tutorial 7 questions: best construct for Exercise 1, and the advantage of `switch` in Exercise 3.

## Answer key

Use only after a real attempt. All programs and results were compiled and run with Java 21 (`javac`), with test input piped in, not inside Eclipse.

**Task 1.** Separate ifs: 40 → (nothing), 60 → `A`, 80 → `AB`, 95 → `ABC`. Chain (`> 50` first): 40 → nothing, 60/80/95 → `A`. Reversed chain (`> 90` first): 60 → `A`, 80 → `B`, 95 → `C`. Separate ifs can run **all three** blocks; a chain runs **at most one**. For the highest matching band, test the highest threshold first.

**Task 2.** Both versions (verified): 60000 → 0.05 · 50000 → 0.05 · 49999.99 → 0.04 · 25000 → 0.04 · 24999.99 → 0.03 · 10000 → 0.03 · 9999.99 → 0.01 · 0 → 0.01. The chain is the lecture’s Option 3 code.

**Task 3.** Broken version: 85 → Third, 65 → Third, 45 → Third, 39 → Fail. Fixed order:

``` java
// 70 and above: First
if (mark >= 70) {
    result = "First";
// 60-69: 2:1
} else if (mark >= 60) {
    result = "2:1";
// 50-59: 2:2
} else if (mark >= 50) {
    result = "2:2";
// 40-49: Third
} else if (mark >= 40) {
    result = "Third";
// below 40: Fail
} else {
    result = "Fail";
}
```

Boundaries (verified): 70 First, 69 2:1, 60 2:1, 59 2:2, 50 2:2, 49 Third, 40 Third, 39 Fail, 85 First.

**Task 4.** `x = 1.0 y = 0.9999999999999999`, not equal with `==`, equivalent with the tolerance. `0.1 * 3` prints `0.30000000000000004` (== false, tolerance true). Ten additions of 0.1 give `0.9999999999999999` (== 1.0 false). The Math page lists four `abs` versions: `int`, `long`, `float`, `double`.

**Task 5.** Both designs (verified): −1 and 0 Not allowed · 1 and 3 A · 4 B · 5 C · 6 Not allowed. Scale-error version:

``` java
if ((weight > 0) && (weight < 4)) {
    label = "A";
} else if (weight == 4) {
    label = "B";
} else if (weight == 5) {
    label = "C";
} else if (weight < 0) {
    label = "Scale error";
} else {
    label = "Not allowed";
}
```

**Task 6.**

``` java
char grade = console.next().charAt(0);
switch (grade) {
    case 'A':
    case 'a':
        System.out.println("The grade is 'A'!");
        break;
    case 'B':
    case 'b':
        System.out.println("The grade is 'B'!");
        break;
    case 'C':
    case 'c':
        System.out.println("The grade is 'C'!");
        break;
    default:
        System.out.println("The grade is invalid.");
}
```

`d` and `F` give `The grade is invalid.`

**Task 7.** Without breaks: 0, 1, 2 → F, C, B, A, Invalid score · 3 → C, B, A, Invalid · 4 → B, A, Invalid · 5 → A, Invalid · 6, 7 → Invalid only. Add `break;` after the F, C, B and A lines. `default` (the last section) needs no break because nothing follows it.

**Task 8.** Labels (verified): 1 → `**A`, 2 → `*A`, 3 → `A`, 4 → B, 5 → C, others Not allowed. Weight 1 runs the statements of cases 1, 2 and 3, then breaks.

``` java
String label = "";
switch (weight) {
    case 1:
        label = label + "*";
    case 2:
        label = label + "*";
    case 3:
        label = label + "A";
        break;
    case 4:
        label = "B";
        break;
    case 5:
        label = "C";
        break;
    default:
        if (weight < 0) {
            label = "Scale error";
        } else {
            label = "Not allowed";
        }
}
```

**Task 9.** 1 Monday/weekday · 5 Friday/weekday · 6 Saturday/weekend · 7 Sunday/weekend · 0 and 8 Invalid day.

**Task 10.** 1 compile → use `if` chain or an `int` scale · 2 compile → remove or change the duplicate · 3 compile → `final char QUIT_OPTION = 'q';` (verified to work) or `case 'q':` · 4 compile → use `if (ok)` · 5 compile → ranges need `if (x >= 70)` · 6 compile → `case "A":` · 7 compile → `case 1:` · 8 logic → add `break;` after `two`.

**Task 11.** Clearest: `if (age < 16 || age > 64) { price = 5; } else { price = 10; }` (or a three-branch chain). A switch cannot test ranges. 15 → £5.00 · 16 → £10.00 · 40 → £10.00 · 64 → £10.00 · 65 → £5.00 · 0 → £5.00.

**Task 12.** Verified: 30 no → £10.00 · 30 yes → £9.00 · 70 yes → £4.00 · 12 yes → `Error: students must be 16 or over.` · 16 yes → £9.00 · 65 no → £5.00.

``` java
// under 16 or over 64 pay the reduced price; 16 to 64 pay standard
if (age < 16 || age > 64) {
    price = CHILD_SENIOR_PRICE;
} else {
    price = STANDARD_PRICE;
}
// students must be 16 or over
if (student && age < 16) {
    System.out.println("Error: students must be 16 or over.");
// working-age student: 10% off
} else if (student && age <= 64) {
    price = price - price * STUDENT_DISCOUNT;
// senior student: 20% off
} else if (student) {
    price = price - price * SENIOR_STUDENT_DISCOUNT;
}
```

**Task 13.** Oct/Oct → `FREE ticket. Code: Q4.1`; Feb/Feb → `Q1.2`; Oct/Mar → normal price. Current `oct`, birth `Oct`: with `.equals()` the months don’t match, so the price is charged; with `.equalsIgnoreCase()` they match and the switch on `"Oct"` gives Q4.1 (verified). But if the **birth** month is typed `oct`, the switch reaches `default`, because a String switch is case-sensitive. Advantage of switch: twelve exact values of one variable read as a clean table.

``` java
switch (birth) {
    case "Jan": code = "Q1.1"; break;
    case "Feb": code = "Q1.2"; break;
    case "Mar": code = "Q1.3"; break;
    // ...Apr to Nov...
    case "Dec": code = "Q4.3"; break;
    default: code = "UNKNOWN";
}
```

**Task 14.** Int version: 1, 3 and 9 work (9 → `Sorry, 9 is not an option.`); `abc` crashes with InputMismatchException (verified). String version: `abc` and an empty line reach `default`. Quit: `case "q": case "Q": System.out.println("Goodbye"); break;`.

**Task 15.** Output (verified): `Keir worked 8 hours for £132.0` and `Rachel worked 8 hours for £104.0`. Full code: Lecture 7 notes, Program A.

**Task 16.** Verified: `7 + 3` 10.0 · `7 - 3` 4.0 · `7 * 3` and `7 x 3` 21.0 · `7 / 2` 3.5 · `7 / 0` error · `7 % 3` 1.0 · `7 ^ 3` `Unknown operator: ^`.

**Task 17.** Verified: 200 OK · 301 Moved Permanently · 403 Forbidden · 404 Not Found · 500 Internal Server Error · 204 Success · 418 Client error · 302 Redirection · 503 Server error · 99 and 600 Invalid status code.

**Task 18.** All three versions print the same; the switch is easiest to read and extend. Lab 6 Task 18 (ports) uses ranges, so it stays an `if` chain. Lab 6 Task 20 (cinema) also uses age ranges and combined conditions, so a switch would not help; only the Tuesday check compares exact values.

**Task 19.** Verified: `P 2 3` → Phishing, P3 Normal, Email Security · `M 5 1` → Malware, P1 Critical, Endpoint Security · `U 2 72` → Unauthorised access, P1 Critical, Identity and Access · `D 3 10` → DDoS, P2 High, Network Operations · `X 1 1` → Unknown, P3 Normal, Security Operations Centre.

``` java
String priority;
// severe, or left open too long
if (severity >= CRITICAL_SEVERITY || hours > MAX_OPEN_HOURS) {
    priority = "P1 Critical";
// medium severity
} else if (severity == 3) {
    priority = "P2 High";
} else {
    priority = "P3 Normal";
}
```

**Task 20.** One model answer (all six tests verified):

``` java
import java.util.Scanner;

/* Task 20 model answer: coffee shop till. */
public class Task20Coffee {
    static Scanner console = new Scanner(System.in);

    public static void main(String[] args) {
        final double ESPRESSO = 2.20, LATTE = 3.10, TEA = 1.80;
        final double MEDIUM_EXTRA = 0.40, LARGE_EXTRA = 0.80, LOYALTY_DISCOUNT = 0.10;

        System.out.print("Drink (1 Espresso, 2 Latte, 3 Tea): ");
        String choice = console.nextLine();
        System.out.print("Size (S/M/L): ");
        char size = console.nextLine().charAt(0);
        System.out.print("Loyalty card (yes/no): ");
        boolean loyal = "yes".equalsIgnoreCase(console.nextLine());
        System.out.print("Quantity: ");
        int qty = console.nextInt();

        String drink = "";
        double base = 0;
        boolean drinkOk = true;
        switch (choice) {
            case "1": drink = "Espresso"; base = ESPRESSO; break;
            case "2": drink = "Latte"; base = LATTE; break;
            case "3": drink = "Tea"; base = TEA; break;
            default: drinkOk = false;
        }

        double extra = 0;
        String sizeName = "";
        boolean sizeOk = true;
        switch (size) {
            case 'S': case 's': sizeName = "Small"; break;
            case 'M': case 'm': extra = MEDIUM_EXTRA; sizeName = "Medium"; break;
            case 'L': case 'l': extra = LARGE_EXTRA; sizeName = "Large"; break;
            default: sizeOk = false;
        }

        // unknown drink number
        if (!drinkOk) {
            System.out.println("Invalid drink choice.");
        // unknown size letter
        } else if (!sizeOk) {
            System.out.println("Invalid size.");
        // must buy at least one
        } else if (qty < 1) {
            System.out.println("Quantity must be at least 1.");
        } else {
            double each = base + extra;
            double subtotal = each * qty;
            double discount = 0;
            // loyalty customers get 10% off
            if (loyal) {
                discount = subtotal * LOYALTY_DISCOUNT;
            }
            System.out.printf("%d x %s %s @ £%.2f%n", qty, sizeName, drink, each);
            System.out.printf("Subtotal: £%.2f%n", subtotal);
            System.out.printf("Discount: £%.2f%n", discount);
            System.out.printf("Total:    £%.2f%n", subtotal - discount);
        }
    }
}
```
