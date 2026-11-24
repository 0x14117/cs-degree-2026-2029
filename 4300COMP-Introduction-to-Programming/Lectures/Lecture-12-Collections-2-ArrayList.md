# Lecture 12 — Collections #2: Variable-Size Collections and ArrayList

**Module:** 4300COMP Introduction to Programming · **Language:** Java

## Overview

Lecture 11's arrays have a size that is fixed when they are created. Lecture 12 introduces a collection that **grows and shrinks** as you add and remove items: the **`ArrayList`**. Instead of square brackets, you work with an `ArrayList` through **methods**: `add`, `get`, `set`, `contains`, `remove`, `size` and `isEmpty`. You will also see three ways to iterate over one, including the new **for-each** loop. These notes rewrite the official Lecture 12 slides in plain English. Every program and output shown was compiled and run with Java 21 (javac on the command line, not Eclipse).

**By the end you should be able to:**

1. Explain the difference between static (fixed-size) and dynamic (variable-size) data structures, and when each fits.
2. Import and create an `ArrayList` of any object type, using wrapper classes such as `Integer` for primitive values.
3. Use `add` (both forms), `set`, `get`, `contains`, `remove` (both forms), `size` and `isEmpty`, and predict their effect on a list.
4. Iterate over an `ArrayList` with a regular `for` loop, a for-each loop and a `while` loop.
5. Avoid the classic traps: wrong indices after removal, `remove(int)` versus `remove(Object)`, and removing items while looping.
6. Choose between an array and an `ArrayList`, and convert between them.

**Learning outcomes:** MLO1 (collections and algorithms), MLO2 (using the `java.util` API and its documentation), MLO3 (problems where the amount of data is unknown in advance).

