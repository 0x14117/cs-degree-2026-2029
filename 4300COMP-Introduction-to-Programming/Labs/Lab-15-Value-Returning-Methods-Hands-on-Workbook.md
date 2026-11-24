# Lab 15 — Value-Returning Methods Hands-on Workbook (20 Tasks)

**Module:** 4300COMP Introduction to Programming · **Language:** Java

## How to use this lab

This lab has **20 hands-on tasks** on Lecture 15: return types and `return`, using returned values, scope and shadowing, the slides' `yesOrNo` and `readFile` methods, and designing methods by purpose, output, input and implementation. **All four official Tutorial 15 exercises are included** (Tasks 2, 11, 12 and 16), marked "official", together with the tutorial's `getSelection` example (Task 15).

**Learning outcomes:** MLO1 (methods), MLO2 (the `Math`, `Character` and `ArrayList` APIs; Javadoc), MLO3 (Tasks 16–20 decompose specifications into returning methods).

**Setup:** create a Java project called **Lab15** in Eclipse (untick *Create module-info.java*). Put every method inside the class, outside `main`, as `public static`. Tutorial 15 reminds you: **never define a method inside another method**, and a value-returning method must **always** return a value.

**Rules for this lab:**

1. **Design first:** for every method, write its purpose, output (return type) and input (parameters) before the body.
2. **Write a Javadoc comment** (`/** ... @param ... @return ... */`) for every method you write.
3. **Test each method on its own** from `main` before using it inside another method.
4. Predict before you run; use the hints only after a real attempt.

The **tracker** is near the end, followed by the **answer key**. Every answer was compiled and run with Java 21 (javac on the command line, not Eclipse) with the inputs shown.

## Part A — Using and writing returning methods (Tasks 1–5)

### Task 1 — Methods you already know

**Class:** `Task01Known` · **Goal:** recognise return types in the Java API.

For each call, write the **return type** and the **value returned**, then print them all to check:

| | Call | Return type | Value |
| --- | --- | --- | --- |
| a | `"abc".length()` | | |
| b | `Math.max(3, 9)` | | |
| c | `Math.sqrt(16)` | | |
| d | `Math.abs(-4)` | | |
| e | `Math.round(2.5)` | | |
| f | `"Hi".equals("hi")` | | |
| g | `Integer.parseInt("42")` | | |
| h | `"Cyber".charAt(0)` | | |

Then look up `Math.round(double)` in the [Math documentation](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Math.html). What type does it return, and why does `int r = Math.round(2.5);` not compile?

### Task 2 — Official Tutorial 15, Exercise 1: calculateTax

**Class:** `TaxCalculator` · **Goal:** read a Javadoc'd header, then implement it.

```java
/**
 * Calculate the amount of tax payable on income.
 *
 * @param income    the income.
 * @param taxRate   the tax rate in %, between 0.0-100.0.
 * @return          the tax payable on the income.
 */
public static float calculateTax(float income, float taxRate) {

}
```

1. Identify (write down or highlight) where the definition **describes** its purpose, parameters and return value; where it is **public and static**; where it says it **returns a floating-point value**; and where it **accepts two floating-point parameters**.
2. Write the statements that calculate and return the tax.
3. Write a `main` that calls `calculateTax` for some incomes and prints the results. Test: 25000 at 20% → 5000.0; 50000 at 0% → 0.0.
4. Try 12345.67 at 20%. The exact answer is 2469.134. What does `float` print? Why might you prefer `double`, or whole pence, for money?

### Task 3 — The slides' scope puzzles

**Class:** `QuestionOne`, `QuestionTwo`, `QuestionThree` · **Goal:** predict which variable a name refers to.

Type the three `celsius` programs from Lecture 15, section 4. For each, **write your four predicted lines first** and choose A, B or C, then run it. For any you got wrong, explain in one sentence which variable each line printed.

### Task 4 — Five small methods

**Class:** `Small` · **Goal:** write returning methods of different types.

Write and test each (design first: purpose, output, input):

| Method | Returns | Tests |
| --- | --- | --- |
| `square(int n)` | `n * n` | `square(7)` → 49 |
| `maxOfTwo(int a, int b)` | the larger | `maxOfTwo(3, 9)` → 9 |
| `isEven(int n)` | `true` if even | `isEven(10)` → true |
| `initials(String first, String last)` | e.g. `"AL"` | `initials("Ada", "Lovelace")` |
| `toFahrenheit(double c)` | `c × 9 / 5 + 32` | 100.0 → 212.0, −40 → −40.0 |

- **Hint 1:** `isEven` can be one line: `return n % 2 == 0;`.
- **Hint 2:** for `initials`, `first.charAt(0) + last.charAt(0)` adds two **numbers**. Start with `""`.

