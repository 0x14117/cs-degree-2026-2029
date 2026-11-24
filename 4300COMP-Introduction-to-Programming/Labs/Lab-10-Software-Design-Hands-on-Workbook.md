# Lab 10 — Software Design (Analysis, Design, Implementation) Hands-on Workbook (20 Tasks)

**Module:** 4300COMP Introduction to Programming · **Language:** Java

## How to use this lab

This lab has **20 hands-on tasks** on Lecture 10: analysing a specification, designing a solution, implementing it in stages and testing it properly. It uses only the Java you already know (Lectures 1–9).

**About the official tutorial:** in the real session, the extended practical is **official Tutorial 10**, a guided analysis, design and implementation exercise for a problem similar to the coursework. That sheet is not in this collection, so its tasks are **not** included here. Do Tutorial 10 from Canvas in your lab session; this workbook is extra practice in the same skills. None of these tasks is the coursework, and none should be used as coursework. Check the official AS2 brief's rules on AI use before asking for any help with it.

**Learning outcomes:** MLO3 (synthesising solutions to specifications) throughout; MLO1 (constructs and algorithms) in Parts C and D.

**Setup:** create a Java project called **Lab10** in Eclipse (untick *Create module-info.java*). Keep a document or notebook open for the analysis and design work: **Tasks 1–12 are mostly done away from the keyboard**, exactly as the slides recommend.

**Rules for this lab:**

1. **No code before design.** For the programming tasks, finish the analysis and design parts first.
2. **Write expected results before you run anything.**
3. **Implement in stages.** Compile and run after each stage.
4. **Record decisions.** Whenever a specification is unclear, write the question and the decision you made.
5. Use the hints only after a real attempt.

The **tracker** is near the end, followed by the **answer key**. Every program in the answer key was compiled and run with Java 21 (javac on the command line, not Eclipse) with the data shown.

## Part A — Analysis (Tasks 1–5)

### Task 1 — IPO tables

**Goal:** separate what a program takes in, does and produces.

Write an IPO table (Inputs with types and source, Processing, Outputs with format) for each specification:

- **(a)** Ask the user for a number of minutes and display it as hours and minutes; for example, 135 displays as `2 h 15 min`.
- **(b)** A taxi charges £3.00 plus £1.80 per mile. Trips **over** 10 miles get 10% off the whole fare. Read the distance in miles (it may be a decimal) and display the fare.
- **(c)** The file `temps.txt` contains 7 daily temperatures in whole degrees Celsius. Display the average temperature to 1 decimal place and the number of days below freezing.

- **Hint 1:** processing says **what**, not how: "convert minutes to hours and remaining minutes", not "use `/` and `%`".
- **Hint 2:** every output row needs a format: decimal places, units, wording.

### Task 2 — Choosing data types

**Goal:** pick the right type for each piece of data, and justify it.

Choose a type for each item and give a one-line reason:

| | Data item | Type | Reason |
| --- | --- | --- | --- |
| 1 | A person's age in years | | |
| 2 | The price of a meal | | |
| 3 | A UK postcode such as `L3 3AF` | | |
| 4 | Whether an item is in stock | | |
| 5 | A grade letter such as `B` | | |
| 6 | The number of students on a module | | |
| 7 | A temperature such as 21.5 °C | | |
| 8 | A phone number such as `07700 900123` | | |
| 9 | A 4-digit PIN such as `0482` | | |
| 10 | A distance in kilometres | | |
| 11 | Whether a customer is a member | | |
| 12 | The number of bytes in a 10 GB file | | |

- **Hint 1:** ask "will I do arithmetic with it?" If not, it may not be a number at all.
- **Hint 2:** for item 12, how big is 10 GB in bytes, and how big can an `int` be (Lab 2)?

### Task 3 — Find the gaps in a vague specification

**Goal:** turn an unclear specification into questions.

> "Write a program that reads customers' ages and works out the ticket price. Children get a discount, pensioners get a bigger discount, and groups get a deal. Show the total."

