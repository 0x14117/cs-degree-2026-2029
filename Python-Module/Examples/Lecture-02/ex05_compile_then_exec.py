# ex05_compile_then_exec.py
# Do the two steps by hand: compile() makes a code object, exec() runs it.
# The inner call, compile(...), happens first. Its result is handed to exec().

print("Step 1: about to compile and run some code")

exec(compile('print("Hello from a code object")', "<my-code>", "exec"))

print("Step 2: about to compile code with a syntax error")

exec(compile('print("This never runs"', "<broken-code>", "exec"))

print("Step 3: this line is never reached")
