# Lab 1 — Hands-on Practical Workbook (20 Tasks)

**Module:** 4300COMP Introduction to Programming · **Language:** Java

## How to use this lab

This lab has **20 hands-on tasks**. Every task means opening Eclipse, typing code yourself and running it. It covers Lecture 1 and Tutorial 1: what a program is, the structure of a Java class, `main`, `System.out.println` and `print`, comments, layout, and the three kinds of error.

**Learning outcomes:** MLO2 (using an IDE) in every task; MLO1 (programming constructs) from Task 6; MLO3 (solving a specification) in Tasks 16–20.

**Rules that make this lab work**

1. Type every line yourself. Do not copy and paste. Typing is how your fingers learn the syntax.
2. Predict before you run. Write your prediction down, then run and compare.
3. Read the hints only in order: Hint 1, then Hint 2, then the answer key. Stop as soon as you are unstuck.
4. Make one new class per task, named as the task says (for example `Task01Hello`).
5. Tick the progress tracker at the end as you go.

**How the 20 tasks get harder**

| Tasks | Level | What you do | Rough time |
| --- | --- | --- | --- |
| 1–5 | Getting started | Type, run and change small programs | 5–10 min each |
| 6–10 | Predict and fix | Predict output, repair broken code | 5–10 min each |
| 11–15 | Write from a spec | Build a program from a short description | 10–15 min each |
| 16–20 | Integrate and assess | Larger programs, mini-project, assessment-style task | 15–30 min each |

**What you need:** Eclipse with a JDK installed (use the version your LJMU lab machines have), and about 4 hours spread over a few sessions.

**Important:** the assessment-style task (Task 20) is practice only. It is not an official LJMU task and its marking guide is not the official marking criteria.

## Setup: one project for the whole lab

You will make **one Eclipse project called `lab1`** and add a new class for each task. This follows the steps in official Tutorial 1.

1. Open **Eclipse IDE for Java Developers**. On a university PC, set the workspace to a folder on your M drive (Tutorial 1 suggests `M:\Eclipse-2026-06`).
2. If Eclipse is not in the **Java perspective**, click **Open Perspective** (top right) and choose **Java**.
3. **File > New > Java Project**. Name: `lab1`. **Untick** “Create module-info.java”. Click **Finish**.
4. Right-click the `src` folder inside `lab1` > **New > Class**.
5. Package: `lab1`. Name: the class name the task gives (for example `Task01Hello`). Tick **public static void main(String\[\] args)**. Click **Finish**.
6. Type your code inside `main`, between its `{` and `}`.
7. Run with the **green circle with a white arrow** (or **Ctrl+F11**). Output appears in the **Console** panel at the bottom.

Every class in this lab starts like this. Eclipse writes it for you in step 5:

```java
package lab1;

public class Task01Hello {

    public static void main(String[] args) {
        // your code goes here
    }

}
```

**Rules to remember from Lecture 1**

- The class name and the file name must match exactly: `Task01Hello` lives in `Task01Hello.java`.
- Java is **case-sensitive**: `System` works, `system` does not.
- Every statement ends with a **semicolon** `;`.
- Every `{` needs a matching `}`.
- The program starts at the first line inside `main` and runs **one statement at a time, top to bottom**.

**If something goes wrong**

| Problem | Likely cause | Fix |
| --- | --- | --- |
| Run button does nothing or asks what to run | You clicked a file with no `main` | Click inside the class that has `main`, then run |
| Red underline under a word | Syntax error on that line | Hover over it to read the message; press **Ctrl+1** for Quick Fix suggestions |
| “Save resources?” pop-up | You edited without saving | Click **OK**; it saves and runs |
| Console panel missing | Panel was closed | **Window > Show View > Console** |
| Everything looks different | Wrong perspective | Switch back to the **Java** perspective (step 2) |

## Tasks 1–5: Getting started

These five tasks get your hands used to Eclipse and to the one statement you know so far: `System.out.println`.

### Task 1 — Hello World (official Tutorial 1, Task 1)

**Class:** `Task01Hello` · **Goal:** create, run and change your first program.

1. Make the class as in Setup.
2. Inside `main`, type: `System.out.println("Hello World!");`
3. Run it. Check the Console shows `Hello World!`
4. Change the message to `Hello LJMU!` and run again.
5. Delete the semicolon, look at the red underline, hover over it and read the message. Put the semicolon back.

