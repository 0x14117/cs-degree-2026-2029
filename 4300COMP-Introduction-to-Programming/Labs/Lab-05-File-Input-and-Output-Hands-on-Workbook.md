# Lab 5 — File Input and Output Hands-on Workbook (20 Tasks)

**Module:** 4300COMP Introduction to Programming · **Language:** Java

## How to use this lab

This lab has **20 hands-on tasks** on Lecture 5: writing files with `PrintWriter`, reading files with `FileReader` + `Scanner`, file locations, schemas, checked exceptions and `throws`, and closing files. All four official Tutorial 5 tasks and the supplementary task are included (marked **official**).

**Learning outcomes:** MLO1 throughout; MLO2 in Tasks 1 and 5 (Eclipse imports, the Java API); MLO3 in Tasks 9–20.

**Setup:** Tutorial 5 names the project **Lab05**. Untick module-info; one class per task with `main` ticked. Every file program needs `throws FileNotFoundException` on `main` and the right imports (press **Ctrl+Shift+O** to add them).

**Creating a data file in Eclipse:** right-click the **Lab05** project (not `src`) \> **New \> File**, type the exact name (e.g. `prog.txt`), click Finish, paste the data, **save** (Ctrl+S). It must appear directly under Lab05, next to `src`.

**Seeing a file your program wrote:** right-click Lab05 \> **Refresh** (F5), then double-click the file.

**Rules**

1.  Type everything yourself. Predict first, then run.

2.  **Write the file’s schema** (items, order, separators, types) before writing any reading code.

3.  Use hints in order; the answer key is at the end.

4.  Data files are assumed to be correct unless a task says otherwise. Handling bad files properly needs `if` and exceptions, which come later.

| Tasks | Focus                                            | Rough time     |
|-------|--------------------------------------------------|----------------|
| 1–5   | Writing files (official Task 1)                  | 5–15 min each  |
| 6–10  | Reading files (official Task 2)                  | 10–20 min each |
| 11–15 | Read, calculate, write (official Tasks 3–4)      | 15–25 min each |
| 16–20 | Larger programs, supplementary, assessment-style | 20–30 min each |

Task 20 is practice only: it is not an official LJMU assessment and its checklist is not the official marking scheme.

## Tasks 1–5: Writing files

### Task 1 — Your first output file (official Tutorial 5, Task 1)

**Class:** `FileOutputTest` · **Goal:** write a file and use Eclipse’s two import helpers.

1.  Create project **Lab05** and class **FileOutputTest** with `main` ticked.

2.  **Auto-complete:** on the `main` line, after `(String[] args)`, type ` throws FileNot` and press **Ctrl+Space**. Choose `FileNotFoundException`. Look at the top of the file: what did Eclipse add?

3.  **Organise Imports:** inside `main`, type `PrintWriter write = new PrintWriter("test1.txt");` It is underlined in red. Press **Ctrl+Shift+O** (Source \> Organise Imports). What did Eclipse add this time?

4.  Add the last two lines:

``` java
write.println("Hello file! Welcome to LJMU");
write.close();
```

5.  Run (Ctrl+F11). The Console is empty: that is correct.

6.  Right-click **Lab05** \> **Refresh** (F5). Find `test1.txt` in the project root and double-click it. Check its contents.

- **Hint 1:** if Ctrl+Space does nothing (some keyboards switch language), use **Edit \> Content Assist**.

- **Hint 2:** the file is in **Lab05**, not inside `src`.

### Task 2 — print, println and printf go to files too

**Class:** `Task02Profile` · **Goal:** prove PrintWriter works exactly like `System.out`.

Write **the same five lines twice**: once with `System.out`, once with a PrintWriter to `profile.txt`.

``` text
STUDENT PROFILE
Name: Sam Archer
Module: 4300COMP
Week 5 topic: File I/O
Progress: 25.0%
```

Rules: use `println` for line 1, `print` + `println` for line 2, and `printf` for lines 3–5 (the percentage must come from a `double` variable with `%.1f%%`).

