# Lab 5 — Operating Systems and the Kernel Hands-on Workbook (20 Tasks)

**Module:** 4301COMP Computer Systems Architecture

**Session:** Teaching Week 03, Session A · **Matching lecture:** `../Lectures/Lecture-05-Operating-Systems-and-the-Kernel.md`

---

## How to use this lab

**What this lab is for.** You will watch the kernel manage real processes and threads, see real system calls (including ones the kernel refuses), measure time spent in user mode and kernel mode, check how your own PC boots, and compare kernel designs.

**Where the official tasks are.**

| Official lab sheet (TW03 Session A) | This workbook |
| --- | --- |
| Task 1 — Map user actions to operating-system services | Task 16 |
| Task 2 — Observe kernel resource management in real time | Task 17 |
| Extra Challenge — Compare kernel architectures and boot sequences | Task 18 |

In the timetabled lab, **do Tasks 16–18 first**.

**Tools**

| Tool | Used in | Notes |
| --- | --- | --- |
| Microsoft Word | Tasks 16–17 | The official sheet asks for `TW03A_YourStudentID.docx` |
| Task Manager, Notepad, Snipping Tool | Tasks 13, 15, 17 | Built into Windows; named on the official sheet |
| System Information (`msinfo32`), Command Prompt | Tasks 14–15 | Built in; read-only commands except where clearly stated |
| Python 3 | Tasks 11–13 | **Optional, your choice.** Free from python.org; built-in modules only |
| Linux or WSL with `strace` | Task 11 (optional part) | **Optional.** Only if you already have Linux or WSL; do not install it just for this |

**Rules:** predict before you check; explain every answer in your own words; use hints only after a real attempt; record what you actually see.

**Labels:** **Verified** = actually run (on an Ubuntu 24.04 Linux machine, Python 3.13) before being written here. **Expected** = not run here; Windows results are all Expected, so record your own.

**Safety.** Only end processes **you** started (such as your own Notepad). Ending system processes can crash Windows or lose work.

---

## Part A — Warm-up: recognise and predict (Tasks 1–5)

### Task 1 — Which OS function?

**Goal:** match everyday events to the OS functions on slide 5 (user interface, memory management, peripheral management, multitasking, security).

| # | Event | OS function |
| --- | --- | --- |
| a | You type your password at the login screen | |
| b | Spotify keeps playing while you write an essay | |
| c | You plug in a USB mouse and it works | |
| d | Opening 30 browser tabs makes the PC use more RAM | |
| e | You double-click an icon on the desktop | |
| f | A guest account cannot open your Documents folder | |
| g | Windows moves an idle program's memory to the page file | |
| h | You print a document | |

**Expected result:** every function used at least once.

- **Hint 1:** Hardware devices → peripheral management.
- **Hint 2:** "Who is allowed?" → security.

---

### Task 2 — User mode or kernel mode?

**Goal:** decide where each piece of work happens.

| # | Work | User mode or kernel mode? |
| --- | --- | --- |
| a | Notepad working out where to wrap a line of text | |
| b | The scheduler choosing the next thread | |
| c | A disk driver sending a command to the SSD | |
| d | Your Java program adding two numbers | |
| e | Handling a timer interrupt | |
| f | Excel recalculating a spreadsheet | |
| g | The kernel checking whether you may open a file | |
| h | A web browser drawing a page's layout in its own memory | |

**Expected result:** 4 user mode, 4 kernel mode.

- **Hint 1:** Ordinary calculation inside a program's own memory needs no privilege.
- **Hint 2:** Anything touching hardware or deciding between processes needs the kernel.

---

### Task 3 — Which system-call category?

**Goal:** classify system calls (slide 11).

Categories: **file**, **process control**, **memory**, **communication**.

| Call or request | Category | Call or request | Category |
| --- | --- | --- | --- |
| `open()` | | `socket()` | |
| `fork()` | | `brk()` | |
| `write()` | | `exec()` / `execve()` | |
| `mmap()` | | `send()` | |
| `close()` | | Start a new app | |
| "Save my file" | | "Give me more memory" | |

**Expected result:** 4 file, 3 process control, 3 memory, 2 communication.

- **Hint 1:** `mmap` and `brk` are named on slide 11 as memory calls.
- **Hint 2:** Starting an app needs a new process and loading a program.

---

### Task 4 — Predict the system calls

**Goal:** predict what the kernel will be asked to do, and what it will answer.

The file `note.txt` contains the 67-byte sentence: *Operating systems manage computer hardware and software resources.* (66 characters plus an end-of-line character).

The program `cat note.txt` prints it to the screen. Predict each call and its **return value**:

| Step | System call | Return value |
| --- | --- | --- |
| 1 | `openat(…, "note.txt", O_RDONLY)` | (a small number: the file descriptor) |
| 2 | `read(3, …)` | |
| 3 | `write(1, …)` | |
| 4 | `read(3, …)` | |
| 5 | `close(3)` | |

Then predict the result of `openat(…, "missing.txt", O_RDONLY)` when the file does not exist.

**Expected result:** matches the Verified trace in the answer key.

- **Hint 1:** `read` and `write` return the number of bytes.
- **Hint 2:** A second `read` at the end of a file returns 0.

---

### Task 5 — Interrupt or exception?

**Goal:** tell external events from errors caused by the current instruction (slide 10).

| # | Event | Interrupt or exception? |
| --- | --- | --- |
| a | A network packet arrives | |
| b | A program divides by zero | |
| c | The timer fires every few milliseconds | |
| d | A program tries to run an invalid instruction | |
| e | You press a key | |
| f | A program tries to write to memory it does not own | |

For each, who runs next: the program, or a kernel handler?

**Expected result:** 3 interrupts, 3 exceptions; a kernel handler runs every time.

- **Hint 1:** Did the **current instruction** cause it?
- **Hint 2:** Lecture section 9.2.

---

## Part B — Find and fix (Tasks 6–10)

### Task 6 — Fix the false statements

**Goal:** correct common misunderstandings.

Each statement is **false**. Rewrite it correctly.

1. "A system call gives the program permission to control the hardware directly."
2. "The kernel is the Windows desktop."
3. "The firmware loads the entire Windows kernel straight from the disk, with no other stages."
4. "On current 64-bit Windows, the kernel file is `ntkrnlpa.exe`."
5. "Phones use microkernels and desktops use monolithic kernels."
6. "The kernel can be swapped out to the page file when memory is low."

**Expected result:** six corrected statements, each linked to a slide.

- **Hint 1:** Slides 10, 12, 17 and 20.
- **Hint 2:** For 6: slide 8 says the kernel's essential parts are **resident**.

---

### Task 7 — Fix the kernel-design table

**Goal:** correct a classmate's table.

Sam Archer's table has **four** errors.

| Kernel | Sam's design | Sam's "where most services run" | Sam's trade-off |
| --- | --- | --- | --- |
| Linux | Microkernel | Kernel space | Fast in-kernel communication; a kernel fault can affect everything |
| MINIX 3 | Microkernel | Kernel space | Good fault isolation; extra IPC and context-switch overhead |
| Windows NT | Hybrid | Mix: substantial kernel-space services plus modular design | A kernel-mode driver can never crash the system |
| Apple's XNU | Monolithic | Mix | Balances performance and isolation |

**Expected result:** four corrected cells.

- **Hint 1:** Slide 21 lists each example.
- **Hint 2:** Slide 25 says something important about kernel-mode drivers.

---

### Task 8 — Why did the kernel refuse?

**Goal:** read real system-call failures.

These lines are real (Verified):

```text
openat(AT_FDCWD, "missing.txt", O_RDONLY) = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/shadow", O_RDONLY) = -1 EACCES (Permission denied)
openat(AT_FDCWD, "note.txt", O_RDONLY) = 3
```

And this is real output from `os_copy.py` (Task 11), run three ways (Verified; the PID will differ):

```text
Copied 67 bytes from note.txt to copy.txt (my PID was 1150)
The operating system refused the request: [Errno 2] No such file or directory: 'missing.txt'
The operating system refused the request: [Errno 13] Permission denied: '/etc/shadow'
```

1. For each `openat` line, explain what was asked, what the kernel answered and why.
2. Match each `os_copy.py` line to one of the `openat` lines.
3. The second failure happened when the program was run as an **ordinary user**. What would you expect if the administrator (root) ran it, and why is that a security concern if an attacker gains administrator rights?

**Expected result:** three explanations; Errno 2 = ENOENT, Errno 13 = EACCES.

- **Hint 1:** A negative return value means failure; the name after it says why.
- **Hint 2:** `/etc/shadow` holds Linux password hashes and is readable only by the administrator.

---

### Task 9 — Where did the boot fail?

**Goal:** locate a boot problem at the right stage.

For each symptom, name the boot stage where it fails (firmware/UEFI, boot manager, OS loader, kernel initialisation, system services, user login) and suggest a first check.

1. The screen says "No bootable device found".
2. The PC shows a **Secure Boot violation** after someone replaced the boot loader.
3. Windows shows a blue screen during start-up after a new graphics driver was installed.
4. Windows starts, but the antivirus icon never appears and it reports "service failed to start".
5. Everything starts, but your password is rejected.
6. A laptop boots from a USB stick you left in, instead of from its SSD.

**Expected result:** six stages and six sensible first checks.

- **Hint 1:** The configured **boot order** is a firmware setting.
- **Hint 2:** Drivers are loaded by the OS loader and initialised with the kernel.

