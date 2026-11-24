# Lecture 13 — String and char Types

**Module:** 4300COMP Introduction to Programming · **Language:** Java

## Overview

You have used `String` since Lecture 1 to store text, print messages and read files. Lecture 13 looks inside it: a `String` is a **sequence of `char` values**, numbered from 0, with **methods** for measuring, searching, cutting and changing case. You will learn why Strings must be compared with `equals`, what **immutable** means, how `char` relates to numbers, and how `StringBuffer` gives you text you *can* change. These notes rewrite the official Lecture 13 slides in plain English. Every program and output shown was compiled and run with Java 21 (javac on the command line, not Eclipse).

**By the end you should be able to:**

1. Explain what a `String` object is and draw the index of each character.
2. Use `length`, `charAt`, `indexOf`, `substring`, `toUpperCase` and `toLowerCase`, and predict their results.
3. Explain immutability, and reassign a variable to keep a changed String.
4. Compare Strings correctly with `equals`, `equalsIgnoreCase`, `startsWith`, `endsWith` and `contains`, and explain why `==` is wrong.
5. Use `char` values: literals, comparisons, arithmetic with their codes, casting back to `char`, and the `Character` helper methods.
6. Loop over the characters of a String.
7. Create and change a `StringBuffer` with `append`, `insert`, `replace` and `reverse`.

**Learning outcomes:** MLO1 (text-processing algorithms), MLO2 (reading the `String`, `Character` and `StringBuffer` API documentation), MLO3 (problems such as ciphers, validators and parsers).

**Matching lab:** Lab 13 (official Tutorial 13: String and char Types).

**What you need from earlier lectures:** `char` and casting (Lecture 2), `Scanner` `next` and `nextLine` (Lecture 4), `equals` (Lecture 6), `for` loops (Lecture 9), and indices from 0 (Lecture 11).

## 1. Why look at String again?

Text is everywhere in programs: values, messages, data read from and written to files. So far you have used String variables and printed String literals. Now you will use what String can do: pull out parts of the text (**substrings**) and single **characters**.

## 2. The String type

- `String` is an **object type**, not a primitive like `int`, `double`, `char` or `boolean`. That is why it has a capital S and why it has **methods**. (The slides say object types are covered in a later session.)
- A String stores text as a **sequence of individual characters**, each of type `char`.
- You can work with single characters or with groups of characters.

### Creating Strings

Unlike most objects, a String does **not** need `new`:

```java
String name = "Joe Bloggs";
int x = 3;
int y = 5;
String point = "(" + x + ", " + y + ")";    // (3, 5)
```

## 3. Indices: how a String is numbered

Characters are numbered from **0**, exactly like an array:

| Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `char` | J | o | e | (space) | B | l | o | g | g | s |

- The first character is at index **0**.
- The last character is at index **`length() - 1`**: here 9, because `"Joe Bloggs".length()` is 10.
- The **space is a character** too, and it has its own index.

## 4. String methods

| Method | What it gives you |
| --- | --- |
| `length()` | The number of characters |
| `charAt(i)` | The `char` at index `i` |
| `indexOf(str)` | The index where `str` first starts, or **−1** if it is not there |
| `substring(i1, i2)` | The characters from `i1` (**included**) up to `i2` (**not included**) |
| `substring(i1)` | From `i1` to the end |
| `toLowerCase()` / `toUpperCase()` | A **new** String in lower / upper case |

Methods are called with **dot notation**: `name.length()`. Note the brackets: `length()` is a method for Strings, whereas arrays use the field `length` without brackets (Lecture 11).

### Examples

The slides' examples use two people's names. These notes use different names with the same method calls. All results verified.

```java
// index        012345678901
String s1 = "Grace Hopper";
String s2 = "Ada Lovelace";
System.out.println(s1.length());               // 12
System.out.println(s1.indexOf("o"));           // 7
System.out.println(s1.substring(6, 9));        // Hop
String s3 = s2.substring(2, 8);
System.out.println(s3.toLowerCase());          // a love
```