### Task 5 — Nested calls

**Class:** add to `Small` · **Goal:** use returned values as arguments.

With your Task 4 methods and `add(int a, int b)`, predict then check:

1. `square(add(1, 2))`
2. `add(square(2), square(3))`
3. `isEven(square(3))`
4. `maxOfTwo(square(-4), add(10, 5))`
5. `toFahrenheit(0)`

For (2), list the order in which the three methods are called and what each returns.

## Part B — Find and fix (Tasks 6–10)

### Task 6 — Return error clinic

**Class:** `Task06Errors` · **Goal:** recognise the compiler's return errors.

Each method has one problem. Record the exact error, explain it, fix it.

```java
// 1
public static int square(int n) {
    int r = n * n;
}

// 2
public static int half(int n) {
    return n / 2.0;
}

// 3
public static int sign(int n) {
    if (n > 0) {
        return 1;
    } else if (n < 0) {
        return -1;
    }
}

// 4
public static int twice(int n) {
    return n * 2;
    System.out.println("done");
}

// 5 (in main)
String s = name();          // where name() is declared to return int

// 6: compiles, but crashes
public static String find() {
    return null;
}
// in main: System.out.println(find().length());
```

### Task 7 — Fix the shadowing bug

**Class:** `Task07Celsius` · **Goal:** replace a confusing static variable with a return value.

`QuestionThree` was meant to set the static `celsius` to 30, but did nothing.

1. Explain exactly why `celsius = celsius;` has no effect.
2. Fix it **without** renaming anything, using the class name: `QuestionThree.celsius = celsius;`. Run it.
3. Now fix it the better way: delete the static variable and write `public static int validCelsius(int value)` that returns the value if it is between −50 and 60, or 0 otherwise. Use it as `int celsius = validCelsius(30);` in `main`.

### Task 8 — Replace a shared static variable with return values

**Class:** `ReceiptV2` · **Goal:** see why returning values is cleaner.

Lab 14 Task 16's receipt kept a running total in a `static int totalPence`, which broke when two receipts were printed.

1. Write `int itemCost(int quantity, int pricePence)` that **returns** the cost.
2. Write `int printItem(String name, int quantity, int pricePence)` that prints the line **and returns** the cost.
3. In `main`, keep the total in a **local** variable: `total += printItem(...);`.
4. Check the total is still **12.25**. Print a second receipt in the same run and show it starts from zero.

### Task 9 — The stack with return values

**Class:** `StackReturn` · **Goal:** trace where returned values go.

Predict the four lines this prints, and draw the stack at each `println`:

```java
public class StackReturn {
    public static void main(String[] args) {
        int[] marks = {60, 75, 90};
        System.out.println("main: average is " + average(marks));
    }
    public static double average(int[] values) {
        System.out.println("average: asking sum");
        int total = sum(values);
        System.out.println("average: sum returned " + total);
        return (double) total / values.length;
    }
    public static int sum(int[] values) {
        System.out.println("sum: adding " + values.length + " values");
        int total = 0;
        for (int v : values) { total += v; }
        return total;
    }
}
```

Why does `main`'s line print **last**, although it is the first `println` in the code?

### Task 10 — The null trap

**Class:** `Task10Null` · **Goal:** see why the slides warn against returning `null`.

1. Write `String findUser(String id)` that returns `"alice"` for `"u1"`, `"bob"` for `"u2"`, and `null` otherwise.
2. In `main`, print `findUser("u3").length()`. Copy the exception message.
3. Change the method to return `""` when the user is not found. What happens now?
4. Write a better version, `boolean userExists(String id)`, and use it before calling `findUser`. Which design do you prefer, and why?

## Part C — The slides' and tutorial's methods (Tasks 11–15)

### Task 11 — Official Tutorial 15, Exercise 2: calculateTaxes

**Class:** add to `TaxCalculator` · **Goal:** one method calling another, over a list.

```java
/**
 * Calculate the amount of tax payable on a collection of incomes.
 *
 * @param incomes   a list of incomes.
 * @param taxRate   the tax rate in %, between 0.0-100.0.
 * @return          the total tax payable on the incomes.
 */
public static float calculateTaxes(ArrayList<Float> incomes, float taxRate) {

}
```

1. Identify the components of this definition, as in Task 2.
2. Implement it. **You must call `calculateTax`** for each income, as the tutorial requires.
3. Extend `main` to build an `ArrayList<Float>` of incomes (25000, 31000, 18500) and print the total tax at 20%. Expected: **14900.00**.

- **Hint 1:** a for-each loop over the list; add each `calculateTax(income, taxRate)` to a running total.

### Task 12 — Official Tutorial 15, Exercise 3: a non-empty answer

