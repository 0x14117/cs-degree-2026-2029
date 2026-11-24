# Lab 16 — Classes and Objects Hands-on Workbook (20 Tasks)

**Module:** 4300COMP Introduction to Programming · **Language:** Java

## How to use this lab

This lab has **20 hands-on tasks** on Lecture 16: writing classes with fields, constructors and methods; creating objects; references; instance versus static members; `private` fields with accessors and mutators; default and overloaded constructors; and `this`. **All four official Tutorial 16 tasks are included** (Tasks 4, 11, 12 and 13), marked "official", along with the tutorial's `Car` example (Task 2).

**Learning outcomes:** MLO4 (object-oriented basics) throughout; MLO1 and MLO3 in Part D.

**Setup:** create a Java project called **Lab16** in Eclipse (untick *Create module-info.java*). **Each public class goes in its own file**, named exactly after the class: use **File > New > Class** for each. Keep `main` in a separate "demo" class (for example `Person.java` and `PersonDemo.java`).

**Rules for this lab:**

1. **Draw objects as boxes** with their field values, and variables as arrows pointing at them.
2. **Fields `private`, methods `public`** unless a task says otherwise.
3. **Test each class from a demo `main`** before using it in a bigger program.
4. Predict before you run; use the hints only after a real attempt.

The **tracker** is near the end, followed by the **answer key**. Every answer was compiled and run with Java 21 (javac on the command line, not Eclipse).

## Part A — First classes and objects (Tasks 1–5)

### Task 1 — Class or object?

**Goal:** use the vocabulary correctly.

1. In this code, identify the **class**, the **fields**, the **constructor**, the **method**, and the **objects** that are created:

```java
public class Lamp {
    private boolean on;
    private String room;

    public Lamp(String room) {
        this.room = room;
        this.on = false;
    }

    public void toggle() {
        on = !on;
    }
}
// elsewhere:
Lamp kitchen = new Lamp("Kitchen");
Lamp hall = new Lamp("Hall");
kitchen.toggle();
```

2. After the last line, what is the value of each lamp's `on` field? Why are they different?
3. For each pair, say which is the class and which is an object: (Student, "you"); (your phone, Phone); (Module, 4300COMP); (Car, DL65 SEN).

### Task 2 — The tutorial's Car

**Classes:** `Car`, `CarDemo` · **Goal:** create objects and use the dot operator.

1. Create `Car.java` with Tutorial 16's class (two fields, a constructor, `calcAge`), and `CarDemo.java` with the tutorial's `main`, adding `println`s so you can see `regNo` and `carAge`.
2. Run it. Expected: `DL65 SEN`, then `1`.
3. Add a second car `"XYZ 444V"` from 1979 and print its age in 2026. Then change only the first car's year and show the second car is unaffected.
4. **Careful:** the slides' and tutorial's `calcAge` may show `year – regYear` with an en dash. Type a normal minus `-`. What happens if you paste the en dash?

### Task 3 — References puzzle

**Class:** `RefPuzzle` · **Goal:** count variables and objects.

```java
Car myCar = new Car("DL65 SEN", 2016);
Car oldCar = new Car("XYZ 444V", 1979);
Car copyCar = new Car("DL65 SEN", 2016);
Car sameCar = myCar;
oldCar = myCar;
```

1. Draw the variables and objects after **each** line.
2. Answer the slides' question: how many variables, and how many unique objects, by the last line? How many objects were **created**? What happens to the one nobody points to?
3. Predict, then print: `myCar == sameCar`, `myCar == copyCar`, `oldCar.regNo`.
4. Add `sameCar.regYear = 2000;` and print `myCar.regYear`. Explain.

### Task 4 — Official Tutorial 16, Task 1: Person

**Classes:** `Person`, `PersonDemo` · **Goal:** write a class from a specification.

**Private members:** `String name`, `int age`, `char sexType` (`'m'` or `'f'`).

**Public methods:** `Person(String name, int age, char sexType)`, a constructor that sets all three; `void print()`, which prints the person's details.

Write a `main` that creates three people and prints each: Joe Bloggs, 21, m; Sue White, 22, f; Ben Black, 23, m.

Then: try to print `p1.name` from `PersonDemo`. What happens, and why is that what we want?

### Task 5 — Instance versus static

**Class:** add to `Person` · **Goal:** see one-copy-per-object versus one-copy-per-class.

1. Add `private static int peopleCreated = 0;` to `Person` and increase it in the constructor.
2. Add `public static int getPeopleCreated()` and print `Person.getPeopleCreated()` after creating the three people. Expected: 3.
3. Why would it be wrong to make `name` static? Try it and print all three people.
4. Try to call `print()` as `Person.print()`. What error do you get? Why?

