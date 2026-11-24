# Lecture 15 — Hexadecimal and Data Representation

**Module:** 4301COMP Computer Systems Architecture

**Session:** Teaching Week 09, Session A

## Start here

Last session you learnt binary and decimal. Binary is exact but hard for people to read; decimal is easy to read but hides the bit pattern. **Hexadecimal** (base 16) sits between them. Every hex digit is exactly four bits, so long binary values become short and readable, and you can still see the bits.

This lecture covers:

- why hex exists;
- its digits and place values;
- binary ↔ hex by **nibbles**;
- decimal ↔ hex by **repeated division by 16** and **powers of 16**;
- where hex appears in real systems: addresses, machine code, MAC and IPv6 addresses, colours and **file bytes in a hex editor**.

After reading, do **Lab 15** (`../Labs/Lab-15-Hexadecimal-and-Data-Representation-Hands-on-Workbook.md`). It contains the official conversion tables, mixed practice and the colour challenge.

**Labels used in these notes:**

| Label | Meaning |
| --- | --- |
| **Official** | From the TW09 Session A slides or lab sheet. |
| **Extra** | Added explanation, not on the slides. |
| **Verified** | Actually run before being written down: every conversion checked with Python 3.13 (`hexconvert.py`, written for this lecture, plus `int()` and `format()`). Real file bytes were read with `hexview.py` (written for this lecture) and cross-checked with Linux `od` and `file`. |
| **Expected** | Not run here (Windows tools, HxD). |

> **Note on the slides.** All slides were readable as text. Slide 14's tip (8-4-2-1 columns per nibble) is shown as a table in section 8.

---

## 1. Overview

| Representation | Example (the same value) | Good for |
| --- | --- | --- |
| Binary | 1100 1111 | What the hardware actually stores |
| Decimal | 207 | Everyday arithmetic |
| Hexadecimal | CF | Reading and writing bit patterns compactly |

Two hex digits are one byte, so a 32-bit address goes from 32 binary digits to **8 hex digits**. That is why debuggers, network tools, hex editors and security tools show data in hex.

**Why this matters for cyber security.** Analysts read hex all the time:

- **Packet captures** show raw bytes in hex.
- **Malware analysis** starts with a **hex dump** of a file.
- **File signatures** ("magic numbers") in the first few bytes reveal a file's **real** type, whatever its name says.
- **Memory addresses**, **MAC addresses** and **IPv6 addresses** are all written in hex.

## 2. By the end you should be able to

1. Explain why hexadecimal is a compact representation of binary.
2. List the 16 hex digits and their decimal and 4-bit binary values.
3. Convert binary → hex by grouping bits into nibbles, and hex → binary by expanding each digit to 4 bits.
4. Convert decimal → hex by repeated division by 16.
5. Convert hex → decimal by powers of 16, or via binary.
6. Check each conversion with a reverse conversion.
7. Read hex in real contexts: memory addresses, machine code, MAC addresses, colours.
8. Read a **hex dump** and identify a file's type from its signature bytes.

## 3. Learning outcomes

**Session learning outcomes (Official, slide 3):**

- Explain why hexadecimal is a compact representation of binary.
- Convert between binary and hexadecimal.
- Convert between decimal and hexadecimal.
- Identify practical uses of hexadecimal representation.

