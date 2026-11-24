# Lab 11 — Collections #1 (Arrays) Hands-on Workbook (20 Tasks)

**Module:** 4300COMP Introduction to Programming · **Language:** Java

## How to use this lab

This lab has **20 hands-on tasks** on Lecture 11: declaring, creating and filling arrays, indices and `length`, iterating with `for`, out-of-bounds errors, references and copying, and the common array algorithms. **All official Tutorial 11 tasks and the supplementary task are included** (Tasks 2, 4, 11, 12 and 16), marked "official".

**Learning outcomes:** MLO1 (arrays and array algorithms), MLO2 (the `java.util.Arrays` API in Tasks 8 and 16), MLO3 (Tasks 18–20 turn specifications into programs).

**Setup:** create a Java project called **Lab11** in Eclipse (untick *Create module-info.java*). One class per task, with `main`. Data files go in the **project folder**. Tutorial 11 reminds you that you will make errors: read Eclipse's messages and use the lecture notes to fix them.

**Rules for this lab:**

1. **Draw the array.** For any task that confuses you, draw a row of boxes with the index under each box and the value inside.
2. **Use the standard loop:** `for (int i = 0; i < array.length; i++)`. Never hard-code the size in the loop if you can use `length`.
3. **Predict before you run.**
4. Use the hints only after a real attempt.

The **tracker** is near the end, followed by the **answer key**. Every answer was compiled and run with Java 21 (javac on the command line, not Eclipse) with the data shown.

## Part A — Creating and reading arrays (Tasks 1–5)

### Task 1 — Create arrays and inspect them

**Class:** `Task01Create` · **Goal:** see what `new` gives you before you store anything.

1. Create arrays of size 3 of each type: `int`, `double`, `boolean`, `String`.
2. **Predict** the value of element `[0]` of each, then print them.
3. Print the `length` of one of them.
4. Create an array whose size comes from the user: read `n`, then `new int[n]`. Print its length. What happens if the user types `-1`?
5. Declare `int[] early;` and try to set `early[0] = 5;` without using `new`. What does the compiler say?

- **Hint 1:** default values: zero for numbers, `false`, and `null` for `String`.
- **Hint 2:** `length` has no brackets for arrays.

### Task 2 — Official Tutorial 11, Task 1

**Class:** `Task02Official` · **Goal:** assign, change and combine elements.

Write a program that:

1. creates an `int` array called `intArray` of size 5;
2. stores the values 21, 33, 58, 17 and 9 in it;
3. changes the value of the **second** element to 3;
4. adds together the values in the **third** and **fourth** elements and stores the result in the **fifth** element;
5. prints the second, third and fifth elements.

**Before running,** write down the index of "second", "third", "fourth" and "fifth", and the expected output.

- **Hint 1:** the second element is index 1.
- **Hint 2:** step 4 is one statement: `intArray[4] = intArray[2] + intArray[3];`

### Task 3 — Predict index expressions

**Class:** `Task03Predict` · **Goal:** read array expressions fluently.

Use `int[] a = {4, 8, 15, 16, 23, 42};`. Predict each, then check by printing them all in one program (run them **in order**, because (g) changes the array).

| | Expression | Prediction | Actual |
| --- | --- | --- | --- |
| a | `a[2]` | | |
| b | `a.length` | | |
| c | `a[a.length - 1]` | | |
| d | `a[1] + a[4]` | | |
| e | with `int i = 3;`, `a[i - 1]` | | |
| f | `a[a[0]]` | | |
| g | after `a[0] = a[5] / 2;`, `a[0]` | | |
| h | after (g), the number of even elements (use a loop) | | |
| i | `String[] s = {"red", "green", "blue"};` then `s[1].length()` | | |
| j | `s.length` | | |
| k | `int[] t = {3, 1, 2}; t[t[1]] = 7;` then print `t[0]`, `t[1]`, `t[2]` with no spaces | | |
| l | `int[] r = new int[4];` filled with `r[k] = k * k`; then `r[3]` and `r[r.length - 2]` | | |

Score yourself out of 12.

- **Hint 1:** for (f), work from the inside out: what is `a[0]`?
- **Hint 2:** (i) is a `String` method, so it has brackets.

### Task 4 — Official Tutorial 11, Task 2

**Class:** `Task04Official` · **Goal:** iterate over a `String` array.