## Part B — Find and fix (Tasks 6–10)

### Task 6 — Class error clinic

**Goal:** recognise the common errors with classes and objects.

Using the final `Car` class from Lecture 16 (with `private int regYear` and two constructors), each line below goes in a separate `main` in another class. Record the error, explain it, fix it.

```java
Car c1 = new Car("X1", 2010); c1.regYear = 2000;      // 1
Car c2 = new Car();                                   // 2
Car c3; System.out.println(c3.calcAge(2026));         // 3
Car c4 = new Car(2010, "X1");                         // 4
int age = calcAge(2026);                              // 5
int r = Math.round(1.7899);                           // 6
```

Also: (7) put `public class CarDemo2 { }` at the bottom of `Car.java` and compile; (8) write `public int getYear{` (no brackets) in a class.

### Task 7 — The missing `this`

**Class:** `NoThis` · **Goal:** see why `this` matters in constructors.

```java
public class NoThis {
    String name;
    int age;
    public NoThis(String name, int age) {
        name = name;
        age = age;
    }
    public static void main(String[] a) {
        NoThis n = new NoThis("Joe", 21);
        System.out.println(n.name + " " + n.age);
    }
}
```

1. Predict, then run. Explain the output using the word **shadowing** (Lecture 15).
2. Fix it with `this`.
3. Fix it a second way, by renaming the parameters. Which do you find clearer?

### Task 8 — Encapsulate the Car

**Class:** `Car` · **Goal:** information hiding with accessor and mutator methods.

1. Make `regYear` `private`. Which lines in `CarDemo` now fail to compile?
2. Add an accessor `getYear()` and fix `CarDemo` to use it.
3. Add the slides' mutator `setYear(int year)`, which refuses years in the future (`import java.time.Year;` and `Year.now().getValue()`). Test it with 2015 and 2099.
4. The slides ask whether silently refusing could confuse other programmers. Write a second version, `boolean trySetYear(int year)`, that returns whether the change was accepted, and print the result.

### Task 9 — Default constructors

**Classes:** `Plain`, `PlainDemo` · **Goal:** see when Java provides a constructor for you.

1. Write `Plain` with fields `String name;` and `int size;` and **no** constructor. In `PlainDemo`, create `new Plain()` and print both fields. What are they?
2. Now add a constructor `Plain(String name, int size)`. Does `new Plain()` still compile? Copy the error.
3. Make both work by adding a no-argument constructor yourself.
4. The slides ask: do we want to allow "blank" `Car` objects with no registration? Give one reason for and one against.

### Task 10 — Overloaded constructors and this(...)

**Class:** `Car` · **Goal:** several ways to create an object.

1. Add the slides' second constructor `Car(String regNo)` that calls `this(regNo, Year.now().getValue());`.
2. Create cars with both constructors and print their years.
3. Move the `this(...)` call so it is the **second** line of the constructor. What error do you get?
4. Add a `private static int carsMade` counter in the two-parameter constructor. Create three cars using both constructors. Is each car counted once? Why?

## Part C — Official tutorial tasks (Tasks 11–15)

### Task 11 — Official Tutorial 16, Task 2: Rectangle

**Classes:** `Rectangle`, `RectangleDemo` · **Goal:** two constructors, a returning method and a void method.

**Private members:** `double width`, `double height`.

**Public methods:**

- `Rectangle()`: default constructor creating a 1 by 1 rectangle;
- `Rectangle(double w, double h)`: a rectangle of the given width and height;
- `double area()`: calculates and returns the area;
- `void scale(double factor)`: scales the rectangle by the factor.

In `main`, create three rectangles: the default, a 2 × 3 and a 4 × 6. Print their areas. Then scale the first by 4 and the second by 0.5, and print the new areas.

Expected: `1.0, 6.0, 24.0`, then `16.0, 1.5`.

- **Hint 1:** the default constructor can call the other one: `this(1.0, 1.0);`.

### Task 12 — Official Tutorial 16, Task 3: Student

**Classes:** `Student`, `StudentDemo` · **Goal:** a class with an array field.

**Private members:** `int id`, `String name`, `String course`, `int[] marks` (5 marks, 0–100).

**Public methods:** `Student(int id, String name, String course, int[] marks)`; `int average()`, which calculates and returns the average mark; `void print()`, which prints the student's details.

Create and print three students, with their averages:

- 1234 Joe Bloggs, Computer Studies, {67, 55, 78, 72, 50}
- 2341 Sue White, Computer Science, {57, 85, 58, 49, 61}
- 3412 Ben Black, Software Engineering, {71, 45, 66, 70, 51}

Use the tutorial's hint to pass the array in the constructor call: `new Student(1234, "Joe Bloggs", "Computer Studies", new int[]{67, 55, 78, 72, 50});`