**Module learning outcomes supported** (module guide, as recorded in this module's project instructions):

| Module LO | How this lecture supports it |
| --- | --- |
| **LO1** Explain the fundamental principles underlying the operation of modern computer systems | How data is represented and displayed |
| **LO2** Demonstrate knowledge of the structure and organisation of computer systems | Addresses, bytes, machine code, file structure |

Relevant to the **exam (60%)** (module guide). The official lab says it practises the conversions used in **written assessments**.

## 4. Matching lab and what you need first

- **Matching lab:** Lab 15. It contains the official tasks:
  - binary ↔ hex, Task 16;
  - decimal ↔ hex, Task 17;
  - mixed practice and the colour challenge, Task 18.
- **The official lab says to work manually** and not to use an automatic online converter. The tools in Lab 15's Part C are for **checking afterwards** and for real-world practice.
- **From Lecture 14:** place values, repeated division, positional and doubling methods, nibbles and bytes.

---

## 5. Recap of the previous session (slide 4, Official)

- A number system is defined by its base and digit set.
- Binary uses powers of two; decimal uses powers of ten.
- Repeated division by two converts decimal values to binary.
- Weighted place values convert binary values back to decimal.

---

## 6. Why another number system? (slides 5–6)

### 6.1 Official

Humans find long binary numbers hard to read. A memory address in a 32-bit computer might look like:

```text
01010111000011110101000101111101
```

- Can you read this address easily?
- Could you memorise it?
- Does it give you any idea of the number?

Grouping the bits in **fours** and writing each group as one **hexadecimal** digit solves this. Hexadecimal means 16: it is the **base-16** system.

```text
0101 0111 0000 1111 0101 0001 0111 1101
  5    7    0    F    5    1    7    D      ->  570F517D (hex)
```

### 6.2 Why 16 and not 10? (Extra)

16 = 2⁴, so **one hex digit is exactly one 4-bit nibble**. Conversion is a simple lookup with no arithmetic across digits. Decimal does not line up with bits: 10 is not a power of 2, so you cannot read bits from decimal digits. The address above is 1,460,621,693 in decimal (Verified). That is accurate, but it tells you nothing about its bits.

---

## 7. The hexadecimal digits (slide 7, Official)

Hex is base 16. It uses the ten digits **0–9** and six letters **A–F**: A = 10, B = 11, C = 12, D = 13, E = 14 and F = 15. One hex digit corresponds to **four binary bits**.

| Decimal | Binary | Hex | | Decimal | Binary | Hex |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 0000 | 0 | | 8 | 1000 | 8 |
| 1 | 0001 | 1 | | 9 | 1001 | 9 |
| 2 | 0010 | 2 | | 10 | 1010 | **A** |
| 3 | 0011 | 3 | | 11 | 1011 | **B** |
| 4 | 0100 | 4 | | 12 | 1100 | **C** |
| 5 | 0101 | 5 | | 13 | 1101 | **D** |
| 6 | 0110 | 6 | | 14 | 1110 | **E** |
| 7 | 0111 | 7 | | 15 | 1111 | **F** |

The slide writes the binary column without leading zeros (10, 11, 100, …). When converting, always use **four** bits: 2 = **0010**.

**Ways of writing hex (Extra).** To make it clear that a number is hex, you may see:

- a subscript: CF₁₆;
- a prefix: `0xCF` in programming;
- a suffix: CFh;
- a hash: `#` in colours.

All of these mean the same value.

---

## 8. Binary ↔ hexadecimal (slides 6, 12–14)

### 8.1 Binary → hex

1. Starting from the **right**, split the bits into groups of 4. Pad the leftmost group with zeros if needed.
2. Convert each group with the **8-4-2-1** weights (slide 14's tip).
3. Write the digits in the same order.

**Official lab example:** 1101 0010₂ → 1101 = 8 + 4 + 1 = 13 = **D**, and 0010 = 2 → **D2₁₆**.

**Worked example (Verified):** 10110101₂

```text
Binary 10110101 -> hexadecimal by nibbles (8-4-2-1):
  1011 = 11 = B
  0101 =  5 = 5
  Result: B5
```

### 8.2 Hex → binary

Replace each hex digit with its **4-bit** pattern, keeping leading zeros.

**Official examples:**

- **5E₁₆** = 0101 1110₂ (official lab).
- **A3₁₆** = 1010 0011₂ (slide 12).

**Slide 14's tip:** use 8 4 2 1 as the columns for each nibble.

| | 8 | 4 | 2 | 1 | | 8 | 4 | 2 | 1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bits | 1 | 0 | 1 | 0 | | 0 | 0 | 1 | 1 |
| Digit | | | **A** | | | | | **3** | |

> **Common confusion.** Writing 3 as **11** instead of **0011** loses the leading zeros. A3 would then become 101011, which is a different number: 43 instead of 163. Every hex digit is **exactly** four bits.

---

## 9. Decimal → hexadecimal: repeated division by 16 (slides 8–10)

### 9.1 Official method

Use the same method as decimal → binary, but divide by **16** instead of 2:

1. Record each remainder.
2. Write remainders **10–15 as A–F**.
3. Repeat until the quotient is 0.
4. Read the remainders from **bottom to top**.

**207₁₀ (slide 9):**

| Division | Quotient | Remainder |
| --- | --- | --- |
| 207 ÷ 16 | 12 | 15 = **F** |
| 12 ÷ 16 | 0 | 12 = **C** |

Bottom to top: **207₁₀ = CF₁₆**. This matches Lecture 14's 207 = 1100 1111₂, because 1100 = C and 1111 = F.

**1,234₁₀ (slide 10):**

| Division | Quotient | Remainder |
| --- | --- | --- |
| 1234 ÷ 16 | 77 | 2 |
| 77 ÷ 16 | 4 | 13 = **D** |
| 4 ÷ 16 | 0 | 4 |

Bottom to top: **1234₁₀ = 4D2₁₆**.

**Official lab example:** 190 ÷ 16 = 11 r 14 (E); 11 ÷ 16 = 0 r 11 (B). So **190₁₀ = BE₁₆**.

### 9.2 A three-digit example (Verified)

```text
Decimal 413 -> hexadecimal by repeated division by 16:
     413 ÷ 16 =    25 remainder 13 = D
      25 ÷ 16 =     1 remainder  9
       1 ÷ 16 =     0 remainder  1
  Read the remainders bottom to top: 413 = 19D (hex)

Hexadecimal 19D -> binary, 4 bits per digit:
  1 = 0001
  9 = 1001
  D = 1101
  Result: 0001 1001 1101
```

### 9.3 Dividing by 16 without a calculator (Extra)

Find the biggest multiple of 16 that fits, using 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224 and 240. For example, 413 ÷ 16: 16 × 25 = 400, so the quotient is 25 and the remainder 413 − 400 = 13 = D.

---

## 10. Hexadecimal → decimal (slides 11–17)

There are two methods (Official).

### 10.1 Via binary: two stages, often simpler (slides 11–13)

Convert hex → binary, then binary → decimal with the place values.

**A3₁₆** = 1010 0011₂:

| Weight | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Bit | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 1 |
| Value | 128 | 0 | 32 | 0 | 0 | 0 | 2 | 1 |

128 + 32 + 2 + 1 = **163**, so A3₁₆ = 163₁₀.

### 10.2 Positional with powers of 16: one stage (slides 15–17)

This is the "classical", one-stage approach. It uses bigger numbers in the working.

**A3₁₆:**

| Digit | A | 3 |
| --- | --- | --- |
| Weight | 16¹ = 16 | 16⁰ = 1 |
| Contribution | 10 × 16 = 160 | 3 × 1 = 3 |

A3₁₆ = 160 + 3 = **163₁₀**.

**2A1₁₆:**

| Digit | 2 | A | 1 |
| --- | --- | --- | --- |
| Weight | 16² = 256 | 16¹ = 16 | 16⁰ = 1 |
| Contribution | 2 × 256 = 512 | 10 × 16 = 160 | 1 × 1 = 1 |

2A1₁₆ = 512 + 160 + 1 = **673₁₀**.

**Official lab example:** 2C₁₆ = (2 × 16¹) + (12 × 16⁰) = **44₁₀**.

**Powers of 16 to know (Extra):**

| Power | 16⁰ | 16¹ | 16² | 16³ | 16⁴ |
| --- | --- | --- | --- | --- | --- |
| Value | 1 | 16 | 256 | 4,096 | 65,536 |

### 10.3 Three-digit example (Verified)

```text
Hexadecimal 1AF -> decimal with powers of 16:
  digit 1 (=  1) x 16^2 ( 256) = 256
  digit A (= 10) x 16^1 (  16) = 160
  digit F (= 15) x 16^0 (   1) = 15
  1AF = 256 + 160 + 15 = 431
```

### 10.4 Quick facts (Extra, Verified)

- 2 hex digits = 1 byte: 00 to FF, which is 0 to 255.
- 4 hex digits = 16 bits: 0000 to FFFF, which is 0 to 65,535.
- 8 hex digits = 32 bits: FFFFFFFF = 4,294,967,295.

---

## 11. Hexadecimal in computer systems (slide 18)

### 11.1 Official

Hexadecimal compactly represents binary values such as:

- memory addresses;
- machine code;
- MAC addresses;
- IPv6 addresses;
- file bytes.

**Web colours** use **#RRGGBB**: two hex digits for each 8-bit red, green and blue component.

| Colour | Hex | Red | Green | Blue |
| --- | --- | --- | --- | --- |
| Black | #000000 | 0 | 0 | 0 |
| White | #FFFFFF | 255 | 255 | 255 |
| Orange | #FF8000 | 255 | 128 | 0 |

### 11.2 Real examples (Extra, Verified where stated)

| Where | Example | Reading it |
| --- | --- | --- |
| **Memory address** | 0x570F517D (slide 5's address) | 8 hex digits = 32 bits |
| **Machine code** | `01 ca` = `add %ecx,%edx` (Lecture 12, Verified objdump) | Each byte of an instruction is two hex digits |
| **MAC address** | `02:fc:00:00:00:01` (the test machine, Verified with `ip link`) | 6 bytes = 48 bits (Lecture 4). The first byte 02 = 0000 0010: bit 1 is set, which marks a **locally administered** (not factory) address |
| **IPv6 address** | `fe80::1`, `::1` | 128 bits written as eight groups of 4 hex digits; `::` stands for a run of zero groups |
| **Colour** | #FF8000 | FF = 255, 80 = 128, 00 = 0 |
| **Port number** | 443 = 0x01BB | Seen in packet hex dumps as the bytes 01 BB |

---

## 12. Hexadecimal editors and file bytes (slide 2: "applications and hexadecimal editors")

**Extra, Verified.** A **hex editor or viewer** shows a file's raw bytes. Each line has three parts:

- the **offset** (position in the file) in hex;
- **16 bytes** as two-digit hex values;
- the same bytes as **text**, with `.` for unprintable bytes.

Free hex editors include **HxD** on Windows; on Linux, `xxd`, `od` and `hexdump` do the same job. Real output from `hexview.py` (Lab 15 Task 11):

```text
hello.txt: signature says no known signature (perhaps plain text)
00000000  48 65 6C 6C 6F 2C 20 34 33 30 31 43 4F 4D 50 21  |Hello, 4301COMP!|
00000010  0A                                               |.|

figure.png: signature says PNG image
00000000  89 50 4E 47 0D 0A 1A 0A 00 00 00 0D 49 48 44 52  |.PNG........IHDR|
00000010  00 00 04 92 00 00 02 22 08 06 00 00 00 93 F7 E2  |......."........|

notes.zip: signature says ZIP archive (also .docx/.xlsx/.pptx)
00000000  50 4B 03 04 14 00 00 00 00 00 CF 7E 78 5D C2 41  |PK.........~x].A|
00000010  24 35 03 00 00 00 03 00 00 00 05 00 00 00 61 2E  |$5............a.|

program: signature says ELF program (Linux)
00000000  7F 45 4C 46 02 01 01 00 00 00 00 00 00 00 00 00  |.ELF............|
00000010  03 00 3E 00 01 00 00 00 80 10 00 00 00 00 00 00  |..>.............|

fake.png: signature says no known signature (perhaps plain text)
00000000  48 65 6C 6C 6F 2C 20 34 33 30 31 43 4F 4D 50 21  |Hello, 4301COMP!|
00000010  0A                                               |.|
```

What the dumps show:

- **Text is just bytes.** `48 65 6C 6C 6F` is "Hello" in ASCII (H = 0x48 = 72). The final `0A` is the newline character. Linux `od` printed the same bytes (Verified).
- **File signatures ("magic numbers").** A PNG starts `89 50 4E 47` (".PNG"), a ZIP `50 4B 03 04` ("PK"), a Linux program `7F 45 4C 46` (".ELF"). Tools such as `file` identify type from these bytes, not from the name (Verified: `file` reported PNG, Zip and ELF).
- **Hex fields mean numbers.** In the PNG, the bytes `00 00 04 92` are the image width: 0x492 = **1,170** pixels. The bytes `00 00 02 22` are the height: 0x222 = **546**. `file` reported "1170 x 546" (Verified).

> **Cyber security link: the name lies, the bytes do not.** `fake.png` above is really plain text with a `.png` name. Its first bytes are `48 65 6C 6C 6F`, not `89 50 4E 47`. Attackers rename executables to look like documents. For example, a Windows program starts with `4D 5A` ("MZ"). Checking signatures in hex is a basic forensic and email-filtering technique. Also note that `.docx`, `.xlsx` and `.pptx` files are really **ZIP** archives: they start with `50 4B`.

---

## 13. Checking your answers (official lab)

The official lab asks for **reverse checks**:

- Hex → binary → hex must reproduce the original digits.
- Decimal → hex → decimal must reproduce the original number.
- Write the **base** beside every final answer: D2₁₆, not just D2.

Quick sanity checks (Extra):

| Check | Why it works |
| --- | --- |
| A 2-digit hex value is never more than 255 | FF = 255 |
| Last hex digit even ↔ value even | 16 is even, so only the last digit decides |
| 3 hex digits ≥ 256 if the first digit is not 0 | 16² = 256 |

---

## 14. Common mistakes

| Mistake | Example | Fix |
| --- | --- | --- |
| Grouping nibbles from the **left** with an uneven length | 110101111 → `1101 0111 1` | Group from the **right** and pad: `0001 1010 1111` = 1AF |
| Dropping leading zeros in nibbles | 3 → 11 | 3 → **0011** |
| Writing remainders as numbers | 207 → "1215" | 12 → C, 15 → F: **CF** |
| Reading remainders top to bottom | 1234 → 2D4 | Bottom to top: **4D2** |
| Treating A–F as letters, not values | "A × 16 = A0 = ?" | A = **10**, so 10 × 16 = 160 |
| Using powers of 10 for hex | 2A1 = 2 × 100 + … | Powers of **16**: 256, 16, 1 |
| No base on the answer | "D2" | **D2₁₆** |
| Thinking `#FF8000` has three values of 4 digits | | **Three bytes**: FF, 80, 00 |
| Trusting a file extension | `fake.png` | Check the signature bytes |

---

## 15. Check yourself: 15 multiple-choice questions

**Q1.** Why is hexadecimal useful in computing?
A) It is faster for the CPU
B) Each hex digit represents exactly four bits, so binary is shorter to read and write
C) It uses less memory
D) Computers store hex internally