---

### Task 10 — Fix the process notes

**Goal:** correct confused definitions.

Sam wrote:

> "A program and a process are the same. When I open Notepad twice there is still one Notepad process. Each thread gets its own PID and its own memory. A 4-core CPU can only ever run one thread at a time. Closing a program never leaves anything running."

Find **five** errors and rewrite the paragraph correctly.

**Expected result:** five corrections.

- **Hint 1:** Slide 9 defines threads and multicore execution.
- **Hint 2:** The official lab asks you to check whether a related background process remains after closing Notepad.

---

## Part C — Build (Tasks 11–15)

### Task 11 — Build a file copier from raw system calls

**Goal:** use the four file system calls from slide 11 yourself.

**Skill you gain:** you can write a program that talks to the OS through its file system calls and handle the kernel's refusals properly.

1. Save as `os_copy.py`:

```python
# os_copy.py - copy a file using the operating system's file calls directly.
#
# os.open, os.read, os.write and os.close are thin Python wrappers around the
# system calls named on the slides: open(), read(), write(), close().
# Each one asks the kernel to do the work; the program never touches the disk.
#
# Usage: python os_copy.py SOURCE DESTINATION

import os
import sys


def copy(source, destination, chunk=4096):
    src = os.open(source, os.O_RDONLY)                          # system call: open
    dst = os.open(destination, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)
    total = 0
    while True:
        data = os.read(src, chunk)                              # system call: read
        if not data:                                            # empty = end of file
            break
        total += os.write(dst, data)                            # system call: write
    os.close(src)                                               # system call: close
    os.close(dst)
    return total


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python os_copy.py SOURCE DESTINATION")
        sys.exit(1)
    try:
        n = copy(sys.argv[1], sys.argv[2])
        print(f"Copied {n} bytes from {sys.argv[1]} to {sys.argv[2]} (my PID was {os.getpid()})")
    except OSError as e:
        # The kernel refused: e.g. the file does not exist, or permission denied.
        print(f"The operating system refused the request: {e}")
```

2. Create a small text file `note.txt`, then run `python os_copy.py note.txt copy.txt`. *What it does:* reads `note.txt` and writes a new file `copy.txt`; it changes nothing else.
3. Run it again with a file that does not exist, and once with a file you are not allowed to read. Record the messages.
4. **Optional, Linux/WSL only:** run `strace -e trace=openat,read,write,close python3 os_copy.py note.txt copy2.txt` and find the calls for `note.txt` and `copy2.txt`. Real output from the checking machine (Verified; start-up calls removed):

   ```text
   openat(AT_FDCWD, "note.txt", O_RDONLY|O_CLOEXEC) = 3
   openat(AT_FDCWD, "copy2.txt", O_WRONLY|O_CREAT|O_TRUNC|O_CLOEXEC, 0644) = 4
   read(3, "Operating systems manage compute"..., 4096) = 67
   write(4, "Operating systems manage compute"..., 67) = 67
   read(3, "", 4096)                       = 0
   close(3)                                = 0
   close(4)                                = 0
   ```

5. Match each line of the Python code to a line of the trace.

**Expected result:** `Copied … bytes`, and the two refusals shown in Task 8 (Verified on Linux). On Windows, a protected file to try is `C:\Windows\System32\config\SAM` (Expected: permission denied, or "in use").

- **Hint 1:** File descriptor 3 is the source, 4 is the destination.
- **Hint 2:** `O_CREAT` asks the kernel to create the file if it does not exist.

---

### Task 12 — Measure user time versus kernel time

**Goal:** see the cost of crossing into the kernel.

**Skill you gain:** you can measure where a program spends its processor time (user mode or kernel mode), which is how performance problems and unusual behaviour are investigated.

1. Save as `user_vs_kernel.py`:

```python
# user_vs_kernel.py - how much time does a program spend in user mode
# (running its own instructions) and in kernel mode (inside system calls)?
#
# os.times() asks the OS how much processor time this process has used:
#   user   = time running the program's own code in user mode
#   system = time the kernel spent working on the program's behalf
#
# Usage: python user_vs_kernel.py

import os
import tempfile


def measure(label, work):
    before = os.times()
    work()
    after = os.times()
    user = after.user - before.user
    system = after.system - before.system
    print(f"{label:<32} user {user:5.2f} s   system (kernel) {system:5.2f} s")


def pure_calculation():
    """Only arithmetic: no system calls inside the loop."""
    total = 0
    for i in range(20_000_000):
        total += i * i


def many_small_writes():
    """Thousands of tiny writes: each os.write is a system call."""
    with tempfile.TemporaryFile() as f:
        fd = f.fileno()
        for _ in range(300_000):
            os.write(fd, b"x")


if __name__ == "__main__":
    measure("Pure calculation", pure_calculation)
    measure("300,000 one-byte writes", many_small_writes)
```

