# Lab 14 — Void Methods Hands-on Workbook (20 Tasks)

**Module:** 4300COMP Introduction to Programming · **Language:** Java

## How to use this lab

This lab has **20 hands-on tasks** on Lecture 14: method headers, defining and calling void methods, parameters and arguments, effects through `static` variables and lists, the call stack, and decomposing programs into methods. **All official Tutorial 14 exercises are included** (Tasks 2, 3, 11 and 12), marked "official". Tutorial 14's additional activity (looking for repetition in your coursework) is in the reflection; check the coursework brief's rules on help first.

**Learning outcomes:** MLO1 (methods), MLO2 (the Eclipse debugger's call-stack view in Task 4), MLO3 (decomposing specifications in Tasks 16–20), MLO4 (classes and messages).

**Setup:** create a Java project called **Lab14** in Eclipse (untick *Create module-info.java*). One class per task. Put your methods **inside the class but outside `main`**, and make them `public static` for now.

**Rules for this lab:**

1. **Header first.** Before writing a method, write its header and a one-line `/** ... */` comment saying what it does.
2. **Name with a verb**, in camelCase.
3. **Trace calls with a stack.** When output surprises you, draw the stack of method calls.
4. Predict before you run; use the hints only after a real attempt.

The **tracker** is near the end, followed by the **answer key**. Every answer was compiled and run with Java 21 (javac on the command line, not Eclipse) with the inputs shown.

## Part A — Reading and writing methods (Tasks 1–5)

### Task 1 — Label the parts

**Goal:** recognise modifiers, return type, name and parameters.

For each header, write the modifiers, return type, name, and the number and types of parameters. Say whether it is a void or a value-returning method.

1. `public static void main(String[] args)`
2. `public static double sqrt(double a)` (from `java.lang.Math`)
3. `public static void repeat(String msg, int n)`
4. `public static void pause()`
5. `private static void printReminder(String event, int hour, int minute)`
6. `public static boolean isHostAlive(String address)`

### Task 2 — Official Tutorial 14, Exercise 1

**Class:** `Hello` · **Goal:** methods that call other methods.

1. Write a void method `sayHello` that takes no input and prints one line: `Hello World!`. Call it from `main`.
2. Write a second void method `tripleHello` that calls `sayHello` three times.
3. Change `main` so that it calls `tripleHello` instead of `sayHello`.

**Think:** how many methods are on the stack while the third `Hello World!` is being printed? Name them.

### Task 3 — Official Tutorial 14, Exercise 2

**Class:** `HelloName` · **Goal:** pass an argument into a method.

Write a void method `helloName` that accepts a `String`, builds a custom message such as `Hello Bob!`, and prints it. In `main`, ask the user to type their name and pass it to `helloName`.

Then: call `helloName` twice more from `main` with **literal** arguments, such as `helloName("Ada");`. What does that show about parameters?

### Task 4 — Predict the call order

**Class:** `Order` · **Goal:** use the stack to predict output.

1. Write down the output of the slides' `StackDemo` (Lecture 14, section 6), then run it.
2. Predict the output of this program, drawing the stack at each step:

```java
public class Order {
    public static void main(String[] args) {
        System.out.println("start");
        second();
        first();
        System.out.println("end");
    }

    public static void first() {
        System.out.println("first in");
        second();
        System.out.println("first out");
    }

    public static void second() {
        System.out.println("second");
    }
}
```

3. **Eclipse:** set a breakpoint on the `println` inside `second`, run as **Debug**, and look at the **Debug** view each time it stops. Write down the stack (the list of methods) both times. Why is it different?

### Task 5 — Naming methods

**Goal:** choose clear names.

Rename each of these methods following the slides' rules (verb, descriptive, camelCase, not too long), and say what was wrong:

`Print`, `x`, `calc_total`, `ShowMenu`, `doStuff`, `printTheUsersNameAndAgeToTheScreenNicely`, `rmv`, `the_password_checker`.

## Part B — Find and fix (Tasks 6–10)

### Task 6 — Method error clinic

**Class:** `Task06Errors` · **Goal:** recognise the common method errors.

Each snippet has one problem. Record the exact compiler error, explain it, fix it.

```java
// 1: calling a method that does not exist
public static void main(String[] args) { sayHi(); }

// 2: wrong number of arguments
public static void main(String[] args) { repeat("hi"); }
public static void repeat(String m, int n) { }

// 3: arguments in the wrong order
public static void main(String[] args) { repeat(3, "hi"); }
public static void repeat(String m, int n) { }

// 4: method inside main
public static void main(String[] args) {
    public static void inner() { }
}

// 5: void method returning a value
public static void five() { return 5; }

// 6: missing static
public static void main(String[] args) { greet(); }
public void greet() { }

// 7: storing the result of a void method
public static void main(String[] args) { int x = show(); }
public static void show() { }

// 8: forgetting the brackets in a call
public static void main(String[] args) { pause; }
public static void pause() { }
```

### Task 7 — Fix the tutorial's example

**Class:** `PrintValue` · **Goal:** correct real code.

Tutorial 14's example is:

```text
public class tut14_example {
	public static void printToScreen( int inputValue )
	{
		System.out.printf(“The value is: %d”,inputValue);
}
public static void main(String[] args)
	{
		// main code
		int testValue = 123;
		methodName(testValue);
	}
}
```

1. Find **three** problems that stop it compiling or behaving well, if copied exactly. (Look at the quotes, the method call, and the class name against Java naming conventions.)
2. Write the corrected program and make it print `The value is: 123` on its own line.
3. Add a second call with the argument `testValue * 2`. What is printed?

### Task 8 — Trace calls with parameters

**Class:** `Trace` · **Goal:** follow arguments through nested calls.

Predict the exact output, drawing the stack with parameter values (for example `greet(name="Ada", times=2)`), then run it:

```java
public class Trace {
    public static void main(String[] args) {
        System.out.println("main starts");
        line('=', 6);
        greet("Ada", 2);
        line('-', 3);
        System.out.println("main ends");
    }

    public static void greet(String name, int times) {
        for (int i = 1; i <= times; i++) {
            System.out.println(i + ": Hi " + name);
            line('.', i);
        }
    }

    public static void line(char symbol, int length) {
        for (int i = 0; i < length; i++) {
            System.out.print(symbol);
        }
        System.out.println();
    }
}
```

There are **two** different variables called `i`. Explain why they don't interfere.

### Task 9 — What can a void method change?

**Class:** `Effects` · **Goal:** understand the three kinds of effect, and pass-by-value.

Type the `Effects` program from Lecture 14, section 5. **Before running**, predict the four lines of output. Then:

1. Which line shows a change to a `static` variable? To an object passed in? Which shows **no** change?
2. Write a method `void doubleAll(ArrayList<Integer> list)` that doubles every element in place using `set`. Show that the caller's list changes.
3. Write `void doubleIt(int n)` that sets `n = n * 2`. Show that the caller's variable does **not** change. Explain why in one sentence.

### Task 10 — Refactor repetition into methods

**Class:** `Before` → `After` · **Goal:** the main reason methods exist.

This program works but repeats itself:

```java
public class Before {
    public static void main(String[] args) {
        System.out.println("==============================");
        System.out.println("  Network check: router");
        System.out.println("==============================");
        System.out.println("Status: OK");
        System.out.println();
        System.out.println("==============================");
        System.out.println("  Network check: printer");
        System.out.println("==============================");
        System.out.println("Status: OFFLINE");
        System.out.println();
        System.out.println("==============================");
        System.out.println("  Network check: server");
        System.out.println("==============================");
        System.out.println("Status: OK");
        System.out.println();
    }
}
```

1. Write `After` with a method `banner(String title)` and a method `report(String device, String status)` that calls `banner`. `main` should be three lines.
2. Prove the output is **identical** (copy both outputs into a text comparison, or compare them line by line).
3. The boss now wants the `=` lines to be `-` lines. How many lines must you change in each version?

## Part C — Writing void methods (Tasks 11–15)

### Task 11 — Official Tutorial 14, Exercise 3: numCompare

**Class:** `NumCompare` · **Goal:** a method with two parameters and a decision.

Write a void method `numCompare` that accepts two integers, works out the larger, and prints the result. Verify it with the tutorial's four tests, calling it four times from `main`:

| # | a | b | Result |
| --- | ---: | ---: | --- |
| 1 | 19 | 45 | 45 is bigger |
| 2 | 12 | 4 | 12 is bigger |
| 3 | 299 | 500 | 500 is bigger |
| 4 | 5 | 5 | Neither is bigger |

### Task 12 — Official Tutorial 14, Exercise 4: diary reminder

**Class:** `Diary` · **Goal:** validated input in `main`, formatted output in a method.

Write a void method that accepts an event name (`String`) and an hour and a minute (`int`s), and prints a reminder in the format `Event Name @ HH:MM`. In `main`, read the event, hour and minute from the keyboard, and **don't let the user proceed until a valid time is entered** (hour 0–23, minute 0–59).

Test: `Team meeting`, then `25` and `10` (rejected), then `9` and `5` → `Team meeting @ 09:05`.

- **Hint 1:** a `do...while` loop (Lecture 8) repeats the time input while it is invalid.
- **Hint 2:** `%02d` prints 5 as `05`.

### Task 13 — Pause, from the slides

**Class:** `Wizard` · **Goal:** a no-parameter method with a shared `Scanner`.

1. Type the slides' `Pause` program, adding the missing `import java.util.Scanner;`.
2. Use `pause()` in a three-step "setup wizard": print `Step 1: create a project`, pause, `Step 2: create a class`, pause, `Step 3: run it`.
3. Write a second method `pauseWith(String message)` that prints a custom message instead of "Press enter to continue...". Use it for the last step.
4. Why is the `Scanner` declared **outside** `main`, as `private static`?

### Task 14 — Drawing with methods

**Class:** `Shapes` · **Goal:** build bigger methods from smaller ones (decomposition).

1. Write `printLine(char symbol, int length)`: prints `symbol` `length` times, then a new line.
2. Write `printBox(int width, int height)`: a hollow box of `#`, using `printLine` for the top and bottom.
3. Write `printTriangle(int rows)`: rows of `^`, 1 to `rows` long, using `printLine`.
4. In `main`: a line of 10 `*`, a 6×3 box, a 4-row triangle, another line of 10 `*`.
5. Draw a diagram showing which method calls which.

### Task 15 — Repeat, and guarding parameters

**Class:** `Repeat` · **Goal:** the slides' parameterised method, made robust.

1. Type the slides' `Repeat` program. Run it with `Hi there` and `3`.
2. What happens if the user enters `0`? `-2`? Is that sensible?
3. Write `repeatNumbered(String message, int n)` that prints `1. Hi there`, `2. Hi there`, …
4. Add a guard at the start of `repeatNumbered`: if `n` is above 100, print `Too many repeats.` and `return;`.

## Part D — Programs built from methods (Tasks 16–20)

### Task 16 — Receipt printer with a shared total

**Class:** `Receipt` · **Goal:** void methods that update a `static` variable.

Write a receipt printer with three void methods:

- `printHeader(String shop)`: shop name and column headings;
- `printItem(String name, int quantity, int pricePence)`: one aligned line, and adds the cost to a `static int totalPence`;
- `printFooter()`: the total in pounds and `Thank you!`.

Test in `main`: Flat white ×2 at 310p, Croissant ×1 at 245p, Water ×3 at 120p. Expected total: **12.25**.

**Question:** what goes wrong if you print two receipts in one run? How could you fix it with what you know? (Lecture 15 shows a cleaner way: returning values.)

### Task 17 — Methods that change a list

**Class:** `ListTools` · **Goal:** void methods with reference-type parameters.

1. Type the slides' `removeSmallest(ArrayList<Integer> numbers)`.
2. Write `removeLargest`.
3. Write `printList(String label, ArrayList<Integer> list)` that prints a label, the list and its size.
4. Test on `[42, 17, 93, 17, 60]`: remove the smallest, then the largest, printing after each. Then test both on an **empty** list.

Which `17` is removed, the first or the second? Why?

### Task 18 — Security toolkit menu

**Class:** `Toolkit` · **Goal:** structure a menu program with one method per job.

Write a menu loop that shows `1) Caesar encode  2) Port lookup  3) Password advice  4) Quit` and calls one void method per option:

- `showMenu()`;
- `printCaesar(String message, int key)`: reuse your Lab 13 cipher;
- `printService(int port)`: 22 SSH, 25 SMTP, 53 DNS, 80 HTTP, 443 HTTPS, otherwise "not in this table" (a `switch`);
- `printPasswordAdvice()`: three lines of advice.

`main` should contain only the loop and the `switch` on the choice. Invalid choices print `Please choose 1-4.`

- **Hint 1:** read every input with `nextLine()` and convert numbers with `Integer.parseInt` to avoid the Scanner trap.

### Task 19 — Mini-project: report card with bars

**Class:** `ReportCard` · **Goal:** decompose a small report into methods that take arrays.

Modules `{"Programming", "Systems", "Maths", "Security"}` with marks `{68, 54, 41, 77}`. Write:

- `printBanner(String title)`: the title between two lines of `=` exactly 4 longer than the title;
- `printBar(String label, int mark)`: label, mark and a bar of `#`, one per 5 marks;
- `printStats(int[] marks)`: average (1 dp) and best mark.

Expected last line: `Average 60.0, best 77`

### Task 20 — Assessment-style task: incident log viewer

**Class:** `IncidentViewer` · **Goal:** a complete program decomposed into void methods.

This is a practice task similar in skills to the module's application assessments. It is **not** an actual assessment question.

**Input** `events.log` (blank lines may appear):

```text
2026-11-24 08:02:11 OK user=alice ip=10.0.0.5
2026-11-24 09:14:02 FAIL user=bob ip=203.0.113.9
2026-11-24 09:14:40 FAIL user=bob ip=203.0.113.9
2026-11-24 09:15:05 OK user=bob ip=10.0.0.8
2026-11-24 13:47:30 FAIL user=admin ip=198.51.100.23

2026-11-24 13:47:31 FAIL user=admin ip=198.51.100.23
2026-11-24 13:47:33 FAIL user=root ip=198.51.100.23
2026-11-24 17:30:00 OK user=carol ip=10.0.0.12
```

**Specification:** `main` reads the non-blank lines into an `ArrayList<String>`, then calls three void methods, each taking the list as a parameter:

1. `printSummary`: `Events: 8 (OK 3, FAIL 5)`;
2. `printByStatus(lines, "FAIL")`: one line per FAIL event showing time, user and IP in columns;
3. `printHourChart`: for each hour that has events, `HH:00`, a `#` per event and the count.

**Expected output:**

```text
Events: 8 (OK 3, FAIL 5)
FAIL events:
  09:14:02  bob      203.0.113.9
  09:14:40  bob      203.0.113.9
  13:47:30  admin    198.51.100.23
  13:47:31  admin    198.51.100.23
  13:47:33  root     198.51.100.23
Events per hour:
  08:00 # 1
  09:00 ### 3
  13:00 ### 3
  17:00 # 1
```

Write a Javadoc comment for each method. **Security question:** three failures in three seconds against `admin` and `root` from one address. What does that pattern suggest, and why are `admin` and `root` targeted?

- **Hint 1:** reuse your Lab 13 log-parsing code inside `printByStatus`.

## Tracker

| Task | Done | Notes / score |
| --- | --- | --- |
| 1 Label the parts | ☐ | |
| 2 Official Ex 1 | ☐ | |
| 3 Official Ex 2 | ☐ | |
| 4 Call order | ☐ | |
| 5 Naming | ☐ | |
| 6 Error clinic (out of 8) | ☐ | |
| 7 Fix the tutorial example | ☐ | |
| 8 Trace with parameters | ☐ | |
| 9 Effects | ☐ | |
| 10 Refactor | ☐ | |
| 11 Official Ex 3 | ☐ | |
| 12 Official Ex 4 | ☐ | |
| 13 Pause | ☐ | |
| 14 Shapes | ☐ | |
| 15 Repeat | ☐ | |
| 16 Receipt | ☐ | |
| 17 ListTools | ☐ | |
| 18 Toolkit menu | ☐ | |
| 19 Report card | ☐ | |
| 20 Incident viewer | ☐ | |

## Reflection

1. In your own words, what happens on the stack when one method calls another?
2. Why does `tryToChange(x)` not change `x`, while `removeSmallest(numbers)` does change `numbers`?
3. Which task showed you most clearly why methods are worth writing?
4. **Tutorial 14's additional activity:** look at your own coursework solution. Find any repeated code that could become a void method. (Check the official brief's rules on help before asking anyone, including AI, about assessed work.)

