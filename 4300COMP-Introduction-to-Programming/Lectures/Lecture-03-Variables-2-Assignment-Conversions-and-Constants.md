# Lecture 3 — Variables #2: Assignment, Conversions and Constants

**Module:** 4300COMP Introduction to Programming · **Language:** Java

## Overview

Lecture 3 goes deeper into variables: how assignment changes a variable’s **state**, how `double` and `String` behave, how to **convert a String into a number** with wrapper classes, how to make **constants** with `final`, and how to read compiler errors calmly. These notes rewrite the official Lecture 3 slides in plain English. Every output shown was run with Java 21.

**By the end you should be able to:**

1. Explain the two steps of getting data into memory: declare, then assign.
2. Trace how a variable’s value changes through several assignments.
3. Explain why a `double` result cannot go straight into an `int`.
4. Join Strings, and explain why `"42.45" + 10` is not `52.45`.
5. Name the wrapper class for each primitive type and explain boxing and unboxing.
6. Convert a String to a number with `Integer.valueOf`, `Double.valueOf` and `Boolean.valueOf`, and say what happens when the text is not a valid number.
7. Declare and use a named constant with `final`, following the naming convention.
8. Fix syntax errors by reading the compiler’s message and line number.

**Learning outcomes:** MLO1 (programming constructs); MLO2 (wrapper classes are your first real use of the Java API).