Compare the Console with `profile.txt`. They should be identical.

- **Hint 1:** in `printf`, `%%` prints a percent sign, and `%n` ends the line.

- **Hint 2:** use a variable name like `file` for the PrintWriter so the two blocks look alike: `System.out.printf(...)` / `file.printf(...)`.

### Task 3 — What happens if you forget close()?

**Class:** `Task03Close` · **Goal:** see the output buffer for yourself.

1.  Write one line, `Will I appear?`, to `close-test.txt` and **do not** call `close()`. Run, Refresh, open the file. What is in it?

2.  Add `write.flush();` (but still no `close()`). Run, Refresh, open. What changed?

3.  Replace `flush()` with `close()`. Run again.

4.  Explain in two sentences what the buffer is and what `flush()` and `close()` do.

- **Hint 1:** PrintWriter keeps text in memory and only writes to disk in chunks.

- **Hint 2:** the file is created as soon as the PrintWriter is created, even if nothing reaches it.

### Task 4 — Overwriting and multiple files

**Class:** `Task04Overwrite` · **Goal:** know what PrintWriter does to an existing file.

1.  Write `Run number 1` to `runs.txt`. Run, Refresh, check.

2.  Change the text to `Run number 2`. Run, Refresh, check. Is `Run number 1` still there?

3.  Now write to **two** files in the same program: `summary.txt` gets one line, `details.txt` gets three lines. Use two PrintWriter variables and close both.

**Warning for later:** never use your **input** file’s name as an output file. PrintWriter would wipe it.

- **Hint 1:** creating a PrintWriter on an existing file empties it straight away.

- **Hint 2:** two variables: `PrintWriter summary = ...;` and `PrintWriter details = ...;`

### Task 5 — Where do files go? (MLO2)

**Class:** `Task05Location` · **Goal:** find out where Java reads and writes relative files.