`substring(6, 9)` takes indices 6, 7 and 8: the number of characters is `9 − 6 = 3`. `substring(2, 8)` of "Ada Lovelace" is "a Love" (6 characters, including the space).

From Tutorial 13: with `String name = "Joe Bloggs";`, `name.indexOf("B")` is 4 and `name.substring(3, 6)` is `" Bl"` (a space, B, l).

**The slides' two questions**, with `String msg = "Building Java Programs";`:

1. Extract `"Java"`: it starts at index 9 and is 4 long, so `msg.substring(9, 13)`.
2. Extract the first word of **any** String: everything before the first space, so `msg.substring(0, msg.indexOf(" "))` gives `"Building"`. (If the String has no space, `indexOf` returns −1 and `substring(0, -1)` crashes, so check first.)

Similarly, the last word is `msg.substring(msg.lastIndexOf(" ") + 1)`, which gives `"Programs"` (verified).

## 5. Strings are immutable

Methods such as `substring` and `toUpperCase` do **not** change the original String. They return a **new** one:

```java
String s = "Hello World";
s.toUpperCase();              // result thrown away
System.out.println(s);        // Hello World
s = s.toUpperCase();          // keep the result by reassigning
System.out.println(s);        // HELLO WORLD
```

Both outputs verified. String objects are **immutable**: no method can change (mutate) them. To "change" a String variable, assign the new String to it.

## 6. Strings and user input

`Scanner`'s `next()` reads one **word** as a String; `nextLine()` reads a whole **line** (Lecture 4).

```java
Scanner console = new Scanner(System.in);
System.out.print("What is your name? ");
String name = console.next();
name = name.toUpperCase();
System.out.println(name + " has " + name.length() + " letters and starts with " + name.substring(0, 1));
```

**Run (verified), input `Fred`:** `FRED has 4 letters and starts with F`

## 7. Comparing Strings

### Why == is wrong

Relational operators are for primitive types. With Strings:

- `<`, `>` and the others do not compile: `error: bad operand types for binary operator '<'` (verified).
- `==` **compiles**, but it checks whether the two variables refer to **the same object**, not whether the text is the same.

```java
String name = console.next();          // user types Fred
if (name == "Fred") {                  // false!
    System.out.println("Welcome " + name);
}
```

With input `Fred` typed at the keyboard, `name == "Fred"` is **false** and the message is not printed (verified).

**Why this trap is so confusing:** Java reuses identical String **literals** written in the code, so `"Fred" == "Fred"` can be `true` (verified). Tests with hard-coded values may seem to work, then the program fails with real input. **Always use `equals`.**

### The equals method and other test methods

```java
if (name.equals("Fred")) {
    System.out.println("Welcome " + name);   // printed when the user types Fred
}
```

| Method | `true` when… |
| --- | --- |
| `equals(str)` | Both contain exactly the same characters |
| `equalsIgnoreCase(str)` | Same characters, ignoring upper/lower case |
| `startsWith(str)` | This String begins with `str` |
| `endsWith(str)` | This String ends with `str` |
| `contains(str)` | `str` appears anywhere in this String |

```java
String name = console.nextLine();
if (name.startsWith("Dr")) {
    System.out.println("Can I have a sick-note?");
}
```

**Alphabetical order:** `a.compareTo(b)` returns a negative number if `a` comes before `b`, 0 if they are equal, and a positive number if `a` comes after. Upper-case letters all come before lower-case ones, so `"Zoo".compareTo("apple")` is negative (verified). (Not in the slides; useful for sorting.)

## 8. The char type

`char` is a **primitive type** for a **single character**. Every character inside a String is a `char`.

- `char` literals use **single quotes**: `'a'`, `'4'`, `'\n'` (newline), `'\''` (an apostrophe).
- `String` literals use **double quotes**: `"a"`.

```java
char letter = 'S';
System.out.println(letter);                  // S
char initial = 'J';
System.out.println(initial + " Bloggs");     // J Bloggs
```

