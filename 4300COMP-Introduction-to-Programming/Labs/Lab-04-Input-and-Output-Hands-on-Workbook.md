# Lab 4 — Input and Output Hands-on Workbook (20 Tasks)

**Module:** 4300COMP Introduction to Programming · **Language:** Java

## How to use this lab

This lab has **20 hands-on tasks** on Lecture 4: console output, escape sequences, the Eclipse debugger, reading input with `Scanner`, the `nextInt()`/`nextLine()` trap, and formatting with `printf`. All three official Tutorial 4 tasks are included (marked **official**), plus the supplementary reading.

**Learning outcomes:** MLO1 throughout; MLO2 in Tasks 1–2 (debugger) and 10 (API behaviour); MLO3 in Tasks 15–20.

**Setup:** Tutorial 4 names the project **Lab04**. Use that name, untick module-info, and make one class per task (tick `main`). Every program that reads input needs these two lines:

``` java
import java.util.Scanner;                              // above the class
static Scanner console = new Scanner(System.in);       // first line inside the class
```

**Typing input in Eclipse:** run the program, then **click inside the Console panel** before typing. Press Enter after each value. To stop a program that is waiting for input, click the red square **Terminate** button on the Console toolbar.

**Rules**

1.  Type everything yourself. Predict first, then run.

2.  **Test with the exact inputs given**, then with your own. Write down what you typed and what came out: that is your test evidence.

3.  Use hints in order; the answer key is at the end.

4.  Assume users type sensible values unless a task says otherwise (Tutorial 4 says the same). Validation needs `if`, which comes later.

| Tasks | Focus                                                      | Rough time     |
|-------|------------------------------------------------------------|----------------|
| 1–5   | Output, debugger, printf predictions (official Task 1)     | 5–15 min each  |
| 6–10  | Reading input with Scanner                                 | 10–15 min each |
| 11–15 | Formatted output (official Task 2)                         | 10–20 min each |
| 16–20 | Full input → calculate → output programs (official Task 3) | 20–30 min each |

Task 20 is practice only: it is not an official LJMU assessment and its checklist is not the official marking scheme.

## Tasks 1–5: Output, the debugger and printf

### Task 1 — Output and stepping through (official Tutorial 4, Task 1)

**Class:** `OutputTest` · **Goal:** write console output and run a program one line at a time.

1.  In `main`, type: `System.out.println("Hello and welcome!");` Run it (**Ctrl+F11**).

2.  Add three more lines:

``` java
System.out.println("This is the introduction to programming module");
System.out.print("This line will be continued");
System.out.println(" by the following line");
```

3.  Predict the output, then run.

4.  **Insert a breakpoint** on the `Hello and welcome!` line: double-click in the left margin (or click the line and press **Ctrl+Shift+B**). A blue dot appears.

5.  **Debug** the program: click the bug icon (or press **F11**). Accept the switch to the Debug perspective.

6.  The program pauses with the next line highlighted. Press **F6 (Step Over)** once. Look at the Console. Repeat until the program ends, watching what appears after each step.

7.  Switch back to the Java perspective (top-right icons).

- **Hint 1:** the highlighted line has **not** run yet; it runs when you press F6.

- **Hint 2:** after the `print` line, the Console shows text with no new line until the next statement runs.

### Task 2 — Watch variables change in the debugger

**Class:** `Task02Watch` · **Goal:** use the **Variables** view to see state change (MLO2).

``` java
int total = 0;
total = total + 15;
total = total * 3;
int bonus = total / 4;
total = total - bonus;
System.out.println(total + " " + bonus);
```

1.  Fill in a trace table on paper first.

2.  Put a breakpoint on `int total = 0;`, debug, and press F6 line by line.

3.  After each step, read `total` and `bonus` in the **Variables** panel (top right in the Debug perspective). Compare with your table.

4.  Notice that `bonus` does not appear in the Variables panel until its line has run. Why?

