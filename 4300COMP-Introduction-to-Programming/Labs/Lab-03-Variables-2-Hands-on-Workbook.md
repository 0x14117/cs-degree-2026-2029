# Lab 3 — Variables \#2 Hands-on Workbook (20 Tasks)

**Module:** 4300COMP Introduction to Programming · **Language:** Java

## How to use this lab

This lab has **20 hands-on tasks** on Lecture 3: assignment and variable state, `double` and `String`, converting text to numbers with wrapper classes, constants with `final`, and debugging. Every official Tutorial 3 task is included (marked **official**): Task 1, all four Task 2 problems and all three supplementary tasks.

**Learning outcomes:** MLO1 throughout; MLO2 in Tasks 12–13 (reading the Java API documentation); MLO3 in Tasks 16–20.

**Setup:** in Eclipse make a project `lab3` (untick module-info), package `lab3`, one class per task named as the task says, with `main` ticked.

**Rules**

1.  Type everything yourself.

2.  **Predict first, then run.** Write predictions on paper.

3.  For Tasks 6 onwards, Tutorial 3 says you must **decide the variables yourself**. Before coding, write a small plan: each variable’s name, type and value, then the calculation.

4.  Use hints in order. The answer key is at the end.

| Tasks | Focus                                                    | Rough time     |
|-------|----------------------------------------------------------|----------------|
| 1–5   | Assignment and state (official Task 1)                   | 5–15 min each  |
| 6–10  | Problem solving (official Task 2)                        | 10–15 min each |
| 11–15 | Conversions, wrappers, constants                         | 10–20 min each |
| 16–20 | Supplementary tasks, mini-project, assessment-style task | 15–30 min each |

Task 20 is practice only: it is not an official LJMU assessment and its checklist is not the official marking scheme.

## Tasks 1–5: Assignment and variable state

### Task 1 — Recap: using variables (official Tutorial 3, Task 1)

**Class:** `Task01Recap` · **Goal:** declare, assign, update and print.

1.  Declare three `int` variables `num1`, `num2` and `sum`.

2.  Store 25 in `num1` and 8 in `num2`.

3.  Update `num1` by adding 5 to it. Then store `num1 + num2` in `sum`.

4.  Print the values of `num1`, `num2` and `sum`, each with a label.

5.  Declare two more `int` variables, `num3` and `prod`. Store 2 in `num3`.

6.  Store `sum * num3` in `prod` and print it.

7.  **Test:** before running, work out every value by hand. Is the output what you expected?

- **Hint 1:** “add 5 to `num1`” is `num1 = num1 + 5;`

- **Hint 2:** order matters: update `num1` **before** calculating `sum`, or `sum` uses the old value.

### Task 2 — Trace the slide example

**Class:** `Task02State` · **Goal:** track program state line by line.

Copy the table on paper and fill it in **before** running.

``` java
int num1, num2, num3;
num1 = 18;
num1 = num1 + 27;
num2 = num1;
num3 = num2 / 5;
num3 = num3 / 4;
System.out.println(num1 + " " + num2 + " " + num3);
```

| After line          | `num1` | `num2` | `num3` |
|---------------------|--------|--------|--------|
| `num1 = 18;`        |        |        |        |
| `num1 = num1 + 27;` |        |        |        |
| `num2 = num1;`      |        |        |        |
| `num3 = num2 / 5;`  |        |        |        |
| `num3 = num3 / 4;`  |        |        |        |

Then change the last line to `num3 = num3 / 4.0;`. What error appears and why? Fix it two different ways.

- **Hint 1:** the last step is integer division.

- **Hint 2:** `num3 / 4.0` is a `double`; `num3` is an `int`.

### Task 3 — Copy, not link

**Class:** `Task03Copy` · **Goal:** prove that assignment copies a value.

``` java
int p = 5;
int q = p;
p = 99;
System.out.println(p + " " + q);
```

1.  Predict the output. Run it.

2.  Add `q = q + 1;` at the end and print both again. Predict first.

3.  Write one sentence explaining what `q = p;` actually does in memory.

- **Hint 1:** at the moment `q = p;` runs, `p` holds 5. That 5 is copied into `q`.

- **Hint 2:** after the copy, the two variables are completely separate boxes.