**Expected output (after step 4):**

```text
Hello LJMU!
```

- **Hint 1:** the statement goes *inside* the curly braces of `main`, not outside.
- **Hint 2:** check capitals: `System` has a capital S; `out` and `println` are lower case.

### Task 2 — Your details (official Tutorial 1, Task 2)

**Class:** `Task02Details` · **Goal:** use several `println` statements in order.

Print your name, your street, your city and a postcode, each on its own line. Then add a fifth line: `Course: BSc Cyber Security`.

**Expected output shape** (your own words will differ — a made-up address is fine):

```text
Name: Sam Example
Street: 1 Example Road
City: Liverpool
Postcode: L1 1AA
Course: BSc Cyber Security
```

- **Hint 1:** one `System.out.println(...)` per line of output.
- **Hint 2:** the text you want printed goes between the double quotes `" "`.

### Task 3 — print versus println

**Class:** `Task03PrintVsPrintln` · **Goal:** see exactly what the `ln` does.

Type this program. **Before running, write down what you think the Console will show.**

```java
System.out.print("A");
System.out.print("B");
System.out.println("C");
System.out.println("D");
System.out.print("E");
System.out.println();
System.out.println("F");
```

Then answer: (a) What does `print` do after printing its text? (b) What does `println` do? (c) What does an empty `System.out.println();` do?

- **Hint 1:** `ln` stands for “line”. `println` prints the text, then moves to a new line.
- **Hint 2:** `print` leaves the cursor at the end of the text, so the next output carries on on the same line.

### Task 4 — Comments

**Class:** `Task04Comments` · **Goal:** write both kinds of comment and use them to switch code off.

1. At the top of the class (above `public class`), write a **multi-line comment** `/* ... */` with your name, the date and one sentence on what the program does.
2. Write three `println` statements: `Line 1`, `Line 2`, `Line 3`.
3. Above each one, add a **single-line comment** `//` saying what it prints.
4. Put `//` in front of the `Line 2` statement. Run. What changed?
5. Click on the `Line 2` statement and press **Ctrl+/**. What does Eclipse do? Press it again.

**Expected output after step 4:**

```text
Line 1
Line 3
```

- **Hint 1:** the compiler ignores everything after `//` on that line, and everything between `/*` and `*/`.
- **Hint 2:** “commenting out” a line is a quick way to test a program without deleting code.

### Task 5 — Special characters inside text

**Class:** `Task05Escapes` · **Goal:** print tabs, new lines, quotes and backslashes.

Some characters cannot be typed directly inside `" "`. Java uses an **escape sequence**: a backslash `\` followed by a letter or symbol.

| Escape | Meaning |
| --- | --- |
| `\n` | new line |
| `\t` | tab (jumps to the next column) |
| `\"` | a double quote character |
| `\\` | a single backslash |

Write **one statement for each** line of this output:

```text
Line one
Line two
Name    Module
Sam     4300COMP
She said "Java is fun"
File path: C:\Users\student
```

Exception: the first two lines must come from **one single** `println`. The gaps on lines 3–4 must be tabs.

- **Hint 1:** `"Line one\nLine two"` prints two lines.
- **Hint 2:** to print `"`, write `\"`. To print `\`, write `\\`. A single `\` on its own makes Java expect an escape and causes an error.

You will need `\t` in Tutorial 2, Task 4 (the squares and cubes table).

## Tasks 6–10: Predict the output and fix the bugs

In these tasks you think first and run second. **Write your prediction on paper before you run anything.** This is exactly the skill the in-class multiple-choice test checks.

The error messages below come from the standard `javac` compiler. Eclipse uses its own compiler, so its wording is different (for example “Syntax error, insert ";" to complete BlockStatements”), but it points at the same problem.

### Task 6 — Predict the output

**Class:** `Task06Predict` · **Goal:** trace a program line by line.

Write down the exact output, including blank lines. Then type it in and run it.

```java
// Part A
System.out.println("Start");
System.out.print("One ");
System.out.print("Two ");
System.out.println("Three");
// System.out.println("Hidden");
System.out.println("End");

