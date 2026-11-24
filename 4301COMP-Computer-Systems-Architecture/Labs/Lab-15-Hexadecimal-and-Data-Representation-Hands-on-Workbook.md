# Lab 15 — Hexadecimal and Data Representation Hands-on Workbook (20 Tasks)

**Module:** 4301COMP Computer Systems Architecture

**Session:** Teaching Week 09, Session A · **Matching lecture:** `../Lectures/Lecture-15-Hexadecimal-and-Data-Representation.md`

---

## How to use this lab

**What this lab is for.** You will practise the hex conversions used in written assessments until they are reliable, and then use hex where it really appears: file bytes in a hex viewer, file signatures, colours, MAC and IPv6 addresses, and binary file fields.

**Where the official tasks are.**

| Official lab sheet (TW09 Session A) | This workbook |
| --- | --- |
| Task 1 — Convert between binary and hexadecimal | Task 16 |
| Task 2 — Convert between decimal and hexadecimal | Task 17 |
| Task 3 — Mixed conversion practice, plus the optional colour challenge | Task 18 |

In the timetabled lab, **do Tasks 16–18 first**. The official sheet suggests **60 minutes** and says:

- work **manually**, and show your method, not only the final answer;
- you may use the lecture slides, but **do not use an automatic online converter**;
- all values are non-negative integers, and binary values are unsigned.

The tools in **Part C** are for **checking afterwards** and for real-world practice. Use them only after you have done the official tasks by hand.

**Tools**

| Tool | Used in | Notes |
| --- | --- | --- |
| Pen and paper; Microsoft Word | Tasks 1–10, 16–18 | `TW09A_YourStudentID.docx` (official) |
| Python 3 | Tasks 11–12, 14 | **Optional, your choice.** Built-in modules only |
| PowerShell (normal user) | Task 13 | `Format-Hex` is built into Windows; read-only |
| A browser | Task 14 | To open a colour swatch file |

**Labels:**

- **Verified** = run before being written here (Python 3.13; Linux `od` and `file`).
- **Expected** = not run here (Windows PowerShell, Word).

---

## Part A — Warm-up (Tasks 1–5)

### Task 1 — The 16 digits

**Goal:** know slide 7's table without looking.

From memory, fill in the binary (4 bits) and decimal values, then check against slide 7.

| Hex | 0 | 3 | 5 | 7 | 8 | 9 | A | B | C | D | E | F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Decimal | | | | | | | | | | | | |
| Binary | | | | | | | | | | | | |

**Expected result:** A = 10 = 1010 … F = 15 = 1111.

- **Hint 1:** 8-4-2-1 columns (slide 14).
- **Hint 2:** A = 10, and count up from there.

---

### Task 2 — Nibble speed drill

**Goal:** convert single nibbles instantly. Time yourself, aiming for under a minute.

Convert to hex: 1001, 0110, 1100, 0011, 1111, 1010, 0111, 1101, 0001, 1110.

Then convert to 4-bit binary: 4, B, 8, E, 2, 9, D, 0, C, 5.

**Expected result:** 9, 6, C, 3, F, A, 7, D, 1, E and 0100, 1011, 1000, 1110, 0010, 1001, 1101, 0000, 1100, 0101.

- **Hint 1:** Learn 1010 = A and 1111 = F as anchors.
- **Hint 2:** 1100 = 8 + 4 = 12 = C.

---

### Task 3 — Count in hex

**Goal:** see how carrying works in base 16.

What comes **next** after each value?

1. 09
2. 0F
3. 19
4. 1F
5. 9F
6. FF
7. FFF
8. 3E7

**Expected result:** 0A, 10, 1A, 20, A0, 100, 1000, 3E8.

- **Hint 1:** F is the largest digit, so F + 1 carries.
- **Hint 2:** FF + 1 = 100, just as 99 + 1 = 100 in decimal.

---

### Task 4 — Why hex?

**Goal:** explain slides 5–6 in your own words.

1. Split slide 5's address `01010111000011110101000101111101` into nibbles and write it in hex.
2. How many characters shorter is the hex version?
3. Give **two** reasons why hex, not decimal, is used to show binary data.

**Expected result:** 570F517D: 8 characters instead of 32 (Verified).

- **Hint 1:** 16 = 2⁴.
- **Hint 2:** Can you see the bits in 1,460,621,693?

---

### Task 5 — Sanity checks

**Goal:** catch impossible answers quickly.

Each line is a student's answer. Say whether it **must be wrong**, and why.