- **Hint 1:** if you can’t see the Variables panel: **Window \> Show View \> Variables**.

- **Hint 2:** a variable only exists once its declaration has been executed.

### Task 3 — Escape sequences

**Class:** `Task03Escapes` · **Goal:** print special characters correctly.

Write one `println` for each line. Gaps on line 3 are tabs.

``` text
He said "Run the scan" and left.
Log saved to D:\logs\scan.txt
It's done.    Status:    OK
{"user": "sam", "admin": false}
```

The last line looks like JSON, a data format you will meet in cyber security tools and web logs.

- **Hint 1:** inside a String, every `"` you want to *show* needs `\"`, and every `\` needs `\\`.

- **Hint 2:** a single quote `'` can be typed directly inside a String; `\'` is only needed inside a `char`.

### Task 4 — Output is just a String: predict

**Class:** `Task04Predict` · **Goal:** predict how text and numbers combine.

``` java
int a = 20, b = 22;
System.out.println("Sum: " + a + b);
System.out.println("Sum: " + (a + b));
System.out.println(a + b + " is the sum");
System.out.print("Line one ");
System.out.println("continues");
System.out.print("No new line");
System.out.println();
String msg = "Total = " + a * b;
System.out.println(msg);
```

Write the exact output (how many lines?). Then run and mark yourself.

- **Hint 1:** left to right; brackets first; `*` before `+`.

- **Hint 2:** an empty `println()` just ends the current line.

### Task 5 — printf predictions

**Class:** `Task05Printf` · **Goal:** read format specifiers like the test will expect.

The square brackets are printed too, so you can see spaces. Predict each, then run all twelve.

| \#  | Statement                      | Your prediction |
|-----|--------------------------------|-----------------|
| a   | `printf("[%d]%n", 7)`          |                 |
| b   | `printf("[%4d]%n", 7)`         |                 |
| c   | `printf("[%-4d]%n", 7)`        |                 |
| d   | `printf("[%04d]%n", 7)`        |                 |
| e   | `printf("[%.3f]%n", 2.5)`      |                 |
| f   | `printf("[%.1f]%n", 9.96)`     |                 |
| g   | `printf("[%8.2f]%n", 12.3456)` |                 |
| h   | `printf("[%s]%n", "cyber")`    |                 |
| i   | `printf("[%8s]%n", "cyber")`   |                 |
| j   | `printf("[%-8s]%n", "cyber")`  |                 |
| k   | `printf("[%d%%]%n", 50)`       |                 |
| l   | `printf("[%,d]%n", 1500000)`   |                 |

(Write each as `System.out.printf(...)` in your code.)

- **Hint 1:** width counts **every** character, including the decimal point.

- **Hint 2:** f: 9.96 to 1 decimal place rounds up — what happens to the 9?

## Tasks 6–10: Reading input with Scanner

### Task 6 — Prompt, read, reply

**Class:** `BasicIO` · **Goal:** your first interactive program.

1.  Prompt for the user’s name and read it with `nextLine()`.

2.  Prompt for their course and read it with `nextLine()`.

3.  Prompt for their favourite programming language and read it.

4.  Print: `Hello Sam Archer, welcome to Cyber Security. Enjoy learning Java!` using the three values.

5.  **Experiment:** delete the first prompt line and run again. How does the program look to a user now?

**Test input:** `Sam Archer` · `Cyber Security` · `Java`

- **Hint 1:** every read follows the pattern: prompt with `print`/`println`, then `variable = console.nextLine();`

- **Hint 2:** `nextLine()` keeps spaces, so a two-word name is fine.

### Task 7 — Read numbers: rectangle calculator

**Class:** `RectangleCalculator` · **Goal:** read `int` values and calculate (the Tutorial 4 example).

Type the Tutorial 4 example: prompts with `print` (not `println`), reads `length` and `width` with `nextInt()`, then prints `Area = 28, perimeter = 22` for inputs 7 and 4.

1.  Test with 7 Enter 4 Enter.