**Question:** the specification says `average()` returns an `int`. What are the exact averages, and what does an `int` average lose? Add `double exactAverage()` for comparison.

### Task 13 — Official Tutorial 16, Task 4: adding rectangles

**Class:** `Rectangle` · **Goal:** a method that takes an object of its own class and returns a new object.

Add to `Rectangle`:

`Rectangle add(Rectangle r)`: adds `r`'s width and height to the current rectangle's, and **returns a new `Rectangle`**.

Revise Task 11's `main` to add together the first and second rectangles and print the new area.

**Watch out for an ambiguity:** the tutorial doesn't say whether to add them **before** or **after** Task 11's scaling. Work out both answers by hand, then print both. Does `add` change `r1` itself? Should it?

- **Hint 1:** inside `add`, you can read `r.width` directly, even though it is `private`. Privacy is per **class**, not per object.

### Task 14 — Describing objects

**Class:** add to `Rectangle` and `Person` · **Goal:** a method that returns a description.

1. Print a `Person` object directly with `System.out.println(p1);`. What appears?
2. Add `String describe()` to `Rectangle` that returns, for example, `4.0 x 6.0`. Use it in your `RectangleDemo` output.
3. Why is a method that **returns** a String more flexible than `print()`, which prints it? (Think about writing to a file, or building a bigger message.)

(The slides say a special method called `toString` does this job automatically; it comes in later sessions.)

### Task 15 — Objects in a list

**Class:** `PersonDemo` · **Goal:** collections of objects.

1. Add accessors `getName()` and `getAge()` to `Person`.
2. Put the three people into an `ArrayList<Person>`.
3. Find and print the **oldest** person, using a for-each loop and the accessors.
4. Print everyone older than 21.

## Part D — Designing with classes (Tasks 16–20)

### Task 16 — A bank account that protects itself

**Classes:** `BankAccount`, `BankDemo` · **Goal:** encapsulation that enforces rules.

- Private fields: `String owner`, `int balancePence` (starts at 0, **never negative**).
- `boolean deposit(int pence)`: refuses zero or negative amounts.
- `boolean withdraw(int pence)`: refuses zero, negative, or more than the balance.
- `int getBalance()` and `String getOwner()`. There is **no** `setBalance`.

Test: deposit 5000 (true), deposit −200 (false), withdraw 1999 (true), withdraw 9999 (false). Expected final balance: **£30.01**.

**Why it matters:** with `balancePence` private and no setter, no other class can make the balance negative, even by mistake. That rule now lives in one place.

### Task 17 — A network device inventory

**Classes:** `Device`, `DeviceDemo` · **Goal:** an object holding a list, with validation and a risk check.

- Private fields: `String hostname`, `String ip`, `ArrayList<Integer> openPorts` (created in the constructor).
- `boolean addPort(int port)`: refuses ports outside 1–65535 and duplicates.
- `boolean isExposed()`: true if port 23 (Telnet) or 3389 (Remote Desktop) is open.
- `String describe()`: one formatted line, ending `REVIEW` if exposed, otherwise `ok`.

Create `web01` (10.0.0.10: ports 80, 443), `legacy` (10.0.0.23: ports 23, 80) and `desk-17` (10.0.0.57: port 3389). Store them in an `ArrayList<Device>`, print every description, and finish with `2 of 3 devices need review.`

**Cyber security link:** Telnet sends everything, including passwords, unencrypted; exposed Remote Desktop is a frequent target of password-guessing attacks. An inventory of what is open on each device is a basic step in securing any network. (Only ever scan or inventory devices you own or are authorised to assess.)

### Task 18 — Ticket numbers with a static counter

**Classes:** `Ticket`, `TicketDemo` · **Goal:** combine a static counter with instance fields.

Each new `Ticket(String issue)` gets the next ID automatically (1, 2, 3, …) from a `private static int nextId`. Add `String describe()` returning `#1: Printer offline`, and `static int ticketsCreated()`.

Create three tickets and print them and the count. Explain why `nextId` must be static and `id` must not be.

### Task 19 — Mini-project: user account with lockout

**Classes:** `UserAccount`, `LoginDemo` · **Goal:** rebuild Lab 8's PIN lockout as a class that guards its own state.

- Private fields: `String username`, `String pin`, `int failedAttempts`, `boolean locked`; a `private static final int MAX_ATTEMPTS = 3`.
- `boolean tryLogin(String attempt)`: returns false at once if locked; on success resets the failure count and returns true; on failure adds 1 and locks the account at 3 failures.
- `boolean isLocked()`, `int attemptsLeft()`, and `void unlock()` (for an administrator).

