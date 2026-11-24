# Lab 2 — Computer Architecture Foundations and the FDE Cycle Hands-on Workbook (20 Tasks)

**Module:** 4301COMP Computer Systems Architecture

**Session:** Teaching Week 01, Session B · **Matching lecture:** `../Lectures/Lecture-02-Computer-Architecture-Foundations-and-the-FDE-Cycle.md`

---

## How to use this lab

**What this lab is for.** You will trace instructions by hand, then **run them** in a small simulator and watch the PC, IR, MAR, MDR and register change, exactly as in the lecture. You will also write short programs with branches and look at real machine code.

**Where the official tasks are.**

| Official lab sheet (TW01 Session B) | This workbook |
| --- | --- |
| Official Task 1 — Map the main architecture components | Task 16 |
| Official Task 2 — Trace a simple instruction cycle | Task 17 |
| Official Extra Challenge — Changes to normal execution | Task 18 |

In the timetabled lab, **do Tasks 16 and 17 first**.

**Tools**

| Tool | Used in | Notes |
| --- | --- | --- |
| Microsoft Word | Tasks 16–17 | Named on the official lab sheet |
| Pen and paper | Everywhere | Trace by hand **before** you run anything |
| Python 3 and `fde_sim.py` (given in Task 11) | Tasks 8–13, 19 | **Optional, your choice.** Free from python.org. Every task can also be done by hand |
| Little Man Computer (LMC) in a web browser | Task 14 | **Your choice, not a module requirement.** A free educational simulator, e.g. <https://peterhigginson.co.uk/lmc/> |
| Compiler Explorer in a web browser | Task 15 | <https://godbolt.org>, free, no account needed |
| Task Manager (Windows) | Task 18 | Built in |

**Rules:** predict before you check; show your working (write register values after **every** step); use hints only after a real attempt; record what you actually see.

**Labels:** **Verified** = run or calculated before being written here. **Expected** = not run here (for example a website), so check it yourself.

**The machine used in this lab.** The lecture's teaching model, with one general-purpose register **R** (the slides also call it ACC in one-address instructions) and these instructions:

| Instruction | Meaning | Group |
| --- | --- | --- |
| `LOAD x` | R ← Memory[x] | Data movement |
| `STORE x` | Memory[x] ← R | Data movement |
| `ADD x` | R ← R + Memory[x] | Arithmetic |
| `SUB x` | R ← R − Memory[x] | Arithmetic |
| `READ x` | Memory[x] ← next input value | I/O |
| `WRITE x` | output Memory[x] | I/O |
| `JUMP x` | PC ← x | Program control |
| `JUMPZ x` | if the EQ flag is set (last result was zero): PC ← x | Program control |
| `JUMPN x` | if the LT flag is set (last result was negative): PC ← x | Program control |
| `HALT` | stop | Program control |
| `DAT n` | not an instruction: a memory cell holding the number n | — |

`LOAD`, `ADD` and `SUB` set the flags: **GT** if R > 0, **EQ** if R = 0, **LT** if R < 0. The program starts at address 0 with PC = 0 and R = 0.

---

## Part A — Warm-up: recognise and predict (Tasks 1–5)

### Task 1 — Name that register or bus

**Goal:** match each description to the right register or bus.

Choose from: **PC, IR, MAR, MDR, R, address bus, data bus, control bus, flags**. Each is used once.

| # | Description | Answer |
| --- | --- | --- |
| a | Holds the instruction currently being carried out | |
| b | Carries the value read from memory back to the processor | |
| c | Holds the address of the next instruction | |
| d | Carries the "read" or "write" signal | |
| e | Holds the address of the memory location being accessed right now | |
| f | Carries the address from the processor to memory | |
| g | Holds the data on its way to or from memory | |
| h | Records whether the last result was greater than, equal to or less than zero | |
| i | Holds a working value, such as a running total | |

**Expected result:** 9 different answers, no repeats.

- **Hint 1:** Registers *hold*; buses *carry*.
- **Hint 2:** MAR = **A**ddress, MDR = **D**ata.

---

### Task 2 — Sort instructions into groups

**Goal:** classify instructions using slide 8's five groups (arithmetic, logic, program control, data movement, I/O).

| Instruction | Group | Instruction | Group |
| --- | --- | --- | --- |
| `ADD 20` | | `AND` | |
| `STORE 12` | | `JUMPZ 7` | |
| `READ 10` | | `SUB 11` | |
| `MOVE A, X` | | `CALL` (subroutine) | |
| `NOT` | | `WRITE 13` | |
| `MULTIPLY` | | `LOAD 40` | |

**Expected result:** 3 arithmetic, 2 logic, 2 program control, 3 data movement, 2 I/O.

- **Hint 1:** Does it calculate, compare bits, change the PC, copy a value, or talk to a device?
- **Hint 2:** A subroutine call changes the PC, so it is program control.

---

### Task 3 — Instruction anatomy

**Goal:** split instructions into opcode and operands and identify the format.

For each instruction: write the **opcode**, the **operand(s)**, whether the operand location is **explicit** or **implicit**, and the **number of addresses** (0, 1, 2 or 3).

1. `ADD <m1>, <m2>, <m3>`
2. `ADD <m1>, <m2>`
3. `ADD <m1>` (uses ACC)
4. `LOAD R1, [40]`
5. `HALT`
6. `ADD` on a stack machine

Then answer: 7. A machine has **16-bit** instructions with a **5-bit opcode** and the rest for one address. How many different opcodes and how many addresses?

**Expected result:** item 7 gives 32 opcodes and 2,048 addresses (Verified).