1. Create a `String` array `strArray` initialised with `"This"`, `"is"`, `"a"`, `"String"`, `"Array"`.
2. Use a `for` loop to print the values. Print them on one line, separated by spaces.
3. Add a second loop that prints each value on its own line with its index: `0: This`.
4. Add a third loop that prints them in **reverse** order.
5. Add a sixth word to the initialiser list. Which of your loops needed changing? (If any did, you hard-coded the size: fix it with `length`.)

- **Hint 1:** reverse: start at `strArray.length - 1`, continue while `i >= 0`, use `i--`.

### Task 5 — Trace an array on paper

**Class:** `Task05Trace` · **Goal:** track an array's contents statement by statement.

Draw the array after **each** statement, then run the code with a print after each line to check.

```java
int[] v = new int[4];
v[0] = 5;
v[3] = v[0] * 2;
v[1] = v[3] - v[0];
v[2] = v[1] + v[3];
v[0] = v[v.length - 1];
for (int i = 1; i < v.length; i++) {
    v[i] = v[i] + v[i - 1];
}
```

What are the final contents? Describe in words what the last loop does.

- **Hint 1:** after the first line, `v` is `[0, 0, 0, 0]`.
- **Hint 2:** in the loop, each element gets the **new** value of the one before it.

## Part B — Find and fix (Tasks 6–10)

### Task 6 — Out-of-bounds clinic

**Class:** `Task06Bounds` · **Goal:** cause, read and fix `ArrayIndexOutOfBoundsException`.

1. Run this code. Copy the full error message, and explain both numbers in it.

```java
int[] marks = {55, 72, 64, 90, 38};
for (int i = 0; i <= marks.length; i++) {
    System.out.println("marks[" + i + "] = " + marks[i]);
}
```

2. Fix it.
3. Write one line that prints the **last** mark without using the number 4.
4. What happens with `marks[-1]`? Does it compile? Does it run?
5. Why does the program print five marks **before** crashing? What does that tell you about when Java checks indices?

- **Hint 1:** valid indices are 0 to `length - 1`.

### Task 7 — Array bug hunt (8 bugs)

**Class:** `Task07Buggy` · **Goal:** fix compile, runtime and logic errors in array code.

This program should print `Count: 5`, `Average: 30.0`, then `Scores: 10 20 30 40 50`, then `Last: 50`. It has **8 bugs**. Fix them all, then record each in a table (line, problem, kind of error, fix).

```java
public class Task07Buggy {
    public static void main(String[] args) {
        int[] scores = new int[5];
        scores = {10, 20, 30, 40, 50};
        int total;
        for (int i = 1; i <= scores.length; i++) {
            total = total + scores[i];
        }
        double average = total / scores.length;
        System.out.println("Count: " + scores.length());
        System.out.println("Average: " + average);
        System.out.println("Scores: " + scores);
        System.out.println("Last: " + scores[scores.length]);
    }
}
```

- **Hint 1:** javac only reports the first problem (3 errors on line 4) until you fix it. Keep going.
- **Hint 2:** two bugs are in the `for` header; one is in the division; three are in the print lines.

### Task 8 — Printing and comparing arrays

**Class:** `Task08PrintCompare` · **Goal:** see that an array variable is a reference.

1. Create `int[] a = {1, 2, 3};` and print it with `System.out.println(a);`. What appears? Run it twice. Does it change?
2. Import `java.util.Arrays` and print `Arrays.toString(a)`.
3. Create `int[] b = {1, 2, 3};`. Print `a == b`. Is that what you expected?
4. Look up `Arrays.equals` in the [Arrays documentation](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Arrays.html) and use it to compare `a` and `b` properly. What does it return?

- **Hint 1:** `==` asks "are these the same array?", not "do they hold the same values?".

### Task 9 — Sharing versus copying

**Class:** `Task09Copy` · **Goal:** understand aliasing.

```java
int[] original = {1, 2, 3};
int[] sameArray = original;
sameArray[0] = 99;
System.out.println(original[0]);
```

1. Predict, then run. Explain the result using the word **reference**.
2. Write a loop that makes a **real** copy, `realCopy`. Change `realCopy[1]` to 42 and show that `original[1]` is unchanged.
3. Draw a diagram: two variable boxes, one array, and arrows. Then a second diagram after the real copy.
4. **Why it matters:** a program keeps a list of allowed ports, and a function makes a "backup" with `backup = allowed;` before editing. What goes wrong?