**Class:** `AskQuestions` · **Goal:** design a method's header from a specification.

Write a method that:

- prints a question to the user;
- reads the next **line** of text typed at the console;
- if the response is not empty (not zero-length and not only spaces), returns it;
- otherwise keeps printing the question and reading lines until the response is not empty.

Before coding, answer the tutorial's design questions: its modifiers (`public static`); its **return type**; how many **parameters** and of what type. Then implement it and use it to ask several questions, printing the answers back.

Test: press Enter, then type three spaces and Enter, then `Sam`. The question should be asked three times.

- **Hint 1:** `response.trim().isEmpty()` is true for `""` and for spaces only.

### Task 13 — yesOrNo, improved

**Class:** `PlayAgain` · **Goal:** use a `boolean`-returning method as a loop condition.

1. Type the slides' `yesOrNo` method (Lecture 15, section 6).
2. Replace its final `if...else` with a **single** `return` statement.
3. Use it to control a game loop: print `Playing round N`, then ask `Play again (yes/no)?`. The loop condition should be the method call itself.
4. Test with `yes`, `maybe`, `Yes`, `no`. How many rounds are played?

### Task 14 — readFile and friends

**Class:** `FileTools` · **Goal:** returning methods that read files.

Create `test.txt` with two lines, `line one` and `line two`.

1. Type the slides' `readFile(String filename)` and print what it returns.
2. Write `int countLines(String filename)` that returns the number of lines.
3. In `main`, use the String returned by `readFile` to print its length and whether it contains `two`.
4. Why must `main` also say `throws FileNotFoundException`?

### Task 15 — The tutorial's getSelection, rewritten

**Class:** `Vending` · **Goal:** understand `while (true)`/`continue`, then write a clearer version.

1. Type Tutorial 15's `MethodExample` (Lecture 15, section 8) and test with `B12`, `7C`, `C7`.
2. In your own words, explain what `while (true)`, `continue` and `return` each do in it.
3. Rewrite it with **two** methods: `boolean isValidSelection(String text)` (a letter followed by a digit, exactly two characters) and `String getSelection()` using a `do...while` loop that repeats while the selection is not valid.
4. Test `isValidSelection` directly from `main` with `"C7"`, `"7C"`, `"C"`, `"CC7"` before using it in the loop.

## Part D — Building with methods (Tasks 16–20)

### Task 16 — Official Tutorial 15, Exercise 4: makeList

**Class:** `MakeListDemo` · **Goal:** implement a method with a generic type and a variable number of parameters.

Arrays have the shortcut `int[] values = {1, 2, 3, 4, 5};`, but `ArrayList` has no such syntax. Implement this method so it builds and returns a new `ArrayList` containing all its parameters:

```java
/**
 * Helper method that builds an array list from its parameters.
 *
 * @param values    the values to add to the array list.
 * @return          an ArrayList containing the values.
 */
public static <T> ArrayList<T> makeList(T... values) {

}
```

As the tutorial explains: `<T>` is a **generic** placeholder for "any type"; `T...` (a **varargs** parameter) means "any number of values", and inside the method `values` is an **array** of `T`.

Check that this works in `main`:

```java
ArrayList<String> messages = makeList("Hello", ", ", "world!");
for (String msg : messages) {
    System.out.print(msg);
}
System.out.println();
```

Then also try `makeList(4, 8, 15, 16, 23, 42)` and `makeList()`.

- **Hint 1:** create `new ArrayList<T>()`, loop over `values` with a for-each loop, add each, and return the list.

### Task 17 — A validation library

**Class:** `Validators` · **Goal:** `boolean`-returning methods that guard input.

Write and test:

1. `isValidPort(int port)`: 1 to 65535.
2. `isValidPercentage(int value)`: 0 to 100.
3. `isValidUsername(String name)`: 3 to 12 characters, each a letter, digit or underscore.
4. `isValidIPv4(String address)`: four whole numbers from 0 to 255 separated by dots. Write a helper `isNumberInRange(String text, int low, int high)` and call it for each part.

| Call | Expected |
| --- | --- |
| `isValidPort(443)`, `(0)`, `(70000)` | true, false, false |
| `isValidUsername("sam_archer")`, `("sa")`, `("sam archer")` | true, false, false |
| `isValidIPv4("192.168.1.20")`, `("192.168.1.256")`, `("10.0.0")`, `("a.b.c.d")` | true, false, false, false |

**Cyber security link:** checks like these are **input validation**, one of the most important defences in secure software. A method that returns early (`return false;`) as soon as one rule fails keeps the logic simple.

### Task 18 — An array statistics library

**Class:** `ArrayStats` · **Goal:** small methods that build on each other.