**Q2.** What decimal value does the hex digit D have?
A) 12
B) 14
C) 13
D) 11

**Q3.** 1101 0010₂ in hex is:
A) D2
B) C2
C) 2D
D) D3

**Q4.** 5E₁₆ in binary is:
A) 0101 1101
B) 0101 1110
C) 0110 1110
D) 1011 1110

**Q5.** 207₁₀ in hex is:
A) FC
B) CE
C) CF
D) DF

**Q6.** Converting 1234 by repeated division by 16 gives the remainders 2, 13, 4 (first to last). The answer is:
A) 2D4
B) 4D2
C) 4132
D) D42

**Q7.** A3₁₆ in decimal is:
A) 163
B) 103
C) 173
D) 160

**Q8.** What is the weight of the leftmost digit in 2A1₁₆?
A) 100
B) 16
C) 16² = 256
D) 2

**Q9.** 2A1₁₆ in decimal is:
A) 673
B) 641
C) 289
D) 545

**Q10.** How many hex digits represent one byte?
A) 1
B) 4
C) 8
D) 2

**Q11.** In #FF8000, what is the green component in decimal?
A) 80
B) 128
C) 255
D) 0

**Q12.** 110101111₂ in hex is:
A) D7 with a 1 left over
B) 1AF
C) 35F
D) 6B1

