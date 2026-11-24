# Lecture 4 — Input and Output #1: Using the Console

**Module:** 4300COMP Introduction to Programming · **Language:** Java

## Overview

Lecture 4 is the point where your programs start **talking to the user**. Until now every value was hard-coded. Now you will print prompts with `System.out`, read what the user types with `System.in` and the `Scanner` class, and format numbers neatly with `printf`. These notes rewrite the official Lecture 4 slides in plain English. Every program shown was run with Java 21, with the typed input supplied.

**By the end you should be able to:**

1. Explain what a **stream** is, and name Java’s standard output and input streams.
2. Use `print`, `println` and escape sequences to control console output.
3. Import `Scanner`, create one for `System.in`, and read a `String`, `int` and `double`.
4. Always **prompt** before reading, so the user knows what to type.
5. Explain the difference between `nextLine()`, `next()` and `nextInt()`, and fix the “skipped input” bug.
6. Format output with `printf`: `%d`, `%f`, `%.2f`, `%s`, `%n`, `%%`, width and zero-padding.
7. Design a small input → calculate → output program from a brief.

**Learning outcomes:** MLO1 (constructs), MLO2 (Scanner and printf are Java API classes you read the documentation for; Tutorial 4 also introduces the Eclipse **debugger**), MLO3 (the Movie Ticket design example).

**Matching lab:** Lab 4 (official Tutorial 4: Basic Input and Output).

**What you need from Lectures 1–3:** `print`/`println`, escape sequences, variables and types, casting, `Integer.valueOf`/`Double.valueOf`.

## 1. Recap: converting data

The lecture opens with two conversions from Lecture 3:

```java
double aDouble = 89122.89;
int anInt = (int) aDouble;           // 89122 — decimal part cut off (truncated)

String aString = "474.889";
float aFloat = Float.valueOf(aString); // 474.889
```

`float` is like `double` but less precise and uses half the memory (32 bits). You will normally use `double`.

## 2. Input, output and streams

Software does not work in isolation. It exchanges data with **input devices** (which send data to the program, like a keyboard) and **output devices** (which receive data from it, like a screen). Programs use I/O to talk to users, to other systems, and to sensors or machines.

**Key terms**

| Term | Meaning |
| --- | --- |
| I/O | Input and output: moving data (bits and bytes) from a source to a destination |
| Stream | A channel for data: a sequence of bytes flowing one way |
| Input stream | Channel from an input device **to** the program |
| Output stream | Channel **from** the program to an output device |
| `System.out` | Java’s standard output stream (the console) |
| `System.in` | Java’s standard input stream (the keyboard, via the console) |
| Console | A simple text-only interface for input and output. Eclipse shows it as the **Console** panel |

**Why streams?** This is **I/O abstraction**: the program only needs to follow the stream’s rules, not know exactly what device is on the other end. The same ideas work later for files (next lecture) and networks.

The data flows like this: **keyboard →** **`System.in`** **→ your program →** **`System.out`** **→ screen**.

## 3. Output with System.out

`System.out` has two methods you already know:

- `print(text)` — shows the text, cursor stays on the same line.
- `println(text)` — shows the text, then moves to a new line.

```java
System.out.println("Hello Programmer!");
System.out.println("How are you?");
```

```text
Hello Programmer!
How are you?
```

**Output is just a String.** Both methods expect a String, so you can build it with concatenation. These two give the same output:

```java
int a = 20, b = 22;
String sum = "The sum is " + (a + b);   // build the String first
System.out.println(sum);

int c = 20, d = 22;
System.out.println("The sum is " + (c + d));   // build it inside println
```

### Escape sequences (revision)

| Escape | Meaning |
| --- | --- |
| `\n` | new line |
| `\t` | tab |
| `\"` | double quote |
| `\'` | single quote |
| `\\` | backslash |

```java
System.out.println("It begins \"It was a bright cold day in April\" ");
System.out.println("The file is in C:\\temp");
```

```text
It begins "It was a bright cold day in April"
The file is in C:\temp
```

## 4. Input with Scanner

`System.in` gives you raw **bytes**, which are awkward to work with. Java’s **`Scanner`** class does the hard work: it reads the bytes and splits the text into **tokens**. A token is a piece of text separated by **whitespace** (spaces, tabs, new lines). For example, the sentence “All animals are equal” becomes four tokens: `All`, `animals`, `are`, `equal`.

### Three steps to use Scanner