### Task 4 — Bank balance simulation

**Class:** `Task04Balance` · **Goal:** use one variable updated many times.

Start with `double balance = 100.0;` Then, one statement each:

1.  Deposit £250.

2.  Withdraw £75.50.

3.  Add 2% interest (multiply by 1.02).

4.  Pay a £20 fee.

Print the balance after **every** step with a label such as `After deposit: 350.0`. Fill in a trace table first. Final value should be `259.99`.

**Extra:** use a `final double INTEREST_RATE = 0.02;` and write step 3 as `balance = balance + balance * INTEREST_RATE;`

- **Hint 1:** every update has the form `balance = balance <operator> value;`

- **Hint 2:** 274.5 × 1.02 = 279.99.

### Task 5 — Bug hunt: eight errors

**Class:** `Task05Bugs` · **Goal:** tell compile errors from runtime errors and fix both.

Type each one **separately** inside `main`. For each: write **compile or runtime**, the cause, and the fix. Messages are from `javac` / the Java runtime; Eclipse words compile errors differently.

| \#  | Broken code                                                      | Message                                                                                |
|-----|------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| 1   | `double length = 23.5, width = 14.7; int area = length * width;` | `incompatible types: possible lossy conversion from double to int`                     |
| 2   | `String s = "42"; int n = s + 1;`                                | `incompatible types: String cannot be converted to int`                                |
| 3   | `int n = 42; String s = n;`                                      | `incompatible types: int cannot be converted to String`                                |
| 4   | `final int MAX = 5; MAX = 6;`                                    | `cannot assign a value to final variable MAX`                                          |
| 5   | `int total; total = total + 10;`                                 | `variable total might not have been initialized`                                       |
| 6   | `int n = Integer.valueOf("42.5");`                               | `Exception in thread "main" java.lang.NumberFormatException: For input string: "42.5"` |
| 7   | `System.out.println(“Hello”);` (curly quotes)                    | `illegal character: '“'`                                                               |
| 8   | `int num` then `num = 25;` on the next line                      | `';' expected`                                                                         |

- **Hint 1:** if Eclipse shows a red underline, it is a compile error. If the code runs and then stops with `Exception in thread "main"`, it is a runtime error.

- **Hint 2:** number 6 needs `Double.valueOf`, and then a cast if you really want an `int`.

## Tasks 6–10: Problem solving with arithmetic

Tutorial 3 says: “you need to decide how many variables are needed and what type of data”. For each task, **fill in a plan table first**, then code.

| Variable name | Type | Value or calculation | Why this type |
|---------------|------|----------------------|---------------|
|               |      |                      |               |

### Task 6 — Land calculation (official Task 2a)

**Class:** `LandCalculation`

One acre is 43,560 square feet. Calculate how many acres are in a tract of 389,767 square feet.

1.  First solve it with `int` variables only. What answer do you get?

2.  Then produce the exact answer as a `double`.

3.  Make 43,560 a constant: `final int SQ_FEET_PER_ACRE = 43560;`

4.  **Extra:** use `%` to print how many square feet are left over after the whole acres.

Note: Java does not allow commas inside numbers. Write `43560`, not `43,560`.

- **Hint 1:** the tutorial’s hint: acres = 389767 / 43560.

- **Hint 2:** an `int` divided by an `int` drops the decimal. Make one side a `double` or cast.

### Task 7 — Area of a rectangle with a message (official Task 2b)

**Class:** `RectangleArea`

A rectangle is 25.7 cm long and 18.5 cm wide. Calculate its area.

The program must use a String variable: `String message = "The area of the rectangle is: ";` Join the area onto this message and print the result.

**Extra:** add the unit so the output ends with `cm squared`.

- **Hint 1:** `message + area` joins them.

- **Hint 2:** if you write `message + length * width`, the `*` happens first, so it still works. Try it.

### Task 8 — Length of fence (official Task 2c)

**Class:** `FenceLength`

Fence posts are 3.45 metres apart and there are 15 posts. Calculate the total length of wire needed. Use an `int` for the number of posts and a `double` for the distance.

1.  Calculate it as the tutorial describes: posts × distance.

2.  **Think like a programmer:** draw 3 posts in a line. How many gaps are there? With 15 posts in a straight line, how many gaps? Write a second calculation for a straight fence and explain which answer is right for which layout.