Write `sum(int[])`, `mean(int[])` (which calls `sum`, and returns 0.0 for an empty array), `min(int[])`, `max(int[])` and `countAbove(int[] values, int threshold)`.

Test with `{72, 38, 55, 91, 64, 47, 70}`: expected `Sum 437, mean 62.43, min 38, max 91, above 60: 4`.

Then compare: how much shorter would Lab 11 Task 20 (marks analyser) be with these methods?

### Task 19 — Mini-project: a Caesar cipher toolkit

**Class:** `CaesarTools` · **Goal:** refactor Lab 13's cipher into reusable returning methods.

Write:

- `char shift(char c, int key)`: shifts one lower-case letter; returns other characters unchanged;
- `String encode(String message, int key)`: lower-cases the message and shifts every character using `shift`;
- `String decode(String message, int key)`: **one line**, using `encode`;
- `int crack(String secret)`: tries keys 1 to 25 and returns the first key whose decoding contains `"the "` or `" the"`, or −1 if none does.

Test:

```text
encode("the meeting is at three", 3)  -> wkh phhwlqj lv dw wkuhh
decode(that, 3)                       -> the meeting is at three
crack(that)                           -> 3
encode("Hello, World!", 13) twice     -> uryyb, jbeyq!  then  hello, world!
```

Why does encoding twice with key 13 give the original text back? (This variant is called ROT13.)

### Task 20 — Assessment-style task: weekly payslip

**Class:** `Payroll` · **Goal:** a complete program built from small returning methods.

This is a practice task similar in skills to the module's application assessments. It is **not** an actual assessment question. The pay rules are **fictional**, for practice only, and are **not** real UK tax rules.

**Rules (as named constants):** standard week 37.5 hours; overtime (hours above 37.5) paid at 1.5× the hourly rate; the first £240.00 of weekly gross pay is tax-free; tax is 20% of gross pay above that.

**Specification:** write these methods and keep `main` short:

| Method | Purpose |
| --- | --- |
| `String askName(String prompt)` | Keep asking until the name is not blank |
| `double askNumber(String prompt, double low, double high)` | Keep asking until the number is in range, with an error message |
| `double grossPay(double hours, double rate)` | Pay including overtime |
| `double taxDue(double gross)` | Tax using the rules above |
| `void printPayslip(...)` | Print the payslip |

**Test plan** (fill in Actual):

| Test | Input | Expected |
| --- | --- | --- |
| 1 | blank name, `Sam Archer`, hours `90` (rejected) then `40`, rate `5` (rejected) then `12.50` | Gross £515.63, tax £55.13, net £460.50 |
| 2 | `Jo`, `20`, `11` | Gross £220.00, tax £0.00, net £220.00 |
| 3 | exactly 37.5 hours | no overtime |
| 4 | gross exactly £240.00 | tax £0.00 |

Test `grossPay` and `taxDue` **on their own** first, with values you have worked out by hand.

- **Hint 1:** read numbers with `Double.parseDouble(console.nextLine().trim())` so blank-line handling stays simple.

## Tracker

| Task | Done | Notes / score |
| --- | --- | --- |
| 1 Known methods (out of 8) | ☐ | |
| 2 Official Ex 1 | ☐ | |
| 3 Scope puzzles (out of 3) | ☐ | |
| 4 Five small methods | ☐ | |
| 5 Nested calls (out of 5) | ☐ | |
| 6 Error clinic (out of 6) | ☐ | |
| 7 Shadowing fix | ☐ | |
| 8 ReceiptV2 | ☐ | |
| 9 Stack with returns | ☐ | |
| 10 Null trap | ☐ | |
| 11 Official Ex 2 | ☐ | |
| 12 Official Ex 3 | ☐ | |
| 13 yesOrNo | ☐ | |
| 14 readFile | ☐ | |
| 15 getSelection | ☐ | |
| 16 Official Ex 4 | ☐ | |
| 17 Validators | ☐ | |
| 18 ArrayStats | ☐ | |
| 19 Caesar toolkit | ☐ | |
| 20 Payslip | ☐ | |

## Reflection

1. In one sentence each: when would you write a void method, and when a value-returning method?
2. Explain shadowing using one of the `celsius` questions.
3. Pick one method you wrote today and describe it with the four design steps: purpose, output, input, implementation.
4. How did splitting Tasks 19 and 20 into small methods change how you tested them?

## Answer key

All code was compiled and run with Java 21 (javac on the command line, not Eclipse). Outputs are actual outputs. In a console not set to UTF-8, `£` may print as `?`.