2.  Test with `7 4` typed on **one line** and a single Enter. Does it still work? Why?

3.  Change the program to use `double` and `nextDouble()`, and print the area with `printf` to 2 decimal places. Test with 2.5 and 4.2 (expected area `10.50`).

- **Hint 1:** `nextInt()` reads one **token**, and tokens are separated by any whitespace, including spaces.

- **Hint 2:** `printf("Area = %.2f%n", area);`

### Task 8 — Reproduce and fix the nextInt()/nextLine() trap

**Class:** `Task08Trap` · **Goal:** see the bug happen, then fix it two ways.

**Step 1 — break it.** Type the slide’s program that reads the **age first** with `nextInt()`, then the name with `nextLine()`, then prints `Hello, <name>. You're old enough to have voted in about <(age-18)/5> general elections so far`. Run it and type `40`.

Write down: did the program wait for your name? What was printed?

**Step 2 — fix A.** Add `console.nextLine();` straight after the `nextInt()` line. Test again with `40` then `Sam Archer`.

**Step 3 — fix B.** Undo fix A. Instead read the age as text and convert it: `age = Integer.valueOf(console.nextLine());` Test again.

**Step 4 — explain.** In two sentences, explain what was left in the input buffer and why fix A works.

- **Hint 1:** use the debugger: put a breakpoint on the `nextLine()` line and look at `name` after stepping over it.

- **Hint 2:** the user typed `40` **and** Enter. `nextInt()` only consumed the `40`.

### Task 9 — next() versus nextLine()

**Class:** `Task09Names` · **Goal:** know exactly how much each method reads.

Type the slide example:

``` java
System.out.println("Please enter your first and last names");
firstName = console.next();
lastName = console.nextLine();
System.out.println("Hello, " + firstName + " " + lastName + "|");
```

(The `|` at the end shows where the text stops.) Run it with each input and record the result:

| Input                | `firstName` | `lastName` | Printed |
|----------------------|-------------|------------|---------|
| `Harry`              |             |            |         |
| `Harry Potter`       |             |            |         |
| `Harry James Potter` |             |            |         |

Then fix the program so `Harry Potter` prints `Hello, Harry Potter|` with exactly one space.

- **Hint 1:** `next()` stops at the first space but leaves the rest of the line, **including that space**.

- **Hint 2:** one fix: read both names with `next()`.

### Task 10 — What does Scanner do with bad input?

**Class:** `Task10BadInput` · **Goal:** investigate API behaviour yourself (MLO2) and think like a security tester.

Write a tiny program: prompt, `int n = console.nextInt();`, then `System.out.println("Read: " + n);`. Run it once per input and record what happens.

| Input typed                                                      | Prediction | Actual |
|------------------------------------------------------------------|------------|--------|
| `42`                                                             |            |        |
| ` 42 ` (spaces around) |            |        |
| `-5`                                                             |            |        |
| `007`                                                            |            |        |
| `4 2`                                                            |            |        |
| `42.0`                                                           |            |        |
| `abc`                                                            |            |        |
| `2147483648`                                                     |            |        |
| `1,000`                                                          |            |        |

Then repeat with `nextDouble()` for: `7`, `7.5`, `.5`, `7,5`.

**Compare:** in Lab 3, `Integer.valueOf("1,000")` crashed. What does `nextInt()` do with `1,000`? (Scanner understands thousands separators for your computer’s region settings; `valueOf` does not.)

**Security reflection:** a tester deliberately types unexpected values to see how a program reacts. Which of your inputs would you report as a bug in a real application, and why?

- **Hint 1:** when the program crashes, read the exception name in the first line of the red text.

- **Hint 2:** `4 2` does not crash. Find out what was read and what was left behind.

## Tasks 11–15: Formatted output

### Task 11 — HotelDesk (official Tutorial 4, Task 2)

**Class:** `HotelDesk` · **Goal:** read input and format it exactly with `printf`.

The program prompts for and reads:

- a room number from 1 to 999 (you choose `int` or another type), and

- a room price from 0.99 to 999.99.

Assume the user types valid values. Then, **using `printf`**, output:

- the room number as **3 digits**, zero-padded: room 10 → `Room 010`, room 5 → `Room 005`;

- the price with a £ sign and exactly 2 decimal places: 50 → `£50.00`.

**Test table** (fill in the actual column):

| Room typed | Price typed | Expected               | Actual |
|------------|-------------|------------------------|--------|
| 10         | 50          | `Room 010` / `£50.00`  |        |
| 5          | 0.99        | `Room 005` / `£0.99`   |        |
| 123        | 89.5        | `Room 123` / `£89.50`  |        |
| 999        | 999.99      | `Room 999` / `£999.99` |        |

Then debug it: breakpoint on the first prompt, F6 through each line, and watch `room` and `price` appear in the Variables view after you type them.

- **Hint 1:** `%03d` pads a whole number with zeros to 3 characters.

- **Hint 2:** the £ sign is just text inside the format string: `"Price: £%.2f%n"`. If it shows as `?`, set the Console encoding to UTF-8 (Run \> Run Configurations \> Common \> Encoding).

### Task 12 — Receipt with aligned columns

**Class:** `Task12Receipt` · **Goal:** use widths to line up a table without tabs.

Print this receipt using `printf` with `%-15s`, `%5d`/`%5s` and `%8.2f`/`%8s`:

``` text
Item              Qty    Price
USB cable           2    25.00
Screen wipes        5    19.95
Mouse mat           1     7.25
TOTAL                    52.20
```

Then calculate the TOTAL in Java instead of typing 52.2.

**Extra:** make it interactive: read the three item names (`nextLine()`), quantities and line prices from the user. Watch out for the trap from Task 8.

- **Hint 1:** `-` in `%-15s` means left-aligned; numbers are usually right-aligned so the decimal points line up.

- **Hint 2:** for the header row, use `%5s` and `%8s` with the words "Qty" and "Price" so they match the column widths.

### Task 13 — Percentages and the %% sign

**Class:** `Task13Percent` · **Goal:** calculate and display a percentage.

Read a student’s name (`nextLine()`), the number of questions answered correctly and the total number of questions (`nextInt()`). Print, in one `printf`:

``` text
Sam Archer: 17/20 correct (85.0%)
```

Test with 17/20 (85.0%) and 2/3 (66.7%).

- **Hint 1:** use `* 100.0` so the division is not integer division.

- **Hint 2:** to print a percent sign in `printf`, write `%%`.

### Task 14 — Currency conversion table

**Class:** `Task14Table` · **Goal:** produce a tidy numeric table with widths and precision.

Use a constant exchange rate `final double EUR_PER_GBP = 1.17;` (a made-up practice rate). Print a two-column table for £10, £20, £40, £80 and £160:

``` text
     GBP      EUR
   10.00    11.70
   20.00    23.40
   40.00    46.80
   80.00    93.60
  160.00   187.20
```

Rule: write the row as one `printf` and **repeat the same two lines** (`printf` row, then `gbp = gbp * 2;`) for each row.

- **Hint 1:** `%8.2f` gives width 8 with 2 decimals.

- **Hint 2:** the header uses `%8s` so the words line up with the numbers.

### Task 15 — Movie Ticket Sale (lecture design example)

**Class:** `MovieTicketSale` · **Goal:** go from a brief to a working program, following the lecture’s design steps.

**Brief:** a cinema owner donates a percentage of ticket income to charity. Input: the movie, ticket price, number of tickets sold, donation percentage. Output: the movie, total sales and the donation.

1.  Fill in a design table: each data item, input or output, type, and which Scanner method reads it.

2.  Write the program **without** looking at the lecture notes’ version.

3.  Test with the slide’s data: `Taken 22`, `14`, `250`, `7.5` → `Total sales: £3500.00`, `Donation : £262.50`.