- **Hint 1:** 3 posts in a straight line have 2 gaps.

- **Hint 2:** this “one more post than gap” mistake is called an **off-by-one error**. It shows up again when you learn loops and arrays.

### Task 9 — Average mark with a constant (official Task 2d)

**Class:** `AverageMark`

Calculate the average mark of 5 students.

1.  Declare a named constant `final int NO_OF_STUDENTS = 5;`

2.  Declare a variable for each student’s mark and give each a mark from 0 to 100 (for example 72, 58, 91, 64, 47).

3.  Calculate and print the total and the average, using the constant.

4.  Print the average both as a whole number and as an exact `double`.

5.  Try to add `NO_OF_STUDENTS = 6;` later in the program. What happens?

- **Hint 1:** `average = total / NO_OF_STUDENTS;`

- **Hint 2:** for the exact average: `(double) total / NO_OF_STUDENTS`.

### Task 10 — Fix the AreaCalculator (from the lecture)

**Class:** `AreaCalculator`

Type the lecture’s program exactly (using straight quotes):

``` java
double length = 23.5;
double width = 14.7;
int area = 0;
area = length * width;
System.out.println("Area is: " + area);
```

1.  Read the error. Which line, and why?

2.  **Fix A:** change the type of `area`. Run and record the output.

3.  **Fix B:** keep `area` as an `int` and use a cast. Run and record the output.

4.  Which fix would you choose for a carpet shop that charges per square metre? Why?

- **Hint 1:** the cast must cover the whole multiplication: `(int) (length * width)`.

- **Hint 2:** compare 345.45 with 345: what is lost?

## Tasks 11–15: Conversions, wrapper classes and constants

### Task 11 — Text or number? Ten predictions

**Class:** `Task11TextOrNumber` · **Goal:** know exactly when `+` joins and when it adds.

`String numString = "42.45";` Predict each line, then print them all.

| \#  | Expression                                          | Your prediction |
|-----|-----------------------------------------------------|-----------------|
| a   | `numString + 10`                                    |                 |
| b   | `Double.valueOf(numString) + 10`                    |                 |
| c   | `numString + 5 + 5`                                 |                 |
| d   | `numString + (5 + 5)`                               |                 |
| e   | `Double.valueOf(numString) * 2`                     |                 |
| f   | `Integer.valueOf("10") + Integer.valueOf("20")`     |                 |
| g   | `"10" + "20"`                                       |                 |
| h   | `Integer.valueOf("10" + "20")`                      |                 |
| i   | `Integer.valueOf("10") / Integer.valueOf("4")`      |                 |
| j   | `Integer.valueOf("7") + Integer.valueOf("3") + "1"` |                 |

- **Hint 1:** after `valueOf`, you have a number. Before it, you have text.

- **Hint 2:** h: the brackets inside `valueOf( )` are worked out first.

### Task 12 — Explore the wrapper classes in the API (MLO2)

**Class:** `Task12Wrappers` · **Goal:** use official documentation to find facts yourself.

1.  Write boxing and unboxing: `Integer boxed = 33;` and `int plain = boxed;`. Print `boxed + plain`.

2.  Convert one String to each of `int`, `double`, `boolean` and `long` using `valueOf`. Use `"9000000000"` for the `long`: why will that not fit in an `int`?

3.  Open the official documentation for [Integer (Java SE 21)](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Integer.html). Find the two **constants** that hold the largest and smallest `int`. Print them. (Notice their names follow the UPPER_CASE convention from the lecture.)

4.  In the same page, find `valueOf(String s)` and `parseInt(String s)`. What does each one **return**? What does the page say they **throw**?

5.  Open the documentation for [Character](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/lang/Character.html). Find a method that checks whether a `char` is a digit and one that turns a letter into upper case. Use both.

- **Hint 1:** on the Integer page, scroll to **Field Summary** for the constants and **Method Summary** for the methods.

- **Hint 2:** the methods you want on the Character page start with `is...` and `to...`.

### Task 13 — Break the converter

**Class:** `Task13BadInput` · **Goal:** find out exactly which text converts and which crashes.

