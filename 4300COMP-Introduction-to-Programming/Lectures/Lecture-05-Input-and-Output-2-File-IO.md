# Lecture 5 — Input and Output #2: File I/O

**Module:** 4300COMP Introduction to Programming · **Language:** Java

## Overview

Lecture 5 takes everything you learned about console I/O and points it at **files**. Because Java treats both as **streams**, the code barely changes: a `FileReader` replaces `System.in` inside a `Scanner`, and a `PrintWriter` replaces `System.out`. The new parts are **where** the file is, **what to do if it is missing**, and **closing** it when you are done. These notes rewrite the official Lecture 5 slides in plain English; every program shown was run with Java 21 against the data files given.

**By the end you should be able to:**

1. Explain why the stream abstraction lets console code be reused for files.
2. Read a text file with `FileReader` + `Scanner`, using `next()`, `nextInt()`, `nextDouble()` and `nextLine()`.
3. Say where Eclipse looks for a file with a relative name, and write an absolute path with `\\`.
4. Plan the reading code from a file’s **structure (schema)**.
5. Explain runtime errors/exceptions, **checked** exceptions, and why `throws FileNotFoundException` is needed.
6. Write a text file with `PrintWriter`, using `print`, `println` and `printf`.
7. Explain why closing (or flushing) an output file matters.
8. Build a read → calculate → write program such as the Grade Calculator.

**Learning outcomes:** MLO1, MLO2 (FileReader, PrintWriter and their API pages; Eclipse auto-complete and Organise Imports), MLO3 (the Grade Calculator and the Tutorial 5 vehicle tasks).

**Matching lab:** Lab 5 (official Tutorial 5: File Input and Output).

**What you need from Lecture 4:** Scanner and its `next...` methods, `printf` specifiers, and the `nextInt()`/`nextLine()` trap.

## 1. Why streams make files easy

A **file** is an area of secondary storage (disk) that holds information: data from other programs, settings, logs. To a program:

- a file you **read** is an **input device**;
- a file you **write** is an **output device**.

Because Java models both console and files as **data streams**, most of what you already know carries over:

| Job | Console (Lecture 4) | File (Lecture 5) |
| --- | --- | --- |
| Source of input | `System.in` | `new FileReader("name.txt")` |
| Reading tool | `new Scanner(System.in)` | `new Scanner(fileReader)` |
| Reading methods | `next()`, `nextInt()`, `nextDouble()`, `nextLine()` | **the same** |
| Output destination | `System.out` | `new PrintWriter("name.txt")` |
| Writing methods | `print`, `println`, `printf` | **the same** |
| Can it be prompted? | Yes, the user reads your prompt | **No**, a file cannot answer questions |
| Extra things to handle | — | file location, file not found, closing |

The slide asks: is “console not found” the same as “file not found”? No. The console is always there; a file may be missing, misnamed, in the wrong folder, or locked. Files need more error handling.

## 2. Reading a file: FileReader + Scanner

The five things you need to know (from the slides):

1. **Where it is:** import `java.io.FileReader` (and `java.util.Scanner`).
2. **Which file** and how to tell Java where to find it.
3. **How to use Scanner** with it: wrap the FileReader in a Scanner.
4. **Error handling:** what can go wrong and what to do.
5. **Closing:** tell Java you have finished with the file.

```java
import java.io.FileReader;
import java.util.Scanner;

public class FileInput {
    public static void main(String[] args) {
        String fileName = "prog.txt";
        FileReader file = new FileReader(fileName);   // open the file
        Scanner read = new Scanner(file);              // wrap it, just like System.in
        // then read file data
        // deal with errors and tell Java we're done with the file
    }
}
```

This sketch does **not compile yet**: see section 5.

**Eclipse helps with imports:** type `FileNot` then **Ctrl+Space** to auto-complete and add the import; or press **Ctrl+Shift+O** (**Source \> Organise Imports**) to add every missing import at once.

## 3. Where does Java look for the file?

A name like `"prog.txt"` is a **relative** filename: Java looks in its **current working directory**, which depends on how the program is run:

| How it runs | Where `prog.txt` must be |
| --- | --- |
| **Eclipse** | the **project root folder** (e.g. `Lab05/prog.txt`, next to `src`, **not** inside `src`) |
| Windows command line | the folder you ran the command from (often next to the `.class` file) |
| Linux command line | the current folder (often your home directory) |

This uncertainty causes “it works on my machine” bugs. A simple fix is an **absolute** pathname, which gives the full location:

```java
String fileName = "M:\\prog.txt";   // the file M:\prog.txt
```

Remember Lecture 4: `\\` is the escape sequence for one backslash.

**In Eclipse:** to create a data file, right-click the project \> **New \> File**, type the name, and paste the data. After a program **writes** a file, right-click the project \> **Refresh** (F5) to see it.

## 4. Reading the data: know the file’s structure

You use exactly the same Scanner methods as for the console. But **you cannot prompt a file**, so you must **know (or assume) the file’s structure** — its **schema**: which items appear, in what order, separated by what, and of what type.

The slide’s file `prog.txt` holds one line: name, age, hourly rate, hours worked.

```text
David 36 22.75 37
```

```java
String name = read.next();          // "David"
int age = read.nextInt();           // 36
double rate = read.nextDouble();    // 22.75
int hoursWorked = read.nextInt();   // 37
double pay = rate * hoursWorked;    // 841.75
```

The slide asks why this line is **incompatible**:

```text
John 32 Pittance! 60
```

`nextDouble()` expects a number for the rate but finds `Pittance!`, so the program stops with `java.util.InputMismatchException` (verified). The reading code and the file’s structure must match exactly.

Tokens are separated by **any** whitespace, so the same four values spread over several lines read exactly the same way with `next()`/`nextInt()`/`nextDouble()`. `nextLine()` is different: it reads to the end of a line. Use it for items that contain spaces (such as `Nissan Juke`), and watch for the Lecture 4 trap.

## 5. Errors and exceptions

Errors can happen while a program runs, for example dividing an `int` by zero, or an input mismatch. These are **runtime errors**, called **exceptions** in Java. A method can either:

- **handle** the exception itself (“catch” it — covered later in the module), or
- **pass it on** (“throw” it) to whatever called the method.

Some exception types are **checked exceptions**: the compiler **forces** you to acknowledge them before the program will compile. Creating a `FileReader` can throw `FileNotFoundException` (a checked exception) if the file cannot be opened. Without acknowledging it (verified):

```text
error: unreported exception FileNotFoundException; must be caught or declared to be thrown
```

For now the module uses the simplest approach, a **throws clause**, which reports the problem rather than handling it:

```java
public static void main(String[] args) throws FileNotFoundException
```

This needs `import java.io.FileNotFoundException;`. If the file really is missing, the program now compiles but stops at runtime and prints the error:

```text
Exception in thread "main" java.io.FileNotFoundException: prog.txt (No such file or directory)
```

(On Windows the bracket reads “The system cannot find the file specified”.)

`InputMismatchException` (from Scanner) is **not** checked, so it needs no throws clause; it simply stops the program if it happens.

## 6. Closing files

`read.close();` closes the Scanner **and** the file inside it, releasing the file for other programs. Close a file as soon as you have finished reading it.

## 7. Writing a file: PrintWriter

`PrintWriter` is the file version of `System.out`. Same five questions:

1. Import `java.io.PrintWriter`.
2. Give it a filename (relative or absolute, same rules as reading).
3. Use `print`, `println` and `printf` exactly as with `System.out`.
4. Errors: creating it also throws `FileNotFoundException`.
5. Close it.

```java
PrintWriter write = new PrintWriter("out.txt");
write.printf("Pay for %s: £%.2f", name, pay);
write.close();
```

**Important behaviours:**