1. 300₁₀ = 12C₁₆
2. FF₁₆ = 256₁₀
3. 7C₁₆ = 1111100₂ (an eight-bit answer was asked for)
4. 190₁₀ = EB₁₆
5. 0x1AF is even
6. A3₁₆ = 1010 11₂

**Expected result:** 1 is right; 2, 3, 4, 5 and 6 are wrong.

- **Hint 1:** The last hex digit decides odd or even.
- **Hint 2:** Each hex digit is exactly 4 bits.

---

## Part B — Find and fix (Tasks 6–10)

### Task 6 — Fix the nibble grouping

**Goal:** correct binary ↔ hex errors.

Sam Archer wrote:

```text
(a) 110101111₂  -> groups 1101 0111 1  -> D71₁₆
(b) 3F₁₆        -> 11 1111         -> 111111₂ (8-bit answer requested)
(c) 1001 0110₂  -> 9 and 6         -> 69₁₆
```

Find each mistake and correct it.

**Expected result:** (a) 1AF₁₆; (b) 0011 1111₂; (c) 96₁₆ (Verified).

- **Hint 1:** Group from the **right**.
- **Hint 2:** The left nibble gives the **first** hex digit.

---

### Task 7 — Fix the division

**Goal:** correct decimal → hex working (slides 8–10).

Sam converted 238 and 1234:

```text
238 ÷ 16 = 14 r 14
14 ÷ 16  = 0  r 14       Answer: 1414

1234 ÷ 16 = 77 r 2
77 ÷ 16   = 4  r 13
4 ÷ 16    = 0  r 4       Answer (top to bottom): 2D4
```

Correct both.

**Expected result:** 238 = EE₁₆; 1234 = 4D2₁₆.

- **Hint 1:** Remainders 10–15 must be written as letters.
- **Hint 2:** Read bottom to top.

---

### Task 8 — Fix the positional working

**Goal:** correct hex → decimal errors (slides 15–17).

```text
(a) 2A1₁₆ = 2 × 100 + A × 10 + 1 = ?
(b) B2₁₆ = 11 + 2 = 13
(c) 5C₁₆ = 5 × 16 + 12 × 16 = 272
```

Correct each one, showing powers of 16.

**Expected result:** (a) 673; (b) 178; (c) 92 (Verified).

- **Hint 1:** Use powers of **16**, not 10.
- **Hint 2:** The rightmost digit has weight 16⁰ = 1.

---

### Task 9 — Fix the colour reading

**Goal:** apply slide 18 correctly.

Sam read #2A7F10 as "red = 2, green = A7, blue = F10". Another student said "#FF8000 is red = 255, green = 80, blue = 0".

1. What did each student do wrong?
2. Give the correct decimal RGB values for both colours.

**Expected result:** #2A7F10 = (42, 127, 16); #FF8000 = (255, 128, 0) (Verified).

- **Hint 1:** Always **two** hex digits per component.
- **Hint 2:** 80₁₆ is not 80₁₀.

---

### Task 10 — Fix the file identification

**Goal:** use signatures, not names (lecture section 12).

These are **real** first bytes, read with `hexview.py` (Verified). A colleague's conclusions are wrong. Correct each one.

```text
fake.png: signature says no known signature (perhaps plain text)
00000000  48 65 6C 6C 6F 2C 20 34 33 30 31 43 4F 4D 50 21  |Hello, 4301COMP!|
00000010  0A                                               |.|
```

Colleague: "fake.png is a picture because it ends in .png."

```text
notes.zip: signature says ZIP archive (also .docx/.xlsx/.pptx)
00000000  50 4B 03 04 14 00 00 00 00 00 CF 7E 78 5D C2 41  |PK.........~x].A|
00000010  24 35 03 00 00 00 03 00 00 00 05 00 00 00 61 2E  |$5............a.|
```

Colleague: "notes.zip and a .docx file are completely different formats."

```text
program: signature says ELF program (Linux)
00000000  7F 45 4C 46 02 01 01 00 00 00 00 00 00 00 00 00  |.ELF............|
00000010  03 00 3E 00 01 00 00 00 80 10 00 00 00 00 00 00  |..>.............|
```

Colleague: "program has no extension, so we can't tell what it is."

**Expected result:** the first is text (no PNG signature); `.docx` files are ZIP archives (`50 4B`); the third is a Linux ELF program (`7F 45 4C 46`).

- **Hint 1:** Lecture section 16's signature table.
- **Hint 2:** The text column shows `.ELF` and `PK`.

---

## Part C — Build and apply (Tasks 11–15)

### Task 11 — A hex viewer of your own

**Goal:** see the raw bytes of any file.