## Answer key

All code was compiled and run with Java 21 (javac on the command line, not Eclipse). Outputs are actual outputs.

**Task 1.** (1) `public static`, `void`, `main`, one `String[]`; void. (2) `public static`, `double`, `sqrt`, one `double`; value-returning. (3) `public static`, `void`, `repeat`, `String` and `int`; void. (4) `public static`, `void`, `pause`, none; void. (5) `private static`, `void`, `printReminder`, `String`, `int`, `int`; void. (6) `public static`, `boolean`, `isHostAlive`, one `String`; value-returning.

**Task 2.**

```java
public class Hello {
    public static void main(String[] args) {
        tripleHello();
    }

    public static void sayHello() {
        System.out.println("Hello World!");
    }

    public static void tripleHello() {
        sayHello();
        sayHello();
        sayHello();
    }
}
```

Output (verified): `Hello World!` three times. While the third is printed, the stack is `main`, `tripleHello`, `sayHello` (three methods).

**Task 3.**

```java
import java.util.Scanner;

public class HelloName {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        System.out.print("What is your name? ");
        String name = console.nextLine();
        helloName(name);
        console.close();
    }

    public static void helloName(String name) {
        System.out.println("Hello " + name + "!");
    }
}
```

Input `Bob` → `Hello Bob!` (verified). Literal arguments work too: a parameter receives a **value**, wherever it came from.

