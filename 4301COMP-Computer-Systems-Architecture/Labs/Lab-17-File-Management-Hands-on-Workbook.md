# Lab 17 — File Management Hands-on Workbook (20 Tasks)

**Module:** 4301COMP Computer Systems Architecture

**Session:** Teaching Week 10, Session A · **Matching lecture:** `../Lectures/Lecture-17-File-Management.md`

---

## How to use this lab

**What this lab is for.** You will:

- inspect real file **metadata** before and after an edit;
- compare **sequential** and **direct** access;
- follow **FAT cluster chains** and watch fragmentation happen;
- identify your file system and read your file **permissions** safely;
- practise a **safe recovery** of a lab file.

**Where the official tasks are.**

| Official lab sheet (TW10 Session A) | This workbook |
| --- | --- |
| Task 1 — Inspect file data and metadata | Task 16 |
| Task 2 — Compare access and file-system features | Task 17 |
| Extra Challenge — Test safe recovery of a lab file | Task 18 |

In the timetabled lab, **do Tasks 16–18 first**.

**Safety rules (official sheet):**

- Work only in **your own lab folder**, in Documents or approved university storage.
- Do **not** bypass blocked tools, elevate privileges, change permissions, take ownership or format drives.
- **Never use Shift+Delete**, and do not install recovery tools.
- If a feature is restricted, **record the restriction** instead of working around it.

**Tools**

| Tool | Used in | Notes |
| --- | --- | --- |
| File Explorer, Notepad, Word, Snipping Tool | Tasks 16–18 | Official tools |
| PowerShell (normal user) | Tasks 13, 14, 16–17 | Read-only commands only |
| Python 3 | Tasks 11–13 | **Optional, your choice.** Built-in modules only |
| Linux with `mkfs.fat`/`mtools` | Task 15 | **Optional:** only if you already have them; the real outputs are provided |

**Labels:**

- **Verified** = run before being written here. This includes a real FAT32 image, a real NTFS image, Python 3.13 and Linux `stat`.
- **Expected** = not run here (Windows tools).

---

## Part A — Warm-up (Tasks 1–5)

### Task 1 — Data or metadata?

**Goal:** apply slide 7.

Label each **D** (data) or **M** (metadata):

1. The sentence inside `sample.txt`
2. `sample.txt`'s size in bytes
3. The pixels of a screenshot
4. The date a photo was taken, stored inside the photo by the camera
5. A file's last-modified time
6. The file's NTFS permissions
7. The folder path of the file
8. The rows of a spreadsheet

**Expected result:** D = 1, 3 and 8; M = 2, 4, 5, 6 and 7.

- **Hint 1:** Metadata is information **about** the data.
- **Hint 2:** Item 4 is stored inside the file, but it still describes the picture (EXIF metadata).

---

### Task 2 — Overlapping categories

**Goal:** apply slide 5.

For each file, describe it as text or binary, executable or data, and structured or unstructured:

1. `notes.txt`
2. `budget.csv`
3. `holiday.jpg`
4. `setup.exe`
5. `backup.ps1` (a PowerShell script)
6. `Lab_Record.docx`

Why is "the three file types are text, binary and executable" wrong?

**Expected result:** six descriptions, with an explanation that the categories overlap. For example, `.ps1` is text **and** executable, and `.docx` is binary, structured and a ZIP container.

- **Hint 1:** A script is text that can be run.
- **Hint 2:** Lecture 15: `.docx` files start with `50 4B`.

---

### Task 3 — Offsets and access choices

**Goal:** use slides 12–13.

A file holds fixed-size **64-byte** records. The first record is at offset 0.

1. What is the byte offset of record 1?
2. What is the byte offset of record 500?
3. What is the byte offset of record 10,000?
4. How many bytes must a **sequential** search read to reach record 10,000, including that record?

Choose **sequential** or **direct** access for each workload:

5. Printing a whole log file
6. Fetching customer 48,213 by ID many times a minute
7. Calculating the total of every record
8. Jumping to the end of a video

**Expected result:** 0; 31,936; 639,936; 640,000 bytes; sequential; direct; sequential; direct.

- **Hint 1:** Offset = (n − 1) × record size.
- **Hint 2:** Repeated distant lookups favour direct access (slide 12).

---

### Task 4 — Follow FAT chains by hand

**Goal:** apply slide 22.

Here is a small FAT ("EOC" = end of chain, "BAD" = damaged, 0 = free):

| Cluster | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FAT entry | 3 | EOC | 9 | 0 | 7 | EOC | BAD | 10 | EOC | 0 | 0 |

Directory entries: `LOG.TXT` first cluster 2; `REPORT.DOC` first cluster 4; `NOTES.TXT` first cluster 6.

1. List each file's chain of clusters.
2. Which file is fragmented?
3. Which clusters are free?
4. Which cluster can never be used, and why?
5. A new 3-cluster file is written using the **lowest free clusters**. Which clusters does it get, and is it fragmented?

**Expected result:**

- LOG = 2, 3. REPORT = 4, 9, 10 (fragmented). NOTES = 6, 7.
- Free clusters: 5, 11 and 12. Cluster 8 is bad.
- The new file gets 5, 11 and 12, so it is fragmented.

- **Hint 1:** Start from the directory entry's first cluster, then keep reading the FAT.
- **Hint 2:** "Not consecutive" means fragmented.

---

### Task 5 — Choose a file system

**Goal:** apply slides 19 and 30–32.

Choose FAT32, exFAT or NTFS and give one reason for each:

1. The Windows C: drive
2. A USB stick for an old car stereo that only reads FAT32
3. A USB drive carrying 12 GB video files between Windows and macOS
4. A shared office drive where each person may only open their own folder
5. A 2 GB SD card for a simple sensor logger
6. A drive where metadata consistency after power cuts matters