- **Hint 1:** Explicit means the address is written in the instruction.
- **Hint 2:** 16 − 5 = 11 bits for the address; count 2⁵ and 2¹¹.

---

### Task 4 — Predict the trace

**Goal:** trace a program by hand, recording registers after each instruction.

```text
0: LOAD 10        10: DAT 8
1: ADD 11         11: DAT 5
2: SUB 12         12: DAT 3
3: STORE 13       13: DAT 0
4: WRITE 13
5: HALT
```

Copy and complete (values **after** each instruction finishes):

| Step | IR | MAR | MDR | R | PC | Output |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | LOAD 10 | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | HALT | | | | | |

**Expected result:** output 10; address 13 ends up containing 10 (Verified).

- **Hint 1:** After a data instruction, the MAR holds the **data** address used during execute, not the instruction's address.
- **Hint 2:** The PC after step *n* is always one more than the address of the instruction in step *n*, unless that instruction was a taken branch.

---

### Task 5 — Follow the PC

**Goal:** predict how the PC changes when a branch is taken.

```text
0: LOAD 10        10: DAT 20
1: JUMP 4         11: DAT 5
2: ADD 11         12: DAT 0
3: HALT
4: SUB 11
5: STORE 12
6: HALT
```

1. List the addresses of the instructions that actually run, in order.
2. Write the PC value after each one.
3. Which instructions are **never** run?
4. What does address 12 contain at the end?

**Expected result:** 5 instructions run; address 12 ends with 15 (Verified).

- **Hint 1:** `JUMP 4` overwrites the PC with 4.
- **Hint 2:** After `JUMP 4`, the next fetch is from address 4, not 2.

---

## Part B — Find and fix (Tasks 6–10)

### Task 6 — Fix the FDE description

**Goal:** correct wrong statements about the cycle.

Sam Archer wrote these notes. **Each statement contains one error.** Rewrite each correctly.

1. "In fetch, the instruction is copied from memory into the PC."
2. "The PC is increased at the end of the execute stage."
3. "During decode, the ALU works out what the instruction means."
4. "The MDR holds the address of the location being read."
5. "Reading a value from memory sets that location to zero."
6. "A branch instruction makes the processor skip the fetch stage."

**Expected result:** six corrected sentences.

- **Hint 1:** Check each against the fetch micro-steps: MAR ← PC, MDR ← Memory[MAR], IR ← MDR, PC ← PC + 1.
- **Hint 2:** Which part of the processor *decodes*? Which register holds the *current* instruction?

---

### Task 7 — Fix the bus table

**Goal:** correct a table of bus roles.

| Bus | Sam's description | Correct? |
| --- | --- | --- |
| Address bus | Carries data from memory to the processor | |
| Data bus | Carries the instruction or value being transferred, in either direction | |
| Control bus | Carries the memory address to read | |
| Address bus direction | Both ways | |
| Control bus | Carries interrupt requests from devices | |

Mark each **correct** or **wrong**, and fix the wrong ones.

**Expected result:** 2 correct, 3 wrong.

- **Hint 1:** Address = *where*, data = *what*, control = *which operation and when*.
- **Hint 2:** Does memory ever need to send the processor an address?

---

### Task 8 — The program that never stops properly

**Goal:** diagnose a missing `HALT` using the simulator's error message.

**Skill you gain:** you can read an error message, link it to a cause and fix it.

```python
PROGRAM = ["LOAD 10", "WRITE 10", "10: DAT 42"]
```

1. Predict: what does the processor fetch after `WRITE 10`?
2. Run it in `fde_sim.py` (Task 11 explains how). Record the exact error message.
3. Fix the program and run it again. Record the output.

**Expected result (Verified):** the error is `Address 2 holds data (0), not an instruction`; the fixed program outputs `[42]`.

- **Hint 1:** The processor does not know where a program "ends". It just fetches the next address.
- **Hint 2:** Add one instruction after `WRITE 10`.

---

### Task 9 — Two wrong answers

**Goal:** find logic errors: the program runs, but the answer is wrong.

**Program B** should output 2 + 3:

```python
PROGRAM = ["LOAD 10", "ADD 11", "STORE 12", "WRITE 13", "HALT",
           "10: DAT 2", "11: DAT 3", "12: DAT 0", "13: DAT 0"]
```

**Program C** should output 10 − 4:

```python
PROGRAM = ["LOAD 11", "SUB 10", "STORE 12", "WRITE 12", "HALT",
           "10: DAT 10", "11: DAT 4", "12: DAT 0"]
```

For each: predict the output, run it, explain the bug in one sentence, fix it and run again.

**Expected result (Verified):** B outputs `[0]` before the fix and `[5]` after; C outputs `[-6]` before and `[6]` after.

- **Hint 1:** For B, compare the STORE address with the WRITE address.
- **Hint 2:** For C, subtraction is not reversible: 4 − 10 ≠ 10 − 4. Which value must be loaded first?

---

### Task 10 — Endless loops

**Goal:** fix two loops that do not end properly.

**Program D** should read a number and count down to 1:

```python
PROGRAM = ["READ 20", "LOAD 20", "JUMPZ 7", "WRITE 20", "SUB 21", "STORE 20",
           "JUMP 0", "HALT", "20: DAT 0", "21: DAT 1"]
INPUTS = [3]
```

**Program D2:**

```python
PROGRAM = ["LOAD 20", "JUMP 1", "HALT", "20: DAT 5"]
```

1. Trace each by hand for a few steps. What goes wrong?
2. Run each and record the message.
3. Fix both.