// Part B
System.out.print("X\n");
System.out.println("Y\tZ");
System.out.println("");
System.out.println("Done");
```

Questions: (a) How many lines does Part A print? (b) Why is `Hidden` not printed? (c) What does `print("X\n")` behave like?

- **Hint 1:** treat each statement in order and keep track of whether the cursor is at the start of a new line.
- **Hint 2:** `println("")` prints nothing and then moves to a new line, so it makes a blank line.

### Task 7 — Predict joined text (the + sign)

**Class:** `Task07Concat` · **Goal:** see that `+` can add numbers *or* join text.

Predict each line, then run.

```java
System.out.println(2 + 3);
System.out.println("2 + 3");
System.out.println("2 + 3 = " + 2 + 3);
System.out.println("2 + 3 = " + (2 + 3));
System.out.println(2 + 3 + " is the answer");
System.out.println("Result: " + 10 * 2);
System.out.println("Java" + " " + "rocks");
```

The rule: Java works **left to right**. While both sides are numbers, `+` adds. As soon as one side is text (a **String**), `+` joins. Brackets `( )` are worked out first. `*` is done before `+`.

- **Hint 1:** line 3 starts with text, so `"2 + 3 = " + 2` becomes the text `"2 + 3 = 2"`, and then `3` is joined on.
- **Hint 2:** line 5 starts with two numbers, so `2 + 3` is added first.

Lecture 2 covers this in detail (“Strings and the Operator +”).

### Task 8 — Fix the syntax errors

**Goal:** read a compiler message and repair the code. For each program below: make the class in Eclipse, type it **with the mistake**, read Eclipse’s message, write down the cause, then fix it.

**8a** — class `Fix1`

```java
System.out.println("Hello")
System.out.println("World");
```

```text
Fix1.java:6: error: ';' expected
```

**8b** — class `Fix2`

```java
system.out.println("Access granted");
```

```text
Fix2.java:6: error: package system does not exist
```

**8c** — class `Fix3`

```java
System.out.println("Missing quote);
```

```text
Fix3.java:6: error: unclosed string literal
```

**8d** — class `Fix4` (the whole class this time)

```java
package lab1;

public class Fix4 {

    public static void main(String[] args) {
        System.out.println("Brace trouble");

}
```

```text
Fix4.java:8: error: reached end of file while parsing
```

**8e** — class `Fix5`

```java
System.out.printn("Typo in the method name");
```

```text
Fix5.java:6: error: cannot find symbol
  symbol:   method printn(String)
```

- **Hint 1:** the line number in the message tells you where the compiler *noticed* the problem. The real mistake is on that line or just before it.
- **Hint 2:** “end of file while parsing” means the compiler ran out of code while still waiting for a `}`.

### Task 9 — Structure, runtime and logic errors

**Goal:** meet the other two kinds of error from Lecture 1 — errors that appear when you **run**, and programs that run but do the **wrong thing**.

**9a — name mismatch.** Create a class called `Wrong`. Change its header line to `public class Fix6 {` and save. Read the error, then explain why the class name and file name must match.

```text
Wrong.java:3: error: class Fix6 is public, should be declared in a file named Fix6.java
```

**9b — capital M.** In a class `Fix7`, change `main` to `Main`. It compiles without any red underline. Run it. What happens?

```text
Error: Main method not found in class lab1.Fix7, please define the main method as:
   public static void main(String[] args)
```

**9c — single quotes.** In a class `Fix8`, type `System.out.println('Hello');` Why does Java complain? (Lecture 2 explains: single quotes hold exactly **one** character, a `char`; text uses double quotes.)

**9d — logic error.** This program runs with no errors, but the steps are in the wrong order. Fix it so the steps print 1, 2, 3.

```java
System.out.println("Step 3: Log out");
System.out.println("Step 1: Enter username");
System.out.println("Step 2: Enter password");
```

For each of 9a–9d, write one line: **syntax error, runtime error or logic error?** and why.

- **Hint 1:** if the program never starts, it is a compile (syntax) problem. If it starts but stops with a message, it is a runtime error. If it finishes but the output is wrong, it is a logic error.
- **Hint 2:** 9b is unusual: the code is valid Java, but the JVM cannot find a method called exactly `main` to start from.

### Task 10 — Break it on purpose: your error diary

**Class:** `Task10Diary` · **Goal:** learn what each error looks like *before* you make it by accident.

Start from a working Hello World. Make **one** change at a time from the list, write down Eclipse’s exact message, then undo it.

| # | Change to make | Eclipse message (you fill in) | Kind of error |
| --- | --- | --- | --- |
| 1 | Remove the closing `)` |  |  |
| 2 | Write `println` as `Println` |  |  |
| 3 | Remove `static` from the `main` line, then run |  |  |
| 4 | Remove `void` from the `main` line |  |  |
| 5 | Remove the last `}` of the class |  |  |
| 6 | Put a statement *outside* `main` (between the two closing braces) |  |  |
| 7 | Write `string[] args` with a small s |  |  |
| 8 | Delete the line `package lab1;` |  |  |

Copy this table into your notebook and fill it in.

- **Hint 1:** some changes give an error only when you run (look at the Console), not while typing.
- **Hint 2:** change 8 is a trap: think about which folder the file is in.

## Tasks 11–15: Write programs from a specification

Now you get a description of what the program must print, not the code. Plan on paper first: **how many lines of output, and what goes on each line?** Then write one `println` per line.

### Task 11 — ShapePrinter (official Tutorial 1, Task 3)

**Project:** `shape` · **Package:** `shape` · **Class:** `ShapePrinter`

This one uses a **new project**, exactly as Tutorial 1 asks, so you practise the whole set-up again. Print these three shapes with one blank line between each.

```text
*******
*     *
*     *
*******

   ***
 *     *
