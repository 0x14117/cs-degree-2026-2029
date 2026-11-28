# Python Module — Python Mastery

Self-study Python course, from beginner to professional. Each day teaches **one skill**: one plain-English lecture, plus one hands-on lab of 25 exercises that practise only that skill. Lectures never rely on anything that has not been taught yet.

| # | Lecture | Lab |
| --- | --- | --- |
| 1 | [Introduction to Programming and Python](Lectures/Lecture-01-Introduction-to-Programming-and-Python.md): showing text with `print()` | [Hands-on Workbook (25 exercises)](Labs/Lab-01-Introduction-to-Programming-and-Python-Hands-on-Workbook.md) |
| 2 | [How Programming Languages Work](Lectures/Lecture-02-How-Programming-Languages-Work.md): check first, then run | [Hands-on Workbook (25 exercises)](Labs/Lab-02-How-Programming-Languages-Work-Hands-on-Workbook.md) |
| 3 | [Installing Python and Setting Up Your Environment](Lectures/Lecture-03-Installing-Python-and-Setting-Up-Your-Environment.md): Python, the terminal and VS Code | [Hands-on Workbook (25 exercises)](Labs/Lab-03-Installing-Python-and-Setting-Up-Your-Environment-Hands-on-Workbook.md) |

## How to study a day

1. Read the lecture slowly. Type and run every example in `Examples/Lecture-NN/`.
2. Answer the knowledge check at the end of the lecture before opening the lab.
3. Work through the lab in order. Save each exercise as its own file in `My-Solutions/Lab-NN/`.
4. Ask for a review. Exercises are marked complete only after review.
5. Write a short entry in [LEARNING_LOG.md](LEARNING_LOG.md).

## Course documents

| File | What it is |
| --- | --- |
| [COURSE_ROADMAP.md](COURSE_ROADMAP.md) | The full syllabus: 11 parts, every chapter, in order |
| [PROGRESS.md](PROGRESS.md) | What is done, scores, weak areas, next steps |
| [LEARNING_LOG.md](LEARNING_LOG.md) | Daily notes in my own words |
| [RESOURCES.md](RESOURCES.md) | Official documentation and trusted references |

## Folder layout

```text
Python-Module/
├── Lectures/              Lecture-NN-<topic>.md
├── Labs/                  Lab-NN-<topic>-Hands-on-Workbook.md
├── Examples/Lecture-NN/   code from each lecture, ready to run
├── My-Solutions/Lab-NN/   MY attempts (never overwritten without permission)
├── Reference-Solutions/Lab-NN/   instructor solutions, added only after I attempt
└── Projects/              weekly and end-of-part projects
```

## Conventions

- Python 3 only. Code is checked with Python 3.13 and 3.14. Error message wording can differ slightly between versions.
- Exercise files are named `ex01_hello.py`, `ex02_….py` and so on.
- No virtual environments, caches or secrets in Git (see `.gitignore`).