### charAt: getting characters out of a String

```java
String name = "Fred";
char firstLetter = name.charAt(0);           // 'F'
System.out.println("First letter in name is " + firstLetter);

for (int i = 0; i < name.length(); i++) {    // visit every character
    char c = name.charAt(i);
    System.out.print(c);
}
```

**Output (verified):** `First letter in name is F`, then `Fred`.

`charAt` with an index of `length()` or more crashes: `StringIndexOutOfBoundsException: Index 4 out of bounds for length 4` (verified).

### char and int

Every `char` is stored as a **number** (its character code). The slides call these ASCII values. Java actually uses **Unicode** (UTF-16), whose first 128 codes are the same as ASCII, so for ordinary English letters, digits and symbols the numbers match.

| Character | Code |
| --- | --- |
| `'A'` | 65 |
| `'B'` | 66 |
| `' '` (space) | 32 |
| `'a'` | 97 |
| `'b'` | 98 |
| `'*'` | 42 |

Mixing `char` and `int` in arithmetic converts the `char` to its `int` code:

```java
System.out.println('a' + 10);          // 107
System.out.println('A' + 'A');         // 130
System.out.println((char) ('a' + 2));  // c
```

All verified. To turn a number back into a character, **cast** it with `(char)`. This is the basis of the Caesar cipher in Lab 13.

Watch out: `'a' + 'b'` is the **number** 195, but `"" + 'a' + 'b'` is the String `"ab"` (verified). As soon as a String is involved, `+` joins text.

### char versus String

| | `"h"` (String) | `'h'` (char) |
| --- | --- | --- |
| Type | Object type | Primitive type |
| Has methods? | Yes: `s.toUpperCase()`, `s.length()`, `s.charAt(0)` | **No** |
| Compare with | `equals` | `==`, `<`, `>` and so on |

Calling a method on a `char`, as in `c = c.toUpperCase();`, gives `error: char cannot be dereferenced` (verified). Use the **`Character`** helper class instead:

| Method | Result |
| --- | --- |
| `Character.toUpperCase(c)` / `toLowerCase(c)` | The changed `char` |
| `Character.isLetter(c)` | `true` for a letter |
| `Character.isDigit(c)` | `true` for 0–9 |
| `Character.isUpperCase(c)` / `isLowerCase(c)` | Case tests |
| `Character.isLetterOrDigit(c)` | Letter or digit |