2. Predict: which job will show more **system (kernel)** time, and why?
3. Run it three times. Record the numbers. Actual output from two runs on the checking machine (Verified; your numbers will differ):

   ```text
   Pure calculation                 user  0.80 s   system (kernel)  0.00 s
   300,000 one-byte writes          user  0.03 s   system (kernel)  0.08 s
   Pure calculation                 user  0.76 s   system (kernel)  0.00 s
   300,000 one-byte writes          user  0.03 s   system (kernel)  0.06 s
   ```

4. **Extend it:** change `many_small_writes` to write **one** block of 300,000 bytes instead (`os.write(fd, b"x" * 300_000)`). Predict, run and explain the difference.

**Expected result:** the calculation is almost all user time; the 300,000 small writes are mostly kernel time; one big write takes almost no time at all.

- **Hint 1:** Each `os.write` is one system call, so one mode switch into the kernel and back.
- **Hint 2:** Slide 23 mentions the **overhead** of user programs invoking kernel functions.

---

### Task 13 — Watch threads appear in Task Manager

**Goal:** see a process's thread count change while you watch.

**Skill you gain:** you can link a running program to its PID and observe its threads and memory in Task Manager, a basic skill in investigating a suspicious process.

1. Save as `threads_demo.py`:

```python
# threads_demo.py - start extra threads inside ONE process, so you can watch
# the process's thread count change in Task Manager (Details tab, Threads column).
#
# Usage: python threads_demo.py [number_of_threads] [seconds]
# Example: python threads_demo.py 5 30

import os
import sys
import threading
import time


def kernel_thread_count():
    """On Linux the kernel reports the thread count in /proc; elsewhere, None."""
    try:
        with open("/proc/self/status") as f:
            for line in f:
                if line.startswith("Threads:"):
                    return int(line.split()[1])
    except OSError:
        return None


if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    seconds = float(sys.argv[2]) if len(sys.argv) > 2 else 30

    print(f"My PID is {os.getpid()}. Look for this PID in Task Manager > Details.")
    print(f"Threads now: {threading.active_count()} (kernel says: {kernel_thread_count()})")

    workers = [threading.Thread(target=time.sleep, args=(seconds,)) for _ in range(n)]
    for w in workers:
        w.start()
    print(f"Started {n} threads that sleep for {seconds} s.")
    print(f"Threads now: {threading.active_count()} (kernel says: {kernel_thread_count()})")

    for w in workers:
        w.join()
    print(f"All finished. Threads now: {threading.active_count()} "
          f"(kernel says: {kernel_thread_count()})")
```

2. Open Task Manager > **Details** with the **PID** and **Threads** columns showing (see Task 17).
3. Run `python threads_demo.py 5 30`. Note the PID it prints, find that PID in Task Manager and watch the **Threads** column for 30 seconds.
4. Run it again with 20 threads. What happens to Threads and to **Working set**?

Actual output on the Linux checking machine (Verified, PID hidden):

```text
$ python3 threads_demo.py 5 1
My PID is <PID>. Look for this PID in Task Manager > Details.
Threads now: 1 (kernel says: 1)
Started 5 threads that sleep for 1.0 s.
Threads now: 6 (kernel says: 6)
All finished. Threads now: 1 (kernel says: 1)
```

**Expected result (Windows):** the Threads count rises by about the number you asked for, then falls back. Windows' count will be **higher** than Python's own count, because Windows gives every process a few extra threads of its own (Expected).

- **Hint 1:** Sort the Details list by PID or name (`python.exe`) to find it quickly.
- **Hint 2:** All the threads share **one** PID: they are inside one process.

---

### Task 14 — How does your own PC boot?

**Goal:** check the firmware, Secure Boot and kernel on your own Windows PC.

**Skill you gain:** you can verify a PC's boot security settings and kernel version, which are standard checks in a security baseline.

On your own Windows PC (Expected; all steps are read-only):

1. `msinfo32` > **System Summary**. Record **BIOS Mode** (UEFI or Legacy), **Secure Boot State** (On, Off or Unsupported), and **BIOS Version/Date**.
2. Command Prompt: `systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System Boot Time"`. *What it does:* shows three lines from the system information report. Record them.
3. File Explorer: go to `C:\Windows\System32`, find **ntoskrnl.exe**, right-click > **Properties** > **Details**. Record its **File version**. Do not move, rename or delete it.
4. Answer: is your PC protected against bootkits by Secure Boot? If it says Off, what would you need to change, and where (do **not** change it now)?

**Linux comparison (Verified on the checking machine):** `uname -sr` printed `Linux 6.18.44-fc-v819` (the kernel name and version). On a PC that booted with UEFI, the folder `/sys/firmware/efi` exists; on the checking machine it did **not** exist, because that virtual machine is started directly by its host without a UEFI firmware stage.

