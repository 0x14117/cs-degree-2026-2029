# Lab 2 — Variables \#1 Hands-on Workbook (20 Tasks)

**Module:** 4300COMP Introduction to Programming · **Language:** Java

## How to use this lab

This lab has **20 hands-on tasks** on Lecture 2: variables, the four main types, arithmetic, precedence, integer division, `%`, casting and Strings. All four official Tutorial 2 tasks and the supplementary task are included (marked **official**), with extra practice around them.

**Learning outcomes:** MLO1 throughout; MLO2 when you use Eclipse to investigate errors; MLO3 in Tasks 16–20.

**Setup:** in Eclipse make a project `lab2` (untick module-info), package `lab2`, and one class per task named as the task says. Tick `public static void main(String[] args)` each time.

**Rules**

1.  Type everything yourself.

2.  **Predict on paper first**, then run. The in-class test is taken without a computer, so predicting correctly is the skill to build.

3.  Use the hints in order and stop when you are unstuck. The answer key is at the end.

4.  When a task says “by hand”, show each step as in the lecture’s worked examples.

| Tasks | Focus                                                           | Rough time     |
|-------|-----------------------------------------------------------------|----------------|
| 1–5   | Variables and types                                             | 5–10 min each  |
| 6–10  | Arithmetic and precedence (official Tasks 1–3)                  | 10–15 min each |
| 11–15 | Mixed types, casting, Strings (official Task 4 + supplementary) | 10–20 min each |
| 16–20 | Calculators, mini-project, assessment-style task                | 20–30 min each |
|       |                                                                 |                |

Task 20 is practice only: it is not an official LJMU assessment and its checklist is not the official marking scheme.

## Tasks 1–5: Variables and types

### Task 1 — Meet the types

**Class:** `Task01Types` · **Goal:** declare one variable of each main type and print it.

Declare and initialise these five variables, then print each one with a label.

| Name        | Type      | Value                        |
|-------------|-----------|------------------------------|
| `age`       | `int`     | your age or any whole number |
| `height`    | `double`  | e.g. `1.78`                  |
| `initial`   | `char`    | your first initial           |
| `isStudent` | `boolean` | `true`                       |
| `fullName`  | `String`  | your name                    |

**Expected output shape:**

``` text
Age: 20
Height: 1.78
Initial: A
Student: true
Name: Sam Archer
```

Then try: change `height` to `2` (no decimal point). What prints? Why?

- **Hint 1:** pattern: `int age = 20;` then `System.out.println("Age: " + age);`

- **Hint 2:** `char` uses single quotes, `String` double quotes, `boolean` no quotes.

### Task 2 — Legal or illegal names?

**Class:** `Task02Names` · **Goal:** let the compiler confirm identifier rules.

For each name, **first write legal/illegal and why**, then test it in Eclipse with `int <name> = 1;`. A red underline means illegal.

`studentCount` · `2ndTry` · `_hidden` · `$price` · `total score` · `class` · `Class` · `max-value` · `value2` · `public` · `fees%` · `numberOfFailedLogins`

Then rename any that are legal but poorly named (for example `_hidden`) following lowerCamelCase.

- **Hint 1:** letters, digits, `_` and `$` only; no digit at the start; no reserved words.

- **Hint 2:** Java is case-sensitive, so `Class` is not the same word as `class`.

### Task 3 — Trace the changing value

**Class:** `Task03Trace` · **Goal:** track one variable through several assignments.

**Copy this trace table on paper and fill it in before running.**

``` java
int score = 10;
System.out.println(score);
score = score + 5;
System.out.println(score);
score = score * 2;
System.out.println(score);
score = score - 7;
System.out.println(score);
```

| After line           | Value of `score` | Printed |
|----------------------|------------------|---------|
| `int score = 10;`    |                  |         |
| `score = score + 5;` |                  |         |
| `score = score * 2;` |                  |         |
| `score = score - 7;` |                  |         |

Then add the slide example below to the same program and explain why it prints two different letters from one variable.

``` java
char grade;
grade = 'B';
System.out.println(grade);
grade = 'A';
System.out.println(grade);
```

- **Hint 1:** the right side is calculated using the value *before* the line runs.

- **Hint 2:** a new assignment replaces the old value completely.

### Task 4 — Swap two values

**Class:** `Task04Swap` · **Goal:** solve a classic problem with a third variable.