Write at least **eight** questions you would need answered before you could design this. Then write the **decisions** you would make if you could not ask anyone, clearly labelled as assumptions.

- **Hint 1:** every word like "children", "bigger", "groups" and "deal" hides a number or a rule.
- **Hint 2:** also ask about input (how does entry end?) and output (format, what exactly is "the total"?).

### Task 4 — Write the conversation first

**Goal:** design the exact input and output before coding.

For specification 1(b) (taxi fare), write out **exactly** what the console should show for two runs: a 12.5-mile trip and a 10-mile trip. Include the prompt, what the user types, and the output line, with the fare worked out by hand.

Then answer: why is the 10-mile trip a better test than, say, a 6-mile trip?

- **Hint 1:** 12.5 miles: 3.00 + 1.80 × 12.5, then 10% off.
- **Hint 2:** read the discount rule again: "over 10 miles".

### Task 5 — Find the boundaries

**Goal:** list boundary test values from written rules.

An online shop has these rules:

1. Orders under £10.00 cannot be placed.
2. Delivery is free for orders of £40.00 or more; otherwise it costs £3.99.
3. A single order can contain at most 20 items.
4. Customers must be at least 18 to buy certain items.

For each rule, list the boundary values to test (on the limit and either side) and the expected result for each.

- **Hint 1:** use the smallest step that makes sense: 1p for money, 1 for item counts and ages.
- **Hint 2:** £9.99, £10.00 and £10.01 are the three values around rule 1.

## Part B — Design (Tasks 6–10)

### Task 6 — Pseudocode

**Goal:** write an algorithm in structured plain English.

Write pseudocode for specification 1(c) (temperatures). Use `SET`, `READ`, `FOR`, `IF` and `SHOW` (or your own consistent words). Then list the variables you need, with types.

- **Hint 1:** the number of temperatures is known (7), so which loop?
- **Hint 2:** the average must be a decimal even though the temperatures are whole numbers.

### Task 7 — Flowchart

**Goal:** draw an algorithm.

Draw a flowchart for specification 1(b) (taxi fare). Use rectangles for actions, a diamond for the decision and arrows for the flow. Draw it on paper, or in Mermaid (as in the Lecture 10 notes) if you like. Then check it by following the arrows for 12.5 miles and for 10 miles.

- **Hint 1:** there is exactly one decision.
- **Hint 2:** the discount is applied **after** the full fare is calculated.

### Task 8 — Map steps onto Java

**Goal:** break a problem into steps Java can do directly.

> "Read exam marks from `marks.txt` until the end of the file. Count how many are passes (40 or more), and find the highest mark. Write the number of marks, the number of passes and the highest mark to `summary.txt`."

Fill in a table with one row per step: the step in plain English, and the Java construct(s) you would use (for example, `Scanner` with `FileReader`, `while (read.hasNextInt())`, `if`, `PrintWriter`).

- **Hint 1:** there should be at least seven steps, including opening and closing both files.
- **Hint 2:** "until the end of the file" tells you which loop and which `Scanner` method.

### Task 9 — Desk-check an algorithm

**Goal:** trace a design by hand before any code exists.

```text
SET total TO 0
SET count TO 0
READ n
WHILE n is not 0
    IF n > 0
        total = total + n
        count = count + 1
    READ n
IF count > 0
    SHOW total / count
ELSE
    SHOW "none"
```

1. Trace it with the input `4 -3 8 0`. Use a table with columns `n`, `total`, `count`. What is shown?
2. Trace it with `4 5 0`. If `total` and `count` are `int` in Java, what will the program print? Is that what the designer probably wanted?
3. Trace it with `0`. What is shown?
4. In one sentence, what does this algorithm do?

- **Hint 1:** the negative number is read but not added.
- **Hint 2:** 9 / 2 in `int` arithmetic is…?

### Task 10 — Fix a flawed design

**Goal:** find mistakes at the design stage, when they are cheapest to fix.