### Task 10 — length, length() and null

**Class:** `Task10LengthNull` · **Goal:** avoid two very common confusions.

1. Write `int[] nums = new int[3];` and try `nums.length()`. Write down the error. Fix it.
2. Write `String word = "hello";` and try `word.length`. Write down the error. Fix it.
3. Create `String[] names = new String[3];` and print `names[0]`. Then print `names[0].length()`. Copy the exception.
4. Write a rule in your own words for when to use brackets after `length`.

- **Hint 1:** arrays: field `length`. Strings: method `length()`.

## Part C — Common array algorithms (Tasks 11–15)

### Task 11 — Official Tutorial 11, Task 3: average

**Class:** `Task11Average` · **Goal:** total an array in a loop.

Create an `int` array initialised with `23, 6, 47, 35, 2, 15`. Use a `for` loop to calculate the **average** of the values. Print the sum and the average to 2 decimal places.

1. Work out the expected sum and average by hand first.
2. What would the average be if you divided two `int`s? Which is correct?

- **Hint 1:** `(double) sum / numbers.length`.

### Task 12 — Official Tutorial 11, Task 4: smallest, largest and odd numbers

**Class:** `Task12MinMaxOdd` · **Goal:** do several jobs in one traversal.

Extend Task 11 so that it also:

1. finds the **smallest** and **largest** numbers;
2. prints only the **odd** numbers, from inside the same `for` loop. The tutorial says it should display 23, 47, 35 and 15.

Then: add `-7` to the array. Is it printed as odd? (Test it: does `-7 % 2 != 0` work where `-7 % 2 == 1` would not?)

- **Hint 1:** start `smallest` and `largest` at `numbers[0]`.
- **Hint 2:** a number is odd when `number % 2 != 0`.

### Task 13 — Read into an array, print backwards

**Class:** `Task13Reverse` · **Goal:** fill an array from input; traverse it backwards.

Read 7 whole numbers from the user into an array, then print them in reverse order.

Test: `3 1 4 1 5 9 2` → `Reversed: 2 9 5 1 4 1 3`

Why is this impossible **without** an array (or 7 separate variables)?

- **Hint 1:** make the size a constant, `final int SIZE = 7;`.

### Task 14 — Search and count

**Class:** `Task14Search` · **Goal:** the linear search pattern.

A firewall log has recorded these destination ports:

```java
int[] ports = {22, 80, 443, 8080, 80, 3389, 443, 80};
```

Ask the user for a port. Print where it **first** appears and how many times it appears, or that it was not found.

| Input | Expected |
| --- | --- |
| `80` | `80 first found at index 1, appears 3 time(s).` |
| `3389` | first found at index 5, appears 1 time(s) |
| `21` | `21 not found.` |

Then: why is `-1` a good starting value for "index not found yet"?

- **Hint 1:** loop over every element; when it equals the target, add 1 to the count, and record the index only if none has been recorded yet.

### Task 15 — The slides' sales operations, complete

**Class:** `Task15Sales` · **Goal:** put every common operation from the slides into one working program.

Using the slides' declarations (`double[] sales`, `int index, maxIndex`, `double largestSale, sum, average`), but with an array of **5**:

