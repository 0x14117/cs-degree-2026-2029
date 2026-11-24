# Lab 16 — Memory and Storage Hands-on Workbook (20 Tasks)

**Module:** 4301COMP Computer Systems Architecture

**Session:** Teaching Week 09, Session B · **Matching lecture:** `../Lectures/Lecture-16-Memory-and-Storage.md`

---

## How to use this lab

**What this lab is for.** You will:

- classify and order memory and storage;
- **measure** the memory hierarchy and locality on a real machine;
- follow virtual addresses through a TLB and page table;
- watch real page faults;
- rebuild a lost drive from RAID parity;
- inventory your own computer's memory and storage;
- answer the official written practice questions.

**Where the official tasks are.** This session's official sheet is a **written practice lab** with Questions 1–5. Only the **solution** version is in the Project.

| Official written practice lab (TW09 Session B) | This workbook |
| --- | --- |
| Question 1 (knowledge check) and Question 2 (memory hierarchy) | Task 16 |
| Question 3 (registers, cache, RAM) and Question 4 (virtual-memory access) | Task 17 |
| Question 5 (paging and segmentation) | Task 18 |

**Answer them yourself before** looking at the answer key or the official solution sheet.

**Tools**

| Tool | Used in | Notes |
| --- | --- | --- |
| Pen and paper | Tasks 1–10, 16–18 | Written answers |
| Python 3 | Tasks 11, 13, 14 | **Optional, your choice.** Built-in modules only. Task 13's script needs Linux or macOS |
| gcc (C compiler) | Task 12 | **Optional:** only if you already have Linux or WSL; the real outputs are provided |
| Task Manager, Resource Monitor, PowerShell (normal user) | Tasks 13, 15 | Read-only |

**Labels:**

- **Verified** = run before being written here, on a Linux VM (Intel Xeon, 2 vCPUs, gcc 13.3) and in Python 3.13.
- **Expected** = not run here (Windows tools).

---

## Part A — Warm-up (Tasks 1–5)

### Task 1 — Classify the memory

**Goal:** separate the two classifications on slide 7.

For each item, tick **volatile** or **non-volatile**, and **primary** or **secondary**.

| Item | Volatile? | Primary or secondary? |
| --- | --- | --- |
| CPU register | | |
| L2 cache | | |
| DDR5 DRAM module | | |
| UEFI firmware flash | | |
| SSD | | |
| HDD | | |
| Magnetic tape | | |
| microSD card | | |

**Expected result:** registers, cache and DRAM are volatile and primary. Firmware flash is non-volatile but primary-addressable in some systems (the overlap on slide 7). The rest are non-volatile and secondary.

- **Hint 1:** Volatile/non-volatile is about **persistence**; primary/secondary is about **role and access**.
- **Hint 2:** Slide 7 names firmware flash as the overlap case.

---

### Task 2 — Put the hierarchy in order

**Goal:** apply slide 8, then match real sizes.

1. Order these from fastest/closest to slowest: main memory, L3 cache, SSD, registers, L1 cache, L2 cache.
2. Match each level to the test machine's real size: 7.8 GiB, 48 KiB (per core), 2 MiB (per core), 260 MiB, 256 GiB.
3. Give three reasons for using several levels, rather than building everything from the fastest technology.

**Expected result:**

| Level | Test-machine size (Verified) |
| --- | --- |
| Registers | (not listed) |
| L1 | 48 KiB |
| L2 | 2 MiB |
| L3 | 260 MiB |
| DRAM | 7.8 GiB |
| SSD/disk | 256 GiB |

The three reasons are speed, cost and capacity.

- **Hint 1:** Slide 8: small and fast at the top.
- **Hint 2:** Official lab Q2b asks the same question.

---

### Task 3 — Temporal or spatial?

**Goal:** recognise locality (slide 15).

Label each **T** (temporal), **S** (spatial) or **both**:

1. A `for` loop's instructions run 10,000 times.
2. A program reads an array from index 0 to 999 in order.
3. A counter variable is incremented on every pass of a loop.
4. A video player reads a file's bytes one after another.
5. A loop sums an array **and** reuses the same loop instructions each time.
6. A program reads a 2D array column by column. Which locality is it **failing** to use?

**Expected result:** T, S, T, S, both; item 6 fails to use spatial locality (Verified about 10× slower, lecture section 9.3).

- **Hint 1:** Temporal = the **same** item again; spatial = **neighbouring** items.
- **Hint 2:** A cache line holds 64 neighbouring bytes.

---

### Task 4 — Split virtual addresses

**Goal:** find the page number and offset (slide 22).

With **4 KiB** pages, the offset is the low 12 bits: the last **3 hex digits**.

| Virtual address | Page number | Offset |
| --- | --- | --- |
| 0x00403A2C | | |
| 0x7FFE1004 | | |
| 0x12345678 | | |
| 0x0000FFFF | | |

Then, with **8 KiB** pages (13-bit offset), split 0x12345678. Why is this harder in hex?

**Expected result:** 0x00403 / 0xA2C; 0x7FFE1 / 0x004; 0x12345 / 0x678; 0x0000F / 0xFFF. With 8 KiB pages, 0x12345678 splits into page 0x91A2 and offset 0x1678 (Verified).

- **Hint 1:** 4 KiB = 2¹², and 12 bits = 3 hex digits.
- **Hint 2:** 13 bits does not fall on a hex-digit boundary, so convert to binary first.

---

### Task 5 — RAID capacity

**Goal:** calculate usable space (slide 36).