4.  Design two more test cases and work out the expected output by hand **before** running.

- **Hint 1:** the movie name can contain spaces, so it needs `nextLine()`. Read it **first** to avoid the trap.

- **Hint 2:** donation = sales × percentage ÷ 100.

## Tasks 16–20: Complete input → calculate → output programs

### Task 16 — Tokyo restaurant: yen to pounds (official Tutorial 4, Task 3)

**Class:** `YenConverter` · **Goal:** design, test-plan and build a program from a specification. You may work alone or in pairs, as the tutorial allows.

**Specification:** you are in a restaurant in Tokyo. Menu prices are in Japanese yen (¥) and **exclude tax**. Convert each price to pounds and pence **with tax added**. The current rate is £1 = ¥200; the tax rate is 10%. The program must ask the user for the yen price, the conversion rate and the tax rate, then display the sterling value.

**Required steps (from the tutorial):**

1.  **Rough design:** list the inputs, the process (the calculation steps) and the outputs.

2.  **Test data:** design 5 conversions with expected outputs **before** coding. Copy and complete:

| Test | Yen price | Rate | Tax % | Expected £ (by hand) | Actual £ |
|------|-----------|------|-------|----------------------|----------|
| 1    | 2000      | 200  | 10    |                      |          |
| 2    | 3500      | 200  | 10    |                      |          |
| 3    | 980       | 200  | 10    |                      |          |
| 4    | 15000     | 200  | 10    |                      |          |
| 5    | 450       | 200  | 10    |                      |          |

3.  **Write the program.** Show the result as pounds and pence, for example `£11.00`.

4.  Run all five tests and fill in the Actual column.

- **Hint 1:** price with tax = yen + yen × tax ÷ 100. Then pounds = price with tax ÷ rate.

- **Hint 2:** read all three values with `nextDouble()` (a rate could have decimals), and print with `%.2f`.

### Task 17 — Account sign-up form

**Class:** `Task17SignUp` · **Goal:** mix `nextLine()`, `next()` and `nextInt()` safely in one program.

Read, in this order:

1.  Full name (`nextLine()`)

2.  Username (one word: `next()`)

3.  Age (`nextInt()`)

4.  Email address (`nextLine()`)

Then print a summary card with `printf`, labels left-aligned to width 10:

``` text
==== ACCOUNT CREATED ====
Name:     Sam Archer
Username: sam_a
Age:      20
Email:    sam@example.com
=========================
```

Test with exactly those values. If the email comes out empty, you have hit the trap from Task 8: fix it.

**Security note (learning, not production):** real sign-up forms must never print or log passwords, and must check every field. That is why this form does not ask for a password.

- **Hint 1:** after `next()` and `nextInt()`, the rest of the line (including Enter) is still waiting.

- **Hint 2:** one `console.nextLine();` after `nextInt()` clears it.

### Task 18 — Interactive unit converter

**Class:** `Task18Converter` · **Goal:** combine constants (Lecture 3), input and `printf`.

Use constants `KM_PER_MILE = 1.609344`, `LB_PER_KG = 2.20462`, `CM_PER_INCH = 2.54`. Ask the user for a distance in miles, a weight in kg and a height in cm. Print each conversion to 2 decimal places.

Test: 26.2 miles → `42.16 km`; 70 kg → `154.32 lb`; 180 cm → `70.87 inches`.

- **Hint 1:** read each with `nextDouble()`.

- **Hint 2:** one `printf` per line, for example `"%.2f miles = %.2f km%n"`.

### Task 19 — Mini-project: weighted module mark calculator

**Class:** `Task19ModuleMark` · **Goal:** a complete, well-presented interactive program.

The 4300COMP module information lists three assessments: Simple Application **30%**, Complex Application **50%**, In-Class Test **20%**. Build a calculator that:

1.  Asks for the student’s name (full line).

2.  Asks for a mark out of 100 for each of the three assessments (may have decimals).

3.  Uses **constants** for the three weights.