**Task 1.** a `int` 3 · b `int` 9 · c `double` 4.0 · d `int` 4 · e `long` 3 · f `boolean` false · g `int` 42 · h `char` `C`. (a–g verified.) `Math.round(double)` returns a `long`, so assigning it to an `int` gives `error: incompatible types: possible lossy conversion from long to int`; cast with `(int)` if you need an `int`.

**Tasks 2 and 11.**

```java
import java.util.ArrayList;

public class TaxCalculator {
    public static void main(String[] args) {
        System.out.println(calculateTax(25000.0f, 20.0f));
        System.out.println(calculateTax(12345.67f, 20.0f));
        System.out.println(calculateTax(50000.0f, 0.0f));

        ArrayList<Float> incomes = new ArrayList<Float>();
        incomes.add(25000.0f);
        incomes.add(31000.0f);
        incomes.add(18500.0f);
        System.out.printf("Total tax: %.2f%n", calculateTaxes(incomes, 20.0f));
    }

    /**
     * Calculate the amount of tax payable on income.
     *
     * @param income    the income.
     * @param taxRate   the tax rate in %, between 0.0-100.0.
     * @return          the tax payable on the income.
     */
    public static float calculateTax(float income, float taxRate) {
        return income * taxRate / 100.0f;
    }

    /**
     * Calculate the amount of tax payable on a collection of incomes.
     *
     * @param incomes   a list of incomes.
     * @param taxRate   the tax rate in %, between 0.0-100.0.
     * @return          the total tax payable on the incomes.
     */
    public static float calculateTaxes(ArrayList<Float> incomes, float taxRate) {
        float total = 0.0f;
        for (float income : incomes) {
            total = total + calculateTax(income, taxRate);
        }
        return total;
    }
}
```

Output (verified): `5000.0`, `2469.134`, `0.0`, `Total tax: 14900.00`. Component identification: the `/** ... */` block describes the purpose, `@param` lines and `@return`; `public static` are the modifiers; `float` before the name is the return type; `(float income, float taxRate)` are the two floating-point parameters. `float` has only about 7 significant digits, so large money values lose accuracy; `double` (about 15–16 digits) or whole pence in `int`/`long` is safer.

**Task 3.** Question One A (0, 0, 20, 20); Question Two C (0, 0, 20, 0); Question Three A (0, 30, 30, 0). All verified; explanations in Lecture 15, section 4.

**Tasks 4 and 5.**

```java
public class Small {
    public static void main(String[] args) {
        System.out.println(square(7) + " " + maxOfTwo(3, 9) + " " + isEven(10) + " " + initials("Ada", "Lovelace") + " " + toFahrenheit(100.0) + " " + toFahrenheit(-40));
        System.out.println(square(add(1, 2)) + " " + add(square(2), square(3)) + " " + isEven(square(3)) + " " + maxOfTwo(square(-4), add(10, 5)) + " " + toFahrenheit(0));
    }
    public static int add(int a, int b) { return a + b; }
    public static int square(int n) { return n * n; }
    public static int maxOfTwo(int a, int b) { if (a > b) { return a; } return b; }
    public static boolean isEven(int n) { return n % 2 == 0; }
    public static String initials(String first, String last) { return "" + first.charAt(0) + last.charAt(0); }
    public static double toFahrenheit(double c) { return c * 9 / 5 + 32; }
}
```

Output (verified): `49 9 true AL 212.0 -40.0` and `9 13 false 16 32.0`. For `add(square(2), square(3))`: `square(2)` returns 4, then `square(3)` returns 9, then `add(4, 9)` returns 13. Arguments are worked out left to right, before the outer method is called.

**Task 6.** (1) `error: missing return statement` → `return n * n;`. (2) `error: incompatible types: possible lossy conversion from double to int` → `return n / 2;` (or make the return type `double`). (3) `error: missing return statement` (n == 0 is not covered) → add `return 0;` at the end. (4) `error: unreachable statement` → move the print before the `return`. (5) `error: incompatible types: int cannot be converted to String`. (6) `NullPointerException` when `.length()` is called on `null` → return `""`. All verified.

**Task 7.** The parameter `celsius` hides the static variable, so both sides of `celsius = celsius;` mean the parameter, which is assigned to itself. `QuestionThree.celsius = celsius;` sets the static (line 4 then prints 30). The `validCelsius` version passes the value back by `return`, with no shared variable to confuse.

**Task 8.**

```java
public class ReceiptV2 {
    public static void main(String[] args) {
        int total = 0;
        total += printItem("Flat white", 2, 310);
        total += printItem("Croissant", 1, 245);
        total += printItem("Water", 3, 120);
        System.out.printf("%-12s %12.2f%n", "TOTAL", total / 100.0);
    }

    /** Print one receipt line and return its cost in pence. */
    public static int printItem(String name, int quantity, int pricePence) {
        int cost = itemCost(quantity, pricePence);
        System.out.printf("%-12s %3d %8.2f%n", name, quantity, cost / 100.0);
        return cost;
    }

    public static int itemCost(int quantity, int pricePence) {
        return quantity * pricePence;
    }
}
```