**Q13.** A file named `photo.png` starts with the bytes 4D 5A. What should an analyst conclude?
A) It is a normal PNG
B) It is a text file
C) Its signature says it is a Windows executable, not an image
D) The file is empty

**Q14.** What is the largest value of a 2-digit hex number?
A) 99
B) 255
C) 256
D) 160

**Q15.** Which method converts hex → decimal in one stage (slide 15)?
A) Positional with powers of 16
B) Nibble grouping
C) Repeated division by 2
D) Doubling

### Answers

| Q | Answer | Why |
| --- | --- | --- |
| 1 | **B** | Slides 6–7. |
| 2 | **C** | Slide 7. |
| 3 | **A** | Official lab example. |
| 4 | **B** | Official lab example. |
| 5 | **C** | Slide 9. |
| 6 | **B** | Read bottom to top (slide 10). |
| 7 | **A** | Slides 12–16. |
| 8 | **C** | Slide 17. |
| 9 | **A** | Slide 17 (Verified). |
| 10 | **D** | Two nibbles. |
| 11 | **B** | 0x80 = 128 (slide 18). |
| 12 | **B** | Group from the right: 0001 1010 1111 (Verified). |
| 13 | **C** | `4D 5A` = "MZ" (section 12). |
| 14 | **B** | FF = 255. |
| 15 | **A** | Slide 15. |