*       *
*       *
 *     *
   ***

  *
 ***
*****
  *
  *
  *
```

- **Hint 1:** count the spaces carefully: the second box line is `*`, five spaces, `*`.
- **Hint 2:** `System.out.println();` with nothing inside the brackets gives the blank line between shapes.

### Task 12 — Your initials in big letters

**Class:** `Task12Initials` · **Goal:** plan a picture row by row.

Print your initials, 5 rows tall, built from `*`. For example, for someone with initials A and A, that is two letter A shapes side by side with a gap of three spaces.

1. Draw the letters on squared paper first, one `*` per square.
2. Write one `println` per row.
3. Run, compare with your drawing, adjust the spaces.

**Extra:** add a third letter (for example a `J` for Java) on the right.

- **Hint 1:** both letters must be on the **same** row of output, so each `println` holds part of every letter.
- **Hint 2:** keep every row the same width by padding with spaces; it makes the letters line up.

### Task 13 — Security incident log with tabs

**Class:** `Task13IncidentLog` · **Goal:** line up columns with `\t`.

Print this table. The gaps must be made with `\t`, not lots of spaces.

```text
Time    Event                   Level
09:02   Login success           Low
09:15   Password failed         Medium
09:16   Account locked          High
10:40   File deleted            Medium
```

- **Hint 1:** a tab jumps to the next column stop (every 8 characters in most consoles). Long words need one `\t`; short words may need two or three.
- **Hint 2:** if the columns do not line up in Eclipse, add or remove one `\t` on that line and run again.

This is the same skill as Tutorial 2, Task 4 (the squares and cubes table).

### Task 14 — Let Java do the maths

**Class:** `Task14Calc` · **Goal:** print a sum where Java calculates the answer (official Tutorial 1, supplementary task).

Print these five lines. The number after `=` must be **calculated by Java**, not typed by you.

```text
2 + 3 = 5
10 - 4 = 6
6 * 7 = 42
20 / 4 = 5
Seconds in a day = 86400
```

**Test of your answer:** change `6 * 7` to `6 * 8` in the calculation. If the output changes to 48, Java is doing the maths. If it still says 42, you typed the answer yourself.

- **Hint 1:** the text part goes in quotes; the calculation does not.
- **Hint 2:** remember Task 7: put the calculation in brackets, `"2 + 3 = " + (2 + 3)`, or Java will join `2` and `3` as text.

### Task 15 — Login warning banner

**Class:** `Task15Banner` · **Goal:** produce exact, neat output (a real-world security notice).

Many systems show a warning before login. Print this banner exactly. Every line must be **30 characters wide** so the right-hand `#` signs line up.

```text
##############################
#                            #
#   AUTHORISED USERS ONLY    #
#   All activity is logged   #
#                            #
##############################
```

- **Hint 1:** count characters in the top line (30 `#`). Each middle line is `#`, 28 characters, `#`.
- **Hint 2:** write the top line first, run it, then copy the width for the other lines and fill in spaces.

## Tasks 16–20: Integration, mini-project and assessment-style task