4.  Calculates each weighted contribution and the overall weighted mark.

5.  Prints a neat report with `printf`: name, each mark and its contribution in aligned columns, and the overall mark to 1 decimal place.

**Test:** marks 65, 58, 72 → overall `62.9`. Marks 70, 40, 55 → `52.0`. Design one more test yourself.

This is a **practice calculator** using the weights from the module information. LJMU’s official rules for combining and rounding marks are not covered here; check Canvas for those.

- **Hint 1:** overall = simple × 0.30 + complex × 0.50 + test × 0.20.

- **Hint 2:** columns: `%-22s %6.1f %8.1f%n` works well for name, mark and contribution.

### Task 20 — Assessment-style practice: car park ticket

**Class:** `Task20Parking` · **Time limit:** 30 minutes, no hints.

Practice only: not an official LJMU assessment, and the checklist is not the official marking scheme.

**Specification:** a car park machine prints a ticket. The program must:

1.  Prompt for and read: driver name (may contain spaces), registration (may contain a space, e.g. `AB12 CDE`), ticket number (whole number), hours parked (whole number), hourly rate in £ (decimal).

2.  Use constants for VAT (20%) and minutes per hour.

3.  Calculate the charge before VAT, the VAT and the total.

4.  Print the ticket with `printf`: the ticket number zero-padded to 6 digits, aligned labels, the stay in hours and minutes, and all money to 2 decimal places with a £ sign.

5.  Contain no `nextLine()` bugs, a header comment and section comments.

**Test:** `Sam Archer`, `AB12 CDE`, `42`, `3`, `2.40` → ticket `000042`, stay `3 h (180 min)`, charge `7.20`, VAT `1.44`, total `8.64`.

**Self-check (practice only)**

- Every input has a clear prompt

- Correct Scanner method for each type; names with spaces read fully

- Constants used, no magic numbers

- `%06d`, `%.2f`, `%-12s` style formatting used correctly

- Test case gives exactly the expected values

- A second test case designed and checked by hand

- Comments and consistent layout

### Supplementary (official): preparing for file I/O