**Expected result (Verified):** D outputs 3, then stops with `READ at address 0 needs an input, but none are left`. D2 stops with `Stopped after 200 steps: is there an endless loop?`

- **Hint 1:** For D, which address should the loop jump back to: the `READ` or the `LOAD`?
- **Hint 2:** For D2, `JUMP 1` is *at* address 1. Where does it send the PC?

---

## Part C — Build (Tasks 11–15)

### Task 11 — Run the FDE simulator

**Goal:** run the simulator and read its trace.

**Skill you gain:** you can run a small Python program and read an instruction-by-instruction trace of a processor's registers.

1. Save this code as `fde_sim.py` (it was tested with Python 3.13):

```python
# fde_sim.py - a tiny fetch-decode-execute simulator for learning.
#
# It models the simple teaching machine from the 4301COMP slides:
#   PC  - Program Counter: address of the next instruction
#   IR  - Instruction Register: the instruction being carried out
#   MAR - Memory Address Register: the address being read or written
#   MDR - Memory Data Register: the value moving to or from memory
#   R   - one general-purpose register (used for arithmetic)
#   flags GT / EQ / LT - result of the last calculation compared with 0
#
# Instructions (one-address format: OPCODE address):
#   LOAD x   R <- Memory[x]          STORE x  Memory[x] <- R
#   ADD x    R <- R + Memory[x]      SUB x    R <- R - Memory[x]
#   READ x   Memory[x] <- next input WRITE x  output Memory[x]
#   JUMP x   PC <- x                 JUMPZ x  if EQ flag: PC <- x
#   JUMPN x  if LT flag: PC <- x     HALT     stop
#   DAT n    not an instruction: a memory cell holding the number n
#
# Start a line with "address:" to put it at that address, e.g. "20: DAT 6".
# Flags are updated by LOAD, ADD and SUB.
#
# Usage: edit PROGRAM and INPUTS at the bottom, then run:  python fde_sim.py

MEMORY_SIZE = 100
MAX_STEPS = 200          # safety limit, so a faulty loop cannot run forever


def load(program):
    """Put the program into memory, starting at address 0.

    A line can start with an address, e.g. "20: DAT 6", to place it there.
    Lines without an address go in the next address in order.
    """
    memory = [0] * MEMORY_SIZE
    address = 0
    for line in program:
        if ":" in line:
            before, line = line.split(":", 1)
            address = int(before)
            line = line.strip()
        parts = line.split()
        if parts[0] == "DAT":
            memory[address] = int(parts[1])            # a data value
        else:
            memory[address] = line                     # an instruction
        address += 1
    return memory


def run(program, inputs=(), trace=True):
    memory = load(program)
    inputs = list(inputs)
    outputs = []
    pc, r = 0, 0
    flags = {"GT": False, "EQ": True, "LT": False}

    for step in range(1, MAX_STEPS + 1):
        # ---------- FETCH ----------
        mar = pc                       # MAR <- PC
        mdr = memory[mar]              # memory read: MDR <- Memory[MAR]
        ir = mdr                       # IR <- MDR
        pc = pc + 1                    # PC advances to the next address

        if not isinstance(ir, str):
            raise ValueError(f"Address {mar} holds data ({ir}), not an instruction")

        # ---------- DECODE ----------
        parts = ir.split()
        opcode = parts[0]
        operand = int(parts[1]) if len(parts) > 1 else None

        # ---------- EXECUTE ----------
        note = ""
        if opcode == "LOAD":
            mar, mdr = operand, memory[operand]
            r = mdr
        elif opcode == "STORE":
            mar, mdr = operand, r
            memory[operand] = mdr
        elif opcode in ("ADD", "SUB"):
            mar, mdr = operand, memory[operand]
            r = r + mdr if opcode == "ADD" else r - mdr
        elif opcode == "READ":
            if not inputs:
                raise ValueError(f"READ at address {pc - 1} needs an input, but none are left")
            value = inputs.pop(0)
            mar, mdr = operand, value
            memory[operand] = value
            note = f"input {value}"
        elif opcode == "WRITE":
            mar, mdr = operand, memory[operand]
            outputs.append(mdr)
            note = f"output {mdr}"
        elif opcode == "JUMP":
            pc = operand
            note = "branch taken"
        elif opcode == "JUMPZ":
            note = "branch taken" if flags["EQ"] else "branch not taken"
            if flags["EQ"]:
                pc = operand
        elif opcode == "JUMPN":
            note = "branch taken" if flags["LT"] else "branch not taken"
            if flags["LT"]:
                pc = operand
        elif opcode == "HALT":
            pass
        else:
            raise ValueError(f"Unknown opcode {opcode!r} at address {pc - 1}")

        if opcode in ("LOAD", "ADD", "SUB"):
            flags = {"GT": r > 0, "EQ": r == 0, "LT": r < 0}

        if trace:
            set_flags = ",".join(k for k, v in flags.items() if v)
            print(f"{step:>3} | IR={ir:<9} | MAR={mar:>2} MDR={mdr!s:>4} "
                  f"| R={r:>4} | PC={pc:>2} | flags={set_flags:<2} | {note}")

        if opcode == "HALT":
            break
    else:
        print(f"Stopped after {MAX_STEPS} steps: is there an endless loop?")

    return outputs, memory, r


if __name__ == "__main__":
    # Example: read two numbers, add them, store and output the total.
    PROGRAM = [
        "READ 10",   # 0: input first number into address 10
        "READ 11",   # 1: input second number into address 11
        "LOAD 10",   # 2: R <- Memory[10]
        "ADD 11",    # 3: R <- R + Memory[11]
        "STORE 12",  # 4: Memory[12] <- R
        "WRITE 12",  # 5: output Memory[12]
        "HALT",      # 6: stop
    ]
    INPUTS = [7, 5]

    print("step | instruction  | memory registers | R | next PC | flags | note")
    outputs, memory, r = run(PROGRAM, INPUTS)
    print("Outputs:", outputs)
```