For each input, **predict** whether `Integer.valueOf(input)` works (and the value) or throws `NumberFormatException`. Then test them **one at a time** (each crash stops the program, so comment out the line once you have seen the result).

| Input text              | Prediction | Actual |
|-------------------------|------------|--------|
| `"42"`                  |            |        |
| `"42.0"`                |            |        |
| `" 42"` (leading space) |            |        |
| `"4 2"`                 |            |        |
| `"-42"`                 |            |        |
| `"+42"`                 |            |        |
| `""` (empty)            |            |        |
| `"forty-two"`           |            |        |
| `"007"`                 |            |        |
| `"2147483648"`          |            |        |

Then repeat for `Double.valueOf` with: `"42"`, `"42.0"`, `" 42 "`, `"1,000"`, `".5"`.

**Cyber security reflection:** in one or two sentences, why should a program never assume user text is a valid number?

- **Hint 1:** the last `int` input is one more than `Integer.MAX_VALUE`.

- **Hint 2:** `Double.valueOf` is more forgiving about spaces than `Integer.valueOf`. Find out how.

### Task 14 — Replace the magic numbers

**Class:** `Task14Constants` · **Goal:** refactor code to use named constants.

This program works, but its numbers have no names (programmers call them **magic numbers**):

``` java
double price = 50.0;
double vat = price * 0.2;
double total = price + vat;
int seats = 40;
int groups = seats / 4;
int spare = seats % 4;
System.out.println("Total: " + total);
System.out.println("Groups: " + groups + ", spare: " + spare);
```

1.  Decide which numbers are fixed rules (constants) and which are data (variables).

2.  Create constants such as `VAT_RATE` and `GROUP_SIZE` with `final` and UPPER_CASE names.

3.  Rewrite the calculations to use them. The output must not change.

4.  Change VAT to 17.5% by editing **one** line. Run again.

- **Hint 1:** 0.2 and 4 are rules; 50.0 and 40 are the data being processed.

- **Hint 2:** constants usually go at the top of `main` so they are easy to find.

### Task 15 — Unit converter with constants

**Class:** `Task15Units` · **Goal:** combine constants, promotion and joining text.

Declare these constants: `KM_PER_MILE = 1.609344`, `LB_PER_KG = 2.20462`, `CM_PER_INCH = 2.54`. Then print:

1.  A 26.2-mile marathon in km.

2.  70 kg in pounds.

3.  A height of 180 cm in inches.

4.  5 miles in km.

Each line must read like `26.2 miles = 42.1648128 km`.

- **Hint 1:** cm to inches is a division by `CM_PER_INCH`.

- **Hint 2:** keep each input in its own well-named variable (`marathonMiles`, `weightKg` ...).

## Tasks 16–20: Supplementary tasks, mini-project and assessment-style task

### Task 16 — Stock commission (official supplementary)

**Class:** `StockCommission`

Ted bought 600 shares at £21.77 per share. He pays the broker a 2% commission. Calculate and print:

1.  The amount paid for the stock without commission.

2.  The commission.

3.  The total including commission.

Use a constant for the commission rate. Plan your variables first.

- **Hint 1:** 2% is `0.02`.

- **Hint 2:** commission = stock cost × rate; total = cost + commission.

### Task 17 — Fahrenheit to Celsius with an int cast (official supplementary)

**Class:** `TempConversion`

Declare a variable for a Fahrenheit value and assign it. Convert to Celsius: subtract 32, multiply by 5, divide by 9. Use an `int` cast so the result is a whole number.

Test with every value in the table. Predict first, then fill in what Java gives you.

| °F   | Exact °C | Your `int` result |
|------|----------|-------------------|
| 212  | 100      |                   |
| 100  | 37.78    |                   |
| 98.6 | 37       |                   |
| 32   | 0        |                   |
| 0    | −17.78   |                   |
| −40  | −40      |                   |

Why is the `int` result for 0 °F −17 and not −18? What does that tell you about how casting treats negative numbers?

- **Hint 1:** use a `double` for Fahrenheit so 98.6 works.

- **Hint 2:** put the cast around the whole calculation: `(int) ((f - 32) * 5 / 9)`.

### Task 18 — Energy drink survey (official supplementary)

**Class:** `EnergyDrinks`