This design is meant to read marks until `-1`, then show the average, the number of passes (40 or more) and the number of distinctions (70 or more). It has **five** faults. Find them all and write a corrected design.

```text
READ mark
WHILE mark is not -1
    SET total TO 0
    total = total + mark
    count = count + 1
    IF mark >= 40
        passes = passes + 1
    ELSE IF mark >= 70
        distinctions = distinctions + 1
    READ mark
SHOW total / count
SHOW passes, distinctions
```

- **Hint 1:** look at where things are set to 0, and whether everything is set at all.
- **Hint 2:** can a mark of 85 ever reach the distinction line? What happens if the first mark is `-1`?

## Part C — Analyse, design and implement in stages (Tasks 11–15)

These five tasks take **one** specification through every stage.

> **Specification: weekly step report.** The file `steps.txt` holds 7 whole numbers: a person's step counts for Monday to Sunday, in order. For each day, display the day name (`Mon` to `Sun`), the step count and a category: **Low** (under 5,000), **Moderate** (5,000 to 9,999) or **Active** (10,000 or more). A negative count is a recording error: show `INVALID` and leave it out of the totals. After the table, show the number of valid days, the total steps, the average per valid day to 1 decimal place, the best day and its count, and the longest run of **consecutive** Active days.

Test data for `steps.txt`: `8200 10450 12034 4300 10000 11020 10500`

### Task 11 — Analysis

Write the IPO table for the step report, and list **at least three** questions the specification leaves open, with your decisions. (For example: what if two days tie for best? Does an INVALID day break an Active streak?)

### Task 12 — Design

1. Write a variables table (name, type, purpose). Include constants for 7, 5,000 and 10,000.
2. Choose the loop and explain why.
3. How will you turn the day number (1–7) into a day name? Name the construct.
4. Write pseudocode for the whole program, including the streak logic.
5. **Desk-check** the streak logic with the test data. What should the longest streak be?

- **Hint 1:** keep two variables for streaks: the current run and the longest so far.
- **Hint 2:** an Active day adds 1 to the current run; any other day resets it to 0.

### Task 13 — Implementation stage 1: read and echo

Write `StepReport` so far as: open `steps.txt`, loop 7 times, read each count, and print the day name and the count. Compile, run and check against the file **before** going on.

### Task 14 — Implementation stage 2: categories and totals

Add the category column, the INVALID handling, the count of valid days, the total and the average. Run and check every line against the expected results you worked out in Task 12.

### Task 15 — Implementation stage 3: best day and streak

Add the best day and the longest Active streak. Run with the test data. Expected final lines:

```text
Valid days: 7
Total steps: 66504
Average per valid day: 9500.6
Best day: Wed (12034)
Longest Active streak: 3 day(s)
```

Then format the table neatly with `printf` (day left-aligned, steps right-aligned).

## Part D — Testing, review and full projects (Tasks 16–20)

### Task 16 — Test plan for the step report

**Goal:** test boundaries and invalid data properly.

Replace `steps.txt` with: `4999 5000 9999 10000 -5 0 10000`

1. **Before running**, write the expected category for each day, the number of valid days, the total, the average, the best day and the longest streak.
2. Run, and fill in the actual results.
3. Which day tests each category boundary? Which tests the INVALID rule? Which tests whether the streak resets?
4. Add two more test files of your own: one where **every** day is INVALID, and one where every day is Active. What should happen in each, and does it?

### Task 17 — Refactor: from working to readable

**Goal:** improve code that already works, without changing what it does.

This program works but is hard to read:

```java
public class Messy { public static void main(String[] a){ double x=0; for(int i=0;i<12;i++){x=x+57.5;} System.out.println(x*1.2); if(x*1.2>800) System.out.println("over"); } }
```

It works out the yearly cost of a £57.50-per-month subscription including 20% VAT, and checks it against an £800 budget. Rewrite it so that:

1. every number has a named constant;
2. every variable has a meaningful name;
3. it is laid out over several lines with consistent indentation;
4. the output is `Yearly cost inc. VAT: £828.00` and then either `Over budget by £28.00` or `Within budget, £… to spare`.

Run both versions and check they agree.

### Task 18 — Code review checklist

**Goal:** review your own earlier work like a professional.

Take your answer to Lab 9 Task 20 (or Lab 8 Task 20). Score it against this checklist and write one improvement for each "no":

| Check | Yes / No |
| --- | --- |
| Every requirement in the specification is met | |
| Names describe what variables hold | |
| No magic numbers: rule values are named constants | |
| Indentation is consistent | |
| Comments explain *why*, not *what* | |
| Input is validated where the specification requires it | |
| No division by zero is possible | |
| Money and counts use suitable types | |
| There is a test plan with normal, boundary and invalid rows | |
| Every test has been run and its actual result recorded | |

Make the improvements, re-run your tests, and note what changed.

### Task 19 — Mini-project: broadband speed log (full cycle)

**Goal:** do all four stages yourself, with less guidance.

> **Specification.** A customer runs a broadband speed test several times and saves each result (in Mbps, a decimal) in `speeds.txt`. The provider guarantees at least **30.0 Mbps**. Read every result until the end of the file. Display the number of tests, the average speed (1 decimal place), the slowest and fastest speeds, and how many tests (and what percentage) were below the guaranteed speed. If **more than 20%** of tests were below it, advise `contact your provider`; otherwise `service within the expected range`. If the file has no results, say so.

Test data: `35.2 41.0 28.5 33.3 22.1 38.9 40.2 29.9 36.0 31.4`

Hand in (to yourself): IPO table, questions and decisions, variables table, pseudocode, test plan with at least 6 tests (include an empty file, exactly 30.0, and exactly 20% below), the program, and the completed test plan.

**Cyber security and consumer link:** a log of measurements is **evidence**. Collecting data systematically and summarising it fairly is the same skill used when investigating incidents from log files.

### Task 20 — Assessment-style task: stock reorder report

**Goal:** a more abstract specification, as the slides say you will meet as your skills develop.

This is a practice task similar in skills to the module's application assessments. It is **not** an actual assessment question.

> **Specification.** A small shop keeps its stock in `stock.txt`. The first line says how many items follow. Each item line has a product code (one word), the quantity in stock, the reorder level and the unit price in pence. An item needs reordering when its quantity is at or below its reorder level; the order should bring its stock up to **twice** the reorder level. Produce `reorder.txt` listing each item to reorder with its code, current quantity, order quantity and order cost in pounds, followed by the total order cost. On the console, show how many items were checked, how many are out of stock, how many need reordering, the total value of current stock, and the total order cost.

Test data for `stock.txt`:

```text
5
A100 12 10 250
B200 0 5 1200
C300 40 15 99
D400 7 8 450
E500 15 15 300
```

Produce all the design documents from Task 19, then the program, then a test plan that includes at least: an item exactly at its reorder level, an item one above it, an out-of-stock item, and a file where nothing needs reordering.

- **Hint 1:** keep money in pence (`int`) and divide by `100.0` only when printing.
- **Hint 2:** `PrintWriter` for `reorder.txt`, `Scanner` with `FileReader` for `stock.txt` (Lecture 5).

## Tracker

| Task | Done | Notes |
| --- | --- | --- |
| 1 IPO tables | ☐ | |
| 2 Data types (out of 12) | ☐ | |
| 3 Vague specification | ☐ | |
| 4 Conversation first | ☐ | |
| 5 Boundaries | ☐ | |
| 6 Pseudocode | ☐ | |
| 7 Flowchart | ☐ | |
| 8 Steps to Java | ☐ | |
| 9 Desk-check | ☐ | |
| 10 Flawed design (out of 5) | ☐ | |
| 11 Step report: analysis | ☐ | |
| 12 Step report: design | ☐ | |
| 13 Stage 1 | ☐ | |
| 14 Stage 2 | ☐ | |
| 15 Stage 3 | ☐ | |
| 16 Test plan | ☐ | |
| 17 Refactor | ☐ | |
| 18 Code review | ☐ | |
| 19 Broadband log | ☐ | |
| 20 Stock reorder report | ☐ | |
| Official Tutorial 10 (Canvas) | ☐ | |