Test with the attempts `1111, 4821, 0000, 1234, 9999, 4821`, printing the result, `isLocked()` and `attemptsLeft()` after each. Then `unlock()` and log in again.

**Questions:** (1) Why does the **correct** PIN fail on the last attempt? (2) Compare with Lab 8 Task 20: what is better about keeping the attempt count inside the object? (3) This toy stores the PIN as plain text. Real systems never do. What do they store instead?

### Task 20 — Assessment-style task: library loans

**Classes:** `Book`, `Library` · **Goal:** a complete program combining a class, an `ArrayList` of objects, file input and a command loop.

This is a practice task similar in skills to the module's application assessments. It is **not** an actual assessment question.

**`Book`:** private `isbn`, `title`, `author`, `onLoan` (initially false); accessors; `boolean lend()` (false if already on loan); `boolean giveBack()` (false if not on loan); `String describe()` (one aligned line with `ON LOAN` or `available`).

**`Library`:** loads `books.txt`, where each line is `isbn;title;author`:

```text
B01;Java Programming;Malik
B02;Computer Systems;Bryant
B03;Security Engineering;Anderson
B04;The Cuckoo's Egg;Stoll
B05;Head First Java;Sierra
```

It then reads commands until `quit`:

| Command | Effect |
| --- | --- |
| `list` | Every book's description |
| `borrow ISBN` | Lend it, or say it is already on loan or doesn't exist |
| `return ISBN` | Return it, or say it wasn't on loan or doesn't exist |
| `author TEXT` | Books whose author contains TEXT (ignoring case), and the number found |
| `quit` | Print how many books are on loan, then stop |
| anything else | A help line |

ISBNs should match ignoring case (`b03` = `B03`).

**Test input** (write the expected output for each line **before** running):

```text
list
borrow B03
borrow b03
return B05
borrow B99
author an
return B03
borrow B01
help
quit
```

- **Hint 1:** split each file line with `indexOf(";")` and `indexOf(";", first + 1)` (Lecture 13).
- **Hint 2:** a helper `Book findBook(String isbn)` that searches the list keeps the command code short.

## Tracker

| Task | Done | Notes / score |
| --- | --- | --- |
| 1 Class or object | ☐ | |
| 2 Tutorial Car | ☐ | |
| 3 References puzzle | ☐ | |
| 4 Official Task 1: Person | ☐ | |
| 5 Instance vs static | ☐ | |
| 6 Error clinic (out of 8) | ☐ | |
| 7 Missing this | ☐ | |
| 8 Encapsulate Car | ☐ | |
| 9 Default constructors | ☐ | |
| 10 Overloaded constructors | ☐ | |
| 11 Official Task 2: Rectangle | ☐ | |
| 12 Official Task 3: Student | ☐ | |
| 13 Official Task 4: add | ☐ | |
| 14 Describing objects | ☐ | |
| 15 Objects in a list | ☐ | |
| 16 Bank account | ☐ | |
| 17 Device inventory | ☐ | |
| 18 Ticket counter | ☐ | |
| 19 User account lockout | ☐ | |
| 20 Library loans | ☐ | |

## Reflection

1. Explain the difference between a class and an object to someone who has never programmed.
2. When should a member be `static`, and when should it belong to each object? Use one example from this lab.
3. Why make fields `private` and provide methods, instead of making everything `public`?
4. Compare Task 19 with Lab 8 Task 20. What has object orientation added?

## Answer key

All code was compiled and run with Java 21 (javac on the command line, not Eclipse). Outputs are actual outputs. Each public class goes in its own file.

**Task 1.** Class `Lamp`; fields `on` and `room`; constructor `Lamp(String room)`; method `toggle`; two objects (kitchen and hall). After `kitchen.toggle()`, the kitchen lamp's `on` is `true` and the hall's is `false`: each object has its own copy of the fields. Classes: Student, Phone, Module, Car; objects: you, your phone, 4300COMP, DL65 SEN.

**Task 2.**

```java
public class Car {
    String regNo;
    int regYear;

    public Car(String regNo, int year) {
        this.regNo = regNo;
        this.regYear = year;
    }

    public int calcAge(int year) {
        return year - regYear;
    }
}
```

With the tutorial's `main` plus prints: `DL65 SEN`, then `1` (verified). The 1979 car is 47 in 2026. The en dash gives `error: illegal character: '–'` (verified).

**Task 3.** 4 variables; 3 objects created; 2 still reachable; the XYZ car becomes unreachable and is garbage-collected. `true`, `false`, `DL65 SEN` (verified). `sameCar.regYear = 2000;` changes `myCar.regYear` too: both variables refer to the same object.

**Tasks 4, 5, 14 and 15.**