---

## 16. Quick reference

**Digits:** 0–9 and A = 10, B = 11, C = 12, D = 13, E = 14, F = 15. One hex digit = 4 bits; two hex digits = 1 byte.

**Binary → hex:** group from the right in fours (pad with leading zeros), then use 8-4-2-1 on each nibble.

**Hex → binary:** write each digit as exactly 4 bits.

**Decimal → hex:** divide by 16, write remainders 10–15 as A–F, read bottom to top.

**Hex → decimal:** either Σ digit × 16ᵏ (powers 1, 16, 256, 4,096) or go via binary.

**Check:** reverse-convert, and write the base on every answer.

**Uses:**

| Use | Form |
| --- | --- |
| Addresses | 0x… |
| Machine code | Bytes |
| MAC address | 6 bytes, e.g. aa:bb:… |
| IPv6 | Groups of 4 hex digits |
| Colours | #RRGGBB |
| Hex dump | Offset, bytes, text |

**File signatures:**

| File type | First bytes |
| --- | --- |
| PNG | 89 50 4E 47 |
| ZIP / Office | 50 4B 03 04 |
| PDF | 25 50 44 46 |
| ELF | 7F 45 4C 46 |
| Windows program | 4D 5A |

## 17. Glossary

| Term | Meaning |
| --- | --- |
| **ASCII** | A code that gives each character a number, e.g. 'H' = 0x48 |
| **Byte** | 8 bits; two hex digits |
| **File signature (magic number)** | Fixed bytes at the start of a file that identify its type |
| **Hex dump** | A display of raw bytes in hex, with offsets and text |
| **Hex editor** | A program that shows and edits a file's raw bytes (e.g. HxD) |
| **Hexadecimal** | Base-16 number system: digits 0–9 and A–F |
| **Nibble** | 4 bits; one hex digit |
| **Offset** | The position of a byte from the start of a file, usually in hex |
| **0x prefix** | Programming notation meaning "this number is hex" |

## 18. Summary

- Hex is base 16. One hex digit is exactly one **nibble** (4 bits), so binary becomes four times shorter and still shows its bits.
- **Binary ↔ hex:** group in fours from the right, use 8-4-2-1, and keep leading zeros.
- **Decimal → hex:** divide by 16, with remainders 10–15 written as A–F, read bottom to top.
- **Hex → decimal:** use powers of 16, or go via binary.
- Always **reverse-check** and **label the base**.
- Hex is how people read **addresses, machine code, MAC and IPv6 addresses, colours and file bytes**. A hex dump shows what a file **really** is, which is a core forensic skill.

## 19. Next

According to slide 20, the next session is **Teaching Week 09, Session B: Memory and Storage**.