**Task 4.** StackDemo: Option C (see Lecture 14, verified). `Order` prints `start`, `second`, `first in`, `second`, `first out`, `end` (verified). In the debugger, the first stop shows `second`, `main`; the second shows `second`, `first`, `main`, because the second time `second` was called by `first`.

**Task 5.** `Print` → `print` (camelCase starts lower case). `x` → e.g. `printReport` (meaningless). `calc_total` → `calculateTotal` (camelCase, not underscores; avoid abbreviations). `ShowMenu` → `showMenu`. `doStuff` → a specific verb such as `processOrders` (not descriptive). `printTheUsersNameAndAgeToTheScreenNicely` → `printUserDetails` (too long). `rmv` → `remove` (abbreviated). `the_password_checker` → `checkPassword` (not a verb, underscores).

**Task 6.** (1) `error: cannot find symbol`. (2) `error: method repeat in class … cannot be applied to given types;`. (3) `error: incompatible types: int cannot be converted to String`. (4) `error: illegal start of expression` (plus a follow-on error). (5) `error: incompatible types: unexpected return value`. (6) `error: non-static method greet() cannot be referenced from a static context`. (7) `error: incompatible types: void cannot be converted to int`. (8) `error: not a statement`. All verified with javac.

**Task 7.** Problems: curly quotes (`error: illegal character: '“'`); the call `methodName(testValue)` names a method that doesn't exist (`printToScreen` was intended); the class name `tut14_example` breaks the convention that class names are in UpperCamelCase (it compiles, but `Tut14Example` or `PrintValue` is better). Also, the format string has no `%n`, so the output has no new line. Corrected:

```java
public class PrintValue {
    public static void printToScreen(int inputValue) {
        System.out.printf("The value is: %d%n", inputValue);
    }

    public static void main(String[] args) {
        int testValue = 123;
        printToScreen(testValue);
    }
}
```

Output (verified): `The value is: 123`. `printToScreen(testValue * 2)` prints `The value is: 246`: the expression is worked out first, and its value is passed.

**Task 8.** Output (verified):

```text
main starts
======
1: Hi Ada
.
2: Hi Ada
..
---
main ends
```

Each `i` is a local variable of its own method, and each method call has its own space on the stack, so `line`'s `i` and `greet`'s `i` are separate variables.

**Task 9.** Output `0`, `1`, `[8, 5]`, `10` (verified). Lines 2, 3 and 4 show a `static` change, an object change and no change. `doubleAll`: `for (int i = 0; i < list.size(); i++) { list.set(i, list.get(i) * 2); }` changes the caller's list. `doubleIt` changes only its own copy of the `int`, because arguments are passed by value.

**Task 10.**

```java
public class After {
    public static void main(String[] args) {
        report("router", "OK");
        report("printer", "OFFLINE");
        report("server", "OK");
    }

    public static void report(String device, String status) {
        banner("Network check: " + device);
        System.out.println("Status: " + status);
        System.out.println();
    }

    public static void banner(String title) {
        System.out.println("==============================");
        System.out.println("  " + title);
        System.out.println("==============================");
    }
}
```

