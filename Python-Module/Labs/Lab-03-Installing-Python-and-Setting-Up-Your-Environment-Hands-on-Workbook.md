# Day 3 Laboratory — Your Setup: Python, Terminal and VS Code

**Part I · Chapter 3 · Day 3** · 25 exercises · Goes with [Lecture 3](../Lectures/Lecture-03-Installing-Python-and-Setting-Up-Your-Environment.md)

## Before you start

**Today's one skill:** using your programming setup confidently. That means checking Python, moving around in the **terminal**, and writing and running files in **VS Code**.

**Python you may use:** only `print()`, as on Days 1 and 2. Today's new skills are terminal commands and VS Code, not Python.

**Terminal commands you will practise:** `python3 --version`, `pwd`, `ls`, `mkdir`, `cd`, `cd ..`, `clear`, `which` / `where.exe`, plus Tab, the up arrow and Ctrl + C.

### How to work

1. Do this lab on **your own laptop** if you can. Use an LJMU machine for anything you cannot do on your laptop, and say so in your notes.
2. Keep a notes file called `lab03_notes.md` in your Lab-03 folder. (You will create `python-labs/Lab-03` in Exercise 4. If you work inside the course repository, use `My-Solutions/Lab-03` instead, and make `python-labs` anyway for practice.) For each exercise, **paste the terminal commands you typed and what the terminal showed**. That is your evidence for review. (Copy from the terminal with the mouse, or Ctrl + Shift + C in many terminals.)
3. Windows users: wherever this lab says `python3`, type `python`. If that does not work, try `py`.
4. Exercises build on each other. Do them in order.
5. Submit after each level for review.

### Levels

| Level | Exercises | What it is for |
| --- | --- | --- |
| 1 | 1–5 | Python is installed, and terminal basics |
| 2 | 6–10 | VS Code, and running files |
| 3 | 11–15 | Speed and confidence in the terminal |
| 4 | 16–20 | Fixing setup problems |
| 5 | 21–25 | Working like a professional |

---

## Level 1 — Python is installed, and terminal basics

### Exercise 1 — Install and check Python

Install Python on your laptop if you have not already (Lecture 3, C.2). Then open a **new** terminal and run:

```bash
python3 --version
```

**Evidence:** paste the output into `lab03_notes.md`, and write which system you use (Windows, macOS or Linux).

**Tests:** Python is installed and the terminal can find it.

---

### Exercise 2 — Where am I?

In a new terminal, run `pwd`.

**Evidence:** paste the output. Then answer in your notes: what is this folder called, and what do you think it is used for? (This is normally your **home folder**.)

**Tests:** `pwd` and the idea of a current folder.

---

### Exercise 3 — What is here?

Run `ls` in your home folder.

**Evidence:** paste the output. Find three folder names you recognise (such as `Documents`, `Downloads` or `Desktop`) and write them down.

**Tests:** `ls`.

---

### Exercise 4 — Build your lab folders

Using only the terminal (no mouse), create this structure inside your home folder or `Documents`:

```text
python-labs/
├── Lab-01/
├── Lab-02/
└── Lab-03/
```

Use `mkdir` and `cd`. After making each folder, check it with `ls`.

**Evidence:** paste every command you typed and the final `ls` of `python-labs`.

**Hint:** Lecture 3, Example 2. If you already use the course repository's `My-Solutions` folders, make this structure anyway, for practice.

**Tests:** `mkdir`, `cd`, `ls` together.

---

### Exercise 5 — Up and down

Starting from `python-labs/Lab-03`, use **only** `cd` and `pwd` to:

1. go up to `python-labs`,
2. go into `Lab-01`,
3. go up and into `Lab-02` **in one command** (hint: `cd ../Lab-02`),
4. go back to your home folder.

Run `pwd` after each step.

**Evidence:** paste the whole session.

**Question:** what does `..` mean?

**Tests:** moving between folders, including `..` inside a path.

---

## Level 2 — VS Code, and running files

### Exercise 6 — Install VS Code and the Python extension

Install VS Code and the **Python** extension published by **Microsoft** (Lecture 3, C.8).

