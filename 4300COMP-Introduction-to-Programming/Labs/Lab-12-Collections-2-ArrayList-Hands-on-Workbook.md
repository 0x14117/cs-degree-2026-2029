# Lab 12 — Collections #2 (ArrayList) Hands-on Workbook (20 Tasks)

**Module:** 4300COMP Introduction to Programming · **Language:** Java

## How to use this lab

This lab has **20 hands-on tasks** on Lecture 12: creating `ArrayList`s, the `add`/`set`/`get`/`contains`/`remove`/`size`/`isEmpty` methods, wrapper classes, the three ways to iterate, and the traps that come with a list that changes size. **All official Tutorial 12 tasks and the supplementary task are included** (Tasks 2, 4, 5, 11 and 14), marked "official".

**Learning outcomes:** MLO1 (collections and algorithms), MLO2 (the `java.util` API: `ArrayList`, `Collections.sort`), MLO3 (Tasks 16–20 turn specifications into programs).

**Setup:** create a Java project called **Lab12** in Eclipse (untick *Create module-info.java*). Use **Source > Organize Imports** (Ctrl+Shift+O) to add `import java.util.ArrayList;`. Data files go in the **project folder**.

**Rules for this lab:**

1. **Write the list down after every change.** Positions move whenever you insert or remove.
2. **Print the list often.** `System.out.println(list)` shows the contents of an `ArrayList`.
3. **Predict before you run.**
4. Use the hints only after a real attempt.

The **tracker** is near the end, followed by the **answer key**. Every answer was compiled and run with Java 21 (javac on the command line, not Eclipse) with the data shown.

## Part A — Using an ArrayList (Tasks 1–5)

### Task 1 — First ArrayList

**Class:** `Task01First` · **Goal:** create, fill and inspect a list.

1. Create an `ArrayList<String>` called `modules`. Print it, its `size()` and `isEmpty()`.
2. Add three module names of your choice. Print the list, size and `isEmpty()` again.
3. Print the first and the last element using `get`. Use `size()` for the last, not a number.
4. Remove the import line and compile. Write down the error, then put it back.

- **Hint 1:** last element: `modules.get(modules.size() - 1)`.

### Task 2 — Official Tutorial 12, Task 1

**Class:** `Task02Names` · **Goal:** add and remove by value, watching the size.

Write a program that creates an `ArrayList` called `strArray` to store `String` elements.

1. Add `"Fred"`, `"Alice"` and `"Bob"`. Print the values and the size.
2. Add `"Sue"`. Print the values and the size.
3. Remove `"Fred"` and `"Alice"`. Print the values and the size.

Write your expected output for all three steps **before** running.

### Task 3 — Predict a sequence of operations

**Class:** `Task03Predict` · **Goal:** track positions as a list changes.

Write the list after each line, then run the code with a `println` after each line to check.

```java
ArrayList<String> q = new ArrayList<String>();
q.add("red");
q.add("green");
q.add(0, "blue");
q.set(2, "pink");
q.add(1, "grey");
q.remove("red");
q.remove(0);
q.add("blue");
```

Finally predict: `q.get(1)`, `q.indexOf("blue")`, `q.contains("red")`, `q.size()`.

- **Hint 1:** `add(0, "blue")` pushes everything else up one place.

### Task 4 — Official Tutorial 12, Task 2

**Class:** `Task04Copy` · **Goal:** copy a fixed array into a variable-size list.

1. Create a standard `int` array called `fixedArray` storing 10, 20 and 30.
2. Create an `ArrayList` called `variableArray` to store `Integer` values.
3. Use a `for` loop to copy the elements of `fixedArray` into `variableArray`.
4. Print the values of `variableArray` and its size.
5. Then: try declaring `ArrayList<int>` instead. What error do you get, and why?

- **Hint 1:** `variableArray.add(fixedArray[i]);`: Java wraps each `int` automatically.

### Task 5 — Official Tutorial 12, Task 3

**Class:** add to `Task02Names` · **Goal:** iterate, and search with `contains`.