**Skill you gain:** you can produce and read a hex dump and identify file types by signature. This is a first step in digital forensics and malware triage.

1. Save as `hexview.py`:

```python
# hexview.py - a tiny read-only hex viewer, like the left half of a hex editor.
# Each line shows: the offset (position in the file, in hex), 16 bytes in hex, and the same
# bytes as text ('.' for bytes that are not printable). It also names common file signatures
# ("magic numbers") found in the first bytes - the way tools identify a file's real type.
#
# Usage: python hexview.py somefile            (first 64 bytes)
#        python hexview.py somefile 256        (first 256 bytes)

import sys

SIGNATURES = {
    bytes.fromhex("89504E470D0A1A0A"): "PNG image",
    bytes.fromhex("FFD8FF"): "JPEG image",
    bytes.fromhex("25504446"): "PDF document (%PDF)",
    bytes.fromhex("504B0304"): "ZIP archive (also .docx/.xlsx/.pptx)",
    bytes.fromhex("7F454C46"): "ELF program (Linux)",
    bytes.fromhex("4D5A"): "Windows program (MZ: .exe/.dll)",
}


def dump(data):
    for offset in range(0, len(data), 16):
        chunk = data[offset:offset + 16]
        hex_part = " ".join(f"{b:02X}" for b in chunk)
        text = "".join(chr(b) if 32 <= b < 127 else "." for b in chunk)
        print(f"{offset:08X}  {hex_part:<47}  |{text}|")


def identify(data):
    for magic, name in SIGNATURES.items():
        if data.startswith(magic):
            return name
    return "no known signature (perhaps plain text)"


if __name__ == "__main__":
    path = sys.argv[1]
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 64
    with open(path, "rb") as f:                     # "rb" = read the raw bytes
        data = f.read(count)
    print(f"{path}: signature says {identify(data)}")
    dump(data)
```

2. Make a text file `hello.txt` containing `Hello, 4301COMP!` and run `python hexview.py hello.txt`. *What it does:* opens the file read-only and prints its first bytes. It never changes the file.
3. Run it on a **PNG**, a **.docx** and a **PDF** from your own computer, choosing files with no private content. Do the signatures match the lecture table?
4. Copy a `.txt` file and rename the copy to `.png`. Run the viewer on it.

Actual output on the test machine (Verified; `od` and `file` agreed):

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
```

**Expected result:** your files show the signatures in lecture section 16. A renamed text file keeps its text bytes.

- **Hint 1:** Look at the first 4 bytes only.
- **Hint 2:** Pass a second argument, such as `256`, to see more bytes.

---

### Task 12 — Check your working with a converter that shows its steps

**Goal:** check hand conversions **after** doing them, using the slides' own methods.

**Skill you gain:** you can verify your own work systematically, using the same algorithms rather than a black-box converter.

1. Save as `hexconvert.py`:

```python
# hexconvert.py - convert between decimal, binary and hexadecimal with the working shown,
# using exactly the methods on the TW09A slides and lab sheet:
#   binary <-> hex : group bits in fours (nibbles), 8-4-2-1 weights per nibble (slides 6, 12-14)
#   decimal -> hex : repeated division by 16, remainders 10-15 written A-F (slides 8-10)
#   hex -> decimal : positional method with powers of 16 (slides 15-17)
# Use it to CHECK your hand working - the official lab asks you to work manually first.
#
# Usage: python hexconvert.py dec 413
#        python hexconvert.py hex 1AF
#        python hexconvert.py bin 10110101

import sys

DIGITS = "0123456789ABCDEF"


def dec_to_hex(n):
    print(f"Decimal {n} -> hexadecimal by repeated division by 16:")
    rems, q = [], n
    while True:
        new_q, r = divmod(q, 16)
        print(f"  {q:>6} ÷ 16 = {new_q:>5} remainder {r:>2}" + (f" = {DIGITS[r]}" if r > 9 else ""))
        rems.append(DIGITS[r])
        q = new_q
        if q == 0:
            break
    h = "".join(reversed(rems))
    print(f"  Read the remainders bottom to top: {n} = {h} (hex)")
    return h


def hex_to_dec(h):
    h = h.upper()
    n = len(h)
    print(f"Hexadecimal {h} -> decimal with powers of 16:")
    parts = []
    for i, d in enumerate(h):
        k = n - 1 - i
        v = DIGITS.index(d)
        parts.append(v * 16 ** k)
        print(f"  digit {d} (= {v:>2}) x 16^{k} ({16 ** k:>4}) = {v * 16 ** k}")
    total = sum(parts)
    print(f"  {h} = {' + '.join(map(str, parts))} = {total}")
    return total