A company surveyed 12,467 customers. About 12% buy one or more energy drinks per week. Of those, about 64% prefer citrus flavour. Display the approximate number of surveyed customers who prefer citrus.

1.  Use constants for both percentages.

2.  Print the number of energy-drink buyers and the number who prefer citrus.

3.  People come in whole numbers: print the citrus figure as an `int` too. Is a cast the right way to make it whole here, or would rounding be better? Explain.

- **Hint 1:** citrus = customers × 0.12 × 0.64.

- **Hint 2:** the cast drops .4656; that happens to be close to correct here, but a value like 957.9 would also become 957.

### Task 19 — Mini-project: order from text data

**Class:** `Task19Order` · **Goal:** combine conversion, constants and calculation in one complete program.

An online shop receives an order as **text** (this is how data arrives from forms and files):

| Item         | Price (String) | Quantity (String) |
|--------------|----------------|-------------------|
| USB cable    | `"12.50"`      | `"2"`             |
| Screen wipes | `"3.99"`       | `"5"`             |
| Mouse mat    | `"7.25"`       | `"1"`             |

**Rules:** VAT is 20%, delivery is £4.99. Both must be constants.

**The program must:**

1.  Store every price and quantity in a `String` variable exactly as shown.

2.  Convert them with `Double.valueOf` / `Integer.valueOf`.

3.  Print a line total for each item.

4.  Print the number of items, the subtotal, the VAT, the delivery and the grand total.

5.  Print the grand total in whole pence using a cast.

6.  Use comments and a clear layout.

Expected key values: subtotal `52.2`, grand total `67.63`, `6763` pence, 8 items. One line total prints as `19.950000000000003`: explain why.

- **Hint 1:** convert once into number variables, then use those for every calculation.

- **Hint 2:** grand total = subtotal + VAT + delivery.

### Task 20 — Assessment-style practice: download time calculator

**Class:** `Task20Download` · **Time limit:** 30 minutes, no hints.

Practice only: not an official LJMU assessment, and the checklist is not the official marking scheme.

**Specification:** a network tool receives three values as **text**: a file size in megabytes (`"750"`), a connection speed in megabits per second (`"50"`), and a monthly data allowance in gigabytes (`"500"`).

**The program must:**

1.  Store the three inputs as Strings, then convert them to `int` with a wrapper class.

2.  Use constants: `BITS_PER_BYTE = 8`, `SECONDS_PER_MINUTE = 60`, `MB_PER_GB = 1024`.

3.  Calculate the download time in whole seconds (size × 8 ÷ speed) and print it as minutes and seconds: `2 min 0 s`.

4.  Also print the exact time in seconds as a `double`.

5.  Convert the allowance to MB and print how many complete downloads of this file fit in it, and how many MB are left over.

6.  Change the inputs to `"4300"` and `"35"` (one line each) and check the program still gives sensible results.

7.  Header comment, section comments, clear labelled output.

**Self-check (practice only)**

- Inputs held as Strings and converted with `valueOf`

- All three constants used; no magic numbers in calculations

- `/` and `%` used correctly for minutes, seconds and leftovers

- Exact time uses a `double` (cast or `.0`)

- Second test case run and results checked by hand

- Clear, labelled output and consistent layout

Send me your code when done and I will review it against the checklist.

## Progress tracker and reflection

Tick a task when it runs correctly **and** you could explain every line.

- Task 1 — Recap (official Task 1)

- Task 2 — Trace the slide example

- Task 3 — Copy, not link

- Task 4 — Bank balance

- Task 5 — Bug hunt (8 errors)

- Task 6 — Land calculation (official 2a)

- Task 7 — Rectangle area (official 2b)

- Task 8 — Fence length (official 2c)

- Task 9 — Average mark with a constant (official 2d)

- Task 10 — Fix the AreaCalculator

- Task 11 — Text or number (score: \_\_/10)

- Task 12 — Wrapper classes in the API

- Task 13 — Break the converter

- Task 14 — Replace the magic numbers

- Task 15 — Unit converter

- Task 16 — Stock commission (official supplementary)

- Task 17 — Fahrenheit to Celsius (official supplementary)

- Task 18 — Energy drink survey (official supplementary)

- Task 19 — Order from text data

- Task 20 — Download time calculator

**Reflection (send me your answers)**