- If `out.txt` does not exist, it is **created**. If it **does** exist, its old contents are **replaced**.
- Why can creating an **output** file throw *FileNotFound*Exception? The [PrintWriter API](https://docs.oracle.com/en/java/javase/22/docs/api/java.base/java/io/PrintWriter.html) says: “if an error occurs while creating or opening the file” — for example the folder does not exist or you have no permission. As the slide says, exceptions aren’t always brilliantly named.

### Why closing an output file really matters

A PrintWriter collects output in a **buffer** (a temporary area in memory) and writes it to the disk in chunks. **Closing** (or calling `write.flush()`) forces anything left in the buffer onto the disk. Verified: a program that does `println("Will I appear?")` but never calls `close()` leaves an **empty** (0-byte) file.

**Cyber security link:** files are a common way for attackers to feed bad data into programs, and output files often hold sensitive results. Know exactly what format you expect, close files promptly, and never write secrets (passwords, keys) to plain text files.

## 8. Worked programs

### Program A — the complete FileInput (read, calculate, write)

This combines the slides’ final input and output versions.

```java
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.PrintWriter;
import java.util.Scanner;

public class FileInput {
    public static void main(String[] args) throws FileNotFoundException {
        // 1. Open the input file and read one record
        FileReader file = new FileReader("prog.txt");
        Scanner read = new Scanner(file);
        String name = read.next();
        int age = read.nextInt();
        double rate = read.nextDouble();
        int hoursWorked = read.nextInt();
        read.close();                                 // finished reading

        // 2. Calculate
        double pay = rate * hoursWorked;

        // 3. Write the result to a file
        PrintWriter write = new PrintWriter("out.txt");
        write.printf("Pay for %s: £%.2f", name, pay);
        write.close();                                // flushes the buffer to disk
    }
}
```

**Input file** `prog.txt` (in the project root): `David 36 22.75 37`

**Result (verified):** the Console stays empty; after Refresh, `out.txt` contains `Pay for David: £841.75`. (The slides’ earlier version printed the same line to the console with `System.out.printf`.)

| Step | What happens |
| --- | --- |
| `new FileReader("prog.txt")` | Opens the file for reading; throws FileNotFoundException if it can’t |
| `new Scanner(file)` | Wraps it so you can read tokens |
| `read.next()` ... `read.nextInt()` | Reads the four tokens in order: David, 36, 22.75, 37 |
| `read.close()` | Releases the input file |
| `rate * hoursWorked` | 22.75 × 37 = 841.75 |
| `new PrintWriter("out.txt")` | Creates (or empties) `out.txt` |
| `write.printf(...)` | Same format string as you would give `System.out.printf` |
| `write.close()` | Writes the buffer to disk and releases the file |

Notice that `age` is read but never used. You still have to read it, because `rate` comes **after** it in the file.

### Program B — Student Grade Calculator (design example)

**Brief:** read a student’s latest five test scores from `grades.txt` and write their name and average to `average.txt`.

**Design steps from the slides:**

1. Identify the data and types (study an example file if you have one): a name (`String`) then five scores (`double`).
2. Open the input file.
3. Read each item in the record and store it (loops will make this shorter later in the module).
4. Calculate.
5. Open the output file and write the formatted result.

The slide implementation code is not shown, so this is one version that produces the slide output:

```java
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.PrintWriter;
import java.util.Scanner;

public class GradeCalculator {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner scan = new Scanner(new FileReader("grades.txt"));
        String name = scan.next();
        double average = 0;
        average += scan.nextDouble();
        average += scan.nextDouble();
        average += scan.nextDouble();
        average += scan.nextDouble();
        average += scan.nextDouble();
        average = average / 5;
        scan.close();

        System.out.println("Writing the following to output file");
        System.out.printf("Student: %s; Average: %.2f%n", name, average);

        PrintWriter out = new PrintWriter("average.txt");
        out.printf("Student: %s; Average: %.2f%n", name, average);
        out.close();
    }
}
```

**`+=`**, as the slide notes, is a shorthand: `average += scan.nextDouble();` means `average = average + scan.nextDouble();`. Here `average` first collects the **total**, then is divided by 5.

**Verified results:**

| `grades.txt` contains | Output and `average.txt` |
| --- | --- |
| `John 45 60 75 66 43` (implementation slide) | `Student: John; Average: 57.80` |
| `John 39 45 60 75 66` (design slide) | `Student: John; Average: 57.00` |

**Slide inconsistency:** the design slide shows the first file but the implementation slide shows the second, and only the second gives 57.80. Use `John 45 60 75 66 43` to match the slide output.

### Program C — FileOutputTest (Tutorial 5, Task 1)

```java
import java.io.FileNotFoundException;
import java.io.PrintWriter;

public class FileOutputTest {
    public static void main(String[] args) throws FileNotFoundException {
        PrintWriter write = new PrintWriter("test1.txt");
        write.println("Hello file! Welcome to LJMU");
        write.close();
    }
}
```

The Console is blank, which is correct: nothing was sent to `System.out`. Refresh the project (F5) to see `test1.txt` in the project root.

## 9. Common mistakes

Messages are from `javac` or the Java 21 runtime on Linux. Eclipse words compile errors differently; Windows words the “not found” detail differently.

| Mistake | What happens | Fix |
| --- | --- | --- |
| No `throws FileNotFoundException` | Compile error: unreported exception FileNotFoundException; must be caught or declared to be thrown | Add the throws clause and its import |
| Missing import for `PrintWriter`/`FileReader` | Compile error: cannot find symbol | Ctrl+Shift+O (Organise Imports) |
| Data file inside `src`, or misnamed (`prog.txt.txt`) | Runtime: FileNotFoundException: prog.txt (No such file or directory) | Put it in the project root; check the exact name |
| Single backslash in a path: `"M:\prog.txt"` | `Compile error``: illegal escape character` | `"M:\\prog.txt"` |
| Reading in a different order from the file | Wrong values, or InputMismatchException | Read in exactly the schema’s order |
| Text where a number is expected (`Pittance!`) | Runtime: InputMismatchException | Fix the data, or the reading code |
| File has fewer items than you read | Runtime: NoSuchElementException | Check the file has every field |
| Forgetting `close()` on a PrintWriter | Output file is empty (0 bytes) | Always `close()` (or `flush()`) |
| Expecting the new file to appear in Eclipse | It is not listed | Right-click project \> Refresh (F5) |
| Writing to a file you still need | PrintWriter **replaces** its contents | Use a different output filename |
| `nextLine()` after `nextInt()`/`nextDouble()` | Empty String (same trap as the console) | Extra `nextLine()` or read lines first |
| Using `next()` for a name with a space | Only the first word is read | `nextLine()` |

## Check yourself: 15 multiple-choice questions

Allow **15 minutes**, no Eclipse. Practice questions written for this module, not real test questions.

1. Which class writes text to a file? (A) `FileReader` (B) `Scanner` (C) `PrintWriter` (D) `System.in`
2. Which package contains `FileReader` and `PrintWriter`? (A) `java.util` (B) `java.io` (C) `java.lang` (D) `java.file`
3. In Eclipse, where must `data.txt` be for `new FileReader("data.txt")` to find it? (A) inside `src` (B) next to the `.java` file (C) the project root folder (D) the desktop
4. Why does `main` need `throws FileNotFoundException`? (A) to make the file load faster (B) it is a checked exception the compiler insists you acknowledge (C) to create the file if it is missing (D) it is only needed on Windows
5. A file contains `Amy 20 9.50 10`. The code reads `next()`, `nextInt()`, `nextDouble()`, `nextInt()` and prints rate × hours with `%.2f`. Output? (A) `95.00` (B) `190.00` (C) `200.00` (D) InputMismatchException
6. A program writes with a PrintWriter but never calls `close()`. The most likely result: (A) compile error (B) the output file is empty (C) the output appears twice (D) the console shows the text
7. The String `"M:\\data.txt"` represents the path: (A) `M:\\data.txt` (B) `M:data.txt` (C) `M:\data.txt` (D) `M:/data.txt`
8. `total += 5;` means: (A) `total = 5;` (B) `total = total + 5;` (C) `total == total + 5` (D) `5 = total + 5;`
9. A file contains `Ali 30 abc 40`. Reading `next()`, `nextInt()`, `nextDouble()` causes: (A) `abc` stored as 0.0 (B) NumberFormatException (C) InputMismatchException (D) FileNotFoundException
10. `new PrintWriter("out.txt")` is called when `out.txt` already contains data. What happens to the old data? (A) kept, new text added to the end (B) replaced (C) exception (D) new text added to the start
11. Which of these is a **checked** exception? (A) InputMismatchException (B) ArithmeticException (C) FileNotFoundException (D) NoSuchElementException
12. A file contains only `Sam 50`. The code calls `next()`, `nextInt()`, `nextInt()`. Result? (A) second int is 0 (B) NoSuchElementException (C) compile error (D) it waits for the user to type
13. The key difference between reading the console and reading a file is: (A) a file uses different Scanner methods (B) you cannot prompt a file, so you must know its structure (C) files can only hold Strings (D) files don’t need importing
14. `grades.txt` contains `Kim 10 20 30 40 50`. What does the Grade Calculator write? (A) `Student: Kim; Average: 30.00` (B) `Average: 150.00` (C) `Student: Kim; Average: 30` (D) `Student: Kim; Average: 25.00`
15. A program wrote `average.txt` but it doesn’t appear in the Package Explorer. What should you do? (A) run the program again (B) restart Eclipse (C) right-click the project and Refresh (F5) (D) add `throws IOException`

### Answers and explanations

| Q | Answer | Why |
| --- | --- | --- |
| 1 | C | PrintWriter is the file version of `System.out` |
| 2 | B | Both are in `java.io` |
| 3 | C | Eclipse runs programs from the project root |
| 4 | B | Checked exceptions must be caught or declared |
| 5 | A | 9.50 × 10 = 95.0, shown to 2 dp |
| 6 | B | Output waits in the buffer; closing flushes it |
| 7 | C | `\\` is one backslash |
| 8 | B | Compound assignment shorthand |
| 9 | C | Scanner’s `next...` methods throw InputMismatchException |
| 10 | B | PrintWriter starts the file again |
| 11 | C | The other three are unchecked |
| 12 | B | There is no more data to read |
| 13 | B | Files can’t answer prompts |
| 14 | A | (10+20+30+40+50) / 5 = 30, formatted `%.2f` |
| 15 | C | Eclipse doesn’t list new files until it refreshes |

Answers 5, 9, 12 and 14 were checked by running the code with Java 21. **Score:** 13–15 go to Lab 5; 10–12 re-read the matching sections; under 10, run Programs A and B yourself first.

## Quick reference and glossary

```java
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.PrintWriter;
import java.util.Scanner;

public class FileTemplate {
    public static void main(String[] args) throws FileNotFoundException {
        // READ (file must be in the Eclipse project root)
        Scanner in = new Scanner(new FileReader("input.txt"));
        String name = in.next();        // or nextLine() for text with spaces
        int count = in.nextInt();
        double value = in.nextDouble();
        in.close();

        // PROCESS
        double result = count * value;

        // WRITE (created or replaced; Refresh Eclipse to see it)
        PrintWriter out = new PrintWriter("output.txt");
        out.printf("%s %d %.2f%n", name, count, result);
        out.close();                    // never forget: flushes the buffer
    }
}
```

| Term | Meaning |
| --- | --- |
| File | Data stored on secondary storage (disk) |
| Data stream | A sequence of data handled the same way whatever the device |
| `FileReader` | `java.io` class that opens a text file for reading; wrap it in a Scanner |
| `PrintWriter` | `java.io` class that writes text to a file with `print`/`println`/`printf` |
| Relative path | A filename found from the current working directory, e.g. `"prog.txt"` |
| Absolute path | The full location, e.g. `"M:\\prog.txt"` |
| Project root | The top folder of an Eclipse project; where relative files are read and written |
| Schema | The structure of a file: which items, in what order, separated how, of what type |
| Record | One set of related items in a file, e.g. one student’s line |
| Exception | An error that happens while the program runs |
| Checked exception | An exception the compiler forces you to catch or declare (e.g. FileNotFoundException) |
| `throws` clause | Declares that a method may pass an exception on instead of handling it |
| Buffer | Memory where output waits before being written to disk |
| `close()` | Releases the file; for output, also flushes the buffer |
| `flush()` | Writes the buffer to disk without closing |
| `+=` | Compound assignment: `a += b` means `a = a + b` |
| Organise Imports | Eclipse Ctrl+Shift+O: adds missing import lines |

**Next:** work through Lab 5. Lecture 6 introduces decisions: `if` statements and Boolean logic.