def bin_to_hex(b):
    b = b.replace(" ", "")
    b = b.zfill((len(b) + 3) // 4 * 4)                   # pad on the left to whole nibbles
    nibbles = [b[i:i + 4] for i in range(0, len(b), 4)]
    print(f"Binary {b} -> hexadecimal by nibbles (8-4-2-1):")
    out = ""
    for nb in nibbles:
        v = sum(w for w, bit in zip((8, 4, 2, 1), nb) if bit == "1")
        print(f"  {nb} = {v:>2} = {DIGITS[v]}")
        out += DIGITS[v]
    print(f"  Result: {out}")
    return out


def hex_to_bin(h):
    print(f"Hexadecimal {h.upper()} -> binary, 4 bits per digit:")
    out = []
    for d in h.upper():
        nb = format(DIGITS.index(d), "04b")
        print(f"  {d} = {nb}")
        out.append(nb)
    print(f"  Result: {' '.join(out)}")
    return "".join(out)


if __name__ == "__main__":
    kind, value = sys.argv[1], sys.argv[2]
    if kind == "dec":
        h = dec_to_hex(int(value)); print(); hex_to_bin(h)
        print(f"\nCheck with Python: format({value}, 'X') = {format(int(value), 'X')}")
    elif kind == "hex":
        hex_to_dec(value); print(); hex_to_bin(value)
        print(f"\nCheck with Python: int('{value}', 16) = {int(value, 16)}")
    else:
        h = bin_to_hex(value); print(); hex_to_dec(h)
        print(f"\nCheck with Python: int('{value}', 2) = {int(value.replace(' ', ''), 2)}")
```

2. **After** finishing Tasks 16–18 by hand, check each answer, for example `python hexconvert.py dec 413`. Actual output (Verified):

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

Check with Python: format(413, 'X') = 19D
```

3. Check `python hexconvert.py hex 1AF` and `python hexconvert.py bin 10110101`.
4. **Extend:** add a mode `hex2dec_via_binary` that converts via binary (slides 11–13) and prints the place-value table.

**Expected result:** every official answer confirmed.

- **Hint 1:** The official lab forbids **online** converters during the task. Use this only to check afterwards.
- **Hint 2:** Step 4 can reuse `hex_to_bin` and Lecture 14's positional method.

---

### Task 13 — Find hex on your own computer

**Goal:** see real hex values on Windows.

**Skill you gain:** you can find and interpret hex identifiers (MAC and IPv6 addresses, file bytes) with built-in Windows tools.

On your own Windows computer (Expected; all read-only):

1. `getmac /v` lists your MAC addresses. Take one: how many bytes does it have? Convert its **first byte** to binary. Is bit 1 (weight 2) set, meaning a locally administered or randomised address?
2. `ipconfig /all` shows your IPv6 address(es). Find the **link-local** one, starting `fe80::`. How many hex digits are in each full group?
3. In **PowerShell**: `Format-Hex .\hello.txt`. *What it does:* shows the file's bytes in hex, like Task 11. Compare the output with your own viewer.
4. Optional: in **Paint**, choose **Edit colours** and enter the RGB values 42, 127, 16. What colour appears? Compare it with Task 14.

**Expected result:**

- A MAC address has 6 bytes.
- Wi-Fi addresses on modern Windows may be **randomised**, so bit 1 of the first byte is set.
- Each full IPv6 group has 4 hex digits.
- `Format-Hex` shows the same bytes as `hexview.py`.

- **Hint 1:** The test machine's MAC began `02` = 0000 0010, so bit 1 is set (Verified).
- **Hint 2:** Do not share your MAC addresses publicly; crop or blur them in any write-up.

---

### Task 14 — Colours in hex

**Goal:** apply slide 18 in code and in a browser.

**Skill you gain:** you can read and write web colour codes. You will need this whenever you style a page or read HTML or CSS during web security work.

1. Save as `colour.py`:

```python
# colour.py - split a web colour #RRGGBB into its three bytes, show the working, and make a swatch page.
# Each pair of hex digits is one 8-bit value (0-255): red, green, blue (slide 18).
#
# Usage: python colour.py 2A7F10
#        python colour.py FF8000 swatch     (also writes swatch.html - open it in a browser)

import sys

DIGITS = "0123456789ABCDEF"


def pair_to_decimal(pair):
    hi, lo = DIGITS.index(pair[0]), DIGITS.index(pair[1])
    return hi * 16 + lo, f"{pair[0]} x 16 + {pair[1]} = {hi} x 16 + {lo} = {hi * 16 + lo}"


if __name__ == "__main__":
    code = sys.argv[1].lstrip("#").upper()
    values = []
    for name, pair in zip(("Red", "Green", "Blue"), (code[0:2], code[2:4], code[4:6])):
        value, working = pair_to_decimal(pair)
        values.append(value)
        print(f"{name:<5} {pair}: {working:<32} binary {value:08b}")
    print(f"#{code} = rgb({values[0]}, {values[1]}, {values[2]})")
    if "swatch" in sys.argv:
        with open("swatch.html", "w") as f:
            f.write(f'<div style="width:200px;height:100px;background:#{code}"></div><p>#{code} = rgb{tuple(values)}</p>')
        print("Wrote swatch.html")
```

2. Run `python colour.py FF8000 swatch`, then open `swatch.html` in your browser. *What it does:* prints the working for each byte and writes a small HTML file containing a coloured box.
3. Predict the decimal values first, then check: #000000, #FFFFFF, #FF0000, #808080, #2A7F10.
4. Which hex code gives rgb(0, 128, 255)?

Actual output for the official challenge colour (Verified):

```text
Red   2A: 2 x 16 + A = 2 x 16 + 10 = 42    binary 00101010
Green 7F: 7 x 16 + F = 7 x 16 + 15 = 127   binary 01111111
Blue  10: 1 x 16 + 0 = 1 x 16 + 0 = 16     binary 00010000
#2A7F10 = rgb(42, 127, 16)
```

**Expected result:** #808080 = (128, 128, 128), grey; rgb(0, 128, 255) = #0080FF.

- **Hint 1:** Each pair is one byte, 00–FF.
- **Hint 2:** Equal R, G and B values give a grey.

---

### Task 15 — Read numbers from file bytes

**Goal:** turn hex bytes in a file into real values.

**Skill you gain:** you can decode fields in binary file formats. Forensic analysts and exploit developers do this every day.

Using the real dumps in Task 11 (Verified):

1. In the PNG, the image **width** is the 4 bytes at offsets 0x10–0x13: `00 00 04 92`. Convert 0x492 to decimal.
2. The **height** is at 0x14–0x17: `00 00 02 22`. Convert it.
3. Check with the `file` command's report: "PNG image data, 1170 x 546".
4. **Byte order (Extra).** In the ELF program, the two bytes at offset 0x12 are `3E 00`. ELF on x86 stores numbers **least significant byte first** ("little-endian"), so the value is 0x003E. Convert it to decimal. (62 means "x86-64" in the ELF standard.)
5. Why must a file format state its byte order?

**Expected result:** 1170, 546 and 62 (Verified). The same two bytes read in the wrong order (0x3E00 = 15,872) would be nonsense.

- **Hint 1:** 0x492 = 4 × 256 + 9 × 16 + 2.
- **Hint 2:** PNG stores numbers most significant byte first ("big-endian").

---

## Part D — Official tasks and integration (Tasks 16–20)

### Task 16 — Convert between binary and hexadecimal (Official Task 1, 15 minutes)

**Goal:** complete the official binary ↔ hex tables by hand.

**Preparation (official):** open **Word > Blank document** and save **TW09A_YourStudentID.docx**. Reproduce the tables in Word and keep your intermediate working visible. Use the slides if you need them, but **no online converter**.

**Official worked examples (not exercise questions):**

- 1101 0010₂ = D2₁₆, because 1101₂ = D₁₆ and 0010₂ = 2₁₆.
- 5E₁₆ = 0101 1110₂.

Always use four bits per hex digit, including leading zeros.

**Official steps**

1. Use the four-bit weights **8, 4, 2 and 1**. Split each binary value into two nibbles and convert each nibble to one hex digit.

   | Eight-bit binary | Left nibble → digit | Right nibble → digit | Hex answer |
   | --- | --- | --- | --- |
   | 0110 1011 | | | |
   | 1001 0110 | | | |
   | 1110 0100 | | | |

2. Replace each hex digit with its four-bit binary equivalent, then combine the two nibbles into an eight-bit result.

   | Hexadecimal | First digit → 4 bits | Second digit → 4 bits | Eight-bit binary |
   | --- | --- | --- | --- |
   | 3F | | | |
   | A6 | | | |
   | 70 | | | |

3. **Check:** take your answer for 0110 1011₂ and convert it back from hex. It must reproduce the original eight bits.

- **Hint 1:** 0110 = 4 + 2 = 6.
- **Hint 2:** 0 = 0000. Do not drop it in 70.

---

### Task 17 — Convert between decimal and hexadecimal (Official Task 2, 20 minutes)

**Goal:** complete the official decimal ↔ hex tables by hand.

**Official worked examples (not exercise questions):**

- 190 ÷ 16 = 11 remainder 14 (E); 11 ÷ 16 = 0 remainder 11 (B). Reading upwards, 190₁₀ = BE₁₆.
- 2C₁₆ = (2 × 16¹) + (12 × 16⁰) = 44₁₀.

**Official steps**

1. **Part A:** repeatedly divide each decimal value by 16. Show each integer quotient and remainder, using A for 10 through to F for 15. Read the remainders from bottom to top. The last value needs **three** hex digits.

   | Decimal | Division steps: quotient and remainder | Hexadecimal answer |
   | --- | --- | --- |
   | 75 | | |
   | 238 | | |
   | 413 | | |

2. **Part B:** use the hex positional weights (16², 16¹, 16⁰ as required). Replace A–F with 10–15, multiply each digit by its weight and add.

   | Hexadecimal | Expanded calculation using powers of 16 | Decimal answer |
   | --- | --- | --- |
   | 5C | | |
   | B2 | | |
   | 1AF | | |

3. **Check:** convert **one** Part A answer back to decimal and **one** Part B answer back to hex. Write both reverse checks directly below your tables.

- **Hint 1:** 75 = 4 × 16 + 11.
- **Hint 2:** 1AF: 1 × 256 + 10 × 16 + 15.

---

### Task 18 — Mixed practice and the colour challenge (Official Task 3 and optional extra challenge, 15 minutes)

**Goal:** answer exam-style conversions independently, with full working.

**Official instructions:** work independently, as you would in a written examination. Write the complete method for every question: place values, nibble grouping or repeated division. A correct final value without working is not enough practice. For the decimal-to-binary question, use the method from TW08 Session B.

| Item | Convert | Your working (show each step) | Final answer |
| --- | --- | --- | --- |
| a | 10110101₂ → decimal | | |
| b | 346₁₀ → hexadecimal | | |
| c | 7C₁₆ → eight-bit binary | | |
| d | 188₁₀ → eight-bit binary | | |
| e | 1100 0111₂ → hexadecimal | | |

**Self-check (official):** choose any two answers and verify them with the reverse conversion. Check that you have written the correct base beside every final answer.

**Optional extra challenge — hexadecimal colours (official):**

1. For **#2A7F10**, identify the three hex byte pairs.
2. Convert each pair to decimal (0–255).
3. Convert the **red** byte to eight-bit binary.
4. Show your working.

This applies the same methods; it is not a new topic.

**Before you finish (official):**

- Tasks 1–3 contain visible working.
- Every final answer has the correct base.
- There are at least **three** reverse checks: one from Task 1 and two from Task 2.

Save the Word document in your own storage. No Packet Tracer, PowerShell or file-editing commands are required for the official tasks.

- **Hint 1:** For (b), 346 = 21 × 16 + 10.
- **Hint 2:** For (d), use Lecture 14's subtraction or division method.

---

### Task 19 — Mini-project: a hex forensics mini-investigation

**Goal:** use hex dumps to establish what files really are, and record the evidence properly.

**Skill you gain:** you can carry out and document a small file-identification investigation. This is the same evidence-led approach used in incident response (Lecture 10's fault records).

1. **Prepare a test folder** on your own computer, with files you created yourself, containing:
   - a real PNG, renamed to `report.pdf`;
   - a text file renamed to `photo.jpg`;
   - a `.docx` renamed to `archive.zip`. Is that actually "wrong"?
   - a real PDF with its correct name;
   - one file chosen by a partner, without telling you what it is.
2. For each file, run `hexview.py` (or `Format-Hex`) and record:
   - the first 8 bytes;
   - the signature match;
   - the **true type**;
   - whether the name is misleading.
3. For the PNG, decode the **width and height** from the bytes (Task 15) and check them against the image's properties in Windows.
4. Write a short **finding** for each file in the format **claim → evidence (hex bytes) → conclusion**.
5. **Reflection (100 words):** why might an email filter that checks only file extensions be bypassed, and how does checking signatures help? What are its limits? A signature can also be faked.

**Evidence table**

| File name | First 8 bytes (hex) | Signature | True type | Name misleading? |
| --- | --- | --- | --- | --- |
| | | | | |

- **Hint 1:** Use only files you created. Do not analyse files you do not own or are not permitted to examine.
- **Hint 2:** `.docx` really is a ZIP, so `archive.zip` is not lying about the **container** format.

---

### Task 20 — Assessment-style practice: hexadecimal

**This is practice only, not a real exam question.** The module exam is two hours with short-answer and essay-style questions (module guide). Marks are invented for planning.

**Rules:** 20 minutes, closed book, no calculator, write it yourself.

**(a)** Explain why hexadecimal is used to display binary data. Use a 16-bit example. *(3 marks)*

**(b)** Convert 1011 1110 0110₂ to hexadecimal. Show the nibble grouping. *(2 marks)*

**(c)** Convert 500₁₀ to hexadecimal by repeated division, and check by converting back. *(5 marks)*

**(d)** Convert 3B7₁₆ to decimal using powers of 16. *(3 marks)*

**(e)** A colour is #C08040. Give its RGB values in decimal and the blue byte in binary. *(3 marks)*

**(f)** Explain how a hex dump could show that a file named `invoice.pdf` is actually a Windows program. *(4 marks)*

**Self-marking checklist**

| Part | A good answer includes | Expected | Actual |
| --- | --- | --- | --- |
| (a) | 1 hex digit = 4 bits; shorter; bits still visible; example such as 1100 1111 0000 1010 = CF0A | 3 points | |
| (b) | 1011 1110 0110 = **BE6** | 2 points | |
| (c) | 500 ÷ 16 = 31 r 4; 31 ÷ 16 = 1 r 15 (F); 1 ÷ 16 = 0 r 1, so **1F4**; check 256 + 240 + 4 = 500 | 5 points | |
| (d) | 3 × 256 + 11 × 16 + 7 = 768 + 176 + 7 = **951** | 3 points | |
| (e) | (192, 128, 64); blue 0x40 = **01000000** | 3 points | |
| (f) | First bytes 4D 5A ("MZ") instead of 25 50 44 46 ("%PDF"); signature beats extension; it is evidence, not proof of malice | 4 points | |
| Time | Within 20 minutes | Yes | |

- **Hint 1:** Check (b)–(e) afterwards with `hexconvert.py`.
- **Hint 2:** Lecture sections 8–12.

---

## Tracker

| Task | Name | Done | Notes / score |
| --- | --- | --- | --- |
| 1 | The 16 digits | ☐ | /12 |
| 2 | Nibble speed drill | ☐ | /20 |
| 3 | Count in hex | ☐ | /8 |
| 4 | Why hex? | ☐ | |
| 5 | Sanity checks | ☐ | /6 |
| 6 | Fix the grouping | ☐ | /3 |
| 7 | Fix the division | ☐ | /2 |
| 8 | Fix the positional working | ☐ | /3 |
| 9 | Fix the colour reading | ☐ | /2 |
| 10 | Fix the file identification | ☐ | /3 |
| 11 | `hexview.py` | ☐ | |
| 12 | `hexconvert.py` | ☐ | |
| 13 | Hex on your own computer | ☐ | |
| 14 | Colours | ☐ | |
| 15 | Numbers in file bytes | ☐ | |
| 16 | **Official Task 1**: Binary ↔ hex | ☐ | /6 |
| 17 | **Official Task 2**: Decimal ↔ hex | ☐ | /6 |
| 18 | **Official Task 3 + colours** | ☐ | /5 + challenge |
| 19 | Mini-project: hex forensics | ☐ | |
| 20 | Assessment-style practice | ☐ | /20 |

## Reflection

1. Which direction of conversion is now the easiest for you, and which still needs practice?
2. How did the reverse checks change your confidence in your answers?
3. What did seeing a real hex dump teach you about what a "file" actually is?
4. Where would you expect to meet hex in your future cyber security work?

---

## Answer key

**(Verified)** = Python 3.13 (`int`, `format`, `hexconvert.py`, `hexview.py`, `colour.py`), Linux `od` and `file`. **(Expected)** = Windows tools.

### Task 1

| Hex | 0 | 3 | 5 | 7 | 8 | 9 | A | B | C | D | E | F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Decimal | 0 | 3 | 5 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| Binary | 0000 | 0011 | 0101 | 0111 | 1000 | 1001 | 1010 | 1011 | 1100 | 1101 | 1110 | 1111 |

### Task 2

As in the expected result.

### Task 3

0A, 10, 1A, 20, A0, 100, 1000, 3E8.

### Task 4 (Verified)

1. **570F517D**.
2. 24 characters shorter (8 instead of 32).
3. Hex lines up with bits (16 = 2⁴), so the bits can be read straight off it; decimal hides the bit pattern.

### Task 5

1. **Right:** 256 + 32 + 12 = 300.
2. **Wrong:** FF = 255.
3. **Wrong:** only 7 bits. The answer is 0111 1100.
4. **Wrong:** 190 = BE (Sam swapped the digits).
5. **Wrong:** F is odd, so 0x1AF is odd.
6. **Wrong:** 3 must be 0011, so the answer is 1010 0011.

### Task 6 (Verified)

- **(a)** Group from the right: 0001 1010 1111 = **1AF₁₆**.
- **(b)** 3 = **0011**, so **0011 1111₂**.
- **(c)** The left nibble 1001 = 9 comes first: **96₁₆**.

### Task 7 (Verified)

- **238:** the remainders 14, 14 must be written E, E: **EE₁₆**.
- **1234:** read bottom to top: **4D2₁₆**.

### Task 8 (Verified)

- **(a)** 2 × 256 + 10 × 16 + 1 = **673**.
- **(b)** 11 × 16 + 2 = **178**.
- **(c)** 5 × 16 + 12 × 1 = **92**.

### Task 9 (Verified)

1. Sam split the code wrongly: it is three pairs, 2A, 7F and 10. The second student read 80 as decimal.
2. **#2A7F10** = (42, 127, 16). **#FF8000** = (255, 128, 0).

### Task 10 (Verified)

- `fake.png` starts with `48 65 6C 6C 6F` ("Hello"): it is a **text** file.
- `.docx` files are ZIP containers (`50 4B 03 04`), so they share a signature.
- `program` starts with `7F 45 4C 46`: it is an **ELF** program.

### Tasks 11–12 (Verified)

As shown.

### Task 13 (Expected)

Your values will differ.

### Task 14 (Verified)

| Colour | RGB |
| --- | --- |
| #000000 | (0, 0, 0) |
| #FFFFFF | (255, 255, 255) |
| #FF0000 | (255, 0, 0) |
| #808080 | (128, 128, 128) |
| #2A7F10 | (42, 127, 16) |

rgb(0, 128, 255) = **#0080FF**.

### Task 15 (Verified)

- **Width:** 0x492 = 4 × 256 + 9 × 16 + 2 = **1170**.
- **Height:** 0x222 = 2 × 256 + 2 × 16 + 2 = **546**.
- **ELF field:** 0x003E = 3 × 16 + 14 = **62**.

### Task 16 (Verified)

| Given | Working | Answer |
| --- | --- | --- |
| 0110 1011 | 6 and B | **6B₁₆** |
| 1001 0110 | 9 and 6 | **96₁₆** |
| 1110 0100 | E and 4 | **E4₁₆** |
| 3F | 0011 1111 | **0011 1111₂** |
| A6 | 1010 0110 | **1010 0110₂** |
| 70 | 0111 0000 | **0111 0000₂** |

**Check:** 6B → 0110 1011.

### Task 17 (Verified)

**Part A**

| Decimal | Division steps | Answer |
| --- | --- | --- |
| 75 | 75 ÷ 16 = 4 r 11 (B); 4 ÷ 16 = 0 r 4 | **4B₁₆** |
| 238 | 238 ÷ 16 = 14 r 14 (E); 14 ÷ 16 = 0 r 14 (E) | **EE₁₆** |
| 413 | 413 ÷ 16 = 25 r 13 (D); 25 ÷ 16 = 1 r 9; 1 ÷ 16 = 0 r 1 | **19D₁₆** |

**Part B**

| Hex | Expanded calculation | Answer |
| --- | --- | --- |
| 5C | 5 × 16 + 12 | **92₁₀** |
| B2 | 11 × 16 + 2 | **178₁₀** |
| 1AF | 256 + 160 + 15 | **431₁₀** |

### Task 18 (Verified)

**(a)** 10110101₂ = 128 + 32 + 16 + 4 + 1 = **181₁₀**.

**(b)** 346₁₀ → hex:

- 346 ÷ 16 = 21 r 10 (A)
- 21 ÷ 16 = 1 r 5
- 1 ÷ 16 = 0 r 1

Reading bottom to top: **15A₁₆**.

**(c)** 7C₁₆ = **0111 1100₂**.

**(d)** 188₁₀ = 128 + 32 + 16 + 8 + 4 = **10111100₂**.

**(e)** 1100 0111₂ = **C7₁₆**.

**Colour #2A7F10:**

| Byte | Hex | Decimal |
| --- | --- | --- |
| Red | 2A | 42 |
| Green | 7F | 127 |
| Blue | 10 | 16 |

Red in binary: **00101010**.

### Tasks 19–20 (model points)

Use the self-marking checklist. Task 20 values were checked with Python:

| Part | Answer |
| --- | --- |
| BE6 | = 3046 |
| 500 | = 1F4 |
| 3B7 | = 951 |
| #C08040 | = (192, 128, 64); blue 01000000 |
