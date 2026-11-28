# ex06_print_dis_mistake.py
# DELIBERATE MISTAKE: dis.dis() already prints. Wrapping it in print() adds a stray "None".

import dis

print(dis.dis("2 + 3"))
