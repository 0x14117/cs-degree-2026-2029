# Lecture 2 — Variables \#1: Data Types, Operators and Strings

**Module:** 4300COMP Introduction to Programming · **Language:** Java

## Overview

Lecture 2 teaches you how a program **stores values** (variables and data types) and **calculates with them** (operators and expressions). These notes rewrite the official Lecture 2 slides in plain English and add worked examples. Every output shown was run with Java 21.

**By the end you should be able to:**

1.  Name the parts of a Java statement: special symbols, reserved words and identifiers.

2.  Tell a legal identifier from an illegal one.

3.  Choose the right primitive type: `int`, `double`, `char` or `boolean`.

4.  Declare a variable, assign a value to it and change that value.

5.  Work out an arithmetic expression the way Java does, including precedence, integer division and `%`.

6.  Predict the result of a mixed `int`/`double` expression and use a cast.

7.  Use `String` and explain when `+` adds and when it joins.

**Learning outcome:** MLO1 (apply programming constructs). The supplied module information links MLO1 to the in-class multiple-choice test, so the Check yourself questions are good practice. None of them is a real test question.

**Matching lab:** Lab 2 (official Tutorial 2: Variables \#1).

**What you need from Lecture 1:** a class, `main`, `System.out.println`, and that statements run top to bottom.

## Parts of a Java program

A Java program is a collection of **classes**. Each class is wrapped in `{ }`. A runnable program has one `main` method, which is where it starts. Inside `main` are **statements**, and each statement is built from small pieces called **tokens**.

A **token** is the smallest piece of code that means something to the compiler. There are three kinds.

| Kind of token           | What it is                                                                           | Examples                                                                          |
|-------------------------|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| Special symbol          | Punctuation and operators with a fixed meaning                                       | `+ - * / %` · `. ; ,` · `< <= > >= == !=` · `=` (assignment)                      |
| Reserved word (keyword) | Words Java owns; you cannot use them as names. Eclipse shows them in purple and bold | `int`, `double`, `char`, `boolean`, `void`, `public`, `static`, `class`, `return` |
| Identifier              | Names **you** choose for variables, methods and classes                              | `sum`, `integer1`, `payRate`, `HelloWorldApp`                                     |

**Example: splitting a statement into tokens**

``` java
int sum = integer1 + integer2;
```

| Token      | Kind                              |
|------------|-----------------------------------|
| `int`      | reserved word                     |
| `sum`      | identifier                        |
| `=`        | special symbol (assignment)       |
| `integer1` | identifier                        |
| `+`        | special symbol (addition)         |
| `integer2` | identifier                        |
| `;`        | special symbol (end of statement) |

### Rules for identifiers

An identifier can contain **letters, digits, the underscore `_` and the dollar sign `$`**. It must **not start with a digit**, it cannot contain spaces, and it cannot be a reserved word. Identifiers are **case-sensitive**: `total`, `Total` and `TOTAL` are three different names.

| Identifier   | Legal? | Why                                        |
|--------------|--------|--------------------------------------------|
| `First`      | Yes    | Letters only                               |
| `payRate`    | Yes    | Letters only                               |
| `count2`     | Yes    | Digit is allowed after the first character |
| `$Amount`    | Yes    | May start with `$`                         |
| `_total`     | Yes    | May start with `_`                         |
| `2place`     | No     | Starts with a digit                        |
| `pass grade` | No     | Contains a space                           |
| `void`       | No     | Reserved word                              |
| `hello!`     | No     | `!` is not allowed                         |
| `my-name`    | No     | `-` is the minus operator                  |

The slides show `int void;`, `boolean 2place;` and `char pass grade;` as invalid declarations for exactly these reasons.

**Naming conventions** (not enforced by the compiler, but expected by markers): variables use **lowerCamelCase** (`numPasses`, `feesPaid`); classes use **UpperCamelCase** (`HelloWorldApp`). Choose names that say what the value means: `sum` beats `s`.

### Comments (revision)

`//` starts a single-line comment. `/* ... */` wraps a multi-line comment. The compiler throws comments away; they are for people.

## Data types

A **data type** is a set of values plus the operations you can do on them. The type tells Java how much memory to reserve and what the bits mean. Java’s basic built-in types are called **primitive types**. The slides group them into three families.

| Family         | Types                                  | Holds                                 | The one you will use most |
|----------------|----------------------------------------|---------------------------------------|---------------------------|
| Integral       | `byte`, `short`, `int`, `long`, `char` | Whole numbers (and single characters) | `int`                     |
| Floating-point | `float`, `double`                      | Numbers with a decimal part           | `double`                  |
| Boolean        | `boolean`                              | `true` or `false` only                | `boolean`                 |

### The four you need now

| Type      | Example values                    | Size                                             | Use it for                                    |
|-----------|-----------------------------------|--------------------------------------------------|-----------------------------------------------|
| `int`     | `0`, `42`, `-67`, `2000000`       | 32 bits (about ±2.1 billion)                     | Counts, ages, scores, number of failed logins |
| `double`  | `12.34`, `25.6`, `-0.5`, `3.0`    | 64 bits                                          | Prices, averages, measurements                |
| `char`    | `'a'`, `'A'`, `'5'`, `'*'`, `' '` | 16 bits                                          | One single character, in **single** quotes    |
| `boolean` | `true`, `false`                   | The slides describe it as one bit of information | Yes/no facts: `feesPaid`, `isLocked`          |

The others exist for special cases: `byte`, `short` and `long` are smaller or bigger whole-number types; `float` is a less precise decimal type (32 bits).

**Key points**

- `'5'` (a `char`) and `5` (an `int`) are different things. The first is a symbol on the keyboard; the second is a number you can do maths with.

- A `char` holds **exactly one** character. `'AB'` is an error.

- `true` and `false` are not text: no quotes.

- `String` (text such as `"Hello"`) is **not** a primitive type. It is a class; see the String section.

**Cyber security link:** choosing the wrong type causes real bugs. A whole-number type has a maximum value; going past it makes the number wrap round to a negative value (called *overflow*). Overflow bugs have caused real security vulnerabilities. You do not need the details yet; just remember that types have limits.

## Variables

A **variable** is a named location in memory that holds one value of one type. Think of a labelled box: the **label** is the name, the **shape of the box** is the type, and **what is inside** is the value. Technically, declaring a variable reserves memory of the right size and links your name to it.

Every variable has three things:

| Part  | Example     | Can it change?                              |
|-------|-------------|---------------------------------------------|
| Type  | `int`       | No — fixed when declared                    |
| Name  | `numPasses` | No                                          |
| Value | `42`        | Yes — that is why it is called a *variable* |

### 1. Declaring

To make a variable you state its **type** and its **name**:

``` java
int numPasses;
boolean feesPaid;
char grade;
```

You can declare several of the same type in one statement: `int integer1, integer2, sum;`

### 2. Assigning

The `=` sign is the **assignment operator**. It means “store the value on the right into the variable on the left”. It is **not** “equals” in the maths sense.

``` java
grade = 'B';
```

Read it aloud as “`grade` **becomes** `'B'`”. The right side is always worked out first, then stored.

### 3. Declaring and assigning together (initialising)

``` java
int numPasses = 42;
boolean feesPaid = false;
```

Giving a variable its first value is called **initialising** it. Java will not let you read a variable that has never been given a value (error: *variable might not have been initialized*).

### 4. Reassigning: the value can change

This is the slide’s “What happens here?” example.

``` java
char grade;
grade = 'B';
System.out.println(grade);
grade = 'A';
System.out.println(grade);
```

| Step | Statement         | Value of `grade`      | Output |
|------|-------------------|-----------------------|--------|
| 1    | `char grade;`     | (no value yet)        |        |
| 2    | `grade = 'B';`    | `'B'`                 |        |
| 3    | `println(grade);` | `'B'`                 | `B`    |
| 4    | `grade = 'A';`    | `'A'` (the B is gone) |        |
| 5    | `println(grade);` | `'A'`                 | `A`    |

A variable holds **one value at a time**. A new assignment overwrites the old value completely.

### 5. Using a variable in its own update

``` java
int a = 5;
a = a + 3;
a = a * 2;
System.out.println(a);
```

| Step         | Right side worked out | New value of `a` |
|--------------|-----------------------|------------------|
| `int a = 5;` | 5                     | 5                |
| `a = a + 3;` | 5 + 3 = 8             | 8                |
| `a = a * 2;` | 8 × 2 = 16            | 16               |

Output: `16`. In maths `a = a + 3` is impossible; in Java it means “take the current `a`, add 3, store the result back in `a`”.

### Literals (constants)

A **literal** is a value written directly in the code. In `integer1 = 10;` the `10` is a literal.

| Kind                   | Examples         |
|------------------------|------------------|
| Integer literal        | `23`, `-67`, `0` |
| Floating-point literal | `12.34`, `25.60` |
| Character literal      | `'a'`, `'5'`     |
| Boolean literal        | `true`, `false`  |
| String literal         | `"Hello World!"` |

For now we **hard-code** literals into variables. From the next lecture you will read values typed by the user instead.

## Arithmetic operators and precedence

Java has five arithmetic operators.

| Operator | Meaning           | Example | Result               |
|----------|-------------------|---------|----------------------|
| `+`      | addition          | `7 + 2` | `9`                  |
| `-`      | subtraction       | `7 - 2` | `5`                  |
| `*`      | multiplication    | `7 * 2` | `14`                 |
| `/`      | division          | `7 / 2` | `3` (whole numbers!) |
| `%`      | remainder (“mod”) | `7 % 2` | `1`                  |

Java needs `*` for multiplication. In algebra `ab` means a × b; in Java `ab` is just one identifier called `ab`.

A **binary** operator has two operands (`a - b`). A **unary** operator has one: the `-` in `-5` or the `+` in `+5`.

### Integer division and remainder

When **both** numbers are `int`, `/` gives a whole-number answer and **throws away** the decimal part. It does not round.

| Expression | Result | Why                                                              |
|------------|--------|------------------------------------------------------------------|
| `17 / 5`   | `3`    | 5 goes into 17 three times; the 0.4 is dropped                   |
| `17 % 5`   | `2`    | 17 − (3 × 5) = 2 left over                                       |
| `17.0 / 5` | `3.4`  | one operand is a `double`, so a decimal answer                   |
| `7 % 10`   | `7`    | 10 goes in 0 times; 7 left over                                  |
| `-7 / 2`   | `-3`   | the decimal part is dropped towards zero, not rounded down to −4 |
| `-7 % 3`   | `-1`   | the remainder takes the sign of the left number                  |

Useful `%` patterns: `n % 2` is `0` for even numbers and `1` for odd positive numbers; `n % 10` gives the last digit of a positive number.

### Order of precedence

Java follows the same idea as BODMAS:

1.  Brackets `( )` first, innermost first.

2.  `*`, `/` and `%` next — they have **equal** precedence, so they are done **left to right**.

3.  `+` and `-` last — equal precedence, **left to right**.

**Worked example 1:** `2 + 3 * 5`

| Step | Operation                     | Expression now |
|------|-------------------------------|----------------|
| 1    | `3 * 5` = 15 (`*` before `+`) | `2 + 15`       |
| 2    | `2 + 15` = 17                 | `17`           |

With brackets, `(2 + 3) * 5` gives `25`.

**Worked example 2:** `20 - 6 / 2 + 1`

| Step | Operation                     | Expression now |
|------|-------------------------------|----------------|
| 1    | `6 / 2` = 3                   | `20 - 3 + 1`   |
| 2    | `20 - 3` = 17 (left to right) | `17 + 1`       |
| 3    | `17 + 1` = 18                 | `18`           |

**Worked example 3 — left to right matters:** `10 / 4 * 2` versus `10 * 2 / 4`

| Expression   | Step 1                          | Step 2   | Result |
|--------------|---------------------------------|----------|--------|
| `10 / 4 * 2` | `10 / 4` = 2 (integer division) | `2 * 2`  | `4`    |
| `10 * 2 / 4` | `10 * 2` = 20                   | `20 / 4` | `5`    |

In maths both would be 5. In Java the order changes the answer, because integer division loses the 0.5 early.

**Worked example 4:** `8 % 3 * 2 + 1`

| Step | Operation                               | Expression now |
|------|-----------------------------------------|----------------|
| 1    | `8 % 3` = 2 (`%` and `*` left to right) | `2 * 2 + 1`    |
| 2    | `2 * 2` = 4                             | `4 + 1`        |
| 3    | `4 + 1` = 5                             | `5`            |

**Brackets for averages (from Tutorial 2):** the average of five numbers is `(a + b + c + d + e) / 5`. Without brackets, `a + b + c + d + e / 5` divides only `e` by 5.

### Integral and floating-point expressions

- **Integral expression:** every operand is a whole number, e.g. `2 + 3 * 5`. The result is an `int`.

- **Floating-point expression:** every operand is a decimal, e.g. `12.8 * 17.5 - 34.50`. The result is a `double`.

## Mixed expressions, promotion and casting

A **mixed expression** has operands of different types, such as an `int` and a `double`.

**The rule:** Java works one operator at a time, following precedence. For each operator: if both sides are `int`, the result is `int`; if either side is `double`, the `int` is **promoted** (converted) to `double` first and the result is `double`. This automatic conversion is called **implicit type coercion** or **promotion**.

| Expression      | Working                                         | Result |
|-----------------|-------------------------------------------------|--------|
| `2 + 3.5`       | `2` promoted to `2.0`; 2.0 + 3.5                | `5.5`  |
| `6 / 4 + 3.9`   | `6 / 4` first: both `int`, so `1`; then 1 + 3.9 | `4.9`  |
| `6.0 / 4 + 3.9` | `6.0 / 4` = 1.5; then 1.5 + 3.9                 | `5.4`  |
| `1 / 2 * 10.0`  | `1 / 2` = `0` (int); 0 × 10.0                   | `0.0`  |

The second and fourth rows are classic test traps: the integer division happens **before** the `double` is ever involved.

### Storing in a variable

- An `int` value can go straight into a `double` variable: `double d = 7;` stores `7.0`.

- A `double` **cannot** go into an `int` variable without permission, because the decimal part would be lost. `int x = 7.9;` is a compile error: *incompatible types: possible lossy conversion from double to int*.

- Watch the right side: `double avg = (125 + 28 + -25) / 3;` stores `42.0`, not `42.666...`. The division is all `int`, so it gives `42`, and only then is it stored as a `double`.

### Casting: explicit type conversion

A **cast** tells Java “convert this to that type, I accept any data loss”.

``` java
(dataTypeName) expression
```

Casting a `double` to `int` **cuts off** the decimal part (towards zero). It does not round.

| Expression                | Working                               | Result |
|---------------------------|---------------------------------------|--------|
| `(int)(7.9 + 6.7)`        | brackets first: 14.6; cast cuts to 14 | `14`   |
| `(int)(7.9) + (int)(6.7)` | 7 + 6                                 | `13`   |
| `(int) -3.7`              | cut towards zero                      | `-3`   |
| `(double) 7 / 2`          | cast happens first: 7.0 / 2           | `3.5`  |
| `(double)(7 / 2)`         | brackets first: 7 / 2 = 3; then 3.0   | `3.0`  |

The first two rows are the slide examples. The last two show **where** you put the cast matters: cast *before* dividing to keep the decimal.

**Practical use:** to get a true average of `int` values, write `(double)(a + b + c) / 3`.

## The String type and the + operator

A `char` holds one character. To hold text of any length, Java uses **`String`**.

- A String is a **sequence of zero or more characters** in **double** quotes: `"Hello World!"`.

- `""` is the **empty string**: zero characters.

- `"123"` is a **numeric string**: it looks like a number but it is text. You cannot do maths with it directly.

- Each character has a **position** (index), and positions **start at 0**. The **length** is the number of characters.

| Index     | 0   | 1   | 2   | 3   | 4   |
|-----------|-----|-----|-----|-----|-----|
| `"Hello"` | H   | e   | l   | l   | o   |

`"Hello"` has length 5, but its last index is 4.

`String` starts with a capital S because it is a **class**, not a primitive type. You declare it just like other variables:

``` java
String name = "Sam";
String module = "4300COMP";
```

### + adds numbers, + joins Strings

The `+` operator does two different jobs:

- Number `+` number → **addition**.

- If **either side is a String** → **concatenation** (joining). The other side is turned into text.

Java still works **left to right**, one `+` at a time. This is the slide example:

``` java
str = "The sum = " + 12 + 26;
```

| Step | Operation                                   | Result so far      |
|------|---------------------------------------------|--------------------|
| 1    | `"The sum = " + 12` → String + int = join   | `"The sum = 12"`   |
| 2    | `"The sum = 12" + 26` → String + int = join | `"The sum = 1226"` |

With brackets, the numbers are added first:

``` java
str = "The sum = " + (12 + 26);
```

| Step | Operation                                     | Result so far    |
|------|-----------------------------------------------|------------------|
| 1    | `(12 + 26)` → brackets first, int + int = add | `38`             |
| 2    | `"The sum = " + 38` → join                    | `"The sum = 38"` |

The same works with variables: `"The sum = " + (num1 + num2)`.

**Numbers first:** `12 + 26 + " is the sum"` gives `"38 is the sum"`, because the first `+` sees two `int`s and adds them before any String appears.

**Watch out for `char`:** a `char` is stored as a number, so `5 + 'A'` gives `70` and `'A' + 'B'` gives `131`. Only once a String is involved does it join: `"" + 5 + 'A'` gives `"5A"`. You will rarely need this, but it is a favourite in predict-the-output questions.

**Cyber security link:** text from users always arrives as a String, even if it looks like a number. A program that mixes up `"123"` and `123` can make wrong decisions, for example in a PIN or quantity check. Converting text safely to numbers comes later in the module, once user input is taught (the Tutorial 2 supplementary task previews it).

## Worked program: adding two integers

This is the program from the slides and from Tutorial 2. The slides build it in five steps.

1.  **Plan:** decide what variables you need, their types and meaningful names.

2.  **Declare** three `int` variables.

3.  **Assign** values to them.

4.  **Calculate** the sum and store it.

5.  **Print** the result as a String joined with the value of `sum`.

``` java
public class MyJavaProgram
{
    public static void main(String[] args)
    {
        int integer1;                 // step 2: declare
        int integer2;
        int sum;

        integer1 = 10;                // step 3: assign
        integer2 = 20;
        sum = integer1 + integer2;    // step 4: calculate

        System.out.println("The sum value is: " + sum);   // step 5: print
    }
}
```

**Expected output** (verified by running it):

``` text
The sum value is: 30
```

### Line by line

| Line                                              | What it does                                                                         |
|---------------------------------------------------|--------------------------------------------------------------------------------------|
| `int integer1;`                                   | Reserves memory for a whole number and names it `integer1`. No value yet.            |
| `int integer2;` / `int sum;`                      | Same for two more variables. Could be one line: `int integer1, integer2, sum;`       |
| `integer1 = 10;`                                  | Stores the literal `10` in `integer1`.                                               |
| `integer2 = 20;`                                  | Stores `20` in `integer2`.                                                           |
| `sum = integer1 + integer2;`                      | Reads both values (10 and 20), adds them, stores `30` in `sum`.                      |
| `System.out.println("The sum value is: " + sum);` | Joins the text and the value of `sum` into `"The sum value is: 30"`, then prints it. |

The braces here sit on their own lines (Allman style). Eclipse puts the `{` at the end of the line instead. Both are valid Java; just be consistent.

### Memory trace

| After statement              | `integer1` | `integer2` | `sum` |
|------------------------------|------------|------------|-------|
| declarations                 | –          | –          | –     |
| `integer1 = 10;`             | 10         | –          | –     |
| `integer2 = 20;`             | 10         | 20         | –     |
| `sum = integer1 + integer2;` | 10         | 20         | 30    |

### Change one thing

| Change                                    | New output               | Why                                                                                                 |
|-------------------------------------------|--------------------------|-----------------------------------------------------------------------------------------------------|
| `integer1 = 15;`                          | `The sum value is: 35`   | `sum` is calculated from the current values                                                         |
| Print with `"... " + integer1 + integer2` | `The sum value is: 1020` | String first, so `+` joins                                                                          |
| Move `sum = ...` above `integer1 = 10;`   | Compile error            | `integer1` would be read before it has a value: *variable integer1 might not have been initialized* |
| `sum = integer1 / integer2;`              | `The sum value is: 0`    | 10 / 20 is integer division                                                                         |

Official Tutorial 2, Task 1 asks you to extend this program with the other operators; Lab 2 walks you through it.

## Common mistakes

| Mistake                                   | Example                         | What happens                                                            | Correct version                             |
|-------------------------------------------|---------------------------------|-------------------------------------------------------------------------|---------------------------------------------|
| Using a variable before giving it a value | `int a; System.out.println(a);` | Compile error: *variable a might not have been initialized*             | `int a = 0;`                                |
| Putting a `double` into an `int`          | `int x = 7.9;`                  | Compile error: *possible lossy conversion from double to int*           | `double x = 7.9;` or `int x = (int) 7.9;`   |
| Expecting a decimal from `int / int`      | `double avg = 7 / 2;`           | Runs, but stores `3.0` (logic error)                                    | `double avg = 7.0 / 2;` or `(double) 7 / 2` |
| Forgetting brackets in an average         | `a + b + c / 3`                 | Only `c` is divided (logic error)                                       | `(a + b + c) / 3`                           |
| Forgetting brackets when printing a sum   | `"Sum: " + a + b`               | Joins: `Sum: 1020`                                                      | `"Sum: " + (a + b)`                         |
| Double quotes for a `char`                | `char c = "A";`                 | Compile error: *incompatible types: String cannot be converted to char* | `char c = 'A';`                             |
| Single quotes for a String                | `String s = 'Hi';`              | Compile error: *unclosed character literal*                             | `String s = "Hi";`                          |
| Small s on String                         | `string name;`                  | Compile error: *cannot find symbol*                                     | `String name;`                              |
| Wrong case on a variable name             | Declared `count`, used `Count`  | Compile error: *cannot find symbol*                                     | Use exactly the declared name               |
| Declaring the same name twice             | `int x = 1; int x = 2;`         | Compile error: *variable x is already defined*                          | Second time: `x = 2;`                       |
| Reading `=` as “equals”                   | `10 = x;`                       | Compile error: “unexpected type” (the left side must be a variable)     | `x = 10;`                                   |
| Quotes round `true`                       | `boolean ok = "true";`          | Compile error: String cannot be converted to boolean                    | `boolean ok = true;`                        |

## Check yourself: 15 multiple-choice questions

Allow yourself **15 minutes**, no Eclipse. Write your answers down, then check. These are practice questions written for this module; they are not real test questions.

1.  Which is a **legal** identifier? (A) `2ndPlace` (B) `total_score` (C) `my score` (D) `class`

2.  Which is a **reserved word**? (A) `sum` (B) `Main` (C) `double` (D) `integer1`

3.  What does `System.out.println(14 / 4);` print? (A) `3.5` (B) `3` (C) `4` (D) `2`

4.  What does `System.out.println(14 % 4);` print? (A) `3` (B) `0` (C) `2` (D) `3.5`

5.  What is the value of `3 + 4 * 2 - 1`? (A) `13` (B) `10` (C) `12` (D) `7`

6.  What is the value of `(int)(9.99)`? (A) `10` (B) `9` (C) `9.0` (D) compile error

7.  What is the value of `5 / 2 + 1.5`? (A) `4.0` (B) `3.5` (C) `4` (D) `3`

8.  What does `System.out.println("Total: " + 4 + 5);` print? (A) `Total: 9` (B) `Total: 45` (C) `Total: 4 5` (D) compile error

9.  What does `System.out.println("Total: " + (4 + 5));` print? (A) `Total: 9` (B) `Total: 45` (C) `Total: (4 + 5)` (D) compile error

10. Which declaration causes a **compile error**? (A) `char c = 'x';` (B) `boolean ok = true;` (C) `int n = 3.5;` (D) `double d = 3;`

11. After `int x = 4; x = x * 3; x = x - 2;` what is `x`? (A) `4` (B) `12` (C) `10` (D) `2`

12. Which type best stores a single keyboard character such as `'#'`? (A) `String` (B) `char` (C) `int` (D) `boolean`

13. What does this print? `double r = 7 / 2; System.out.println(r);` (A) `3.5` (B) `3` (C) `3.0` (D) `4.0`

14. In Java, what does `=` do in `total = 10;`? (A) checks whether `total` equals 10 (B) stores 10 in `total` (C) declares `total` (D) prints 10

15. For `String s = "Cyber";` what are the length and the index of `'C'`? (A) 5 and 1 (B) 4 and 0 (C) 5 and 0 (D) 6 and 1

### Answers and explanations

| Q   | Answer | Why                                                                               |
|-----|--------|-----------------------------------------------------------------------------------|
| 1   | B      | A starts with a digit, C has a space, D is a reserved word                        |
| 2   | C      | `double` is a type keyword; `Main` is a legal name because Java is case-sensitive |
| 3   | B      | `int / int` drops the decimal: 14 / 4 = 3                                         |
| 4   | C      | 14 − (3 × 4) = 2                                                                  |
| 5   | B      | `4 * 2` = 8 first; 3 + 8 − 1 = 10                                                 |
| 6   | B      | Casting cuts off the decimal, it does not round                                   |
| 7   | B      | `5 / 2` = 2 (int), then 2 + 1.5 = 3.5                                             |
| 8   | B      | String first, so each `+` joins                                                   |
| 9   | A      | Brackets first: 4 + 5 = 9, then join                                              |
| 10  | C      | A `double` cannot go into an `int` without a cast                                 |
| 11  | C      | 4 → 12 → 10                                                                       |
| 12  | B      | `char` holds exactly one character                                                |
| 13  | C      | `7 / 2` = 3 (int), stored as `3.0`                                                |
| 14  | B      | `=` is assignment; comparison is `==`, covered later                              |
| 15  | C      | 5 characters; indexes start at 0                                                  |

All answers were checked by running the code with Java 21. **Score:** 13–15 move on to Lab 2; 10–12 re-read the sections for the ones you missed; under 10, go through the worked examples again before the lab.

## Quick reference and glossary

``` java
// Declare, assign, initialise
int count;                 // declare
count = 3;                 // assign
int total = 0;             // declare + initialise
double price = 9.99;
char grade = 'A';          // single quotes, one character
boolean locked = false;    // no quotes
String name = "Sam";      // double quotes, capital S

// Arithmetic
int q = 17 / 5;            // 3   (integer division)
int r = 17 % 5;            // 2   (remainder)
double d = 17.0 / 5;       // 3.4
double avg = (double)(a + b + c) / 3;   // true average
int whole = (int) 9.99;    // 9   (cut, not rounded)

// Printing
System.out.println("Sum: " + (a + b));  // brackets to add first
```

**Precedence:** brackets → `* / %` (left to right) → `+ -` (left to right).

**Promotion:** `int` op `int` → `int`; anything with a `double` → `double`, one operator at a time.

| Term                               | Meaning                                                                                        |
|------------------------------------|------------------------------------------------------------------------------------------------|
| Token                              | Smallest meaningful piece of code: special symbol, reserved word or identifier                 |
| Reserved word                      | Word owned by Java, e.g. `int`, `public`; cannot be a name                                     |
| Identifier                         | A name you choose; letters, digits, `_`, `$`; not starting with a digit                        |
| Data type                          | A set of values and the operations on them                                                     |
| Primitive type                     | Built-in basic type: `int`, `double`, `char`, `boolean` (and `byte`, `short`, `long`, `float`) |
| Variable                           | Named memory location holding one value of one type                                            |
| Declaration                        | Statement that creates a variable: `int x;`                                                    |
| Assignment                         | Storing a value with `=`: `x = 5;`                                                             |
| Initialisation                     | Giving a variable its first value                                                              |
| Literal                            | A value written directly in code: `10`, `2.5`, `'a'`, `"Hi"`                                   |
| Operand                            | A value an operator works on                                                                   |
| Unary / binary operator            | One operand (`-5`) / two operands (`a - b`)                                                    |
| Precedence                         | The order operators are applied                                                                |
| Integer division                   | `int / int`, decimal part discarded                                                            |
| Modulus `%`                        | Remainder after division                                                                       |
| Mixed expression                   | Operands of different types                                                                    |
| Implicit type coercion (promotion) | Java automatically converting `int` to `double` in a mixed expression                          |
| Cast                               | Explicit conversion: `(int) 7.9`                                                               |
| String                             | Class for text: a sequence of characters in double quotes                                      |
| Empty string                       | `""`, length 0                                                                                 |
| Concatenation                      | Joining Strings with `+`                                                                       |

**Next:** work through Lab 2.