(`Character` is the wrapper class for `char` from Lecture 3. Tutorial 15's example uses `isLetter` and `isDigit`.)

### Comparing char values

Unlike Strings, `char` values **can** be compared with relational operators, because they are numbers underneath: `'a' < 'b'`, `'X' == 'X'` and `'Q' != 'q'` are all `true`.

```java
for (char c = 'a'; c <= 'z'; c++) {           // prints the alphabet
    System.out.print(c);
}

String word = console.next();
if (word.charAt(word.length() - 1) == 's') {   // test the last character
    System.out.println(word + " is plural.");
}
```

## 9. StringBuffer: text you can change

A `StringBuffer` is like a String that **can** be modified: its length and content change through method calls. Unlike String, you must create it with `new`:

```java
StringBuffer hello = new StringBuffer("Hello World");
```

`StringBuffer hello = "Hello World";` does not compile: `error: incompatible types: String cannot be converted to StringBuffer` (verified).

| Method | Effect |
| --- | --- |
| `append(x)` | Adds `x` to the end |
| `insert(i, x)` | Inserts `x` at index `i` |
| `replace(i1, i2, str)` | Replaces the characters from `i1` to `i2` (exclusive) with `str` |
| `reverse()` | Reverses the characters |
| `toString()` | Gives an ordinary String with the current text |

```java
StringBuffer birthdayMsg = new StringBuffer("Happy Birthday");
birthdayMsg.insert(6, "40th ");
System.out.println(birthdayMsg);        // Happy 40th Birthday
birthdayMsg.append("!");                // Happy 40th Birthday!
birthdayMsg.replace(6, 10, "21st");     // Happy 21st Birthday!
```

All verified. Unlike String methods, these change the buffer itself, so no reassignment is needed.

**Slide note:** the slide's version of this example has two typing errors: the String `"Happy Birthday` is missing its closing quote (`error: unclosed string literal`), and it calls `someBuffer.insert` although the variable is named `birthdayMsg`. The version above fixes both.

**When to use it:** building up text bit by bit, for example in a loop. Each `+` on a String creates a whole new String; a `StringBuffer` changes in place. Java also has `StringBuilder`, which has the same methods; the next lecture mentions it.

## 10. Common mistakes

| Mistake | Symptom (verified) | Fix |
| --- | --- | --- |
| `if (name == "Fred")` | Compiles; false for typed input | `name.equals("Fred")` |
| `s.toUpperCase();` without assigning | String unchanged | `s = s.toUpperCase();` |
| `charAt(length())` | `StringIndexOutOfBoundsException: Index 4 out of bounds for length 4` | Last character is `charAt(length() - 1)` |
| `substring(3, 1)` (end before start) | `StringIndexOutOfBoundsException: Range [3, 1) out of bounds for length 4` | Start ≤ end ≤ length |
| Expecting `substring(a, b)` to include index `b` | One character short | The end index is exclusive |
| `c.toUpperCase()` on a `char` | `error: char cannot be dereferenced` | `Character.toUpperCase(c)` |
| `'ab'` or `'Fred'` | `error: unclosed character literal` | Single quotes hold one character; use `"..."` for text |
| `char c = s;` | `error: incompatible types: String cannot be converted to char` | `s.charAt(0)` |
| `StringBuffer b = "text";` | `error: incompatible types: String cannot be converted to StringBuffer` | `new StringBuffer("text")` |
| `"a" < "b"` | `error: bad operand types for binary operator '<'` | `compareTo` |
| `'a' + 'b'` expecting `"ab"` | Prints 195 | `"" + 'a' + 'b'` |
| `indexOf` result not checked | `-1` passed to `substring` crashes | Check for −1 first |

## 11. Check yourself — 15 multiple-choice questions

1. What is `"Joe Bloggs".length()`? (A) 9 (B) 10 (C) 11 (D) 8
2. What is `"Joe Bloggs".charAt(4)`? (A) `' '` (B) `'B'` (C) `'l'` (D) `'o'`
3. What is `"Grace Hopper".substring(6, 9)`? (A) `"Hopp"` (B) `"Hop"` (C) `" Ho"` (D) `"opp"`
4. What is `"Grace Hopper".indexOf("z")`? (A) 0 (B) 12 (C) −1 (D) an exception
5. After `String s = "Hello World"; s.toUpperCase();`, what does `System.out.println(s)` print? (A) `HELLO WORLD` (B) `Hello World` (C) `hello world` (D) nothing
6. Which correctly checks whether `name` holds `Fred`? (A) `name == "Fred"` (B) `name.equals("Fred")` (C) `name = "Fred"` (D) `name.equals('Fred')`
7. What is `'a' + 10`? (A) `'k'` (B) `"a10"` (C) 107 (D) 97
8. What is `(char) ('a' + 2)`? (A) `'c'` (B) 99 (C) `"a2"` (D) `'b'`
9. What happens with `char c = 'h'; c = c.toUpperCase();`? (A) `c` becomes `'H'` (B) `error: char cannot be dereferenced` (C) runtime error (D) `c` stays `'h'`
10. How do you extract the first word of any String `msg` that contains a space? (A) `msg.substring(0, msg.indexOf(" "))` (B) `msg.substring(msg.indexOf(" "))` (C) `msg.charAt(0)` (D) `msg.substring(0, 1)`
11. Which method checks the start of a String? (A) `contains` (B) `startsWith` (C) `indexOf` (D) `charAt`
12. Which line creates a `StringBuffer` correctly? (A) `StringBuffer b = "Hi";` (B) `StringBuffer b = new StringBuffer("Hi");` (C) `String b = new StringBuffer();` (D) `StringBuffer b = 'Hi';`
13. After `StringBuffer m = new StringBuffer("Happy Birthday"); m.insert(6, "40th ");`, what is `m`? (A) `Happy Birthday 40th` (B) `Happy 40th Birthday` (C) `40th Happy Birthday` (D) `Happy40th Birthday`
14. Which String methods change the original String object? (A) `toUpperCase` (B) `substring` (C) all of them (D) none of them
15. What is `"" + 'a' + 'b'`? (A) 195 (B) `"ab"` (C) `"195"` (D) a compile error

### Answers

| Q | Answer | Why |
| --- | --- | --- |
| 1 | B | Nine letters and a space (verified) |
| 2 | B | Index 3 is the space; 4 is B |
| 3 | B | Indices 6, 7, 8 (verified) |
| 4 | C | Not found |
| 5 | B | Strings are immutable; the result was not assigned (verified) |
| 6 | B | `==` compares objects; single quotes are for one `char` |
| 7 | C | `'a'` is 97 (verified) |
| 8 | A | 99 cast back to `char` (verified) |
| 9 | B | Primitives have no methods (verified) |
| 10 | A | Verified |
| 11 | B | |
| 12 | B | Verified |
| 13 | B | Verified |
| 14 | D | String is immutable; they all return new Strings |
| 15 | B | Joining to a String first (verified) |

**Score:** 13–15 go to Lab 13; 10–12 re-read the sections for the ones you missed; under 10, draw the index tables for "Joe Bloggs" and "Grace Hopper" and redo the examples by hand.

## 12. Quick reference

```java
String s = "Joe Bloggs";
s.length();                 // 10
s.charAt(0);                // 'J'
s.indexOf("B");             // 4 (-1 if absent)
s.lastIndexOf("g");         // 8
s.substring(4);             // "Bloggs"
s.substring(0, 3);          // "Joe"  (end index excluded)
s = s.toUpperCase();        // reassign to keep the result
s.equals("JOE BLOGGS");     // compare text: never ==
s.equalsIgnoreCase("joe bloggs");
s.startsWith("JOE"); s.endsWith("S"); s.contains("BLOG");
s.trim();                   // remove spaces at both ends

char c = 'a';
int code = c;               // 97
char next = (char) (c + 1); // 'b'
Character.toUpperCase(c); Character.isLetter(c); Character.isDigit(c);

for (int i = 0; i < s.length(); i++) { char ch = s.charAt(i); }

StringBuffer b = new StringBuffer("text");
b.append("!"); b.insert(0, ">"); b.replace(1, 5, "TEXT"); b.reverse();
String result = b.toString();
```

## 13. Glossary

| Term | Meaning |
| --- | --- |
| String | An object type storing a sequence of characters |
| `char` | A primitive type for one character, written in single quotes |
| Index | The position of a character, starting at 0 |
| Substring | A part of a String, from a start index up to (not including) an end index |
| Immutable | Cannot be changed after creation; String methods return new Strings |
| Dot notation | Calling a method on a value: `name.length()` |
| Character code | The number stored for a `char` (ASCII/Unicode), e.g. `'A'` is 65 |
| `Character` | The wrapper class for `char`, with helpers such as `isLetter` |
| `StringBuffer` | A changeable sequence of characters |
| Unicode | The international character set Java uses; its first 128 codes match ASCII |

## 14. Summary

- A String is an object holding a sequence of `char` values, indexed from 0 to `length() - 1`.
- Its methods (`length`, `charAt`, `indexOf`, `substring`, `toUpperCase`…) return results; they never change the original, because Strings are immutable.
- Compare Strings with `equals` (and its relatives), never `==`.
- `char` is a primitive: compare it with `==` and `<`, do arithmetic with its code, and use `Character` for helpers.
- `StringBuffer` is text you can change with `append`, `insert`, `replace` and `reverse`.

**Next:** work through Lab 13. Lecture 14 starts **methods**: writing your own.