Start with `int a = 7;` and `int b = 3;`. Write statements so that afterwards `a` holds 3 and `b` holds 7. Print `a = 3, b = 7`.

First try this and see why it fails:

``` java
a = b;
b = a;
```

- **Hint 1:** after `a = b;` the 7 is lost for ever. You need to save it somewhere first.

- **Hint 2:** declare `int temp = a;` before overwriting `a`.

### Task 5 — Bug hunt: nine broken declarations

**Class:** `Task05Bugs` · **Goal:** read type and variable errors.

Each line below has one mistake. Type them **one at a time** inside `main`, read Eclipse’s message, then fix it. The messages shown are from `javac`; Eclipse words them differently.

| \#  | Broken code                                 | Message (javac)                                                    |
|-----|---------------------------------------------|--------------------------------------------------------------------|
| 1   | `int count = 5`                             | `';' expected`                                                     |
| 2   | `Int total = 10;`                           | `cannot find symbol`                                               |
| 3   | `char c = "A";`                             | `incompatible types: String cannot be converted to char`           |
| 4   | `String s = 'Hi';`                          | `unclosed character literal`                                       |
| 5   | `boolean ok = "true";`                      | `incompatible types: String cannot be converted to boolean`        |
| 6   | `double price = 9.99; int whole = price;`   | `incompatible types: possible lossy conversion from double to int` |
| 7   | `int count = 1; System.out.println(Count);` | `cannot find symbol`                                               |
| 8   | `int a; System.out.println(a);`             | `variable a might not have been initialized`                       |
| 9   | `int x = 1; int x = 2;`                     | `variable x is already defined in method main(String[])`           |

For line 6, give **two** different fixes: one that changes the type and one that uses a cast. What does the cast version store?

- **Hint 1:** messages with “cannot find symbol” mean Java does not recognise a name: check spelling and capitals.

- **Hint 2:** “incompatible types” means the value on the right does not fit the type on the left.

## Tasks 6–10: Arithmetic and precedence

### Task 6 — All five operators (official Tutorial 2, Task 1)

**Class:** `MyJavaProgram` · **Goal:** extend the lecture’s sum program.

Type the sum program from Lecture 2 (`integer1 = 10`, `integer2 = 20`, prints `The sum value is: 30`). Then add the subtraction, multiplication, division and remainder of `integer1` and `integer2`.

**Before running, predict all five lines.** Two of them often surprise people.

**Expected output:**

``` text
The sum value is: 30
The difference value is: -10
The product value is: 200
The division value is: 0
The remainder value is: 10
```

Then change `integer1` to `47` and `integer2` to `5` and predict again.

- **Hint 1:** either make new `int` variables (`difference`, `product`, ...) or calculate inside the `println` with brackets.

- **Hint 2:** 10 / 20 is integer division. 20 goes into 10 zero times, with 10 left over.

### Task 7 — Order of evaluation (official Tutorial 2, Task 2)

**Class:** `Task07Precedence` · **Goal:** apply precedence by hand, then prove it with code.

For each statement, **by hand**: number the operators in the order Java applies them, and show the value after each step (like the lecture’s worked examples).

``` java
x = 7 + 3 * 6 / 2 - 1;
y = 2 % 2 + 2 * 2 - 2 / 2;
z = (3 * 9 * (3 + (9 * 3) / (3)));
```

Then write a program that declares `int x, y, z;`, assigns these three expressions and prints the values. Do they match your working?

(Tutorial 2 writes the names as capital `X`, `Y`, `Z`; use lower case in Java, following the naming convention.)

- **Hint 1:** in `x`, `*` and `/` have equal precedence, so go left to right: `3 * 6` first, then `/ 2`.

- **Hint 2:** in `z`, start with the innermost brackets: `(9 * 3)`, then `/ (3)`, then `3 + ...`.

### Task 8 — Division and remainder in real life

**Class:** `Task08DivMod` · **Goal:** use `/` and `%` together to split a quantity.

Write three short calculations. Use variables for the inputs so you can change them.

1.  **Time:** `int totalSeconds = 3725;` Print `1 h 2 m 5 s`.

2.  **Money:** `int pence = 1234;` Print `Pounds: 12, pence: 34`.

3.  **Weeks:** `int days = 100;` Print `14 weeks and 2 days`.