1.  Print the folder Java is running in: `System.out.println(System.getProperty("user.dir"));` Find this method in the [System class documentation](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/System.html#getProperty(java.lang.String)). Compare the printed path with your Eclipse workspace and Lab05 folder.

2.  Create `where.txt` inside the **`src`** folder (not the project root). Try `new FileReader("where.txt")` (with throws). What happens? Read the exception message.

3.  Move the file to the project root (drag it in the Package Explorer). Run again.

4.  Write a file using an **absolute** path. On a university PC, your M drive is a good choice: `"M:\\abs-test.txt"`. At home, choose a folder you know, e.g. `"C:\\Users\\<you>\\Documents\\abs-test.txt"`. Find the file in Windows Explorer.

- **Hint 1:** `user.dir` in Eclipse is the project root folder.

- **Hint 2:** every backslash in a Java String must be doubled.

## Tasks 6–10: Reading files

### Task 6 — The lecture’s pay program

**Class:** `FileInput` · **Goal:** read one record and calculate from it.

1.  Create `prog.txt` in the project root containing: `David 36 22.75 37`

2.  Write the lecture’s program: read name (`next()`), age (`nextInt()`), rate (`nextDouble()`), hours (`nextInt()`), close the Scanner, then print `Pay for David: £841.75` with `printf`.

3.  Change the file to `John 32 Pittance! 60`. Run. Which exception, and on which read?

4.  Change it back. Now **rename** the file to `Prog.txt` (capital P) and run. On Windows this may still work; explain why it is risky to rely on that.

5.  Delete the throws clause. What compile error do you get?

- **Hint 1:** the `throws` clause and its import (`java.io.FileNotFoundException`) go on the `main` line.

- **Hint 2:** Windows ignores capital letters in file names, but Linux and macOS do not. Java programs often run on Linux servers.

### Task 7 — Design from a schema

**Class:** `Task07Laptop` · **Goal:** turn a written file structure into reading code.

**Schema** for `laptop.txt`:

``` text
<model name, may contain spaces> (new line)
<RAM in GB, whole number> (space) <storage in GB, whole number> (space) <price in pounds, decimal> (space) <in stock: true or false> (new line)
```

**Example file:**

``` text
Dell XPS 13
16 512 1299.99 true
```

1.  Fill in a plan table: item, Java type, Scanner method.

2.  Write the program and print: `Dell XPS 13: 16 GB RAM, 512 GB storage, £1299.99, in stock: true`

3.  Write a second test file for a different laptop and check the output by hand.

- **Hint 1:** Scanner has `nextBoolean()` for `true`/`false` (look it up in the Scanner API).

- **Hint 2:** read the model with `nextLine()` **first** — then the trap cannot happen.

### Task 8 — Same data, different layouts

**Class:** `Task08Layouts` · **Goal:** understand how Scanner splits a file into tokens.

Keep the Task 6 reading code (four `next...` calls). Run it against each version of the file:

| File | Contents                                                                           |
|------|------------------------------------------------------------------------------------|
| A    | `David 36 22.75 37` on one line                                                    |
| B    | each value on its own line (4 lines)                                               |
| C    | `David 36`, then a blank line, then `22.75` and `37` separated by spaces and a tab |

Does the output change? Explain why.

**Part 2 — the trap returns.** Create `staff.txt`:

``` text
1042
Sam Archer
12.50
```

Read it with `nextInt()`, then `nextLine()`, then `nextDouble()`. What happens? Fix it.

- **Hint 1:** `next()`, `nextInt()` and `nextDouble()` skip **any** whitespace: spaces, tabs, new lines, blank lines.

- **Hint 2:** after `nextInt()` reads `1042`, the rest of that line (just the newline) is still waiting.

### Task 9 — Vehicle fuel data (official Tutorial 5, Task 2)

**Class:** `VehicleFuel` · **Goal:** plan and implement reading a real file format.

The file holds fuel details for a vehicle. **Schema:**

``` text
<Vehicle brand and model> (new line)
<Economy, mpg (imperial), 1dp> (space) <Fuel capacity, whole litres> (space) <Fuel cost per litre, pence, 1dp> (new line)
```

**Example file** `vehicle.txt` (download from Canvas or create it):

``` text
Nissan Juke
46.5 50 129.9
```

**Before coding, decide:** where the file goes and its name; the variable and type for each item; how to open it (with the throws clause); the order of reads; and how to produce the output.

**Required console output** (values from the file):

``` text
Vehicle Nissan Juke holds 50 litres of fuel at a cost of 129.9 p/litre.
On average, it returns 46.5 mpg.
```

The two decimals must be shown to 1 dp. Keep this program: Tasks 11 and 12 build on it.

- **Hint 1:** the model contains a space, so read it with `nextLine()`.

- **Hint 2:** `printf` with `%s`, `%d` and `%.1f`.

### Task 10 — Bug hunt: eight file errors

**Goal:** recognise every common file mistake from its symptom. For each, make the mistake on purpose in a copy of Task 6, record the exact message, then fix it.

| \#  | Mistake to make                                   | Symptom (javac / Java 21 on Linux)                                                    |
|-----|---------------------------------------------------|---------------------------------------------------------------------------------------|
| 1   | Remove `throws FileNotFoundException`             | `unreported exception FileNotFoundException; must be caught or declared to be thrown` |
| 2   | Remove the `import java.io.FileReader;` line      | `cannot find symbol`                                                                  |
| 3   | Move `prog.txt` into `src`                        | `FileNotFoundException: prog.txt (No such file or directory)`                         |
| 4   | Use the path `"M:\prog.txt"` with one backslash   | `illegal escape character`                                                            |
| 5   | Swap the `nextDouble()` and `nextInt()` reads     | `InputMismatchException`                                                              |
| 6   | Change the file to `David 36` only                | `NoSuchElementException`                                                              |
| 7   | In a PrintWriter program, delete `close()`        | No error, but the output file is empty                                                |
| 8   | Read `nextInt()` then `nextLine()` on `staff.txt` | Name is empty; the next read crashes                                                  |

For each row, add a column in your notes: **compile error, runtime error, or logic error?**

- **Hint 1:** on Windows, number 3’s message says “The system cannot find the file specified”.

- **Hint 2:** number 5 crashes because `nextInt()` meets `22.75`.

## Tasks 11–15: Read, calculate, write

### Task 11 — Cost to fill and range (official Tutorial 5, Task 3)

**Class:** extend `VehicleFuel` from Task 9 (or copy it to `VehicleFuel3`).

**Facts:** there are **4.54609 litres** in an imperial gallon. The tank is empty at the start.

Extend the program so it calculates:

- the **cost to fill the tank** (capacity × pence per litre, converted to pounds);

- the **range**: range = mpg × capacity in **gallons** (convert litres to gallons first).

Then add these console lines:

``` text
It will cost £<price, pounds.pence> to fuel the vehicle at the specified rates.
On average, this will give the vehicle a range of <range> miles.
```

**Plan your test first:** work out the Nissan Juke values by hand (calculator allowed) before running. Then test with two more vehicles of your own.

- **Hint 1:** make the gallon factor a constant: `final double LITRES_PER_GALLON = 4.54609;`

- **Hint 2:** pounds = litres × pence ÷ 100; gallons = litres ÷ 4.54609.

### Task 12 — Write the results file (official Tutorial 5, Task 4)

**Class:** extend your Task 11 program.

No new calculations: produce `output.txt` with this **schema**. Lines 1–2 have the same format as the input file:

``` text
<Vehicle brand and model> (new line)
<Economy, mpg, 1dp> (space) <Fuel capacity, whole litres> (space) <Fuel cost per litre, pence, 1dp> (new line)
<Range in miles, 1dp> (space) <Cost to fill tank, pounds.pence, 2dp> (new line)
```

Remember to close the PrintWriter, and Refresh the project to see the file. Open it and check every value and space.

**Extra challenge:** because lines 1–2 copy the input format exactly, Task 9’s program should be able to read `output.txt` as if it were `vehicle.txt`. Try it by changing the input filename.

- **Hint 1:** `out.println(model);` then `out.printf("%.1f %d %.1f%n", ...)`.

- **Hint 2:** the cost goes in **without** a £ sign; the schema says pounds.pence only.

### Task 13 — Grade Calculator (lecture design example)

**Class:** `GradeCalculator` · **Goal:** implement the lecture brief yourself.

**Brief:** read a student’s latest five test scores from `grades.txt` and write their name and average to `average.txt` in the form `Student: John; Average: 57.80`. Also show the same line on the console.

1.  Follow the lecture’s design steps (data and types, open, read each item, calculate, write).

2.  Use `+=` to build the total.

3.  Test with `John 45 60 75 66 43` (should give 57.80) and with `John 39 45 60 75 66` (the design slide’s file). Write both expected averages down **before** running.

4.  Change the data file so the five scores are on five separate lines. Does your program still work?

- **Hint 1:** start `double average = 0;` then `average += scan.nextDouble();` five times, then divide by 5.

- **Hint 2:** see Lecture 5 notes, Program B, if you get stuck.

### Task 14 — Round trip: write a file, then read it back

**Class:** `Task14RoundTrip` · **Goal:** see why writer and reader must agree on the schema.

1.  **Write part:** store `name = "Sam Archer"`, `year = 1`, `credits = 120.0`, `fullTime = true` in variables, and write them to `student.txt` with this schema: name on line 1; year, credits (1 dp) and fullTime separated by spaces on line 2. Close it.

2.  **Read part (same program, after closing):** open `student.txt`, read the four values back into **new** variables, and print them separated by `|`: `Sam Archer|1|120.0|true`.

3.  **Break it:** change the writer so it puts the name on the **same line** as the numbers. What happens to the reader? What does this teach you about file formats?

- **Hint 1:** for the boolean, write with `%b` and read with `nextBoolean()`.

- **Hint 2:** you must `close()` the writer before reading, or the data may still be in the buffer.

### Task 15 — Security log summary

**Class:** `Task15LogSummary` · **Goal:** turn raw log data into a short report (a common cyber security job).

`access.txt` schema: server name (line 1); username, successful logins and failed logins separated by spaces (line 2).

``` text
web-01
sam 120 6
```

Write `security_report.txt`:

``` text
Security report for web-01
User: sam
Logins: 126 total, 6 failed (4.76%)
```

Then test with a second file where failures are high (e.g. `bob 12 48`) and check the percentage by hand.

**Learning note:** a high failure rate can indicate someone guessing passwords. Next lecture’s `if` statements will let the program flag it automatically.

- **Hint 1:** failure % = failed × 100.0 ÷ (successful + failed).

- **Hint 2:** in `printf`, `%.2f%%` shows two decimals and a percent sign.

## Tasks 16–20: Larger programs

### Task 16 — Payslip generator

**Class:** `Task16Payslip` · **Goal:** a full read → calculate → formatted-write program.

`payroll.txt` schema: employee name (line 1, may contain spaces); hourly rate, standard hours and overtime hours separated by spaces (line 2).

``` text
Sam Archer
12.50 37 5
```

Overtime is paid at 1.5 × the hourly rate (make 1.5 a constant). Write `payslip.txt`:

``` text
PAYSLIP
Employee:   Sam Archer
Basic:      37 h @ £12.50 = £  462.50
Overtime:    5 h @ £18.75 = £   93.75
Gross pay:                  £  556.25
```

The £ signs and decimal points must line up.

- **Hint 1:** labels `%-12s`, hours `%2d`, money `%8.2f`.

- **Hint 2:** for the last line, pad with an empty String of the right width: count the characters in `37 h @ £12.50 = `.

### Task 17 — Read a configuration file

**Class:** `Task17Config` · **Goal:** read mixed types, including a `boolean`.

Programs often read their settings from a config file. `app.conf` schema: application name (line 1); port (whole number), timeout in seconds (decimal) and debug mode (`true`/`false`) on line 2.

``` text
PortScanner Lite
8080 2.5 false
```

Print:

``` text
Application: PortScanner Lite
Port: 8080
Timeout: 2.5 s (2500 ms)
Debug mode: false
```

Then change the file to `debug` = `yes` and run. What happens, and why does that matter for a real tool?

**Security note:** debug mode left switched on in real software often leaks extra information to attackers, which is why it is usually `false`.

- **Hint 1:** `nextBoolean()` reads `true` or `false` (any capitals).

- **Hint 2:** milliseconds = `(int) (timeout * 1000)`.

### Task 18 — Preview: decisions (official supplementary)

**Class:** `IfElseDemo`, then extend `VehicleFuel` · **Goal:** get a head start on Lecture 6.

1.  Type and debug the `IfElseDemo` program from the official Java tutorial [The if-then and if-then-else Statements](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/if.html). Step through it with F6 and watch which lines are skipped. With `testscore = 76`, which grade is printed?

2.  Change `testscore` to 95, 85, 65 and 40, predicting each grade first.

3.  Add to your vehicle program: if the mpg is **more than 50**, print a message congratulating the user on a fuel-efficient car; if it is **less than 35**, chastise them for choosing a gas guzzler.

4.  Edit `vehicle.txt` to test mpg values of 55.0, 30.1, 46.5, and exactly 35.0 and 50.0. Which values give no message? Why?

- **Hint 1:** `if (mpg > 50) { ... } else if (mpg < 35) { ... }`

- **Hint 2:** `>` means strictly greater, so 50.0 is **not** more than 50.

### Task 19 — Mini-project: module results from a file

**Class:** `Task19ModuleReport` · **Goal:** combine file input, constants, calculation and file output.

Reuse the Lab 4 weighted mark idea (Simple Application 30%, Complex Application 50%, In-Class Test 20%), but now with files.

`marks.txt` schema: student name (line 1); the three marks out of 100, separated by spaces (line 2).

``` text
Sam Archer
65 58 72
```

The program must write `module_report.txt` containing: a title line, the name, each assessment’s name, mark and weighted contribution in aligned columns, and the overall mark to 1 dp (`62.9` for this data). Use constants for the weights, comment each section, and close both files.

Test with at least two data files, with expected results worked out by hand first. This is a practice calculator, not LJMU’s official mark-combining rules.

- **Hint 1:** read with `nextLine()` first, then three `nextDouble()` calls.

- **Hint 2:** columns: `%-22s %6.1f %8.1f%n`.

### Task 20 — Assessment-style practice: network traffic report

**Class:** `Task20Traffic` · **Time limit:** 30 minutes, no hints.

Practice only: not an official LJMU assessment, and the checklist is not the official marking scheme.

**Specification:** a router logs its traffic to `traffic.txt`. Schema: device name (line 1, may contain spaces); bytes sent, bytes received and duration in seconds, separated by spaces (line 2).

``` text
Office Router 2
734003200 52428800 3600
```

Write `traffic_report.txt`:

``` text
TRAFFIC REPORT: Office Router 2
Sent:          700.0 MB
Received:       50.0 MB
Total:         750.0 MB
Duration: 1 h 0 min
Average:       1.748 Mbps
```

**Rules:** 1 MB = 1,048,576 bytes; 1 megabit = 1,000,000 bits; 8 bits per byte. All must be constants. Average Mbps = total bytes × 8 ÷ 1,000,000 ÷ seconds.

**Trap to avoid:** calculating `(sent + received) * 8` with `int` overflows (Lab 2, Task 18) and gives a wrong number with no error. Make sure the calculation uses `double` (or `long`).

**Self-check (practice only)**

- Correct imports, throws clause, both files closed

- Device name with spaces read correctly

- All conversion factors are named constants

- No integer overflow; result matches 1.748 Mbps

- Output file matches the layout exactly (check spaces)

- A second data file tested with hand-worked expected values

- Header comment and section comments

Send me your code when done and I will review it against the checklist.

## Progress tracker and reflection

Tick a task when it works with every test file **and** you could explain every line.

- Task 1 — First output file (official Task 1)

- Task 2 — print/println/printf to a file

- Task 3 — Forgetting close()

- Task 4 — Overwriting and multiple files

- Task 5 — Where do files go?

- Task 6 — Pay program

- Task 7 — Design from a schema

- Task 8 — Same data, different layouts

- Task 9 — Vehicle fuel data (official Task 2)

- Task 10 — Bug hunt (8 errors)

- Task 11 — Cost and range (official Task 3)

- Task 12 — Results file (official Task 4)

- Task 13 — Grade Calculator

- Task 14 — Round trip

- Task 15 — Security log summary

- Task 16 — Payslip

- Task 17 — Config file

- Task 18 — if-else preview (official supplementary)

- Task 19 — Module report from a file

- Task 20 — Network traffic report

**Reflection (send me your answers)**

1.  What changes, and what stays the same, when you switch from console I/O to file I/O?

2.  What is a checked exception, and why does `main` need `throws FileNotFoundException`?

3.  Why must you close an output file? What did Task 3 show you?

4.  What is a schema, and why must the writer and reader agree on it (Task 14)?

5.  Where does Eclipse look for `prog.txt`, and how did Task 5 prove it?

6.  Which task did you need hints for?

## Answer key

Use only after a real attempt. Programs and outputs were compiled and run with Java 21 (`javac`) on Linux, with the data files given, not inside Eclipse. Eclipse steps (auto-complete, Organise Imports, Refresh, debugger) and Windows paths were not tested.

**Task 1.** Ctrl+Space adds `import java.io.FileNotFoundException;`; Ctrl+Shift+O adds `import java.io.PrintWriter;`. `test1.txt` contains `Hello file! Welcome to LJMU`.

**Task 2.** File version (the console version is identical with `System.out`):

``` java
double progress = 25.0;
PrintWriter file = new PrintWriter("profile.txt");
file.println("STUDENT PROFILE");
file.print("Name: ");
file.println("Sam Archer");
file.printf("Module: %s%n", "4300COMP");
file.printf("Week %d topic: %s%n", 5, "File I/O");
file.printf("Progress: %.1f%%%n", progress);
file.close();
```

**Task 3.** Without `close()`: the file exists but is **empty** (0 bytes). With `flush()`: the line appears. With `close()`: the line appears and the file is released. The buffer holds output in memory; `flush()` writes it to disk; `close()` flushes and releases the file.

**Task 4.** After the second run, `runs.txt` contains only `Run number 2`: PrintWriter empties an existing file when it opens it.

**Task 5.** `user.dir` is the project root folder. A file inside `src` gives `FileNotFoundException`; moved to the root it works.

**Task 6.** Output `Pay for David: £841.75`. `Pittance!` → `InputMismatchException` on the `nextDouble()` read. Without the throws clause: `unreported exception FileNotFoundException; must be caught or declared to be thrown`.

**Task 7.**

``` java
Scanner in = new Scanner(new FileReader("laptop.txt"));
String model = in.nextLine();
int ramGb = in.nextInt();
int storageGb = in.nextInt();
double price = in.nextDouble();
boolean inStock = in.nextBoolean();
in.close();
System.out.printf("%s: %d GB RAM, %d GB storage, £%.2f, in stock: %b%n",
        model, ramGb, storageGb, price, inStock);
```

**Task 8.** Files A, B and C all give `Pay for David: 841.75`: `next...` methods skip any whitespace. `staff.txt` with `nextInt()` then `nextLine()`: the name is `""`, then `nextDouble()` meets `Sam` → `InputMismatchException`. Fix: add `in.nextLine();` after `nextInt()`.

**Task 9.**

``` java
Scanner in = new Scanner(new FileReader("vehicle.txt"));
String model = in.nextLine();
double mpg = in.nextDouble();
int capacity = in.nextInt();
double pencePerLitre = in.nextDouble();
in.close();
System.out.printf("Vehicle %s holds %d litres of fuel at a cost of %.1f p/litre.%n",
        model, capacity, pencePerLitre);
System.out.printf("On average, it returns %.1f mpg.%n", mpg);
```

**Task 10.** 1, 2 and 4: compile errors. 3, 5, 6: runtime errors. 7 and 8: logic errors (8 then causes a runtime error on the next read).

**Task 11.**

``` java
final double LITRES_PER_GALLON = 4.54609;
double costPounds = capacity * pencePerLitre / 100;
double gallons = capacity / LITRES_PER_GALLON;
double range = mpg * gallons;
System.out.printf("It will cost £%.2f to fuel the vehicle at the specified rates.%n", costPounds);
System.out.printf("On average, this will give the vehicle a range of %.1f miles.%n", range);
```

Verified results:

| Vehicle (file line 2)               | Cost to fill | Range       |
|-------------------------------------|--------------|-------------|
| Nissan Juke (46.5 50 129.9)         | £64.95       | 511.4 miles |
| Ford Fiesta ST (38.2 42 141.9)      | £59.60       | 352.9 miles |
| Toyota Yaris Hybrid (68.9 36 135.5) | £48.78       | 545.6 miles |

**Task 12.**

``` java
PrintWriter out = new PrintWriter("output.txt");
out.println(model);
out.printf("%.1f %d %.1f%n", mpg, capacity, pencePerLitre);
out.printf("%.1f %.2f%n", range, costPounds);
out.close();
```

`output.txt` for the Juke (verified):

``` text
Nissan Juke
46.5 50 129.9
511.4 64.95
```

**Task 13.** `John 45 60 75 66 43` → `57.80`; `John 39 45 60 75 66` → `57.00`. Five separate lines still work. Full code: Lecture 5 notes, Program B.

**Task 14.** Prints `Sam Archer|1|120.0|true`. If the writer puts the name on the same line as the numbers, the reader’s `nextLine()` swallows the whole line and the next read fails: writer and reader must follow the same schema.

**Task 15.**

``` java
Scanner in = new Scanner(new FileReader("access.txt"));
String server = in.nextLine();
String user = in.next();
int ok = in.nextInt();
int failed = in.nextInt();
in.close();

int total = ok + failed;
double failPct = failed * 100.0 / total;

PrintWriter out = new PrintWriter("security_report.txt");
out.printf("Security report for %s%n", server);
out.printf("User: %s%n", user);
out.printf("Logins: %d total, %d failed (%.2f%%)%n", total, failed, failPct);
out.close();
```

`bob 12 48` → 60 total, 48 failed (80.00%).

**Task 16.** Key lines (output verified to match the task exactly):

``` java
double basic = rate * standardHours;
double overtime = overtimeHours * rate * OVERTIME_MULTIPLIER;
double gross = basic + overtime;
out.printf("%-12s%2d h @ £%.2f = £%8.2f%n", "Basic:", standardHours, rate, basic);
out.printf("%-12s%2d h @ £%.2f = £%8.2f%n", "Overtime:", overtimeHours, rate * OVERTIME_MULTIPLIER, overtime);
out.printf("%-12s%16s£%8.2f%n", "Gross pay:", "", gross);
```

**Task 17.** `debug` = `yes` → `InputMismatchException`: only `true`/`false` are accepted by `nextBoolean()`. A real tool would crash on start-up from one typo in its config file.

**Task 18.** `testscore = 76` → `Grade = C`; 95 → A, 85 → B, 65 → D, 40 → F. Vehicle messages (verified): 55.0 congratulate; 30.1 gas guzzler; 46.5, 35.0 and 50.0 no message, because 35.0 is not less than 35 and 50.0 is not more than 50.

**Task 19.** 65/58/72 → `62.9`.

**Task 20.** One model answer:

``` java
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.PrintWriter;
import java.util.Scanner;

/*
 * Task 20 model answer: network traffic report from a router log file.
 */
public class Task20Traffic {
    public static void main(String[] args) throws FileNotFoundException {
        // Constants
        final double BYTES_PER_MB = 1024 * 1024;
        final int BITS_PER_BYTE = 8;
        final double BITS_PER_MEGABIT = 1000000;
        final int SECONDS_PER_MINUTE = 60;
        final int SECONDS_PER_HOUR = 3600;

        // Read the log
        Scanner in = new Scanner(new FileReader("traffic.txt"));
        String device = in.nextLine();
        int sent = in.nextInt();
        int received = in.nextInt();
        int seconds = in.nextInt();
        in.close();

        // Calculate (double avoids int overflow)
        double sentMb = sent / BYTES_PER_MB;
        double receivedMb = received / BYTES_PER_MB;
        double totalBytes = (double) sent + received;
        double mbps = totalBytes * BITS_PER_BYTE / BITS_PER_MEGABIT / seconds;
        int hours = seconds / SECONDS_PER_HOUR;
        int minutes = (seconds % SECONDS_PER_HOUR) / SECONDS_PER_MINUTE;

        // Write the report
        PrintWriter out = new PrintWriter("traffic_report.txt");
        out.printf("TRAFFIC REPORT: %s%n", device);
        out.printf("%-10s%10.1f MB%n", "Sent:", sentMb);
        out.printf("%-10s%10.1f MB%n", "Received:", receivedMb);
        out.printf("%-10s%10.1f MB%n", "Total:", sentMb + receivedMb);
        out.printf("%-10s%d h %d min%n", "Duration:", hours, minutes);
        out.printf("%-10s%10.3f Mbps%n", "Average:", mbps);
        out.close();
    }
}
```

Verified: the report matches the task exactly. With `int` arithmetic, `(sent + received) * 8` gave `1996488704` instead of 6,291,456,000 — a silent overflow.