These tasks combine everything from Lecture 1: class structure, `main`, `print`/`println`, escape sequences, `+` with brackets, comments, layout and Eclipse tools.

### Task 16 — Unscramble the program

**Class:** `Task16Unscramble` · **Goal:** understand the structure of a Java class well enough to rebuild it.

The 11 lines below make one working program, but they are shuffled. Put them in the right order in Eclipse and run it. Indent correctly.

```text
System.out.println("2. Check for updates");
}
public class Task16Unscramble {
System.out.println("Security checklist");
package lab1;
System.out.println("3. Back up your files");
public static void main(String[] args) {
// Morning security checklist
}
System.out.println("------------------");
System.out.println("1. Lock your screen");
```

**Expected output:**

```text
Security checklist
------------------
1. Lock your screen
2. Check for updates
3. Back up your files
```

Then answer: which closing brace closes `main`, and which closes the class?

- **Hint 1:** the order of the outside is always: `package` line, class header, `main` header, statements, `}` for `main`, `}` for the class.
- **Hint 2:** the comment describes the whole checklist, so it goes just before the first `println`.

### Task 17 — Eclipse power tools (MLO2)

**Class:** `Task17Shortcuts` · **Goal:** work faster and let the IDE help you.

Do each step, then tick it in the tracker.

1. **Line numbers:** right-click the grey margin left of the code > **Show Line Numbers**.
2. **Code template:** inside `main`, type `syso` then press **Ctrl+Space**. Eclipse writes `System.out.println();` for you. Fill in `"Shortcut 1"`.
3. Use `syso` + Ctrl+Space to make four more lines: `Shortcut 2` to `Shortcut 5`.
4. **Messy then tidy:** delete all the indentation so every line starts at the left edge. Press **Ctrl+Shift+F** (Format). What happens?
5. **Toggle comment:** select lines 2–4 of your statements and press **Ctrl+/**. Run. Press it again.
6. **Quick Fix:** change `System` to `system`. Click on the red underline and press **Ctrl+1**. Read the suggestions and pick the right one.
7. **Save and run:** **Ctrl+S** saves the file. **Ctrl+F11** runs the program.
8. **Rename:** in the Package Explorer, right-click `Task17Shortcuts.java` > **Refactor > Rename** to `Task17Tools`. Open the file: did the class name change too?

Write one sentence: why does Eclipse change the class name when you rename the file?

- **Hint 1:** `syso` only works when the cursor is inside a method such as `main`.
- **Hint 2:** on some laptops Ctrl+Space switches keyboard language. If that happens, use **Edit > Content Assist** from the menu instead.

### Task 18 — Tidy up someone else’s code

**Class:** `Task18Messy` · **Goal:** make working code readable, without changing what it prints.

This program compiles and runs, but it is very hard to read. Type it exactly as shown, run it and note the output.

```java
package lab1;
public class Task18Messy{
public static void main(String[] args){System.out.println("Password rules:");System.out.println("1. At least 12 characters");
System.out.print("2. Mix of ");System.out.println("letters and numbers");
        System.out.println("3. Never reuse a password");}}
```

Now tidy it by hand (not with Ctrl+Shift+F):

1. One statement per line.
2. Correct indentation: 4 spaces inside the class, 8 inside `main`.
3. Each closing `}` on its own line, lined up with the line that opened it.
4. Add a `/* */` comment at the top saying what the program does.
5. Run again. The output must be **identical** to before.

Why does this matter? Java ignores layout, but people (your lecturer, your marker, you in three weeks) do not.

- **Hint 1:** each `;` marks the end of a statement, so a new line can start after each one.
- **Hint 2:** the `print` and `println` on line 4 make **one** line of output together. Keep them in that order.

### Task 19 — Mini-project: profile card

**Class:** `Task19ProfileCard` · **Goal:** plan and build a complete small program from a spec.

**Specification**

1. A border of `=` signs at the top and bottom, at least 30 characters wide.
2. A title line: `STUDENT PROFILE`.
3. Four labelled lines using `\t` to line up the values: Name, Course, University, Module.
4. A blank line, then a heading `Skills I am learning:` followed by three bullet lines that start with ` -  `.
5. One line that uses a **calculation done by Java**, for example `Weeks in a year: 52` worked out as `(365 / 7)`.
6. At least one line built from a `print` followed by a `println`.
7. A `/* */` comment at the top, and a `//` comment above each section.

