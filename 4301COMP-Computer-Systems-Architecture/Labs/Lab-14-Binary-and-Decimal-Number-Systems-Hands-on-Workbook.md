# Lab 14 — Binary and Decimal Number Systems Hands-on Workbook (20 Tasks)

**Module:** 4301COMP Computer Systems Architecture

**Session:** Teaching Week 08, Session B · **Matching lecture:** `../Lectures/Lecture-14-Binary-and-Decimal-Number-Systems.md`

---

## How to use this lab

**What this lab is for.** You will practise every conversion method from the slides until it is automatic, check your answers in two ways, and use binary where it really appears in computing and security:

- bit flags;
- IPv4 addresses and masks;
- file permissions.

**Where the official tasks are.**

| Official lab sheet (TW08 Session B) | This workbook |
| --- | --- |
| Task 1 — Convert decimal values to binary | Task 16 |
| Task 2 — Convert binary values to decimal | Task 17 |
| Extra Challenge — Use binary flags | Task 18 |

In the timetabled lab, **do Tasks 16–18 first**. All values in the official activity are **unsigned** (official sheet).

**Tools**

| Tool | Used in | Notes |
| --- | --- | --- |
| Pen and paper | Tasks 1–10 | Do the working by hand first |
| Microsoft Word, Snipping Tool | Tasks 16–18 | `TW08B_YourStudentID.docx`, as on the official sheet |
| Windows Calculator (Programmer mode) | Task 15 | Already installed on Windows |
| Python 3 | Tasks 11–14 | **Optional, your choice.** Built-in modules only |

**Rules:**

- Show your working.
- Keep **leading zeros** in fixed-width answers.
- **Check** every answer with a second method (slide 30).

**Labels:**

- **Verified** = run before being written here (Python 3.13 and Linux).
- **Expected** = not run here (Word, Snipping Tool, Windows Calculator).

---

## Part A — Warm-up (Tasks 1–5)

### Task 1 — Place values

**Goal:** apply slide 11's formula: position k has weight Nᵏ.

1. Write the weights of positions 0–7 in **binary**.
2. Write the weights of positions 0–4 in **decimal**.
3. In 6,205₁₀, what does the digit 2 contribute? Write 6,205 in the form d × 10ᵏ + ….
4. In 1010₂, what does the leftmost 1 contribute?
5. In base 5 (digits 0–4), what is the weight of position 2? What is 132₅ in decimal?

**Expected result:** binary weights 1, 2, 4, …, 128; 2 contributes 200; the leftmost 1 contributes 8; 25; 132₅ = 42 (Verified).

- **Hint 1:** Positions count from **0** on the right.
- **Hint 2:** 132₅ = 1 × 25 + 3 × 5 + 2 × 1.

---

### Task 2 — Count in binary

**Goal:** see the counting pattern (slide 18).

Fill the gaps (5 bits):

| Decimal | 0 | 1 | 2 | 3 | 4 | | 7 | 8 | | 15 | 16 | | 31 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Binary | 00000 | 00001 | | | | 00110 | | | 01100 | | | 10001 | |

Then answer:

1. Which bit changes on every count?
2. What happens when you add 1 to 01111?
3. Why does 10₁₀ need four binary digits?

**Expected result:** 31 = 11111; 01111 + 1 = 10000 (the carry ripples left).

- **Hint 1:** The rightmost bit alternates 0, 1, 0, 1.
- **Hint 2:** 10 = 8 + 2, and 8 needs the fourth position.

---

### Task 3 — How big can it get?

**Goal:** use 2ⁿ patterns and the range 0 to 2ⁿ − 1.

| Bits | Patterns | Largest unsigned value | Real example |
| --- | --- | --- | --- |
| 1 | | | A single flag |
| 4 | | | A hex digit |
| 8 | | | An IPv4 octet |
| 10 | | | |
| 12 | | | A VLAN ID field |
| 16 | | | A port number |
| 24 | | | |

**Expected result:** 2/1, 16/15, 256/255, 1024/1023, 4096/4095, 65536/65535, 16777216/16777215 (Verified).

- **Hint 1:** Each extra bit doubles the number of patterns.
- **Hint 2:** All bits set = 2ⁿ − 1 (slide 16).

---

### Task 4 — Sanity checks

**Goal:** spot impossible answers without converting.

Each line is a student's answer. Without full working, say whether it **must be wrong** and why.