Six drives of **4 TB** each (24 TB raw). Give the usable capacity and how many drive failures are **always** survived:

| Level | Usable TB | Failures always survived |
| --- | --- | --- |
| RAID 0 | | |
| RAID 5 | | |
| RAID 6 (two parity blocks, Extra) | | |
| RAID 10 (three mirror pairs) | | |

**Expected result:** 24 / 0; 20 / 1; 16 / 2; 12 / 1 (more if the failures fall in different pairs).

- **Hint 1:** RAID 5 loses one drive's capacity to parity.
- **Hint 2:** In RAID 10, two failures in the **same** pair lose data.

---

## Part B — Find and fix (Tasks 6–10)

### Task 6 — Fix the myths

**Goal:** correct statements using the slides.

Each is wrong. Correct it and cite the slide.

1. "Non-volatile memory is permanent and cannot be changed."
2. "All primary memory is volatile."
3. "Registers are just SRAM."
4. "My 64-bit laptop can address 2⁶⁴ bytes of physical RAM."
5. "SSDs are electromechanical, like HDDs."
6. "Windows 'Committed' memory shows how much of the page file is in use."
7. "Our server has RAID 1, so we don't need backups."

**Expected result:** seven corrections, citing slides 7, 10, 16, 19, 27, 21 and 36.

- **Hint 1:** The test machine: 52 bits physical, 57 virtual (Verified).
- **Hint 2:** What happens to a mirror when ransomware encrypts a file?

---

### Task 7 — Fix the MMU walkthrough

**Goal:** correct a wrong description of address translation.

Sam Archer wrote:

> "The CPU sends the physical address to the TLB. On a TLB miss there is always a page fault, and the OS reads the page from disk. The MMU then adds the frame number to the offset, and the offset is converted to the frame's offset."

Find **four** errors and rewrite the description correctly, following slide 22.

**Expected result:** four corrections: virtual not physical; a TLB miss goes to the page table first; not every page fault reads the disk; the offset is unchanged and combined with the frame number, not added to it.

- **Hint 1:** Lecture section 13's flowchart.
- **Hint 2:** Real evidence: 25,600 page faults, 0 from disk (Verified).

---

### Task 8 — Fix the paging and segmentation table

**Goal:** apply slide 25.

A student's table has **five** errors. Find and correct them.

| | Paging | Segmentation |
| --- | --- | --- |
| Block size | Variable | Fixed |
| Address | Segment number + offset | Page number + offset |
| Table holds | Base and limit | Frame number |
| Fragmentation | External | Internal |
| Main strength | Logical protection and sharing | No external fragmentation |

**Expected result:** every row is swapped; the correct version is in lecture section 14.1.

- **Hint 1:** Paging = fixed pages.
- **Hint 2:** Internal = wasted space *inside* a block.

---

### Task 9 — Fix the RAID decisions

**Goal:** apply slides 36–37.

Correct each decision and justify it.

1. "For our accounts server we chose RAID 0 for safety."
2. "With four drives, RAID 0+1 and RAID 10 are equally resilient."
3. "We have RAID 5 across 4 drives, so we can lose any two drives."
4. "Our NAS mirrors to a second drive, so ransomware can't hurt us."

**Expected result:** RAID 0 has no redundancy; RAID 10 survives 4/6 two-drive failures versus 2/6 for RAID 0+1 (Verified); RAID 5 survives one failure; RAID is not a backup.

- **Hint 1:** Run `raid_sim.py` (Task 14).
- **Hint 2:** Slide 37's last line.

---

### Task 10 — Fix the decoder reasoning

**Goal:** apply slides 18–20.

1. "A 4-to-16 decoder has 4 outputs." Correct this.
2. "To select one of 64 locations you need a 64-to-6 decoder." Correct this.
3. "Row/column decoding uses more select lines than one big decoder." Check this for 16 locations and for 1,024 locations.

**Expected result:**

1. It has 16 outputs.
2. You need a 6-to-64 decoder (6 address bits).
3. Wrong: for 16 locations, 8 lines versus 16; for 1,024 locations, 64 lines versus 1,024.

- **Hint 1:** n inputs give 2ⁿ outputs.
- **Hint 2:** 1,024 locations = 32 × 32 grid, using two 5-to-32 decoders.

---

## Part C — Measure and model (Tasks 11–15)

### Task 11 — Model the MMU and TLB

**Goal:** follow addresses through a TLB and page table (slides 21–23).

**Skill you gain:** you can model a hardware mechanism in code and test your understanding against it. Engineers use this approach to explore designs before building them.

1. Save as `vmem_sim.py`:

```python
# vmem_sim.py - follow virtual addresses through a TLB and page table, like the MMU (slides 21-23).
#   virtual address = [ page number | offset ]   with 4 KiB pages: offset = low 12 bits (3 hex digits)
#   TLB hit   -> frame number + unchanged offset
#   TLB miss  -> look in the page table; if the page is present, update the TLB
#   not present -> PAGE FAULT: the OS maps a frame (here: the next free one) and the access is retried
#
# Usage: python vmem_sim.py

PAGE_SIZE = 4096                     # 4 KiB = 2^12, so the offset is 12 bits
OFFSET_BITS = 12
TLB_SIZE = 2                         # a tiny TLB so misses are easy to see

page_table = {0x00400: 0x0A1, 0x00401: 0x0A2, 0x7FFF0: 0x013}   # page -> frame (present pages)
tlb = {}                             # page -> frame, holds at most TLB_SIZE entries
tlb_order = []                       # oldest first, for replacement
next_free_frame = 0x200
stats = {"hit": 0, "miss": 0, "fault": 0}


def translate(vaddr):
    global next_free_frame
    page, offset = vaddr >> OFFSET_BITS, vaddr & (PAGE_SIZE - 1)
    line = f"0x{vaddr:08X} = page 0x{page:05X} | offset 0x{offset:03X}  ->  "
    if page in tlb:
        stats["hit"] += 1
        frame = tlb[page]
        line += "TLB hit"
    else:
        stats["miss"] += 1
        if page in page_table:
            frame = page_table[page]
            line += "TLB miss, page table gives frame"
        else:
            stats["fault"] += 1
            frame = next_free_frame
            next_free_frame += 1
            page_table[page] = frame
            line += "TLB miss, PAGE FAULT: OS maps new frame"
        if len(tlb) >= TLB_SIZE:                 # replace the oldest TLB entry
            del tlb[tlb_order.pop(0)]
        tlb[page] = frame
        tlb_order.append(page)
    paddr = (frame << OFFSET_BITS) | offset
    print(f"{line:<88} 0x{frame:03X} -> physical 0x{paddr:06X}")
    return paddr


if __name__ == "__main__":
    for va in (0x00400010, 0x00400FFC, 0x00401004, 0x7FFF0ABC, 0x00400020, 0x570F517D, 0x570F5180):
        translate(va)
    print(f"\nTLB hits {stats['hit']}, misses {stats['miss']}, page faults {stats['fault']}")
```

2. Run `python vmem_sim.py`. *What it does:* simulates the MMU for a list of addresses; it does not touch real memory. Actual output (Verified):

```text
0x00400010 = page 0x00400 | offset 0x010  ->  TLB miss, page table gives frame           0x0A1 -> physical 0x0A1010
0x00400FFC = page 0x00400 | offset 0xFFC  ->  TLB hit                                    0x0A1 -> physical 0x0A1FFC
0x00401004 = page 0x00401 | offset 0x004  ->  TLB miss, page table gives frame           0x0A2 -> physical 0x0A2004
0x7FFF0ABC = page 0x7FFF0 | offset 0xABC  ->  TLB miss, page table gives frame           0x013 -> physical 0x013ABC
0x00400020 = page 0x00400 | offset 0x020  ->  TLB miss, page table gives frame           0x0A1 -> physical 0x0A1020
0x570F517D = page 0x570F5 | offset 0x17D  ->  TLB miss, PAGE FAULT: OS maps new frame    0x200 -> physical 0x20017D
0x570F5180 = page 0x570F5 | offset 0x180  ->  TLB hit                                    0x200 -> physical 0x200180

TLB hits 2, misses 5, page faults 1
```

3. Explain why the 5th access (0x00400020) **missed** the TLB, even though page 0x00400 was used before.
4. Change `TLB_SIZE` to 4 and run again. How many hits, misses and faults are there now?
5. **Extend:** add a "read-only" set of pages. Make a write to such a page print `PROTECTION FAULT` instead of translating it.

**Expected result:** with `TLB_SIZE = 4`: 3 hits, 4 misses, 1 fault (Verified).

- **Hint 1:** The 2-entry TLB was refilled by pages 0x00401 and 0x7FFF0 in between.
- **Hint 2:** For step 5, add a `write=False` parameter to `translate`.

---

### Task 12 — Measure the hierarchy and locality (optional C)

**Goal:** see slides 8 and 15 as real numbers.

**Skill you gain:** you can measure performance experimentally instead of guessing. This is how engineers find real bottlenecks.

**Only if you already have gcc** (Linux, WSL or macOS). Otherwise, analyse the real outputs below.

1. Save `latency.c`:

```c
/* latency.c - measure average memory access time for different working-set sizes.
   It follows a random chain of pointers through a buffer (so the CPU cannot predict
   the next address). Small buffers fit in L1/L2/L3 cache; large ones must come from DRAM.
   Compile: gcc -O2 latency.c -o latency      Run: ./latency */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

static double now(void) { struct timespec t; clock_gettime(CLOCK_MONOTONIC, &t); return t.tv_sec + t.tv_nsec / 1e9; }

int main(void) {
    size_t sizes_kib[] = {16, 32, 256, 1024, 8192, 65536, 262144, 1048576};
    for (int s = 0; s < 8; s++) {
        size_t n = sizes_kib[s] * 1024 / sizeof(void *);
        void **buf = malloc(n * sizeof(void *));
        size_t *order = malloc(n * sizeof(size_t));
        for (size_t i = 0; i < n; i++) order[i] = i;
        srand(42);
        for (size_t i = n - 1; i > 0; i--) { size_t j = (size_t)rand() % (i + 1); size_t t = order[i]; order[i] = order[j]; order[j] = t; }
        for (size_t i = 0; i < n; i++) buf[order[i]] = &buf[order[(i + 1) % n]];   /* one big random cycle */
        void **p = &buf[order[0]];
        size_t steps = 20000000;
        double t0 = now();
        for (size_t i = 0; i < steps; i++) p = (void **)*p;
        double t1 = now();
        printf("%8zu KiB  %6.1f ns per access%s\n", sizes_kib[s], (t1 - t0) / steps * 1e9, p == NULL ? "!" : "");
        free(buf); free(order);
    }
    return 0;
}
```

2. Save `locality.c`:

```c
/* locality.c - spatial locality in action: add up the same 4096 x 4096 array of ints twice.
   Row by row visits neighbouring addresses (good spatial locality, one 64-byte cache line
   serves 16 ints). Column by column jumps 16 KiB each step (poor spatial locality).
   Compile: gcc -O1 locality.c -o locality      Run: ./locality */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 4096
static double now(void) { struct timespec t; clock_gettime(CLOCK_MONOTONIC, &t); return t.tv_sec + t.tv_nsec / 1e9; }
int main(void) {
    int *a = malloc((size_t)N * N * sizeof(int));
    for (size_t i = 0; i < (size_t)N * N; i++) a[i] = 1;
    long sum; double t0, t1;
    sum = 0; t0 = now();
    for (int r = 0; r < N; r++) for (int c = 0; c < N; c++) sum += a[(size_t)r * N + c];
    t1 = now(); printf("row by row:       sum %ld in %6.1f ms\n", sum, (t1 - t0) * 1000);
    sum = 0; t0 = now();
    for (int c = 0; c < N; c++) for (int r = 0; r < N; r++) sum += a[(size_t)r * N + c];
    t1 = now(); printf("column by column: sum %ld in %6.1f ms\n", sum, (t1 - t0) * 1000);
    free(a); return 0;
}
```

3. Compile and run: `gcc -O2 latency.c -o latency && ./latency`, then `gcc -O1 locality.c -o locality && ./locality`.

Real outputs (Verified):

```text
      16 KiB     1.9 ns per access
      32 KiB     2.1 ns per access
     256 KiB     5.7 ns per access
    1024 KiB     9.5 ns per access
    8192 KiB    35.2 ns per access
   65536 KiB   136.4 ns per access
  262144 KiB   154.1 ns per access
 1048576 KiB   174.5 ns per access
```

```text
row by row:       sum 16777216 in   12.4 ms
column by column: sum 16777216 in  166.9 ms
```

4. Where are the big jumps in `latency`? Match them to the L1 (48 KiB) and L2 (2 MiB) sizes.
5. How many times slower is the column-by-column traversal? Explain using cache lines.

**Expected result:** jumps after 32 KiB (L1) and after 1 MiB (L2); about 10–13× slower column-wise.

- **Hint 1:** Your own machine's numbers will differ, but the **shape** should be similar.
- **Hint 2:** One 64-byte line holds 16 ints.

---

### Task 13 — Watch page faults

**Goal:** see slide 21's page faults and Windows memory counters.

**Skill you gain:** you can observe virtual memory behaviour with real OS counters. This helps diagnose "out of memory" problems and spot suspicious memory use.

1. On Linux or macOS (optional), save and run `page_faults.py`:

```python
# page_faults.py - watch page faults happen when a program first touches new memory.
# The OS gives the program a range of VIRTUAL addresses at once, but only maps a physical
# frame to each page when that page is first used. Each first use causes a page fault that the
# OS resolves - usually by handing over a zero-filled frame, with NO disk access ("minor" fault).
# Linux/macOS only (uses the resource module). Read-only: it only allocates and frees its own memory.
#
# Usage: python3 page_faults.py

import mmap
import resource

PAGE = mmap.PAGESIZE
SIZE = 100 * 1024 * 1024                         # 100 MiB


def faults():
    r = resource.getrusage(resource.RUSAGE_SELF)
    return r.ru_minflt, r.ru_majflt


print(f"Page size: {PAGE} bytes;  100 MiB = {SIZE // PAGE} pages")
m = mmap.mmap(-1, SIZE)                          # reserve 100 MiB of virtual memory
min0, maj0 = faults()
print(f"After reserving 100 MiB:   minor faults so far {min0}, major {maj0}")
for offset in range(0, SIZE, PAGE):              # write one byte in every page
    m[offset] = 1
min1, maj1 = faults()
print(f"After touching every page: +{min1 - min0} minor faults, +{maj1 - maj0} major (disk) faults")
for offset in range(0, SIZE, PAGE):              # touch them all again
    m[offset] = 2
min2, maj2 = faults()
print(f"Touching them a second time: +{min2 - min1} minor faults (pages are now mapped)")
m.close()
```

Actual output (Verified):

```text
Page size: 4096 bytes;  100 MiB = 25600 pages
After reserving 100 MiB:   minor faults so far 1055, major 1
After touching every page: +25600 minor faults, +0 major (disk) faults
Touching them a second time: +0 minor faults (pages are now mapped)
```

2. On **Windows** (Expected), open **Task Manager > Performance > Memory**. Record:
   - **In use**;
   - **Available**;
   - **Committed**, shown as two numbers: x / y;
   - **Cached**;
   - **Paged pool** and **Non-paged pool**.
3. Open **Resource Monitor** (`resmon`) **> Memory**. Find the **Hard Faults/sec** column. Open a large program and watch it.
4. Explain why "Committed" is not the same as page-file use (slide 21).

**Expected result:** exactly one minor fault per page touched (25,600 for 100 MiB) and no disk faults (Verified). On Windows, hard faults rise briefly when a program starts.

- **Hint 1:** "Hard" faults on Windows roughly correspond to "major" faults (those that need storage).
- **Hint 2:** Committed is a promise backed by RAM **and/or** the page file.

---

### Task 14 — Rebuild a failed drive with parity

**Goal:** see why parity RAID survives one failure, and compare layouts.

**Skill you gain:** you can use XOR parity and reason about failure tolerance, the core of storage reliability planning.

1. Save as `raid_sim.py`:

```python
# raid_sim.py - see how RAID levels place blocks, use capacity, and survive drive failures (slides 36-37).
#   RAID 0  : striping, no redundancy
#   RAID 1  : mirroring
#   RAID 5  : striping with XOR parity (any ONE drive can fail)
#   RAID 10 : stripe of mirrors        RAID 0+1 : mirror of stripes
# Usage: python raid_sim.py

from itertools import combinations

# ---- 1. RAID 5 parity: XOR lets you rebuild any one missing block ----------------------------
d1, d2, d3 = 0b10110010, 0b01101100, 0b11100001          # three data bytes on three drives
parity = d1 ^ d2 ^ d3                                     # the parity byte on the fourth drive
print("RAID 5 parity (XOR):")
print(f"  drive 1 {d1:08b}\n  drive 2 {d2:08b}\n  drive 3 {d3:08b}\n  parity  {parity:08b}")
rebuilt = d1 ^ d3 ^ parity                                # drive 2 has failed
print(f"  drive 2 fails -> rebuild = d1 XOR d3 XOR parity = {rebuilt:08b}  (matches: {rebuilt == d2})")

# ---- 2. Usable capacity ---------------------------------------------------------------------
def usable(level, n, size_tb):
    return {"RAID 0": n * size_tb, "RAID 1": size_tb, "RAID 5": (n - 1) * size_tb,
            "RAID 10": n * size_tb / 2, "RAID 0+1": n * size_tb / 2}[level]

print("\nUsable capacity with 4 drives of 2 TB (8 TB raw):")
for level in ("RAID 0", "RAID 1", "RAID 5", "RAID 10", "RAID 0+1"):
    print(f"  {level:<9} {usable(level, 4, 2):>4g} TB")
print("  (RAID 1 shown as one 4-way mirror; a 2-drive mirror of 2 TB drives also gives 2 TB)")

# ---- 3. Which two-drive failures does each 4-drive layout survive? ---------------------------
# Drives 1-4. Slide 37's layouts:
#   RAID 10  : mirror pairs {1,2} and {3,4}; data survives if each pair keeps at least one drive
#   RAID 0+1 : stripe sets {1,2} and {3,4} mirrored; data survives if at least one whole set is intact
#   RAID 5   : survives any single failure only
def survives(level, failed):
    pairs = ({1, 2}, {3, 4})
    if level == "RAID 10":
        return all(p - failed for p in pairs)
    if level == "RAID 0+1":
        return any(not (p & failed) for p in pairs)
    if level == "RAID 5":
        return len(failed) <= 1
    if level == "RAID 0":
        return len(failed) == 0

print("\nTwo drives fail at once (6 possible pairs out of 4 drives):")
for level in ("RAID 0", "RAID 5", "RAID 0+1", "RAID 10"):
    ok = [f"{a}+{b}" for a, b in combinations(range(1, 5), 2) if survives(level, {a, b})]
    print(f"  {level:<9} survives {len(ok)}/6: {', '.join(ok) or 'none'}")
print("\nRemember: RAID protects against some DRIVE failures. It is not a backup - deletion,")
print("ransomware and corruption are copied to every mirror instantly.")
```

2. Run `python raid_sim.py`. Actual output (Verified):

```text
RAID 5 parity (XOR):
  drive 1 10110010
  drive 2 01101100
  drive 3 11100001
  parity  00111111
  drive 2 fails -> rebuild = d1 XOR d3 XOR parity = 01101100  (matches: True)

Usable capacity with 4 drives of 2 TB (8 TB raw):
  RAID 0       8 TB
  RAID 1       2 TB
  RAID 5       6 TB
  RAID 10      4 TB
  RAID 0+1     4 TB
  (RAID 1 shown as one 4-way mirror; a 2-drive mirror of 2 TB drives also gives 2 TB)

Two drives fail at once (6 possible pairs out of 4 drives):
  RAID 0    survives 0/6: none
  RAID 5    survives 0/6: none
  RAID 0+1  survives 2/6: 1+2, 3+4
  RAID 10   survives 4/6: 1+3, 1+4, 2+3, 2+4

Remember: RAID protects against some DRIVE failures. It is not a backup - deletion,
ransomware and corruption are copied to every mirror instantly.
```

3. Change `d1, d2, d3` to three bytes of your own, and rebuild drive **1** instead of drive 2.
4. Why can RAID 5 **not** rebuild when two drives fail? Use XOR to explain.
5. **Extend:** add RAID 6 to `usable()` (n − 2 drives of capacity) and to `survives()` (any two failures).

**Expected result:** your rebuild matches. With two unknowns there is only one equation, so XOR cannot recover both.

- **Hint 1:** a XOR b XOR b = a.
- **Hint 2:** For RAID 6, `return len(failed) <= 2`.

---

### Task 15 — Inventory your own memory and storage

**Goal:** connect the lecture to your own hardware.

**Skill you gain:** you can produce a hardware inventory from built-in tools. This is basic asset management and a step in incident response.

On your own Windows computer (Expected; read-only, no administrator rights needed):

1. **Task Manager > Performance > CPU**: record the L1, L2 and L3 cache sizes.
2. **Task Manager > Performance > Memory**: record total RAM, speed, **slots used**, and form factor.
3. PowerShell:

   ```powershell
   Get-CimInstance Win32_PhysicalMemory | Select-Object Manufacturer, Capacity, Speed
   Get-PhysicalDisk | Select-Object FriendlyName, MediaType, Size
   ```

   *What they do:* list your RAM modules and your physical disks. Nothing is changed.
4. Fill in this table, and say whether your disk is an **SSD** or an **HDD**:

   | Level | Your value |
   | --- | --- |
   | L1 / L2 / L3 | |
   | RAM total (modules × size) | |
   | Disk type and size | |