The outputs of `Before` and `After` were compared with `diff` and are identical (verified). Changing `=` to `-`: 6 lines in `Before`, 2 in `After`.

**Task 11.**

```java
public class NumCompare {
    public static void main(String[] args) {
        numCompare(19, 45);
        numCompare(12, 4);
        numCompare(299, 500);
        numCompare(5, 5);
    }

    public static void numCompare(int a, int b) {
        if (a > b) {
            System.out.println(a + " is bigger");
        } else if (b > a) {
            System.out.println(b + " is bigger");
        } else {
            System.out.println("Neither is bigger");
        }
    }
}
```

All four results match the tutorial's table (verified).

**Task 12.**

```java
import java.util.Scanner;

public class Diary {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        System.out.print("Event name: ");
        String event = console.nextLine();

        int hour, minute;
        do {
            System.out.print("Hour (0-23): ");
            hour = console.nextInt();
            System.out.print("Minute (0-59): ");
            minute = console.nextInt();
            if (hour < 0 || hour > 23 || minute < 0 || minute > 59) {
                System.out.println("That is not a valid time. Try again.");
            }
        } while (hour < 0 || hour > 23 || minute < 0 || minute > 59);

        printReminder(event, hour, minute);
        console.close();
    }

    public static void printReminder(String event, int hour, int minute) {
        System.out.printf("%s @ %02d:%02d%n", event, hour, minute);
    }
}
```