**Expected result:** a small table of your PC's values.

- **Hint 1:** "Secure Boot State: Unsupported" usually means BIOS Mode is Legacy.
- **Hint 2:** The kernel's file version usually matches the OS build number from `systeminfo`.

---

### Task 15 — Same job, two interfaces

**Goal:** manage a process with the GUI and then with the CLI.

**Skill you gain:** you can find and stop a process from the command line, which is faster to repeat and script than the GUI.

1. Open **Notepad** yourself (type nothing important).
2. **GUI:** in Task Manager > Details, find `Notepad.exe` and note its PID.
3. **CLI:** in Command Prompt, run `tasklist /FI "IMAGENAME eq notepad.exe"`. *What it does:* lists only Notepad processes, with PID and memory use. Read-only. Does the PID match?
4. **CLI, changes something:** run `taskkill /PID <the PID>`. *What it does:* asks that one process to close (like clicking X). Only use the PID of the Notepad **you** opened.
5. Compare the two interfaces: which was quicker? Which could you put in a script to run on 100 PCs?

**Expected result:** matching PIDs; Notepad closes after `taskkill` (Expected).

- **Hint 1:** On Windows 11, Notepad may appear as `Notepad.exe` with a capital N; the filter is not case-sensitive.
- **Hint 2:** If Notepad asks to save, that is the program responding to the close request.

---

## Part D — Official tasks and integration (Tasks 16–20)

### Task 16 — Map user actions to operating-system services (Official Task 1)

**Goal:** connect everyday actions to the OS subsystems and system calls behind them.

**Official steps**

1. Create a record document named **TW03A_YourStudentID.docx**.
2. For each user action (**opening a file**, **starting an application**, **sending a network packet**, **requesting additional virtual memory from the OS**, **responding to a key press**), identify the OS subsystem (e.g. File System, Process Manager, Network Stack, Memory Manager, Input/Output Driver).
3. For each action, state whether it requires an OS/kernel service, and briefly explain why.
4. Consider whether the application can complete the operation itself in user mode or must request a protected service from the kernel.
5. Choose **two** actions and identify the general **system-call category** (file, process, memory, network/communication). You do not need exact Windows system calls.
6. Briefly explain why user applications are **restricted from controlling hardware directly** without going through the kernel.

**Suggested table**

| User action | OS subsystem | Kernel service needed? Why? | User mode alone possible? | System-call category |
| --- | --- | --- | --- | --- |
| Opening a file | | | | |
| Starting an application | | | | |
| Sending a network packet | | | | |
| Requesting more virtual memory | | | | |
| Responding to a key press | | | | |

**Test plan**

| Check | Expected | Actual |
| --- | --- | --- |
| Document named correctly | `TW03A_<your ID>.docx` | |
| Five actions, each with a subsystem | Yes | |
| Each "needs kernel?" answer has a reason | Yes | |
| Two system-call categories identified | Yes | |
| Explanation of the hardware restriction mentions protection, isolation and abstraction | Yes | |

- **Hint 1:** All five need the kernel. The interesting part is **why**.
- **Hint 2:** Use lecture sections 8–10.

---

### Task 17 — Observe kernel resource management in real time (Official Task 2)

**Goal:** record real PID, thread, CPU-time and memory values, and link them to kernel responsibilities.

**Official steps**

1. Open **Task Manager** (Ctrl + Shift + Esc) > **Details**. Right-click a column heading > **Select columns** > make sure **PID**, **Threads**, **CPU time** and **Working set (memory)** are ticked > **OK**.
2. Choose **three** active background or system processes and record:

   | Process name | PID | Threads | CPU time | Working set / memory |
   | --- | --- | --- | --- | --- |
   | 1. | | | | |
   | 2. | | | | |
   | 3. | | | | |

   (Working set gives an indication of the physical memory currently associated with a process.)

3. **Notepad activity:**
   - Before opening Notepad, look through the list for a Notepad process.
   - Open Notepad and type exactly: *Operating systems manage computer hardware and software resources.*
   - In Task Manager, find the Notepad process. Record its **PID, Threads, CPU time and Working set**.
   - Use **Snipping Tool** to capture the Notepad row and paste it into your Word record.
   - In Notepad, save the text as **TW03A_Notepad.txt**, then close Notepad normally.
   - In Task Manager, observe whether the Notepad process disappears or whether any related background process remains.

   *Official note:* your PID, thread count, CPU time and memory values may differ from other students' and may change over time. This is normal.

4. Answer (choose from process/thread management, memory management, file-system management, device management):
   - Two OS/kernel responsibilities involved when **Notepad starts**.
   - Two OS/kernel responsibilities involved when the **text file is saved**.