Output (verified): the three lines and `TOTAL 12.25`. A second receipt uses its own local `total`, so it cannot pick up the first receipt's amount.

**Task 9.** Output (verified):

```text
average: asking sum
sum: adding 3 values
average: sum returned 225
main: average is 75.0
```

`main`'s `println` needs the value of `average(marks)` **before** it can print, so `average` (and inside it `sum`) must run and return first.

**Task 10.** `NullPointerException` (Java 21 explains which value was null). Returning `""` makes `.length()` give 0, with no crash. `userExists` makes the "not found" case explicit, so the caller can't forget to check: clearer than a special value.

**Task 12.**

```java
import java.util.Scanner;

public class AskQuestions {
    private static Scanner console = new Scanner(System.in);

    public static void main(String[] args) {
        String name = askNonEmpty("What is your name? ");
        String course = askNonEmpty("What are you studying? ");
        System.out.println("Hello " + name + ", good luck with " + course + ".");
    }

    /**
     * Ask a question until the user types something other than spaces.
     *
     * @param question  the question to print.
     * @return          the user's non-empty answer.
     */
    public static String askNonEmpty(String question) {
        String response;
        do {
            System.out.print(question);
            response = console.nextLine();
        } while (response.trim().isEmpty());
        return response;
    }
}
```

Return type `String`; one `String` parameter (the question): the method knows nothing else in advance. Verified: blank and spaces-only answers make it ask again; `Sam` and `Cyber Security` give `Hello Sam, good luck with Cyber Security.`

**Task 13.**

```java
import java.util.Scanner;

public class PlayAgain {
    static Scanner input = new Scanner(System.in);

    public static void main(String[] args) {
        int round = 1;
        do {
            System.out.println("Playing round " + round);
            round++;
        } while (yesOrNo("Play again (yes/no)? "));
        System.out.println("Thanks for playing " + (round - 1) + " round(s).");
    }

    public static boolean yesOrNo(String msg) {
        String ans;
        do {
            System.out.print(msg);
            ans = input.next();
        } while (!(ans.equalsIgnoreCase("yes") || ans.equalsIgnoreCase("no")));
        return ans.equalsIgnoreCase("yes");
    }
}
```

With `yes`, `maybe`, `Yes`, `no`: three rounds (`maybe` just repeats the question) (verified).

**Task 14.**

```java
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Scanner;

public class FileTools {
    public static void main(String[] args) throws FileNotFoundException {
        String text = readFile("test.txt");
        System.out.print(text);
        System.out.println("Lines: " + countLines("test.txt"));
        System.out.println("Characters (incl. newlines): " + text.length());
        System.out.println("Contains 'two': " + text.contains("two"));
    }

    public static String readFile(String filename) throws FileNotFoundException {
        String content = "";
        Scanner reader = new Scanner(new FileReader(filename));
        while (reader.hasNextLine()) {
            content += reader.nextLine() + "\n";
        }
        reader.close();
        return content;
    }

    public static int countLines(String filename) throws FileNotFoundException {
        int lines = 0;
        Scanner reader = new Scanner(new FileReader(filename));
        while (reader.hasNextLine()) {
            reader.nextLine();
            lines++;
        }
        reader.close();
        return lines;
    }
}
```

Output (verified): the two lines, `Lines: 2`, `Characters (incl. newlines): 18`, `Contains 'two': true`. `main` calls methods that may throw a checked `FileNotFoundException`, so it must either handle it or declare it.

**Task 15.** `while (true)` repeats forever; `continue` jumps back to the loop test; `return response;` ends the whole method (and so the loop) with the answer. Rewrite:

```java
import java.util.Scanner;

public class Vending {
    private static Scanner console = new Scanner(System.in);

    public static void main(String[] args) {
        String selection = getSelection();
        System.out.printf("Dispensing item %s...%n", selection);
    }

    /** Keep asking until the user enters a letter followed by a digit. */
    public static String getSelection() {
        String response;
        do {
            System.out.print("Enter a selection (A1-Z9): ");
            response = console.next();
        } while (!isValidSelection(response));
        return response;
    }

    /** True if text is exactly a letter followed by a digit, such as C7. */
    public static boolean isValidSelection(String text) {
        return text.length() == 2
                && Character.isLetter(text.charAt(0))
                && Character.isDigit(text.charAt(1));
    }
}
```