Verified: `25`/`10` prints `That is not a valid time. Try again.`, then `9`/`5` gives `Team meeting @ 09:05`.

**Task 13.** See Lecture 14 Program A (verified). `pauseWith(String message)` prints `message` instead of the fixed text, then `console.nextLine()`. The `Scanner` is shared by **every** method in the class: a variable declared inside `main` would not be visible inside `pause`.

**Task 14.**

```java
public class Shapes {
    public static void main(String[] args) {
        printLine('*', 10);
        printBox(6, 3);
        printTriangle(4);
        printLine('*', 10);
    }

    public static void printLine(char symbol, int length) {
        for (int i = 0; i < length; i++) {
            System.out.print(symbol);
        }
        System.out.println();
    }

    public static void printBox(int width, int height) {
        printLine('#', width);
        for (int row = 1; row <= height - 2; row++) {
            System.out.print('#');
            for (int col = 1; col <= width - 2; col++) {
                System.out.print(' ');
            }
            System.out.println('#');
        }
        if (height > 1) {
            printLine('#', width);
        }
    }

    public static void printTriangle(int rows) {
        for (int r = 1; r <= rows; r++) {
            printLine('^', r);
        }
    }
}
```

Output (verified):

```text
**********
######
#    #
######
^
^^
^^^
^^^^
**********
```

Call diagram: `main` calls all three; `printBox` and `printTriangle` both call `printLine`.

**Task 15.** `Hi there` ×3 (verified). With 0 or −2, the loop condition is false at the start, so nothing is printed and there is no error. That is reasonable, but a message would help the user. `repeatNumbered` prints `(i + 1) + ". " + message`; the guard is `if (n > 100) { System.out.println("Too many repeats."); return; }`.

**Task 16.**

```java
public class Receipt {
    public static int totalPence = 0;      // shared by all the methods in this class

    public static void main(String[] args) {
        printHeader("Campus Cafe");
        printItem("Flat white", 2, 310);
        printItem("Croissant", 1, 245);
        printItem("Water", 3, 120);
        printFooter();
    }

    public static void printHeader(String shop) {
        System.out.println("*** " + shop + " ***");
        System.out.printf("%-12s %3s %8s%n", "Item", "Qty", "Cost");
    }

    public static void printItem(String name, int quantity, int pricePence) {
        int cost = quantity * pricePence;
        totalPence = totalPence + cost;
        System.out.printf("%-12s %3d %8.2f%n", name, quantity, cost / 100.0);
    }

    public static void printFooter() {
        System.out.printf("%-12s %12.2f%n", "TOTAL", totalPence / 100.0);
        System.out.println("Thank you!");
    }
}
```