Test each with a second value (for example 7322 seconds, 99 pence, 365 days) and check by hand.

- **Hint 1:** `/` gives *how many whole* units; `%` gives *what is left over*.

- **Hint 2:** for minutes: first take what is left after hours (`totalSeconds % 3600`), then divide that by 60.

### Task 9 — Predict ten expressions

**Class:** `Task09Predict` · **Goal:** exam-style prediction practice.

Write your prediction for each, then print them all and mark yourself.

| \#  | Expression            | Your prediction |
|-----|-----------------------|-----------------|
| a   | `9 / 2`               |                 |
| b   | `9 % 2`               |                 |
| c   | `9.0 / 2`             |                 |
| d   | `2 * 3 + 4 * 5`       |                 |
| e   | `2 * (3 + 4) * 5`     |                 |
| f   | `30 / 4 / 2`          |                 |
| g   | `30 / (4 / 2)`        |                 |
| h   | `25 % 7 % 3`          |                 |
| i   | `-9 / 4`              |                 |
| j   | `1 + 2 + "3" + 4 + 5` |                 |

Aim for 10/10. For each one you got wrong, write one sentence on the rule you missed.

- **Hint 1:** f and g look alike, but the brackets in g change which division happens first.

- **Hint 2:** j: the first `+` sees two numbers; after that a String is involved.

### Task 10 — Average of three numbers (official Tutorial 2, Task 3)

**Class:** `Task10Average` · **Goal:** meet the integer-division trap in a real calculation.

**Part A (official):** declare four `int` variables `num1`, `num2`, `num3` and `average`. Store 125, 28 and −25 in the first three. Store the average of the three in `average`. Print all four values.

**Part B:** work out the true average on a calculator. Why is Part A’s answer different?

**Part C:** add a `double realAverage` that holds the exact average. Find **two** different ways to write the right-hand side so it keeps the decimal.

- **Hint 1:** brackets are needed so the sum is divided, not just `num3`.

- **Hint 2:** for Part C, make one operand a `double`: either divide by `3.0`, or cast the sum with `(double)`.

## Tasks 11–15: Mixed types, casting and Strings

### Task 11 — Promotion and casting predictions

**Class:** `Task11Casting` · **Goal:** predict when Java keeps or drops the decimal.

| \#  | Expression         | Your prediction |
|-----|--------------------|-----------------|
| a   | `7 / 2 * 2.0`      |                 |
| b   | `7 / 2.0 * 2`      |                 |
| c   | `3 + 4 / 8`        |                 |
| d   | `3 + 4 / 8.0`      |                 |
| e   | `(int) 5.99 + 1`   |                 |
| f   | `(int)(5.99 + 1)`  |                 |
| g   | `(double) 10 / 4`  |                 |
| h   | `(double)(10 / 4)` |                 |
| i   | `(int) 'A'`        |                 |
| j   | `(char) 66`        |                 |

Print them all and mark yourself. Remember: a `double` result always prints with a decimal point, so `6` and `6.0` are different answers.

- **Hint 1:** go one operator at a time. The type of each step depends only on its two operands.

- **Hint 2:** i and j are new: a `char` is stored as a number (its character code). Casting converts between the two. Try `(char) 67` too.

### Task 12 — Temperature converter

**Class:** `Task12Temperature` · **Goal:** use `double` and avoid the integer-division trap.

The formula is F = C × 9 ÷ 5 + 32.

1.  Declare `double celsius = 25;` and calculate `fahrenheit`. Print `25.0 C = 77.0 F`.

2.  Now write the formula as `9 / 5 * celsius + 32`. What do you get, and why?

3.  Fix version 2 **without** changing the order of the terms.

4.  Test with 37.5 °C (should give 99.5) and −40 °C (should give −40.0).

- **Hint 1:** in version 2, `9 / 5` is worked out first, and both are `int`.

- **Hint 2:** `9.0 / 5` fixes it.

### Task 13 — The + puzzle with Strings

**Class:** `Task13Strings` · **Goal:** control when `+` adds and when it joins.

``` java
String first = "Sam";
String course = "Cyber Security";
int year = 1;
```

1.  Print `Name: Sam, course: Cyber Security, year 1` using the three variables.

2.  Predict, then print: `"Next year: " + year + 1` — why is it wrong? Fix it so it prints `Next year: 2`.