**Test plan**

| Check | Expected | Actual |
| --- | --- | --- |
| Four columns visible | PID, Threads, CPU time, Working set | |
| Three processes recorded | Real values | |
| Notepad row recorded and screenshotted | Yes | |
| File saved as TW03A_Notepad.txt | Yes | |
| Observation after closing recorded honestly | "Disappeared" or "X remained" | |
| Two responsibilities for start; two for save | Yes | |

- **Hint 1:** The typed sentence is the same 67-byte text used in Tasks 4 and 11: saving it triggers the same kind of `open`/`write`/`close` requests.
- **Hint 2:** Starting a program needs a new process **and** memory for it.

---

### Task 18 — Compare kernel architectures and boot sequences (Official Extra Challenge)

**Goal:** compare kernel designs and put the boot stages in order.

**Official steps**

1. Complete:

   | Operating system/kernel | Kernel design | Where do most services execute? | One advantage or trade-off |
   | --- | --- | --- | --- |
   | Linux | Modular monolithic | | |
   | MINIX 3 | Microkernel | | |
   | Windows NT | Hybrid | | |
   | Apple's XNU | Hybrid | | |

2. Why should the terms monolithic, microkernel and hybrid be treated as **architectural categories** rather than absolute descriptions of every component in an operating system?
3. Put the stages into the correct boot order (1 to 6): [ ] Firmware / UEFI · [ ] Boot manager · [ ] Operating-system loader · [ ] Kernel initialisation · [ ] System services · [ ] User login.

**Test plan**

| Check | Expected | Actual |
| --- | --- | --- |
| Four rows complete | Yes | |
| Categories question answered with "implementation" and "mixed designs" | Yes | |
| Boot order | 1–6 in the order listed in the lecture | |

- **Hint 1:** Slides 21 and 24–25.
- **Hint 2:** Lecture section 12.2.

---

### Task 19 — Mini-project: OS security baseline of your own PC

**Goal:** produce a one-page baseline record of your computer's OS and boot security.

**Skill you gain:** you can produce a basic OS **security baseline**, a record of how a machine is set up that later checks are compared against.

Using Tasks 14, 15 and 17 (all read-only), write a one-page record titled "OS baseline: [device type]" with:

1. **OS:** name, version/build, `ntoskrnl.exe` file version, kernel design category (with one sentence on what that means).
2. **Boot:** BIOS mode, Secure Boot state, last boot time.
3. **Processes:** total number of processes (Task Manager > Performance > CPU shows "Processes" and "Threads"), and the three processes using the most memory, each with PID and working set.
4. **Start-up:** the apps listed in Task Manager > **Startup apps**, with their status.
5. **Three observations**, each one sentence: something good, something to check, and one question to research.

**Test plan**

| Check | Expected | Actual |
| --- | --- | --- |
| All five sections present | Yes | |
| Every value has a source (which tool) | Yes | |
| Observations are facts you saw, not guesses | Yes | |
| No changes made to the PC | Yes | |
| No personal information (name, student ID) | Yes | |

- **Hint 1:** Total processes and threads are shown under the CPU graph on the Performance tab.
- **Hint 2:** An unfamiliar start-up app is a good "something to check": search its publisher before deciding anything.

---

### Task 20 — Assessment-style practice: the operating system and kernel

**This is practice only, not a real exam question.** The module exam is two hours with short-answer and essay-style questions, and covers operating systems (module guide). Marks are invented for planning.

**Rules:** 25 minutes, closed book, write it yourself.

**(a)** State four functions of an operating system. *(2 marks)*

**(b)** Explain the difference between user mode and kernel mode, and why the distinction matters for security. *(4 marks)*

**(c)** Describe the stages of booting a modern PC from power-on to user login, including the role of UEFI Secure Boot. *(5 marks)*

**(d)** Explain what a system call is, giving examples from two categories, and compare monolithic, microkernel and hybrid kernel designs with one example and one trade-off each. *(9 marks; aim for 250–350 words)*

**Self-marking checklist**

| Part | A good answer includes | Expected | Actual |
| --- | --- | --- | --- |
| (a) | Four of: user interface, memory management, peripheral management, multitasking, security | 2 points | |
| (b) | Privilege levels; applications restricted; kernel full access; isolation of programs from each other and the kernel; system calls as the only controlled entry | 4 points | |
| (c) | Firmware (UEFI) init and checks → boot manager → OS loader → kernel init → services → login; Secure Boot verifies boot components, stops bootkits | 5 points | |
| (d) | Controlled request; kernel checks and may refuse; two categories with real names; three designs with Linux / MINIX 3 or QNX / Windows NT or XNU; overhead vs fault isolation; "depends on implementation" | 9 points | |
| Time | Within 25 minutes | Yes | |