Verified: `B12` and `7C` rejected, `C7` accepted. `isValidSelection`: `"C7"` true; `"7C"`, `"C"`, `"CC7"` false. The length test comes first, and `&&` stops early (short-circuit, Lecture 6), so `charAt(1)` is never called on a one-character String.

**Task 16.**

```java
import java.util.ArrayList;

public class MakeListDemo {
    public static void main(String[] args) {
        ArrayList<String> messages = makeList("Hello", ", ", "world!");
        for (String msg : messages) {
            System.out.print(msg);
        }
        System.out.println();

        ArrayList<Integer> numbers = makeList(4, 8, 15, 16, 23, 42);
        System.out.println(numbers + " size " + numbers.size());
        ArrayList<String> none = makeList();
        System.out.println(none.isEmpty());
    }

    /**
     * Helper method that builds an array list from its parameters.
     *
     * @param values    the values to add to the array list.
     * @return          an ArrayList containing the values.
     */
    public static <T> ArrayList<T> makeList(T... values) {
        ArrayList<T> list = new ArrayList<T>();
        for (T value : values) {
            list.add(value);
        }
        return list;
    }
}
```

Output (verified): `Hello, world!`, `[4, 8, 15, 16, 23, 42] size 6`, `true`. javac prints a **note** (not an error) about "unchecked or unsafe operations": generic varargs trigger this warning. Adding `@SafeVarargs` on the line above the method removes it; you can ignore it for this exercise.

**Task 17.**

```java
public class Validators {
    public static void main(String[] args) {
        System.out.println(isValidPort(443) + " " + isValidPort(0) + " " + isValidPort(70000));
        System.out.println(isValidPercentage(100) + " " + isValidPercentage(-1));
        System.out.println(isValidUsername("sam_archer") + " " + isValidUsername("sa") + " " + isValidUsername("sam archer"));
        System.out.println(isValidIPv4("192.168.1.20") + " " + isValidIPv4("192.168.1.256") + " " + isValidIPv4("10.0.0") + " " + isValidIPv4("a.b.c.d"));
    }

    /** A TCP/UDP port number is 1 to 65535. */
    public static boolean isValidPort(int port) {
        return port >= 1 && port <= 65535;
    }

    public static boolean isValidPercentage(int value) {
        return value >= 0 && value <= 100;
    }

    /** 3 to 12 characters, each a letter, digit or underscore. */
    public static boolean isValidUsername(String name) {
        if (name.length() < 3 || name.length() > 12) {
            return false;
        }
        for (int i = 0; i < name.length(); i++) {
            char c = name.charAt(i);
            if (!(Character.isLetterOrDigit(c) || c == '_')) {
                return false;
            }
        }
        return true;
    }

    /** Four whole numbers 0-255 separated by dots, e.g. 192.168.1.20. */
    public static boolean isValidIPv4(String address) {
        int parts = 0;
        String rest = address + ".";              // so every part ends with a dot
        while (rest.length() > 0) {
            int dot = rest.indexOf(".");
            String part = rest.substring(0, dot);
            if (!isNumberInRange(part, 0, 255)) {
                return false;
            }
            parts++;
            rest = rest.substring(dot + 1);
        }
        return parts == 4;
    }

    /** True if text is 1-3 digits whose value is between low and high. */
    public static boolean isNumberInRange(String text, int low, int high) {
        if (text.length() < 1 || text.length() > 3) {
            return false;
        }
        for (int i = 0; i < text.length(); i++) {
            if (!Character.isDigit(text.charAt(i))) {
                return false;
            }
        }
        int value = Integer.parseInt(text);
        return value >= low && value <= high;
    }
}
```

Output (verified): `true false false`, `true false`, `true false false`, `true false false false`.

**Task 18.**

```java
public class ArrayStats {
    public static void main(String[] args) {
        int[] marks = {72, 38, 55, 91, 64, 47, 70};
        System.out.println("Sum " + sum(marks) + ", mean " + String.format("%.2f", mean(marks))
                + ", min " + min(marks) + ", max " + max(marks) + ", above 60: " + countAbove(marks, 60));
    }

    public static int sum(int[] values) {
        int total = 0;
        for (int v : values) {
            total = total + v;
        }
        return total;
    }

    public static double mean(int[] values) {
        if (values.length == 0) {
            return 0.0;
        }
        return (double) sum(values) / values.length;
    }

    public static int min(int[] values) {
        int smallest = values[0];
        for (int v : values) {
            if (v < smallest) {
                smallest = v;
            }
        }
        return smallest;
    }

    public static int max(int[] values) {
        int largest = values[0];
        for (int v : values) {
            if (v > largest) {
                largest = v;
            }
        }
        return largest;
    }

    public static int countAbove(int[] values, int threshold) {
        int count = 0;
        for (int v : values) {
            if (v > threshold) {
                count++;
            }
        }
        return count;
    }
}
```