5. Compare with the test machine (lecture section 7.2). Which level is the biggest difference?

**Expected result:** a completed inventory. Most modern laptops have an SSD (MediaType `SSD`).

- **Hint 1:** Capacity is in bytes. Divide by 1,073,741,824 to get GiB.
- **Hint 2:** Slide 17's example: 64 GB = 8 × 8 GB modules.

---

## Part D — Official written practice and integration (Tasks 16–20)

### Task 16 — Knowledge check and hierarchy (Official Questions 1 and 2)

**Goal:** answer official Questions 1 and 2 independently.

**Question 1 — Quick knowledge check (official).** Choose one answer (A, B, C or D) for each.

- **(a)** A program accesses one array element, then several elements next to it. This is an example of:
  - A. temporal locality
  - B. spatial locality
  - C. virtualisation
  - D. mirroring
- **(b)** Which description best fits DRAM?
  - A. needs regular refresh
  - B. stores data on spinning platters
  - C. is always non-volatile
  - D. is used only for firmware
- **(c)** The processor does not find a requested translation in the TLB. What is the most appropriate next step?
  - A. delete the file
  - B. consult the page table
  - C. reboot the system
  - D. format the drive
- **(d)** A firmware update is retained after a PC is switched off because its code is commonly stored in:
  - A. CPU registers
  - B. volatile cache
  - C. rewritable flash
  - D. ordinary DRAM

**Question 2 — Organising the memory hierarchy (official).**

- **(a)** Arrange from fastest/closest to the CPU to slowest/furthest: SSD, L2 cache, main memory (DRAM), CPU registers and L1 cache.
- **(b)** Give three reasons why a modern computer uses several memory levels rather than building all storage from its fastest technology.

**Expected result:** four letters and a correct order, plus three reasons (speed, cost, capacity).

- **Hint 1:** Lecture sections 7, 9, 10, 13 and 15.
- **Hint 2:** Do not look at the solution sheet until you have written your own answers.

---

### Task 17 — Registers, cache, RAM and virtual memory (Official Questions 3 and 4)

**Goal:** answer official Questions 3 and 4 in full sentences.

**Question 3 — Registers, cache and main memory (official).**

- **(a)** A CPU is executing an instruction. Explain one typical role of a register and one typical role of the cache.
- **(b)** Why is SRAM commonly suitable for CPU caches while DRAM is commonly suitable for main memory? Refer to speed and to cost or density.
- **(c)** A small set of instructions is executed repeatedly. Explain how temporal locality may make a cache useful.

**Question 4 — Following a virtual-memory access (official).** A running application uses virtual addresses. The processor generates a virtual address containing a page number and an offset.

- **(a)** The required translation is already in the TLB. Explain how the MMU obtains the physical address.
- **(b)** The translation is not in the TLB, but the page is mapped to a physical frame. What should happen next?
- **(c)** Later, the application causes a valid page fault. Describe one action the OS might take, and explain why a page fault does not always require disk access.

**Expected result:** answers that use the terms frame number, unchanged offset, page table, TLB update, and minor versus disk-backed faults.

- **Hint 1:** Task 11's simulation shows (a) and (b) happening.
- **Hint 2:** Task 13's real output is evidence for (c).

---

### Task 18 — Two ways to organise memory (Official Question 5)

**Goal:** answer official Question 5.

Scheme A divides virtual memory into equal-sized blocks. Scheme B treats a program as variable-sized logical regions.

- **(a)** Identify the memory-management technique used by Scheme A and by Scheme B.
- **(b)** For Scheme A, explain how a page table is used when the CPU accesses a virtual address. Include the purpose of the offset.
- **(c)** A fixed-size block has some unused space; another system develops gaps between variable-sized allocations. Name the type of fragmentation in each case.

**Expected result:** paging and segmentation; page number → frame, offset unchanged; internal and external fragmentation.

- **Hint 1:** Lecture section 14.
- **Hint 2:** Use the worked example: 10,000 bytes in 4 KiB pages wastes 2,288 bytes.

---

### Task 19 — Mini-project: storage and backup plan for a small office

**Goal:** design storage that balances performance, capacity, availability and **real** backups.

**Skill you gain:** you can justify a storage design with calculations and explain why RAID and backups solve different problems, as an IT administrator must.

**Brief.** A 12-person design studio needs:

- **8 TB** of usable shared project storage, growing about 2 TB per year;
- protection against a single drive failure **and** against accidental deletion or ransomware;
- staff access from their PCs over the office LAN.

Steps:

1. **Deployment:** DAS, NAS or SAN? Justify using slides 38–39.
2. **RAID choice:** compare RAID 1, 5, 6 and 10 for 4 TB drives. Use `raid_sim.py`-style calculations to find how many drives each needs for at least 8 TB usable (plus growth), and what failures each survives.
3. **Backups:** design a backup that covers what RAID does not. Include:
   - an **offline or off-site** copy, using slide 30's tape **or** a cloud service;
   - how often to back up;
   - a test **restore**.

   (The "3-2-1" rule is Extra: 3 copies, 2 media types, 1 off-site.)