```java
import java.util.Scanner;                         // 1. import it

public class ExampleInput {
    static Scanner console = new Scanner(System.in);   // 2. create one for System.in

    public static void main(String[] args) {
        String name;
        String age;
        name = console.nextLine();                // 3. read with its methods
        age = console.nextLine();
    }
}
```

| Line | Meaning |
| --- | --- |
| `import java.util.Scanner;` | `Scanner` lives in the package `java.util`. `import` tells the compiler where to find it. It goes **above** the class |
| `static Scanner console = new Scanner(System.in);` | Creates a Scanner object called `console` that reads from the keyboard. `new` creates an object (objects are covered properly later). `static` lets `main` use it |
| `console.nextLine()` | Waits for the user to type a line and press Enter, then returns the whole line as a String |

If the user types `John` then `25`, `name` holds `"John"` and `age` holds `"25"` (a String). But this program **prints nothing**, so it just looks frozen. Always **prompt first**.

### Scanner methods

| Method | Reads | Returns | Stops at |
| --- | --- | --- | --- |
| `nextLine()` | Everything up to Enter | `String` | the end of the line (and **removes** the newline) |
| `next()` | One token (one word) | `String` | the next whitespace |
| `nextInt()` | One token as a whole number | `int` | the next whitespace |
| `nextDouble()` | One token as a decimal number | `double` | the next whitespace |