1. 57 → 111000
2. 200 → 011001000 (8-bit answer requested)
3. 10010110 → 151
4. 300 → an 8-bit value
5. 00001101 → 13
6. 11111111 → 256

**Expected result:** lines 1, 2, 3, 4 and 6 are wrong; line 5 is right.

- **Hint 1:** Odd numbers end in 1.
- **Hint 2:** 8 bits hold at most 255.

---

### Task 5 — Which base?

**Goal:** read base subscripts carefully (slide 17).

Give the decimal value of each:

| Written | Decimal value |
| --- | --- |
| 10₂ | |
| 10₁₀ | |
| 101₂ | |
| 101₁₀ | |
| 1000₂ | |
| 11₂ + 11₁₀ | |

**Expected result:** 2, 10, 5, 101, 8, 14.

- **Hint 1:** The digits alone do not tell you the value; the base does.
- **Hint 2:** 11₂ = 3.

---

## Part B — Find and fix (Tasks 6–10)

### Task 6 — Fix the division working

**Goal:** find errors in repeated division (slides 19–21).

Sam Archer converted 85:

```text
85 ÷ 2 = 42 r 1
42 ÷ 2 = 21 r 0
21 ÷ 2 = 10 r 1
10 ÷ 2 = 5  r 0
5  ÷ 2 = 2  r 1
2  ÷ 2 = 1  r 0
Answer (reading top to bottom): 101010
```

Find **two** mistakes and give the correct 8-bit answer.

**Expected result:** 85 = 01010101 (Verified).

- **Hint 1:** When does the method stop (slide 19)?
- **Hint 2:** Which direction do you read the remainders?

---

### Task 7 — Fix the positional working

**Goal:** correct place-value errors.

Sam converted 10011 like this:

```text
Weight: 128 64 32 16 8
Bit:      1  0  0  1 1
Answer: 128 + 16 + 8 = 152
```

Sam also wrote: "the rightmost bit is position 1, so its weight is 2."

1. What went wrong with the alignment?
2. Correct the statement about the rightmost bit.
3. Give the right answer.

**Expected result:** 10011₂ = 19 (slide 24).

- **Hint 1:** Line the bits up from the **right**.
- **Hint 2:** Pad to 8 bits first: 00010011.

---

### Task 8 — Fix the doubling working

**Goal:** correct doubling-method errors (slides 27–30).

Sam converted 1101 two ways:

```text
Attempt A (right to left):  1 → 1;  0 → 2;  1 → 5;  1 → 11   answer 11
Attempt B (adds then doubles): (0+1)×2=2; (2+1)×2=6; (6+0)×2=12; (12+1)×2=26   answer 26
```

Explain each mistake and do it correctly.

**Expected result:** 1101₂ = 13: 1 → 3 → 6 → 13 (Verified).

- **Hint 1:** Read left to right.
- **Hint 2:** Double first, then add.

---

### Task 9 — Fix the 8-bit answers

**Goal:** apply the official lab's fixed-width rule.

| Decimal | Sam's 8-bit answer | Problem? | Correct |
| --- | --- | --- | --- |
| 13 | 1101 | | |
| 42 | 00101010 | | |
| 128 | 1000000 | | |
| 255 | 011111111 | | |
| 256 | 100000000 | | |