## Reflection

1. Which stage did you find hardest: analysis, design, implementation or testing? Why?
2. Did designing first save you time in Tasks 13–15 compared with how you wrote earlier labs?
3. What did your test plans catch that you would otherwise have missed?
4. Write three questions you would ask your tutor about the coursework specification (from the official brief, not this lab).

## Answer key

Design answers have more than one correct form. Compare the **ideas**, not the exact words. All programs were compiled and run with Java 21 (javac, not Eclipse). In a console not set to UTF-8, `£` may print as `?` (Lecture 4).

**Task 1.**

| | Inputs | Processing | Outputs |
| --- | --- | --- | --- |
| (a) | minutes: `int`, console, 0 or more | split into whole hours and remaining minutes | `2 h 15 min` style text |
| (b) | miles: `double`, console, more than 0 | fare = 3.00 + 1.80 × miles; if miles > 10, take 10% off | fare in £ to 2 decimal places |
| (c) | 7 temperatures: `int`, file `temps.txt` | add them up; count those below 0; average = total / 7 | average to 1 dp; count of days below freezing |

(a) is `minutes / 60` and `minutes % 60` when implemented: 135 → `2 h 15 min` (verified).

**Task 2.** 1 `int` · 2 `double` (or `int` pence if you will add up many prices) · 3 `String` · 4 `boolean` · 5 `char` (or `String`) · 6 `int` · 7 `double` · 8 `String` (not calculated with; `int` would lose the leading 0 and is too small) · 9 `String` (leading 0; never calculated with) · 10 `double` · 11 `boolean` · 12 `long` (10 GB is about 10,000,000,000 bytes, larger than the `int` maximum of 2,147,483,647).

**Task 3.** Example questions: What ages count as a child? As a pensioner? Are the age limits inclusive? What is the full price? How big is each discount (amount or percentage)? How many people make a group? What is the group deal, and does it combine with other discounts? How does entry end? What happens with an invalid age (negative, 150)? Is "the total" the total cost, the number of tickets, or both? What format should prices use? Any decisions you make must be written down and labelled as assumptions.

**Task 4.**

```text
Distance in miles: 12.5
Fare: £22.95
```

```text
Distance in miles: 10
Fare: £21.00
```

(Both fares verified.) 12.5 miles: 3.00 + 22.50 = 25.50, minus 10% = 22.95. 10 miles: no discount, because 10 is not **over** 10. It is the boundary, so it catches a `>=` written instead of `>`; a 6-mile trip tests nothing interesting.

**Task 5.**

| Rule | Test values → expected |
| --- | --- |
| Minimum order £10 | £9.99 → rejected; £10.00 → accepted; £10.01 → accepted |
| Free delivery from £40 | £39.99 → £3.99 delivery; £40.00 → free; £40.01 → free |
| Max 20 items | 19 → OK; 20 → OK; 21 → rejected; also 0 → rejected (at least 1 item) |
| Age 18+ | 17 → refused; 18 → allowed; 19 → allowed |

**Task 6.**

```text
SET total TO 0
SET belowZero TO 0
OPEN temps.txt
FOR day FROM 1 TO 7
    READ temp
    total = total + temp
    IF temp < 0
        belowZero = belowZero + 1
CLOSE file
SET average TO total / 7   (as a decimal)
SHOW average to 1 dp
SHOW belowZero
```

Variables: `total` `int`, `belowZero` `int`, `temp` `int`, `average` `double`, constant `DAYS = 7`. A `for` loop, because the count (7) is known.

