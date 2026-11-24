# Lab 13 — String and char Hands-on Workbook (20 Tasks)

**Module:** 4300COMP Introduction to Programming · **Language:** Java

## How to use this lab

This lab has **20 hands-on tasks** on Lecture 13: String indices and methods, immutability, comparing Strings, `char` and character codes, the `Character` helpers and `StringBuffer`. **All official Tutorial 13 tasks and the supplementary Caesar cipher are included** (Tasks 2, 4, 5, 12, 13 and 16), marked "official". Several tasks are text-processing jobs from cyber security: ciphers, password rules, log parsing and username generation.

**Learning outcomes:** MLO1 (string-processing algorithms), MLO2 (the `String`, `Character` and `StringBuffer` documentation), MLO3 (Tasks 16–20 turn specifications into programs).

**Setup:** create a Java project called **Lab13** in Eclipse (untick *Create module-info.java*). Keep the [String documentation](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/String.html) open in a browser tab; you will use it.

**Rules for this lab:**

1. **Draw the index table** for any String you work with: index numbers above, characters below. Count spaces too.
2. **`substring(a, b)` excludes `b`.** Check every substring by counting `b − a` characters.
3. **Never compare Strings with `==`.**
4. Predict before you run; use the hints only after a real attempt.

The **tracker** is near the end, followed by the **answer key**. Every answer was compiled and run with Java 21 (javac on the command line, not Eclipse) with the inputs shown.

## Part A — Reading Strings (Tasks 1–5)

### Task 1 — Draw the index table

**Class:** `Task01Index` · **Goal:** see a String as numbered characters.

For `String cs = "Cyber Security";`:

1. Draw the index table (indices 0 to 13).
2. Predict, then print: `cs.length()`, `cs.charAt(6)`, `cs.indexOf("e")`, `cs.lastIndexOf("e")`, `cs.substring(6)`, `cs.substring(0, 5)`.
3. Using `indexOf(" ")`, write expressions that give the first word and the second word **without** typing any numbers.

### Task 2 — Official Tutorial 13, Task 1

**Class:** `Task02Name` · **Goal:** `charAt`, `length` and `toUpperCase` on your own name.

Write a program that stores your name (first name and surname) in a String, then:

1. displays the **2nd** and **5th** characters;
2. displays the number of characters in your name, **subtracting one for the space**;
3. converts your name to upper case and prints it.

Before running, write the indices you will use for "2nd" and "5th". (The answer key uses the placeholder name "Sam Archer"; use your own.)

### Task 3 — Predict String expressions

**Class:** `Task03Predict` · **Goal:** read String methods fluently.

`String w = "Programming";` Predict, then check:

| | Expression | Prediction | Actual |
| --- | --- | --- | --- |
| a | `w.length()` | | |
| b | `w.charAt(3)` | | |
| c | `w.indexOf("gram")` | | |
| d | `w.indexOf("m")` | | |
| e | `w.lastIndexOf("m")` | | |
| f | `w.substring(3, 7)` | | |
| g | `w.substring(7)` | | |
| h | `w.toUpperCase().charAt(0)` | | |
| i | `w.startsWith("pro")` | | |
| j | `w.equalsIgnoreCase("PROGRAMMING")` | | |
| k | `w.charAt(w.length() - 1)` | | |
| l | `w.contains("Gram")` | | |

Score out of 12.

### Task 4 — Official Tutorial 13, Task 2: backwards

**Class:** `Task04Backwards` · **Goal:** loop over characters in reverse.

Store any text in a String, then print its letters **backwards, all on one line**.

Then do it a second way using `StringBuffer`'s `reverse()`. Which is shorter? Which shows more clearly how it works?

- **Hint 1:** start at `text.length() - 1` and count down to 0, printing `text.charAt(i)`.

### Task 5 — Official Tutorial 13, Task 3: names and initials

**Class:** `Task05Initials` · **Goal:** combine input, joining and `charAt`.

Ask for the first name and then the surname. Print the full name, the initials, and the number of characters in each name, exactly as in the tutorial's sample:

```text
Please, type in your first name: Joe
Please, type in your last name: Bloggs
Your full name is Joe Bloggs.
Your initials are JB
Your first name has 3 characters.
Your last name has 6 characters.
```

Then: what goes wrong if the user types `joe bloggs` in lower case? Fix the initials so they are always upper case.

- **Hint 1:** `first.charAt(0) + last.charAt(0)` adds two **numbers** if nothing before them is a String. Put them inside a String expression.

## Part B — Find and fix (Tasks 6–10)

### Task 6 — == versus equals

**Class:** `Task06Compare` · **Goal:** see the `==` trap for yourself.

```java
Scanner console = new Scanner(System.in);
System.out.print("What is your name? ");
String name = console.next();
System.out.println(name == "Fred");
System.out.println(name.equals("Fred"));
String literal = "Fred";
System.out.println(literal == "Fred");
```

1. Run it and type `Fred`. Record the three results.
2. Explain why the first and third lines differ, even though both look like they compare "Fred" with "Fred".
3. Why is this trap dangerous in a **login** check?
4. Add a test with `equalsIgnoreCase` and type `FRED`.

### Task 7 — The immutability bug

**Class:** `Task07Immutable` · **Goal:** find bugs caused by ignoring returned Strings.

This code should tidy a username (remove spaces at the ends, make lower case) and print `[admin]`, but it prints `[  Admin  ]`:

```java
String user = "  Admin  ";
user.trim();
user.toLowerCase();
System.out.println("[" + user + "]");
```

1. Explain why nothing changed.
2. Fix it with two reassignments, then with one line by **chaining**: `user = user.trim().toLowerCase();`
3. **Security link:** why do login systems usually tidy usernames like this before comparing them?

### Task 8 — String and char error clinic

**Class:** `Task08Errors` · **Goal:** recognise the error messages.

Try each line on its own, record the exact error (compile or runtime), explain it, fix it.

```java
char c1 = 'h'; c1 = c1.toUpperCase();          // 1
StringBuffer b = "Hello World";                // 2
char c2 = 'ab';                                // 3
String s = "Fred"; System.out.println(s.charAt(4));       // 4
System.out.println(s.substring(3, 1));         // 5
char c3 = s;                                   // 6
String t = 'Fred';                             // 7
boolean before = "apple" < "banana";           // 8
```

### Task 9 — char arithmetic

**Class:** `Task09CharMaths` · **Goal:** use character codes.

Predict, then check:

| | Expression | Prediction | Actual |
| --- | --- | --- | --- |
| a | `'b' - 'a'` | | |
| b | `(char) ('A' + 25)` | | |
| c | `'z' - 'a' + 1` | | |
| d | `(int) '0'` | | |
| e | `'7' - '0'` | | |
| f | `'C' + 1` | | |
| g | `(char) ('C' + 1)` | | |
| h | `"" + 'C' + 1` | | |
| i | `'a' > 'Z'` | | |

Then explain: (1) how (e) converts a digit character into its number value; (2) why (i) is `true`, and what that means for sorting words that mix upper and lower case.

### Task 10 — Fix the slide's StringBuffer example

**Class:** `Task10Buffer` · **Goal:** correct real code from the slides.

The Lecture 13 slide shows:

```java
StringBuffer birthdayMsg = new StringBuffer("Happy Birthday);
someBuffer.insert(6,"40th ");
```

and says the output is `Happy 40th Birthday`.

1. Find and fix the **two** errors. Add a `println`.
2. Extend it: `append("!")`, then use `replace` to change `40th` to `21st`, then `reverse()`. Print after each step.
3. Convert the final buffer to a String with `toString()` and print its length.

## Part C — Text processing (Tasks 11–15)

### Task 11 — Cutting Strings apart

**Class:** `Task11Extract` · **Goal:** combine `indexOf` and `substring`.

