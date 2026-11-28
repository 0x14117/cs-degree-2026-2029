# ex04_constant_folding.py
# The compiler works out some calculations in advance. This is called constant folding.

import dis

print("--- 60 * 60 * 24 ---")
dis.dis("60 * 60 * 24")

print('--- "Cyber" + "Security" ---')
dis.dis('"Cyber" + "Security"')

print('--- "=" * 20 ---')
dis.dis('"=" * 20')

print('--- "-" * 5000  (too long to fold) ---')
dis.dis('"-" * 5000')