The official [Scanner documentation](https://docs.oracle.com/en/java/javase/22/docs/api/java.base/java/util/Scanner.html) (linked in the slides) lists all of them.

### Bad input

If `nextInt()` gets text that is not a whole number (`twenty` or `25.5`), the program stops with:

```text
Exception in thread "main" java.util.InputMismatchException
```

For now you may assume users type valid data, as Tutorial 4 says. Checking input properly needs `if`, loops and exceptions, which come later.

## 5. The nextInt() then nextLine() trap

This is the most common Scanner bug, and the slides spend a whole page on it.

- `nextInt()` reads the number but **leaves the Enter (newline) behind** in the input buffer.
- `nextLine()` reads up to the next newline. If one is already waiting, it returns at once with an **empty String**.

The slide’s broken version asks for the age first:

```java
System.out.println("Please enter your age");
age = console.nextInt();
System.out.println("Please enter your name");
name = console.nextLine();   // grabs the leftover newline!
```

The user types `40` and presses Enter. Then the name prompt appears and the program does **not wait**. Verified output:

```text
Hello, . You're old enough to have voted in about 4 general elections so far
```

| What the user typed | Buffer after `nextInt()` | What `nextLine()` returns |
| --- | --- | --- |
| `40` Enter | the newline only | `""` (empty) |

**Two fixes from the slides:**

1. **Read everything with** **`nextLine()`** **and convert:** `age = Integer.valueOf(console.nextLine());`
2. **Add an extra** **`console.nextLine();`** **after every** **`next...()`** **call** to throw away the leftover newline.

### next() versus nextLine()

```java
System.out.println("Please enter your first and last names");
firstName = console.next();
lastName = console.nextLine();
```

| User types | `firstName` | `lastName` |
| --- | --- | --- |
| `Harry` Enter | `"Harry"` | `""` (empty: only the newline was left) |
| `Harry Potter` Enter | `"Harry"` | `" Potter"` (note the leading space) |

The slide asks: how to fix it? Use `next()` twice (`firstName = console.next(); lastName = console.next();`) when the user types both names on one line.

## 6. Formatting output with printf

```java
System.out.printf(formatString, argumentList);
```

The **format string** is text containing **format specifiers** (starting with `%`). Each specifier is replaced by the next argument in the list, formatted as you ask.

```java
int centimeters = 150;
System.out.printf("There are %.2f inches in %d centimeters.%n", centimeters / 2.54, centimeters);
```

```text
There are 59.06 inches in 150 centimeters.
```

- `%.2f` → 1st argument (`centimeters / 2.54` = 59.055…) as a decimal number, **2 decimal places**.
- `%d` → 2nd argument as a whole number.
- `%n` → new line (needs no argument). `printf` does **not** add a new line by itself.

### Specifier layout: `%[flags][width][.precision]conversion`

| Specifier | Meaning | Example | Output (verified) |
| --- | --- | --- | --- |
| `%d` | whole number | `printf("%d", 42)` | `42` |
| `%5d` | width 5, right-aligned | `printf("[%5d]", 42)` | `[   42]` |
| `%-5d` | width 5, left-aligned | `printf("[%-5d]", 42)` | `[42   ]` |
| `%03d` | pad with zeros to 3 | `printf("%03d", 5)` | `005` |
| `%f` | decimal number |  |  |
| `%.2f` | 2 decimal places (rounded) | `printf("%.2f", 1234.5)` | `1234.50` |
| `%08.2f` | zero-pad to 8 chars, 2 dp | `printf("%08.2f", 33.456)` | `00033.46` |
| `%,.2f` | thousands separators | `printf("%,.2f", 1234567.891)` | `1,234,567.89` |
| `%s` | String | `printf("[%-10s]", "Java")` | `[Java      ]` |
| `%c` | char | `printf("%c", 'A')` | `A` |
| `%b` | boolean | `printf("%b", true)` | `true` |
| `%n` | new line |  |  |
| `%%` | a literal `%` | `printf("%d%% done", 75)` | `75% done` |

The slide’s example `%08.2f` of 33.456: flag `0` (pad with zeros), width `8` (total characters, including the point and decimals), precision `.2`, conversion `f` → `00033.46`.

**Rounding:** `printf` **rounds** (halves go up: `%.0f` of 2.5 prints `3`), whereas a cast **cuts off**. Use `printf` for display; keep the full value in the variable.

**Mismatch error:** using `%d` with a `double` (for example `printf("%d", 2.5)`) compiles but crashes at runtime with `IllegalFormatConversionException`.

## 7. Worked programs

In the runs below, the lines the user typed are shown after the prompts. When you run these in Eclipse, click in the Console panel before typing, then press Enter.

### Program A — BasicIO (prompt, read, reply)

```java
import java.util.Scanner;

public class BasicIO {
    static Scanner console = new Scanner(System.in);

    public static void main(String[] args) {
        String name, age;
        System.out.println("Please enter your name");   // prompt (output)
        name = console.nextLine();                       // read (input)
        System.out.println("Please enter your age");
        age = console.nextLine();
        System.out.println("Hello, " + name + ", who is " + age);
    }
}
```

**Run (verified):**

```text
Please enter your name
John
Please enter your age
25
Hello, John, who is 25
```

The pattern to remember: **prompt → read → store**, repeated for each item, then **process → output**.

### Program B — BasicIOTypes (reading an int)

```java
String name;
int age;
System.out.println("Please enter your name");
name = console.nextLine();
System.out.println("Please enter your age");
age = console.nextInt();
System.out.println("Hello, " + name
        + ". You're old enough to have voted in about "
        + (age - 16) / 5 + " general elections so far ");
```

**Run (verified):** name `Sam`, age `40` → `Hello, Sam. You're old enough to have voted in about 4 general elections so far`

`(age - 16) / 5` = 24 / 5 = 4 (integer division). This order works because `nextLine()` comes **before** `nextInt()`. Swap them and you get the trap from section 5.

### Program C — the Movie Ticket Sale (design example)

**Brief:** a cinema owner donates part of the income to charity. Calculate the donation.

**Design steps from the slides:**

1. Identify the data and its types.

| Data | Direction | Type | Read with |
| --- | --- | --- | --- |
| Movie name | input | `String` | `nextLine()` (names can contain spaces) |
| Ticket price | input | `double` | `nextDouble()` |
| Tickets sold | input | `int` | `nextInt()` |
| Donation percentage | input | `double` | `nextDouble()` (e.g. 7.5) |
| Total sales, donation | output | `double` | printed with `%.2f` |

2. For each item: prompt, read, store.
3. Calculate.
4. Output, formatted with `printf`.

One possible implementation (the slides live-code this, so the exact code is not on the slides):

```java
import java.util.Scanner;

public class MovieTicketSale {
    static Scanner console = new Scanner(System.in);

    public static void main(String[] args) {
        String movie;
        double price, percent;
        int tickets;

        System.out.println("Please enter the movie name");
        movie = console.nextLine();
        System.out.println("Please enter the ticket price");
        price = console.nextDouble();
        System.out.println("Please enter the number of tickets sold");
        tickets = console.nextInt();
        System.out.println("Please enter the donation percentage");
        percent = console.nextDouble();

        double sales = price * tickets;
        double donation = sales * percent / 100;

        System.out.printf("Movie : %s%n", movie);
        System.out.printf("Total sales: £%.2f%n", sales);
        System.out.printf("Donation : £%.2f%n", donation);
    }
}
```

**Run (verified, same input as the slide):**

```text
Please enter the movie name
Taken 22
Please enter the ticket price
14
Please enter the number of tickets sold
250
Please enter the donation percentage
7.5
Movie : Taken 22
Total sales: £3500.00
Donation : £262.50
```

Why no trap here? The only `nextLine()` is the **first** read. After that every read is `nextDouble()`/`nextInt()`, which skip leftover whitespace.

**The £ sign:** if the Console shows `?` or strange characters instead of `£`, the console’s character encoding is not UTF-8. In Eclipse: **Run \> Run Configurations \> Common \> Encoding**, choose UTF-8.

### Program D — RectangleCalculator (from Tutorial 4)

```java
System.out.print("Enter the length: ");
length = console.nextInt();
System.out.print("Enter the width:  ");
width = console.nextInt();
area = length * width;
perimeter = 2 * (length + width);
System.out.println("Area = " + area + ", perimeter = " + perimeter);
```

Note the prompts use `print`, not `println`, so the user types on the same line as the prompt: `Enter the length: 7`.

## 8. Common mistakes

Messages are from `javac` or the Java 21 runtime. Eclipse words compile errors differently.

| Mistake | Example | What happens | Fix |
| --- | --- | --- | --- |
| Forgetting the import | `Scanner` used with no `import` line | Compile error: cannot find symbol — class Scanner | `import java.util.Scanner;` above the class |
| Lower-case class name | `new scanner(System.in)` | Compile error: cannot find symbol — class scanner | `Scanner` |
| Reading with no prompt | `name = console.nextLine();` first | Program looks frozen | Print a prompt first |
| `nextLine()` straight after `nextInt()` | age then name | Name is empty `""`; the program does not wait | Extra `console.nextLine();` after `nextInt()`, or read every line with `nextLine()` and convert |
| `next()` for a full name | `Sam Archer` | Only `Sam` is read | `nextLine()` |
| Wrong type for the method | `String s = console.nextInt();` | Compile error: int cannot be converted to String | Match the variable type to the method |
| Text where a number is expected | user types `twenty` for `nextInt()` | Runtime: InputMismatchException | Valid input for now; checking comes later |
| Wrong specifier for the type | `printf("%d", 2.5)` | Runtime: IllegalFormatConversionException: d != java.lang.Double | `%f` / `%.2f` for decimals |
| Fewer arguments than specifiers | `printf("%d and %d", 5)` | Prints `5 and `, then MissingFormatArgumentException | One argument per specifier |
| Expecting `printf` to add a new line | `printf("Total: %d", t)` | Next output carries on on the same line | End with `%n` |
| Writing `%` for a percent sign | `printf("50% off")` | `Prints 50, then MissingFormatArgumentException (Java reads “% o” as a specifier)` | `%%` |
| Using a cast to round money | `(int) (price * 100)` | Cuts off, never rounds up | Display with `%.2f` |

## Check yourself: 15 multiple-choice questions

Allow **15 minutes**, no Eclipse. Practice questions written for this module, not real test questions.

1. Which package must you import `Scanner` from? (A) `java.lang` (B) `java.io` (C) `java.util` (D) `java.scanner`
2. Which is Java’s standard **input** stream? (A) `System.out` (B) `System.in` (C) `Scanner.in` (D) `Console.in`
3. What does `System.out.printf("%.2f", 150 / 2.54);` print? (A) `59.05` (B) `59.06` (C) `59.055` (D) `59`
4. What does `System.out.printf("%03d", 7);` print? (A) `7` (B) `700` (C) `007` (D) `  7`
5. What does `System.out.printf("%d%%", 90);` print? (A) `90%` (B) `90%%` (C) `90` (D) runtime error
6. Which Scanner method reads a full name such as `Sam Archer`? (A) `next()` (B) `nextLine()` (C) `nextInt()` (D) `nextName()`
7. The user types `Room 101 is free` and presses Enter. What do `w = console.next(); n = console.nextInt(); r = console.nextLine();` store? (A) `"Room"`, `101`, `" is free"` (B) `"Room 101"`, `0`, `"is free"` (C) `"Room"`, `101`, `""` (D) InputMismatchException
8. After `age = console.nextInt();` the user typed `40` and Enter. What does the next `console.nextLine()` return? (A) `"40"` (B) the next line the user types (C) `""` (empty) (D) `null`
9. What happens with `System.out.printf("%d", 2.5);`? (A) prints `2` (B) prints `3` (C) compile error (D) compiles, then IllegalFormatConversionException
10. What does `%n` do in `printf`? (A) prints the letter n (B) inserts a new line (C) prints a number (D) nothing
11. What does `System.out.printf("%08.2f", 33.456);` print? (A) `33.46` (B) `00033.46` (C) `33.45600` (D) `0033.456`
12. The user types `abc` when `nextInt()` runs. What happens? (A) the value is 0 (B) compile error (C) InputMismatchException (D) NumberFormatException
13. What is the output of `System.out.print("A"); System.out.printf("B%n"); System.out.println("C");`? (A) `ABC` on one line (B) `AB` then `C` on the next line (C) `A`, `B`, `C` on three lines (D) `A` then `BC`
14. What does `System.out.printf("%.1f", 7.25);` print? (A) `7.2` (B) `7.3` (C) `7.25` (D) `7`
15. In Java I/O, a **stream** is: (A) a type of loop (B) a channel carrying a sequence of bytes between a source and a destination (C) a variable that holds text (D) the Eclipse Console window

### Answers and explanations

| Q | Answer | Why |
| --- | --- | --- |
| 1 | C | `import java.util.Scanner;` |
| 2 | B | `System.out` is output; `System.in` is input |
| 3 | B | 59.055… rounded to 2 dp |
| 4 | C | Zero-padded to width 3 |
| 5 | A | `%%` prints one `%` |
| 6 | B | `next()` stops at the space |
| 7 | A | `next()` stops at the space, `nextInt()` reads 101, `nextLine()` takes the rest including the leading space |
| 8 | C | The leftover newline ends the line at once |
| 9 | D | `%d` needs a whole number; the mismatch is found only when it runs |
| 10 | B | `printf` never adds a new line unless you ask |
| 11 | B | Zero flag, width 8, 2 dp |
| 12 | C | Scanner throws InputMismatchException (NumberFormatException comes from `valueOf`) |
| 13 | B | `print` stays on the line; `%n` ends it |
| 14 | B | `printf` rounds halves up |
| 15 | B | Definition from the slides |

All answers were checked by running the code with Java 21. **Score:** 13–15 go to Lab 4; 10–12 re-read the matching sections; under 10, re-run the worked programs yourself first.

## Quick reference and glossary

```java
import java.util.Scanner;                              // above the class

public class Template {
    static Scanner console = new Scanner(System.in);   // one Scanner for the program

    public static void main(String[] args) {
        System.out.print("Name: ");                    // prompt
        String name = console.nextLine();              // whole line

        System.out.print("Age: ");
        int age = console.nextInt();                   // one whole number
        console.nextLine();                            // throw away the leftover newline

        System.out.print("Price: ");
        double price = console.nextDouble();           // one decimal number

        System.out.printf("%s is %d and paid £%.2f%n", name, age, price);
    }
}
```

**printf cheat sheet:** `%d` int · `%f` double · `%.2f` 2 dp · `%s` String · `%c` char · `%b` boolean · `%n` new line · `%%` percent · `%5d` width 5 · `%-10s` left-aligned · `%03d` zero-padded · `%,d` thousands separator.

| Term | Meaning |
| --- | --- |
| I/O | Input/output: moving data between a program and devices |
| Input / output device | Sends data to the program (keyboard) / receives data from it (screen) |
| Stream | A one-way channel carrying a sequence of bytes |
| I/O abstraction | Code follows the stream’s rules without knowing the exact device |
| Console | Text-only input/output interface; the Console panel in Eclipse |
| `System.out` / `System.in` | Standard output / standard input streams |
| `Scanner` | `java.util` class that turns input bytes into tokens and values |
| `import` | Tells the compiler which package a class comes from |
| Token | A piece of input separated by whitespace |
| Whitespace | Spaces, tabs and new lines |
| Input buffer | Where typed characters wait until a Scanner method reads them |
| Prompt | Output telling the user what to type |
| Format string / specifier | The text given to `printf` / a `%` code inside it saying how to show one value |
| Precision / width / flag | Decimal places / minimum characters / options such as `0` or `-` |
| InputMismatchException | Thrown by Scanner when the input does not match the type requested |
| Debugger / breakpoint / step over | Eclipse tools to pause a program at a line and run it one line at a time (Tutorial 4, Task 1) |

**Next:** work through Lab 4. Lecture 5 moves from the console to **files**.
