# ex03_compile_is_not_run.py
# Compiling and running are separate steps.
# None of these lines would work if they were RUN, but they all COMPILE without complaint.

import dis

print("--- a name that does not exist ---")
dis.dis("print(undefined_name)")

print("--- dividing by zero ---")
dis.dis("1 / 0")

print("Finished. No error, because nothing above was run.")