Tutorial 4 suggests reading three official Java tutorials before next week: [I/O Streams](https://docs.oracle.com/javase/tutorial/essential/io/streams.html), [Byte Streams](https://docs.oracle.com/javase/tutorial/essential/io/bytestreams.html) and [Character Streams](https://docs.oracle.com/javase/tutorial/essential/io/charstreams.html). Try copying one of the examples into Eclipse; it needs the `xanadu.txt` file described on those pages, placed in your project’s root folder. Step through it with the debugger. Don’t worry if parts are unfamiliar: files are the topic of Lecture 5.

## Progress tracker and reflection

Tick a task when it runs correctly with every test input **and** you could explain every line.

- Task 1 — Output and stepping through (official Task 1)

- Task 2 — Watch variables in the debugger

- Task 3 — Escape sequences

- Task 4 — Output is just a String

- Task 5 — printf predictions (score: \_\_/12)

- Task 6 — Prompt, read, reply

- Task 7 — Rectangle calculator

- Task 8 — The nextInt()/nextLine() trap

- Task 9 — next() versus nextLine()

- Task 10 — Bad input investigation

- Task 11 — HotelDesk (official Task 2)

- Task 12 — Receipt with aligned columns

- Task 13 — Percentages

- Task 14 — Currency table

- Task 15 — Movie Ticket Sale

- Task 16 — Tokyo restaurant (official Task 3)

- Task 17 — Account sign-up form

- Task 18 — Unit converter

- Task 19 — Weighted module mark

- Task 20 — Car park ticket

- Supplementary reading on streams

**Reflection (send me your answers)**

1.  In your own words, what is a stream? Name the two standard ones.

2.  Explain the `nextInt()`/`nextLine()` trap to someone who has never seen it, and give both fixes.

3.  When would you use `printf` instead of `println`?

4.  Which input from Task 10 surprised you most?

5.  What did stepping through with the debugger show you that running normally did not?

6.  Which task did you need hints for?

## Answer key

Use only after a real attempt. All programs were compiled and run with Java 21 (`javac`), with the test input piped in, not inside Eclipse. The Eclipse debugger steps (Tasks 1, 2, 11) were not run.

**Task 1.** Output:

``` text
Hello and welcome!
This is the introduction to programming module
This line will be continued by the following line
```

**Task 2.** `total`: 0 → 15 → 45; `bonus` = 45 / 4 = 11; `total` = 34. Prints `34 11`. `bonus` only appears in Variables once its declaration has run.

**Task 3.**

``` java
System.out.println("He said \"Run the scan\" and left.");
System.out.println("Log saved to D:\\logs\\scan.txt");
System.out.println("It's done.\tStatus:\tOK");
System.out.println("{\"user\": \"sam\", \"admin\": false}");
```

**Task 4.** Six lines: `Sum: 2022` · `Sum: 42` · `42 is the sum` · `Line one continues` · `No new line` · `Total = 440`.

**Task 5.** a `[7]` · b `[ 7]` · c `[7 ]` · d `[0007]` · e `[2.500]` · f `[10.0]` · g `[ 12.35]` · h `[cyber]` · i `[ cyber]` · j `[cyber ]` · k `[50%]` · l `[1,500,000]`.

**Task 6.** Three `print` prompts each followed by `nextLine()`; then `System.out.println("Hello " + name + ", welcome to " + course + ". Enjoy learning " + language + "!");` Without a prompt, the program appears to hang.

**Task 7.** 7 and 4 → `Area = 28, perimeter = 22`, whether typed on two lines or as `7 4` on one line (tokens are split by any whitespace). `double` version with 2.5 and 4.2 → `Area = 10.50`.

**Task 8.** Broken: the name prompt appears but the program doesn’t wait; output `Hello, . You're old enough to have voted in about 4 general elections so far`. Both fixes then print `Hello, Sam Archer. ...`. Explanation: `nextInt()` read `40` but left the Enter (newline) in the buffer; `nextLine()` read up to that newline and returned an empty String. The extra `nextLine()` consumes it.

**Task 9.**

| Input                | `firstName` | `lastName`        | Printed                                                               |
|----------------------|-------------|-------------------|-----------------------------------------------------------------------|
| `Harry`              | `Harry`     | `""`              | `Hello, Harry \|`                                                      |
| `Harry Potter`       | `Harry`     | `" Potter"`       | `Hello, Harry  Potter\|` |
| `Harry James Potter` | `Harry`     | `" James Potter"` | `Hello, Harry  James Potter\|` |

Fix: `lastName = console.next();`

**Task 10.** `nextInt()`: `42` → 42 · spaces around → 42 · `-5` → -5 · `007` → 7 · `4 2` → 4 (the ` 2` stays in the buffer) · `42.0`, `abc` and `2147483648` → InputMismatchException · `1,000` → 1000 (tested with UK and US region settings). `nextDouble()`: `7` → 7.0 · `7.5` → 7.5 · `.5` → 0.5 · `7,5` → InputMismatchException. Bugs worth reporting: any crash on ordinary user typing (`abc`, `42.0`), and `4 2` silently becoming 4.

**Task 11.**

``` java
import java.util.Scanner;

public class HotelDesk {
    static Scanner console = new Scanner(System.in);

    public static void main(String[] args) {
        int room;
        double price;
        System.out.print("Enter the room number (1-999): ");
        room = console.nextInt();
        System.out.print("Enter the room price (0.99-999.99): ");
        price = console.nextDouble();
        System.out.printf("Room %03d%n", room);
        System.out.printf("Price: £%.2f%n", price);
    }
}
```

All four test rows give the expected output.

**Task 12.**

``` java
System.out.printf("%-15s %5s %8s%n", "Item", "Qty", "Price");
System.out.printf("%-15s %5d %8.2f%n", "USB cable", 2, 25.0);
System.out.printf("%-15s %5d %8.2f%n", "Screen wipes", 5, 19.95);
System.out.printf("%-15s %5d %8.2f%n", "Mouse mat", 1, 7.25);
System.out.printf("%-15s %5s %8.2f%n", "TOTAL", "", 25.0 + 19.95 + 7.25);
```

**Task 13.** `System.out.printf("%s: %d/%d correct (%.1f%%)%n", name, correct, total, correct * 100.0 / total);` → `85.0%` and `66.7%`.

**Task 14.** Header `printf("%8s %8s%n", "GBP", "EUR")`; each row `printf("%8.2f %8.2f%n", gbp, gbp * EUR_PER_GBP)` then `gbp = gbp * 2;`. Output matches the task exactly.

**Task 15.** See Lecture 4 notes, Program C. Slide data gives `£3500.00` and `£262.50`.

**Task 16.** Expected values (verified): ¥2000 → £11.00 · ¥3500 → £19.25 · ¥980 → £5.39 · ¥15000 → £82.50 · ¥450 → £2.48 (2.475 rounds up).

``` java
System.out.print("Enter the menu price in yen: ");
double yen = console.nextDouble();
System.out.print("Enter the conversion rate (yen per pound): ");
double rate = console.nextDouble();
System.out.print("Enter the tax rate (%): ");
double tax = console.nextDouble();

double yenWithTax = yen + yen * tax / 100;
double pounds = yenWithTax / rate;
System.out.printf("Price with tax: ¥%.0f = £%.2f%n", yenWithTax, pounds);
```

**Task 17.** Without a fix, `Email:` is empty. Fix: `console.nextLine();` straight after `age = console.nextInt();`. Each card line: `System.out.printf("%-10s%s%n", "Name:", fullName);` (use `%d` for age).

**Task 18.** `42.16 km`, `154.32 lb`, `70.87 inches`.

**Task 19.** 65/58/72 → 19.5 + 29.0 + 14.4 = `62.9`; 70/40/55 → 21.0 + 20.0 + 11.0 = `52.0`.

**Task 20.** One model answer:

``` java
import java.util.Scanner;

/*
 * Task 20 model answer: car park ticket.
 * Reads driver and stay details, prints a formatted ticket.
 */
public class Task20Parking {
    static Scanner console = new Scanner(System.in);

    public static void main(String[] args) {
        // Constants
        final double VAT_RATE = 0.20;
        final int MINUTES_PER_HOUR = 60;

        // Input: text lines first, numbers last (avoids the nextLine trap)
        System.out.print("Driver name: ");
        String driver = console.nextLine();
        System.out.print("Registration: ");
        String reg = console.nextLine();
        System.out.print("Ticket number: ");
        int ticket = console.nextInt();
        System.out.print("Hours parked: ");
        int hours = console.nextInt();
        System.out.print("Hourly rate: ");
        double rate = console.nextDouble();

        // Calculations
        double net = hours * rate;
        double vat = net * VAT_RATE;
        double total = net + vat;

        // Ticket
        System.out.printf("%nTICKET %06d%n", ticket);
        System.out.printf("%-12s%s%n", "Driver:", driver);
        System.out.printf("%-12s%s%n", "Reg:", reg);
        System.out.printf("%-12s%d h (%d min)%n", "Stay:", hours, hours * MINUTES_PER_HOUR);
        System.out.printf("%-12s£%8.2f%n", "Charge:", net);
        System.out.printf("%-12s£%8.2f%n", "VAT 20%:", vat);
        System.out.printf("%-12s£%8.2f%n", "TOTAL:", total);
    }
}
```

Verified output for the test input:

``` text
TICKET 000042
Driver:     Sam Archer
Reg:        AB12 CDE
Stay:       3 h (180 min)
Charge:     £    7.20
VAT 20%:    £    1.44
TOTAL:      £    8.64
```

`"VAT 20%:"` is safe here because it is an **argument**, not part of the format string.
