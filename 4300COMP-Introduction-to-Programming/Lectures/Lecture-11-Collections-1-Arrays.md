# Lecture 11 — Collections #1: Fixed-Size Arrays

**Module:** 4300COMP Introduction to Programming · **Language:** Java

## Overview

Every variable so far has held **one** value: one `int`, one `String`. Real programs handle **collections** of values: a class list, a week of readings, 24 hours of login failures. Lecture 11 introduces Java's first collection, the **array**: one variable that holds many values of the same type, each in a numbered position. You will learn to declare, create, fill and read arrays, and see why **arrays and `for` loops go together**. These notes rewrite the official Lecture 11 slides in plain English. Every program and output shown was compiled and run with Java 21 (javac on the command line, not Eclipse).

**By the end you should be able to:**

1. Explain what a collection is, and the difference between fixed-size and variable-size collections.
2. Declare and create an array with `new`, and with an initialiser list `{ ... }`.
3. Explain **indices**: why the first element is `[0]` and the last is `[length - 1]`.
4. Assign to and read from array elements, and use an element anywhere an ordinary variable can go.
5. Use `.length` and a `for` loop to visit every element.
6. Write the common array operations: initialise, input, print, sum, average, largest (with its position), smallest, search and count.
7. Recognise and fix `ArrayIndexOutOfBoundsException`.
8. Explain why `b = a` does not copy an array, and how to copy one properly.