- **Hint 1:** Use the real `openat`/`read` trace as evidence in (d).
- **Hint 2:** Lecture sections 8, 10, 12 and 14.

---

## Tracker

| Task | Name | Done | Notes / score |
| --- | --- | --- | --- |
| 1 | Which OS function? | ☐ | /8 |
| 2 | User mode or kernel mode? | ☐ | /8 |
| 3 | Which system-call category? | ☐ | /12 |
| 4 | Predict the system calls | ☐ | /6 |
| 5 | Interrupt or exception? | ☐ | /6 |
| 6 | Fix the false statements | ☐ | /6 |
| 7 | Fix the kernel-design table | ☐ | /4 |
| 8 | Why did the kernel refuse? | ☐ | |
| 9 | Where did the boot fail? | ☐ | /6 |
| 10 | Fix the process notes | ☐ | /5 |
| 11 | File copier from system calls | ☐ | |
| 12 | User time versus kernel time | ☐ | |
| 13 | Threads in Task Manager | ☐ | |
| 14 | How does your PC boot? | ☐ | |
| 15 | Same job, two interfaces | ☐ | |
| 16 | **Official Task 1** — Map actions to OS services | ☐ | |
| 17 | **Official Task 2** — Observe resource management | ☐ | |
| 18 | **Official Extra Challenge** — Kernels and boot | ☐ | |
| 19 | Mini-project: OS baseline | ☐ | |
| 20 | Assessment-style practice | ☐ | /20 |

## Reflection

1. What did you see in Task Manager when you closed Notepad? Did it match what you expected?
2. In Task 12, why do 300,000 small writes cost so much more kernel time than one big write?
3. Is Secure Boot on for your PC? If not, why might that be?
4. Which kernel design would you choose for a car's braking controller, and why?

---

## Answer key

**(Verified)** = run on the Ubuntu 24.04 checking machine with Python 3.13 and `strace`. **(Expected)** = Windows or your own PC; not run here.

### Task 1

a security · b multitasking · c peripheral management · d memory management · e user interface · f security · g memory management · h peripheral management.

### Task 2

User mode: a, d, f, h. Kernel mode: b, c, e, g.

### Task 3

File: `open`, `write`, `close`, "save my file". Process control: `fork`, `exec`, "start a new app". Memory: `mmap`, `brk`, "give me more memory". Communication: `socket`, `send`.

### Task 4 (Verified)

| Step | Call | Return |
| --- | --- | --- |
| 1 | `openat(…, "note.txt", O_RDONLY)` | **3** |
| 2 | `read(3, …)` | **67** |
| 3 | `write(1, …)` | **67** |
| 4 | `read(3, …)` | **0** (end of file) |
| 5 | `close(3)` | **0** (success) |

Missing file: `-1 ENOENT (No such file or directory)`.

### Task 5

Interrupts: a, c, e. Exceptions: b, d, f. In every case the processor switches to kernel mode and a **kernel handler** runs; for exceptions the kernel usually stops the faulty program.

### Task 6

1. A system call is a **controlled request**; the kernel does the work and may refuse; the program never gets unrestricted hardware access (slide 10).
2. The kernel is the **privileged core** of the OS; the desktop is a user-mode user interface (slides 8, 19).
3. Firmware starts a **boot manager**, which starts the **OS loader**, which loads the kernel and boot-critical drivers (slide 17).
4. It is **`ntoskrnl.exe`**; `ntkrnlpa.exe` is obsolete (slide 12).
5. Kernel design is an **architectural trade-off**, not decided by device type (slide 20). (Android phones run the monolithic Linux kernel.)
6. The kernel's essential parts stay **resident** in memory; it is **user space** that can be swapped to the page file (slides 8, 23).

### Task 7

Linux → **modular monolithic** (not microkernel). MINIX 3 → most services in **user space** (not kernel space). Windows NT trade-off → kernel-mode drivers **can** still crash the system (slide 25). XNU → **hybrid** (not monolithic).

### Task 8 (Verified)

1. `missing.txt`: asked to open a file for reading; **ENOENT**, it does not exist. `/etc/shadow`: asked to open the password-hash file; **EACCES**, the user lacks permission. `note.txt`: success; file descriptor **3**.
2. "Copied 67 bytes" ↔ the successful open; `[Errno 2]` ↔ ENOENT; `[Errno 13]` ↔ EACCES.
3. Root would be allowed to read it. That is why attackers try to gain administrator rights: the kernel enforces permissions **by user**, so an attacker who becomes root (or Administrator) is trusted by the kernel and can read secrets such as password hashes.

### Task 9