**Task 7.** Start → read miles → fare = 3.00 + 1.80 × miles → diamond "miles > 10?" → yes: fare = fare × 0.9 → (both branches) show fare → end. Following it with 12.5 takes the "yes" branch (£22.95); with 10 it takes "no" (£21.00).

**Task 8.**

| Step | Java |
| --- | --- |
| Open the marks file | `Scanner read = new Scanner(new FileReader("marks.txt"));` with `throws FileNotFoundException` |
| Set count, passes and highest | `int` variables before the loop |
| Repeat until end of file | `while (read.hasNextInt())` |
| Read a mark | `read.nextInt()` |
| Count it; count a pass if ≥ 40 | `count++`; `if (mark >= 40) passes++;` |
| Update the highest | `if (count == 1 \|\| mark > highest)` |
| Close the input | `read.close()` |
| Open the output file and write three lines | `PrintWriter out = new PrintWriter("summary.txt");` and `out.println(...)` |
| Close the output | `out.close()` (otherwise the file may be empty) |

**Task 9.** (1) `n` 4 → total 4, count 1; `n` −3 → skipped; `n` 8 → total 12, count 2; `n` 0 → stop. Shows `6`. (2) total 9, count 2; with `int` arithmetic it prints `4`, but the average is 4.5. The design should say the division is decimal. (3) Shows `none`. (4) It shows the average of the positive numbers entered before 0.

**Task 10.** Faults: (1) `total` is reset to 0 **inside** the loop, so only the last mark is kept; set it once before the loop. (2) `count`, `passes` and `distinctions` are never set to 0. (3) The `ELSE IF mark >= 70` can never run, because any mark of 70+ already matched `>= 40`; use two separate `IF`s (a distinction is also a pass), or test 70 first if they are meant to be separate categories. (4) If the first mark is `-1`, `count` is 0 and the average divides by zero; check `count > 0` first. (5) `total / count` would be integer division; make the average a decimal. Corrected:

```text
SET total, count, passes, distinctions TO 0
READ mark
WHILE mark is not -1
    total = total + mark
    count = count + 1
    IF mark >= 40 THEN passes = passes + 1
    IF mark >= 70 THEN distinctions = distinctions + 1
    READ mark
IF count > 0
    SHOW total / count as a decimal
ELSE
    SHOW "no marks"
SHOW passes, distinctions
```

**Task 11.** Inputs: 7 step counts, `int`, file `steps.txt`. Processing: categorise each day; skip negatives from totals; count valid days; total; average; best day; longest run of consecutive Active days. Outputs: a table of day, steps, category; then the five summary lines. Example decisions: a tie for best keeps the **first** day; an INVALID day **breaks** a streak; if all days are INVALID, skip the average and best-day lines.

**Task 12.** Constants `DAYS = 7`, `MODERATE = 5000`, `ACTIVE = 10000`. Variables `steps`, `validDays`, `total`, `best` (`int`); `bestDay`, `dayName`, `category` (`String`); `streak`, `longestStreak` (`int`). A `for` loop (exactly 7 days). A `switch` on the day number gives the name. Desk-check of the streak with the test data: Mon 0, Tue 1, Wed 2, Thu 0, Fri 1, Sat 2, Sun 3 → longest **3**.

**Tasks 13–15.** Final program:

```java
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Scanner;

public class StepReport {
    public static void main(String[] args) throws FileNotFoundException {
        final int DAYS = 7;
        final int MODERATE = 5000;     // 5000 to 9999 steps
        final int ACTIVE = 10000;      // 10000 steps or more

        Scanner read = new Scanner(new FileReader("steps.txt"));
        int validDays = 0;
        int total = 0;
        int best = -1;
        String bestDay = "";
        int streak = 0;                // current run of Active days
        int longestStreak = 0;

        System.out.printf("%-4s %7s  %s%n", "Day", "Steps", "Category");
        for (int day = 1; day <= DAYS; day++) {
            int steps = read.nextInt();

            String dayName;
            switch (day) {
                case 1: dayName = "Mon"; break;
                case 2: dayName = "Tue"; break;
                case 3: dayName = "Wed"; break;
                case 4: dayName = "Thu"; break;
                case 5: dayName = "Fri"; break;
                case 6: dayName = "Sat"; break;
                default: dayName = "Sun"; break;
            }

            String category;
            if (steps < 0) {
                category = "INVALID";
            } else if (steps >= ACTIVE) {
                category = "Active";
            } else if (steps >= MODERATE) {
                category = "Moderate";
            } else {
                category = "Low";
            }
            System.out.printf("%-4s %7d  %s%n", dayName, steps, category);

            if (steps >= 0) {
                validDays++;
                total = total + steps;
                if (steps > best) {
                    best = steps;
                    bestDay = dayName;
                }
            }

            if (steps >= ACTIVE) {
                streak++;
                if (streak > longestStreak) {
                    longestStreak = streak;
                }
            } else {
                streak = 0;            // the run is broken
            }
        }
        read.close();

        System.out.println();
        System.out.println("Valid days: " + validDays);
        System.out.println("Total steps: " + total);
        if (validDays > 0) {
            System.out.printf("Average per valid day: %.1f%n", (double) total / validDays);
            System.out.println("Best day: " + bestDay + " (" + best + ")");
        }
        System.out.println("Longest Active streak: " + longestStreak + " day(s)");
    }
}
```

Output with the test data (verified):

```text
Day    Steps  Category
Mon     8200  Moderate
Tue    10450  Active
Wed    12034  Active
Thu     4300  Low
Fri    10000  Active
Sat    11020  Active
Sun    10500  Active

Valid days: 7
Total steps: 66504
Average per valid day: 9500.6
Best day: Wed (12034)
Longest Active streak: 3 day(s)
```