4. **Security:** who can access the NAS? How will you protect backups from the same ransomware?
5. **Justify** in 200 words, linking each choice to a requirement (Lecture 12, slide 15's decision rule).

**Decision table**

| Option | Drives × 4 TB | Usable TB | Survives | Cost/complexity | Choose? |
| --- | --- | --- | --- | --- | --- |
| RAID 5 | | | | | |
| RAID 6 | | | | | |
| RAID 10 | | | | | |

- **Hint 1:** RAID 5 with 4 × 4 TB gives 12 TB.
- **Hint 2:** A backup must be **separate** from the system it protects.

---

### Task 20 — Assessment-style practice: memory and storage

**This is practice only, not a real exam question.** The module exam is two hours with short-answer and essay-style questions covering architecture, operating systems and networking. The report covers data storage and networking (module guide). Marks are invented for planning.

**Rules:** 25 minutes, closed book, write it yourself.

**(a)** Explain why computers use a memory hierarchy rather than a single type of memory. *(4 marks)*

**(b)** Distinguish temporal and spatial locality, with one example of each. *(4 marks)*

**(c)** A virtual address 0x0040ABCD is accessed on a system with 4 KiB pages. Give the page number and offset, and explain what the MMU does if the translation is not in the TLB but the page is present. *(5 marks)*

**(d)** A company stores its customer database on a server with RAID 1. The manager says "we are fully protected against data loss". Evaluate this claim, referring to RAID levels, backups and at least one realistic threat. *(7 marks; aim for 200–300 words)*

**Self-marking checklist**

| Part | A good answer includes | Expected | Actual |
| --- | --- | --- | --- |
| (a) | No single technology is fast, large and cheap; levels from registers to SSD; average speed close to the fast levels at low cost | 4 points | |
| (b) | Definitions plus examples (loop reuse; sequential array access) | 4 points | |
| (c) | Page **0x0040A**, offset **0xBCD**; page-table lookup, TLB update, frame + unchanged offset | 5 points | |
| (d) | RAID 1 survives one drive failure; it does not protect against deletion, ransomware, corruption, fire or theft; independent offline/off-site backups; tested restores; conclusion | 7 points | |
| Time | Within 25 minutes | Yes | |

- **Hint 1:** For (c), the offset is the last 3 hex digits.
- **Hint 2:** Lecture sections 7, 9, 13 and 17.

---

## Tracker

| Task | Name | Done | Notes / score |
| --- | --- | --- | --- |
| 1 | Classify the memory | ☐ | /8 |
| 2 | Order the hierarchy | ☐ | |
| 3 | Temporal or spatial? | ☐ | /6 |
| 4 | Split virtual addresses | ☐ | /5 |
| 5 | RAID capacity | ☐ | /4 |
| 6 | Fix the myths | ☐ | /7 |
| 7 | Fix the MMU walkthrough | ☐ | /4 |
| 8 | Fix the paging table | ☐ | /5 |
| 9 | Fix the RAID decisions | ☐ | /4 |
| 10 | Fix the decoder reasoning | ☐ | /3 |
| 11 | `vmem_sim.py` | ☐ | |
| 12 | Measure latency and locality | ☐ | |
| 13 | Page faults | ☐ | |
| 14 | `raid_sim.py` | ☐ | |
| 15 | Own inventory | ☐ | |
| 16 | **Official Q1–Q2** | ☐ | /4 + |
| 17 | **Official Q3–Q4** | ☐ | |
| 18 | **Official Q5** | ☐ | |
| 19 | Mini-project: storage plan | ☐ | |
| 20 | Assessment-style practice | ☐ | /20 |

## Reflection

1. Which real measurement in this lab surprised you most, and why?
2. In your own words, why does a page fault not always mean the disk is used?
3. How would you explain "RAID is not a backup" to a non-technical manager?
4. Which part of this topic do you expect to use in the data storage parts of your coursework?

---

## Answer key

**(Verified)** = Linux VM, gcc 13.3, Python 3.13. **(Expected)** = Windows tools. **Official Questions 1–5:** these model answers agree with the official solution sheet; check your own answers against that sheet too.

### Task 1

| Item | Classification |
| --- | --- |
| Register, L2 cache, DRAM | Volatile, primary |
| Firmware flash | Non-volatile, primary-addressable in some systems (the overlap) |
| SSD, HDD, tape, microSD | Non-volatile, secondary |

### Task 2 (Verified sizes)

1. Registers → L1 → L2 → L3 → main memory → SSD.
2. Sizes as in the expected result.
3. **Speed:** registers and caches are very fast for frequently needed data. **Cost:** fast memory is expensive per bit. **Capacity:** slower technologies are much larger and cheaper.

### Task 3

T, S, T, S, both. Item 6 fails to use **spatial** locality.

### Task 4 (Verified)

| Virtual address | Page number | Offset |
| --- | --- | --- |
| 0x00403A2C | 0x00403 | 0xA2C |
| 0x7FFE1004 | 0x7FFE1 | 0x004 |
| 0x12345678 | 0x12345 | 0x678 |
| 0x0000FFFF | 0x0000F | 0xFFF |

With 8 KiB pages, 0x12345678 has page **0x91A2** and offset **0x1678**. 13 bits is not a whole number of hex digits, so the boundary falls inside a digit.

### Task 5

| Level | Usable TB | Failures always survived |
| --- | --- | --- |
| RAID 0 | 24 | 0 |
| RAID 5 | 20 | 1 |
| RAID 6 | 16 | 2 |
| RAID 10 | 12 | 1 (up to 3 if each failure is in a different pair) |

### Task 6

1. Non-volatile means it survives power-off; the data can still change (slide 7).
2. Firmware flash is primary-addressable but non-volatile (slides 7 and 10).
3. Registers use specialised cells (slide 16).
4. The physical address width is implementation-specific, e.g. 52 bits (slide 19; Verified).
5. SSDs have no moving parts (slide 27).
6. Committed is a commitment backed by RAM and/or the page file (slide 21).
7. RAID is not a backup (slide 36).

### Task 7

**Errors:**

1. The CPU produces a **virtual** address.
2. A TLB miss means **consulting the page table**; a fault happens only if the page is not present.
3. A page fault **may or may not** read the disk.
4. The frame number is **combined** with the **unchanged** offset.

**Correct:** the CPU produces page | offset. The MMU checks the TLB; on a hit it uses frame | offset. On a miss it reads the page table and updates the TLB. If the page is not present, the OS resolves a page fault (possibly without disk access) and resumes the instruction.

### Task 8

| | Paging | Segmentation |
| --- | --- | --- |
| Block size | Fixed | Variable |
| Address | Page number + offset | Segment number + offset |
| Table holds | Frame number | Base and limit |
| Fragmentation | Internal | External |
| Main strength | No external fragmentation | Logical protection and sharing |

### Task 9 (Verified with `raid_sim.py`)

1. RAID 0 has no redundancy. Use RAID 1, 5, 6 or 10, **and** backups.
2. RAID 10 survives 4 of 6 two-drive failures; RAID 0+1 survives 2 of 6.
3. RAID 5 survives only one failure.
4. Ransomware encrypts the files, and the mirror copies the change instantly. Keep independent, offline backups.

### Task 10

1. 16 outputs.
2. A 6-to-64 decoder.
3. Wrong: 8 lines versus 16, and 64 versus 1,024.

### Task 11 (Verified)

3. The 2-entry TLB was refilled by pages 0x00401 and 0x7FFF0 in between, so page 0x00400 had been evicted.
4. With `TLB_SIZE = 4`: **3 hits, 4 misses, 1 fault**.
5. Model:

```python
READ_ONLY = {0x7FFF0}
def translate(vaddr, write=False):
    page = vaddr >> OFFSET_BITS
    if write and page in READ_ONLY:
        print(f"0x{vaddr:08X}: PROTECTION FAULT (write to read-only page)")
        return None
    # ... rest as before
```

### Task 12 (Verified)

- **Latency:** about 2 ns up to 32 KiB (within L1); about 6–10 ns at 256 KiB–1 MiB (L2); 35 ns at 8 MiB; 136–175 ns beyond that.
- **Locality:** 12.4 ms row-wise versus 166.9 ms column-wise, about **13×** slower (a second run gave about 10×).

### Task 13 (Verified on Linux; Windows Expected)

- **Linux:** 25,600 minor faults and 0 major faults, then 0 more on the second pass.
- **Windows:** your own values. Committed is not page-file use (slide 21).

### Task 14 (Verified)

4. With two drives missing there are two unknowns but only one XOR equation, so neither block can be recovered.
5. RAID 6 model:

```python
# in usable():  "RAID 6": (n - 2) * size_tb
# in survives(): if level == "RAID 6": return len(failed) <= 2
```

### Task 15 (Expected)

Your own values.

### Task 16 (official Q1–Q2)

**Q1:**

| Part | Answer |
| --- | --- |
| (a) | **B** |
| (b) | **A** |
| (c) | **B** |
| (d) | **C** |

**Q2:**

- **(a)** CPU registers → L1 cache → L2 cache → main memory (DRAM) → SSD.
- **(b)** Speed, cost and capacity, as in Task 2.

### Task 17 (official Q3–Q4, model answers)

**Q3:**

- **(a)** A register temporarily holds data, an address, an instruction or the processor state needed during execution. The cache holds copies of selected blocks from lower levels, so frequently needed instructions and data are reached faster.
- **(b)** SRAM is faster, which suits low-latency caches, but uses more silicon per bit and costs more. DRAM is denser and cheaper per bit, which suits large main memory.
- **(c)** Recently used instructions are likely to be used again. In a repeated loop their blocks stay in cache, so later passes are served from cache instead of main memory, improving the average access time.

**Q4:**

- **(a)** The MMU finds the frame number for the virtual page in the TLB and combines it with the unchanged offset to form the physical address. No page-table lookup is needed.
- **(b)** The MMU consults the page table. If the entry is valid and accessible, it adds the translation to the TLB and continues with the physical address. No page fault is needed.
- **(c)** The OS resolves the mapping, for example by loading the page from the page file or the original file. Not every fault needs disk access: the OS may supply a new zero-filled page (Verified: 25,600 minor faults, 0 disk faults). It then updates the mapping and resumes the instruction.

### Task 18 (official Q5, model answers)

- **(a)** Scheme A is **paging**; Scheme B is **segmentation**.
- **(b)** The virtual address is a page number plus an offset. The page table gives the frame number. The frame number is combined with the unchanged offset to form the physical address. The offset locates the byte within the page or frame, and stays the same because pages and frames are the same size.
- **(c)** Unused space inside a fixed block is **internal** fragmentation. Gaps between variable allocations are **external** fragmentation.

### Task 19

Your own design. For 8 TB usable now, with 4 TB drives:

| RAID level | Drives | Usable |
| --- | --- | --- |
| RAID 5 | 3 | 8 TB |
| RAID 6 | 4 | 8 TB |
| RAID 10 | 4 | 8 TB |
| RAID 1 | 2 | 4 TB (cannot meet 8 TB with this drive size) |

Plan for growth, and add an independent backup.

### Task 20

- **(c)** Page **0x0040A**, offset **0xBCD**.
- Other parts: see the checklist.