**Expected result:** NTFS; FAT32; exFAT; NTFS (ACLs); FAT32 (or exFAT if supported); NTFS (journalling).

- **Hint 1:** FAT32's single-file limit is 4 GiB − 1 byte.
- **Hint 2:** Permissions need ACLs.

---

## Part B — Find and fix (Tasks 6–10)

### Task 6 — Fix the myths

**Goal:** correct statements using the slides.

Each statement is wrong. Correct it and cite the slide.

1. "Binary files are always faster than text files."
2. "My SSD should be defragmented every week."
3. "When I delete a file on a FAT USB stick, its data is erased."
4. "The second FAT copy guarantees I can recover a corrupted volume."
5. "NTFS volumes are limited to 2 TB."
6. "FAT32 supports per-user permissions like NTFS."
7. "NTFS journalling means I don't need backups."

**Expected result:** seven corrections, citing slides 10, 14, 25, 23, 31, 26 and 27/32.

- **Hint 1:** The real FAT image kept "Secret proje…" after deletion (lecture section 13.2).
- **Hint 2:** The journal covers **metadata**.

---

### Task 7 — Fix the chain reading

**Goal:** correct FAT reasoning errors.

Using Task 4's FAT, Sam Archer wrote:

> "REPORT.DOC starts at cluster 4, so its clusters are 4, 5 and 6. Cluster 8 says BAD, so the file stored there is corrupted. NOTES.TXT ends at cluster 6, because 6 is listed in the directory."

Find **three** errors and correct them.

**Expected result:** the chain is 4 → 9 → 10, not consecutive; BAD marks a damaged cluster, which no file uses; NOTES **starts** at 6 and ends at 7 (EOC).

- **Hint 1:** Never assume clusters are consecutive. Follow the entries.
- **Hint 2:** The directory gives the **first** cluster only.

---

### Task 8 — Fix the maintenance policy

**Goal:** apply slide 14.

An IT policy says:

> "All computers will run a full defragmentation every Monday at 9 am on every drive, including SSDs and USB sticks, using a third-party defragmenter installed on each machine."

Rewrite the policy correctly, with reasons.

**Expected result:**

- Use Windows' **Optimize Drives**, which is media-aware: defragment HDDs, retrim SSDs.
- Do not routinely defragment SSDs.
- Do not install extra tools without need.
- Schedule maintenance outside working hours.

- **Hint 1:** Slide 14's last bullet.
- **Hint 2:** Lecture section 10.2 explains TRIM.

---

### Task 9 — Fix the protection claims

**Goal:** separate the four protection layers (lecture section 16).

Each claim is wrong. Correct it.

1. "Our file server uses RAID 1, so deleted files can be recovered."
2. "The NTFS journal will bring back the report I overwrote."
3. "The Recycle Bin always catches deleted files, even on network drives."
4. "We back up to a USB drive that stays plugged in, so ransomware can't hurt our backups."

**Expected result:** four corrections, covering RAID, journalling, the Recycle Bin and backup independence.

- **Hint 1:** Which layer protects against **deletion**?
- **Hint 2:** A connected backup can be encrypted along with everything else.

---

### Task 10 — Fix the lab record

**Goal:** check evidence claims (as in Lecture 10).

A student's lab record says:

1. "After editing sample.txt, the Created time changed, which proves the file was recreated."
2. "Ctrl+F found Record08 instantly, which proves Notepad used direct disk access."
3. "The ZIP was smaller, so I have turned on NTFS compression."
4. "The Security tab was unavailable, so I took ownership of the file to see the permissions."

Explain what is wrong with each, and what should have been written or done.

**Expected result:**

1. Creation and modification are separate. If Created really changed, record it as an observation, but check whether the editor saved by replacing the file.
2. Ctrl+F may scan the contents (official sheet).
3. ZIP creates a separate archive; it is not NTFS compression (official sheet).
4. The student should have recorded the limitation; taking ownership is forbidden (official sheet).

- **Hint 1:** Some editors save by writing a new file and renaming it, which can change creation metadata. Record what you see.
- **Hint 2:** All four points are on the official sheet.

---

## Part C — Build and observe (Tasks 11–15)

### Task 11 — Simulate FAT allocation, deletion and defragmentation

**Goal:** see slides 14 and 22–25 happen step by step.

**Skill you gain:** you can model how a file system allocates space. This is the basis of understanding fragmentation, slack and deleted-file recovery in digital forensics.

1. Save as `fat_sim.py`:

```python
# fat_sim.py - a small FAT model: allocate files as cluster chains, delete, fragment and defragment.
# It follows slide 22's rules: one FAT entry per cluster; 0 = free; EOC = end of chain;
# any other number = the next cluster. A directory maps each file name to its FIRST cluster.
# Works on any computer (built-in Python only); nothing touches a real disk.
#
# Usage: python fat_sim.py

EOC = "EOC"
CLUSTERS = 16                                   # a tiny volume: clusters 2..17 hold data
fat = {c: 0 for c in range(2, 2 + CLUSTERS)}    # 0 means free
directory = {}                                  # name -> first cluster
deleted = {}                                    # name -> first cluster (marked deleted, like 0xE5)


def allocate(name, n_clusters):
    free = [c for c in sorted(fat) if fat[c] == 0][:n_clusters]   # first free clusters, in order
    if len(free) < n_clusters:
        print(f"  cannot store {name}: disk full")
        return
    for a, b in zip(free, free[1:]):
        fat[a] = b                              # each cluster points to the next
    fat[free[-1]] = EOC
    directory[name] = free[0]


def chain(first):
    out = [first]
    while fat[out[-1]] != EOC:
        out.append(fat[out[-1]])
    return out


def delete(name):
    first = directory.pop(name)
    for c in chain(first):
        fat[c] = 0                              # clusters become free; their DATA is not erased
    deleted[name] = first


def defragment():
    """Rewrite every file so its clusters are consecutive, starting at cluster 2."""
    files = {name: len(chain(first)) for name, first in directory.items()}
    for c in fat:
        fat[c] = 0
    directory.clear()
    for name, n in files.items():
        allocate(name, n)


def show(title):
    print(f"\n{title}")
    print("  FAT:  " + "  ".join(f"{c}:{fat[c]}" for c in fat))
    for name, first in directory.items():
        cl = chain(first)
        frag = "contiguous" if all(b == a + 1 for a, b in zip(cl, cl[1:])) else "FRAGMENTED"
        print(f"  {name:<6} first cluster {first:>2}  chain {cl}  {frag}")


if __name__ == "__main__":
    allocate("A", 3); allocate("B", 2); allocate("C", 3); allocate("E", 4)
    show("1. Four files written one after another")
    delete("B"); delete("E")
    show("2. B and E deleted: their clusters are free (data still on disk until reused)")
    allocate("D", 5)
    show("3. New 5-cluster file D fills B's gap first, then the rest: fragmented")
    defragment()
    show("4. After defragmentation every file is contiguous")
```

2. Run `python fat_sim.py`. *What it does:* models a 16-cluster FAT volume in memory; no real disk is used. Actual output (Verified):

```text

1. Four files written one after another
  FAT:  2:3  3:4  4:EOC  5:6  6:EOC  7:8  8:9  9:EOC  10:11  11:12  12:13  13:EOC  14:0  15:0  16:0  17:0
  A      first cluster  2  chain [2, 3, 4]  contiguous
  B      first cluster  5  chain [5, 6]  contiguous
  C      first cluster  7  chain [7, 8, 9]  contiguous
  E      first cluster 10  chain [10, 11, 12, 13]  contiguous

2. B and E deleted: their clusters are free (data still on disk until reused)
  FAT:  2:3  3:4  4:EOC  5:0  6:0  7:8  8:9  9:EOC  10:0  11:0  12:0  13:0  14:0  15:0  16:0  17:0
  A      first cluster  2  chain [2, 3, 4]  contiguous
  C      first cluster  7  chain [7, 8, 9]  contiguous

3. New 5-cluster file D fills B's gap first, then the rest: fragmented
  FAT:  2:3  3:4  4:EOC  5:6  6:10  7:8  8:9  9:EOC  10:11  11:12  12:EOC  13:0  14:0  15:0  16:0  17:0
  A      first cluster  2  chain [2, 3, 4]  contiguous
  C      first cluster  7  chain [7, 8, 9]  contiguous
  D      first cluster  5  chain [5, 6, 10, 11, 12]  FRAGMENTED

4. After defragmentation every file is contiguous
  FAT:  2:3  3:4  4:EOC  5:6  6:7  7:EOC  8:9  9:10  10:11  11:12  12:EOC  13:0  14:0  15:0  16:0  17:0
  A      first cluster  2  chain [2, 3, 4]  contiguous
  C      first cluster  5  chain [5, 6, 7]  contiguous
  D      first cluster  8  chain [8, 9, 10, 11, 12]  contiguous
```

3. Change the program to delete **C** instead of B, then write D (5 clusters). Is D fragmented now?
4. **Extend:** add a `free_space()` function that prints the free clusters and the **largest contiguous gap**. Explain why a disk can have enough free space in total but still fragment a new file.