**Plan first:** sketch the full output on paper, then number each line. That number is how many output lines your program needs.

- **Hint 1:** build it section by section. Run after each section is done.
- **Hint 2:** `365 / 7` gives `52` in Java, not `52.14`, because both numbers are whole numbers. Lecture 2 explains why.

### Task 20 — Assessment-style practice: Cyber Toolkit start screen

**Class:** `Task20Toolkit` · **Goal:** meet a full specification under time pressure. Give yourself **30 minutes**, no hints until the time is up.

This is a practice task in the style of a simple application brief. It is **not** an official LJMU assessment and the checklist is **not** the official marking scheme.

**Specification:** the program prints a start screen for a made-up security tool. It must show:

1. A banner: a line of 40 `=`, the title `CYBER TOOLKIT v1.0` roughly centred, another line of 40 `=`.
2. A blank line.
3. A heading `Main menu` and four numbered options using `\t` after the number: Check password strength, View login history, Scan a file, Exit.
4. A blank line.
5. A heading `Status report` with two lines whose numbers Java calculates: failed logins today = 3 + 4 + 2, and scans this week = 5 per day × 7 days.
6. A final prompt ` Choose an option (1-4):  ` printed with `print`, followed on the **same line** by `[input comes in a later lab]`.
7. A header comment with a short description of the program, and a comment above each section.

**Self-check (practice only)**

- [ ] Compiles and runs with no errors
- [ ] Output matches the spec line by line
- [ ] Numbers are calculated by Java (test by changing one value)
- [ ] `print` used correctly for the final prompt
- [ ] Tabs used in the menu
- [ ] Header comment and section comments present
- [ ] Consistent indentation and one statement per line

When you are done, review your own code against this checklist, then compare it with the model answer in the answer key.

## Progress tracker and reflection

Tick each task when it runs and you can explain it without looking at the hints.

- [ ] Task 1 — Hello World
- [ ] Task 2 — Your details
- [ ] Task 3 — print versus println
- [ ] Task 4 — Comments
- [ ] Task 5 — Special characters
- [ ] Task 6 — Predict the output
- [ ] Task 7 — Predict joined text
- [ ] Task 8 — Fix the syntax errors (8a–8e)
- [ ] Task 9 — Structure, runtime and logic errors (9a–9d)
- [ ] Task 10 — Error diary
- [ ] Task 11 — ShapePrinter
- [ ] Task 12 — Initials
- [ ] Task 13 — Incident log
- [ ] Task 14 — Let Java do the maths
- [ ] Task 15 — Login banner
- [ ] Task 16 — Unscramble
- [ ] Task 17 — Eclipse power tools
- [ ] Task 18 — Tidy up
- [ ] Task 19 — Profile card
- [ ] Task 20 — Cyber Toolkit start screen

**Reflection (answer in a sentence or two each)**

1. In your own words, what happens between pressing Run and seeing output? Use the words *source code*, *compiler*, *bytecode* and *JVM*.
2. Which error from Tasks 8–10 surprised you most, and why?
3. What is the difference between `print` and `println`?
4. Why does `"2 + 3 = " + 2 + 3` print `2 + 3 = 23`?
5. Which task did you need the hints for? That tells you what to practise next.

## Answer key

Use this only after a real attempt. Every program and output below was compiled and run with Java 21 (`javac`), not inside Eclipse; Task 10’s Eclipse messages and Task 17’s steps were not tested.

**Tasks 1–2.** One `System.out.println("...");` per line, inside `main`.

**Task 3.** Output:

```text
ABC
D
E
F
```

(a) `print` stays on the same line. (b) `println` prints, then moves to a new line. (c) An empty `println()` just ends the current line (here it ends the line after `E`).

**Task 4.** Line 2 disappears from the output because the compiler ignores a commented-out line. Ctrl+/ adds or removes `//` at the start of the selected lines.

**Task 5.**

```java
System.out.println("Line one\nLine two");
System.out.println("Name\tModule");
System.out.println("Sam\t4300COMP");
System.out.println("She said \"Java is fun\"");
System.out.println("File path: C:\\Users\\student");
```

**Task 6.** Output:

```text
Start
One Two Three
End
X
Y       Z

Done
```

(a) 3 lines. (b) It is commented out. (c) `print("X\n")` behaves like `println("X")`.

