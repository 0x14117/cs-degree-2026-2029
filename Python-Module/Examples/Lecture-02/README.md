# Day 2 examples

Code from the lecture, one file per demo. Type each one yourself first, then compare.

| File | Lecture demo |
| --- | --- |
| `ex01_which_python.py` | Demo 1 — Ask Python about itself |
| `ex02_disassemble_print.py` | Demo 2 — Your first disassembly |
| `ex03_compile_is_not_run.py` | Demo 3 — Compiling is not running |
| `ex04_constant_folding.py` | Demo 4 — Constant folding |
| `ex05_compile_then_exec.py` | Demo 5 — Compile, then run, by hand (ends with a deliberate `SyntaxError`) |
| `ex06_print_dis_mistake.py` | Demo 6 — The stray `None` (deliberate mistake) |
| `ex07_pipeline_target.py` | Demo 7 — Feed this file to `-m tokenize`, `-m ast` and `-m dis` |
| `ex08_import_cache/main.py`, `greet.py` | Demo 8 — Importing creates a `__pycache__` |
| `ex09_runtime_error_later.py` | Demo 9 — Python runs two lines, then fails (deliberate `NameError`) |
| `java/Hello.java` | Demo 10 — Java bytecode with `javap -c` |
| `java/Broken.java` | Demo 9 — `javac` refuses to compile (deliberate error) |
| `c/hello.c` | Demo 11 — A native compile with `gcc` |
| `ex10_fake_secret.py` | Demo 12 — A fake secret that survives compilation |

Run any Python example from this folder with `python3 ex01_which_python.py` (or `py ex01_which_python.py` on Windows).

The listings in the lecture come from Python 3.13. On 3.14 or newer, a few instruction names differ (for example `LOAD_SMALL_INT` instead of `RETURN_CONST`). That is expected: bytecode is version-specific.

Generated files (`__pycache__/`, `*.class`, `hello.out`) are ignored by Git. Delete them whenever you like.