3.  Predict, then print: `first + year + year` and `year + year + first`. Explain the difference.

4.  Print the number of characters in `first` using `first.length()`.

5.  Declare `String empty = "";` and print its length.

- **Hint 1:** left to right; once a String appears, every later `+` joins.

- **Hint 2:** brackets force the adding to happen first.

### Task 14 — Squares and cubes table (official Tutorial 2, Task 4)

**Class:** `Task14Table` · **Goal:** produce a neat table using only what you know so far (no loops yet).

Print the numbers 0 to 10 with their squares and cubes, using `\t` to make columns:

``` text
Number  Square  Cube
0       0       0
1       1       1
2       4       8
...
10      100     1000
```

Requirement: Java must **calculate** every square and cube.

**Smart approach using reassignment:** declare `int n = 0;`, print one row using `n * n` and `n * n * n`, then `n = n + 1;`, then copy those two lines for each row. Every row’s code is identical, so there is nothing to retype. (Later in the module you will learn loops, which do this repetition for you.)

- **Hint 1:** one row: `System.out.println(n + "\t" + n * n + "\t" + n * n * n);` — `*` happens before `+`, so no extra brackets are needed here.

- **Hint 2:** if the columns drift in Eclipse’s console, add a second `\t` in the header only.

### Task 15 — Numbers stored as text (official supplementary task)

**Class:** `TestStringNumbers` · **Goal:** convert numeric Strings into numbers.

This is the code from Tutorial 2. Type it in and read the error.

``` java
String twentyThree = "23";
String oneFourFive = "145";
String aDecimal = "25.4";

int total = twentyThree + oneFourFive + aDecimal;

System.out.println("The total value is " + total);
```

1.  Why does the `int total = ...` line fail? What would `twentyThree + oneFourFive + aDecimal` produce if it were stored in a String?