1.  What is the difference between a compile error and a runtime exception? Give one example of each from this lab.

2.  Why does `num2 = num1;` not link the two variables?

3.  When would you use `Double.valueOf` instead of `Integer.valueOf`?

4.  Name two benefits of a constant over a typed number.

5.  In Task 8, which answer did you think was right for a real fence, and why?

6.  Which task did you need hints for?

## Answer key

Use only after a real attempt. All outputs were produced by running the code with Java 21 (`javac`), not inside Eclipse.

**Task 1.** `num1` 30, `num2` 8, `sum` 38, `prod` 76.

``` java
int num1, num2, sum;
num1 = 25;
num2 = 8;
num1 = num1 + 5;
sum = num1 + num2;
System.out.println("num1 = " + num1 + ", num2 = " + num2 + ", sum = " + sum);
int num3, prod;
num3 = 2;
prod = sum * num3;
System.out.println("prod = " + prod);
```

**Task 2.** Rows: 18/–/– → 45/–/– → 45/45/– → 45/45/9 → 45/45/2. Output `45 45 2`. `num3 = num3 / 4.0;` gives “possible lossy conversion from double to int”. Fixes: declare `num3` as `double` (then 2.25), or `num3 = (int) (num3 / 4.0);` (2).

**Task 3.** `99 5`; after `q = q + 1;` it prints `99 6`. `q = p;` copies the value 5 into `q`’s own memory.

**Task 4.** 350.0 → 274.5 → 279.99 → 259.99.

**Task 5.**

| \#  | Kind    | Fix                                                                |
|-----|---------|--------------------------------------------------------------------|
| 1   | compile | `double area = ...` or `int area = (int) (length * width);`        |
| 2   | compile | `int n = Integer.valueOf(s) + 1;`                                  |
| 3   | compile | `String s = "" + n;` or `String.valueOf(n)`                        |
| 4   | compile | Remove the reassignment, or don’t make it `final`                  |
| 5   | compile | `int total = 0;`                                                   |
| 6   | runtime | `double d = Double.valueOf("42.5");` (or cast to `int` afterwards) |
| 7   | compile | Straight quotes `"Hello"`                                          |
| 8   | compile | `int num;`                                                         |

**Task 6.** `int` version: `8` acres. Exact: `8.947819100091827`. Leftover: `41287` square feet.

``` java
final int SQ_FEET_PER_ACRE = 43560;
int tractSqFeet = 389767;
int wholeAcres = tractSqFeet / SQ_FEET_PER_ACRE;
double exactAcres = (double) tractSqFeet / SQ_FEET_PER_ACRE;
int leftover = tractSqFeet % SQ_FEET_PER_ACRE;
```

**Task 7.** `The area of the rectangle is: 475.45` (extra: `... 475.45 cm squared`).

**Task 8.** Tutorial calculation: 15 × 3.45 = `51.75` m. A straight fence with 15 posts has 14 gaps: 14 × 3.45 prints `48.300000000000004` (about 48.3 m; the tail is a `double` rounding artefact). 51.75 is right if the fence goes all the way round, back to the first post.

**Task 9.** With 72, 58, 91, 64, 47: total `332`, average `66` (int) and `66.4` (exact). `NO_OF_STUDENTS = 6;` gives “cannot assign a value to final variable NO_OF_STUDENTS”.

**Task 10.** Error on `area = length * width;`. Fix A (`double area`) prints `Area is: 345.45`. Fix B (`(int) (length * width)`) prints `Area is: 345`. A carpet shop needs Fix A: cutting off 0.45 m² loses money.

**Task 11.** a `42.4510` · b `52.45` · c `42.4555` · d `42.4510` · e `84.9` · f `30` · g `1020` · h `1020` (the number) · i `2` · j `101`.

**Task 12.** `boxed + plain` = `66`. 9,000,000,000 is larger than the biggest `int` (2,147,483,647), so it needs `Long.valueOf`. Constants: `Integer.MAX_VALUE` = `2147483647`, `Integer.MIN_VALUE` = `-2147483648`. `valueOf` returns an `Integer` object; `parseInt` returns a primitive `int`; both throw `NumberFormatException` for text that is not a valid integer. Character methods: `Character.isDigit('7')` gives `true`; `Character.toUpperCase('a')` gives `A`.