**Expected result:** step 3 leaves the free clusters as 7–9 (C's) and 10–17. D gets 7–11, which is contiguous. Step 4 shows the largest gap.

- **Hint 1:** Allocation takes the **lowest free** clusters first, as in Task 4.
- **Hint 2:** `[c for c in sorted(fat) if fat[c] == 0]` lists the free clusters.

---

### Task 12 — Sequential versus direct access, measured

**Goal:** see slides 12–13 in numbers.

**Skill you gain:** you can design fixed-size record files and use `seek` for direct access. Databases and log analysers rely on this technique.

1. Save as `records.py`:

```python
# records.py - sequential access versus random (direct) access on a real file (slides 12-13).
# It writes 100,000 fixed-size records, then finds record 80,000 two ways:
#   1. sequential: read from the start until the record is found (like scanning a log)
#   2. direct: calculate its byte offset (record number x record size) and seek straight to it
# It counts the bytes each method had to read.
#
# Usage: python records.py

import os
import time

RECORD_SIZE = 32                           # every record is exactly 32 bytes, so offsets are easy
COUNT = 100_000
TARGET = 80_000
PATH = "records.dat"

with open(PATH, "wb") as f:                # create the file: Record000001, Record000002, ...
    for i in range(1, COUNT + 1):
        f.write(f"Record{i:06d} value={i * 7:<12}\n".encode().ljust(RECORD_SIZE, b" ")[:RECORD_SIZE])
print(f"File: {os.path.getsize(PATH):,} bytes = {COUNT:,} records x {RECORD_SIZE} bytes")

# 1. Sequential: read records in order until the wanted one appears
t0 = time.perf_counter()
read_bytes = 0
with open(PATH, "rb") as f:
    while True:
        rec = f.read(RECORD_SIZE)
        read_bytes += len(rec)
        if rec.startswith(f"Record{TARGET:06d}".encode()):
            break
t_seq = time.perf_counter() - t0
print(f"Sequential: read {read_bytes:,} bytes ({read_bytes // RECORD_SIZE:,} records) in {t_seq * 1000:.1f} ms -> {rec.decode().strip()}")

# 2. Direct: jump straight to (TARGET - 1) x RECORD_SIZE
t0 = time.perf_counter()
with open(PATH, "rb") as f:
    offset = (TARGET - 1) * RECORD_SIZE
    f.seek(offset)                         # move the file position without reading
    rec = f.read(RECORD_SIZE)
t_dir = time.perf_counter() - t0
print(f"Direct:     seek to byte offset {offset:,}, read {len(rec)} bytes in {t_dir * 1000:.3f} ms -> {rec.decode().strip()}")
os.remove(PATH)
```

2. Run `python records.py`. *What it does:* creates a 3.2 MB file in the current folder, searches it both ways, then deletes the file. Actual output (Verified):

```text
File: 3,200,000 bytes = 100,000 records x 32 bytes
Sequential: read 2,560,000 bytes (80,000 records) in 35.6 ms -> Record080000 value=560000
Direct:     seek to byte offset 2,559,968, read 32 bytes in 0.059 ms -> Record080000 value=560000
```

3. Change `TARGET` to 100 and then to 99,999. How do the sequential times compare? What about direct access?
4. Why would direct access be harder if records had **different** lengths? What could help (slide 13)?

**Expected result:** sequential time grows with the record number; direct-access time stays tiny. Variable-length records need an **index** or other metadata to find offsets.

- **Hint 1:** Direct access reads only 32 bytes, whatever the target.
- **Hint 2:** An index is a table of record number → offset.

---

### Task 13 — Metadata before and after an edit

**Goal:** check official Task 1's findings with a script, and compare with PowerShell.

**Skill you gain:** you can collect file timestamps systematically, the first step of a forensic timeline.

1. Save as `file_meta.py`:

```python
# file_meta.py - show file DATA versus file METADATA, like the official Get-ChildItem command.
# For every file in a folder it prints name, size (bytes), created, modified and accessed times.
# Run it, edit a file, run it again, and compare: the data changed, and so did some metadata.
# Read-only: it only reads information about the files.
#
# Usage: python file_meta.py              (current folder)
#        python file_meta.py C:\path\to\folder

import os
import sys
import datetime as dt

folder = sys.argv[1] if len(sys.argv) > 1 else "."


def when(ts):
    return dt.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S")


print(f"{'Name':<16} {'Bytes':>8}  {'Created':<19}  {'Modified':<19}  {'Accessed':<19}")
for name in sorted(os.listdir(folder)):
    path = os.path.join(folder, name)
    if not os.path.isfile(path):
        continue
    st = os.stat(path)
    # Creation time: st_birthtime where the OS provides it (Windows, macOS, newer Linux Python);
    # otherwise show 'not available' rather than guessing.
    created = when(st.st_birthtime) if hasattr(st, "st_birthtime") else "not available"
    print(f"{name:<16} {st.st_size:>8}  {created:<19}  {when(st.st_mtime):<19}  {when(st.st_atime):<19}")
```

2. In your lab folder, run `python file_meta.py`, edit `sample.txt`, then run it again.
3. Compare with PowerShell's `Get-ChildItem | Select-Object Name, Length, CreationTime, LastWriteTime, Attributes` (Expected).

Actual output on Linux (Verified; Linux's Python cannot report creation time, but `stat` can):

```text
Name                Bytes  Created              Modified             Accessed           
capture.png         31142  not available        2026-11-24 16:06:47  2026-11-24 16:06:47
sample.txt             20  not available        2026-11-24 16:06:47  2026-11-24 16:06:47
Name                Bytes  Created              Modified             Accessed           
capture.png         31142  not available        2026-11-24 16:06:47  2026-11-24 16:06:47
sample.txt             49  not available        2026-11-24 16:06:50  2026-11-24 16:06:47
```

```text
before: sample.txt  size=20  birth=2026-11-24 16:06:47 +0000  modify=2026-11-24 16:06:47 +0000  change=2026-11-24 16:06:47 +0000
after:  sample.txt  size=49  birth=2026-11-24 16:06:47 +0000  modify=2026-11-24 16:06:50 +0000  change=2026-11-24 16:06:50 +0000
```

**Expected result:**

- The size and Modified time change; the Created time does not (Verified with `stat` on Linux).
- On Windows with Python 3.12 or later, the Created column shows a real date (Expected).
- Reading the file may update "Accessed", depending on system settings.

- **Hint 1:** If Created **does** change, your editor may have saved by replacing the file. Record what you observe.
- **Hint 2:** Timestamps are evidence. Write down the time zone too.

---

### Task 14 — Inspect your file system safely (Windows)

**Goal:** read your file-system configuration and permissions without changing anything.

**Skill you gain:** you can audit storage settings and file permissions read-only. This is an everyday task in system administration and security reviews.

On your own Windows computer (Expected; normal, non-elevated PowerShell):

1. `Get-Volume`. *What it does:* lists drives with their file system (NTFS, FAT32, exFAT) and size. Record your C: drive and any USB drive.
2. `Get-Acl .\sample.txt | Format-List`. *What it does:* shows the owner and the access-control entries of your own file. Which accounts have **FullControl**, **Modify** or **Read**?
3. Open **Optimize Drives** (Start → type "defragment"). Record each drive's **Media type** and **Current status**. Do not click Optimize.
4. Read the extension-hiding setting:

   ```text
   reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced" /v HideFileExt
   ```

   What does the value mean now that you have turned on **File name extensions**?
5. Right-click `sample.txt` > **Properties**. Compare **Size** and **Size on disk**. Why are they different?

**Expected result:**

- C: is NTFS. USB sticks are often FAT32 or exFAT.
- Your account has access to your own file.
- Optimize Drives shows "Solid state drive" or "Hard disk drive".
- `HideFileExt` = 0 once extensions are shown.
- A small file uses a whole cluster on disk (Verified on Linux: 49 bytes used 4,096).

- **Hint 1:** If a command is blocked, record that and move on. Do not elevate.
- **Hint 2:** Lecture section 7.2 explains slack.

---

### Task 15 — A real FAT32 volume (optional, Linux)

**Goal:** see real clusters, chains, deletion markers and the 4 GiB limit.

**Skill you gain:** you can examine a file system's raw structures. This is a core digital-forensics skill.

**Only if you already have Linux with `mkfs.fat` and `mtools`.** Everything happens inside an image **file**; no real drive is touched.

1. Save as `fat_reader.py`:

```python
# fat_reader.py - read a real FAT32 disk image and show how FAT finds files (slides 21-26).
#   boot sector  -> where the FATs, the data area and the root directory are
#   directory entry -> file name, size and FIRST cluster
#   FAT entries  -> the chain of following clusters (0x0FFFFFF8+ = end of chain, 0 = free)
# It also shows deleted entries (first byte 0xE5) and whether their data is still on the disk.
# Read-only: it only opens the image file for reading.
#
# Usage: python fat_reader.py fat.img

import struct
import sys

img = open(sys.argv[1] if len(sys.argv) > 1 else "fat.img", "rb").read()

# ---- boot sector (the first 512 bytes) ------------------------------------------------------
bytes_per_sector, sectors_per_cluster, reserved, num_fats = struct.unpack_from("<HBHB", img, 11)
fat_size = struct.unpack_from("<I", img, 36)[0]               # sectors per FAT (FAT32 field)
root_cluster = struct.unpack_from("<I", img, 44)[0]
cluster_size = bytes_per_sector * sectors_per_cluster
fat_start = reserved * bytes_per_sector
data_start = (reserved + num_fats * fat_size) * bytes_per_sector
print(f"Boot sector: {bytes_per_sector} bytes/sector x {sectors_per_cluster} = {cluster_size}-byte clusters, "
      f"{num_fats} copies of the FAT, root directory starts at cluster {root_cluster}")


def fat_entry(n, copy=0):
    off = fat_start + copy * fat_size * bytes_per_sector + n * 4
    return struct.unpack_from("<I", img, off)[0] & 0x0FFFFFFF


def chain(first):
    out = [first]
    while True:
        nxt = fat_entry(out[-1])
        if nxt >= 0x0FFFFFF8 or nxt == 0:
            return out, nxt
        out.append(nxt)


def runs(clusters):
    """Write a cluster list compactly as runs, e.g. [3, 4, 5, 9] -> '3-5, 9'."""
    out, start = [], clusters[0]
    for a, b in zip(clusters, clusters[1:] + [None]):
        if b != a + 1:
            out.append(f"{start}-{a}" if a != start else str(a))
            start = b
    return ", ".join(out)


def cluster_data(n):
    off = data_start + (n - 2) * cluster_size                 # clusters are numbered from 2
    return img[off:off + cluster_size]


print(f"Both FAT copies identical: {all(fat_entry(i, 0) == fat_entry(i, 1) for i in range(2, 40))}")
print("\nRoot directory entries (32 bytes each):")
root = cluster_data(root_cluster)
for i in range(0, len(root), 32):
    e = root[i:i + 32]
    if e[0] == 0x00:
        break                                                 # no more entries
    if e[11] == 0x0F or e[11] & 0x08:
        continue                                              # long-name piece or volume label
    name = e[0:8].decode(errors="replace").rstrip() + "." + e[8:11].decode().rstrip()
    first = (struct.unpack_from("<H", e, 20)[0] << 16) | struct.unpack_from("<H", e, 26)[0]
    size = struct.unpack_from("<I", e, 28)[0]
    if e[0] == 0xE5:
        sample = cluster_data(first)[:12]
        state = "free" if fat_entry(first) == 0 else "REUSED by another file"
        print(f"  DELETED  {'?' + name[1:]:<12} size {size:>8}  first byte 0xE5; cluster {first} is now {state};"
              f" bytes there: {sample!r}")
        continue
    clusters, end = chain(first)
    contiguous = all(b == a + 1 for a, b in zip(clusters, clusters[1:]))
    print(f"  {name:<12} size {size:>8}  clusters {runs(clusters):<15} ({len(clusters)} clusters, end 0x{end:07X})"
          f"  {'contiguous' if contiguous else 'FRAGMENTED'}")
```

2. Build and fill a 64 MiB FAT32 image:

   ```bash
   truncate -s 64M fat.img
   mkfs.fat -F 32 -S 512 -s 8 fat.img
   export MTOOLS_SKIP_CHECK=1
   ```

   Then copy files in with `mcopy -i fat.img A.txt ::/A.TXT` and delete them with `mdel -i fat.img ::/B.TXT`.

3. Run `python3 fat_reader.py fat.img`. Real output after the lecture's sequence (Verified):

```text
Boot sector: 512 bytes/sector x 8 = 4096-byte clusters, 2 copies of the FAT, root directory starts at cluster 2
Both FAT copies identical: True

Root directory entries (32 bytes each):
  A.TXT        size    10000  clusters 3-5             (3 clusters, end 0xFFFFFFF)  contiguous
  D.TXT        size    16000  clusters 6-7, 16346-16347 (4 clusters, end 0xFFFFFFF)  FRAGMENTED
  DELETED  ?.TXT        size     8800  first byte 0xE5; cluster 8 is now free; bytes there: b'Secret proje'
  FILL1.BIN    size 66908160  clusters 11-16345        (16335 clusters, end 0xFFFFFFF)  contiguous
  DELETED  ?2.TXT       size     8000  first byte 0xE5; cluster 16346 is now REUSED by another file; bytes there: b'DDDDDDDDDDDD'
  FILL2.BIN    size     8192  clusters 16348-16349     (2 clusters, end 0xFFFFFFF)  contiguous
```

4. Real file-size test (Verified):

   ```text
   4,294,967,295-byte file -> copied to FAT32
   4,294,967,296-byte file -> File "BIG4G.BIN" too big   (the same file copied to an NTFS image without error)
   ```

**Expected result:** your own chains, deleted entries and (if you try it) the same 4 GiB boundary.

- **Hint 1:** Create big test files without using disk space: `truncate -s 4294967296 big.bin`.
- **Hint 2:** Deleted entries begin with `E5` in a hex dump (Lecture 15's `hexview.py` works on `fat.img`).

---

## Part D — Official tasks and integration (Tasks 16–20)

### Task 16 — Inspect file data and metadata (Official Task 1)

**Goal:** capture metadata before and after an edit, and explain the difference.

**Official steps**

1. **Create your working files.**
   - Open **File Explorer** (**Windows+E**) and go to **Documents** or approved writable university storage.
   - Create a folder (**Ctrl+Shift+N**) named **TW10A_YourStudentID**.
   - In **Word**, create **Lab_Record.docx** in that folder for your observations and screenshots.
   - In **Notepad**, type one sentence and use **File > Save as** to create **sample.txt** in the same folder.
   - Press **Windows+Shift+S**, capture a small screen area, then open the **Snipping Tool** notification and save a **PNG** in the lab folder. If no notification appears, open Snipping Tool and save from there.
   - In File Explorer, enable **View > Show > File name extensions**.
2. **Read file metadata.**
   - Open the lab folder in File Explorer, click the address bar, type `powershell` and press **Enter**.
   - Run `Get-Location` to confirm you are in your lab folder.
   - Then run the read-only command:

     ```powershell
     Get-ChildItem | Select-Object Name, Length, CreationTime, LastWriteTime, Attributes
     ```

     Record or capture the metadata. **Length** is in bytes.
   - If PowerShell is blocked, **do not bypass it**. Use the Properties windows in step 3.
3. **Inspect individual file properties.** For each file, right-click > **Properties > General**. Record **Type of file**, **Location**, **Size**, **Created** and **Modified**, with timestamps and units. Screenshot one Properties window as before-edit evidence. Close with **Cancel** or **X**, and do not change attributes.
4. **Modify a file and compare.** Open **sample.txt**, change the sentence and save. Repeat the PowerShell command (or Properties). Capture the after-edit values. Identify what changed, noting that creation time and modified time are **different properties**.
5. **Explain your findings.** Put the before-and-after screenshots in your lab record. Explain the difference between file data and metadata, and identify **at least one metadata value that changed**.

**Record**

| File | Type | Size before | Size after | Created | Modified before | Modified after |
| --- | --- | --- | --- | --- | --- | --- |
| sample.txt | | | | | | |
| *your PNG* | | | | | | |
| Lab_Record.docx | | | | | | |

- **Hint 1:** Task 13 shows the same comparison done by script.
- **Hint 2:** The Word file's own metadata changes every time you save it.

---

### Task 17 — Compare access and file-system features (Official Task 2)

**Goal:** identify your file system, contrast scanning with seeking, compare a folder with a ZIP, and read permissions safely.

**Official steps**

1. **Identify the file system.** In **File Explorer > This PC**, right-click the drive holding your lab folder and choose **Properties > General**. Record the **File system**.
   - If network storage shows no type, inspect the local **Windows (C:)** drive instead and record which drive you inspected.
   - Optional: `Get-Volume` in normal PowerShell. If it is blocked, rely on Properties. Do not elevate, format or change permissions.
2. **Compare searching with direct access.**
   - In Notepad, enter ten lines labelled **Record01** to **Record10**, each with a short value, and save as **records.txt**.
   - Press **Ctrl+F**, search for **Record08**, and record the line.
   - In your Word lab record, type a line containing **Record08** and find it with **Home > Find** (**Ctrl+F**).
   - Using the lecture, explain the difference between scanning records and seeking to a known byte offset. Ctrl+F does **not** prove direct disk access: an application may scan the contents.
3. **Compare a folder with a ZIP archive.**
   - Close the files, open the **parent** folder, right-click **TW10A_YourStudentID** and choose **Compress to ZIP file** (or **Compress to > ZIP File**). Save the ZIP **beside** the folder, not inside it.
   - Compare **Size** in **Properties > General** for the ZIP and the folder. Very small and already-compressed files may show little saving.
   - Explain that ZIP creates a **separate archive** and is not NTFS compression. If ZIP creation is unavailable, record the restriction rather than installing software.
4. **Inspect permissions safely.**
   - Right-click **sample.txt** > **Properties > Security**. Select an account or group and look at its **Allow** and **Deny** entries without changing them.
   - The basic meanings are: **read** = access the contents; **write** = make permitted changes; **execute** = run a program. NTFS can enforce these.
   - Do **not** click **Edit**, take ownership or change permissions. If the tab is unavailable, record that.
5. **Record your evidence.**
   - Add evidence of the file-system type, the ZIP and the permissions to your lab record. Where a feature was unavailable, record the restriction and give a written explanation instead.
   - State **one key advantage of NTFS over FAT**, such as ACLs or metadata journalling.

**ZIP comparison on Linux, using similar files (Verified):**

```text
Folder: 3 files, 75,191 bytes
ZIP:    22,981 bytes
  capture.png   31,142 ->  22,471 bytes (72%)
  notes.txt     44,000 ->     150 bytes (0%)
  sample.txt        49 ->      50 bytes (102%)
```

Text compressed hugely, the PNG only partly (it is already compressed), and the tiny 49-byte file got slightly **bigger**, because a ZIP adds its own headers.

- **Hint 1:** Task 12 measures the difference between scanning and seeking.
- **Hint 2:** Lecture section 14 lists NTFS's advantages.

---

### Task 18 — Test safe recovery of a lab file (Official Extra Challenge)

**Goal:** practise user-level recovery safely, and explain how it differs from journalling, RAID and backups.

**Official steps**

1. **Create a disposable file and a backup.**
   - In your lab folder, create **RecoverMe.txt** containing a unique sentence.
   - Copy and paste it to make **RecoverMe_Backup.txt**, and keep it. This is your safety copy if your storage does not support Recycle Bin restoration.
2. **Try deletion and a safe restore.**
   - Select only **RecoverMe.txt** and press **Delete**. **Never Shift+Delete.**
   - If Windows warns of **permanent** deletion, select **Cancel**. Instead, rename the original to **RecoverMe_Practice.txt** and copy the backup to recreate **RecoverMe.txt**.
   - Otherwise, open **Recycle Bin** from Start. If **RecoverMe.txt** is there, right-click > **Restore**. If it is not there, recreate it from the backup and record that the storage bypassed the Recycle Bin.
   - Do not install recovery tools or attempt administrator-level recovery.
3. **Verify and capture evidence.**
   - Open the restored or recreated file and check its sentence.
   - Inspect its **Properties** and record any differences in timestamps or other metadata.
   - Capture the Recycle Bin and restored-file evidence where available. Otherwise, capture the backup and the recreated file, and explain why.
4. **Explain the result.** In your lab record, explain how this user-level recovery differs from **file-system resilience** (journalling), a **separate backup**, and **RAID**.

**Record**

| Step | What happened | Evidence |
| --- | --- | --- |
| Delete | Recycle Bin, or a "permanent" warning? | |
| Restore or recreate | | |
| Metadata after | Created / Modified compared with before | |

- **Hint 1:** Lecture section 16's table compares the four protections.
- **Hint 2:** A recreated copy gets a **new** creation time. A Recycle Bin restore usually keeps the original metadata. Check and record which happened.

---

### Task 19 — Mini-project: a file-handling policy for a small team

**Goal:** apply the whole lecture to a realistic requirement.

**Skill you gain:** you can write a short, justified data-handling policy. Security and IT teams produce these, and they draw directly on file-system knowledge.

**Brief.** A five-person student society runs:

- a shared Windows PC holding membership records, which include personal data;
- two USB sticks used to move posters (some PSD files over 5 GB) to a print shop's Mac;
- a laptop whose SSD is "running slow".

Write a 1–2 page policy covering:

1. **File systems:** which file system for each device, and why. Use slides 30–32 and test the 5 GB requirement against FAT32's limit.
2. **Permissions:** an ACL plan for the membership folder. Who can read? Who can modify? Show it as a table.
3. **Deletion:** why deleting membership files from a USB stick does not erase them (lecture section 13.2), and what to do instead, such as encryption or not putting personal data on sticks.
4. **Maintenance:** what to do about the "slow" SSD (slide 14), and what **not** to do.
5. **Protection layers:** a backup plan that is separate from RAID and journalling (lecture section 16), including a test restore.
6. **Evidence:** for any two claims in your policy, include real evidence from your own computer, such as `Get-Volume` output, the Optimize Drives media type or `Get-Acl`.

**ACL table (start)**

| Folder | Group | Read | Modify | Full control |
| --- | --- | --- | --- | --- |
| Membership | Committee | ✓ | ✓ | |
| Membership | Members | | | |

- **Hint 1:** 5 GB > 4 GiB − 1 byte, so FAT32 is out for those sticks.
- **Hint 2:** Least privilege: give only the access each role needs.

---

### Task 20 — Assessment-style practice: file management

**This is practice only, not a real exam question.** The module exam is two hours with short-answer and essay-style questions. The report covers data storage and networking (module guide). Marks are invented for planning.

**Rules:** 25 minutes, closed book, write it yourself.

**(a)** Distinguish file data from file metadata, giving two examples of metadata. *(3 marks)*

**(b)** A file holds 128-byte records. Calculate the byte offset of record 2,000, and explain why direct access to it is faster than sequential access. *(4 marks)*

**(c)** Explain how FAT locates all the clusters of a file, and what happens to a file's directory entry, FAT entries and data when it is deleted. *(6 marks)*

**(d)** Compare FAT32 and NTFS for (i) a company's Windows file server, and (ii) a USB stick used with many different devices. Refer to permissions, journalling, file-size limits and compatibility, and explain why journalling is not a backup. *(7 marks; aim for 250–300 words)*

**Self-marking checklist**

| Part | A good answer includes | Expected | Actual |
| --- | --- | --- | --- |
| (a) | Data = contents; metadata = information about the data (size, times, location, owner, permissions) | 3 points | |
| (b) | (2000 − 1) × 128 = **255,872**; seek reads one record versus scanning 2,000 records | 4 points | |
| (c) | Directory entry gives the first cluster; the FAT chain gives the next clusters to EOC; deletion marks the entry 0xE5 and frees the FAT entries; the data remains until overwritten | 6 points | |
| (d) | NTFS: ACLs, journal, large files, MFT. FAT32: wide compatibility, no ACLs or journal, 4 GiB − 1 limit (exFAT as an alternative). Journal = metadata consistency only; a backup is a separate copy | 7 points | |
| Time | Within 25 minutes | Yes | |

- **Hint 1:** Use the real FAT experiment as evidence in (c).
- **Hint 2:** Lecture sections 9, 12, 13, 14 and 16.

---

## Tracker

| Task | Name | Done | Notes / score |
| --- | --- | --- | --- |
| 1 | Data or metadata? | ☐ | /8 |
| 2 | Overlapping categories | ☐ | /6 |
| 3 | Offsets and access choices | ☐ | /8 |
| 4 | FAT chains by hand | ☐ | /5 |
| 5 | Choose a file system | ☐ | /6 |
| 6 | Fix the myths | ☐ | /7 |
| 7 | Fix the chain reading | ☐ | /3 |
| 8 | Fix the maintenance policy | ☐ | |
| 9 | Fix the protection claims | ☐ | /4 |
| 10 | Fix the lab record | ☐ | /4 |
| 11 | `fat_sim.py` | ☐ | |
| 12 | `records.py` | ☐ | |
| 13 | `file_meta.py` | ☐ | |
| 14 | Inspect your file system | ☐ | |
| 15 | Real FAT32 volume (optional) | ☐ | |
| 16 | **Official Task 1**: Metadata | ☐ | |
| 17 | **Official Task 2**: Access and features | ☐ | |
| 18 | **Official Extra Challenge**: Safe recovery | ☐ | |
| 19 | Mini-project: file-handling policy | ☐ | |
| 20 | Assessment-style practice | ☐ | /20 |

## Reflection

1. Which metadata change surprised you most in Task 16 or 13?
2. After seeing deleted data survive on a FAT volume, how will you handle sensitive files on USB sticks?
3. Explain to a friend in two sentences why an SSD should not be defragmented.
4. Which protection layer (Recycle Bin, journal, RAID, backup) did you previously over-trust?

---

## Answer key

**(Verified)** = real FAT32/NTFS images, Python 3.13, Linux `stat`. **(Expected)** = Windows tools.

### Task 1

- **Data:** 1, 3, 8.
- **Metadata:** 2, 4, 5, 6, 7.

### Task 2

| File | Description |
| --- | --- |
| `notes.txt` | Text, data, unstructured |
| `budget.csv` | Text, data, structured |
| `holiday.jpg` | Binary, data, structured |
| `setup.exe` | Binary, executable, structured |
| `backup.ps1` | Text **and** executable |
| `.docx` | Binary, data, structured (a ZIP container) |

The categories overlap (slide 5).

### Task 3

1. 0
2. 499 × 64 = **31,936**
3. 9,999 × 64 = **639,936**
4. 10,000 × 64 = **640,000** bytes
5. Sequential
6. Direct
7. Sequential
8. Direct

### Task 4

1. LOG = **2 → 3**. REPORT = **4 → 9 → 10**. NOTES = **6 → 7**.
2. REPORT.DOC is fragmented.
3. Clusters 5, 11 and 12 are free.
4. Cluster 8 is marked BAD (damaged), so it is never allocated.
5. The new file gets **5, 11, 12**, which is fragmented.

### Task 5

1. NTFS: ACLs and journalling.
2. FAT32: the device's only option.
3. exFAT: no 4 GiB limit, and cross-platform.
4. NTFS: ACLs.
5. FAT32, or exFAT: simple and compatible.
6. NTFS: metadata journalling.

### Task 6

1. Slide 10: it depends on parsing, I/O and the application.
2. Slide 14: use TRIM/Optimize Drives, not routine defragmentation.
3. Slide 25: the entry is marked and the clusters freed, but the data remains until overwritten (Verified).
4. Slide 23: the second FAT is a redundant copy; recovery is not guaranteed.
5. Slide 31: up to 8 PB in supported configurations.
6. Slide 26: FAT has no ACLs.
7. Slides 27 and 32: the journal keeps metadata consistent; it is not a backup.

### Task 7

1. REPORT's chain is 4 → 9 → 10 (follow the FAT).
2. BAD marks a damaged cluster, which no file uses.
3. NOTES **starts** at 6 (the directory gives the first cluster) and **ends** at 7.

### Task 8

Model policy: "Windows **Optimize Drives** runs on its built-in schedule. It defragments **HDD** volumes and **retrims SSDs**. SSDs are never manually defragmented (slide 14). No third-party defragmenters are installed. Maintenance runs outside working hours."

### Task 9

1. RAID copies the deletion to every mirror. Use backups or the Recycle Bin.
2. The journal records metadata, not old file contents.
3. Network and some removable storage may bypass the Recycle Bin (official sheet).
4. A connected backup can be encrypted too. Keep an offline or off-site copy.

### Task 10

The answers are as in the expected result.

### Task 11 (Verified)

- **Original run:** output as shown.
- **Step 3, deleting C instead of B:**
  - After C and E are deleted, the free clusters are 7–17.
  - D (5 clusters) gets 7, 8, 9, 10 and 11, which is **contiguous**.
- **Step 4, model:**

```python
def free_space():
    free = [c for c in sorted(fat) if fat[c] == 0]
    best = run = 0
    for i, c in enumerate(free):
        run = run + 1 if i and c == free[i - 1] + 1 else 1
        best = max(best, run)
    print(f"free clusters {free}; largest contiguous gap {best}")
```

### Task 12 (Verified)

Sequential time grows with `TARGET`, while direct access stays at about 0.06 ms. Variable-length records need an **index** of record → offset.

### Task 13 (Verified on Linux; Windows Expected)

As shown: the size went from 20 to 49 bytes and the Modified time changed, but the birth time did not.

### Task 14 (Expected)

The results are your own.

### Task 15 (Verified)

As shown.

### Tasks 16–18 (Expected)

The results are your own. Record any restrictions honestly.

### Tasks 19–20 (model points)

Use the checklists. Task 20(b): (2,000 − 1) × 128 = **255,872** bytes.
