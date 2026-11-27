# Python Mastery

A complete, self-paced Python course: from "what is a program?" to network tools, web back ends and production-quality software. It runs alongside my BSc (Hons) Cyber Security degree at LJMU, so later parts lean towards automation, networking and security.

Every learning day has two parts that go together:

1. **A lecture** (`lecture.md`), written like a textbook chapter.
2. **A laboratory** (`lab.md`) with at least 25 hands-on programming exercises in five levels.

## How to study a day

1. Read the lecture slowly. Type and run every example in `examples/`.
2. Answer the knowledge check at the end of the lecture before opening the lab.
3. Work through the lab in order. Save each exercise as its own file in `solutions/my-solutions/`.
4. Ask for a review. Exercises are marked complete only after review.
5. Write a short entry in [LEARNING_LOG.md](LEARNING_LOG.md).

## Course documents

| File | What it is |
| --- | --- |
| [COURSE_ROADMAP.md](COURSE_ROADMAP.md) | The full syllabus: 11 parts, every chapter, in order |
| [PROGRESS.md](PROGRESS.md) | What is done, scores, weak areas, next steps |
| [LEARNING_LOG.md](LEARNING_LOG.md) | Daily notes in my own words |
| [RESOURCES.md](RESOURCES.md) | Official documentation and trusted references |

## Lessons so far

| Day | Part | Chapter | Lecture | Lab |
| --- | --- | --- | --- | --- |
| 1 | I. Foundations | 1. Introduction to Programming and Python | [Lecture](00-Foundations/Chapter-01-Introduction-to-Programming-and-Python/lecture.md) | [Lab (30 exercises)](00-Foundations/Chapter-01-Introduction-to-Programming-and-Python/lab.md) |

## Folder layout

```text
Python-Module/
├── README.md, COURSE_ROADMAP.md, PROGRESS.md, LEARNING_LOG.md, RESOURCES.md
├── 00-Foundations/
│   └── Chapter-01-Introduction-to-Programming-and-Python/
│       ├── lecture.md
│       ├── lab.md
│       ├── examples/            code from the lecture, ready to run
│       └── solutions/
│           ├── my-solutions/    MY attempts (never overwritten without permission)
│           └── reference/       instructor solutions, added only after I attempt
├── 01-Control-Flow/  …  10-Advanced-Development/
├── Projects/
└── Reference/
```

## Conventions

- Python 3 only. Code is checked with Python 3.13 and the 3.15 series. Error message wording can differ slightly between versions.
- Exercise files are named `ex01_hello.py`, `ex02_….py` and so on.
- One commit per learning day at least, with a clear message.
- No virtual environments, caches or secrets in Git (see `.gitignore`).