**Task 16.** Expected and actual (verified): Mon 4999 Low · Tue 5000 Moderate · Wed 9999 Moderate · Thu 10000 Active · Fri −5 INVALID · Sat 0 Low · Sun 10000 Active. Valid days 6; total 39998; average 6666.3; best Thu (10000) (Sun ties, and the first is kept because the test is `>`); longest streak 1 (Fri's INVALID breaks the run). Mon/Tue test the Low/Moderate boundary, Wed/Thu the Moderate/Active boundary, Fri the INVALID rule, Sat zero. All INVALID: valid days 0, total 0, no average or best line, streak 0. All Active: streak 7.

**Task 17.**

```java
public class YearlyCost {
    public static void main(String[] args) {
        final double MONTHLY_FEE = 57.50;   // pounds, before VAT
        final int MONTHS = 12;
        final double VAT_RATE = 0.20;
        final double BUDGET = 800.00;

        double yearlyNet = 0;
        for (int month = 1; month <= MONTHS; month++) {
            yearlyNet = yearlyNet + MONTHLY_FEE;
        }
        double yearlyGross = yearlyNet * (1 + VAT_RATE);
        System.out.printf("Yearly cost inc. VAT: £%.2f%n", yearlyGross);
        if (yearlyGross > BUDGET) {
            System.out.printf("Over budget by £%.2f%n", yearlyGross - BUDGET);
        } else {
            System.out.printf("Within budget, £%.2f to spare%n", BUDGET - yearlyGross);
        }
    }
}
```

The messy version prints `828.0` and `over`; the refactored version prints `Yearly cost inc. VAT: £828.00` and `Over budget by £28.00` (both verified). (The loop could simply be `MONTHLY_FEE * MONTHS`; it is kept to match the original.)

**Task 18.** Your own review; there is no single answer. The most common findings are magic numbers, missing zero checks before dividing, and tests that were planned but never run.

**Task 19.**

```java
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Scanner;

public class BroadbandLog {
    public static void main(String[] args) throws FileNotFoundException {
        final double GUARANTEED = 30.0;          // Mbps promised by the provider
        final double COMPLAINT_PERCENT = 20.0;   // complain if more than this % of tests are below

        Scanner read = new Scanner(new FileReader("speeds.txt"));
        int tests = 0;
        int below = 0;
        double total = 0;
        double fastest = 0;
        double slowest = 0;

        while (read.hasNextDouble()) {
            double speed = read.nextDouble();
            tests++;
            total = total + speed;
            if (tests == 1 || speed > fastest) {
                fastest = speed;
            }
            if (tests == 1 || speed < slowest) {
                slowest = speed;
            }
            if (speed < GUARANTEED) {
                below++;
            }
        }
        read.close();

        if (tests == 0) {
            System.out.println("No speed tests found.");
        } else {
            double percentBelow = 100.0 * below / tests;
            System.out.println("Tests: " + tests);
            System.out.printf("Average: %.1f Mbps (slowest %.1f, fastest %.1f)%n", total / tests, slowest, fastest);
            System.out.printf("Below %.1f Mbps: %d (%.1f%%)%n", GUARANTEED, below, percentBelow);
            if (percentBelow > COMPLAINT_PERCENT) {
                System.out.println("Advice: contact your provider.");
            } else {
                System.out.println("Advice: service within the expected range.");
            }
        }
    }
}
```

Output with the test data (verified):

```text
Tests: 10
Average: 33.6 Mbps (slowest 22.1, fastest 41.0)
Below 30.0 Mbps: 3 (30.0%)
Advice: contact your provider.
```

Design notes: an EOF-controlled `while` (unknown number of tests, could be zero); `%%` prints a percent sign in `printf`; exactly 30.0 is **not** below the guarantee; exactly 20% below is **not** "more than 20%", so the advice is "within the expected range".

**Task 20.**

```java
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.PrintWriter;
import java.util.Scanner;

public class StockReport {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner read = new Scanner(new FileReader("stock.txt"));
        PrintWriter out = new PrintWriter("reorder.txt");

        int items = read.nextInt();
        int outOfStock = 0;
        int toReorder = 0;
        int stockValue = 0;       // pence
        int orderTotal = 0;       // pence

        out.printf("%-6s %4s %5s %10s%n", "Code", "Have", "Order", "Cost (£)");
        for (int i = 1; i <= items; i++) {
            String code = read.next();
            int quantity = read.nextInt();
            int reorderLevel = read.nextInt();
            int pricePence = read.nextInt();

            stockValue = stockValue + quantity * pricePence;
            if (quantity == 0) {
                outOfStock++;
            }
            if (quantity <= reorderLevel) {
                int orderQty = 2 * reorderLevel - quantity;   // top up to twice the reorder level
                int cost = orderQty * pricePence;
                out.printf("%-6s %4d %5d %10.2f%n", code, quantity, orderQty, cost / 100.0);
                toReorder++;
                orderTotal = orderTotal + cost;
            }
        }
        out.printf("Total order cost: £%.2f%n", orderTotal / 100.0);
        read.close();
        out.close();

        System.out.println("Items checked: " + items);
        System.out.println("Out of stock: " + outOfStock);
        System.out.println("Items to reorder: " + toReorder + " (see reorder.txt)");
        System.out.printf("Stock value: £%.2f%n", stockValue / 100.0);
        System.out.printf("Order cost: £%.2f%n", orderTotal / 100.0);
    }
}
```

Console output (verified):

```text
Items checked: 5
Out of stock: 1
Items to reorder: 3 (see reorder.txt)
Stock value: £146.10
Order cost: £205.50
```

`reorder.txt` (verified):

```text
Code   Have Order   Cost (£)
B200      0    10     120.00
D400      7     9      40.50
E500     15    15      45.00
Total order cost: £205.50
```

E500 (15 with reorder level 15) tests "at the reorder level"; A100 (12 with level 10) is above it and correctly not listed; B200 is out of stock. Design choices worth noting in your documents: a `for` loop because the file states the count; money in pence; `PrintWriter` closed so the file is actually written.

**Next:** Lecture 11, arrays: the first way to store a whole collection of values in one variable.