**Learning outcomes:** MLO1 (collections and the algorithms that process them), MLO2 (the `java.util.Arrays` API for sorting and printing, from the tutorial's supplementary task), MLO3 (problems that need all the data kept, such as "list everything above the average").

**Matching lab:** Lab 11 (official Tutorial 11: Collections #1).

**What you need from earlier lectures:** types (Lecture 2), `Scanner` and file reading (Lectures 4–5), `if` (Lecture 6) and especially the `for` loop and off-by-one errors (Lecture 9).

## 1. Collections

Many applications work with **collections** of elements:

| Application | Collection of… |
| --- | --- |
| Personal organiser | appointments |
| Library catalogue | books |
| Student record system | students and their marks |
| Bank account management | accounts and transactions |

The elements usually need **processing**: reading their values, and changing them.

Java offers two kinds of collection:

| Kind | Size | Notes from the slides |
| --- | --- | --- |
| **Fixed-size arrays** | Chosen when the array is created; cannot change | Efficient |
| **Variable-size collections** | Grow and shrink as needed | More flexible, with some extra overhead |

This lecture covers **arrays**. Variable-size collections come next.

## 2. What is an array?

So far, each variable held one value (a **scalar** variable):

```java
int totalCost = 100;
String message = "Hello";
```

An **array** holds **more than one value at a time**, all of the **same type**. The slides compare it to a spreadsheet column: one column, many rows, each row with a position number and a value.

| Index (position) | 0 | 1 | 2 | … |
| --- | ---: | ---: | ---: | --- |
| Value | 10 | 14 | 36 | … |

- Positions are called **indices** (singular: **index**).
- Indices **start at 0** and go up by one.
- Each position holds one value, called an **element**.

In the slides' picture, position 0 holds 10, position 1 holds 14, position 2 holds 36, and so on.

A spreadsheet with **several** columns would be a **two-dimensional** array. The slides say these are **not covered in this module**.

## 3. Declaring and creating an array

Creating an array takes two steps.

**Step 1: declare** a variable that can refer to an array. The **square brackets** `[]` say "this is an array, not a single value":

```java
int[] intArray;
```

This says *what type* of values the array holds (`int`) but **not how many**. No array exists yet.

**Step 2: create** the array with the `new` operator, giving its **size**:

```java
intArray = new int[6];
```

Now `intArray` refers to an array with 6 positions: indices 0 to 5.

Both steps on one line (the usual way):

```java
int[] intArray = new int[6];
```

### Facts about a new array (all verified)

- Its size is **fixed**. You cannot add a seventh element later.
- Every element starts with a **default value**: `0` for `int`, `0.0` for `double`, `false` for `boolean`, and `null` (no object) for `String`.
- Its size is stored in `intArray.length` (here 6). **No brackets**: `length` is not a method for arrays.
- The size can come from a variable: `new double[n]`, as long as `n` has a value. A negative size causes `NegativeArraySizeException` when the program runs.

Java also accepts `int intArray[]` (brackets after the name; the slide's `String args []` uses this form). Both mean the same, but `int[] intArray` is the normal style because the type ("array of int") is all in one place.

## 4. Assigning values to elements

Use the array name and an index in square brackets, exactly like an ordinary assignment:

```java
intArray[0] = 10;    // position 0
intArray[1] = 14;    // position 1
intArray[2] = 36;    // position 2: the THIRD element
```

Because counting starts at 0, the **third** position has index **2**. The element with index `i` is element number `i + 1`.

## 5. Initialiser lists

If you know the values when you write the program, list them in braces. Java counts them and creates an array of exactly that size:

```java
int[] intArray = {1, 2, 3, 4};                                     // length 4
String[] seasons = {"Autumn", "Spring", "Summer", "Winter"};
boolean[] boolArray = {false, true, false, true};
```

An initialiser list can only be used **in the declaration**. Writing `intArray = {4, 5, 6};` on a later line does not compile (`error: illegal start of expression`). To replace the contents later, assign elements one by one, or use `intArray = new int[] {4, 5, 6};`.

## 6. Accessing elements

To read a value, write the array name and the index:

```java
System.out.println(intArray[2]);
```

An element such as `intArray[2]` behaves like an ordinary variable. It can go on the **left** of an assignment, or **inside an expression**:

```java
intArray[2] = 12;                     // change it
int thirdValue = intArray[2] + 3;     // use it
```

### Program A — ArrayExample (from the slides)

```java
public class ArrayExample {
    public static void main(String[] args) {
        int[] intArray = {1, 2, 3, 4};
        intArray[0] = 5;
        intArray[1] = 2 * intArray[0];
        int thirdValue = intArray[2];
        System.out.println("First value is " + intArray[0]);
        System.out.println("Second value is " + intArray[1]);
        System.out.println("Third value is " + thirdValue);
    }
}
```

**Output (verified):**

```text
First value is 5
Second value is 10
Third value is 3
```

| Statement | Array after it |
| --- | --- |
| `int[] intArray = {1, 2, 3, 4};` | `[1, 2, 3, 4]` |
| `intArray[0] = 5;` | `[5, 2, 3, 4]` |
| `intArray[1] = 2 * intArray[0];` | `[5, 10, 3, 4]` |
| `int thirdValue = intArray[2];` | unchanged; `thirdValue` is 3 |

**Slide note:** the slide prints with curly "smart" quotes (`“First value is “`), which Java rejects with `error: illegal character: '“'`. Type straight quotes.

## 7. Iteration: arrays and for loops

The index does not have to be a literal number. Any `int` expression works, including a variable:

```java
int index = 1;
intArray[index] = 12;
```

Changing `index` by hand is awkward, so we let a **`for` loop** do it. A `for` loop is a counting loop (Lecture 9), and visiting positions 0, 1, 2, … is counting. Visiting every element of a collection like this is called **iterating over** or **traversing** the array.

```java
int[] intArray = new int[5];
for (int index = 0; index < 5; index++) {
    intArray[index] = index;
}
```

Better: replace the literal `5` with the array's `length`, so the loop is always the right size even if the array changes:

```java
int[] intArray = new int[5];
for (int index = 0; index < intArray.length; index++) {
    intArray[index] = index;
    System.out.println(intArray[index]);
}
```

**Output (verified):** `0`, `1`, `2`, `3`, `4` on separate lines.

**The standard loop for an array:** `for (int i = 0; i < array.length; i++)`. Start at **0**, continue while `i` is **less than** `length`. Those two details prevent almost every off-by-one error.

## 8. Going out of bounds

The valid indices of an array are `0` to `length - 1`. Using any other index **compiles** but **crashes** when that line runs:

```java
int[] marks = {55, 72, 64, 90, 38};
for (int i = 0; i <= marks.length; i++) {      // bug: <= instead of <
    System.out.println("marks[" + i + "] = " + marks[i]);
}
```

**Run (verified):** the five marks are printed, then:

```text
Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: Index 5 out of bounds for length 5
```

The message tells you the bad index (5) and the array's length (5). Fix: `i < marks.length`. The last element is `marks[marks.length - 1]`, never `marks[marks.length]`.

**Cyber security link:** Java **checks every index** and stops the program rather than touching memory outside the array. Languages such as C do not check. There, writing past the end of an array (a **buffer overflow**) silently overwrites neighbouring memory. Buffer overflows have been behind many serious real-world attacks. Java's bounds checking is one reason it is called a memory-safe language.

## 9. Common array operations

The slides list the operations you will write again and again: initialisation, data input, output, and finding the largest, smallest, sum and average. They assume these declarations:

```java
double[] sales = new double[10];
int index, maxIndex;
double largestSale, sum, average;
```

### Initialisation

```java
for (index = 0; index < sales.length; index++) {
    sales[index] = 10.00;
}
```

### Data input from the user

```java
for (index = 0; index < sales.length; index++) {
    System.out.println("Enter sales value");
    sales[index] = console.nextDouble();
}
```

### Printing the values

```java
for (index = 0; index < sales.length; index++) {
    System.out.print(sales[index] + " ");
}
```

### Sum and average

```java
sum = 0;
for (index = 0; index < sales.length; index++) {
    sum = sum + sales[index];
}
if (sales.length != 0) {
    average = sum / sales.length;
} else {
    average = 0.0;
}
```

The `length != 0` check looks unnecessary here (the array has 10 elements), but it is a good habit: when the size comes from input (`new double[n]`), `n` may be 0, and dividing by zero would give a wrong result.

### Largest value (maximum)

```java
largestSale = sales[0];
for (index = 1; index < sales.length; index++) {
    if (sales[index] > largestSale) {
        largestSale = sales[index];
    }
}
```

Start with the **first element** as "largest so far" (not 0: what if every sale were negative?), then compare from index **1**. This assumes the array has at least one element.

The slides declare `maxIndex` but do not use it. Recording **where** the largest value is, as well as what it is, is often more useful. The complete program below does both.

### Program B — The sales operations as one program

```java
import java.util.Scanner;

public class SalesDemo {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        double[] sales = new double[5];
        int index, maxIndex;
        double largestSale, sum, average;

        // Initialisation: every element set to 10.00
        for (index = 0; index < sales.length; index++) {
            sales[index] = 10.00;
        }

        // Data input from the user
        for (index = 0; index < sales.length; index++) {
            System.out.print("Enter sales value " + (index + 1) + ": ");
            sales[index] = console.nextDouble();
        }
        System.out.println();

        // Print the values
        for (index = 0; index < sales.length; index++) {
            System.out.print(sales[index] + " ");
        }
        System.out.println();

        // Sum and average
        sum = 0;
        for (index = 0; index < sales.length; index++) {
            sum = sum + sales[index];
        }
        if (sales.length != 0) {
            average = sum / sales.length;
        } else {
            average = 0.0;
        }

        // Largest value, and where it is
        largestSale = sales[0];
        maxIndex = 0;
        for (index = 1; index < sales.length; index++) {
            if (sales[index] > largestSale) {
                largestSale = sales[index];
                maxIndex = index;
            }
        }

        System.out.printf("Sum: %.2f%n", sum);
        System.out.printf("Average: %.2f%n", average);
        System.out.printf("Largest sale: %.2f at index %d (sale number %d)%n", largestSale, maxIndex, maxIndex + 1);
        console.close();
    }
}
```

(The array has 5 elements here instead of 10, to keep testing short.)

**Run (verified), input `120.50 89.99 310.00 45.25 199.95`:**

```text
120.5 89.99 310.0 45.25 199.95
Sum: 765.69
Average: 153.14
Largest sale: 310.00 at index 2 (sale number 3)
```

(The prompts are left out above. The initialisation to 10.00 is immediately replaced by the input; it is there to show the pattern.)

### More operations you will need

| Operation | Pattern |
| --- | --- |
| **Smallest** | Like largest, with `<` |
| **Count** matching elements | `count = 0`; in the loop, `if (condition) count++` |
| **Search** for a value | Loop; when `array[i] == target`, record `i` (start with `-1` meaning "not found") |
| **Reverse order** | `for (int i = array.length - 1; i >= 0; i--)` |
| **Two passes** | One loop to work out the average, a second loop to list values above it |

The last row shows the real reason arrays matter. Without an array, once you read a value and move on, it is gone. "List every value above the average" needs **all** the values **after** the average is known, so they must be stored.

## 10. Arrays are references: copying and printing

An array variable does not hold the elements directly. It holds a **reference**: the location of the array object in memory. Two consequences surprise beginners:

```java
int[] original = {1, 2, 3};
int[] sameArray = original;          // copies the REFERENCE, not the values
sameArray[0] = 99;
System.out.println(original[0]);     // 99!
```

Both variables now refer to **the same** array, so a change through one is visible through the other (verified). To make an independent copy, create a new array and copy each element:

```java
int[] realCopy = new int[original.length];
for (int i = 0; i < original.length; i++) {
    realCopy[i] = original[i];       // copies each VALUE
}
```

Changing `realCopy[1]` then leaves `original[1]` unchanged (verified).

**Printing an array directly does not show its contents.** `System.out.println(original);` prints something like `[I@61bbe9ba` (verified): a type code and an identity number, which change between runs. Either loop over the elements, or use the `Arrays` class from the Java API:

```java
import java.util.Arrays;
...
System.out.println(Arrays.toString(original));   // [99, 2, 3]
```

Similarly, `==` between two arrays checks whether they are **the same array**, not whether they hold equal values. `original == sameArray` is `true`; an array that merely contains the same numbers gives `false` (both verified).

**The `Arrays` class** (`java.util.Arrays`) is part of the Java API. Tutorial 11's supplementary task uses its `sort` method, which puts the elements into ascending order **in place** (it changes the array). See the official documentation: [java.util.Arrays](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Arrays.html).

## 11. Parallel arrays

To store related data, such as a student's name **and** mark, you can use two arrays of the same length where the same index refers to the same student:

```java
String[] names = {"Priya", "Tom", "Aisha"};
int[] marks = {72, 48, 91};        // marks[i] belongs to names[i]
```

Find the index of the best mark, then use that index in **both** arrays: `names[best]` and `marks[best]`. Lab 11 practises this. (Later in the module, classes give a tidier way to group related data.)

## 12. length versus length()

| Thing | How to get its size | Wrong version gives |
| --- | --- | --- |
| Array | `myArray.length` (no brackets) | `myArray.length()` → `error: cannot find symbol` (method `length()`) |
| String | `myString.length()` (brackets) | `myString.length` → `error: cannot find symbol` (variable `length`) |

Both errors were verified with javac.

## 13. Common mistakes

| Mistake | Symptom (verified) | Fix |
| --- | --- | --- |
| `i <= array.length` in a loop | `ArrayIndexOutOfBoundsException: Index 5 out of bounds for length 5` | `i < array.length` |
| Last element as `array[array.length]` | Same exception | `array[array.length - 1]` |
| Loop starting at 1 | First element skipped (no error!) | Start at 0 |
| `array = {1, 2, 3};` after the declaration | `error: illegal start of expression` | Use `{...}` only when declaring, or `new int[] {...}` |
| Using an array before `new` | `error: variable a might not have been initialized` | `int[] a = new int[size];` |
| `array.length()` | `error: cannot find symbol` | `array.length` |
| A `double` index: `a[1.5]` | `error: incompatible types: possible lossy conversion from double to int` | Indices are `int` |
| Wrong element type: `int n = words[0];` (a `String`) | `error: incompatible types: String cannot be converted to int` | Match the types |
| Printing the array variable | `[I@...` | A loop, or `Arrays.toString` |
| `b = a` to copy | Changes to `b` also change `a` | Copy element by element |
| Using an element of a new `String[]` | `null`; calling a method on it throws `NullPointerException` | Fill the array first |
| Largest starts at 0 | Wrong when every value is negative | Start at `array[0]` |

## 14. Check yourself — 15 multiple-choice questions

Questions 1–8 use `int[] a = {4, 8, 15, 16, 23, 42};`

1. What is `a[2]`? (A) 8 (B) 15 (C) 16 (D) 4
2. What is `a.length`? (A) 5 (B) 6 (C) 7 (D) 42
3. What is `a[a.length - 1]`? (A) 23 (B) 42 (C) an exception (D) 6
4. What is `a[1] + a[4]`? (A) 31 (B) 24 (C) 23 (D) 39
5. With `int i = 3;`, what is `a[i - 1]`? (A) 16 (B) 15 (C) 8 (D) 23
6. What is `a[a[0]]`? (A) 4 (B) 16 (C) 23 (D) an exception
7. What happens with `a[6]`? (A) 0 (B) 42 (C) compile error (D) `ArrayIndexOutOfBoundsException`
8. After `a[0] = a[5] / 2;`, how many elements are even? (A) 2 (B) 3 (C) 4 (D) 5
9. What does `new int[4]` contain at first? (A) four random numbers (B) `null` (C) four zeros (D) nothing until assigned; using it is an error
10. What does `new String[3]` contain at first? (A) three empty strings `""` (B) three `null`s (C) `"null"` (D) nothing
11. What does `int[] t = {3, 1, 2}; t[t[1]] = 7;` leave in `t`? (A) `{7, 1, 2}` (B) `{3, 7, 2}` (C) `{3, 1, 7}` (D) an exception
12. `int[] b = a; b[0] = 99;` What is `a[0]` now? (A) its old value (B) 99 (C) 0 (D) an error
13. Which correctly gives the number of elements in an array `nums`? (A) `nums.length()` (B) `nums.size()` (C) `nums.length` (D) `length(nums)`
14. Why does the slides' maximum algorithm start the loop at index 1? (A) index 0 is invalid (B) `largestSale` already holds element 0 (C) arrays start at 1 (D) to avoid an exception
15. What does `Arrays.sort(numbers)` do to `{23, 6, 47, 35, 2, 15}`? (A) returns a sorted copy and leaves `numbers` unchanged (B) changes `numbers` to `{2, 6, 15, 23, 35, 47}` (C) sorts into descending order (D) prints the sorted values

### Answers

| Q | Answer | Why |
| --- | --- | --- |
| 1 | B | Index 2 is the third element (verified) |
| 2 | B | Six values (verified) |
| 3 | B | The last element (verified) |
| 4 | A | 8 + 23 (verified) |
| 5 | B | `a[2]` (verified) |
| 6 | C | `a[0]` is 4, so `a[4]` is 23 (verified) |
| 7 | D | Valid indices are 0 to 5; it compiles but fails when run |
| 8 | B | Array becomes `{21, 8, 15, 16, 23, 42}`; even: 8, 16, 42 (verified) |
| 9 | C | Default value for `int` (verified) |
| 10 | B | Default for `String` is `null` (verified) |
| 11 | B | `t[1]` is 1, so `t[1] = 7` (verified: prints 372) |
| 12 | B | `b` and `a` refer to the same array (verified) |
| 13 | C | Arrays use the `length` field, not a method |
| 14 | B | Element 0 is the starting "largest so far" |
| 15 | B | `sort` changes the array in place, ascending (verified) |

**Score:** 13–15 go to Lab 11; 10–12 re-read the sections for the ones you missed; under 10, re-run Programs A and B and draw each array as a row of boxes with indices.

## 15. Quick reference

```java
int[] a = new int[5];                 // 5 zeros, indices 0..4
int[] b = {10, 14, 36};               // initialiser list (declaration only)
String[] s = {"Autumn", "Winter"};

a[0] = 7;                             // assign
int x = a[0] + 1;                     // read
int n = a.length;                     // size (no brackets)
int last = a[a.length - 1];           // last element

for (int i = 0; i < a.length; i++) {  // the standard traversal
    // use a[i]
}

int max = a[0];                       // largest
for (int i = 1; i < a.length; i++) {
    if (a[i] > max) { max = a[i]; }
}

import java.util.Arrays;
Arrays.sort(a);                       // ascending, in place
System.out.println(Arrays.toString(a));
```

## 16. Glossary

| Term | Meaning |
| --- | --- |
| Collection | A group of values handled together |
| Scalar variable | A variable holding a single value |
| Array | A fixed-size collection of values of one type, accessed by index |
| Element | One value stored in an array |
| Index | The position number of an element, starting at 0 |
| `new` | Operator that creates an array (or object) |
| Initialiser list | `{...}` values that create and fill an array in its declaration |
| `length` | The number of elements in an array |
| Traverse / iterate | Visit every element in turn, usually with a `for` loop |
| `ArrayIndexOutOfBoundsException` | Runtime error from using an index outside `0` to `length - 1` |
| Default value | The starting value of each element: 0, 0.0, false or null |
| Reference | The location of an array (or object) in memory; what an array variable holds |
| Aliasing | Two variables referring to the same array |
| Parallel arrays | Arrays of the same length where the same index refers to the same item |
| Buffer overflow | Writing past the end of an array in a language without bounds checking; a classic security flaw |
| `java.util.Arrays` | A Java API class with helpers such as `sort` and `toString` |

## 17. Summary

- A collection holds many values; Java has fixed-size **arrays** and variable-size collections.
- Declare with `type[] name`, create with `new type[size]` or an initialiser list `{...}`.
- Indices run from **0** to **length − 1**; anything else throws `ArrayIndexOutOfBoundsException`.
- An element (`a[i]`) works anywhere an ordinary variable does.
- Iteration and arrays go together: `for (int i = 0; i < a.length; i++)`.
- The common operations are initialise, input, output, sum, average, largest/smallest (with position), count and search.
- An array variable holds a reference: `b = a` shares the array, and printing it shows `[I@...`; copy element by element and use `Arrays.toString` to print.

**Next:** work through Lab 11. The next lecture moves on to **variable-size** collections.