Output (verified): items 6.20, 2.45, 3.60 and `TOTAL 12.25`. A second receipt would **add to** the first receipt's total, because `totalPence` is never reset; set `totalPence = 0;` inside `printHeader`. Shared `static` variables are easy to get wrong, which is why the next lecture prefers methods that return values.

**Task 17.**

```java
import java.util.ArrayList;

public class ListTools {
    public static void main(String[] args) {
        ArrayList<Integer> readings = new ArrayList<Integer>();
        readings.add(42); readings.add(17); readings.add(93); readings.add(17); readings.add(60);
        printList("start", readings);
        removeSmallest(readings);
        printList("after removeSmallest", readings);
        removeLargest(readings);
        printList("after removeLargest", readings);
        ArrayList<Integer> empty = new ArrayList<Integer>();
        removeSmallest(empty);
        printList("empty list", empty);
    }

    public static void printList(String label, ArrayList<Integer> list) {
        System.out.println(label + ": " + list + " (size " + list.size() + ")");
    }

    public static void removeSmallest(ArrayList<Integer> numbers) {
        if (numbers.isEmpty()) {
            return;
        }
        int smallestIndex = 0;
        for (int i = 0; i < numbers.size(); i++) {
            if (numbers.get(i) < numbers.get(smallestIndex)) {
                smallestIndex = i;
            }
        }
        numbers.remove(smallestIndex);
    }

    public static void removeLargest(ArrayList<Integer> numbers) {
        if (numbers.isEmpty()) {
            return;
        }
        int largestIndex = 0;
        for (int i = 1; i < numbers.size(); i++) {
            if (numbers.get(i) > numbers.get(largestIndex)) {
                largestIndex = i;
            }
        }
        numbers.remove(largestIndex);
    }
}
```

Output (verified):

```text
start: [42, 17, 93, 17, 60] (size 5)
after removeSmallest: [42, 93, 17, 60] (size 4)
after removeLargest: [42, 17, 60] (size 3)
empty list: [] (size 0)
```

The **first** 17 is removed: the test is `<` (strictly less), so a later equal value never replaces the first one found. `remove(smallestIndex)` uses the `int` index version, so the right element goes.

**Task 18.**

```java
import java.util.Scanner;

public class Toolkit {
    private static Scanner console = new Scanner(System.in);

    public static void main(String[] args) {
        boolean running = true;
        while (running) {
            showMenu();
            String choice = console.nextLine().trim();
            switch (choice) {
                case "1":
                    System.out.print("Message: ");
                    String message = console.nextLine();
                    System.out.print("Key: ");
                    int key = Integer.parseInt(console.nextLine().trim());
                    printCaesar(message, key);
                    break;
                case "2":
                    System.out.print("Port number: ");
                    printService(Integer.parseInt(console.nextLine().trim()));
                    break;
                case "3":
                    printPasswordAdvice();
                    break;
                case "4":
                    running = false;
                    break;
                default:
                    System.out.println("Please choose 1-4.");
            }
        }
        System.out.println("Toolkit closed.");
    }

    public static void showMenu() {
        System.out.println();
        System.out.println("1) Caesar encode  2) Port lookup  3) Password advice  4) Quit");
        System.out.print("Choice: ");
    }

    public static void printCaesar(String message, int key) {
        String lower = message.toLowerCase();
        String result = "";
        for (int i = 0; i < lower.length(); i++) {
            char c = lower.charAt(i);
            if (c >= 'a' && c <= 'z') {
                c = (char) ('a' + (c - 'a' + key % 26 + 26) % 26);
            }
            result = result + c;
        }
        System.out.println("Encoded: " + result);
    }

    public static void printService(int port) {
        switch (port) {
            case 22:  System.out.println(port + ": SSH (remote shell)"); break;
            case 25:  System.out.println(port + ": SMTP (email)"); break;
            case 53:  System.out.println(port + ": DNS (name lookup)"); break;
            case 80:  System.out.println(port + ": HTTP (web, unencrypted)"); break;
            case 443: System.out.println(port + ": HTTPS (web, encrypted)"); break;
            default:  System.out.println(port + ": not in this table");
        }
    }

    public static void printPasswordAdvice() {
        System.out.println("- Use a long passphrase, e.g. three random words");
        System.out.println("- Never reuse a password on two sites");
        System.out.println("- Turn on two-step verification where you can");
    }
}
```