```java
public class Person {
    private String name;
    private int age;
    private char sexType;        // 'm' or 'f', as the tutorial specifies

    public Person(String name, int age, char sexType) {
        this.name = name;
        this.age = age;
        this.sexType = sexType;
    }

    public void print() {
        System.out.println(name + ", " + age + ", " + sexType);
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }
}
```

```java
import java.util.ArrayList;

public class PersonDemo {
    public static void main(String[] args) {
        Person p1 = new Person("Joe Bloggs", 21, 'm');
        Person p2 = new Person("Sue White", 22, 'f');
        Person p3 = new Person("Ben Black", 23, 'm');
        p1.print();
        p2.print();
        p3.print();

        ArrayList<Person> people = new ArrayList<Person>();
        people.add(p1);
        people.add(p2);
        people.add(p3);
        Person oldest = people.get(0);
        for (Person p : people) {
            if (p.getAge() > oldest.getAge()) {
                oldest = p;
            }
        }
        System.out.println("Oldest: " + oldest.getName());
        System.out.println(p1);
    }
}
```

Output (verified):

```text
Joe Bloggs, 21, m
Sue White, 22, f
Ben Black, 23, m
Oldest: Ben Black
Person@3764951d
```

(The code after `@` varies.) `p1.name` from `PersonDemo` gives `error: name has private access in Person`: only `Person` can touch its data. Task 5: with a static counter, `Person.getPeopleCreated()` prints 3. A static `name` would be shared, so every person would print the **last** name set. `Person.print()` fails with `error: non-static method print() cannot be referenced from a static context`: `print` needs a particular person.

**Task 6.** (1) `error: regYear has private access in Car`. (2) `error: no suitable constructor found for Car(no arguments)`. (3) `error: variable c3 might not have been initialized`. (4) `error: incompatible types: int cannot be converted to String`. (5) `error: cannot find symbol` (no object). (6) `error: incompatible types: possible lossy conversion from long to int`. (7) `error: class CarDemo2 is public, should be declared in a file named CarDemo2.java`. (8) `error: ';' expected`. All verified.

**Task 7.** Prints `null 0` (verified): inside the constructor, the parameters shadow the fields, so `name = name;` assigns each parameter to itself. Fix: `this.name = name; this.age = age;`, or rename the parameters (`newName`, `newAge`).

**Tasks 8 and 10.** The final `Car` and `CarDemo` are in Lecture 16, section 10 (verified). Making `regYear` private breaks `myCar.regYear = 2015;` in `CarDemo` (`has private access`). `setYear(2099)` is refused (in 2026). `trySetYear`:

```java
public boolean trySetYear(int year) {
    if (year <= Year.now().getValue()) {
        regYear = year;
        return true;
    }
    return false;
}
```

`this(...)` as the second line gives an error saying the call to `this` must be the **first statement** in the constructor. Each car is counted once: the one-parameter constructor passes on to the two-parameter one, which does the counting.

**Task 9.** With no constructor: `null 0` (verified). After adding `Plain(String name, int size)`, `new Plain()` fails with `error: constructor Plain in class Plain cannot be applied to given types;`. Adding `public Plain() { }` makes both work. For blank cars: convenient when the data arrives later. Against: an object can exist in an invalid state (no registration), causing bugs later.

**Tasks 11, 13 and 14 (Rectangle).**

```java
public class Rectangle {
    private double width;
    private double height;

    /** Default constructor: a 1 by 1 rectangle. */
    public Rectangle() {
        this(1.0, 1.0);
    }

    public Rectangle(double w, double h) {
        width = w;
        height = h;
    }

    public double area() {
        return width * height;
    }

    public void scale(double factor) {
        width = width * factor;
        height = height * factor;
    }

    /** Return a NEW rectangle whose sides are the sums of this one's and r's. */
    public Rectangle add(Rectangle r) {
        return new Rectangle(this.width + r.width, this.height + r.height);
    }

    public String describe() {
        return width + " x " + height;
    }
}
```

```java
public class RectangleDemo {
    public static void main(String[] args) {
        Rectangle r1 = new Rectangle();
        Rectangle r2 = new Rectangle(2, 3);
        Rectangle r3 = new Rectangle(4, 6);
        System.out.println("Areas: " + r1.area() + ", " + r2.area() + ", " + r3.area());

        Rectangle sumBefore = r1.add(r2);         // Task 4, before scaling
        System.out.println("r1 + r2 before scaling: " + sumBefore.describe() + ", area " + sumBefore.area());

        r1.scale(4);
        r2.scale(0.5);
        System.out.println("After scaling: " + r1.area() + ", " + r2.area());

        Rectangle sumAfter = r1.add(r2);          // Task 4, after scaling
        System.out.println("r1 + r2 after scaling: " + sumAfter.describe() + ", area " + sumAfter.area());
        System.out.println("r1 unchanged by add: " + r1.describe());
    }
}
```