Output (verified): `Sum 437, mean 62.43, min 38, max 91, above 60: 4`. (`String.format` works like `printf` but **returns** the formatted String instead of printing it.)

**Task 19.**

```java
public class CaesarTools {
    public static void main(String[] args) {
        String secret = encode("the meeting is at three", 3);
        System.out.println(secret);
        System.out.println(decode(secret, 3));
        int key = crack(secret);
        System.out.println("Cracked key: " + key + " -> " + decode(secret, key));
        System.out.println(encode("Hello, World!", 13) + " / " + encode(encode("Hello, World!", 13), 13));
    }

    /** Shift every letter by key (lower-cases the text first). */
    public static String encode(String message, int key) {
        String lower = message.toLowerCase();
        String result = "";
        for (int i = 0; i < lower.length(); i++) {
            result = result + shift(lower.charAt(i), key);
        }
        return result;
    }

    /** Decoding is encoding with the opposite key. */
    public static String decode(String message, int key) {
        return encode(message, -key);
    }

    /** Shift one character; non-letters are returned unchanged. */
    public static char shift(char c, int key) {
        if (c < 'a' || c > 'z') {
            return c;
        }
        return (char) ('a' + (c - 'a' + key % 26 + 26) % 26);
    }

    /** Try every key; return the first whose decoding contains " the" or "the ". */
    public static int crack(String secret) {
        for (int key = 1; key <= 25; key++) {
            String attempt = decode(secret, key);
            if (attempt.contains("the ") || attempt.contains(" the")) {
                return key;
            }
        }
        return -1;          // no key found
    }
}
```

Output (verified):

```text
wkh phhwlqj lv dw wkuhh
the meeting is at three
Cracked key: 3 -> the meeting is at three
uryyb, jbeyq! / hello, world!
```

ROT13: 13 + 13 = 26, a full trip round the alphabet, so the same operation both encodes and decodes.

**Task 20.**

```java
import java.util.Scanner;

public class Payroll {
    // Fictional practice rates: NOT real UK tax rules.
    public static final double STANDARD_HOURS = 37.5;
    public static final double OVERTIME_RATE = 1.5;
    public static final double TAX_FREE_WEEKLY = 240.00;
    public static final double TAX_RATE = 0.20;

    private static Scanner console = new Scanner(System.in);

    public static void main(String[] args) {
        String name = askName("Employee name: ");
        double hours = askNumber("Hours worked (0-80): ", 0, 80);
        double rate = askNumber("Hourly rate in pounds (10-100): ", 10, 100);

        double gross = grossPay(hours, rate);
        double tax = taxDue(gross);
        double net = gross - tax;
        printPayslip(name, hours, rate, gross, tax, net);
    }

    public static String askName(String prompt) {
        String name;
        do {
            System.out.print(prompt);
            name = console.nextLine().trim();
        } while (name.isEmpty());
        return name;
    }

    public static double askNumber(String prompt, double low, double high) {
        double value;
        do {
            System.out.print(prompt);
            value = Double.parseDouble(console.nextLine().trim());
            if (value < low || value > high) {
                System.out.println("Please enter a value from " + low + " to " + high + ".");
            }
        } while (value < low || value > high);
        return value;
    }

    public static double grossPay(double hours, double rate) {
        if (hours <= STANDARD_HOURS) {
            return hours * rate;
        }
        double overtime = hours - STANDARD_HOURS;
        return STANDARD_HOURS * rate + overtime * rate * OVERTIME_RATE;
    }

    public static double taxDue(double gross) {
        if (gross <= TAX_FREE_WEEKLY) {
            return 0.0;
        }
        return (gross - TAX_FREE_WEEKLY) * TAX_RATE;
    }

    public static void printPayslip(String name, double hours, double rate, double gross, double tax, double net) {
        System.out.println();
        System.out.println("PAYSLIP: " + name);
        System.out.printf("Hours %.1f at £%.2f%n", hours, rate);
        System.out.printf("Gross pay: £%8.2f%n", gross);
        System.out.printf("Tax:       £%8.2f%n", tax);
        System.out.printf("Net pay:   £%8.2f%n", net);
    }
}
```

Tests 1 and 2 verified. Working for test 1: 37.5 × 12.50 = 468.75; overtime 2.5 × 12.50 × 1.5 = 46.875; gross 515.625 (shown 515.63); tax (515.625 − 240) × 0.2 = 55.125 (shown 55.13); net 460.50. The constants are declared `public static final` at class level so every method can use them; a `final` variable cannot be changed (Lecture 3).

**Next:** Lecture 16 — classes and objects.