1 Firmware/UEFI: check the boot order and that the drive is detected. 2 Firmware (Secure Boot verification): restore a signed boot loader. 3 Kernel initialisation (driver loaded with the kernel): roll back the driver in Safe Mode. 4 System services: check the service and its event log. 5 User login: check the account, Caps Lock, keyboard layout. 6 Firmware boot order: remove the USB stick or move the SSD up the boot order.

### Task 10

(1) A program is a file; a process is a running instance. (2) Opening Notepad twice normally creates **two** processes with different PIDs (Expected on Windows; some modern apps share one process). (3) Threads **share** their process's PID and memory. (4) A 4-core CPU can run **several** threads at the same time (slide 9). (5) Closing a program may leave a related background process running; the official lab asks you to check this.

### Task 11 (Verified on Linux)

Output: `Copied 67 bytes from note.txt to copy.txt (my PID was …)`; refusals as in Task 8. Code → trace: `os.open(source, …)` → `openat(… "note.txt" …) = 3`; `os.open(destination, …)` → `openat(… "copy2.txt", O_WRONLY|O_CREAT|O_TRUNC …) = 4`; `os.read` → `read(3, …) = 67` then `= 0`; `os.write` → `write(4, …) = 67`; `os.close` ×2 → `close(3)`, `close(4)`. (Python adds `O_CLOEXEC` automatically.)

### Task 12 (Verified; numbers vary)

Two runs: pure calculation 0.80 s and 0.76 s user, 0.00 s system; 300,000 one-byte writes 0.03 s user, 0.08 s and 0.06 s system. The writes are mostly **kernel** time because each `os.write` is a separate system call with a mode switch and checks. One 300,000-byte write is **one** system call, so its kernel time is close to zero: crossing into the kernel has a fixed cost each time (slide 23's "overhead").

### Task 13 (Linux Verified; Windows Expected)

Linux: 1 → 6 → 1 threads with `5 1`. Windows: the Threads column rises by about the number requested and falls when they finish; the absolute number is higher because Windows adds its own threads to every process. Working set rises slightly with more threads, because each thread needs its own stack memory.

### Task 14 (Expected)

Your values. A typical recent PC: BIOS Mode UEFI; Secure Boot State On; `ntoskrnl.exe` version matching the OS build. If Secure Boot is Off, it is changed in the UEFI firmware settings (and may need BIOS Mode UEFI): do not change it without understanding the consequences.

### Task 15 (Expected)

PIDs match. `taskkill /PID n` closes Notepad (it may prompt to save). The CLI is easy to repeat and script; the GUI is easier to explore.

### Task 16 (model rows)

| Action | Subsystem | Why the kernel is needed | Category |
| --- | --- | --- | --- |
| Opening a file | File system | Disk access and permission checks are protected | File |
| Starting an application | Process manager | A new process, address space and scheduling need the kernel | Process |
| Sending a network packet | Network stack (+ NIC driver) | The network card is hardware; the stack is in the kernel | Communication |
| Requesting more virtual memory | Memory manager | Only the kernel can change address-space mappings | Memory |
| Responding to a key press | I/O (keyboard) driver | A hardware interrupt is handled by the kernel, then passed to the app | (I/O via the kernel) |

None can be completed in user mode alone. Applications are restricted so that one program cannot damage the hardware, read other programs' data or bypass security; the kernel provides **protection**, **isolation** and a standard **abstraction**.

### Task 17 (Expected)

Your values. Starting Notepad: process/thread management (create process, schedule threads) and memory management (allocate address space, load the program into RAM). Saving: file-system management (create the file, record where it is) and device management (driver writes to the SSD).

### Task 18

| Kernel | Where most services execute | Advantage or trade-off |
| --- | --- | --- |
| Linux | Kernel space (drivers as loadable modules) | Fast in-kernel communication; a kernel-mode fault can affect the whole system |
| MINIX 3 | User space (small kernel: scheduling, IPC) | Better fault isolation; extra IPC and context-switch overhead |
| Windows NT | Substantial services in kernel space, with modular design | Balance of performance and isolation; kernel-mode driver faults can still crash it |
| Apple's XNU | Mixed (Mach microkernel ideas + BSD services in kernel space) | Balance of performance, compatibility and isolation |

Categories: real kernels mix ideas, and slide 24 says actual reliability and performance depend on the implementation, not only the category.

Boot order: **1** Firmware/UEFI · **2** Boot manager · **3** OS loader · **4** Kernel initialisation · **5** System services · **6** User login.

### Task 19

Use the test plan. A good baseline lets someone else compare the PC later and spot changes.

### Task 20 (model points)

(a) Four of the five slide-5 functions. (b) The processor runs applications in user mode (restricted: no direct hardware access, only their own memory) and the kernel in kernel mode (full access); this isolates programs from each other and from the kernel, and forces every privileged action through checked system calls. (c) Lecture section 12. (d) Lecture sections 10 and 14, with the real trace as an example.