**Task 7.** Output:

```text
5
2 + 3
2 + 3 = 23
2 + 3 = 5
5 is the answer
Result: 20
Java rocks
```

**Task 8.**

| Part | Cause | Fix |
| --- | --- | --- |
| 8a | Missing `;` after `println("Hello")` | Add `;` |
| 8b | `system` must be `System` (case-sensitive) | Capital S |
| 8c | Text has no closing `"` | `"Missing quote"` |
| 8d | `main` is never closed, so the class’s `}` closes `main` and the class has none | Add `}` |
| 8e | Method name typed as `printn` | `println` |

**Task 9.** 9a: syntax (compile) error — a public class must be in a file of the same name; rename the class back to `Wrong`. 9b: compiles, but fails when run: the JVM looks for a method called exactly `main`; treat this as a runtime (start-up) error. 9c: syntax error — single quotes hold one `char`; use `"Hello"`. 9d: logic error — runs fine but in the wrong order; move `Step 3` to the end.

**Task 10 (expected kinds).** 1: syntax. 2: syntax (`Println` not found). 3: compiles, then Run fails because `main` must be `static` (runtime/start-up). 4: syntax (a method needs a return type). 5: syntax (end of file while parsing). 6: syntax (a statement cannot sit directly inside a class). 7: syntax (`string` not found; the type is `String`). 8: Eclipse error — the file is in folder `lab1`, so it must declare `package lab1;`.

**Task 11.** One `println` per row, `System.out.println();` between shapes. Output matches the spec exactly.

**Task 12.** Model for “AA”:

```java
System.out.println("  *       *  ");
System.out.println(" * *     * * ");
System.out.println("*****   *****");
System.out.println("*   *   *   *");
System.out.println("*   *   *   *");
```

**Task 13.**

```java
System.out.println("Time\tEvent\t\t\tLevel");
System.out.println("09:02\tLogin success\t\tLow");
System.out.println("09:15\tPassword failed\t\tMedium");
System.out.println("09:16\tAccount locked\t\tHigh");
System.out.println("10:40\tFile deleted\t\tMedium");
```

**Task 14.**

```java
System.out.println("2 + 3 = " + (2 + 3));
System.out.println("10 - 4 = " + (10 - 4));
System.out.println("6 * 7 = " + (6 * 7));
System.out.println("20 / 4 = " + (20 / 4));
System.out.println("Seconds in a day = " + (24 * 60 * 60));
```

**Task 15.** Each middle line is `#` + 28 characters + `#`, for example `"#   AUTHORISED USERS ONLY    #"`.

**Task 16.**

```java
package lab1;

public class Task16Unscramble {

    public static void main(String[] args) {
        // Morning security checklist
        System.out.println("Security checklist");
        System.out.println("------------------");
        System.out.println("1. Lock your screen");
        System.out.println("2. Check for updates");
        System.out.println("3. Back up your files");
    }

}
```

The first `}` closes `main`; the last `}` closes the class.

**Task 17.** Ctrl+Shift+F re-indents the whole file. Renaming the file renames the class because a public class must have the same name as its file.

**Task 18.** Output (before and after tidying):

```text
Password rules:
1. At least 12 characters
2. Mix of letters and numbers
3. Never reuse a password
```

**Task 19.** Many correct answers. Check against the seven spec points; keep your own version to compare.

**Task 20.** One model answer:

```java
package lab1;

/*
 * Task 20 model answer: Cyber Toolkit start screen.
 * Prints a banner, a menu and a short status report.
 */
public class Task20Toolkit {

    public static void main(String[] args) {
        // Banner
        System.out.println("========================================");
        System.out.println("          CYBER TOOLKIT v1.0");
        System.out.println("========================================");
        System.out.println();

        // Menu
        System.out.println("Main menu");
        System.out.println("1.\tCheck password strength");
        System.out.println("2.\tView login history");
        System.out.println("3.\tScan a file");
        System.out.println("4.\tExit");
        System.out.println();

        // Status report with calculations
        System.out.println("Status report");
        System.out.println("Failed logins today:\t" + (3 + 4 + 2));
        System.out.println("Scans this week:\t" + (5 * 7));
        System.out.print("Choose an option (1-4): ");
        System.out.println("[input comes in a later lab]");
    }

}
```

The status lines print `9` and `35`.