Output (verified):

```text
Areas: 1.0, 6.0, 24.0
r1 + r2 before scaling: 3.0 x 4.0, area 12.0
After scaling: 16.0, 1.5
r1 + r2 after scaling: 5.0 x 5.5, area 27.5
r1 unchanged by add: 4.0 x 4.0
```

So the answer is 12.0 if you add before scaling and 27.5 after; note your interpretation, and check with your tutor if it matters. `add` returns a **new** rectangle and leaves `r1` unchanged, as the tutorial's "return a new Rectangle" suggests. A method returning a String can be printed, written to a file or joined into other text; `print()` can only print.

**Task 12.**

```java
public class Student {
    private int id;
    private String name;
    private String course;
    private int[] marks;          // 5 marks, 0-100

    public Student(int id, String name, String course, int[] marks) {
        this.id = id;
        this.name = name;
        this.course = course;
        this.marks = marks;
    }

    /** The average mark, as the tutorial specifies: an int (the decimal part is dropped). */
    public int average() {
        int total = 0;
        for (int m : marks) {
            total = total + m;
        }
        return total / marks.length;
    }

    /** A more accurate average, for comparison. */
    public double exactAverage() {
        int total = 0;
        for (int m : marks) {
            total = total + m;
        }
        return (double) total / marks.length;
    }

    public void print() {
        System.out.print(id + " " + name + ", " + course + ", marks:");
        for (int m : marks) {
            System.out.print(" " + m);
        }
        System.out.println();
    }
}
```

```java
public class StudentDemo {
    public static void main(String[] args) {
        Student s1 = new Student(1234, "Joe Bloggs", "Computer Studies", new int[]{67, 55, 78, 72, 50});
        Student s2 = new Student(2341, "Sue White", "Computer Science", new int[]{57, 85, 58, 49, 61});
        Student s3 = new Student(3412, "Ben Black", "Software Engineering", new int[]{71, 45, 66, 70, 51});
        Student[] students = {s1, s2, s3};
        for (Student s : students) {
            s.print();
            System.out.printf("  average %d (exact %.1f)%n", s.average(), s.exactAverage());
        }
    }
}
```

Output (verified):

```text
1234 Joe Bloggs, Computer Studies, marks: 67 55 78 72 50
  average 64 (exact 64.4)
2341 Sue White, Computer Science, marks: 57 85 58 49 61
  average 62 (exact 62.0)
3412 Ben Black, Software Engineering, marks: 71 45 66 70 51
  average 60 (exact 60.6)
```

An `int` average drops the decimal part (integer division), so 60.6 becomes 60, not 61. Near a grade boundary that matters.

**Task 16.**

```java
public class BankAccount {
    private String owner;
    private int balancePence;          // never negative

    public BankAccount(String owner) {
        this.owner = owner;
        this.balancePence = 0;
    }

    /** Add money; refuses zero or negative amounts. */
    public boolean deposit(int pence) {
        if (pence <= 0) {
            return false;
        }
        balancePence = balancePence + pence;
        return true;
    }

    /** Take money out; refuses if it would go overdrawn. */
    public boolean withdraw(int pence) {
        if (pence <= 0 || pence > balancePence) {
            return false;
        }
        balancePence = balancePence - pence;
        return true;
    }

    public int getBalance() {
        return balancePence;
    }

    public String getOwner() {
        return owner;
    }
}
```

```java
public class BankDemo {
    public static void main(String[] args) {
        BankAccount acc = new BankAccount("Sam Archer");
        System.out.println(acc.deposit(5000) + " " + acc.deposit(-200) + " " + acc.withdraw(1999) + " " + acc.withdraw(9999));
        System.out.printf("%s has £%.2f%n", acc.getOwner(), acc.getBalance() / 100.0);
    }
}
```

Output (verified): `true false true false` and `Sam Archer has £30.01`.

**Task 17.**

```java
import java.util.ArrayList;

public class Device {
    private String hostname;
    private String ip;
    private ArrayList<Integer> openPorts;

    public Device(String hostname, String ip) {
        this.hostname = hostname;
        this.ip = ip;
        this.openPorts = new ArrayList<Integer>();
    }

    /** Record an open port; refuses invalid or duplicate ports. */
    public boolean addPort(int port) {
        if (port < 1 || port > 65535 || openPorts.contains(port)) {
            return false;
        }
        openPorts.add(port);
        return true;
    }

    /** True if a risky remote-access port is open: Telnet (23) or RDP (3389). */
    public boolean isExposed() {
        return openPorts.contains(23) || openPorts.contains(3389);
    }

    public String describe() {
        String risk = "ok";
        if (isExposed()) {
            risk = "REVIEW";
        }
        return String.format("%-10s %-15s ports %-16s %s", hostname, ip, openPorts, risk);
    }
}
```