1. Use a `for` loop to iterate over the `ArrayList` from Task 2 and print each element with its index.
2. Use `contains` with an `if...else` to check whether `"Fred"` is present, printing a suitable message either way.
3. **Think:** the tutorial asks for a `for` loop **and** `contains`, but `contains` already searches the whole list. Write the check a second way, without `contains`, using a for-each loop and `equals`. Which is shorter? Which do you understand better?

## Part B — Find and fix (Tasks 6–10)

### Task 6 — ArrayList error clinic

**Class:** `Task06Errors` · **Goal:** recognise the common compile and runtime errors.

Try each snippet on its own. Record the exact error, explain it, fix it.

```java
ArrayList<int> list1 = new ArrayList<int>();               // 1

ArrayList<String> list2 = new ArrayList<String>();
list2.add("a");
System.out.println(list2[0]);                              // 2
System.out.println(list2.length);                          // 3
list2.add(5);                                              // 4
System.out.println(list2.get(list2.size()));               // 5
```

- **Hint 1:** four of these are compile errors; one only fails when it runs.

### Task 7 — The slide's remove bug

**Class:** `Task07SlideBug` · **Goal:** see why positions move.

The Lecture 12 slide on `remove` contains:

```java
ArrayList<String> sList = new ArrayList<String>();
sList.add("Fred");
sList.add(1, "Alice");
sList.set(1, "Sue");
sList.remove("Fred");
sList.remove(1);
```

The slide says the last line removes "Sue".

1. Draw the list after each line.
2. Run it. Copy the exception message and explain both numbers in it.
3. Fix the last line so it really removes Sue. Then write a version that removes Sue **by value** instead.

### Task 8 — Integer lists: two traps

**Class:** `Task08IntegerTraps` · **Goal:** understand `remove(int)` versus `remove(Object)`, and `==` on `Integer`.

1. Create an `ArrayList<Integer>` containing 10, 25, 7. Call `remove(7)`. What happens? Why?
2. Now use `remove(Integer.valueOf(7))`. What does the list contain?
3. Run:

```java
Integer a = 127, b = 127, c = 128, d = 128;
System.out.println((a == b) + " " + (c == d) + " " + c.equals(d));
```

Explain the output, and write a rule for comparing values taken from an `ArrayList<Integer>`.

- **Hint 1:** a list of size 3 has no index 7.
- **Hint 2:** `==` asks "same object?"; `equals` asks "same value?".

### Task 9 — Removing while looping

**Class:** `Task09RemoveLoop` · **Goal:** understand the `i--` in Tutorial 12's hint.

Start with `[Bread, Apples, Eggs, Milk]`. The goal is to remove every word ending in `s`.

1. Write a forwards `for` loop that removes a word when `word.endsWith("s")`, **without** `i--`. Predict, then run. Which plural survives, and why?
2. Add `i--` after the `remove`. Run again.
3. Write a third version that loops **backwards** (from `size() - 1` down to 0) with no `i--`. Why does going backwards avoid the problem?

- **Hint 1:** draw the list and the value of `i` at each step.

### Task 10 — Three ways to iterate

**Class:** `Task10Iterate` · **Goal:** use each loop style for the job it suits.

Using `ArrayList<Integer> scores` containing 55, 72, 64, 90, 38:

1. Print the total using a **for-each** loop.
2. Print each score with its position (`1: 55` …) using a **regular `for`** loop.
3. Using a **`while`** loop, find the position of the first score below 40 and stop there.
4. Inside a for-each loop, try `scores.remove(...)`. What happens? (Write down the exception's name.) Why should you never change a list's size in a for-each loop?

- **Hint 1:** for-each: `for (int s : scores)`, unboxing each `Integer` to `int`.

## Part C — Lists of unknown size (Tasks 11–15)

### Task 11 — Official Tutorial 12, Task 4: numbers from a file

**Class:** `Task11FileStats` · **Goal:** read an unknown amount of data into a list.

`numbers.txt` contains:

```text
12 7 30 -4 18 25
9
```

Read **all** the integers into an `ArrayList<Integer>`, then calculate the average and find the smallest and largest numbers.

Expected: 7 numbers, average 13.86 (2 dp), smallest −4, largest 30.

Then empty the file and run again. Make sure your program says so instead of crashing.

- **Hint 1:** `while (read.hasNextInt()) { numbers.add(read.nextInt()); }`
- **Hint 2:** check `isEmpty()` before using `get(0)`.

### Task 12 — Collect until a sentinel

**Class:** `Task12Reverse` · **Goal:** see the advantage over arrays.

Read whole numbers until `-1` into an `ArrayList`, then print how many were entered and print them in reverse order.

Test: `4 8 15 16 23 42 -1` → `You entered 6 numbers.` and `Reversed: 42 23 16 15 8 4`

Why would this be awkward with an array from Lecture 11?

### Task 13 — Searching a list

**Class:** `Task13Search` · **Goal:** use `indexOf`, `lastIndexOf`, `contains` and counting.

A login record holds: `alice, bob, alice, carol, alice, dave`.

1. Print `indexOf("alice")`, `lastIndexOf("alice")` and `indexOf("eve")`.
2. Count how many times `alice` appears using a for-each loop.
3. Look up `lastIndexOf` in the [ArrayList documentation](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayList.html). What does it return when the value is absent?

### Task 14 — Official Tutorial 12, supplementary: remove plurals

**Class:** `Task14Plurals` · **Goal:** read words from a file into a list and filter them.

`words.txt` contains, one per line: `Bread`, `Cheese`, `Apples`, `Milk`, `Eggs`.

1. Read the words into an `ArrayList<String>` and print them.
2. Remove all plural words (those ending in `s`), using the tutorial's hint loop, and print the new list.

Expected: `[Bread, Cheese, Apples, Milk, Eggs]` then `[Bread, Cheese, Milk]`.

**Think:** "ends in s" is a rough rule. Name two English words it would get wrong. (This kind of shortcut is common in real filters, and it is why they need testing.)

### Task 15 — Array or ArrayList?

**Class:** `Task15Convert` · **Goal:** convert both ways and choose wisely.

1. Convert `String[] days = {"Mon", "Tue", "Wed"};` into an `ArrayList<String>` with a loop.
2. Add `"Thu"` to the list. Convert the list back to an array with `toArray(new String[0])` and print its length.
3. For each situation, choose array or `ArrayList` and give one reason: (a) the 12 months of the year; (b) items in an online shopping basket; (c) 1,000,000 sensor readings of type `double`, count known in advance; (d) users currently logged in to a server.

## Part D — Programs with lists (Tasks 16–20)

### Task 16 — To-do list menu

**Class:** `Task16ToDo` · **Goal:** a menu program that grows and shrinks a list.

Write a menu loop: `[A]dd, [R]emove, [L]ist, [Q]uit`.

- **A** reads a task (a whole line) and adds it.
- **L** prints the tasks numbered from 1, or `Nothing to do!` if empty.
- **R** reads a task number (from 1) and removes it, or prints `No task N.` if invalid.
- **Q** ends the loop and prints how many tasks are left.
- Anything else prints `Unknown option.`

Test: add two tasks, list, try to remove task 5, remove task 1, list, type `X`, quit.

- **Hint 1:** read every input with `nextLine()` to avoid the `nextInt`/`nextLine` trap (Lecture 4); convert a number with `Integer.parseInt(...)`.
- **Hint 2:** the user's number 1 is index 0.

### Task 17 — Unique visitors

**Class:** `Task17Unique` · **Goal:** build a list without duplicates.

A web server logged visits from these addresses:

```java
String[] visits = {"10.0.0.5", "10.0.0.7", "10.0.0.5", "192.168.1.20", "10.0.0.7", "10.0.0.9"};
```

Build an `ArrayList<String>` of **unique** addresses, in order of first appearance, and print `6 visits from 4 addresses: [...]`.

- **Hint 1:** add an address only if the list does not already contain it.

### Task 18 — Blocklist checker

**Class:** `Task18Blocklist` · **Goal:** use one list to make decisions about other data.

`blocklist.txt` holds blocked IP addresses, one per line. `connections.txt` holds incoming connection addresses, one per line:

```text
blocklist.txt          connections.txt
203.0.113.9            10.0.0.5
198.51.100.23          203.0.113.9
203.0.113.44           10.0.0.7
                       198.51.100.23
                       10.0.0.5
                       203.0.113.9
```

Read the blocklist into an `ArrayList`. Then, for each connection, print `ALLOW` or `DENY` and the address. Finally print `Allowed 3, denied 3 (3 addresses on the blocklist)`.

**Cyber security link:** this is a toy version of how a firewall or web server applies a **deny list**. (The addresses above come from ranges reserved for documentation, so they are safe to use in examples.) Question: what is the difference between a **deny list** (block these, allow everything else) and an **allow list** (allow only these)? Which is safer by default?

### Task 19 — Mini-project: failed-login watchlist

**Class:** `Task19Watchlist` · **Goal:** count per user with two parallel `ArrayList`s.

`auth_log.txt` holds login attempts, one per line: a username and `OK` or `FAIL`.

```text
alice OK
bob FAIL
bob FAIL
carol FAIL
bob FAIL
alice FAIL
mallory FAIL
mallory FAIL
mallory FAIL
mallory FAIL
carol OK
bob OK
```

**Specification:**

1. Read every line. For each `FAIL`, add 1 to that user's count. Users appear in the list in the order of their first failure.
2. Print each user who failed at least once with their count.
3. Print a **watchlist** of users with **3 or more** failures.

Expected:

```text
bob: 3 failed
carol: 1 failed
alice: 1 failed
mallory: 4 failed
Watchlist (3+ failures): [bob, mallory]
```

**Questions:** (1) Why do `users` and `failures` have to stay in step? (2) `bob` eventually logged in successfully. Should he still be on the watchlist? Write a short argument for each side. (3) What would make this tool more useful to a security analyst?

- **Hint 1:** `int index = users.indexOf(user);` If it is −1, add the user and a count of 1; otherwise `failures.set(index, failures.get(index) + 1)`.

### Task 20 — Assessment-style task: event attendee manager

**Class:** `Attendees` · **Goal:** a complete command-driven program using an `ArrayList`.

This is a practice task similar in skills to the module's application assessments. It is **not** an actual assessment question.

**Specification:** an event has a capacity of **5**. The program repeatedly reads a command:

- `register NAME`: add the name, unless it is already registered (**ignoring case**) or the event is full. Print `Registered NAME (n/5)`, `NAME is already registered.` or `Sorry, the event is full.`
- `cancel NAME`: remove the name (ignoring case), or print `NAME is not registered.`
- `list`: print the number attending and the names in **alphabetical order**, without changing the registration order.
- `quit`: stop, save the names (in registration order) to `attendees.txt`, one per line, and print how many were saved.
- anything else: `Unknown command: ...`

**Test input:**

```text
register Sam
register priya
register sam
register Leo
register Aisha
register Ben
register Zoe
list
cancel Tom
cancel leo
list
dance
quit
```

Write a test plan from this input with an expected line for each command, then run it.

- **Hint 1:** `Collections.sort(list)` (import `java.util.Collections`) sorts a list in place; sort a **copy**: `new ArrayList<String>(names)`.
- **Hint 2:** `console.next()` reads the command word, then a second `console.next()` reads the name.

## Tracker

| Task | Done | Notes / score |
| --- | --- | --- |
| 1 First ArrayList | ☐ | |
| 2 Official Task 1 | ☐ | |
| 3 Predict sequence (out of 10) | ☐ | |
| 4 Official Task 2 | ☐ | |
| 5 Official Task 3 | ☐ | |
| 6 Error clinic (out of 5) | ☐ | |
| 7 Slide remove bug | ☐ | |
| 8 Integer traps | ☐ | |
| 9 Removing while looping | ☐ | |
| 10 Three loops | ☐ | |
| 11 Official Task 4 | ☐ | |
| 12 Sentinel and reverse | ☐ | |
| 13 Searching | ☐ | |
| 14 Official supplementary: plurals | ☐ | |
| 15 Array or ArrayList | ☐ | |
| 16 To-do menu | ☐ | |
| 17 Unique visitors | ☐ | |
| 18 Blocklist | ☐ | |
| 19 Failed-login watchlist | ☐ | |
| 20 Attendee manager | ☐ | |

## Reflection

1. In one sentence each: when would you choose an array, and when an `ArrayList`?
2. Which trap (moving positions, `remove(int)`, `==` on `Integer`, removing in a loop) caught you, and how will you spot it next time?
3. Which of the three loop styles do you find clearest, and why?
4. How did using lists change the way you designed Tasks 18–20 compared with arrays in Lab 11?

## Answer key

All code was compiled and run with Java 21 (javac on the command line, not Eclipse). Outputs are actual outputs.

**Task 1.** A new list prints `[]`, size 0, `isEmpty()` true. Without the import: `error: cannot find symbol` (class `ArrayList`), reported twice on the declaration line (verified).

**Tasks 2 and 5.**

```java
import java.util.ArrayList;

public class Task02Names {
    public static void main(String[] args) {
        ArrayList<String> strArray = new ArrayList<String>();
        strArray.add("Fred");
        strArray.add("Alice");
        strArray.add("Bob");
        System.out.println(strArray + " size " + strArray.size());

        strArray.add("Sue");
        System.out.println(strArray + " size " + strArray.size());

        strArray.remove("Fred");
        strArray.remove("Alice");
        System.out.println(strArray + " size " + strArray.size());

        // Official Task 3: a for loop with contains and if...else
        for (int i = 0; i < strArray.size(); i++) {
            System.out.println("Element " + i + ": " + strArray.get(i));
        }
        if (strArray.contains("Fred")) {
            System.out.println("Fred is in the list");
        } else {
            System.out.println("Fred is not in the list");
        }
    }
}
```

Output (verified):

```text
[Fred, Alice, Bob] size 3
[Fred, Alice, Bob, Sue] size 4
[Bob, Sue] size 2
Element 0: Bob
Element 1: Sue
Fred is not in the list
```

Task 5 question 3, without `contains`: `boolean found = false; for (String s : strArray) { if (s.equals("Fred")) { found = true; } }`. `contains` does exactly this for you.

**Task 3.** `[blue, red, green]` (after the three adds) → `[blue, red, pink]` → `[blue, grey, red, pink]` → `[blue, grey, pink]` → `[grey, pink]` → `[grey, pink, blue]`. Then `pink`, `2`, `false`, `3`. All verified.

**Task 4.**

```java
import java.util.ArrayList;

public class Task04Copy {
    public static void main(String[] args) {
        int[] fixedArray = {10, 20, 30};
        ArrayList<Integer> variableArray = new ArrayList<Integer>();
        for (int i = 0; i < fixedArray.length; i++) {
            variableArray.add(fixedArray[i]);
        }
        System.out.println(variableArray + " size " + variableArray.size());
    }
}
```

Output (verified): `[10, 20, 30] size 3`. `ArrayList<int>` gives `error: unexpected type`: the base type must be an object type.

**Task 6.** (1) `error: unexpected type` → `ArrayList<Integer>`. (2) `error: array required, but ArrayList<String> found` → `list2.get(0)`. (3) `error: cannot find symbol` → `list2.size()`. (4) `error: incompatible types: int cannot be converted to String` → add a `String`. (5) Compiles, then `IndexOutOfBoundsException: Index 1 out of bounds for length 1` → `get(list2.size() - 1)`. All verified.

**Task 7.** `[Fred]` → `[Fred, Alice]` → `[Fred, Sue]` → `[Sue]` → crash: `IndexOutOfBoundsException: Index 1 out of bounds for length 1` (index 1 asked for; the list has length 1) (verified). Fix: `sList.remove(0);` or `sList.remove("Sue");`.

**Task 8.** (1) `remove(7)` means "remove index 7": `IndexOutOfBoundsException: Index 7 out of bounds for length 3`. (2) `[10, 25]` (verified). (3) `true false true` (verified): Java reuses `Integer` objects for small values (−128 to 127), so `==` only happens to work there. Rule: compare `Integer` values with `.equals()`, or store them in `int` variables first.

**Task 9.** Without `i--`: `[Bread, Eggs, Milk]`. "Eggs" survives because after "Apples" (index 1) is removed, "Eggs" moves to index 1, and `i++` moves on to index 2. With `i--`: `[Bread, Milk]`. Backwards also gives `[Bread, Milk]` (both verified): removing at index `i` only moves the elements **after** `i`, which have already been checked.

**Task 10.** Total 319. The `while` loop finds 38 at position 5 (index 4). Removing inside a for-each loop throws `ConcurrentModificationException`: the loop detects that the list changed under it.

**Task 11.**

```java
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Scanner;

public class Task11FileStats {
    public static void main(String[] args) throws FileNotFoundException {
        ArrayList<Integer> numbers = new ArrayList<Integer>();
        Scanner read = new Scanner(new FileReader("numbers.txt"));
        while (read.hasNextInt()) {
            numbers.add(read.nextInt());
        }
        read.close();

        if (numbers.isEmpty()) {
            System.out.println("The file contains no numbers.");
        } else {
            int sum = 0;
            int smallest = numbers.get(0);
            int largest = numbers.get(0);
            for (int n : numbers) {
                sum = sum + n;
                if (n < smallest) {
                    smallest = n;
                }
                if (n > largest) {
                    largest = n;
                }
            }
            System.out.println("Read " + numbers.size() + " numbers: " + numbers);
            System.out.printf("Average: %.2f%n", (double) sum / numbers.size());
            System.out.println("Smallest: " + smallest + ", largest: " + largest);
        }
    }
}
```

Output (verified): `Read 7 numbers: [12, 7, 30, -4, 18, 25, 9]`, `Average: 13.86`, `Smallest: -4, largest: 30`. Empty file: `The file contains no numbers.` (verified).

**Task 12.**

```java
import java.util.ArrayList;
import java.util.Scanner;

public class Task12Reverse {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        ArrayList<Integer> values = new ArrayList<Integer>();
        System.out.print("Enter whole numbers, -1 to finish: ");
        int n = console.nextInt();
        while (n != -1) {
            values.add(n);
            n = console.nextInt();
        }
        System.out.println("You entered " + values.size() + " numbers.");
        System.out.print("Reversed:");
        for (int i = values.size() - 1; i >= 0; i--) {
            System.out.print(" " + values.get(i));
        }
        System.out.println();
        console.close();
    }
}
```

Output verified as in the task. With an array you would have to choose a size before knowing how many numbers will come.

**Task 13.** `0 4 -1`; alice appears 3 times (verified). `lastIndexOf` returns −1 when the value is absent.

**Task 14.**

```java
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Scanner;

public class Task14Plurals {
    public static void main(String[] args) throws FileNotFoundException {
        ArrayList<String> words = new ArrayList<String>();
        Scanner read = new Scanner(new FileReader("words.txt"));
        while (read.hasNext()) {
            words.add(read.next());
        }
        read.close();
        System.out.println("All words: " + words);

        // remove all plural words
        for (int i = 0; i < words.size(); i++) {
            String word = words.get(i);
            if (word.endsWith("s")) {
                words.remove(i);
                i--;              // the next word has moved into position i
            }
        }
        System.out.println("Without plurals: " + words);
    }
}
```

Output (verified): `All words: [Bread, Cheese, Apples, Milk, Eggs]`, `Without plurals: [Bread, Cheese, Milk]`. Words the rule gets wrong: "Bus", "Glass" (singular, ending in s) and "Children", "Mice" (plural, no s).

**Task 15.** After adding "Thu", `toArray` gives an array of length 4. (a) array (fixed 12); (b) `ArrayList` (changes constantly); (c) array (known count; primitives are more efficient); (d) `ArrayList` (users log in and out).

**Task 16.**

```java
import java.util.ArrayList;
import java.util.Scanner;

public class Task16ToDo {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        ArrayList<String> tasks = new ArrayList<String>();
        boolean running = true;
        while (running) {
            System.out.print("[A]dd, [R]emove, [L]ist, [Q]uit: ");
            String choice = console.nextLine().trim().toUpperCase();
            switch (choice) {
                case "A":
                    System.out.print("Task: ");
                    tasks.add(console.nextLine());
                    break;
                case "R":
                    System.out.print("Number to remove: ");
                    int number = Integer.parseInt(console.nextLine().trim());
                    if (number >= 1 && number <= tasks.size()) {
                        System.out.println("Removed: " + tasks.remove(number - 1));
                    } else {
                        System.out.println("No task " + number + ".");
                    }
                    break;
                case "L":
                    if (tasks.isEmpty()) {
                        System.out.println("Nothing to do!");
                    }
                    for (int i = 0; i < tasks.size(); i++) {
                        System.out.println((i + 1) + ". " + tasks.get(i));
                    }
                    break;
                case "Q":
                    running = false;
                    break;
                default:
                    System.out.println("Unknown option.");
            }
        }
        System.out.println("Goodbye. " + tasks.size() + " task(s) left.");
        console.close();
    }
}
```

Verified with the test sequence: it lists two tasks, prints `No task 5.`, `Removed: Revise arrays`, lists `1. Finish Lab 12`, `Unknown option.`, then `Goodbye. 1 task(s) left.` `remove(index)` **returns** the removed element, which is why it can be printed. (`trim()` removes spaces from both ends of a String; Lecture 13 covers more String methods.)

**Task 17.**

```java
import java.util.ArrayList;

public class Task17Unique {
    public static void main(String[] args) {
        String[] visits = {"10.0.0.5", "10.0.0.7", "10.0.0.5", "192.168.1.20", "10.0.0.7", "10.0.0.9"};
        ArrayList<String> unique = new ArrayList<String>();
        for (String ip : visits) {
            if (!unique.contains(ip)) {
                unique.add(ip);
            }
        }
        System.out.println(visits.length + " visits from " + unique.size() + " addresses: " + unique);
    }
}
```

Output (verified): `6 visits from 4 addresses: [10.0.0.5, 10.0.0.7, 192.168.1.20, 10.0.0.9]`.

**Task 18.**

```java
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Scanner;

public class Task18Blocklist {
    public static void main(String[] args) throws FileNotFoundException {
        ArrayList<String> blocked = new ArrayList<String>();
        Scanner read = new Scanner(new FileReader("blocklist.txt"));
        while (read.hasNext()) {
            blocked.add(read.next());
        }
        read.close();

        int allowed = 0, denied = 0;
        Scanner conns = new Scanner(new FileReader("connections.txt"));
        while (conns.hasNext()) {
            String ip = conns.next();
            if (blocked.contains(ip)) {
                System.out.println("DENY  " + ip);
                denied++;
            } else {
                System.out.println("ALLOW " + ip);
                allowed++;
            }
        }
        conns.close();
        System.out.println("Allowed " + allowed + ", denied " + denied + " (" + blocked.size() + " addresses on the blocklist)");
    }
}
```

Output (verified): ALLOW, DENY, ALLOW, DENY, ALLOW, DENY, then `Allowed 3, denied 3 (3 addresses on the blocklist)`. An allow list is safer by default: anything not explicitly trusted is refused, so a new or unknown threat is blocked automatically. A deny list only blocks threats someone already knows about.

**Task 19.**

```java
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Scanner;

public class Task19Watchlist {
    public static void main(String[] args) throws FileNotFoundException {
        final int THRESHOLD = 3;
        ArrayList<String> users = new ArrayList<String>();     // users[i] ...
        ArrayList<Integer> failures = new ArrayList<Integer>(); // ... has failures[i] failed logins

        Scanner read = new Scanner(new FileReader("auth_log.txt"));
        while (read.hasNext()) {
            String user = read.next();
            String result = read.next();
            if (result.equals("FAIL")) {
                int index = users.indexOf(user);
                if (index == -1) {
                    users.add(user);
                    failures.add(1);
                } else {
                    failures.set(index, failures.get(index) + 1);
                }
            }
        }
        read.close();

        ArrayList<String> watchlist = new ArrayList<String>();
        for (int i = 0; i < users.size(); i++) {
            System.out.println(users.get(i) + ": " + failures.get(i) + " failed");
            if (failures.get(i) >= THRESHOLD) {
                watchlist.add(users.get(i));
            }
        }
        System.out.println("Watchlist (" + THRESHOLD + "+ failures): " + watchlist);
    }
}
```

Output verified as in the task. (1) The same index must mean the same user in both lists; if one list changes without the other, counts are attached to the wrong user. (2) For keeping him: three failures before a success can mean a guessed password. For removing him: he may simply have mistyped. Many systems flag this pattern for a human to check. (3) Ideas: timestamps, source addresses, failures within a short time window, and saving the report to a file.

**Task 20.**

```java
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Attendees {
    public static void main(String[] args) throws FileNotFoundException {
        final int CAPACITY = 5;
        Scanner console = new Scanner(System.in);
        ArrayList<String> names = new ArrayList<String>();
        boolean running = true;

        while (running) {
            System.out.print("Command (register, cancel, list, quit): ");
            String command = console.next().toLowerCase();
            if (command.equals("register")) {
                String name = console.next();
                boolean duplicate = false;
                for (String existing : names) {
                    if (existing.equalsIgnoreCase(name)) {
                        duplicate = true;
                    }
                }
                if (duplicate) {
                    System.out.println(name + " is already registered.");
                } else if (names.size() >= CAPACITY) {
                    System.out.println("Sorry, the event is full.");
                } else {
                    names.add(name);
                    System.out.println("Registered " + name + " (" + names.size() + "/" + CAPACITY + ")");
                }
            } else if (command.equals("cancel")) {
                String name = console.next();
                int found = -1;
                for (int i = 0; i < names.size(); i++) {
                    if (names.get(i).equalsIgnoreCase(name)) {
                        found = i;
                    }
                }
                if (found == -1) {
                    System.out.println(name + " is not registered.");
                } else {
                    names.remove(found);
                    System.out.println("Cancelled " + name);
                }
            } else if (command.equals("list")) {
                ArrayList<String> sorted = new ArrayList<String>(names);
                Collections.sort(sorted);
                System.out.println(sorted.size() + " attending: " + sorted);
            } else if (command.equals("quit")) {
                running = false;
            } else {
                System.out.println("Unknown command: " + command);
            }
        }

        PrintWriter out = new PrintWriter("attendees.txt");
        for (String name : names) {
            out.println(name);
        }
        out.close();
        System.out.println("Saved " + names.size() + " name(s) to attendees.txt");
        console.close();
    }
}
```

Output with the test input (verified, prompts removed):

```text
Registered Sam (1/5)
Registered priya (2/5)
sam is already registered.
Registered Leo (3/5)
Registered Aisha (4/5)
Registered Ben (5/5)
Sorry, the event is full.
5 attending: [Aisha, Ben, Leo, Sam, priya]
Tom is not registered.
Cancelled leo
4 attending: [Aisha, Ben, Sam, priya]
Unknown command: dance
Saved 4 name(s) to attendees.txt
```

`attendees.txt` contains `Sam`, `priya`, `Aisha`, `Ben`. Notice `priya` sorts **last**: `Collections.sort` orders Strings by character code, and every upper-case letter comes before every lower-case letter. A good test plan catches this; one fix is `Collections.sort(sorted, String.CASE_INSENSITIVE_ORDER);`.

**Next:** Lecture 13, `String` and `char` in depth.