**Task 13.** `Integer.valueOf`: `"42"` → 42 · `"42.0"` crash · `" 42"` crash · `"4 2"` crash · `"-42"` → -42 · `"+42"` → 42 · `""` crash · `"forty-two"` crash · `"007"` → 7 · `"2147483648"` crash (too big). `Double.valueOf`: `"42"` → 42.0 · `"42.0"` → 42.0 · `" 42 "` → 42.0 (spaces at the ends are ignored) · `"1,000"` crash · `".5"` → 0.5.

**Task 14.**

``` java
final double VAT_RATE = 0.2;
final int GROUP_SIZE = 4;
double price = 50.0;
int seats = 40;
double vat = price * VAT_RATE;
double total = price + vat;
int groups = seats / GROUP_SIZE;
int spare = seats % GROUP_SIZE;
```

Output `Total: 60.0` and `Groups: 10, spare: 0`. With `VAT_RATE = 0.175`: `Total: 58.75`.

**Task 15.** `26.2 miles = 42.1648128 km` · `70 kg = 154.3234 lb` · `180 cm = 70.86614173228347 inches` · `5 miles = 8.04672 km`.

**Task 16.** Cost `13062.0`, commission `261.24`, total `13323.24`.

**Task 17.** 212 → 100 · 100 → 37 · 98.6 → 37 · 32 → 0 · 0 → -17 · -40 → -40. A cast cuts towards zero, so −17.78 becomes −17, not −18. Model: `int celsius = (int) ((fahrenheit - 32) * 5 / 9);`

**Task 18.** Energy-drink buyers `1496.04`; citrus `957.4656`; as an `int`, `957`. A cast always cuts down towards zero; for whole people, rounding would be fairer (rounding methods come later).

**Task 19.** Line totals `25.0`, `19.950000000000003`, `7.25`; 8 items; subtotal `52.2`; VAT `10.440000000000001`; grand total `67.63`; `6763` pence. 3.99 cannot be stored exactly in binary, so × 5 shows a tiny error.

**Task 20.** One model answer:

``` java
package lab3;

/*
 * Task 20 model answer: download time calculator.
 * Inputs arrive as text and are converted with Integer.valueOf.
 */
public class Task20Download {

    public static void main(String[] args) {
        // Constants
        final int BITS_PER_BYTE = 8;
        final int SECONDS_PER_MINUTE = 60;
        final int MB_PER_GB = 1024;

        // Inputs (as text)
        String sizeText = "750";      // file size in MB
        String speedText = "50";      // speed in megabits per second
        String allowanceText = "500"; // monthly allowance in GB

        // Convert text to numbers
        int sizeMb = Integer.valueOf(sizeText);
        int speedMbps = Integer.valueOf(speedText);
        int allowanceGb = Integer.valueOf(allowanceText);

        // Download time
        int seconds = sizeMb * BITS_PER_BYTE / speedMbps;
        double exactSeconds = (double) sizeMb * BITS_PER_BYTE / speedMbps;

        // Allowance
        int allowanceMb = allowanceGb * MB_PER_GB;
        int downloads = allowanceMb / sizeMb;
        int leftoverMb = allowanceMb % sizeMb;

        // Report
        System.out.println("DOWNLOAD CALCULATOR");
        System.out.println("-------------------");
        System.out.println("File: " + sizeMb + " MB at " + speedMbps + " Mbps");
        System.out.println("Time: " + (seconds / SECONDS_PER_MINUTE) + " min "
                + (seconds % SECONDS_PER_MINUTE) + " s");
        System.out.println("Exact time: " + exactSeconds + " s");
        System.out.println();
        System.out.println("Allowance: " + allowanceMb + " MB");
        System.out.println("Full downloads that fit: " + downloads);
        System.out.println("MB left over: " + leftoverMb);
    }

}
```

| Inputs           | Time        | Exact               | Allowance | Fit | Left over |
|------------------|-------------|---------------------|-----------|-----|-----------|
| 750 MB, 50 Mbps  | 2 min 0 s   | 120.0 s             | 512000 MB | 682 | 500 MB    |
| 4300 MB, 35 Mbps | 16 min 22 s | 982.8571428571429 s | 512000 MB | 119 | 300 MB    |