```java
import java.util.ArrayList;

public class DeviceDemo {
    public static void main(String[] args) {
        ArrayList<Device> network = new ArrayList<Device>();

        Device web = new Device("web01", "10.0.0.10");
        web.addPort(80);
        web.addPort(443);
        Device legacy = new Device("legacy", "10.0.0.23");
        legacy.addPort(23);
        legacy.addPort(80);
        Device desk = new Device("desk-17", "10.0.0.57");
        desk.addPort(3389);
        System.out.println(desk.addPort(3389) + " " + desk.addPort(70000));

        network.add(web);
        network.add(legacy);
        network.add(desk);
        int exposed = 0;
        for (Device d : network) {
            System.out.println(d.describe());
            if (d.isExposed()) {
                exposed++;
            }
        }
        System.out.println(exposed + " of " + network.size() + " devices need review.");
    }
}
```

Output (verified):

```text
false false
web01      10.0.0.10       ports [80, 443]        ok
legacy     10.0.0.23       ports [23, 80]         REVIEW
desk-17    10.0.0.57       ports [3389]           REVIEW
2 of 3 devices need review.
```

The list field is created in the constructor; without `new ArrayList<Integer>()`, `addPort` would throw `NullPointerException`.

**Task 18.**

```java
public class Ticket {
    private static int nextId = 1;     // shared by the class: one copy
    private int id;                    // one per object
    private String issue;

    public Ticket(String issue) {
        this.id = nextId;
        nextId++;
        this.issue = issue;
    }

    public String describe() {
        return "#" + id + ": " + issue;
    }

    public static int ticketsCreated() {
        return nextId - 1;
    }
}
```

```java
public class TicketDemo {
    public static void main(String[] args) {
        Ticket a = new Ticket("Printer offline");
        Ticket b = new Ticket("Password reset");
        Ticket c = new Ticket("Phishing email reported");
        System.out.println(a.describe());
        System.out.println(b.describe());
        System.out.println(c.describe());
        System.out.println("Created: " + Ticket.ticketsCreated());
    }
}
```

Output (verified): `#1: Printer offline`, `#2: Password reset`, `#3: Phishing email reported`, `Created: 3`. `nextId` must be shared so each new ticket continues the sequence; `id` must belong to each ticket, or every ticket would show the latest number.

**Task 19.**

```java
public class UserAccount {
    private static final int MAX_ATTEMPTS = 3;

    private String username;
    private String pin;              // a toy example: real systems store a salted hash, never the PIN
    private int failedAttempts;
    private boolean locked;

    public UserAccount(String username, String pin) {
        this.username = username;
        this.pin = pin;
        this.failedAttempts = 0;
        this.locked = false;
    }

    /** Try to log in. Returns true only if the account is unlocked and the PIN matches. */
    public boolean tryLogin(String attempt) {
        if (locked) {
            return false;
        }
        if (pin.equals(attempt)) {
            failedAttempts = 0;
            return true;
        }
        failedAttempts++;
        if (failedAttempts >= MAX_ATTEMPTS) {
            locked = true;
        }
        return false;
    }

    public boolean isLocked() {
        return locked;
    }

    public int attemptsLeft() {
        return MAX_ATTEMPTS - failedAttempts;
    }

    /** An administrator unlocks the account. */
    public void unlock() {
        locked = false;
        failedAttempts = 0;
    }

    public String getUsername() {
        return username;
    }
}
```

```java
public class LoginDemo {
    public static void main(String[] args) {
        UserAccount sam = new UserAccount("sam", "4821");
        String[] attempts = {"1111", "4821", "0000", "1234", "9999", "4821"};
        for (String a : attempts) {
            boolean ok = sam.tryLogin(a);
            String result = "denied";
            if (ok) {
                result = "OK";
            }
            System.out.printf("%s -> %s (locked: %b, left: %d)%n", a, result, sam.isLocked(), sam.attemptsLeft());
        }
        sam.unlock();
        System.out.println("After unlock: " + sam.tryLogin("4821"));
    }
}
```

Output (verified):

```text
1111 -> denied (locked: false, left: 2)
4821 -> OK (locked: false, left: 3)
0000 -> denied (locked: false, left: 2)
1234 -> denied (locked: false, left: 1)
9999 -> denied (locked: true, left: 0)
4821 -> denied (locked: true, left: 0)
After unlock: true
```

(1) After three failures the account is locked, and a locked account refuses even the correct PIN; that is the point of a lockout. (2) No other code can reset the counter or unlock the account except through the class's own methods; in Lab 8 any line of `main` could change the variables. (3) A **hash** of the PIN or password, made with a slow, salted password-hashing algorithm, so a stolen database does not reveal the secrets directly.