**Evidence:** in your notes, write the version of VS Code (**Help → About** on Windows/Linux, **Code → About Visual Studio Code** on a Mac), and confirm the Python extension shows as installed.

**Tests:** setting up the editor.

---

### Exercise 7 — Open the folder, create a file, run it

1. In VS Code, use **File → Open Folder...** to open `python-labs/Lab-03`.
2. Create a file `ex07_hello_vscode.py` in the Explorer panel.
3. Type a program that shows:

   ```text
   Hello from VS Code!
   This file was written in the editor
   and run in the integrated terminal.
   ```

4. Save it, open the integrated terminal (**Ctrl + `**), and run it with `python3 ex07_hello_vscode.py`.

**Evidence:** paste the output. Also run `pwd` in the integrated terminal and paste that. Which folder is it in, and why?

**Tests:** the full editor-to-terminal workflow.

---

### Exercise 8 — The Run button

Open `ex07_hello_vscode.py` and run it with the **▷** button at the top right.

**Evidence:** paste what appeared in the terminal, including the command VS Code typed for you.

**Question:** the command VS Code typed probably looks longer than `python3 ex07_hello_vscode.py`. What extra information does it include?

**Tests:** the second way to run, and knowing what it does.

---

### Exercise 9 — The unsaved-file trap

1. Make sure **Auto Save is off** (**File → Auto Save** should not be ticked).
2. Change the first line of `ex07_hello_vscode.py` to show `Hello AGAIN from VS Code!`. **Do not save.** Note the white dot on the tab.
3. Run it from the terminal with `python3 ex07_hello_vscode.py`. What appears?
4. Now save and run again.
5. Finally, turn **Auto Save** on, and leave it on.

**Evidence:** paste both outputs, and explain in one sentence why they were different.

**Tests:** understanding that the terminal runs the saved file.

---

### Exercise 10 — Run a file from somewhere else

1. In the terminal, go to your `python-labs` folder (not `Lab-03`).
2. Try `python3 ex07_hello_vscode.py`. What happens, and why?
3. Now run it by giving its path: `python3 Lab-03/ex07_hello_vscode.py`.
4. Go to your home folder and run it again, with the longer path it now needs.

**Evidence:** paste all three attempts.

**Hint:** Lecture 3, C.7 and Example 3. **Tests:** current folder versus path.

---

## Level 3 — Speed and confidence in the terminal

### Exercise 11 — Tab completion

From your home folder, get into `python-labs/Lab-03` by typing **as few letters as possible** and pressing **Tab** to finish each name.

Then run `ex07_hello_vscode.py` using Tab to complete the file name.

**Evidence:** in your notes, write exactly which keys you pressed (for example `cd pyt[Tab]La[Tab]...`).

**Question:** what happens when you press Tab and there are **two** names that start the same way, such as `Lab-01` and `Lab-02`?

**Tests:** using Tab to type less and avoid spelling mistakes.

---

### Exercise 12 — The up arrow

1. Run `python3 ex07_hello_vscode.py`.
2. Run `pwd`, then `ls`.
3. Now press the **up arrow** three times and Enter, so you run the Python file again **without retyping it**.

**Evidence:** describe what each press of the up arrow showed.

**Tests:** command history.

---

### Exercise 13 — Clear the screen, stop a command

1. Run a few commands, then type `clear`. What happened to your files? (Check with `ls`.)
2. Start Python on its own with `python3`. You will see `>>>`. Type `exit()` to leave.
3. Start it again, and this time press **Ctrl + D** (macOS/Linux) or **Ctrl + Z then Enter** (Windows) to leave instead.

**Evidence:** paste what you saw, and write one sentence on what `>>>` means.

**Hint:** Lecture 3, Example 7. **Tests:** controlling the terminal.

---

### Exercise 14 — A file for each day

In `python-labs/Lab-03`, create three files in VS Code: `ex14_monday.py`, `ex14_tuesday.py` and `ex14_friday.py`. Each one prints two lines about what you do on that university day.

Run all three from the terminal **one after another**, using the up arrow and editing only the day's name each time.

**Evidence:** paste all three outputs, and the `ls` of the folder.

**Tests:** fast create-and-run cycles.

---

### Exercise 15 — Read your notes back in the terminal

Show the contents of a file **in the terminal**, without opening VS Code:

- macOS/Linux: `cat ex14_monday.py`
- Windows PowerShell: `cat ex14_monday.py` also works (or `type ex14_monday.py`)

Then show your notes file the same way.

**Question:** what is the difference between `cat ex14_monday.py` and `python3 ex14_monday.py`? Write the output of each.

**Tests:** knowing the difference between **reading** a file and **running** it.

---

## Level 4 — Fixing setup problems

### Exercise 16 — "Command not found"

Deliberately type these, one at a time, and paste what each shows:

```bash
pyhton3 --version
python3 --verison
Python3 --version
```

**Question:** for each one, is the problem with the **command name** (the terminal could not find the program) or with **what you asked the program** to do? How can you tell from the message?

**Tests:** reading terminal messages. (On a Mac, `Python3` with a capital P might work, because macOS ignores capitals in file names. Write down what happens on your computer.)

---

### Exercise 17 — "Can't open file"

Deliberately try each of these, and paste what each shows:

1. Run a file that does not exist: `python3 ex99_missing.py`
2. Misspell a real file: `python3 ex07_helo_vscode.py`
3. Leave out `.py`: `python3 ex07_hello_vscode`

**Question:** look at the path shown in each message. How does it help you find the problem? Is this a Python syntax error, a runtime error, or neither?

**Hint:** Lecture 3, C.7. **Tests:** environment errors versus code errors.

---

### Exercise 18 — Where is Python?

1. Find which Python the terminal uses: `which python3` (macOS/Linux) or `where.exe python` (Windows).
2. In VS Code, open the command palette (**Ctrl + Shift + P**), choose **Python: Select Interpreter**, and look at the list.

**Evidence:** paste the path from step 1, and write the interpreter VS Code shows at the bottom right of its window.

**Question:** do the terminal and VS Code use the same Python? If you have more than one in the list, which version is newest?

**Tests:** PATH, and choosing an interpreter.

---

### Exercise 19 — Spaces in names

1. Make a folder **with a space** in its name: `mkdir "test folder"`.
2. Try to go into it **without** quotes: `cd test folder`. Paste what happens.
3. Now go in **with** quotes: `cd "test folder"`.
4. Go back up, and try Tab completion: type `cd tes` then Tab. What did the terminal type for you?

**Question:** why does this course name everything without spaces?

**Tests:** paths with spaces.

---

### Exercise 20 — Diagnose the problem

A classmate sends you these five problems. For each one, write in your notes **what is wrong** and **the exact fix**. Then, where you safely can, recreate the problem on your own computer to check your answer.

| # | What they say |
| --- | --- |
| a | "I typed `python3 lab1.py` and it said `can't open file`, but I can see `lab1.py` in VS Code!" |
| b | "I installed Python 10 minutes ago, but my terminal says `python: command not found`." |
| c | "I changed my program, but it keeps printing the old message." |
| d | "My terminal now shows `>>>` and none of my commands work." |
| e | "VS Code says my file is `lab1.py.txt`." |

**Tests:** troubleshooting with Lecture 3, section G.

---

## Level 5 — Working like a professional

### Exercise 21 — My setup report

**File:** `ex21_my_setup.py`

Write a program that **prints** a report of your own setup. Find each fact yourself using today's commands, then type it into your `print()` lines:

```text
==============================
        MY PYTHON SETUP
==============================
Computer system:   ...
Python version:    ...
Python location:   ...
Editor:            ...
Lab folder:        ...
Auto Save:         ...
==============================
```

**Tests:** collecting facts about your environment, and Day 1 printing.

---

### Exercise 22 — Keyboard only

Without touching the mouse, do the following, using the terminal for steps 1 to 3:

1. Go to `python-labs/Lab-03`.
2. Make a new folder `keyboard-test` and go into it.
3. Open VS Code in the current folder by typing `code .` (the dot means "this folder").
4. In VS Code, create `ex22_keyboard.py`, type a 3-line program, and save it, all with keyboard shortcuts.
5. Open the integrated terminal with **Ctrl + `** and run the file.

**Evidence:** list every command and shortcut you used.

**Note:** if `code .` gives "command not found" on a Mac, open VS Code, press **Cmd + Shift + P** and run **Shell Command: Install 'code' command in PATH**, then open a new terminal. Write down whether you needed this.

**Tests:** a fast, mouse-free workflow.

---

### Exercise 23 — A setup guide for a classmate

**File:** `ex23_setup_guide.py`

A classmate is starting this course tomorrow and has nothing installed. Write a program that **prints** a clear, step-by-step setup guide for **your** operating system, in your own words. It must cover:

- installing Python and checking it,
- opening a terminal,
- making a lab folder and moving into it,
- installing VS Code and the Python extension,
- creating, saving and running a first file,
- three common problems and their fixes.

It must be at least **25 lines** of output, with headings and numbered steps.

**Tests:** explaining the whole setup, so you know you understand it.

---

### Exercise 24 — Timed drill

Time yourself. Starting from a **brand new** terminal in your home folder:

1. go to `python-labs`,
2. make a folder `drill`,
3. go into it,
4. create `ex24_drill.py` in VS Code that prints `Drill complete`,
5. run it from the terminal,
6. go back to your home folder.

**Evidence:** your time, and every command you typed. Then do it a **second** time and write your new time. Aim for under two minutes.

**Tests:** speed through repetition.

---

### Exercise 25 — Final task: set up the whole course

Get your working area ready for the rest of the course:

1. Make sure `python-labs` has `Lab-01` to `Lab-05` folders (create the missing ones with `mkdir`).
2. Move your Day 1 and Day 2 exercise files into the right folders, if they are not already there. (You can drag them in VS Code's Explorer panel.)
3. In `Lab-03`, write `ex25_check.py`, which prints:

   ```text
   Setup complete.
   Python works.
   The terminal works.
   VS Code works.
   Ready for Day 4.
   ```

4. Run it three ways: from the integrated terminal, with the ▷ button, and from a separate terminal window, using a path, while standing in your home folder.

**Evidence:** an `ls` of `python-labs` and each Lab folder, and the output of all three runs.

**Tests:** everything from today.

---

## Submitting for review

When you finish a level, say **"Review Day 3, Level N"** and share your `lab03_notes.md` and your `.py` files. For each exercise you get:

- ✅ pass, or 🔁 try again
- what went wrong and **why**
- a tip to make it faster or safer

## Progress tracker

| # | Exercise | Attempted | Reviewed |
| --- | --- | --- | --- |
| 1 | Install and check Python | ⬜ | ⬜ |
| 2 | Where am I? | ⬜ | ⬜ |
| 3 | What is here? | ⬜ | ⬜ |
| 4 | Build your lab folders | ⬜ | ⬜ |
| 5 | Up and down | ⬜ | ⬜ |
| 6 | Install VS Code and the Python extension | ⬜ | ⬜ |
| 7 | Open the folder, create a file, run it | ⬜ | ⬜ |
| 8 | The Run button | ⬜ | ⬜ |
| 9 | The unsaved-file trap | ⬜ | ⬜ |
| 10 | Run a file from somewhere else | ⬜ | ⬜ |
| 11 | Tab completion | ⬜ | ⬜ |
| 12 | The up arrow | ⬜ | ⬜ |
| 13 | Clear the screen, stop a command | ⬜ | ⬜ |
| 14 | A file for each day | ⬜ | ⬜ |
| 15 | Read your notes back in the terminal | ⬜ | ⬜ |
| 16 | "Command not found" | ⬜ | ⬜ |
| 17 | "Can't open file" | ⬜ | ⬜ |
| 18 | Where is Python? | ⬜ | ⬜ |
| 19 | Spaces in names | ⬜ | ⬜ |
| 20 | Diagnose the problem | ⬜ | ⬜ |
| 21 | My setup report | ⬜ | ⬜ |
| 22 | Keyboard only | ⬜ | ⬜ |
| 23 | A setup guide for a classmate | ⬜ | ⬜ |
| 24 | Timed drill | ⬜ | ⬜ |
| 25 | Final task: set up the whole course | ⬜ | ⬜ |
