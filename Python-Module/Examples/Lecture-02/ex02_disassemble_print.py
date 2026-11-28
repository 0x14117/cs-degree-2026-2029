# ex02_disassemble_print.py
# Show the bytecode that one line of Python turns into.
# dis.dis() compiles the text you give it and prints the instructions. It does not run them.

import dis

dis.dis('print("Hi")')