Verified with inputs `1`, `Attack at dawn`, `3` (→ `Encoded: dwwdfn dw gdzq`), `2`/`443`, `2`/`8080`, `3`, `9` (→ `Please choose 1-4.`) and `4`.

**Task 19.**

```java
public class ReportCard {
    public static void main(String[] args) {
        String[] modules = {"Programming", "Systems", "Maths", "Security"};
        int[] marks = {68, 54, 41, 77};
        printBanner("Semester 1 report");
        for (int i = 0; i < modules.length; i++) {
            printBar(modules[i], marks[i]);
        }
        printStats(marks);
    }

    public static void printBanner(String title) {
        String line = "";
        for (int i = 0; i < title.length() + 4; i++) {
            line = line + "=";
        }
        System.out.println(line);
        System.out.println("  " + title);
        System.out.println(line);
    }

    public static void printBar(String label, int mark) {
        System.out.printf("%-12s %3d |", label, mark);
        for (int i = 0; i < mark / 5; i++) {
            System.out.print("#");
        }
        System.out.println();
    }

    public static void printStats(int[] marks) {
        int total = 0, best = marks[0];
        for (int m : marks) {
            total = total + m;
            if (m > best) {
                best = m;
            }
        }
        System.out.printf("Average %.1f, best %d%n", (double) total / marks.length, best);
    }
}
```

Output (verified):

```text
=====================
  Semester 1 report
=====================
Programming   68 |#############
Systems       54 |##########
Maths         41 |########
Security      77 |###############
Average 60.0, best 77
```

**Task 20.**

```java
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Scanner;

public class IncidentViewer {
    public static void main(String[] args) throws FileNotFoundException {
        ArrayList<String> lines = new ArrayList<String>();
        Scanner read = new Scanner(new FileReader("events.log"));
        while (read.hasNextLine()) {
            String line = read.nextLine().trim();
            if (!line.isEmpty()) {
                lines.add(line);
            }
        }
        read.close();

        printSummary(lines);
        printByStatus(lines, "FAIL");
        printHourChart(lines);
    }

    /** Print how many events there are and how many of each status. */
    public static void printSummary(ArrayList<String> lines) {
        int ok = 0, fail = 0;
        for (String line : lines) {
            if (line.contains(" OK ")) {
                ok++;
            } else if (line.contains(" FAIL ")) {
                fail++;
            }
        }
        System.out.println("Events: " + lines.size() + " (OK " + ok + ", FAIL " + fail + ")");
    }

    /** Print every event with the given status, as time, user and IP. */
    public static void printByStatus(ArrayList<String> lines, String status) {
        System.out.println(status + " events:");
        for (String line : lines) {
            if (line.contains(" " + status + " ")) {
                String time = line.substring(11, 19);
                int userStart = line.indexOf("user=") + 5;
                String user = line.substring(userStart, line.indexOf(" ", userStart));
                String ip = line.substring(line.indexOf("ip=") + 3);
                System.out.printf("  %s  %-8s %s%n", time, user, ip);
            }
        }
    }

    /** Print one row per hour that has events, with a # for each event. */
    public static void printHourChart(ArrayList<String> lines) {
        System.out.println("Events per hour:");
        for (int hour = 0; hour < 24; hour++) {
            int count = 0;
            for (String line : lines) {
                if (Integer.parseInt(line.substring(11, 13)) == hour) {
                    count++;
                }
            }
            if (count > 0) {
                System.out.printf("  %02d:00 ", hour);
                for (int i = 0; i < count; i++) {
                    System.out.print("#");
                }
                System.out.println(" " + count);
            }
        }
    }
}
```

Output verified as in the task. Rapid failures against `admin` and `root` from one address suggest an automated **password-guessing** (brute-force) attempt. Those names are targeted because they exist on many systems and usually have the most privileges, so an attacker doesn't need to guess the username.

**Next:** Lecture 15 — methods that return values.