2. Open a terminal in the folder where you saved it and run `python fde_sim.py` (on some systems `python3 fde_sim.py`). *What it does:* runs the example program and prints a trace. It does not read or change any files.

3. Compare your output with this actual output (Verified):

```text
step | instruction  | memory registers | R | next PC | flags | note
  1 | IR=READ 10   | MAR=10 MDR=   7 | R=   0 | PC= 1 | flags=EQ | input 7
  2 | IR=READ 11   | MAR=11 MDR=   5 | R=   0 | PC= 2 | flags=EQ | input 5
  3 | IR=LOAD 10   | MAR=10 MDR=   7 | R=   7 | PC= 3 | flags=GT |
  4 | IR=ADD 11    | MAR=11 MDR=   5 | R=  12 | PC= 4 | flags=GT |
  5 | IR=STORE 12  | MAR=12 MDR=  12 | R=  12 | PC= 5 | flags=GT |
  6 | IR=WRITE 12  | MAR=12 MDR=  12 | R=  12 | PC= 6 | flags=GT | output 12
  7 | IR=HALT      | MAR= 6 MDR=HALT | R=  12 | PC= 7 | flags=GT |
Outputs: [12]
```

4. Answer from the trace: (a) Which steps used an input? (b) Why is the MAR **6** at the HALT step? (c) Why does the PC never go back to a lower number in this program?

5. To run your own program, replace `PROGRAM` and `INPUTS` at the bottom of the file. A line such as `"20: DAT 6"` puts 6 at address 20.

**Expected result:** your output matches the Verified output exactly.

- **Hint 1:** "MAR=6" at HALT: the HALT was fetched from address 6 and did not use any data address.
- **Hint 2:** There are no branch instructions in the example.

---

### Task 12 — Build: output the larger of two numbers

**Goal:** write a program that uses a **conditional branch** to make a decision.

**Specification:** read two numbers A and B; output whichever is larger; if they are equal, output either.

1. Plan it in words first: "Calculate A − B. If the result is negative, B is larger…"
2. Write it for the simulator using `READ`, `LOAD`, `SUB`, `JUMPN`, `WRITE`, `HALT`.
3. Test it with this test plan:

| Test | A | B | Expected | Actual |
| --- | --- | --- | --- | --- |
| B larger | 4 | 9 | 9 | |
| A larger | 9 | 4 | 9 | |
| Equal | 6 | 6 | 6 | |
| Zero | 0 | 3 | 3 | |

**Expected result:** all four tests pass (the model answer passed all four, Verified).

- **Hint 1:** `SUB` sets the LT flag when A − B < 0.
- **Hint 2:** You need two `WRITE` instructions, each followed by its own `HALT`.

---

### Task 13 — Build: a countdown loop

**Goal:** write a loop using `JUMPZ` and `JUMP`.

**Specification:** read a number *n*; output *n*, *n* − 1, …, 1; then stop. If *n* is 0, output nothing.

1. Write it (you may start from your fixed Program D in Task 10).
2. Run it with input 3 and with input 0.
3. Count how many instructions the processor executed for input 3 (the step numbers in the trace).

**Expected result (Verified):** input 3 outputs `[3, 2, 1]` in **22** steps; input 0 outputs `[]`.

- **Hint 1:** Test for zero **before** writing the value.
- **Hint 2:** The loop body is: write, subtract 1, store, jump back to the load.

---

### Task 14 — Little Man Computer

**Goal:** see the same ideas in a widely used educational simulator.

**Skill you gain:** you can write, assemble and step through a program in Little Man Computer and watch the PC, IR and accumulator change.

LMC uses three-digit instructions. The first digit is the opcode and the last two are the address (opcodes: 1 ADD, 2 SUB, 3 STA (store), 5 LDA (load), 6 BRA (branch always), 7 BRZ (branch if zero), 8 BRP (branch if zero or positive), 901 INP, 902 OUT, 000 HLT).