2.  Read the official Java tutorial page that Tutorial 2 links, [Converting Between Numbers and Strings](https://docs.oracle.com/javase/tutorial/java/data/converting.html). Find the methods that turn a String into an `int` and into a `double`.

3.  Fix the program so it prints `The total value is 193.4`.

- **Hint 1:** `+` with Strings joins them; it never adds the numbers inside.

- **Hint 2:** the API provides `Integer.parseInt("23")` and `Double.parseDouble("25.4")`. Think about which type `total` must be, given that one value has a decimal part.

This is your first use of the Java API (MLO2): reading documentation to find a method you have not been taught.

## Tasks 16–20: Calculators, mini-project and assessment-style task

From here on, plan before you code: list the **inputs** (variables with given values), the **calculations**, and the **outputs** (exact lines to print). Values are hard-coded for now; reading them from the keyboard comes later.

### Task 16 — Shopping bill and the decimal surprise

**Class:** `Task16Bill` · **Goal:** calculate money and see why programmers are careful with `double`.

A student buys 3 notebooks at £2.50, 2 pens at £1.20 and 1 USB stick at £8.99.

1.  Use `int` variables for the quantities and `double` variables for the prices. Calculate and print the subtotal (expected `18.89`).

2.  Calculate a 10% student discount (`subtotal * 0.10`) and print it. Look closely at the output. What is odd?

3.  Rewrite the calculation using **whole pence** in `int` variables (250, 120, 899). Print the total as pounds and pence using `/ 100` and `% 100`.

4.  **Edge case:** what does your pence version print if the total is 1805 pence? Is that correct? (You cannot fully fix this until you learn formatted output or `if`; just describe the problem.)

- **Hint 1:** computers store `double` in binary, so many decimal values (like 0.1) cannot be stored exactly. Tiny errors appear in the last digits.

- **Hint 2:** 1805 % 100 is 5, not 05.

### Task 17 — Storage and data calculator

**Class:** `Task17Storage` · **Goal:** apply `/` and `%` to computing units (cyber context).

Use 1 KB = 1024 bytes and 1 MB = 1024 KB, and 1 character = 8 bits (true for plain English text).

1.  `int fileBytes = 5000000;` Print the size in whole KB (`4882 KB`).

2.  Print the same size as `4 MB and 786 KB`.

3.  `int passwordLength = 12;` Print how many bits the password takes: `96 bits`.

4.  A network sends 1500 bytes per packet. How many full packets for `fileBytes`, and how many bytes are in the last partial packet?

- **Hint 1:** MB = bytes / 1024 / 1024. The leftover KB is (bytes / 1024) % 1024.

- **Hint 2:** full packets: `/ 1500`; leftover: `% 1500`.

### Task 18 — Password guessing and integer overflow

**Class:** `Task18BruteForce` · **Goal:** see a real limit of `int` (and why type choice matters in security).

A password of lower-case letters only has 26 options per character. For length 4 there are 26 × 26 × 26 × 26 possible passwords.

1.  Calculate and print the number of possible passwords of length 4 and length 6 using `int`.

2.  Now do length 8 with `int`. Is the answer believable? Print `Integer.MAX_VALUE` to see the biggest `int`.

3.  Fix it with the `long` type: `long eight = 26L * 26 * 26 * 26 * 26 * 26 * 26 * 26;` The `L` makes the first literal a `long`, so the whole multiplication is done in `long`.

4.  Try `long eightBad = 26 * 26 * 26 * 26 * 26 * 26 * 26 * 26;` (no `L`). Why is it still wrong even though the variable is `long`?

5.  If an attacker can try 1000 guesses per second, print how many **seconds** to try every 4-letter password, **minutes** for 6 letters and **days** for 8 letters.

Learning point (not for production): real attackers are far faster than 1000 guesses per second, and real advice is to use long passphrases. The programming lesson is that an `int` silently wraps round when it overflows — no error message.

- **Hint 1:** the right-hand side is calculated in `int` *before* it is stored, so the overflow has already happened.

- **Hint 2:** days = guesses / 1000 / 60 / 60 / 24.

### Task 19 — Mini-project: module results report

**Class:** `Task19Results` · **Goal:** plan and build a complete report from a specification.

**Inputs (hard-coded):** five module marks out of 100: 68, 73, 55, 81, 64. A student name (String) and a final grade letter (`char`, set it to `'B'` yourself — working it out automatically needs `if`, which comes later).

**The report must print:**

1.  A title line and a line of `-` characters.

2.  The student’s name.

3.  Each module mark on its own line, labelled `Module 1:` to `Module 5:` with a tab before the mark.

4.  The total of all marks (341).

5.  The average as a whole number using integer division (68), labelled `Average (int):`.

6.  The exact average as a `double` (68.2), labelled `Average (exact):`.

7.  The percentage of the maximum possible marks (out of 500), as a `double`.

8.  The grade letter.

**Constraints:** at least one cast; no number in the output may be typed by hand except the five marks; comments above each section.

- **Hint 1:** make `int total` first, then reuse it for every later calculation.

- **Hint 2:** percentage = `total * 100.0 / 500`.

### Task 20 — Assessment-style practice: club event budget

**Class:** `Task20EventBudget` · **Time limit:** 30 minutes, no hints.

Practice only: not an official LJMU assessment, and the checklist is not the official marking scheme.

**Specification:** a made-up student Cyber Club runs a capture-the-flag evening. Write a program that prints a budget report.

**Data:** 47 tickets sold at £3.00 each; room hire £60.00; pizza £45.50; the event lasts 150 minutes; players are put into teams of 4.

**The program must:**

1.  Store every data item in a suitably typed and well-named variable (`int` for counts, `double` for money).

2.  Calculate and print total income, total costs and profit.

3.  Print the profit per ticket sold as a `double`, and also as whole pence using a cast.

4.  Print how many full teams of 4 can be made and how many players are left over.

5.  Print the event length as hours and minutes (`2 h 30 min`).

6.  Use `String` concatenation with brackets wherever a calculation appears inside a `println`.

7.  Include a header comment and section comments; use clear layout with a title and blank lines between sections.

**Self-check (practice only)**

- Compiles and runs

- Correct types chosen for every variable

- All numbers calculated by Java (test by changing tickets to 50)

- Integer division and `%` used correctly for teams and time

- At least one cast, with a comment saying why

- Output clearly labelled and readable

- Comments and consistent indentation

Send me your code when done and I will review it against the checklist.

## Progress tracker and reflection

Tick a task when it runs correctly **and** you could explain every line to someone else.

- Task 1 — Meet the types

- Task 2 — Legal or illegal names

- Task 3 — Trace the changing value

- Task 4 — Swap two values

- Task 5 — Bug hunt (9 errors)

- Task 6 — All five operators (official Task 1)

- Task 7 — Order of evaluation (official Task 2)

- Task 8 — Division and remainder in real life

- Task 9 — Predict ten expressions (score: \_\_/10)

- Task 10 — Average of three numbers (official Task 3)

- Task 11 — Promotion and casting (score: \_\_/10)

- Task 12 — Temperature converter

- Task 13 — The + puzzle with Strings

- Task 14 — Squares and cubes table (official Task 4)

- Task 15 — Numbers stored as text (official supplementary)

- Task 16 — Shopping bill

- Task 17 — Storage calculator

- Task 18 — Password guessing and overflow

- Task 19 — Module results report

- Task 20 — Club event budget

**Reflection (send me your answers)**

1.  Explain the difference between declaring, assigning and initialising a variable, with one line of code for each.

2.  Why does `7 / 2` give `3` but `7 / 2.0` give `3.5`?

3.  When would you use a cast, and what can you lose?

4.  Why did the swap in Task 4 need a third variable?

5.  What did Task 18 teach you about choosing a data type?

6.  Your scores for Tasks 9 and 11. Which rules caught you out?

## Answer key

Use only after a real attempt. All outputs below were produced by running the code with Java 21 (`javac`), not inside Eclipse.

**Task 1.** Changing `height` to `2` prints `2.0`: the `int` literal is promoted because the variable is a `double`.

**Task 2.** Legal: `studentCount`, `_hidden`, `$price`, `Class`, `value2`, `numberOfFailedLogins`. Illegal: `2ndTry` (starts with a digit), `total score` (space), `class` and `public` (reserved words), `max-value` (`-`), `fees%` (`%`). Better name for `_hidden`: `hidden` or something meaningful.

**Task 3.** `score`: 10 → 15 → 30 → 23; output `10`, `15`, `30`, `23`. Then `B`, `A`: one variable, one value at a time; the second assignment overwrites the first.

**Task 4.** `a = b; b = a;` gives `a = 3, b = 3` because the 7 is overwritten. Fix:

``` java
int temp = a;
a = b;
b = temp;
System.out.println("a = " + a + ", b = " + b);
```

**Task 5.** 1: add `;`. 2: `int` (lower case). 3: `'A'`. 4: `"Hi"`. 5: `true` without quotes. 6: `double whole = price;` or `int whole = (int) price;` (stores `9`). 7: `count`. 8: give `a` a value first. 9: second line becomes `x = 2;`.

**Task 6.** Output as shown in the task. With 47 and 5: `52`, `42`, `235`, `9`, `2`.

**Task 7.**

| Statement | Steps                                                       | Value |
|-----------|-------------------------------------------------------------|-------|
| `x`       | 3 × 6 = 18 → 18 / 2 = 9 → 7 + 9 = 16 → 16 − 1               | `15`  |
| `y`       | 2 % 2 = 0 → 2 × 2 = 4 → 2 / 2 = 1 → 0 + 4 = 4 → 4 − 1       | `3`   |
| `z`       | 9 × 3 = 27 → 27 / 3 = 9 → 3 + 9 = 12 → 3 × 9 = 27 → 27 × 12 | `324` |

**Task 8.**

``` java
int totalSeconds = 3725;
int hours = totalSeconds / 3600;
int minutes = (totalSeconds % 3600) / 60;
int seconds = totalSeconds % 60;
System.out.println(hours + " h " + minutes + " m " + seconds + " s");

int pence = 1234;
System.out.println("Pounds: " + pence / 100 + ", pence: " + pence % 100);

int days = 100;
System.out.println(days / 7 + " weeks and " + days % 7 + " days");
```

Test values: 7322 s → 2 h 2 m 2 s; 99 p → 0 and 99; 365 days → 52 weeks and 1 day.

**Task 9.** a `4` · b `1` · c `4.5` · d `26` · e `70` · f `3` (30/4 = 7, 7/2 = 3) · g `15` (4/2 = 2, 30/2) · h `1` (25%7 = 4, 4%3 = 1) · i `-2` · j `3345` (1+2 = 3, then joins "3", 4, 5).

**Task 10.** Part A prints `125`, `28`, `-25`, `42` with `average = (num1 + num2 + num3) / 3;`. True average 42.666…; integer division dropped the decimal. Part C: `(num1 + num2 + num3) / 3.0` or `(double)(num1 + num2 + num3) / 3`, both giving `42.666666666666664`.

**Task 11.** a `6.0` · b `7.0` · c `3` · d `3.5` · e `6` · f `6` · g `2.5` · h `2.0` · i `65` · j `B`.

**Task 12.** `celsius * 9 / 5 + 32` gives `77.0`. `9 / 5 * celsius + 32` gives `57.0` because `9 / 5` is `1`. Fix: `9.0 / 5 * celsius + 32`. 37.5 → `99.5`; −40 → `-40.0`.

**Task 13.** 2: prints `Next year: 11`; fix `"Next year: " + (year + 1)`. 3: `Sam11` (String first, joins) and `2Sam` (adds first). 4: `4`. 5: `0`.

**Task 14.**

``` java
int n = 0;
System.out.println("Number\tSquare\tCube");
System.out.println(n + "\t" + n * n + "\t" + n * n * n);
n = n + 1;
System.out.println(n + "\t" + n * n + "\t" + n * n * n);
n = n + 1;
// ...repeat the pair of lines until the row for 10
```

Last row: `10 100 1000`.

**Task 15.** `+` joins the Strings into `"2314525.4"`, and a String cannot be stored in an `int`. Fix:

``` java
double total = Integer.parseInt(twentyThree)
             + Integer.parseInt(oneFourFive)
             + Double.parseDouble(aDecimal);
System.out.println("The total value is " + total);
```

Output: `The total value is 193.4`. `total` must be a `double` because 25.4 has a decimal part.

**Task 16.** Subtotal `18.89`; discount prints `1.8890000000000002` (binary rounding error). Pence version: total `1889`, printed as `18.89`. Edge case: 1805 prints `18.5`, which is wrong; it should be `18.05`.

**Task 17.** `4882 KB` · `4 MB and 786 KB` · `96 bits` · 3333 full packets and 500 bytes left over.

**Task 18.** Length 4: `456976`. Length 6: `308915776`. Length 8 with `int`: `-1626332928` (overflow: the true value is bigger than `Integer.MAX_VALUE`, `2147483647`). With `26L`: `208827064576`. `eightBad` is still `-1626332928` because the multiplication is done in `int` before storing. Times at 1000 guesses/s: `456 s`, `5148 min`, `2416 days`.

**Task 19.** One model answer (prints total `341`, `68`, `68.2`, `68.2`):

``` java
int mark1 = 68, mark2 = 73, mark3 = 55, mark4 = 81, mark5 = 64;
int total = mark1 + mark2 + mark3 + mark4 + mark5;
int averageInt = total / 5;
double averageExact = (double) total / 5;
double percentage = total * 100.0 / 500;
```

**Task 20.** One model answer:

``` java
package lab2;

/*
 * Task 20 model answer: Cyber Club event budget report.
 * All values are hard-coded; every result is calculated by Java.
 */
public class Task20EventBudget {

    public static void main(String[] args) {
        // Data
        int ticketsSold = 47;
        double ticketPrice = 3.00;
        double roomCost = 60.00;
        double pizzaCost = 45.50;
        int eventMinutes = 150;
        int teamSize = 4;

        // Calculations
        double income = ticketsSold * ticketPrice;
        double costs = roomCost + pizzaCost;
        double profit = income - costs;
        double profitPerTicket = profit / ticketsSold;
        // cast: keep whole pence only, dropping the fraction of a penny
        int profitPerTicketPence = (int) (profitPerTicket * 100);

        // Report
        System.out.println("CYBER CLUB CTF EVENING - BUDGET");
        System.out.println("===============================");
        System.out.println();
        System.out.println("Income:\t\t" + income);
        System.out.println("Costs:\t\t" + costs);
        System.out.println("Profit:\t\t" + profit);
        System.out.println();
        System.out.println("Profit per ticket: " + profitPerTicket);
        System.out.println("Profit per ticket (pence): " + profitPerTicketPence);
        System.out.println();
        System.out.println("Teams of " + teamSize + ": " + (ticketsSold / teamSize)
                + ", players left over: " + (ticketsSold % teamSize));
        System.out.println("Event length: " + (eventMinutes / 60) + " h "
                + (eventMinutes % 60) + " min");
    }

}
```

Expected results: income `141.0`, costs `105.5`, profit `35.5`, per ticket `0.7553191489361702` and `75` pence, `11` teams with `3` left over, `2 h 30 min`.