**Task 20.**

```java
public class Book {
    private String isbn;
    private String title;
    private String author;
    private boolean onLoan;

    public Book(String isbn, String title, String author) {
        this.isbn = isbn;
        this.title = title;
        this.author = author;
        this.onLoan = false;
    }

    public String getIsbn() { return isbn; }
    public String getTitle() { return title; }
    public String getAuthor() { return author; }
    public boolean isOnLoan() { return onLoan; }

    /** Lend the book; returns false if it is already on loan. */
    public boolean lend() {
        if (onLoan) {
            return false;
        }
        onLoan = true;
        return true;
    }

    /** Return the book; returns false if it was not on loan. */
    public boolean giveBack() {
        if (!onLoan) {
            return false;
        }
        onLoan = false;
        return true;
    }

    public String describe() {
        String status = "available";
        if (onLoan) {
            status = "ON LOAN";
        }
        return String.format("%-5s %-30s %-18s %s", isbn, title, author, status);
    }
}
```

```java
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.Scanner;

public class Library {
    private static ArrayList<Book> books = new ArrayList<Book>();

    public static void main(String[] args) throws FileNotFoundException {
        loadBooks("books.txt");
        Scanner console = new Scanner(System.in);
        boolean running = true;
        while (running) {
            System.out.print("> ");
            String command = console.next().toLowerCase();
            switch (command) {
                case "list":
                    for (Book b : books) {
                        System.out.println(b.describe());
                    }
                    break;
                case "borrow":
                    borrow(console.next());
                    break;
                case "return":
                    giveBack(console.next());
                    break;
                case "author":
                    searchAuthor(console.nextLine().trim());
                    break;
                case "quit":
                    running = false;
                    break;
                default:
                    System.out.println("Commands: list, borrow ISBN, return ISBN, author NAME, quit");
            }
        }
        System.out.println(countOnLoan() + " book(s) on loan at close.");
        console.close();
    }

    /** Each line of the file: isbn;title;author */
    public static void loadBooks(String filename) throws FileNotFoundException {
        Scanner read = new Scanner(new FileReader(filename));
        while (read.hasNextLine()) {
            String line = read.nextLine().trim();
            int first = line.indexOf(";");
            int second = line.indexOf(";", first + 1);
            if (first > 0 && second > first) {
                books.add(new Book(line.substring(0, first), line.substring(first + 1, second), line.substring(second + 1)));
            }
        }
        read.close();
        System.out.println("Loaded " + books.size() + " books.");
    }

    /** Return the book with this ISBN, or null if there is none. */
    public static Book findBook(String isbn) {
        for (Book b : books) {
            if (b.getIsbn().equalsIgnoreCase(isbn)) {
                return b;
            }
        }
        return null;
    }

    public static void borrow(String isbn) {
        Book b = findBook(isbn);
        if (b == null) {
            System.out.println("No book " + isbn + ".");
        } else if (b.lend()) {
            System.out.println("Borrowed: " + b.getTitle());
        } else {
            System.out.println(b.getTitle() + " is already on loan.");
        }
    }

    public static void giveBack(String isbn) {
        Book b = findBook(isbn);
        if (b == null) {
            System.out.println("No book " + isbn + ".");
        } else if (b.giveBack()) {
            System.out.println("Returned: " + b.getTitle());
        } else {
            System.out.println(b.getTitle() + " was not on loan.");
        }
    }

    public static void searchAuthor(String name) {
        int found = 0;
        for (Book b : books) {
            if (b.getAuthor().toLowerCase().contains(name.toLowerCase())) {
                System.out.println(b.describe());
                found++;
            }
        }
        System.out.println(found + " match(es) for \"" + name + "\".");
    }

    public static int countOnLoan() {
        int count = 0;
        for (Book b : books) {
            if (b.isOnLoan()) {
                count++;
            }
        }
        return count;
    }
}
```

Output with the test input (verified, `> ` prompts removed): `Loaded 5 books.`, the five books `available`, `Borrowed: Security Engineering`, `Security Engineering is already on loan.`, `Head First Java was not on loan.`, `No book B99.`, two author matches (Bryant and Anderson, with B03 `ON LOAN`) and `2 match(es) for "an".`, `Returned: Security Engineering`, `Borrowed: Java Programming`, the help line, then `1 book(s) on loan at close.`

Design notes: `findBook` returns `null` for "not found", which Lecture 15 warns about; it is safe here only because **every** caller checks `b == null` straight away. The `books` list is a `private static` field so all of `Library`'s static methods can share it.

**Next:** the slides say later sessions cover structured data design, compound data types, and methods such as `toString` and `equals`.