1. initialise every element to 10.00;
2. read 5 sales values from the user;
3. print them on one line;
4. calculate the sum and average (with the slides' `length != 0` check);
5. find the largest sale **and its index** (`maxIndex`, which the slides declare but never use);
6. add the **smallest** sale and its index.

Test: `120.50 89.99 310.00 45.25 199.95` → sum 765.69, average 153.14, largest 310.00 at index 2, smallest 45.25 at index 3.

## Part D — Official supplementary task and integration (Tasks 16–20)

### Task 16 — Official Tutorial 11, supplementary: sort the array

**Class:** `Task16Sort` · **Goal:** research and use a Java API method.

Tutorial 11 asks you to research how Java sorts an array, then sort the values from Task 3 (`23, 6, 47, 35, 2, 15`) and print them in ascending order. The tutorial links a W3Schools page; also read the official [Arrays documentation](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Arrays.html) for `sort(int[] a)`.

1. Answer from the documentation: what does `sort` **return**? Does it change the original array?
2. Write the program: sort, then print with a `for` loop **and** with `Arrays.toString`.
3. After sorting, what are the smallest and largest values? Where are they? How could you have found them **without** the loop from Task 12?
4. How would you print them in **descending** order using what you already know?

- **Hint 1:** `import java.util.Arrays;` then `Arrays.sort(numbers);`.
- **Hint 2:** descending: loop backwards over the sorted array.

### Task 17 — Parallel arrays: who came top?

**Class:** `Task17TopStudent` · **Goal:** keep related data in two arrays with matching indices.

```java
String[] names = {"Priya", "Tom", "Aisha", "Leo", "Maya"};
int[] marks = {72, 48, 91, 66, 85};
```

1. Find the **index** of the highest mark, then print `Top student: Aisha with 91`.
2. Print a neat two-column table of every name and mark with `printf`.
3. Add the lowest-scoring student.
4. What goes wrong if someone later sorts `marks` with `Arrays.sort` but not `names`?

- **Hint 1:** track `best` as an **index**, starting at 0, and compare `marks[i] > marks[best]`.

### Task 18 — Two passes: values above the average

**Class:** `Task18AboveAverage` · **Goal:** a problem that genuinely needs an array.

`readings.txt` holds the number of readings followed by the readings:

```text
6
12.5 9.0 14.25 7.75 11.0 10.5
```

Read them into an array of exactly the right size, print the average to 2 decimal places, then list every reading **above** the average.

Expected: `Average: 10.83` and `Above average: 12.5 14.25 11.0`

Explain in two sentences why this needs two loops and why the values must be stored.

- **Hint 1:** `int n = read.nextInt(); double[] readings = new double[n];`

### Task 19 — Mini-project: failed logins by hour

**Class:** `Task19LoginHours` · **Goal:** analyse a day of security data with an array.

`failed_logins.txt` holds 24 whole numbers: the failed login attempts recorded in each hour from 00:00 to 23:00.

```text
2 0 1 0 0 3 4 6 12 8 5 3
4 2 31 47 9 3 6 2 22 5 3 1
```

**Specification:**

1. Read the 24 values into an array (index = hour).
2. Print a table: hour as `HH:00`, the count, and a bar of `*` (one star per 5 failures). Mark any hour with **20 or more** failures with `<-- ALERT`.
3. Print the total failures, the **peak hour** and its count, and how many hours reached the alert level.

Expected summary lines:

```text
Total failed logins: 179
Peak hour: 15:00 (47 failures)
Hours at or above 20: 3
```

**Questions:**

1. Why is an array a natural fit here (what does the index mean)?
2. `%02d` prints `7` as `07`. Where else is zero-padding useful?
3. **Cyber security link:** a sudden spike of failed logins in one hour can indicate a password-guessing attack (brute force, as in Lab 9 Task 19). What other pattern in this data would you want to investigate? (For example, activity at unusual hours.)

- **Hint 1:** the bar is a nested loop: `for (int s = 0; s < failures[hour] / PER_STAR; s++)`.
- **Hint 2:** track the peak as an index, like Task 17.

### Task 20 — Assessment-style task: module marks analyser

**Class:** `MarksAnalyser` · **Goal:** read a data set into arrays, analyse it, and write a report file.

This is a practice task similar in skills to the module's application assessments. It is **not** an actual assessment question.

**Input** `module_marks.txt`: the number of students, then one line per student with an ID (one word) and a mark.

```text
10
S01 72
S02 38
S03 55
S04 91
S05 64
S06 47
S07 70
S08 59
S09 33
S10 81
```

**Specification:** write `marks_report.txt` containing:

1. the number of students;
2. the **mean** and the **median** mark, to 1 decimal place;
3. the lowest and highest marks;
4. the pass rate (pass = 40 or more) as `passes/students (percentage%)`;
5. how many students fall in each band: below 40, 40–59, 60–69, 70+;
6. the IDs of every student **above the mean**.

The original order of the marks must be kept (do not sort the array that matches the IDs). The **median** is the middle value of the sorted marks; with an even number of students it is the average of the two middle values.

**Expected `marks_report.txt`:**

```text
Students: 10
Mean: 61.0  Median: 61.5
Lowest: 33  Highest: 91
Pass rate: 8/10 (80.0%)
Below 40: 2
40-59:    3
60-69:    1
70+:      4
Above the mean: S01 S04 S05 S07 S10
```

**Test plan** (fill in Actual): the file above; an odd number of students (median is the middle value); every student failing; one student only.

**Plan first:** analysis (IPO), design (which arrays, which loops, why a copy is needed for the median), then implement in stages.

- **Hint 1:** an `int[] bands = new int[4];` can hold the four band counts: index 0 for below 40, and so on.
- **Hint 2:** copy `marks` into a new array with a loop, then `Arrays.sort` the copy.

## Tracker

| Task | Done | Notes / score |
| --- | --- | --- |
| 1 Create and inspect | ☐ | |
| 2 Official Task 1 | ☐ | |
| 3 Predict (out of 12) | ☐ | |
| 4 Official Task 2 | ☐ | |
| 5 Trace on paper | ☐ | |
| 6 Out-of-bounds clinic | ☐ | |
| 7 Bug hunt (out of 8) | ☐ | |
| 8 Printing and comparing | ☐ | |
| 9 Sharing vs copying | ☐ | |
| 10 length and null | ☐ | |
| 11 Official Task 3: average | ☐ | |
| 12 Official Task 4: min, max, odd | ☐ | |
| 13 Reverse | ☐ | |
| 14 Search and count | ☐ | |
| 15 Sales operations | ☐ | |
| 16 Official supplementary: sort | ☐ | |
| 17 Parallel arrays | ☐ | |
| 18 Above average | ☐ | |
| 19 Failed logins by hour | ☐ | |
| 20 Marks analyser | ☐ | |

## Reflection

1. In your own words, why does the first element have index 0 and the last `length - 1`?
2. Which task showed most clearly why arrays are needed (rather than one variable per value)?
3. Explain aliasing to a friend in two sentences.
4. Which array error did you hit most often today, and how will you avoid it?

## Answer key

All code was compiled and run with Java 21 (javac on the command line, not Eclipse). Outputs shown are actual outputs.

**Task 1.** Element `[0]` of each: `0`, `0.0`, `false`, `null`; `length` 3 (verified). `new int[-1]` throws `NegativeArraySizeException: -1` when it runs. Using `early` without `new`: `error: variable early might not have been initialized`.

**Task 2.**

```java
public class Task01Official {
    public static void main(String[] args) {
        int[] intArray = new int[5];
        intArray[0] = 21;
        intArray[1] = 33;
        intArray[2] = 58;
        intArray[3] = 17;
        intArray[4] = 9;

        intArray[1] = 3;                          // change the second element
        intArray[4] = intArray[2] + intArray[3];  // third + fourth into the fifth

        System.out.println("Second: " + intArray[1]);
        System.out.println("Third: " + intArray[2]);
        System.out.println("Fifth: " + intArray[4]);
    }
}
```

Output (verified): `Second: 3`, `Third: 58`, `Fifth: 75`. Indices: second 1, third 2, fourth 3, fifth 4.

**Task 3.** a 15 · b 6 · c 42 · d 31 · e 15 · f 23 · g 21 · h 3 · i 5 · j 3 · k `372` · l `9 4`. All verified.

**Task 4.**

```java
public class Task02Official {
    public static void main(String[] args) {
        String[] strArray = {"This", "is", "a", "String", "Array"};
        for (int i = 0; i < strArray.length; i++) {
            System.out.print(strArray[i] + " ");
        }
        System.out.println();
        for (int i = 0; i < strArray.length; i++) {
            System.out.println(i + ": " + strArray[i]);
        }
    }
}
```

Output (verified): `This is a String Array` then `0: This` … `4: Array`. Reverse: `for (int i = strArray.length - 1; i >= 0; i--)` prints `Array String a is This`. With `length` in every loop, adding a sixth word needs no loop changes.

**Task 5.** `[0,0,0,0]` → `[5,0,0,0]` → `[5,0,0,10]` → `[5,5,0,10]` → `[5,5,15,10]` → `[10,5,15,10]` → loop → `[10,15,30,40]`. The loop turns each element into a **running total** of all elements up to it.

**Task 6.** (1) Five marks, then `Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: Index 5 out of bounds for length 5`: index 5 was used on an array of length 5 (verified). (2) `i < marks.length`. (3) `System.out.println(marks[marks.length - 1]);`. (4) It compiles; when run, it throws `ArrayIndexOutOfBoundsException: Index -1 out of bounds for length 5`. (5) Java checks each index **when that line runs**, not at compile time, so the first five accesses succeed.

**Task 7.** Bugs: (1) `scores = {...}` after the declaration (`illegal start of expression`) → put the list in the declaration: `int[] scores = {10, 20, 30, 40, 50};`; (2) `int total;` → `int total = 0;`; (3) loop starts at 1, skipping `scores[0]` → start at 0; (4) `<=` → `<`; (5) `total / scores.length` is integer division → `(double) total / scores.length`; (6) `scores.length()` → `scores.length`; (7) printing `scores` shows `[I@...` → print with a loop (or `Arrays.toString`); (8) `scores[scores.length]` → `scores[scores.length - 1]`. The first compile reports 3 errors, all on line 4 (verified). Fixed program:

```java
public class Task07Fixed {
    public static void main(String[] args) {
        int[] scores = {10, 20, 30, 40, 50};
        int total = 0;
        for (int i = 0; i < scores.length; i++) {
            total = total + scores[i];
        }
        double average = (double) total / scores.length;
        System.out.println("Count: " + scores.length);
        System.out.println("Average: " + average);
        System.out.print("Scores:");
        for (int i = 0; i < scores.length; i++) {
            System.out.print(" " + scores[i]);
        }
        System.out.println();
        System.out.println("Last: " + scores[scores.length - 1]);
    }
}
```

Output (verified): `Count: 5`, `Average: 30.0`, `Scores: 10 20 30 40 50`, `Last: 50`.

**Task 8.** (1) Something like `[I@61bbe9ba` (`[I` means "array of int"); the number usually changes between runs. (2) `[1, 2, 3]`. (3) `false`: they are two different arrays. (4) `Arrays.equals(a, b)` returns `true`, because it compares the elements in order. (1)–(3) verified.

**Task 9.** (1) Prints `99`: `sameArray = original` copies the reference, so both names point at one array (verified). (2) A loop copying each element; afterwards `original[1]` is still 2 while `realCopy[1]` is 42 (verified). (4) The "backup" is the same list, so every edit also changes the backup, and there is nothing to restore.

**Task 10.** (1) `error: cannot find symbol` (symbol: method `length()`); fix `nums.length`. (2) `error: cannot find symbol` (symbol: variable `length`); fix `word.length()`. (3) Prints `null`, then `NullPointerException` (Java 21 adds a message explaining which value was null). (4) Arrays: no brackets. Strings: brackets. All verified.

**Tasks 11 and 12.**

```java
import java.util.Arrays;

public class Task0304Official {
    public static void main(String[] args) {
        int[] numbers = {23, 6, 47, 35, 2, 15};

        int sum = 0;
        int smallest = numbers[0];
        int largest = numbers[0];
        System.out.print("Odd numbers: ");
        for (int i = 0; i < numbers.length; i++) {
            sum = sum + numbers[i];
            if (numbers[i] < smallest) {
                smallest = numbers[i];
            }
            if (numbers[i] > largest) {
                largest = numbers[i];
            }
            if (numbers[i] % 2 != 0) {
                System.out.print(numbers[i] + " ");
            }
        }
        System.out.println();
        double average = (double) sum / numbers.length;
        System.out.printf("Sum: %d, average: %.2f%n", sum, average);
        System.out.println("Smallest: " + smallest + ", largest: " + largest);

        // Supplementary task: sort into ascending order
        Arrays.sort(numbers);
        System.out.print("Sorted: ");
        for (int i = 0; i < numbers.length; i++) {
            System.out.print(numbers[i] + " ");
        }
        System.out.println();
        System.out.println(Arrays.toString(numbers));
    }
}
```

Output (verified):

```text
Odd numbers: 23 47 35 15
Sum: 128, average: 21.33
Smallest: 2, largest: 47
Sorted: 2 6 15 23 35 47
[2, 6, 15, 23, 35, 47]
```

With `int` division the average would be 21, which is wrong. In Java, `-7 % 2` is `-1`, so `% 2 != 0` correctly finds negative odd numbers while `% 2 == 1` would miss them.

**Task 13.**

```java
import java.util.Scanner;

public class Reverse {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        final int SIZE = 7;
        int[] values = new int[SIZE];
        for (int i = 0; i < values.length; i++) {
            System.out.print("Value " + (i + 1) + ": ");
            values[i] = console.nextInt();
        }
        System.out.println();
        System.out.print("Reversed: ");
        for (int i = values.length - 1; i >= 0; i--) {
            System.out.print(values[i] + " ");
        }
        System.out.println();
        console.close();
    }
}
```

Output (verified): `Reversed: 2 9 5 1 4 1 3`. Without storage, the first value would be lost by the time the last is read.

**Task 14.**

```java
import java.util.Scanner;

public class Search {
    public static void main(String[] args) {
        Scanner console = new Scanner(System.in);
        int[] ports = {22, 80, 443, 8080, 80, 3389, 443, 80};
        System.out.print("Port to find: ");
        int target = console.nextInt();

        int firstIndex = -1;            // -1 means "not found yet"
        int count = 0;
        for (int i = 0; i < ports.length; i++) {
            if (ports[i] == target) {
                count++;
                if (firstIndex == -1) {
                    firstIndex = i;
                }
            }
        }
        if (firstIndex == -1) {
            System.out.println(target + " not found.");
        } else {
            System.out.println(target + " first found at index " + firstIndex + ", appears " + count + " time(s).");
        }
        console.close();
    }
}
```

`80` and `21` verified as in the table. `-1` can never be a real index, so it safely means "not found".

**Task 15.** See Lecture 11, Program B (verified: sum 765.69, average 153.14, largest 310.00 at index 2). Smallest: start `smallestSale = sales[0]; minIndex = 0;` and update when `sales[index] < smallestSale`: 45.25 at index 3.

**Task 16.** `sort` returns nothing (`void`) and sorts the array **in place**, in ascending order. Output in Tasks 11–12 above. After sorting, the smallest is `numbers[0]` (2) and the largest is `numbers[numbers.length - 1]` (47). Descending: loop from the last index down to 0.

**Task 17.**

```java
public class TopStudent {
    public static void main(String[] args) {
        String[] names = {"Priya", "Tom", "Aisha", "Leo", "Maya"};
        int[] marks = {72, 48, 91, 66, 85};          // marks[i] belongs to names[i]

        int best = 0;                                 // index of the best so far
        for (int i = 1; i < marks.length; i++) {
            if (marks[i] > marks[best]) {
                best = i;
            }
        }
        System.out.println("Top student: " + names[best] + " with " + marks[best]);
        for (int i = 0; i < names.length; i++) {
            System.out.printf("%-6s %3d%n", names[i], marks[i]);
        }
    }
}
```

Output (verified): `Top student: Aisha with 91` then the table. Lowest: Tom with 48. Sorting only `marks` breaks the link between index and student, so every name would get someone else's mark.

**Task 18.**

```java
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Scanner;

public class AboveAverage {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner read = new Scanner(new FileReader("readings.txt"));
        int n = read.nextInt();                 // how many readings follow
        double[] readings = new double[n];
        for (int i = 0; i < n; i++) {
            readings[i] = read.nextDouble();
        }
        read.close();

        double sum = 0;
        for (int i = 0; i < readings.length; i++) {
            sum = sum + readings[i];
        }
        double average = sum / readings.length;
        System.out.printf("Average: %.2f%n", average);

        System.out.print("Above average: ");    // second pass: needs every value again
        for (int i = 0; i < readings.length; i++) {
            if (readings[i] > average) {
                System.out.print(readings[i] + " ");
            }
        }
        System.out.println();
    }
}
```

Output (verified): `Average: 10.83`, `Above average: 12.5 14.25 11.0`. The average is only known after every value has been read, and then every value is needed again to compare with it.

**Task 19.**

```java
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Scanner;

public class LoginHours {
    public static void main(String[] args) throws FileNotFoundException {
        final int HOURS = 24;
        final int ALERT_LEVEL = 20;       // failed logins in one hour that need a look
        final int PER_STAR = 5;           // one * per 5 failures in the chart

        int[] failures = new int[HOURS];
        Scanner read = new Scanner(new FileReader("failed_logins.txt"));
        for (int hour = 0; hour < HOURS; hour++) {
            failures[hour] = read.nextInt();
        }
        read.close();

        int total = 0;
        int peakHour = 0;
        int alerts = 0;
        for (int hour = 0; hour < HOURS; hour++) {
            total = total + failures[hour];
            if (failures[hour] > failures[peakHour]) {
                peakHour = hour;
            }
            if (failures[hour] >= ALERT_LEVEL) {
                alerts++;
            }
        }

        System.out.println("Hour  Fails  Chart");
        for (int hour = 0; hour < HOURS; hour++) {
            System.out.printf("%02d:00 %5d  ", hour, failures[hour]);
            for (int s = 0; s < failures[hour] / PER_STAR; s++) {
                System.out.print("*");
            }
            if (failures[hour] >= ALERT_LEVEL) {
                System.out.print("  <-- ALERT");
            }
            System.out.println();
        }
        System.out.println();
        System.out.println("Total failed logins: " + total);
        System.out.printf("Peak hour: %02d:00 (%d failures)%n", peakHour, failures[peakHour]);
        System.out.println("Hours at or above " + ALERT_LEVEL + ": " + alerts);
    }
}
```

Part of the output (verified):

```text
14:00    31  ******  <-- ALERT
15:00    47  *********  <-- ALERT
16:00     9  *
...
20:00    22  ****  <-- ALERT
```

The summary lines match the task (verified). The index is the hour, so each element's position carries meaning. Zero-padding is also useful for dates, times, and IDs such as ticket numbers. Other patterns worth investigating: failures at night when nobody should be working (the 20:00 spike here), or a slow steady stream that stays below the alert level.

**Task 20.**

```java
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.PrintWriter;
import java.util.Arrays;
import java.util.Scanner;

public class MarksAnalyser {
    public static void main(String[] args) throws FileNotFoundException {
        final int PASS = 40;

        Scanner read = new Scanner(new FileReader("module_marks.txt"));
        int n = read.nextInt();
        String[] ids = new String[n];
        int[] marks = new int[n];
        for (int i = 0; i < n; i++) {
            ids[i] = read.next();
            marks[i] = read.nextInt();
        }
        read.close();

        int sum = 0, passes = 0;
        int lowest = marks[0], highest = marks[0];
        int[] bands = new int[4];          // 0: <40, 1: 40-59, 2: 60-69, 3: 70+
        for (int i = 0; i < n; i++) {
            sum = sum + marks[i];
            if (marks[i] >= PASS) {
                passes++;
            }
            if (marks[i] < lowest) {
                lowest = marks[i];
            }
            if (marks[i] > highest) {
                highest = marks[i];
            }
            if (marks[i] >= 70) {
                bands[3]++;
            } else if (marks[i] >= 60) {
                bands[2]++;
            } else if (marks[i] >= PASS) {
                bands[1]++;
            } else {
                bands[0]++;
            }
        }
        double mean = (double) sum / n;

        int[] sorted = new int[n];          // copy, so the original order is kept
        for (int i = 0; i < n; i++) {
            sorted[i] = marks[i];
        }
        Arrays.sort(sorted);
        double median;
        if (n % 2 == 1) {
            median = sorted[n / 2];
        } else {
            median = (sorted[n / 2 - 1] + sorted[n / 2]) / 2.0;
        }

        PrintWriter out = new PrintWriter("marks_report.txt");
        out.println("Students: " + n);
        out.printf("Mean: %.1f  Median: %.1f%n", mean, median);
        out.println("Lowest: " + lowest + "  Highest: " + highest);
        out.printf("Pass rate: %d/%d (%.1f%%)%n", passes, n, 100.0 * passes / n);
        out.println("Below 40: " + bands[0]);
        out.println("40-59:    " + bands[1]);
        out.println("60-69:    " + bands[2]);
        out.println("70+:      " + bands[3]);
        out.print("Above the mean:");
        for (int i = 0; i < n; i++) {
            if (marks[i] > mean) {
                out.print(" " + ids[i]);
            }
        }
        out.println();
        out.close();
        System.out.println("Report written to marks_report.txt");
    }
}
```

The report file matches the expected output exactly (verified). Sorted marks: 33 38 47 55 59 64 70 72 81 91, so the median is (59 + 64) / 2 = 61.5. The copy is needed because sorting `marks` itself would separate the marks from their IDs (Task 17). This program assumes at least one student; an empty file would need a check before `marks[0]` (worth adding to your test plan).

**Next:** the next lecture moves from fixed-size arrays to **variable-size** collections.