**Matching lab:** Lab 3 (official Tutorial 3: Variables #2).

**What you need from Lecture 2:** declaring and assigning variables, `int`/`double`/`char`/`boolean`/`String`, precedence, integer division, casting and `+` with Strings.

## 1. Getting data into memory

A program can only work on data that is in memory. So far you have **hard-coded** data (typed literals into the program); next session covers data typed by the user. Either way, two steps are needed:

1. **Allocate memory:** declare a variable, `datatype identifier;`
2. **Store the data:** assign a value to it.

Facts about variables from the slides:

- The content can change while the program runs.
- A variable must be **declared before it is used**.
- A local variable is **not automatically given a value**. Reading it before assigning is a compile error.
- When a new value is assigned, **the old one is destroyed**.
- A value can only change through an **assignment statement** or an **input (read) statement**.

```java
int num1;
int num2;
double sale;
char first;
String str;
```

## 2. Assignment and variable state

The assignment statement has the form:

```java
variable = expression;
```

Java **evaluates the expression on the right first**, then stores the result in the variable on the left, replacing any previous value. The first assignment **initialises** the variable. In Java a single `=` is the **assignment operator**.

```java
num1 = 4;
num2 = 4 * 5 - 11;          // 20 - 11 = 9
sale = 0.02 * 1000;         // 20.0
first = 'D';
str = "It is a sunny day.";
```

### Tracing state (the slide example)

The **state** of a program is the set of values its variables hold at one moment. Trace each line:

```java
int num1, num2, num3;
num1 = 18;           // line 1
num1 = num1 + 27;    // line 2
num2 = num1;         // line 3
num3 = num2 / 5;     // line 4
num3 = num3 / 4;     // line 5
```

| After line | Working | `num1` | `num2` | `num3` |
| --- | --- | --- | --- | --- |
| declaration | memory reserved, no values | – | – | – |
| 1 | store 18 | 18 | – | – |
| 2 | 18 + 27 = 45 | 45 | – | – |
| 3 | copy the value of `num1` | 45 | 45 | – |
| 4 | 45 / 5 = 9 | 45 | 45 | 9 |
| 5 | 9 / 4 = 2 (integer division) | 45 | 45 | 2 |

Verified output when printed: `45 45 2`.

**Line 3 copies a value**, it does not link the variables. If you change `num1` afterwards, `num2` stays 45.

## 3. double types

`double` holds **floating-point** values: numbers with a “point something” such as 8.7, 12.5 or 10.1. Storing a `double` result in an `int` is not allowed, because the decimal part would be lost. Eclipse underlines it in red, and the compiler refuses.

The slide’s `AreaCalculator`:

```java
public class AreaCalculator {
    public static void main(String[] args) {
        double length = 23.5;
        double width = 14.7;
        int area = 0;
        area = length * width;
        System.out.println("Area is: " + area);
    }
}
```

```text
AreaCalculator.java:6: error: incompatible types: possible lossy conversion from double to int
```

**Two fixes:** make `area` a `double` (keeps 345.45), or cast: `area = (int) (length * width);` (stores 345, decimal cut off). Choose based on what the program needs.

**Watch out:** the slide prints the code with curly “smart” quotes (“ ”). If you copy them into Eclipse you get an error; Java only accepts straight quotes `"`.

## 4. String types

A `String` is a sequence of characters.

```java
String hello = "Hello";
String world = "World";
String helloWorld = hello + " " + world;   // "Hello World"
```

The `+` joins (concatenates) them. The `" "` in the middle adds the space.

**Strings are objects.** `int` and `double` are primitive types (lower-case names); `String` is a class (capital S). Objects can do more: they carry built-in methods such as `length()`. Manipulating Strings is covered in a later lecture.

## 5. Converting Strings to numbers

Programs often hold numbers as text. User input, for example, arrives as a String (next session). Text cannot be used in arithmetic:

```java
String numString = "42.45";
double numDouble = 42.45;
```

| Variable | What is stored |
| --- | --- |
| `numDouble` | the number 42.45 |
| `numString` | five characters: `4` `2` `.` `4` `5` |

The slide asks: what is `numString + 10`? Because one side is a String, `+` joins: the result is `"42.4510"`, not 52.45.

### Primitive wrapper classes

Every primitive type has a matching **wrapper class**: an object version with extra abilities.

| Primitive | Wrapper |
| --- | --- |
| `int` | `Integer` |
| `char` | `Character` |
| `long` | `Long` |
| `short` | `Short` |
| `byte` | `Byte` |
| `float` | `Float` |
| `double` | `Double` |
| `boolean` | `Boolean` |

Only `int` → `Integer` and `char` → `Character` change name; the rest just gain a capital letter.

**Boxing and unboxing.** Java converts between the two automatically:

```java
Integer x = 33;   // boxing: primitive int -> Integer object
int y = x;        // unboxing: Integer object -> primitive int
```

Most of your work will use the primitive types. The wrappers matter now because of one useful job: **parsing** (reading a number out of text).

### valueOf: text to number

```java
String numString = "42.45";
double numDouble = Double.valueOf(numString);   // 42.45

String trueString = "true";
boolean aBool = Boolean.valueOf(trueString);    // true

int whole = Integer.valueOf("42");              // 42
```

Now `numDouble + 10` gives `52.45`.

| Call | Result (verified) |
| --- | --- |
| `Integer.valueOf("42") + 8` | `50` |
| `Integer.valueOf("-7") * 2` | `-14` |
| `Double.valueOf("3") / 2` | `1.5` |
| `Boolean.valueOf("TRUE")` | `true` (case is ignored) |
| `Boolean.valueOf("yes")` | `false` — anything other than “true” gives `false`, with no error |

`Integer.parseInt("42")` and `Double.parseDouble("42.45")` (used in Lab 2) do the same job. Either is fine.

### When conversion fails

If the text is not a valid number, Java cannot convert it. It throws an **exception**: its way of saying “something is wrong”, and the program stops.

```java
String numString = "42.4x";
double numDouble = Double.valueOf(numString);
```

```text
Exception in thread "main" java.lang.NumberFormatException: For input string: "42.4x"
```

This is a **runtime** error: the code compiles fine; it fails only when it runs. Other inputs that fail the same way (verified): `Integer.valueOf("42.5")` (an `int` cannot have a decimal point), `Integer.valueOf(" 42")` (space), `Integer.valueOf("")` (empty), `Double.valueOf("1,000")` (comma). Handling exceptions is taught later in the module.

**Cyber security link:** never trust text to be a valid number. Every program that reads input must expect bad data. Crashing on `"42.4x"` is the mildest outcome; unchecked input is a root cause of many real vulnerabilities.

## 6. Constants

A **named constant** is a memory location whose value **cannot change** while the program runs. Declare it with the reserved word `final` and give it its value straight away:

```java
final datatype CONSTANT_NAME = value;
```

```java
final double CENTIMETERS_PER_INCH = 2.54;
final int NO_OF_STUDENTS = 40;
final char BLANK = ' ';
final double PAY_RATE = 15.75;
```

**Naming convention:** constants use **UPPER\_CASE with underscores**, so anyone reading the code knows at once it never changes.

Trying to change one is a compile error:

```text
error: cannot assign a value to final variable NO_OF_STUDENTS
```

**Why use constants?** Readability and easy maintenance.

```java
final int NO_OF_STUDENTS = 40;
int totalModuleMarks;
int averageMark;
averageMark = totalModuleMarks / NO_OF_STUDENTS;
```

`totalModuleMarks / NO_OF_STUDENTS` explains itself; `totalModuleMarks / 40` does not. If the class grows to 45, you change **one** line instead of hunting for every 40 (and risking changing a 40 that meant something else).

(The slide declares `totalModuleMarks` without a value. In a real program you must assign it before the division, or it will not compile.)

## 7. Worked programs

### Program A — a constant in a conversion

```java
public class InchConverter {
    public static void main(String[] args) {
        final double CENTIMETERS_PER_INCH = 2.54;   // never changes
        int inches = 70;
        double centimetres = inches * CENTIMETERS_PER_INCH;
        System.out.println(inches + " inches = " + centimetres + " cm");
    }
}
```

**Expected output (verified):**

```text
70 inches = 177.8 cm
```

| Line | What happens |
| --- | --- |
| `final double CENTIMETERS_PER_INCH = 2.54;` | Creates a constant; any later `CENTIMETERS_PER_INCH = ...` is a compile error |
| `int inches = 70;` | Declares and initialises a normal variable |
| `inches * CENTIMETERS_PER_INCH` | `int` × `double`: 70 is promoted to 70.0; result 177.8 |
| `println(...)` | Joins text and numbers left to right (a String comes second, so no adding happens) |

### Program B — text to numbers

```java
public class PriceFromText {
    public static void main(String[] args) {
        String priceText = "19.99";
        String qtyText = "3";

        double price = Double.valueOf(priceText);   // text -> double
        int qty = Integer.valueOf(qtyText);          // text -> int

        System.out.println("Joined: " + priceText + qtyText);
        System.out.println("Total: " + price * qty);
    }
}
```

**Expected output (verified):**

```text
Joined: 19.993
Total: 59.97
```

The first line shows what happens with the text: it is joined, not multiplied. After `valueOf`, the numbers can be used in arithmetic. In `"Total: " + price * qty`, `*` is done before `+`, so the multiplication happens first.

**Modify it:** change `qtyText` to `"three"`. It still compiles, but running it gives `NumberFormatException: For input string: "three"`.

### Program C — debugging step by step

The slides show a program called `ProgramNum` with two compiler errors. The slide code itself is an image, so this is a similar program built to produce the same two errors:

```java
public class ProgramNum
{
    public static void main(String[] args)
    {
        final int SECRET = 7;

        // declare a variable to hold a number
        int num
        num = 25;

        System.out.println("num is " + num);
        System.out.println("num times SECRET is " + num * SECRET);

    }
```

```text
ProgramNum.java:8: error: ';' expected
        int num
               ^
ProgramNum.java:14: error: reached end of file while parsing
    }
     ^
2 errors
```

**How to work through it:**

1. **Don’t panic.** Two errors can come from two small typos.
2. **Start with the first error.** One mistake can cause later “fake” errors, so fix from the top and recompile.
3. **Read the message and line number:** line 8, `';' expected`. The `^` points to where Java expected it: right after `int num`. Add the `;`.
4. **Second error, line 14:** “reached end of file while parsing” means Java ran out of code while still inside an open `{`. Count the braces: two `{`, only one `}`. Add the closing brace for the class.
5. **Recompile.** Expected output after both fixes:

```text
num is 25
num times SECRET is 175
```

### Good programming style (from the slides)

- Remember the common syntax rules: semicolons end statements, commas separate items, braces come in pairs.
- Use blank lines and indentation so the structure is visible.
- Use the red underlines Eclipse gives you; hover to read the message.
- Follow the naming conventions: `lowerCamelCase` for variables, `UpperCamelCase` for classes, `UPPER_CASE` for constants.

## 8. Common mistakes

All messages below are from `javac` or the Java runtime (Java 21). Eclipse words compile errors differently but flags the same lines.

| Mistake | Example | What happens | Fix |
| --- | --- | --- | --- |
| `double` result into an `int` | `int area = length * width;` | Compile error: possible lossy conversion from double to int | Make it `double`, or cast `(int)` if cutting is intended |
| Doing maths with a String | `String s = "42"; int n = s + 1;` | Compile error: String cannot be converted to int | `int n = Integer.valueOf(s) + 1;` |
| Storing a number in a String variable | `int n = 42; String s = n;` | Compile error: int cannot be converted to String | `String s = "" + n;` or `String.valueOf(n)` |
| Expecting `"42.45" + 10` to add | `numString + 10` | Runs, gives `42.4510` (logic error) | Convert first: `Double.valueOf(numString) + 10` |
| Converting text that is not a number | `Double.valueOf("42.4x")` | Runtime: NumberFormatException | Make sure the text is a valid number (handling comes later) |
| Decimal text into `Integer` | `Integer.valueOf("42.5")` | Runtime: NumberFormatException | Use `Double.valueOf` |
| Assuming `Boolean.valueOf` checks input | `Boolean.valueOf("yes")` | Quietly gives `false` | Only `"true"` (any case) gives `true` |
| Changing a constant | `final int MAX = 5; MAX = 6;` | Compile error: cannot assign a value to final variable MAX | Use a normal variable if it must change |
| Lower-case constant name | `final int max = 5;` | Compiles, but breaks the convention | `MAX` |
| Thinking `num2 = num1` links them | `num2 = num1; num1 = 0;` | `num2` keeps the old value | Assignment copies a value at that moment |
| Fixing the last error first | — | Later errors may be side-effects of the first | Fix from the top, recompile |
| Curly quotes copied from slides | `“Area is: ”` | Compile error (illegal character) | Retype with straight quotes `"` |

## Check yourself: 15 multiple-choice questions

Allow **15 minutes**, no Eclipse. Practice questions written for this module, not real test questions.

1. After `int a = 10; a = a + 5; int b = a; a = 0;` what is `b`? (A) 0 (B) 10 (C) 15 (D) compile error
2. Which line declares a constant correctly? (A) `final int MAX_USERS = 50;` (B) `int final MAX_USERS = 50;` (C) `constant int MAX_USERS = 50;` (D) `final MAX_USERS = 50;`
3. What is the wrapper class for `int`? (A) `Int` (B) `Integer` (C) `Number` (D) `int`
4. What does `System.out.println("42.45" + 10);` print? (A) `52.45` (B) `42.4510` (C) `52` (D) compile error
5. What does `System.out.println(Double.valueOf("42.45") + 10);` print? (A) `52.45` (B) `42.4510` (C) `52` (D) runtime error
6. What happens with `int n = Integer.valueOf("4x");`? (A) compile error (B) `n` is 4 (C) compiles, then NumberFormatException when run (D) `n` is 0
7. What is `Boolean.valueOf("yes")`? (A) `true` (B) `false` (C) NumberFormatException (D) compile error
8. `Integer x = 33;` is an example of: (A) casting (B) unboxing (C) boxing (D) concatenation
9. What happens with `final double RATE = 0.2; RATE = 0.25;`? (A) `RATE` becomes 0.25 (B) compile error (C) runtime error (D) `RATE` stays 0.2 with a warning
10. After `int num1 = 18; num1 = num1 + 27; int num3 = num1 / 5 / 4;` what is `num3`? (A) 2.25 (B) 2 (C) 9 (D) 45
11. What does `double sale = 0.02 * 1000; System.out.println(sale);` print? (A) `20` (B) `20.0` (C) `0.02` (D) compile error
12. Which line does **not** compile? (A) `double d = 23.5 * 14.7;` (B) `int area = 23.5 * 14.7;` (C) `int area = (int) (23.5 * 14.7);` (D) `double d = 7;`
13. Which name follows the convention for a constant? (A) `noOfStudents` (B) `NoOfStudents` (C) `NO_OF_STUDENTS` (D) `no_of_students`
14. The compiler says `reached end of file while parsing`. The most likely cause is: (A) a missing semicolon (B) a missing closing brace `}` (C) a misspelt variable (D) a wrong data type
15. What does `System.out.println(Integer.valueOf("7") + Integer.valueOf("3") + "1");` print? (A) `731` (B) `11` (C) `101` (D) `10`

### Answers and explanations

| Q | Answer | Why |
| --- | --- | --- |
| 1 | C | `b` copied the value 15; changing `a` later does not affect it |
| 2 | A | `final`, type, UPPER\_CASE name, value |
| 3 | B | `int` → `Integer` (and `char` → `Character`) |
| 4 | B | A String on the left, so `+` joins |
| 5 | A | Converted to a `double` first, so `+` adds |
| 6 | C | The code is valid; the text is checked only when it runs |
| 7 | B | Only "true" (any case) gives `true`; no exception |
| 8 | C | Primitive → wrapper object is boxing |
| 9 | B | `final` variables cannot be reassigned |
| 10 | B | 45 / 5 = 9, 9 / 4 = 2 (integer division) |
| 11 | B | A `double` always prints with a decimal point |
| 12 | B | A `double` cannot go into an `int` without a cast |
| 13 | C | Constants: UPPER\_CASE with underscores |
| 14 | B | Java ran out of code while a `{` was still open |
| 15 | C | 7 + 3 = 10 (both numbers), then joined with "1" |

All answers were checked by running the code with Java 21. **Score:** 13–15 go to Lab 3; 10–12 re-read the sections for the ones you missed; under 10, rework the trace tables first.

## Quick reference and glossary

```java
// Assignment: right side first, then stored on the left
num1 = num1 + 27;
num2 = num1;                       // copies the value

// Constants
final int NO_OF_STUDENTS = 40;     // UPPER_CASE, value set once

// Text -> number (wrapper classes)
int i     = Integer.valueOf("42");
double d  = Double.valueOf("42.45");
boolean b = Boolean.valueOf("true");
// Integer.parseInt / Double.parseDouble do the same job

// Boxing and unboxing
Integer boxed = 33;    // int -> Integer
int plain = boxed;     // Integer -> int

// double -> int needs a cast (decimal is cut off)
int area = (int) (length * width);
```

| Term | Meaning |
| --- | --- |
| Assignment statement | `variable = expression;` — evaluate the right, store on the left |
| Initialise | Give a variable its first value |
| State | The values all variables hold at one moment |
| Floating-point value | A number with a decimal part, stored as `double` (or `float`) |
| Object | A value made from a class, with its own methods; `String` is one |
| Wrapper class | Object version of a primitive: `Integer`, `Double`, `Character`, `Boolean`, ... |
| Boxing / unboxing | Automatic primitive → wrapper / wrapper → primitive conversion |
| Parsing | Reading a value out of text, e.g. `Double.valueOf("42.45")` |
| Exception | A runtime error object; Java’s way of saying something went wrong. Unhandled, it stops the program |
| NumberFormatException | Thrown when text cannot be converted to a number |
| Named constant | A `final` variable whose value cannot change after it is set |
| `final` | Reserved word that makes a variable constant |
| Syntax error | Breaking Java’s grammar rules; found by the compiler |

**Next:** work through Lab 3.
