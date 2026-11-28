# ex01_which_python.py
# Ask the running interpreter to describe itself.
# "import" loads a module (a toolbox of ready-made code). Chapter 50 covers it fully.

import sys
import platform

print("Version:       ", sys.version)
print("Implementation:", platform.python_implementation())
print("Built with:    ", platform.python_compiler())
print("Cache tag:     ", sys.implementation.cache_tag)
print("Program file:  ", sys.executable)