1. Open an LMC simulator (for example <https://peterhigginson.co.uk/lmc/>).
2. Type this program into the editor:

   ```text
           INP
           STA FIRST
           INP
           ADD FIRST
           OUT
           HLT
   FIRST   DAT
   ```

3. Click **Submit** (or **Assemble**). Look at memory: the first six cells should hold **901, 306, 901, 106, 902, 000** (checked with an LMC assembler written for this lab; the website itself was not run here).
4. Click **Step** repeatedly with inputs 7 and 5. At each step, write down the PC, IR (or "instruction") and accumulator.
5. Explain `306`: which digit is the opcode and which digits are the address?

**Expected result:** output 12. Memory addresses 0–5 hold the codes above. (Expected for the website; the program logic was Verified.)

- **Hint 1:** `STA FIRST` stores into the address of the label FIRST, which is address 6.
- **Hint 2:** `306` = opcode 3 (store) + address 06.

---

### Task 15 — Real machine code with Compiler Explorer

**Goal:** see a real compiler turn a line of code into processor instructions and bytes.

**Skill you gain:** you can read a basic disassembly listing and find the load, add and store pattern, the first step in reverse engineering and malware analysis.

1. Go to <https://godbolt.org>. Choose language **C** and compiler **x86-64 gcc** (any recent version).
2. Paste:

   ```c
   int total;

   void add(int a, int b) {
       total = a + b;
   }
   ```

3. In the output pane, find the `add` instruction. Use the **Output** (gear) menu to turn on **Compile to binary object** so the instruction bytes are shown.
4. Answer: (a) Which instructions **load** `a` and `b` into registers? (b) Which instruction does the addition? (c) Which instruction **stores** into `total`? (d) What bytes does the add instruction use?

For comparison, this is the real output of the same code compiled with gcc 13.3 (`gcc -O0`) and disassembled with `objdump -d -M intel` (Verified):

```text
   0:   f3 0f 1e fa             endbr64
   4:   55                      push   rbp
   5:   48 89 e5                mov    rbp,rsp
   8:   89 7d fc                mov    DWORD PTR [rbp-0x4],edi
   b:   89 75 f8                mov    DWORD PTR [rbp-0x8],esi
   e:   8b 55 fc                mov    edx,DWORD PTR [rbp-0x4]
  11:   8b 45 f8                mov    eax,DWORD PTR [rbp-0x8]
  14:   01 d0                   add    eax,edx
  16:   89 05 00 00 00 00       mov    DWORD PTR [rip+0x0],eax
  1c:   90                      nop
  1d:   5d                      pop    rbp
  1e:   c3                      ret
```

**Expected result:** your listing has the same `add eax, edx` pattern; other details may differ by compiler version (Expected).

- **Hint 1:** In Intel syntax, the **destination is first**: `mov edx, [...]` loads into edx.
- **Hint 2:** The add uses only two bytes. Look at address 14.

---

## Part D — Official tasks and integration (Tasks 16–20)

### Task 16 — Map the main architecture components (Official Task 1)

**Goal:** produce a clear reference table of the components and buses.

**Official steps (from the TW01 Session B lab sheet)**

1. Create a Word document named `TW01B_YourStudentID.docx`. Insert a table with columns **Component**, **Main role** and **Example information held or transferred**.
2. Add rows for **processor**, **main memory**, **secondary storage** and **input/output**.
3. Add separate rows for the **address bus**, **data bus** and **control bus**. Explain the distinct role of each bus.
4. Below the table, explain why **main memory** and **secondary storage** are not interchangeable terms.

**Test plan**

| Check | Expected | Actual |
| --- | --- | --- |
| File named correctly | `TW01B_<your ID>.docx` | |
| Three columns as specified | Component / Main role / Example | |
| Seven rows | Processor, main memory, secondary storage, I/O, three buses | |
| Each bus has a distinct role | Where / what / which operation | |
| Example column is concrete | e.g. "address 40", "the value 25", "READ signal" | |
| Memory vs storage explanation | Mentions volatility, speed and that programs run from main memory | |

- **Hint 1:** Lecture 2 section 16.1 and Lecture 1 section 18.
- **Hint 2:** A good example entry for the data bus: "the value 25 travelling from address 40 to the MDR".

---

### Task 17 — Trace a simple instruction cycle (Official Task 2)

**Goal:** trace `LOAD R1, [40]` through fetch, decode and execute.

**Official steps (from the TW01 Session B lab sheet)**

1. Use the instruction `LOAD R1, [40]`. State its **opcode**, **destination register** and **source operand**.
2. Insert a table with columns **Stage**, **Main component** and **What happens**. Add rows for **fetch**, **decode** and **execute**.
3. For **fetch**, describe how the Program Counter identifies the instruction and how the Instruction Register receives it.
4. For **decode**, state how the control unit identifies the LOAD operation and its operands.
5. For **execute**, state how the contents of address 40 are copied into R1, then explain what happens to the Program Counter during normal sequential execution.

**Optional check in the simulator (Verified).** The simulator has one register called R, so `LOAD R1, [40]` becomes `LOAD 40`. With address 40 holding 25:

```python
PROGRAM = ["LOAD 40", "HALT", "40: DAT 25"]
```

Actual trace:

```text
  1 | IR=LOAD 40   | MAR=40 MDR=  25 | R=  25 | PC= 1 | flags=GT |
  2 | IR=HALT      | MAR= 1 MDR=HALT | R=  25 | PC= 2 | flags=GT |
```

**Test plan**

| Check | Expected | Actual |
| --- | --- | --- |
| Opcode, destination, source named | LOAD · R1 · contents of address 40 | |
| Fetch row | MAR ← PC; read; MDR ← instruction; IR ← MDR; PC + 1 | |
| Decode row | Control unit recognises LOAD, destination R1, source address 40 | |
| Execute row | MAR ← 40; read signal; MDR ← Memory[40]; R1 ← MDR | |
| Buses named | Address bus carries 40; data bus carries the value; control bus carries READ | |
| PC explanation | Already advanced during fetch; next instruction follows in sequence | |
| Memory unchanged | Address 40 still holds its value | |

- **Hint 1:** There are **two** memory reads: one to fetch the instruction, one to fetch the data.
- **Hint 2:** Lecture 2 section 17 has the same pattern for `LOAD 20`.

---

### Task 18 — Changes to normal execution (Official Extra Challenge)

**Goal:** explain branches, subroutine calls and interrupts, and see interrupts on a real computer.

**Official steps (from the TW01 Session B lab sheet)**

1. Explain how a **branch** differs from an ordinary sequential instruction.
2. Explain why a **subroutine call** saves a **return address**.
3. Explain how an **interrupt** temporarily transfers control to a handler and then allows the interrupted work to continue.

**Supplementary: see interrupts happening (Expected on Windows).**

4. Open Task Manager (Ctrl + Shift + Esc) → **Processes** tab, scroll to **Windows processes** and find **System interrupts**. Watch its CPU % while you move the mouse quickly and type. Record what you see (it may stay near 0%: that is normal and worth recording).
5. Linux alternative (read-only): `cat /proc/interrupts` lists how many interrupts each device has caused on each processor core. Real output from the Linux machine used to check this lab (Verified, first lines only):

   ```text
              CPU0       CPU1
    24:          1          0  IO-APIC   5-edge      ACPI:Ged
    25:          0          1  IO-APIC   6-edge      ACPI:Ged
    26:         11          0  IO-APIC   4-edge      ttyS0
   ```

   Each row is a source of interrupts (for example `ttyS0` is a serial port) and each column is a processor core.

**Test plan**

| Check | Expected | Actual |
| --- | --- | --- |
| Branch explained | Overwrites the PC; next fetch from the target; conditional vs unconditional | |
| Subroutine explained | Return address = address after the call; saved before jumping; restored on return | |
| Interrupt explained | Event-driven; finish current instruction; save PC and registers; handler; restore; continue | |
| Observation recorded | A real value from Task Manager (or `/proc/interrupts`) | |

- **Hint 1:** Compare all three in a table: caused by, planned or not, what is saved.
- **Hint 2:** Without a saved return address, a subroutine called from two places could only ever return to one of them.

---

### Task 19 — Mini-project: multiply by repeated addition

**Goal:** build a complete program with a loop, a counter and a running total.

**Skill you gain:** you can turn an algorithm into low-level instructions and prove it works with a test plan.

The teaching machine has no multiply instruction. Build one: A × B = A added to itself B times.

**Specification**

- Read A, then B.
- Output A × B.
- Must work when A or B is 0.
- Use address 20 for A, 21 for B (the counter), 22 for the total and 23 for the constant 1.

**Steps**

1. Write the algorithm in plain English (5–7 lines).
2. Draw a flowchart (paper or Mermaid).
3. Write the program for `fde_sim.py`.
4. Run the test plan.
5. Count the steps for 3 × 4 and for 6 × 6. How does the number of steps grow as B gets bigger?

**Test plan**

| Test | A | B | Expected | Actual |
| --- | --- | --- | --- | --- |
| Normal | 3 | 4 | 12 | |
| B is zero | 7 | 0 | 0 | |
| A is zero | 0 | 5 | 0 | |
| Square | 6 | 6 | 36 | |
| A is one | 1 | 9 | 9 | |

**Expected result:** all five pass (the model answer passed all five, Verified).

- **Hint 1:** Loop: if counter = 0, finish; otherwise total ← total + A, counter ← counter − 1, go back.
- **Hint 2:** Test the counter with `LOAD 21` then `JUMPZ`, at the **top** of the loop, so B = 0 works.

---

### Task 20 — Assessment-style practice: explaining the FDE cycle

**This is practice only, not a real exam question.** The module exam is two hours with short-answer and essay-style questions (module guide). Marks below are invented for planning.

**Rules:** 25 minutes, closed book, write it yourself.

**(a)** State the three characteristics of the von Neumann architecture. *(3 marks)*

**(b)** Explain the role of each of the address bus, data bus and control bus. *(3 marks)*

**(c)** Explain the difference between a three-address and a one-address instruction, using `ADD` as an example. *(4 marks)*

**(d)** Describe the fetch–decode–execute cycle for the instruction `ADD 21`, where register R holds 6 and address 21 holds 9. Refer to the PC, MAR, MDR, IR, ALU and buses, and state the final value of R. *(10 marks; aim for 250–350 words)*

**Self-marking checklist**

| Part | A good answer includes | Expected | Actual |
| --- | --- | --- | --- |
| (a) | Four sub-systems; stored program; sequential execution | 3 points | |
| (b) | Address = where; data = what, both ways; control = read/write, timing, interrupts | 3 points | |
| (c) | `<m3> ← <m1> + <m2>` vs `ACC ← ACC + <m1>`; explicit vs implicit; length trade-off | 4 points | |
| (d) | Fetch micro-steps in order; PC + 1 during fetch; CU decodes opcode and operand; MAR ← 21; read; MDR ← 9; ALU adds; R ← 15; flags; correct buses named | 10 points | |
| Time | Within 25 minutes | Yes | |

- **Hint 1:** Plan (d) as a numbered list first, then turn it into sentences.
- **Hint 2:** Lecture 2 section 17 traces `ADD 21` with exactly these numbers.

---

## Tracker

| Task | Name | Done | Notes / score |
| --- | --- | --- | --- |
| 1 | Name that register or bus | ☐ | /9 |
| 2 | Sort instructions into groups | ☐ | /12 |
| 3 | Instruction anatomy | ☐ | /7 |
| 4 | Predict the trace | ☐ | |
| 5 | Follow the PC | ☐ | /4 |
| 6 | Fix the FDE description | ☐ | /6 |
| 7 | Fix the bus table | ☐ | /5 |
| 8 | Missing HALT | ☐ | |
| 9 | Two wrong answers | ☐ | |
| 10 | Endless loops | ☐ | |
| 11 | Run the simulator | ☐ | |
| 12 | Larger of two numbers | ☐ | /4 tests |
| 13 | Countdown loop | ☐ | |
| 14 | Little Man Computer | ☐ | |
| 15 | Compiler Explorer | ☐ | |
| 16 | **Official Task 1** — Map the components | ☐ | |
| 17 | **Official Task 2** — Trace `LOAD R1, [40]` | ☐ | |
| 18 | **Official Extra Challenge** — Changes to normal execution | ☐ | |
| 19 | Mini-project: multiply | ☐ | /5 tests |
| 20 | Assessment-style practice | ☐ | /20 |

## Reflection

1. Which register did you find hardest to keep track of in your traces, and why?
2. In Task 13, how many instructions ran to count down from 3? What does that tell you about how many instructions a real program runs?
3. Explain, in two sentences, why the PC is updated during fetch rather than at the end of execute.
4. What surprised you about the real machine code in Task 15?

---

## Answer key

Results marked **(Verified)** were run in `fde_sim.py` (Python 3.13), checked with an LMC assembler written for this lab, compiled with gcc 13.3, or calculated. **(Expected)** results depend on your own computer or a website that was not run here.

### Task 1

a IR · b data bus · c PC · d control bus · e MAR · f address bus · g MDR · h flags · i R.

### Task 2

| Instruction | Group | Instruction | Group |
| --- | --- | --- | --- |
| `ADD 20` | Arithmetic | `AND` | Logic |
| `STORE 12` | Data movement | `JUMPZ 7` | Program control |
| `READ 10` | I/O | `SUB 11` | Arithmetic |
| `MOVE A, X` | Data movement | `CALL` | Program control |
| `NOT` | Logic | `WRITE 13` | I/O |
| `MULTIPLY` | Arithmetic | `LOAD 40` | Data movement |

### Task 3

| # | Opcode | Operands | Explicit/implicit | Addresses |
| --- | --- | --- | --- | --- |
| 1 | ADD | m1, m2, m3 | Explicit | 3 |
| 2 | ADD | m1, m2 | Explicit (m2 is also the destination) | 2 |
| 3 | ADD | m1 (+ ACC implied) | m1 explicit, ACC implicit | 1 |
| 4 | LOAD | R1, [40] | Explicit register and explicit address | 2 (a register and a memory address) |
| 5 | HALT | none | — | 0 |
| 6 | ADD | none written (top two stack items) | Implicit | 0 |

7. 2⁵ = **32** opcodes; 16 − 5 = 11 address bits; 2¹¹ = **2,048** addresses (Verified).

### Task 4 (Verified)

| Step | IR | MAR | MDR | R | PC | Output |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | LOAD 10 | 10 | 8 | 8 | 1 | |
| 2 | ADD 11 | 11 | 5 | 13 | 2 | |
| 3 | SUB 12 | 12 | 3 | 10 | 3 | |
| 4 | STORE 13 | 13 | 10 | 10 | 4 | |
| 5 | WRITE 13 | 13 | 10 | 10 | 5 | 10 |
| 6 | HALT | 5 | HALT | 10 | 6 | |

Address 13 contains 10 at the end; addresses 10–12 are unchanged.

### Task 5 (Verified)

1. Addresses run: **0, 1, 4, 5, 6**.
2. PC after each: 1, **4**, 5, 6, 7.
3. Never run: address 2 (`ADD 11`) and address 3 (`HALT`).
4. R = 20 − 5 = 15, so address 12 contains **15**.

### Task 6

1. The instruction is copied into the **IR** (the PC holds its address).
2. The PC is increased **during fetch**.
3. The **control unit** decodes the instruction; the ALU only does arithmetic and logic.
4. The **MAR** holds the address; the MDR holds the data.
5. Reading **does not change** the location.
6. A branch still goes through fetch, decode and execute; during execute it **overwrites the PC**, so the *next* fetch comes from the target.

### Task 7

| Row | Verdict | Correction |
| --- | --- | --- |
| Address bus carries data | **Wrong** | It carries the **address** (where) |
| Data bus, either direction | **Correct** | — |
| Control bus carries the address | **Wrong** | It carries **control signals** (read/write, timing, interrupts) |
| Address bus both ways | **Wrong** | One way: processor → memory/devices |
| Control bus carries interrupt requests | **Correct** | — |

### Task 8 (Verified)

1. It fetches address 2, which contains data (0), not an instruction.
2. `ERROR: Address 2 holds data (0), not an instruction` (the simulator's message).
3. Fix: `["LOAD 10", "WRITE 10", "HALT", "10: DAT 42"]` → `Outputs: [42]`.

A real processor would not give a friendly message. It would try to run the data as if it were an instruction, which is exactly why stored-program computers need care (Lecture 1, section 14).

### Task 9 (Verified)

- **B:** stores the total at 12 but writes address 13 (still 0), so it outputs `[0]`. Fix: `WRITE 12` → `[5]`.
- **C:** loads 4 and subtracts 10, giving −6. Fix: `LOAD 10` then `SUB 11` → `[6]`.

### Task 10 (Verified)

- **D:** `JUMP 0` sends the loop back to `READ`, which asks for a new input each time round. After outputting 3, it fails with `READ at address 0 needs an input, but none are left`. Fix: `JUMP 1` (back to the `LOAD`). The fixed program outputs `[3, 2, 1]`.
- **D2:** `JUMP 1` is at address 1, so it jumps to itself forever: `Stopped after 200 steps: is there an endless loop?`. Fix: remove the jump, or make it jump to `HALT` (`JUMP 2`).

### Task 11 (Verified)

(a) Steps 1 and 2. (b) `HALT` was fetched from address 6 and uses no data address, so the MAR still holds 6 from the fetch. (c) There are no branches, so the PC only ever increases by 1.

### Task 12 (model answer, Verified)

```python
PROGRAM = ["READ 10",    # 0: A
           "READ 11",    # 1: B
           "LOAD 10",    # 2: R <- A
           "SUB 11",     # 3: R <- A - B (sets LT if B is larger)
           "JUMPN 7",    # 4: if negative, B is larger
           "WRITE 10",   # 5: output A
           "HALT",       # 6
           "WRITE 11",   # 7: output B
           "HALT"]       # 8
```

Results: (4, 9) → `[9]`; (9, 4) → `[9]`; (6, 6) → `[6]`; (0, 3) → `[3]`. All pass.

### Task 13 (Verified)

```python
PROGRAM = ["READ 20", "LOAD 20", "JUMPZ 7", "WRITE 20", "SUB 21", "STORE 20",
           "JUMP 1", "HALT", "20: DAT 0", "21: DAT 1"]
```

Input 3 → `[3, 2, 1]` in 22 steps (the last trace line is step 22). Input 0 → `[]`.

### Task 14

Machine codes for addresses 0–5: **901, 306, 901, 106, 902, 000**; inputs 7 and 5 give output **12** (Verified with the lab's LMC assembler; the website was not run). `306`: opcode **3** = store (STA), address **06** = where FIRST is.

### Task 15 (Verified for gcc 13.3; your website output is Expected)

(a) `mov edx, DWORD PTR [rbp-0x4]` and `mov eax, DWORD PTR [rbp-0x8]` load a and b. (b) `add eax, edx`. (c) `mov DWORD PTR [rip+0x0], eax` stores into total. (d) `01 d0`. (The `[rip+0x0]` shows zero because the final address of `total` is filled in later by the linker.)

### Task 16 (model rows)

| Component | Main role | Example information held or transferred |
| --- | --- | --- |
| Processor | Fetches, decodes and executes instructions | The instruction `ADD 21` in the IR; R = 15 |
| Main memory | Holds the running program and its data | Address 21 holds 9 |
| Secondary storage | Keeps programs and files when power is off | `notes.txt` on the SSD |
| Input/output | Moves data between the computer and the outside world | Key code from the keyboard; pixels to the screen |
| Address bus | Carries the address of the location to access (processor → memory) | 21 |
| Data bus | Carries the data or instruction being transferred, both ways | The value 9, or the instruction `ADD 21` |
| Control bus | Carries control signals such as read, write, clock and interrupt requests | READ |

Main memory and secondary storage are not interchangeable: main memory is fast and volatile and the processor runs programs from it; secondary storage is slower, non-volatile and holds data for later, so programs must be copied into main memory before they can run.

### Task 17 (model answer)

Opcode **LOAD**; destination **R1**; source operand **the contents of memory address 40**.

| Stage | Main component | What happens |
| --- | --- | --- |
| Fetch | PC, MAR, memory, MDR, IR, buses | MAR ← PC (address bus carries it); control unit sends READ; memory puts `LOAD R1, [40]` on the data bus into the MDR; IR ← MDR; PC ← PC + 1 |
| Decode | Control unit | Reads the opcode in the IR (LOAD = data movement), finds the destination R1 and the source address 40, and prepares the control signals |
| Execute | MAR, memory, MDR, R1, buses | MAR ← 40 (address bus); READ signal; memory puts the contents of address 40 on the data bus into the MDR; R1 ← MDR. Address 40 is unchanged |

PC: it already advanced during fetch, so it points to the next instruction in memory, which is fetched next because LOAD does not change the flow of control.

### Task 18

See the comparison table in Lecture 2 section 18.4. Model points: a branch writes a new address into the PC so the next fetch comes from the target (conditional branches only if a flag is set); a subroutine can be called from many places, so the call saves the address of the next instruction and the return puts it back in the PC; an interrupt is triggered by an event, the processor finishes the current instruction, saves the PC and registers, runs the OS's handler, then restores them so the interrupted program continues unchanged. Observation: your own value (Expected).

### Task 19 (model answer, Verified)

```python
PROGRAM = ["READ 20",    # 0: A
           "READ 21",    # 1: B = counter
           "LOAD 21",    # 2: top of loop: counter zero?
           "JUMPZ 11",   # 3: yes -> finished
           "LOAD 22",    # 4: total
           "ADD 20",     # 5: total + A
           "STORE 22",   # 6
           "LOAD 21",    # 7: counter
           "SUB 23",     # 8: counter - 1
           "STORE 21",   # 9
           "JUMP 2",     # 10: back to the top
           "WRITE 22",   # 11: output total
           "HALT",       # 12
           "20: DAT 0", "21: DAT 0", "22: DAT 0", "23: DAT 1"]
```

Results: 3 × 4 → `[12]`; 7 × 0 → `[0]`; 0 × 5 → `[0]`; 6 × 6 → `[36]`; 1 × 9 → `[9]`. All pass. Step counts: 3 × 4 takes **42** steps and 6 × 6 takes **60** (Verified). Each extra unit of B adds 9 more steps (one pass through the 9-instruction loop), so the step count grows in proportion to B: steps = 6 + 9 × B.

### Task 20 (model points)

(a) Four sub-systems (memory, ALU, control unit, I/O); program stored in memory during execution; instructions executed sequentially. (b) Address bus: carries the address, processor to memory; data bus: carries data/instructions both ways; control bus: read/write, timing and interrupt signals. (c) Three-address: `ADD m1, m2, m3` means m3 ← m1 + m2, every location explicit; one-address: `ADD m1` means ACC ← ACC + m1, the accumulator implicit; one-address instructions are shorter but more of them are needed. (d) See Lecture 2 section 17: fetch (MAR ← PC, READ, MDR ← `ADD 21`, IR ← MDR, PC + 1); decode by the control unit; execute (MAR ← 21 on the address bus, READ on the control bus, MDR ← 9 on the data bus, ALU adds 6 + 9, R ← **15**, flags set to GT).