**Expected result:** 13 → 00001101; 42 is correct; 128 → 10000000 (Sam's has only 7 digits); 255 → 11111111; 256 **cannot** be stored in 8 bits.

- **Hint 1:** Count the digits: exactly 8.
- **Hint 2:** Task 3's ranges.

---

### Task 10 — Fix the flag settings

**Goal:** apply the Extra Challenge's bit numbering.

Using the lab's flags:

| Bit | Weight | Flag |
| --- | --- | --- |
| 0 | 1 | power |
| 1 | 2 | alarm |
| 2 | 4 | network |
| 3 | 8 | sensor |

Bits 4–7 must be 0.

Sam wanted **power and sensor on**, everything else off, and wrote `10010000 = 144`.

1. What numbering mistake did Sam make?
2. What is the correct value?
3. A second student wrote `11111101` for "everything on except alarm". What is wrong?

**Expected result:** power + sensor = 00001001 = 9. The second answer sets unused bits 4–7 (it should be 00001101 = 13).

- **Hint 1:** Bit 0 is on the **right** (official sheet).
- **Hint 2:** Unused bits must remain 0.

---

## Part C — Build and apply (Tasks 11–15)

### Task 11 — A converter that shows its working

**Goal:** automate every method on the slides, with checks.

**Skill you gain:** you can turn a written algorithm into code and use it to check hand working. Writing a checker for your own work is a habit good engineers keep.

1. Save as `convert.py`:

```python
# convert.py - convert between decimal and binary, showing every step of working.
# The methods are exactly the ones on the TW08B slides and lab sheet:
#   decimal -> binary : repeated division by 2 (slides 19-21) and the subtraction method (lab Task 1)
#   binary -> decimal : positional method (slides 23-25) and doubling method (slides 27-30)
# Every answer is checked with Python's own int() and format() at the end.
#
# Usage: python convert.py 57              (decimal to binary)
#        python convert.py 101001101       (binary to decimal; any input made of only 0s and 1s
#                                           with 4 or more digits is treated as binary)
#        python convert.py 0b101            (force binary)

import sys


def repeated_division(n):
    print(f"Repeated division of {n} by 2 (slide 19):")
    print("  Division     Quotient  Remainder")
    remainders, q = [], n
    while True:
        new_q, r = divmod(q, 2)
        print(f"  {q:>5} ÷ 2   {new_q:>8}  {r:>9}")
        remainders.append(str(r))
        q = new_q
        if q == 0:
            break
    result = "".join(reversed(remainders))
    print(f"  Read the remainders from bottom to top: {n} = {result} (binary)")
    return result


def subtraction(n, bits=8):
    print(f"\nSubtraction method, {bits} bits (lab Task 1):")
    remainder, out = n, ""
    for k in range(bits - 1, -1, -1):
        w = 2 ** k
        if w <= remainder:
            print(f"  weight {w:>4}: {w} <= {remainder}, write 1, remainder {remainder} - {w} = {remainder - w}")
            remainder -= w
            out += "1"
        else:
            print(f"  weight {w:>4}: {w} >  {remainder}, write 0")
            out += "0"
    print(f"  Result: {out} (remainder {remainder})")
    return out


def positional(b):
    n = len(b)
    used = [(2 ** (n - 1 - i)) for i, bit in enumerate(b) if bit == "1"]
    print(f"Positional method for {b} (slides 23-25):")
    print("  Weight " + " ".join(f"{2 ** (n - 1 - i):>5}" for i in range(n)))
    print("  Bit    " + " ".join(f"{bit:>5}" for bit in b))
    total = sum(used)
    print(f"  {b} = {' + '.join(map(str, used)) or '0'} = {total}")
    return total


def doubling(b):
    print(f"\nDoubling method for {b} (slides 27-30): start at 0, total = total x 2 + bit")
    total = 0
    for bit in b:
        new = total * 2 + int(bit)
        print(f"  bit {bit}: {total} x 2 + {bit} = {new}")
        total = new
    print(f"  {b} = {total}")
    return total


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "57"
    is_binary = arg.startswith("0b") or (set(arg) <= {"0", "1"} and len(arg) >= 4)
    if is_binary:
        b = arg[2:] if arg.startswith("0b") else arg
        a, c = positional(b), doubling(b)
        print(f"\nCheck: both methods agree: {a == c};  Python int('{b}', 2) = {int(b, 2)}")
    else:
        n = int(arg)
        r = repeated_division(n)
        if n < 256:
            s = subtraction(n)
            print(f"\nCheck: padded to 8 bits {r.zfill(8)} == {s}: {r.zfill(8) == s};  Python: {format(n, '08b')}")
        else:
            print(f"\nCheck: Python format({n}, 'b') = {format(n, 'b')}")
```

2. Run `python convert.py 57` and `python convert.py 101001101`. *What it does:* prints the full working for each method and a final check. Actual output for 101001101 (Verified):

```text
Positional method for 101001101 (slides 23-25):
  Weight   256   128    64    32    16     8     4     2     1
  Bit        1     0     1     0     0     1     1     0     1
  101001101 = 256 + 64 + 8 + 4 + 1 = 333

Doubling method for 101001101 (slides 27-30): start at 0, total = total x 2 + bit
  bit 1: 0 x 2 + 1 = 1
  bit 0: 1 x 2 + 0 = 2
  bit 1: 2 x 2 + 1 = 5
  bit 0: 5 x 2 + 0 = 10
  bit 0: 10 x 2 + 0 = 20
  bit 1: 20 x 2 + 1 = 41
  bit 1: 41 x 2 + 1 = 83
  bit 0: 83 x 2 + 0 = 166
  bit 1: 166 x 2 + 1 = 333
  101001101 = 333

Check: both methods agree: True;  Python int('101001101', 2) = 333
```

3. Use it to check **your** answers to Tasks 6–9.
4. Convert the slide 26 long value: `python convert.py 110101110110111101010110101`.
5. **Extend:** add a function that prints the doubling method's working **as a table** (bit, calculation, new total), like slide 28.

**Expected result:** the long value is 112,949,941 (Verified).

- **Hint 1:** Inputs of 4 or more 0s and 1s are treated as binary; prefix `0b` to force it.
- **Hint 2:** For step 5, `print(f"{bit:>3}  {total} x 2 + {bit:<3} {new:>6}")`.

---

### Task 12 — Flags with bitwise operators

**Goal:** set, clear and test flags the way programs do.

**Skill you gain:** you can use AND, OR, XOR and NOT on bits. This is how device drivers, network protocols and permission systems read and change flags.

1. Save as `flags.py`:

```python
# flags.py - use the bits of one byte as on/off flags (the official Extra Challenge).
#   bit 0 (weight 1) = power, bit 1 (weight 2) = alarm, bit 2 (weight 4) = network, bit 3 (weight 8) = sensor
#   bits 4-7 are unused and must stay 0.
# A program tests, sets and clears flags with the bitwise operators & (AND), | (OR) and ~ (NOT).
#
# Usage: python flags.py

FLAGS = {"power": 0, "alarm": 1, "network": 2, "sensor": 3}      # name -> bit number


def show(value, title):
    print(f"{title}: {value:08b} = {value}")
    for name, bit in FLAGS.items():
        weight = 1 << bit                                       # 2 to the power bit
        state = "ON " if value & weight else "off"              # test: AND with the weight
        print(f"   bit {bit} (weight {weight}) {name:<8} {state}")
    assert value & 0b11110000 == 0, "bits 4-7 must stay 0"


def turn_on(value, name):
    return value | (1 << FLAGS[name])                           # OR sets one bit, leaves the rest


def turn_off(value, name):
    return value & ~(1 << FLAGS[name]) & 0xFF                    # AND with NOT clears one bit


if __name__ == "__main__":
    v = 0
    for name in ("power", "network", "sensor"):
        v = turn_on(v, name)
    show(v, "Before")
    after = turn_on(v, "alarm")
    show(after, "After ")
    changed = v ^ after                                         # XOR shows which bits differ
    print(f"Changed bits (XOR): {changed:08b} -> bit {changed.bit_length() - 1}")
    print(f"Turn the network off again: {turn_off(after, 'network'):08b} = {turn_off(after, 'network')}")
```

2. Run `python flags.py`. Actual output (Verified):

```text
Before: 00001101 = 13
   bit 0 (weight 1) power    ON 
   bit 1 (weight 2) alarm    off
   bit 2 (weight 4) network  ON 
   bit 3 (weight 8) sensor   ON 
After : 00001111 = 15
   bit 0 (weight 1) power    ON 
   bit 1 (weight 2) alarm    ON 
   bit 2 (weight 4) network  ON 
   bit 3 (weight 8) sensor   ON 
Changed bits (XOR): 00000010 -> bit 1
Turn the network off again: 00001011 = 11
```

3. Modify it to start with **only the alarm on**, then turn the power on. What is the value?
4. **Extend:** add a fifth flag, `door`, on bit 4, and update the unused-bit check to cover only bits 5–7.

**Expected result:** alarm + power = 00000011 = 3.

- **Hint 1:** `1 << 4` is 16.
- **Hint 2:** Bits 5–7 together are `0b11100000`.

---

### Task 13 — Binary inside IPv4 addresses

**Goal:** use this week's skills on Lecture 7's addressing.

**Skill you gain:** you can convert IPv4 addresses and masks to binary by hand. This is the key skill for subnetting and for reading firewall rules.

1. Convert each octet of **192.168.1.130** to 8-bit binary.
2. Convert the mask **255.255.255.192** to binary. How many 1s are there? That number is the prefix (/n).
3. AND the last octets (130 AND 192) bit by bit. What is the network address?
4. Convert 10, 172, 16, 31, 224 and 248 to binary.
5. On **your own computer**, run `ipconfig` (Expected). Convert your own IPv4 address's **last octet** and your mask to binary.

**Expected result (Verified):**

```text
192.168.1.130   = 11000000.10101000.00000001.10000010
255.255.255.192 = 11111111.11111111.11111111.11000000   (26 ones -> /26)
network         = 192.168.1.128
```

- **Hint 1:** 130 = 128 + 2.
- **Hint 2:** AND gives 1 only where **both** bits are 1.

---

### Task 14 — Read file permissions as binary

**Goal:** apply binary to a real security control.

**Skill you gain:** you can read and set Unix permission modes. Auditors check these on servers, and attackers look for weak ones.

Each permission digit is 3 bits: read = 4, write = 2, execute = 1.

1. Complete the table:

   | Mode | Owner bits | Group bits | Others bits | `ls -l` style |
   | --- | --- | --- | --- | --- |
   | 754 | 111 | 101 | 100 | rwxr-xr-- |
   | 644 | | | | |
   | 600 | | | | |
   | 750 | | | | |
   | 777 | | | | |

2. Which mode would you never want on a password file, and why?
3. Optional, on Linux or WSL: `touch test.txt`, then `chmod 640 test.txt`, then `stat -c '%a %A' test.txt`. *What it does:* creates an empty file, sets its permissions, and prints them as a number and as letters.

**Expected result (Verified on Linux):**

```text
754 -rwxr-xr--
644 -rw-r--r--
600 -rw-------
750 -rwxr-x---
777 -rwxrwxrwx
```

- **Hint 1:** 6 = 4 + 2 = read + write.
- **Hint 2:** 7 for "others" means anyone can change the file.

---

### Task 15 — Check with Windows Calculator (Programmer mode)

**Goal:** use a standard tool to verify conversions and see bit positions.

**Skill you gain:** you can use Programmer mode to check binary, decimal and hex quickly. Analysts and developers use it every day.

On your own Windows computer (Expected):

1. Open **Calculator** > menu (☰) > **Programmer**.
2. Select **DEC**, type `207`. Read the **BIN** line. Does it match slide 21?
3. Select **BIN**, type `101001101`. Read the **DEC** line.
4. Click the **bit-toggling keypad** (the icon with dots). Click bits to make `00001101` and watch DEC. Click bit 1 to switch the alarm on.
5. Note the **HEX** line for each value. You will need it next session.

**Expected result:** 207 = 1100 1111; 101001101 = 333; 13 → 15 when bit 1 is set; hex CF, 14D, D, F.

- **Hint 1:** Calculator groups binary digits in fours, which matches nibbles (slide 9).
- **Hint 2:** Set the word size to **BYTE** to see exactly 8 bits.

---

## Part D — Official tasks and integration (Tasks 16–20)

### Task 16 — Convert decimal values to binary (Official Task 1)

**Goal:** complete the official decimal-to-binary table.

**Official steps**

1. **1.1:** Open **Word > Blank document** and save **TW08B_YourStudentID.docx**. Choose **Insert > Table > Insert Table** with **10 columns** and **6 rows**, headed **Decimal, 128, 64, 32, 16, 8, 4, 2, 1, Check**. Put one decimal value in each remaining row. Use **Layout > Orientation > Landscape** only if you need more width. All values are **unsigned**.
2. **1.2:** Convert **13, 42, 85, 128 and 200** to eight-bit binary:
   - Start with the original value as a remainder.
   - Scan the weights from **128 down to 1**.
   - If a weight is no larger than the remainder, write **1** and subtract it; otherwise write **0**.
   - Finish with remainder zero.

   Example, separate from the exercises: **18 = 16 + 2**, so 18 = **00010010**.
3. **1.3:** For each place value, enter **1** when it is used and **0** when not, including leading zeros.
4. **1.4:** In **Check**, add the weights marked 1 and confirm the original value. For **one** row, also use the **repeated-division** method: divide by 2, record the quotient and remainder, repeat until zero, read the remainders bottom to top, and pad on the left to eight bits.
5. **1.5:** Use **Snipping Tool** to capture the completed table and paste it below your working.

| Decimal | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 | Check |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 13 | | | | | | | | | |
| 42 | | | | | | | | | |
| 85 | | | | | | | | | |
| 128 | | | | | | | | | |
| 200 | | | | | | | | | |

- **Hint 1:** 42 = 32 + 8 + 2.
- **Hint 2:** Task 11's script prints both methods for any value.

---

### Task 17 — Convert binary values to decimal (Official Task 2)

**Goal:** complete the official binary-to-decimal table.

**Official steps**

1. **2.1:** Create a second table with the same eight weights plus **Binary** and **Decimal** columns. Convert **00010110, 00111100, 01010001, 10100000 and 11111111** by hand. Keep leading zeros and align each bit with its weight.
2. **2.2:** Write the place values **128, 64, 32, 16, 8, 4, 2 and 1** above the bits and select only the values whose bit is **1**.
3. **2.3:** Add the selected place values and record each decimal result.
4. **2.4:** For **two** values, reverse-check by converting the decimal answer back to eight-bit binary using the place values.
5. **2.5:** Use **Snipping Tool** to capture the completed working and the two reverse checks.

| Binary | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 | Decimal |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 00010110 | | | | | | | | | |
| 00111100 | | | | | | | | | |
| 01010001 | | | | | | | | | |
| 10100000 | | | | | | | | | |
| 11111111 | | | | | | | | | |

- **Hint 1:** 11111111 is the largest 8-bit value (Task 3).
- **Hint 2:** Try the doubling method as a third check.

---

### Task 18 — Use binary flags (Official Extra Challenge)

**Goal:** encode device states as bits.

**Official steps**

1. **E.1:** Bit positions count from right to left:
   - **bit 0** (weight 1) = **power**;
   - **bit 1** (weight 2) = **alarm**;
   - **bit 2** (weight 4) = **network**;
   - **bit 3** (weight 8) = **sensor**.

   **Bits 4–7** are unused and must remain **0**. Set an active flag to **1** and an inactive flag to **0**.
2. **E.2:** Write the eight-bit binary value and its decimal value when **power, network and sensor** are on but **alarm** is off.
3. **E.3:** Change the value so that the **alarm is also on**, and identify the bit that changed.
4. **E.4:** Check both values by hand using the bit positions and powers of two, then capture the completed flag table.

| Flag | Bit / weight | Before | After |
| --- | --- | --- | --- |
| power | 0 / 1 | | |
| alarm | 1 / 2 | | |
| network | 2 / 4 | | |
| sensor | 3 / 8 | | |
| bits 4–7 | 16–128 | | |
| **Value** | | | |

- **Hint 1:** Add the weights of the flags that are on.
- **Hint 2:** Task 12's script shows the result and which bit changed.

---

### Task 19 — Mini-project: design a status byte for a network device

**Goal:** design and document your own 8-bit flag format, then use it.

**Skill you gain:** you can design a compact binary format and its documentation, the way protocol and firmware designers do.

**Brief.** A small office Wi-Fi access point reports its status in **one byte**. Design the format for at least **six** flags, chosen from:

- link up;
- DHCP lease obtained;
- WPA3 enabled;
- guest network on;
- firmware update available;
- error;
- overheating;
- client limit reached.

Steps:

1. **Specification table:** bit number, weight, flag name, meaning of 1 and meaning of 0. State which bits are unused and that they must be 0.
2. **Five test cases:** a description such as "link up, WPA3 on, error" → binary → decimal. Include all-off (0) and all-defined-on.
3. **Decode:** give your table to a partner along with three decimal values, for example 37, 129 and 6, and ask them to decode which flags are on. If you are working alone, decode them yourself the next day.
4. **Code:** adapt `flags.py` to your format and check all your test cases. Record actual outputs.
5. **Reflection (100 words):** why is it essential to document the **bit numbering direction** and the **unused bits**?

**Test plan**

| # | Description | Binary | Decimal | Script output matches? |
| --- | --- | --- | --- | --- |
| 1 | All off | 00000000 | 0 | |
| 2 | | | | |

- **Hint 1:** Put the most important flags in the lowest bits, so they are easy to test.
- **Hint 2:** Task 10 shows what happens when numbering is not documented.

---

### Task 20 — Assessment-style practice: number systems

**This is practice only, not a real exam question.** The module exam is two hours with short-answer and essay-style questions (module guide). Marks are invented for planning.

**Rules:** 20 minutes, closed book, no calculator, write it yourself.

**(a)** Explain what is meant by a positional number system with base N. Use 4,582₁₀ as an example. *(3 marks)*

**(b)** Convert 173₁₀ to 8-bit binary using repeated division. Show every step. *(4 marks)*

**(c)** Convert 10110110₂ to decimal using **both** the positional and doubling methods. *(4 marks)*

**(d)** A device's status byte uses bit 0 = power, bit 1 = alarm, bit 2 = network and bit 3 = sensor. The byte reads 00001011. State which flags are on, explain how a program could test the alarm flag, and explain why the bit numbering must be stated. *(5 marks)*

**(e)** State the largest unsigned value that fits in 8, 16 and 32 bits, and explain why it is 2ⁿ − 1. *(4 marks)*

**Self-marking checklist**

| Part | A good answer includes | Expected | Actual |
| --- | --- | --- | --- |
| (a) | Digits 0 to N − 1; weight Nᵏ from position 0 on the right; 4 × 10³ + 5 × 10² + 8 × 10¹ + 2 × 10⁰ | 3 points | |
| (b) | 8 divisions, remainders read bottom to top: **10101101** | 4 points | |
| (c) | 128 + 32 + 16 + 4 + 2 = **182**; doubling 1, 2, 5, 11, 22, 45, 91, 182 | 4 points | |
| (d) | Power, alarm and sensor on (1 + 2 + 8 = 11); AND with 2 ≠ 0 means on; numbering prevents misreading | 5 points | |
| (e) | 255, 65,535, 4,294,967,295; all ones = one less than the next weight | 4 points | |
| Time | Within 20 minutes | Yes | |

- **Hint 1:** Check (b) and (c) with `convert.py` afterwards.
- **Hint 2:** Lecture sections 7, 11, 13, 14 and 16.

---

## Tracker

| Task | Name | Done | Notes / score |
| --- | --- | --- | --- |
| 1 | Place values | ☐ | /5 |
| 2 | Count in binary | ☐ | |
| 3 | How big can it get? | ☐ | /7 |
| 4 | Sanity checks | ☐ | /6 |
| 5 | Which base? | ☐ | /6 |
| 6 | Fix the division | ☐ | /2 |
| 7 | Fix the positional working | ☐ | /3 |
| 8 | Fix the doubling | ☐ | /2 |
| 9 | Fix the 8-bit answers | ☐ | /5 |
| 10 | Fix the flags | ☐ | /3 |
| 11 | `convert.py` | ☐ | |
| 12 | `flags.py` | ☐ | |
| 13 | Binary in IPv4 | ☐ | |
| 14 | Permissions | ☐ | |
| 15 | Calculator Programmer mode | ☐ | |
| 16 | **Official Task 1**: Decimal → binary | ☐ | /5 |
| 17 | **Official Task 2**: Binary → decimal | ☐ | /5 |
| 18 | **Official Extra Challenge**: Flags | ☐ | |
| 19 | Mini-project: status byte | ☐ | |
| 20 | Assessment-style practice | ☐ | /20 |

## Reflection

1. Which conversion method do you find fastest, and which do you trust most? Why?
2. What mistake did you make most often, and what check caught it?
3. Where else in this module have you already met binary without converting it (addresses, masks, flags)?
4. How confident are you converting without a calculator? Rate yourself 1–5 and plan one practice session.

---

## Answer key

**(Verified)** = Python 3.13 and Linux. **(Expected)** = Word, Snipping Tool, Windows Calculator.

### Task 1 (Verified)

1. Binary weights for positions 0–7: 1, 2, 4, 8, 16, 32, 64, 128.
2. Decimal weights for positions 0–4: 1, 10, 100, 1,000, 10,000.
3. The digit 2 contributes **200**. 6,205 = 6 × 10³ + 2 × 10² + 0 × 10¹ + 5 × 10⁰.
4. The leftmost 1 contributes **8**.
5. The weight of position 2 in base 5 is 5² = **25**. 132₅ = 25 + 15 + 2 = **42**.

### Task 2

**Missing binary values:** 2 = 00010, 3 = 00011, 4 = 00100, 7 = 00111, 8 = 01000, 15 = 01111, 16 = 10000, 31 = 11111.

**Missing decimal values:** 00110 = 6, 01100 = 12, 10001 = 17.

1. The rightmost bit (bit 0) changes on every count.
2. 01111 + 1 = **10000**: the carry ripples left.
3. Because 10 ≥ 8 = 2³, it needs position 3.

### Task 3 (Verified)

| Bits | Patterns | Largest value |
| --- | --- | --- |
| 1 | 2 | 1 |
| 4 | 16 | 15 |
| 8 | 256 | 255 |
| 10 | 1,024 | 1,023 |
| 12 | 4,096 | 4,095 |
| 16 | 65,536 | 65,535 |
| 24 | 16,777,216 | 16,777,215 |

### Task 4

1. **Wrong:** 57 is odd, so the answer must end in 1 (the correct answer is 111001).
2. **Wrong:** 9 digits for an 8-bit answer (the correct answer is 11001000).
3. **Wrong:** the number ends in 0, so it is even, but 151 is odd (10010110 = 150).
4. **Wrong:** 300 > 255.
5. **Right.**
6. **Wrong:** 255 is the maximum.

### Task 5

2, 10, 5, 101, 8, and 3 + 11 = 14.

### Task 6 (Verified)

1. Sam stopped at quotient 1. One more division is needed: 1 ÷ 2 = 0 r 1.
2. Sam read the remainders top to bottom.

The remainders are 1, 0, 1, 0, 1, 0, 1. Read bottom to top: 1010101, which padded to 8 bits is **01010101** (85).

### Task 7

1. The bits were aligned from the left under 128, so each bit got the wrong weight.
2. The rightmost bit is **position 0**, with weight **1**.
3. Correctly aligned: 16 + 2 + 1 = **19**.

### Task 8 (Verified)

- **Attempt A** read right to left. Because 1101 reversed is 1011, it gave 11.
- **Attempt B** added before doubling, which gives twice the right answer (26 = 2 × 13).

**Correct:** 0 × 2 + 1 = 1; 1 × 2 + 1 = 3; 3 × 2 + 0 = 6; 6 × 2 + 1 = **13**.

### Task 9 (Verified)

| Decimal | Correct 8-bit answer |
| --- | --- |
| 13 | 00001101 |
| 42 | 00101010 (Sam was correct) |
| 128 | 10000000 (Sam's answer had only 7 digits) |
| 255 | 11111111 (Sam's had 9 digits) |
| 256 | Does not fit in 8 bits |

### Task 10 (Verified)

1. Sam numbered the bits from the left.
2. Power (1) + sensor (8) = **00001001 = 9**.
3. The second student set the unused bits 4–7. The correct value is **00001101 = 13**.

### Task 11 (Verified)

The outputs are as shown. The slide 26 value is **112,949,941**.

### Task 12 (Verified)

Step 3: **00000011 = 3**. Step 4 model:

```python
FLAGS = {"power": 0, "alarm": 1, "network": 2, "sensor": 3, "door": 4}
# ...
    assert value & 0b11100000 == 0, "bits 5-7 must stay 0"
```

### Task 13 (Verified)

- Steps 1–3: as shown. The mask has **26** ones, so /26, and the network is **192.168.1.128**.
- Step 4:

| Decimal | Binary |
| --- | --- |
| 10 | 00001010 |
| 172 | 10101100 |
| 16 | 00010000 |
| 31 | 00011111 |
| 224 | 11100000 |
| 248 | 11111000 |

### Task 14 (Verified)

| Mode | Owner | Group | Others | Letters |
| --- | --- | --- | --- | --- |
| 644 | 110 | 100 | 100 | rw-r--r-- |
| 600 | 110 | 000 | 000 | rw------- |
| 750 | 111 | 101 | 000 | rwxr-x--- |
| 777 | 111 | 111 | 111 | rwxrwxrwx |

**777** on a password file lets anyone read and change it. Such files should be 600 or stricter.

### Task 15 (Expected)

| Value | Result | Hex |
| --- | --- | --- |
| 207 | BIN 1100 1111 | CF |
| 101001101₂ | DEC 333 | 14D |
| 13, then bit 1 set | 13 → 15 | D → F |

### Task 16 (Verified)

| Decimal | 8-bit binary | Check |
| --- | --- | --- |
| 13 | 00001101 | 8 + 4 + 1 |
| 42 | 00101010 | 32 + 8 + 2 |
| 85 | 01010101 | 64 + 16 + 4 + 1 |
| 128 | 10000000 | 128 |
| 200 | 11001000 | 128 + 64 + 8 |

### Task 17 (Verified)

| Binary | Decimal | Working |
| --- | --- | --- |
| 00010110 | **22** | 16 + 4 + 2 |
| 00111100 | **60** | 32 + 16 + 8 + 4 |
| 01010001 | **81** | 64 + 16 + 1 |
| 10100000 | **160** | 128 + 32 |
| 11111111 | **255** | All weights |

### Task 18 (Verified)

- **Before:** 00001101 = **13**.
- **After:** 00001111 = **15**.
- **Bit 1** (alarm, weight 2) changed.

### Tasks 19–20 (model points)

Use the self-marking checklist. In Task 19, 37 = 32 + 4 + 1, 129 = 128 + 1 and 6 = 4 + 2; decode these against your own table.