**Matching lab:** Lab 12 (official Tutorial 12: Collections #2).

**What you need from earlier lectures:** wrapper classes `Integer` and `Double` (Lecture 3), `String` methods `equals` and `equalsIgnoreCase` (Lectures 6 and 10), loops (Lectures 8–9), arrays (Lecture 11).

## 1. Recap: fixed-size arrays

- Arrays use square brackets to declare them: `int[] intArray = new int[5];`
- Square brackets also select one element, on the left of an assignment (`values[2] = 12;`) or in an expression (`int thirdValue = values[2] + 3;`).
- A `for` loop visits each element in turn.

## 2. Why variable-size collections?

The slides call arrays **static data structures**: once you choose a size, the amount of memory is fixed. That is fine when you know how many items there are and that number won't change ("a building has 7 floors").

Often you **don't** know: how many students will enrol, how many lines a log file has, how many items a user will add. You could create a huge array and hope it is never exceeded, but that is **wasteful**, and it still fails if the guess is too small.

The better solution is a **variable-size collection** such as `ArrayList`. It **grows** as you add items and **shrinks** as you remove them (the slides call it *elastic*). Collections like this are **dynamic data structures**.

`ArrayList` is one of several collection classes in Java: `LinkedList`, `HashMap`, `TreeSet` and `PriorityQueue` are others. Some keep items in order, some don't; some allow duplicates, some don't. The slides keep to `ArrayList` at a basic level.

## 3. Creating an ArrayList

`ArrayList` lives in the package `java.util`, so it must be **imported**:

```java
import java.util.ArrayList;
```

In Eclipse, **Source > Organize Imports** adds it for you. Without the import, javac reports `error: cannot find symbol` for `ArrayList`.

The general form:

```java
ArrayList<BaseType> aList = new ArrayList<BaseType>();
```

The **base type** in angle brackets says what type of element the list holds:

```java
ArrayList<String> sList = new ArrayList<String>();
```

### The base type must be an object type

The base type **cannot** be a primitive type such as `int`, `char` or `double`. `ArrayList<int>` gives `error: unexpected type`. Use the matching **wrapper class** from Lecture 3:

| Primitive | Wrapper class |
| --- | --- |
| `int` | `Integer` |
| `double` | `Double` |
| `boolean` | `Boolean` |
| `char` | `Character` |

```java
ArrayList<Integer> iList = new ArrayList<Integer>();
```

You still store and read ordinary `int` values. Java converts automatically between `int` and `Integer` (**autoboxing** and **unboxing**, Lecture 3):

```java
iList.add(10);                 // the int 10 is wrapped in an Integer automatically
int first = iList.get(0);      // and unwrapped automatically
```

(The slides say object types are covered properly in a later session.)

## 4. The ArrayList operations

Arrays use the simple square-bracket notation. `ArrayList` supports more kinds of change, so it uses **methods**, called with a dot. The most used are `add`, `set`, `get`, `contains` and `remove`. Some, such as `add` and `remove`, can be used in more than one way.

| Method | What it does |
| --- | --- |
| `add(value)` | Adds `value` at the **end** |
| `add(index, value)` | Inserts `value` **at** `index`, moving later elements up one place |
| `set(index, value)` | **Replaces** the element at `index` |
| `get(index)` | **Returns** the element at `index` |
| `contains(value)` | `true` if `value` is in the list |
| `remove(value)` | Removes the first element equal to `value` |
| `remove(index)` | Removes the element **at** `index`, moving later elements down one place |
| `size()` | The number of elements |
| `isEmpty()` | `true` if the size is 0 |
| `indexOf(value)` | The index of the first match, or −1 |

Indices start at 0, exactly as for arrays. Valid indices are `0` to `size() - 1` (for `add(index, value)` you may also use `size()`, which means "at the end").

### Tracing the slides' example

The slides build up one example step by step. Here it is as one program, printing the list after each step (printing an `ArrayList` directly **does** show its contents, unlike an array):

```java
import java.util.ArrayList;

public class Operations {
    public static void main(String[] args) {
        ArrayList<String> sList = new ArrayList<String>();
        sList.add("Fred");                 System.out.println("add Fred        -> " + sList);
        sList.add(1, "Alice");             System.out.println("add(1, Alice)   -> " + sList);
        sList.set(1, "Sue");               System.out.println("set(1, Sue)     -> " + sList);
        String second = sList.get(1);      System.out.println("get(1)          -> " + second);
        if (sList.contains("Sue")) {
            System.out.println("Sue is in the list");
        }
        sList.remove("Fred");              System.out.println("remove(Fred)    -> " + sList);
        sList.remove(0);                   System.out.println("remove(0)       -> " + sList);
        System.out.println("isEmpty: " + sList.isEmpty() + ", size: " + sList.size());
    }
}
```

**Output (verified):**

```text
add Fred        -> [Fred]
add(1, Alice)   -> [Fred, Alice]
set(1, Sue)     -> [Fred, Sue]
get(1)          -> Sue
Sue is in the list
remove(Fred)    -> [Sue]
remove(0)       -> []
isEmpty: true, size: 0
```

**Slide note: positions move after a removal.** The slide on `remove` runs `sList.remove("Fred");` and then `sList.remove(1);`, describing the second call as removing "Sue". But once Fred is removed, Sue **moves down to position 0**, and the list has only one element. Run as written, `remove(1)` crashes (verified):

```text
Exception in thread "main" java.lang.IndexOutOfBoundsException: Index 1 out of bounds for length 1
```

The next slide (isEmpty and size) correctly uses `remove(0)`, as above. The lesson: **every `add(index, …)` and `remove(…)` changes the positions of the elements after it.**

### The slides' complete example

```java
import java.util.ArrayList;

public class ArrayListExample {
    public static void main(String[] args) {
        ArrayList<String> al = new ArrayList<String>();
        System.out.println("Initial size of al: " + al.size());
        al.add("A");
        al.add("B");
        al.add("C");
        System.out.println("Size of al after additions: " + al.size());
        System.out.println("Contents of al: " + al);
        al.remove("C");
        al.remove(1);
        System.out.println("Size of al after deletions: " + al.size());
        System.out.println("Contents of al: " + al);
    }
}
```

**Output (verified):**

```text
Initial size of al: 0
Size of al after additions: 3
Contents of al: [A, B, C]
Size of al after deletions: 1
Contents of al: [A]
```

`remove("C")` removes the value C; then `remove(1)` removes whatever is at index 1 (B), leaving `[A]`.

**Typing note:** the slide mixes curly and straight quotes (`al.add(“A");`). Curly quotes give `error: illegal character: '“'`; always type straight quotes. The slide's `import java.util.*;` imports every class in `java.util`; importing just `java.util.ArrayList` is clearer.

## 5. Iterating over an ArrayList

As with arrays, iteration goes hand in hand with collections. `ArrayList` offers three common styles. All three print the same names (verified).

**Regular `for` loop** (like arrays, but `size()` and `get(i)`):

```java
for (int i = 0; i < sList.size(); i++) {
    System.out.println(i + " " + sList.get(i));
}
```

**For-each loop** (also called the *enhanced for loop*):

```java
for (String str : sList) {
    System.out.println(str);
}
```

Read it as "for each `String str` in `sList`". On every iteration, `str` holds the next element. There is no index variable, so you cannot use the position, and you must **not** add to or remove from the list inside this loop. Use it when you just need to read every element. It also works on arrays: `for (int value : intArray)`.

**`while` loop** (equivalent to the `for` loop, Lecture 9):

```java
int i = 0;
while (i < sList.size()) {
    System.out.println(i + " " + sList.get(i));
    i++;
}
```

| Need | Best loop |
| --- | --- |
| Read every element, position not needed | for-each |
| Need the index, or need to `set`/`remove` | regular `for` |
| Stop when something is found, or a condition is not count-based | `while` |

## 6. Three traps

### Trap 1: removing while looping forwards

Tutorial 12's supplementary task removes plural words with this loop:

```java
for (int i = 0; i < words.size(); i++) {
    String word = words.get(i);
    if (word.endsWith("s")) {
        words.remove(i);
        i--;              // the next word has moved into position i
    }
}
```

Why `i--`? After `remove(i)`, every later element shifts down one place, so the **next** word is now at position `i`. Without `i--`, the loop's `i++` would skip it. With `[Bread, Apples, Eggs, Milk]` and no `i--`, the result is `[Bread, Eggs, Milk]`: "Eggs" slipped past (verified). An alternative that avoids the problem is looping **backwards**, from `size() - 1` down to 0 (verified to give `[Bread, Milk]`).

### Trap 2: remove(int) versus remove(Object) with Integer lists

With an `ArrayList<Integer>`, `list.remove(7)` removes the element **at index 7**, not the value 7, because the `int` version is chosen. To remove the value, wrap it: `list.remove(Integer.valueOf(7))` (verified).

### Trap 3: comparing Integer objects with ==

Elements of an `ArrayList<Integer>` are `Integer` **objects**. `==` between two objects compares whether they are the **same object** (Lecture 11, section 10), not whether the numbers are equal. Java reuses objects for small values, so `==` happens to work for 127 but **not** for 128 (verified: `true` then `false`). Compare with `.equals()`, or unbox to `int` first (`int a = list.get(0);`).

## 7. ArrayList or array?

The slides give three reasons not to use `ArrayList` everywhere:

1. An `ArrayList` is **less efficient** than an array.
2. It lacks the short, familiar **square-bracket** notation.
3. Its base type must be an **object type**, not `int`, `char` or `double`.

| Use an array when… | Use an `ArrayList` when… |
| --- | --- |
| The number of elements is known and fixed | The number changes or is unknown |
| You store primitives in large numbers | You need to add, insert or remove items |
| Speed and simplicity matter most | You want ready-made `contains`, `indexOf`, `remove` |

**Converting:** an array into a list with a loop (`for` each element, `list.add(...)`, Tutorial 12 Task 2). A list into an array with the `toArray` method mentioned in the slides: `Integer[] asArray = iList.toArray(new Integer[0]);` (verified).

## 8. Common mistakes

| Mistake | Symptom (verified with javac) | Fix |
| --- | --- | --- |
| No import | `error: cannot find symbol` (class `ArrayList`) | `import java.util.ArrayList;` |
| `ArrayList<int>` | `error: unexpected type` | `ArrayList<Integer>` |
| `list[0]` | `error: array required, but ArrayList<String> found` | `list.get(0)` |
| `list.length` or `list.length()` | `error: cannot find symbol` | `list.size()` |
| Adding the wrong type: `stringList.add(5)` | `error: incompatible types: int cannot be converted to String` | Match the base type |
| `list.get(list.size())` | `IndexOutOfBoundsException: Index 1 out of bounds for length 1` (for a list of one) | Last element is `get(size() - 1)` |
| Using old positions after `remove` | `IndexOutOfBoundsException` or the wrong element | Recalculate positions; trace the list |
| Removing forwards without `i--` | Some elements skipped | `i--` after removing, or loop backwards |
| `integerList.remove(7)` to remove the value 7 | Removes index 7 (or crashes) | `remove(Integer.valueOf(7))` |
| `==` between `Integer` elements | Works for small values only | `.equals()` or unbox to `int` |
| Curly quotes copied from slides | `error: illegal character: '“'` | Straight quotes |

## 9. Check yourself — 15 multiple-choice questions

1. Why are arrays called static data structures? (A) they use `static` (B) their size is fixed once created (C) they cannot be changed at all (D) they are stored in a file
2. Which line creates a list of whole numbers? (A) `ArrayList<int> a = new ArrayList<int>();` (B) `ArrayList<Integer> a = new ArrayList<Integer>();` (C) `ArrayList a = new int[5];` (D) `Integer[] a = new ArrayList();`
3. After `list.add("A"); list.add("B"); list.add(1, "C");`, what is `list`? (A) `[A, B, C]` (B) `[A, C, B]` (C) `[C, A, B]` (D) `[A, C]`
4. What does `set(1, "Sue")` do to `[Fred, Alice]`? (A) `[Fred, Sue, Alice]` (B) `[Fred, Sue]` (C) `[Sue, Alice]` (D) error
5. How do you get the number of elements in an `ArrayList` called `list`? (A) `list.length` (B) `list.length()` (C) `list.size()` (D) `list.count()`
6. In the slides' complete example, what is printed last? (A) `Contents of al: [A, B]` (B) `Contents of al: [A]` (C) `Contents of al: [B]` (D) `Contents of al: []`
7. `[Fred, Sue]` → `remove("Fred")` → `remove(1)`. What happens? (A) the list is empty (B) Sue is removed (C) `IndexOutOfBoundsException` (D) compile error
8. What does `System.out.println(list)` print for an `ArrayList` holding A and B? (A) `[A, B]` (B) something like `java.util.ArrayList@1b6d` (C) `AB` (D) a compile error
9. Which loop is shortest when you only need to read each element? (A) `while` (B) regular `for` (C) for-each (D) `do...while`
10. `ArrayList<Integer> n` holds `[10, 25, 7]`. What does `n.remove(Integer.valueOf(7))` leave? (A) `[10, 25]` (B) `[10, 25, 7]` (C) an exception (D) `[25, 7]`
11. What does `list[0]` give for an `ArrayList`? (A) the first element (B) `error: array required, but ArrayList<String> found` (C) `null` (D) a runtime exception
12. Why does the plural-removal loop use `i--` after `remove(i)`? (A) to stop the loop (B) because the next element moved into position `i` (C) because `remove` returns `i` (D) to avoid a compile error
13. Which is a reason the slides give for **not** always using `ArrayList`? (A) it cannot grow (B) it is less efficient than an array (C) it cannot hold Strings (D) it has no `size` method
14. `Integer c = 128, d = 128;` What is `c == d`? (A) `true` (B) `false` (C) compile error (D) exception
15. What does `isEmpty()` return for a list after all its elements are removed? (A) `false` (B) `true` (C) 0 (D) `null`

### Answers

| Q | Answer | Why |
| --- | --- | --- |
| 1 | B | The memory is fixed when the array is created |
| 2 | B | Base type must be the wrapper `Integer` (A gives `unexpected type`) |
| 3 | B | `add(1, "C")` inserts at index 1 and pushes B up |
| 4 | B | `set` replaces (verified) |
| 5 | C | |
| 6 | B | Verified |
| 7 | C | Sue moved to index 0; the list has length 1 (verified) |
| 8 | A | `ArrayList` prints its contents |
| 9 | C | |
| 10 | A | Removes the value 7 (verified) |
| 11 | B | Verified |
| 12 | B | |
| 13 | B | |
| 14 | B | Different `Integer` objects (verified); use `.equals` |
| 15 | B | Verified |

**Score:** 13–15 go to Lab 12; 10–12 re-read the sections for the ones you missed; under 10, run the Operations program and draw the list after every line.

## 10. Quick reference

```java
import java.util.ArrayList;

ArrayList<String> names = new ArrayList<String>();
ArrayList<Integer> nums = new ArrayList<Integer>();

names.add("Fred");            // append
names.add(0, "Alice");        // insert at index 0
names.set(1, "Sue");          // replace index 1
String s = names.get(0);      // read index 0
boolean has = names.contains("Sue");
int where = names.indexOf("Sue");   // -1 if absent
names.remove("Sue");          // by value
names.remove(0);              // by index
int n = names.size();
boolean none = names.isEmpty();

for (int i = 0; i < names.size(); i++) { names.get(i); }
for (String name : names) { }               // read-only traversal
nums.remove(Integer.valueOf(7));             // remove the VALUE 7
```

## 11. Glossary

| Term | Meaning |
| --- | --- |
| Static data structure | A structure whose size is fixed when created (an array) |
| Dynamic data structure | A structure that grows and shrinks as needed |
| `ArrayList` | Java's resizable list collection, in `java.util` |
| Base type | The element type in angle brackets, e.g. `<String>` |
| Wrapper class | Object version of a primitive: `Integer`, `Double`, `Boolean`, `Character` |
| Autoboxing / unboxing | Automatic conversion between a primitive and its wrapper |
| `import` | Makes a class from another package available by its short name |
| For-each loop | `for (Type x : collection)`: visits each element without an index |
| `toArray` | Copies an `ArrayList`'s elements into an array |

## 12. Summary

- Use fixed-size arrays when the number of elements is known and won't change; use a variable-size `ArrayList` when it is unknown or changes.
- Import `java.util.ArrayList`; the base type must be an object type, so use `Integer`, `Double` and so on for primitives.
- Work with an `ArrayList` through methods: `add`, `set`, `get`, `contains`, `remove`, `size`, `isEmpty`.
- Positions shift after an insertion or removal, so trace carefully.
- Iterate with a regular `for` loop, a for-each loop or a `while` loop.

**Next:** work through Lab 12. Lecture 13 looks closely at the `String` and `char` types.