1. From `"Building Java Programs"`, extract `"Java"` (answer the slide's first question).
2. Write expressions that give the **first word** and the **last word** of any String that contains spaces (answer the slide's second question). Test on three different sentences.
3. From the email address `sam.archer@example.ac.uk`, extract the username (before `@`) and the domain (after `@`).
4. What happens with your first-word expression when the String has **no** space? Add an `if` that handles it.

- **Hint 1:** last word: `s.substring(s.lastIndexOf(" ") + 1)`.

### Task 12 — Official Tutorial 13, Task 4: capitalise each word

**Class:** `Task12Capitalise` · **Goal:** build a new String character by character.

Store `"The quick brown fox jumps over the lazy dog"` and change it so that each word begins with a capital letter:

```text
The Quick Brown Fox Jumps Over The Lazy Dog
```

- **Hint 1:** a character starts a word if it is the first character, or the character before it is a space.
- **Hint 2:** build the result in a String (or a `StringBuffer`), adding `Character.toUpperCase(c)` or `c` each time.

### Task 13 — Official Tutorial 13, Task 5: swap fox and dog

**Class:** `Task13Swap` · **Goal:** rebuild a String from pieces.

Change `"The quick brown fox jumps over the lazy dog"` so that it reads:

```text
The quick brown dog jumps over the lazy fox
```

1. Do it with `indexOf` and `substring` only (find each word, then join the pieces around them).
2. Look up `replace(CharSequence, CharSequence)` in the String documentation and do it a second way. Why can't you simply replace "fox" with "dog" and then "dog" with "fox"?

### Task 14 — Character statistics

**Class:** `Task14Counts` · **Goal:** classify every character with `Character` methods.

For `"Meet me at Gate 7 at 09:30, not Gate 12!"`, count: vowels, upper-case letters, digits, spaces, and other symbols. Print one summary line.

Expected: `Length 40: vowels 10, upper-case 3, digits 7, spaces 9, other symbols 3`

- **Hint 1:** a quick vowel test: `"aeiouAEIOU".indexOf(c) != -1`.

### Task 15 — Palindromes

**Class:** `Task15Palindrome` · **Goal:** clean, reverse and compare text.

A palindrome reads the same forwards and backwards, ignoring case, spaces and punctuation ("Never odd or even").

1. Read a phrase with `nextLine()`.
2. Build a `StringBuffer` of only its letters and digits, in lower case.
3. Compare it with its reverse using `equals` on the two Strings.

Test with `Never odd or even` (yes), `Cyber security` (no), and one of your own.

## Part D — Ciphers, passwords and logs (Tasks 16–20)

### Task 16 — Official Tutorial 13, supplementary: Caesar cipher

**Class:** `SecretMessage` · **Goal:** shift letters using character codes.

A Caesar cipher shifts each letter by a fixed amount, the **key**. With a key of 3: A → D, H → K, and wrapping round the end of the alphabet, X → A and Z → C.

Start from the tutorial's outline:

```java
import java.util.*;

public class SecretMessage {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);

        System.out.print("Enter your secret message: ");
        String message = console.nextLine();
        message = message.toLowerCase();

        System.out.print("Enter your secret key: ");
        int key = console.nextInt();

        // code to encode the secret message goes here
    }
}
```

Fill in the encoding. Letters are shifted; spaces and punctuation are kept as they are.

| Test | Message | Key | Expected |
| --- | --- | --- | --- |
| 1 | `Attack at Dawn!` | 3 | `dwwdfn dw gdzq!` |
| 2 | `xyz abc` | 3 | `abc def` (wrap-around) |
| 3 | `dwwdfn dw gdzq!` | −3 | `attack at dawn!` (decoding) |
| 4 | `hello` | 29 | `khoor` (same as key 3) |

**Cyber security link:** the Caesar cipher is the classic first example in cryptography, and it is completely insecure: Task 19 breaks it. Never use home-made encryption to protect real data; real systems use tested standard algorithms.

- **Hint 1:** position in the alphabet: `int position = c - 'a';` (0 to 25).
- **Hint 2:** wrap with `% 26`. For negative keys, add 26 before taking `% 26`: `(position + key % 26 + 26) % 26`. Turn back into a letter with `(char) ('a' + shifted)`.

### Task 17 — Password policy checker

**Class:** `PasswordCheck` · **Goal:** check text against several rules and report every failure.

Read a username and a password (whole lines). Report each rule the password breaks:

- at least 12 characters;
- at least one upper-case letter, one lower-case letter, one digit, and one symbol or space;
- must not contain the username (ignoring case).

Print `Password accepted.` or the number of problems.

| Username | Password | Expected |
| --- | --- | --- |
| `sam` | `password` | 4 problems (length, upper, digit, symbol) |
| `sam` | `Correct-Horse-42-Battery` | accepted |
| `sarcher` | `Sarcher2026!!xx` | 1 problem (contains the username) |

**Think:** current UK government guidance (NCSC) favours long passphrases such as "three random words" over complicated short passwords. How would you change these rules to encourage that? (This is a learning exercise; real systems should also check passwords against lists of known breached passwords.)

### Task 18 — Log line parser

**Class:** `LogParser` · **Goal:** extract fields from structured text.

A security log line looks like this:

```text
2026-11-24 09:14:02 FAIL user=bob ip=203.0.113.9
```

Extract and print the date, the time, the hour as an `int`, the status, the user and the IP address:

```text
Date:   2026-11-24
Time:   09:14:02 (hour 9)
Status: FAIL
User:   bob
IP:     203.0.113.9
```

1. First use fixed positions where the format guarantees them (date and time).
2. Then use `indexOf("user=")` and `indexOf("ip=")` so the code still works if the status were `OK` instead of `FAIL`. Test it.
3. Convert the hour with `Integer.parseInt` (Lab 2).

### Task 19 — Mini-project: crack a Caesar cipher

**Class:** `CaesarCrack` · **Goal:** brute-force all keys and spot the answer.

You intercepted this message, encrypted with an unknown Caesar key:

```text
wkh phhwlqj lv dw wkuhh
```

1. There are only 25 possible keys. Write a loop that decodes the message with **every** key from 1 to 25 and prints each attempt with its key.
2. Make the program mark any attempt that contains the word `the` (a very common English word).
3. What is the key, and what does the message say?
4. Why does this show the Caesar cipher is insecure? How many keys would a computer need to try for a cipher with 2¹²⁸ possible keys, and why is that different?

- **Hint 1:** decoding is shifting **back**: `(c - 'a' - key + 26) % 26`.

### Task 20 — Assessment-style task: username generator

**Class:** `Usernames` · **Goal:** a complete text-processing program with files and an `ArrayList`.

This is a practice task similar in skills to the module's application assessments. It is **not** an actual assessment question.

**Input** `staff.txt`, one full name per line (blank lines may appear):

```text
Joe Bloggs
Sue White
James Blogg
Priya Raghunathan
Jo Bloggs
Mary-Jane O'Neill
Cher

Joe Bloggs
```

**Specification:**

1. A username is the first letter of the first name followed by the surname (the **last** word), in lower case, with any non-letters removed from the surname.
2. A username is at most **8** characters; cut it down if longer.
3. Usernames must be unique: if one is taken, add 2, then 3, and so on (`jbloggs`, `jbloggs2`, …).
4. Skip blank lines. Skip a line with only one name, printing `Skipped (needs first and last name): ...`.
5. Write each `username full name` pair to `usernames.txt`, show them on the console, and finish with the number created.

**Expected console output:**

```text
jbloggs      Joe Bloggs
swhite       Sue White
jblogg       James Blogg
praghuna     Priya Raghunathan
jbloggs2     Jo Bloggs
moneill      Mary-Jane O'Neill
Skipped (needs first and last name): Cher
jbloggs3     Joe Bloggs
7 usernames written to usernames.txt
```

Write a test plan covering each rule (including the length limit, a duplicate and a surname with punctuation) before you code. **Question:** the second "Joe Bloggs" might be the same person listed twice, or a different person with the same name. Which should the program assume, and who should decide?

- **Hint 1:** keep the usernames already issued in an `ArrayList<String>`, and use `contains` in a `while` loop to find a free one.
- **Hint 2:** read with `hasNextLine()`/`nextLine()` and `trim()` each line.

## Tracker

| Task | Done | Notes / score |
| --- | --- | --- |
| 1 Index table | ☐ | |
| 2 Official Task 1 | ☐ | |
| 3 Predict (out of 12) | ☐ | |
| 4 Official Task 2 | ☐ | |
| 5 Official Task 3 | ☐ | |
| 6 == vs equals | ☐ | |
| 7 Immutability bug | ☐ | |
| 8 Error clinic (out of 8) | ☐ | |
| 9 char arithmetic (out of 9) | ☐ | |
| 10 Fix StringBuffer slide | ☐ | |
| 11 Cutting Strings | ☐ | |
| 12 Official Task 4 | ☐ | |
| 13 Official Task 5 | ☐ | |
| 14 Character statistics | ☐ | |
| 15 Palindromes | ☐ | |
| 16 Official supplementary: Caesar | ☐ | |
| 17 Password checker | ☐ | |
| 18 Log parser | ☐ | |
| 19 Crack the cipher | ☐ | |
| 20 Username generator | ☐ | |

## Reflection

1. Explain "Strings are immutable" and show one bug it causes.
2. When do you compare with `==`, and when with `equals`? Give an example of each.
3. Which `char` trick (codes, casting, `Character` methods) was most useful today?
4. Tasks 16–20 are real security tasks in miniature. Which interested you most, and what would you want to learn next about it?

## Answer key

All code was compiled and run with Java 21 (javac on the command line, not Eclipse). Outputs are actual outputs.

**Task 1.** `14`, `S`, `3`, `7`, `Security`, `Cyber` (verified). First word: `cs.substring(0, cs.indexOf(" "))`; second: `cs.substring(cs.indexOf(" ") + 1)`.

**Task 2.**

```java
public class Task02Name {
    public static void main(String[] args) {
        String name = "Sam Archer";                       // use your own name
        System.out.println("2nd character: " + name.charAt(1));
        System.out.println("5th character: " + name.charAt(4));
        System.out.println("Letters (without the space): " + (name.length() - 1));
        System.out.println(name.toUpperCase());
    }
}
```

Output (verified): `2nd character: a`, `5th character: A`, `Letters (without the space): 9`, `SAM ARCHER`. The 2nd character is index 1 and the 5th is index 4. The brackets around `name.length() - 1` matter: without them, `+` would join text first.

**Task 3.** a 11 · b `g` · c 3 · d 6 · e 7 · f `gram` · g `ming` · h `P` · i `false` (case matters) · j `true` · k `g` · l `false`. All verified.

**Task 4.**

```java
public class Task04Backwards {
    public static void main(String[] args) {
        String text = "Cyber Security";
        for (int i = text.length() - 1; i >= 0; i--) {
            System.out.print(text.charAt(i));
        }
        System.out.println();
    }
}
```

Output (verified): `ytiruceS rebyC`. With a buffer: `System.out.println(new StringBuffer(text).reverse());`.

**Task 5.**

```java
import java.util.Scanner;

public class Task05Initials {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        System.out.print("Please, type in your first name: ");
        String first = console.next();
        System.out.print("Please, type in your last name: ");
        String last = console.next();
        System.out.println();
        System.out.println("Your full name is " + first + " " + last + ".");
        System.out.println("Your initials are " + first.charAt(0) + last.charAt(0));
        System.out.println("Your first name has " + first.length() + " characters.");
        System.out.println("Your last name has " + last.length() + " characters.");
        console.close();
    }
}
```

Output with `Joe` and `Bloggs` matches the tutorial (verified). For lower-case input use `Character.toUpperCase(first.charAt(0))`, and likewise for the surname.

**Task 6.** With `Fred` typed: `false`, `true`, `true` (verified). Typed input creates a **new** String object, so `==` (same object?) is false. Identical literals in the code are reused as one object, so `literal == "Fred"` is true. In a login check, `==` would reject the correct password typed by a user while seeming to work in tests with hard-coded values. `name.equalsIgnoreCase("FRED")` is true for `FRED`.

**Task 7.** `trim()` and `toLowerCase()` return **new** Strings, which were thrown away (verified: prints `[  Admin  ]`). Fix: `user = user.trim().toLowerCase();` → `[admin]`. Tidying stops `Admin`, `admin ` and `ADMIN` from being treated as different accounts, which could otherwise confuse access checks or let someone register a look-alike name.

**Task 8.** (1) `error: char cannot be dereferenced` → `Character.toUpperCase(c1)`. (2) `error: incompatible types: String cannot be converted to StringBuffer` → `new StringBuffer("Hello World")`. (3) `error: unclosed character literal` → `"ab"` as a String. (4) Runtime: `StringIndexOutOfBoundsException: Index 4 out of bounds for length 4` → `charAt(3)`. (5) Runtime: `StringIndexOutOfBoundsException: Range [3, 1) out of bounds for length 4` → `substring(1, 3)`. (6) `error: incompatible types: String cannot be converted to char` → `s.charAt(0)`. (7) `error: unclosed character literal` → `"Fred"`. (8) `error: bad operand types for binary operator '<'` → `"apple".compareTo("banana") < 0`. All verified.

**Task 9.** a 1 · b `Z` · c 26 · d 48 · e 7 · f 68 · g `D` · h `C1` · i `true` (verified). (1) Digit characters have consecutive codes from `'0'` (48), so subtracting `'0'` gives the digit's value. (2) All upper-case codes (65–90) are below all lower-case codes (97–122), so simple sorting puts every capitalised word before every lower-case word (as seen with `priya` in Lab 12 Task 20).

**Task 10.** Errors: the missing closing `"` in `"Happy Birthday"`, and `someBuffer` should be `birthdayMsg`. Fixed and extended:

```java
public class BufferDemo {
    public static void main(String[] args) {
        StringBuffer birthdayMsg = new StringBuffer("Happy Birthday");
        birthdayMsg.insert(6, "40th ");
        System.out.println(birthdayMsg);
        birthdayMsg.append("!");
        System.out.println(birthdayMsg);
        birthdayMsg.replace(6, 10, "21st");
        System.out.println(birthdayMsg);
        StringBuffer word = new StringBuffer("stressed");
        word.reverse();
        System.out.println(word);
        String back = word.toString();
        System.out.println(back.length());
    }
}
```

Output (verified): `Happy 40th Birthday`, `Happy 40th Birthday!`, `Happy 21st Birthday!`, `desserts`, `8`. (For your own version, reverse `birthdayMsg` itself.)

**Task 11.** `msg.substring(9, 13)` → `Java`; first word `Building`, last word `Programs` (verified). Email: `sam.archer` and `example.ac.uk` (verified). With no space, `indexOf` returns −1, and `substring(0, -1)` throws `StringIndexOutOfBoundsException`; check `if (s.indexOf(" ") == -1)` and use the whole String as the first word.

**Task 12.**

```java
public class Task12Capitalise {
    public static void main(String[] args) {
        String text = "The quick brown fox jumps over the lazy dog";
        String result = "";
        boolean startOfWord = true;
        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            if (startOfWord) {
                result = result + Character.toUpperCase(c);
            } else {
                result = result + c;
            }
            startOfWord = (c == ' ');      // the next character starts a word if this one is a space
        }
        System.out.println(result);
    }
}
```

Output (verified): `The Quick Brown Fox Jumps Over The Lazy Dog`.

**Task 13.**

```java
public class Task13Swap {
    public static void main(String[] args) {
        String text = "The quick brown fox jumps over the lazy dog";

        // Method 1: cut and rebuild with indexOf and substring
        int fox = text.indexOf("fox");
        int dog = text.indexOf("dog");
        String swapped = text.substring(0, fox) + "dog" + text.substring(fox + 3, dog) + "fox" + text.substring(dog + 3);
        System.out.println(swapped);

        // Method 2: replace via a temporary placeholder
        String temp = text.replace("fox", "#TEMP#").replace("dog", "fox").replace("#TEMP#", "dog");
        System.out.println(temp);
    }
}
```

Both print `The quick brown dog jumps over the lazy fox` (verified). Replacing fox → dog first would leave **two** "dog"s, and the second step would then turn both into "fox". A temporary placeholder avoids that.

**Task 14.**

```java
public class Task14Counts {
    public static void main(String[] args) {
        String sentence = "Meet me at Gate 7 at 09:30, not Gate 12!";
        int vowels = 0, upper = 0, digits = 0, spaces = 0, other = 0;
        for (int i = 0; i < sentence.length(); i++) {
            char c = sentence.charAt(i);
            if ("aeiouAEIOU".indexOf(c) != -1) {
                vowels++;
            }
            if (Character.isUpperCase(c)) {
                upper++;
            }
            if (Character.isDigit(c)) {
                digits++;
            } else if (c == ' ') {
                spaces++;
            } else if (!Character.isLetter(c)) {
                other++;
            }
        }
        System.out.println("Length " + sentence.length() + ": vowels " + vowels + ", upper-case " + upper
                + ", digits " + digits + ", spaces " + spaces + ", other symbols " + other);
    }
}
```

Output verified as in the task.

**Task 15.**

```java
import java.util.Scanner;

public class Task15Palindrome {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        System.out.print("Enter a phrase: ");
        String phrase = console.nextLine();

        StringBuffer letters = new StringBuffer();
        for (int i = 0; i < phrase.length(); i++) {
            char c = phrase.charAt(i);
            if (Character.isLetterOrDigit(c)) {
                letters.append(Character.toLowerCase(c));
            }
        }
        String forwards = letters.toString();
        String backwards = letters.reverse().toString();
        System.out.println();
        if (forwards.equals(backwards)) {
            System.out.println("\"" + phrase + "\" is a palindrome.");
        } else {
            System.out.println("\"" + phrase + "\" is not a palindrome.");
        }
        console.close();
    }
}
```

Both tests verified. Note `forwards` is taken **before** `reverse()`, because `reverse` changes the buffer itself.

**Task 16.**

```java
import java.util.Scanner;

public class SecretMessage {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);

        System.out.print("Enter your secret message: ");
        String message = console.nextLine();
        message = message.toLowerCase();

        System.out.print("Enter your secret key: ");
        int key = console.nextInt();

        // code to encode the secret message goes here
        String encoded = "";
        for (int i = 0; i < message.length(); i++) {
            char c = message.charAt(i);
            if (c >= 'a' && c <= 'z') {
                int position = c - 'a';                         // 0 for a ... 25 for z
                int shifted = (position + key % 26 + 26) % 26;  // wrap around, also for negative keys
                c = (char) ('a' + shifted);
            }
            encoded = encoded + c;                              // non-letters are kept as they are
        }
        System.out.println();
        System.out.println("Encoded: " + encoded);
        console.close();
    }
}
```

All four tests give the expected results (verified).

**Task 17.**

```java
import java.util.Scanner;

public class PasswordCheck {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        System.out.print("Username: ");
        String username = console.nextLine();
        System.out.print("Password: ");
        String password = console.nextLine();
        System.out.println();

        boolean hasUpper = false, hasLower = false, hasDigit = false, hasSymbol = false;
        for (int i = 0; i < password.length(); i++) {
            char c = password.charAt(i);
            if (Character.isUpperCase(c)) {
                hasUpper = true;
            } else if (Character.isLowerCase(c)) {
                hasLower = true;
            } else if (Character.isDigit(c)) {
                hasDigit = true;
            } else {
                hasSymbol = true;
            }
        }

        int problems = 0;
        if (password.length() < 12) {
            System.out.println("- must be at least 12 characters (has " + password.length() + ")");
            problems++;
        }
        if (!hasUpper) {
            System.out.println("- needs an upper-case letter");
            problems++;
        }
        if (!hasLower) {
            System.out.println("- needs a lower-case letter");
            problems++;
        }
        if (!hasDigit) {
            System.out.println("- needs a digit");
            problems++;
        }
        if (!hasSymbol) {
            System.out.println("- needs a symbol or space");
            problems++;
        }
        if (password.toLowerCase().contains(username.toLowerCase())) {
            System.out.println("- must not contain the username");
            problems++;
        }
        if (problems == 0) {
            System.out.println("Password accepted.");
        } else {
            System.out.println(problems + " problem(s) found.");
        }
        console.close();
    }
}
```

All three tests verified. To encourage passphrases: raise the minimum length (for example 15+) and drop the character-type rules, which mostly push people towards predictable patterns like `Password1!`.

**Task 18.**

```java
public class LogParser {
    public static void main(String[] args) {
        String line = "2026-11-24 09:14:02 FAIL user=bob ip=203.0.113.9";

        String date = line.substring(0, 10);
        String time = line.substring(11, 19);
        int statusStart = 20;
        int statusEnd = line.indexOf(" ", statusStart);
        String status = line.substring(statusStart, statusEnd);

        int userStart = line.indexOf("user=") + 5;
        String user = line.substring(userStart, line.indexOf(" ", userStart));
        String ip = line.substring(line.indexOf("ip=") + 3);
        int hour = Integer.parseInt(time.substring(0, 2));

        System.out.println("Date:   " + date);
        System.out.println("Time:   " + time + " (hour " + hour + ")");
        System.out.println("Status: " + status);
        System.out.println("User:   " + user);
        System.out.println("IP:     " + ip);
    }
}
```

Output verified as in the task. `indexOf(" ", start)` searches from position `start`, which finds the end of the status word whatever its length.

**Task 19.**

```java
public class CaesarCrack {
    public static void main(String[] args) {
        String secret = "wkh phhwlqj lv dw wkuhh";
        for (int key = 1; key <= 25; key++) {
            String attempt = "";
            for (int i = 0; i < secret.length(); i++) {
                char c = secret.charAt(i);
                if (c >= 'a' && c <= 'z') {
                    c = (char) ('a' + (c - 'a' - key + 26) % 26);     // shift BACK by key
                }
                attempt = attempt + c;
            }
            String marker = "";
            if (attempt.contains("the ") || attempt.contains(" the")) {
                marker = "   <-- contains \"the\"";
            }
            System.out.printf("key %2d: %s%s%n", key, attempt, marker);
        }
    }
}
```

Only one line is marked (verified): `key  3: the meeting is at three   <-- contains "the"`. With just 25 keys, a computer tries them all instantly. A modern cipher with 2¹²⁸ keys cannot be searched like this: even trying a trillion keys a second would take far longer than the age of the universe.

**Task 20.**

```java
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Scanner;

public class Usernames {
    public static void main(String[] args) throws FileNotFoundException {
        final int MAX_LENGTH = 8;
        ArrayList<String> usernames = new ArrayList<String>();
        Scanner read = new Scanner(new FileReader("staff.txt"));
        PrintWriter out = new PrintWriter("usernames.txt");

        while (read.hasNextLine()) {
            String line = read.nextLine().trim();
            int space = line.indexOf(" ");
            if (line.isEmpty()) {
                // ignore blank lines
            } else if (space == -1) {
                System.out.println("Skipped (needs first and last name): " + line);
            } else {
                String first = line.substring(0, space);
                String last = line.substring(line.lastIndexOf(" ") + 1);

                // keep only letters from the surname, in lower case
                String cleanLast = "";
                for (int i = 0; i < last.length(); i++) {
                    char c = last.charAt(i);
                    if (Character.isLetter(c)) {
                        cleanLast = cleanLast + Character.toLowerCase(c);
                    }
                }
                String base = Character.toLowerCase(first.charAt(0)) + cleanLast;
                if (base.length() > MAX_LENGTH) {
                    base = base.substring(0, MAX_LENGTH);
                }

                String username = base;
                int number = 2;
                while (usernames.contains(username)) {
                    username = base + number;
                    number++;
                }
                usernames.add(username);
                out.println(username + " " + line);
                System.out.printf("%-12s %s%n", username, line);
            }
        }
        read.close();
        out.close();
        System.out.println(usernames.size() + " usernames written to usernames.txt");
    }
}
```

Output verified as in the task, and `usernames.txt` starts `jbloggs Joe Bloggs`. Note `Character.toLowerCase(first.charAt(0)) + cleanLast` works because `cleanLast` is a String, so `+` joins text. On the duplicate question: a program cannot know, so it should not silently merge records; a person (for example HR) should confirm, and the program could flag exact duplicates for review.

**Next:** Lecture 14 — writing your own methods.
