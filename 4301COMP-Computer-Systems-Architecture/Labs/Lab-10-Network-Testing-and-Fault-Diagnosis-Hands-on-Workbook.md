# Lab 10 — Network Testing and Fault Diagnosis Hands-on Workbook (20 Tasks)

**Module:** 4301COMP Computer Systems Architecture

**Session:** Teaching Week 05, Session B · **Matching lecture:** `../Lectures/Lecture-10-Network-Testing-and-Fault-Diagnosis.md`

---

## How to use this lab

**What this lab is for.** You will build a known-good routed network with a web server, break it on purpose, diagnose each fault in dependency order and record it properly. You will also automate the two habits that separate good troubleshooters from guessers: choosing the next check from evidence, and checking for regressions after a repair.

**Where the official tasks are.**

| Official lab sheet (TW05 Session B) | This workbook |
| --- | --- |
| Task 1 — Build a known-good routed baseline | Task 16 |
| Task 2 — Diagnose faults in dependency order | Task 17 |
| Extra Challenge — Diagnose a mask fault | Task 18 |

In the timetabled lab, **do Tasks 16–18 first**.

**Tools**

| Tool | Used in | Notes |
| --- | --- | --- |
| Cisco Packet Tracer 9.0 | Tasks 14, 16–19 | Named on the official sheet |
| Microsoft Word | Tasks 17–18 | For `TW05B_YourStudentID.docx` |
| Windows Command Prompt | Task 13 | Your own computer; read-only commands |
| Python 3 | Tasks 11–12 | **Optional, your choice.** Built-in modules only |
| A Linux system with `sudo` (VM or WSL) | Task 15 | **Optional.** Only if you already have one; nothing extra to install |

**Rules (official and lecture):**

- Write the **expected result before** each test.
- Introduce **one fault at a time**.
- Make the **smallest** repair.
- Repeat the failed test, then run a **regression** check.
- Record what you actually see.

**Labels:**

- **Verified** = run before being written here. The official network was rebuilt as a real Linux network and every fault was tested. Python 3.13 was also used.
- **Expected** = not run here (Packet Tracer, Cisco IOS, Windows).

---

## Part A — Warm-up: claims, order and evidence (Tasks 1–5)

### Task 1 — Write testable claims

**Goal:** turn requirements into tests with expected results (slide 5).

For the official network (PC-A 10.50.10.10, PC-B 10.50.20.10, server 10.50.20.20, router G0/0 10.50.10.1, G0/1 10.50.20.1, all /24), complete each row.

| # | Requirement | Device and test | Expected result |
| --- | --- | --- | --- |
| a | PC-A can use its gateway | | |
| b | The router knows both networks | | |
| c | PC-B and PC-A can talk in both directions | | |
| d | PC-A can see the practice web page | | |
| e | PC-B's settings match the design | | |
| f | The server is reachable from its own LAN | | |

**Expected result:** six rows, each naming one device, one command and one observable outcome.

- **Hint 1:** "Works" is not an expected result. "Replies" or "shows `C 10.50.20.0/24`" is.
- **Hint 2:** Lecture section 6.2's table.

---

### Task 2 — Put the checks in dependency order

**Goal:** apply slide 6.

PC-B cannot load `http://10.50.20.20` from another network. Number these checks 1–8 in the order you should do them, and give each one its layer (1–5).

| Check | Order | Layer |
| --- | --- | --- |
| Open `http://10.50.20.20` in PC-A's browser | | |
| `show ip route` on the router | | |
| Look at PC-B's link light and `show interfaces status` on Switch-B | | |
| `ipconfig` on PC-B | | |
| `show vlan brief` on Switch-B | | |
| `ping 10.50.20.1` from PC-B | | |
| `show ip interface brief` on the router | | |
| `ping 10.50.20.20` from PC-B (same LAN) | | |

**Expected result:** link first, service last.

- **Hint 1:** Layer 2 includes proving that **local** switching works.
- **Hint 2:** Configuration before traffic within each layer is a sensible habit (slide 8).

---

### Task 3 — Configuration check or traffic test?

**Goal:** apply slide 7.

Classify each item and state one thing it **cannot** prove.

1. `ipconfig`
2. `ping 10.50.20.1`
3. `show vlan brief`
4. Opening the web page in a browser
5. `show ip route`
6. `tracert 10.50.20.10`
7. Pinging 127.0.0.1

**Expected result:** 3 configuration checks, 4 traffic tests; each with a limitation.

- **Hint 1:** Does it show what is **set**, or what **happens**?
- **Hint 2:** Loopback is traffic, but it never leaves the computer.

---

### Task 4 — Read the host configuration

**Goal:** apply slide 8 and spot the problem before pinging.

The design for every PC-B row is **10.50.20.10 / 255.255.255.0 / gateway 10.50.20.1**. For each `ipconfig` result, say what is wrong (if anything) and its effect.

| # | Address | Mask | Gateway |
| --- | --- | --- | --- |
| a | 10.50.20.10 | 255.255.255.0 | 10.50.20.254 |
| b | 10.50.20.10 | 255.255.255.252 | 10.50.20.1 |
| c | 169.254.8.10 | 255.255.0.0 | (blank) |
| d | 10.50.20.10 | 255.255.255.0 | 10.50.20.1 |
| e | 10.50.20.10 | 255.255.255.0 | (blank) |
| f | 10.50.20.10 | 255.255.255.248 | 10.50.20.1 |

For b and f, write out the host's subnet range with full working.

**Expected result:** one correct row (d). For b: 10.50.20.8–.11. For f: 10.50.20.8–.15. Both Verified with Python.

- **Hint 1:** /30 → blocks of 4; /29 → blocks of 8.
- **Hint 2:** Is the gateway inside the range you worked out?

---

### Task 5 — Choose the next test

**Goal:** answer slide 13's knowledge check, plus two more.

For each case, give **one** next test and justify it in one sentence.

| Case | Symptom |
| --- | --- |
| A (official) | Client has 169.254.8.10 |
| B (official) | Gateway ping succeeds but remote ping fails |
| C (official) | Server ping succeeds but browser fails |
| D | PC-B's own-IP ping succeeds, but it cannot ping the server on the same LAN |
| E | Every PC in one VLAN can ping each other but not the gateway; other VLANs are fine |

**Expected result:** each answer names a layer and a specific command or check.

- **Hint 1:** D: what does an own-IP ping **not** test? (slide 9)
- **Hint 2:** E: the router or its switch-facing port (Lecture 9).

---

## Part B — Find and fix (Tasks 6–10)

### Task 6 — Fix the troubleshooting log

**Goal:** spot method mistakes in someone else's diagnosis.

Sam Archer's log for "PC-B cannot reach PC-A":

```text
1. Opened the browser on PC-A - page loads, so the web server is fine.
2. Changed PC-B's gateway to 10.50.20.2 and its mask to 255.255.0.0, then rebooted the router.
3. Pinged PC-B's own IP - it worked, so the cable is fine.
4. ping 10.50.10.10 from PC-B - works now. Done.
```

Find **five** method mistakes, then rewrite the log as it should have been done.

**Expected result:** five mistakes covering the expected results, the dependency order, the number of changes, the own-IP claim and the retest.

- **Hint 1:** How many changes were made at step 2?
- **Hint 2:** Slide 15 has four retest steps; how many did Sam do?

---

### Task 7 — Fix the fault records

**Goal:** separate symptom, evidence, root cause and repair (slide 14).

Each record has its parts mixed up or vague. Rewrite each one correctly.

**Record 1.**
- Symptom: G0/1 was administratively down.
- Evidence: PC-B could not reach PC-A.
- Root cause: the network was broken.
- Repair: changed PC-B's address to 10.50.10.20 so it is in the working network.

**Record 2.**
- Symptom: wrong mask.
- Evidence: I think the mask was wrong.
- Root cause: ping failed.
- Repair: set the mask to 255.255.255.0 and also changed the gateway and DNS server, just in case.

**Expected result:** each part in the right box; the repairs are single, smallest changes; the evidence is observations, not opinions.

- **Hint 1:** "Ping failed" is a symptom.
- **Hint 2:** Record 1's repair breaks a rule from the official lab.

---

### Task 8 — Diagnose three mystery faults (real output)

**Goal:** identify faults from real test results.

These are **real results** from the official network rebuilt on Linux (Verified). PC-B's `ipconfig` was correct in all three. Each run has one fault. For each one, give the most likely root cause, the layer, the next check that would prove it, and the repair.

**Baseline (for comparison):**

```text
== Baseline
  pcb  ping 10.50.20.20   (server, same LAN)     REPLY
  pcb  ping 10.50.20.1    (PC-B's configured gw) REPLY
  pcb  ping 10.50.10.10   (remote host PC-A)     REPLY
  pcb  http 10.50.20.20   (web service)          HTTP OK: <h1>Practice page</h1>
  pca  ping 10.50.10.1    (gateway G0/0)         REPLY
  pca  ping 10.50.20.10   (remote host PC-B)     REPLY
  pca  ping 10.50.20.20   (remote server)        REPLY
  pca  http 10.50.20.20   (web service)          HTTP OK: <h1>Practice page</h1>
```

**Mystery 1:**

```text
== Mystery 1
  pcb  ping 10.50.20.20   (server, same LAN)     FAIL (100% packet loss)
  pcb  ping 10.50.20.1    (PC-B's configured gw) FAIL (100% packet loss)
  pcb  ping 10.50.10.10   (remote host PC-A)     FAIL (100% packet loss)
  pcb  http 10.50.20.20   (web service)          HTTP FAIL
  pca  ping 10.50.10.1    (gateway G0/0)         REPLY
  pca  ping 10.50.20.10   (remote host PC-B)     FAIL (100% packet loss)
  pca  ping 10.50.20.20   (remote server)        REPLY
  pca  http 10.50.20.20   (web service)          HTTP OK: <h1>Practice page</h1>
```

**Mystery 2:**

```text
== Mystery 2
  pcb  ping 10.50.20.20   (server, same LAN)     REPLY
  pcb  ping 10.50.20.1    (PC-B's configured gw) REPLY
  pcb  ping 10.50.10.10   (remote host PC-A)     REPLY
  pcb  http 10.50.20.20   (web service)          HTTP FAIL
  pca  ping 10.50.10.1    (gateway G0/0)         REPLY
  pca  ping 10.50.20.10   (remote host PC-B)     REPLY
  pca  ping 10.50.20.20   (remote server)        REPLY
  pca  http 10.50.20.20   (web service)          HTTP FAIL
```

**Mystery 3:**

```text
== Mystery 3
  pcb  ping 10.50.20.20   (server, same LAN)     FAIL (100% packet loss)
  pcb  ping 10.50.20.1    (PC-B's configured gw) FAIL (100% packet loss)
  pcb  ping 10.50.10.10   (remote host PC-A)     FAIL (100% packet loss)
  pcb  http 10.50.20.20   (web service)          HTTP FAIL
  pca  ping 10.50.10.1    (gateway G0/0)         REPLY
  pca  ping 10.50.20.10   (remote host PC-B)     FAIL (100% packet loss)
  pca  ping 10.50.20.20   (remote server)        REPLY
  pca  http 10.50.20.20   (web service)          HTTP OK: <h1>Practice page</h1>
```

Mysteries 1 and 3 give **identical** results. Which extra piece of evidence would tell them apart?

**Expected result:** two layer-1/2 faults and one layer-5 fault.

- **Hint 1:** In Mystery 2, which tests still pass?
- **Hint 2:** For 1 and 3: the link light and `show interfaces status` versus `show vlan brief`.

---

### Task 9 — A repair that caused a regression

**Goal:** see why slide 15's regression check matters.

On the Linux build, PC-B had the official Fault 1 (gateway 10.50.20.254). Instead of fixing PC-B, someone changed the **router's** G0/1 address to 10.50.20.254 "to match". The regression checker compared the results before and after (Verified):

```text
OK          pcb ping 10.50.20.20
FIXED       pcb ping 10.50.20.254
REGRESSION  pcb ping 10.50.20.1
FIXED       pcb ping 10.50.10.10
OK          pcb http 10.50.20.20
OK          pca ping 10.50.10.1
FIXED       pca ping 10.50.20.10
REGRESSION  pca ping 10.50.20.20
REGRESSION  pca http 10.50.20.20

Verdict: NOT finished: 3 test(s) need attention
```

1. Why do PC-B's tests now pass?
2. Why did PC-A lose the web page? (Hint: which gateway does the **server** use?)
3. What should the repair have been?
4. Straight after the bad change, PC-A → server **still worked** for a while. Why? (Lecture section 16.2.)

**Expected result:** the server's gateway explains the regression; the correct repair changes one PC setting.

- **Hint 1:** Three devices use 10.50.20.0/24: PC-B, the server and the router.
- **Hint 2:** ARP caches remember MAC addresses for a few minutes.

---

### Task 10 — The branch printer, three ways

**Goal:** reason like slide 12's worked example.

A printer is at 10.50.20.30. For each evidence set, say where the fault most likely is and the next check.

| Case | Evidence |
| --- | --- |
| a | Users' gateway pings work; other remote services work; printer fails **from every network** |
| b | Printer works from 10.50.20.0/24 but fails from 10.50.10.0/24; other services in 10.50.20.0/24 work from both |
| c | Printer works from everywhere by ping, but no one can print |

**Expected result:** a printer's own port/settings; the printer's **gateway**; the printing service.

- **Hint 1:** In b, the printer's own LAN works. What does it need to reply to another network?
- **Hint 2:** In c, which slide says a successful ping proves something limited?

---

## Part C — Build (Tasks 11–15)

### Task 11 — Encode the diagnosis method

**Goal:** turn slides 6–8 into a tool that names the next check.

**Skill you gain:** you can write down a troubleshooting procedure precisely enough for a program to follow it. That is how runbooks and automated monitoring checks are designed.

1. Save as `diagnose.py`:

```python
# diagnose.py - suggest the next check from configuration and traffic evidence,
# following the bottom-up dependency order on TW05B slide 6:
#   1 device and link  2 VLAN and local switching  3 host address, mask, gateway
#   4 router interface and route  5 transport and application service
# It does not repair anything: it narrows the fault and names the next check.
#
# Usage: python diagnose.py
# Fill in DESIGN (what the host should have) and CASES (what you actually saw).
# A test result is True (worked), False (failed) or None (not tested yet).

import ipaddress

DESIGN = {"address": "10.50.20.10", "mask": "255.255.255.0", "gateway": "10.50.20.1"}


def config_checks(seen, design):
    """Slide 8: read the host configuration before using ping."""
    found = []
    addr = ipaddress.ip_address(seen["address"])
    if addr in ipaddress.ip_network("169.254.0.0/16"):
        return ["address is 169.254.x.x: DHCP failed; check the DHCP server, link and VLAN"]
    want = ipaddress.ip_interface(f"{design['address']}/{design['mask']}").network
    if addr not in want:
        found.append(f"address {addr} is not in the intended network {want}")
    if seen["mask"] != design["mask"]:
        found.append(f"mask {seen['mask']} does not match the design ({design['mask']})")
    mine = ipaddress.ip_interface(f"{seen['address']}/{seen['mask']}").network
    if not seen["gateway"]:
        found.append("no default gateway is set")
    else:
        gw = ipaddress.ip_address(seen["gateway"])
        if gw not in mine:
            found.append(f"gateway {gw} is outside this host's own subnet {mine}")
        if seen["gateway"] != design["gateway"]:
            found.append(f"gateway {gw} does not match the design ({design['gateway']})")
    return found


def diagnose(case, design=DESIGN):
    lines = []
    problems = config_checks(case["ipconfig"], design)
    lines += ["CONFIG: " + p for p in problems] or ["CONFIG: matches the design"]
    t = case["tests"]
    if t.get("link") is False:
        return lines + ["LAYER 1 (device and link): link is down. Next: cable, port lights, "
                        "'show interfaces status' on the switch."]
    if problems:
        return lines + ["LAYER 3 (host settings): fix the configuration item above, then repeat the failed test."]
    if t.get("local_host") is False:
        return lines + ["LAYER 2 (VLAN and local switching): settings are right but a host on the same LAN "
                        "does not answer. Next: 'show vlan brief' and 'show interfaces status' for this exact port."]
    if t.get("gateway") is False:
        return lines + ["LAYER 4 (router interface): the correct gateway does not answer. "
                        "Next: 'show ip interface brief' on the router."]
    if t.get("remote") is False:
        return lines + ["LAYER 4 (routes and return path): gateway works, remote host does not. "
                        "Next: 'show ip route' on the router, then the remote host's address, mask and gateway."]
    if t.get("service") is False:
        return lines + ["LAYER 5 (service): the network path works but the application does not. "
                        "Next: is the service switched on, on the right port, at the right address?"]
    if None in t.values():
        return lines + ["Not enough evidence yet: run the tests marked None, lowest layer first."]
    return lines + ["No fault: every expected result appeared."]


CASES = {
    "Baseline": {"ipconfig": {"address": "10.50.20.10", "mask": "255.255.255.0", "gateway": "10.50.20.1"},
                 "tests": {"link": True, "local_host": True, "gateway": True, "remote": True, "service": True}},
    "Fault 1 (official)": {"ipconfig": {"address": "10.50.20.10", "mask": "255.255.255.0", "gateway": "10.50.20.254"},
                           "tests": {"link": True, "local_host": True, "gateway": False, "remote": False, "service": True}},
    "Fault 2 (official)": {"ipconfig": {"address": "10.50.20.10", "mask": "255.255.255.0", "gateway": "10.50.20.1"},
                           "tests": {"link": True, "local_host": True, "gateway": False, "remote": False, "service": True}},
    "Extra Challenge (/30)": {"ipconfig": {"address": "10.50.20.10", "mask": "255.255.255.252", "gateway": "10.50.20.1"},
                              "tests": {"link": True, "local_host": False, "gateway": False, "remote": False, "service": False}},
    "Case A (slide 13)": {"ipconfig": {"address": "169.254.8.10", "mask": "255.255.0.0", "gateway": ""},
                          "tests": {"link": True, "local_host": None, "gateway": None, "remote": None, "service": None}},
    "Wrong VLAN on PC-B's port": {"ipconfig": {"address": "10.50.20.10", "mask": "255.255.255.0", "gateway": "10.50.20.1"},
                                  "tests": {"link": True, "local_host": False, "gateway": False, "remote": False, "service": False}},
    "Case C (slide 13)": {"ipconfig": {"address": "10.50.20.10", "mask": "255.255.255.0", "gateway": "10.50.20.1"},
                          "tests": {"link": True, "local_host": True, "gateway": True, "remote": True, "service": False}},
}

if __name__ == "__main__":
    for name, case in CASES.items():
        print(f"== {name}")
        for line in diagnose(case):
            print("   " + line)
```

2. Run `python diagnose.py`. *What it does:* prints a suggested next check for each case in `CASES`; it touches no real network. Actual output (Verified):

```text
== Baseline
   CONFIG: matches the design
   No fault: every expected result appeared.
== Fault 1 (official)
   CONFIG: gateway 10.50.20.254 does not match the design (10.50.20.1)
   LAYER 3 (host settings): fix the configuration item above, then repeat the failed test.
== Fault 2 (official)
   CONFIG: matches the design
   LAYER 4 (router interface): the correct gateway does not answer. Next: 'show ip interface brief' on the router.
== Extra Challenge (/30)
   CONFIG: mask 255.255.255.252 does not match the design (255.255.255.0)
   CONFIG: gateway 10.50.20.1 is outside this host's own subnet 10.50.20.8/30
   LAYER 3 (host settings): fix the configuration item above, then repeat the failed test.
== Case A (slide 13)
   CONFIG: address is 169.254.x.x: DHCP failed; check the DHCP server, link and VLAN
   LAYER 3 (host settings): fix the configuration item above, then repeat the failed test.
== Wrong VLAN on PC-B's port
   CONFIG: matches the design
   LAYER 2 (VLAN and local switching): settings are right but a host on the same LAN does not answer. Next: 'show vlan brief' and 'show interfaces status' for this exact port.
== Case C (slide 13)
   CONFIG: matches the design
   LAYER 5 (service): the network path works but the application does not. Next: is the service switched on, on the right port, at the right address?
```

3. Add a case for **Mystery 2** from Task 8 and run it. Does it agree with your answer?
4. Add a case for slide 13 **Case B** (`gateway: True`, `remote: False`). Which layer does it name?
5. **Extend:** add a check that the address is not the **network** or **broadcast** address of its subnet. Test it with address 10.50.20.0.

**Expected result:** Mystery 2 → layer 5; Case B → layer 4 (routes and return path).

- **Hint 1:** Each case has an `ipconfig` dictionary and a `tests` dictionary; `None` means "not tested yet".
- **Hint 2:** For step 5: `if addr in (mine.network_address, mine.broadcast_address):`.

---

### Task 12 — Automate the regression check

**Goal:** compare test runs before and after a repair (slide 15).

**Skill you gain:** you can compare two sets of test results automatically, which is how change-management and CI pipelines catch regressions.

1. Save as `retest.py`:

```python
# retest.py - compare a test run before and after a repair (TW05B slide 15).
# For every test it reports:
#   FIXED       failed before, works now        (the repair worked)
#   REGRESSION  worked before, fails now        (the repair broke something else)
#   STILL FAIL  failed both times
#   OK          worked both times
#
# Usage: python retest.py before.txt after.txt
# Each file has one test per line: "<test name> | PASS" or "<test name> | FAIL".
# (It also reads the output of the Linux build in Lab 10 Task 15.)

import re
import sys


def load(path):
    results = {}
    for line in open(path, encoding="utf-8"):
        if "|" in line:                                  # simple format: name | PASS
            name, result = (part.strip() for part in line.rsplit("|", 1))
            results[name] = result.upper().startswith("PASS")
        else:                                            # Task 15 format
            m = re.match(r"\s+(\w+)\s+(ping \S+|http \S+)\s+.*?\s(REPLY|HTTP OK|FAIL|HTTP FAIL|NONE)", line)
            if m and "(gateway)" not in m.group(2):
                results[f"{m.group(1)} {m.group(2)}"] = m.group(3) in ("REPLY", "HTTP OK")
    return results


def compare(before, after):
    rows = []
    for name in after:
        if name not in before:
            rows.append(("NEW", name))
            continue
        b, a = before[name], after[name]
        status = {(False, True): "FIXED", (True, False): "REGRESSION",
                  (False, False): "STILL FAIL", (True, True): "OK"}[(b, a)]
        rows.append((status, name))
    return rows


if __name__ == "__main__":
    before, after = load(sys.argv[1]), load(sys.argv[2])
    rows = compare(before, after)
    for status, name in rows:
        print(f"{status:<11} {name}")
    bad = [n for s, n in rows if s in ("REGRESSION", "STILL FAIL")]
    print("\nVerdict:", "repair confirmed, no regressions" if not bad else f"NOT finished: {len(bad)} test(s) need attention")
```

2. Create `before.txt`:

   ```text
   PC-B ping server | PASS
   PC-B ping gateway | FAIL
   PC-B ping PC-A | FAIL
   PC-B web page | PASS
   ```

   and `after.txt`:

   ```text
   PC-B ping server | FAIL
   PC-B ping gateway | PASS
   PC-B ping PC-A | PASS
   PC-B web page | PASS
   ```

3. Run `python retest.py before.txt after.txt`. *What it does:* reads both files and compares each test; nothing is sent over the network. Actual output (Verified):

   ```text
   REGRESSION  PC-B ping server
   FIXED       PC-B ping gateway
   FIXED       PC-B ping PC-A
   OK          PC-B web page

   Verdict: NOT finished: 1 test(s) need attention
   ```

4. Use it on your **own** Task 17 results: write `before.txt` from Fault 2 and `after.txt` from the retest.
5. Real comparison from the Linux build, Fault 2 before and after `no shutdown` (Verified):

   ```text
   OK          pcb ping 10.50.20.20
   FIXED       pcb ping 10.50.20.1
   FIXED       pcb ping 10.50.10.10
   OK          pcb http 10.50.20.20
   OK          pca ping 10.50.10.1
   FIXED       pca ping 10.50.20.10
   FIXED       pca ping 10.50.20.20
   FIXED       pca http 10.50.20.20

   Verdict: repair confirmed, no regressions
   ```

**Expected result:** your Fault 2 comparison shows only FIXED and OK lines.

- **Hint 1:** The test names must be **identical** in both files.
- **Hint 2:** A REGRESSION line means: stop, the repair is not finished.

---

### Task 13 — Run the ping sequence on your own computer

**Goal:** apply slides 8–9 to a real network you use.

**Skill you gain:** you can diagnose your own connection in a logical order, the first thing any IT support or security role expects.

On **your own Windows computer** (Expected; read-only commands that change nothing):

1. `ipconfig` *(shows your settings)*. Record your IPv4 address, mask and default gateway. Is the address 169.254.x.x?
2. `ping 127.0.0.1` *(tests your TCP/IP software only)*.
3. `ping <your own IPv4 address>` *(tests your interface configuration only)*.
4. `ping <your default gateway>` *(tests your link, Wi-Fi or switch, and the gateway)*.
5. `ping 1.1.1.1` *(a well-known public address: tests the route beyond your gateway)*.
6. `nslookup www.ljmu.ac.uk` *(tests DNS, an application service)*.
7. Open `https://www.ljmu.ac.uk` in a browser *(tests HTTPS)*.

Before each step, write the expected result. Then, **with Wi-Fi switched off or the cable unplugged**, repeat steps 2–4. Which still succeed, and why?

The same experiment on Linux, with the interface down (Verified):

```text
ping 127.0.0.1    -> 64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.020 ms
ping 10.50.20.10  -> 64 bytes from 10.50.20.10: icmp_seq=1 ttl=64 time=0.013 ms   (its own IP)
ping 10.50.20.20  -> ping: connect: Network is unreachable
```

**Expected result:** with the link off, steps 2 and 3 still succeed; step 4 fails. (Windows may remove the address when the link goes down, in which case step 3 has nothing to ping: record what you see.) Some networks block ping to the gateway or the internet: record a timeout and move on to the next step.

- **Hint 1:** University networks sometimes block ICMP; your home network usually does not.
- **Hint 2:** Do not use these commands against networks you are not permitted to test.

---

### Task 14 — Watch the mask fault in Simulation mode

**Goal:** see the evidence behind the Extra Challenge (official optional step).

**Skill you gain:** you can inspect ARP and ICMP packets layer by layer, which is the basis of packet analysis with tools such as Wireshark.

Using a copy of your Task 18 fault file (Expected):

1. **Simulation** > **Edit Filters**: tick only **ARP** and **ICMP**.
2. On PC-B, `ping 10.50.20.20`. Click **Capture/Forward** step by step.
3. Click an envelope in the **Event List** > **Info** > **OSI Model**. Record what PC-B does first: does it ARP for the **server** or for the **gateway**? Does it send anything at all?
4. Repeat for `ping 10.50.20.1`.
5. Return to **Realtime**. Fix the mask and repeat step 2. What changed in the first event?

**Expected result:** with the correct /24, PC-B ARPs for 10.50.20.20 directly. With /30, it treats .20 as remote, so its behaviour depends on how Packet Tracer handles a gateway outside the subnet. Record exactly what you see.

- **Hint 1:** Lecture section 17 explains why systems differ.
- **Hint 2:** The OSI Model view shows the decision at each layer in plain words.

---

### Task 15 — Build the official network as a real Linux network (optional)

**Goal:** run the official baseline and faults on real network software, not a simulator.

**Skill you gain:** you can build an isolated test network with Linux network namespaces, a standard way to test routing and firewall changes safely.

**Only if you already have a Linux system with `sudo`** (a VM or WSL 2). It uses `ip`, `ping`, `curl` and `python3`, which are normally already present. It changes nothing outside the test network, and `clean` removes everything.

1. Save as `build_net.sh`:

```bash
#!/bin/bash
# build_net.sh - build the official TW05B network as real Linux network namespaces.
# Each namespace is a separate network stack: its own interfaces, addresses, routes and ARP table.
#   pca  = PC-A            10.50.10.10/24  gw 10.50.10.1
#   rtr  = Router          g00 10.50.10.1/24   g01 10.50.20.1/24  (IP forwarding on)
#   pcb  = PC-B            10.50.20.10/24  gw 10.50.20.1
#   srv  = Service-Server  10.50.20.20/24  gw 10.50.20.1  (HTTP on port 80)
#   swa, swb = Linux bridges acting as Switch-A and Switch-B
# Needs root. Usage: sudo bash build_net.sh      (remove with: sudo bash build_net.sh clean)
set -e
clean() {
  for n in pca pcb srv rtr; do ip netns del $n 2>/dev/null || true; done
  ip link del swa 2>/dev/null || true; ip link del swb 2>/dev/null || true
}
clean
[ "$1" = "clean" ] && exit 0
for n in pca pcb srv rtr; do ip netns add $n; ip -n $n link set lo up; done
ip link add swa type bridge; ip link set swa up
ip link add swb type bridge; ip link set swb up
# cable NAME-in-namespace  NAMESPACE  bridge-port-name  bridge
cable() { ip link add $1 netns $2 type veth peer name $3; ip link set $3 master $4 up; ip -n $2 link set $1 up; }
cable eth0 pca a-fa01 swa       # PC-A Fa0 -> Switch-A Fa0/1
cable g00  rtr a-fa24 swa       # Router G0/0 -> Switch-A Fa0/24
cable g01  rtr b-fa24 swb       # Router G0/1 -> Switch-B Fa0/24
cable eth0 pcb b-fa01 swb       # PC-B Fa0 -> Switch-B Fa0/1
cable eth0 srv b-fa02 swb       # Server Fa0 -> Switch-B Fa0/2
ip -n rtr addr add 10.50.10.1/24 dev g00
ip -n rtr addr add 10.50.20.1/24 dev g01
ip netns exec rtr sysctl -qw net.ipv4.ip_forward=1
ip -n pca addr add 10.50.10.10/24 dev eth0; ip -n pca route add default via 10.50.10.1
ip -n pcb addr add 10.50.20.10/24 dev eth0; ip -n pcb route add default via 10.50.20.1
ip -n srv addr add 10.50.20.20/24 dev eth0; ip -n srv route add default via 10.50.20.1
mkdir -p /tmp/tw05b_www && echo '<html><body><h1>Practice page</h1></body></html>' > /tmp/tw05b_www/index.html
ip netns exec srv python3 -m http.server 80 --bind 10.50.20.20 --directory /tmp/tw05b_www >/tmp/tw05b_http.log 2>&1 &
sleep 1
echo "network built"
```

2. Save as `tests.sh`:

```bash
#!/bin/bash
# tests.sh LABEL - run the official TW05B test sequence from PC-B (and PC-A), one line per test.
p() { # namespace target description
  if ip netns exec $1 ping -c 2 -W 1 -q $2 >/tmp/p.txt 2>&1; then r=REPLY; else r="FAIL ($(grep -oE 'Network is unreachable|[0-9]+% packet loss' /tmp/p.txt | head -1))"; fi
  printf "  %-4s %-18s %-22s %s\n" $1 "ping $2" "$3" "$r"; }
h() { if out=$(ip netns exec $1 curl -s -m 3 http://10.50.20.20/ 2>&1); then r="HTTP OK: $(echo "$out" | grep -o '<h1>.*</h1>')"; else r="HTTP FAIL"; fi
  printf "  %-4s %-18s %-22s %s\n" $1 "http 10.50.20.20" "(web service)" "$r"; }
echo "== $1"
p pcb 10.50.20.20 "(server, same LAN)"
GW=$(ip -n pcb route show default | awk '{print $3}')
if [ -n "$GW" ]; then p pcb $GW "(PC-B's configured gw)"; else printf "  %-4s %-18s %-22s %s\n" pcb "ping (gateway)" "(PC-B's configured gw)" "NONE: no default route accepted"; fi
[ "$GW" != "10.50.20.1" ] && p pcb 10.50.20.1 "(router G0/1)"
p pcb 10.50.10.10 "(remote host PC-A)"
h pcb
p pca 10.50.10.1  "(gateway G0/0)"
p pca 10.50.20.10 "(remote host PC-B)"
p pca 10.50.20.20 "(remote server)"
h pca
```

3. Run `sudo bash build_net.sh`, then `sudo bash tests.sh Baseline`. *What they do:* the first creates the four "devices" and two "switches"; the second runs the official test sequence. Actual output (Verified):

   ```text
   == Baseline
     pcb  ping 10.50.20.20   (server, same LAN)     REPLY
     pcb  ping 10.50.20.1    (PC-B's configured gw) REPLY
     pcb  ping 10.50.10.10   (remote host PC-A)     REPLY
     pcb  http 10.50.20.20   (web service)          HTTP OK: <h1>Practice page</h1>
     pca  ping 10.50.10.1    (gateway G0/0)         REPLY
     pca  ping 10.50.20.10   (remote host PC-B)     REPLY
     pca  ping 10.50.20.20   (remote server)        REPLY
     pca  http 10.50.20.20   (web service)          HTTP OK: <h1>Practice page</h1>
   ```

4. Create the official faults one at a time, then repair each:

   | Fault | Create | Repair |
   | --- | --- | --- |
   | 1 Wrong gateway | `sudo ip -n pcb route replace default via 10.50.20.254` | `sudo ip -n pcb route replace default via 10.50.20.1` |
   | 2 G0/1 shut down | `sudo ip -n rtr link set g01 down` | `sudo ip -n rtr link set g01 up` |
   | 3 /30 mask | `sudo ip -n pcb addr flush dev eth0` then `sudo ip -n pcb addr add 10.50.20.10/30 dev eth0` then `sudo ip -n pcb route add default via 10.50.20.1` | Flush, then add `10.50.20.10/24` and the default route again |

5. After each fault, run `sudo bash tests.sh "Fault N"` and compare with the baseline. Also try `sudo ip -n rtr route` during Fault 2.
6. Finish with `sudo bash build_net.sh clean`.

Real Fault 1 output (Verified):

```text
== Fault 1: PC-B default gateway set to 10.50.20.254
  pcb  ping 10.50.20.20   (server, same LAN)     REPLY
  pcb  ping 10.50.20.254  (PC-B's configured gw) FAIL (100% packet loss)
  pcb  ping 10.50.20.1    (router G0/1)          REPLY
  pcb  ping 10.50.10.10   (remote host PC-A)     FAIL (100% packet loss)
  pcb  http 10.50.20.20   (web service)          HTTP OK: <h1>Practice page</h1>
  pca  ping 10.50.10.1    (gateway G0/0)         REPLY
  pca  ping 10.50.20.10   (remote host PC-B)     FAIL (100% packet loss)
  pca  ping 10.50.20.20   (remote server)        REPLY
  pca  http 10.50.20.20   (web service)          HTTP OK: <h1>Practice page</h1>
```

**Expected result:** your results match those in lecture section 17. For Fault 3, Linux refuses the gateway: `Error: Nexthop has invalid gateway.`

- **Hint 1:** On Linux, setting an interface **down** with `ip link set` deletes its routes. After bringing it back up, add the default route again (this happened during testing).
- **Hint 2:** If a test fails straight after a repair, wait a few seconds and run it again.

---

## Part D — Official tasks and integration (Tasks 16–20)

### Task 16 — Build a known-good routed baseline (Official Task 1)

**Goal:** build, test and record a working baseline with a web service.

**Skill you gain:** you can establish a tested baseline before changing anything, the reference point for all later diagnosis.

**Official steps**

1. **1.1:** Open Cisco Packet Tracer 9.0 (sign in if prompted). Work in the **Logical workspace**; all configuration is inside the simulation, not Windows.
   - Add one **1941** router, two **2960-24TT** switches, two **PC-PT** devices and one **Server-PT**.
   - Rename them (**Config > Global Settings > Display Name**) **Router**, **Switch-A**, **Switch-B**, **PC-A**, **PC-B** and **Service-Server**.
   - With **Copper Straight-Through**, connect:
     - PC-A Fa0 → Switch-A **Fa0/1**
     - Switch-A **Fa0/24** → Router **G0/0**
     - Router **G0/1** → Switch-B **Fa0/24**
     - PC-B Fa0 → Switch-B **Fa0/1**
     - Server Fa0 → Switch-B **Fa0/2**
2. **1.2:** **Router > CLI**. Answer **no** to the initial configuration dialog and press **Enter** again. Type each command on its own line:

   ```text
   enable
   configure terminal
   interface g0/0
   ip address 10.50.10.1 255.255.255.0
   no shutdown
   exit
   interface g0/1
   ip address 10.50.20.1 255.255.255.0
   no shutdown
   end
   show ip interface brief
   show ip route
   ```

   Expect G0/0 and G0/1 **up/up** and connected routes for both /24 networks. Wait for green links (or **Fast Forward Time**). A first ping can lose a reply while ARP resolves; repeat it before diagnosing a fault.
3. **1.3:** **Desktop > IP Configuration > Static**:
   - **PC-A:** 10.50.10.10, 255.255.255.0, gateway 10.50.10.1.
   - **PC-B:** 10.50.20.10, the same mask, gateway 10.50.20.1.
4. **1.4:** **PC-A > Command Prompt:** `ipconfig`, `ping 10.50.10.1`, `ping 10.50.20.10`. **PC-B:** `ipconfig`, `ping 10.50.20.1`, `ping 10.50.10.10`. All should eventually reply.
5. **1.5:** Save as **TW05B_Baseline_YourStudentID.pkt**. Capture `show ip interface brief` and one successful remote ping.
6. **1.6:** **Service-Server > Desktop > IP Configuration > Static:** 10.50.20.20, 255.255.255.0, gateway 10.50.20.1. Then:
   - **Services > HTTP > On**.
   - **index.html > Edit**: enter `<html><body><h1>Practice page</h1></body></html>` and click **Save**.
   - From **PC-B > Command Prompt**: `ping 10.50.20.20`.
7. **1.7:** From **PC-A**: `ping 10.50.20.20`, then **Desktop > Web Browser** → `http://10.50.20.20`. Capture both results to distinguish **routed connectivity** from a **working application service**. Save.

**Baseline test plan** (write the expected column first)

| # | From | Test | Expected | Actual |
| --- | --- | --- | --- | --- |
| 1 | Router | `show ip interface brief` | G0/0, G0/1 up/up | |
| 2 | Router | `show ip route` | `C` 10.50.10.0/24 and 10.50.20.0/24 | |
| 3 | PC-A | `ping 10.50.10.1` | Replies | |
| 4 | PC-A | `ping 10.50.20.10` | Replies | |
| 5 | PC-B | `ping 10.50.20.1` | Replies | |
| 6 | PC-B | `ping 10.50.10.10` | Replies | |
| 7 | PC-B | `ping 10.50.20.20` | Replies | |
| 8 | PC-A | `ping 10.50.20.20` | Replies | |
| 9 | PC-A | `http://10.50.20.20` | "Practice page" | |

- **Hint 1:** Task 15's Linux baseline shows the same tests passing (Verified).
- **Hint 2:** If the page fails but the ping works, check that **HTTP is On** (layer 5).

---

### Task 17 — Diagnose faults in dependency order (Official Task 2)

**Goal:** diagnose two faults, one at a time, and record them.

**Official steps**

1. **2.1:** **File > Save As** `TW05B_Faults_YourStudentID.pkt`. Introduce only one fault at a time. On **PC-B > IP Configuration**, change **Default Gateway** to **10.50.20.254**. Diagnose in this order:
   - Check the cables and link indicators.
   - At each switch: `enable`, then `show interfaces status`.
   - On PC-B: `ipconfig`.
   - At `Router#`: `show ip interface brief` and `show ip route`.
   - On PC-B: `ping 10.50.20.20` (server), `ping 10.50.20.254` (configured gateway), `ping 10.50.10.10` (remote host), then `http://10.50.20.20` in the Web Browser.

   Local server tests should work, while the incorrect gateway and the remote ping fail. A ping to the PC's own IP tests only that host, not its cable.
2. **2.2:** Use `ipconfig` on PC-B and compare it with the design. Correct the gateway to **10.50.20.1** and repeat the failed remote ping. Repeat the server ping or HTTP test as a **regression check**.
3. **2.3:** Create a router-interface fault. At `Router#`:

   ```text
   configure terminal
   interface g0/1
   shutdown
   ```

   On PC-B check its link to Switch-B and run `ipconfig`, `ping 10.50.20.20`, `ping 10.50.20.1`, then `ping 10.50.10.10`. The server is local to PC-B and should still respond; the router gateway and the remote host should fail.
4. **2.4:** At `Router(config-if)#`:

   ```text
   do show ip interface brief
   no shutdown
   end
   show ip interface brief
   ```

   Check that G0/1 changes from **administratively down** to **up/up**. Wait for green links, then:
   - repeat the server test as a regression check;
   - then repeat the gateway and remote-host pings.

   **Do not change a correct PC address to repair a router-interface fault.**
5. **2.5:** Create **TW05B_YourStudentID.docx**. For each fault, record the symptom, evidence, root cause, repair and retest, with one relevant screenshot.

**Expected results** (Verified on the Linux build; Packet Tracer Expected)

| PC-B test | Fault 1 (gw .254) | Fault 2 (G0/1 shut) |
| --- | --- | --- |
| `ping 10.50.20.20` | Replies | Replies |
| `ping` configured gateway | **Fails** (.254) | **Fails** (.1) |
| `ping 10.50.10.10` | **Fails** | **Fails** |
| Web page | Loads | Loads |
| What proves the cause | `ipconfig` gateway ≠ design | `show ip interface brief`: administratively down; no `C 10.50.20.0/24` |

**Fault record template**

| | Fault 1 | Fault 2 |
| --- | --- | --- |
| Symptom | | |
| Evidence | | |
| Root cause | | |
| Repair | | |
| Retest (failed test) | | |
| Regression check | | |

- **Hint 1:** In Fault 1, try PC-A → PC-B too. It fails even though PC-A is perfect. Why? (Lecture section 14.)
- **Hint 2:** Lecture section 15.2 is a complete model record for Fault 2.

---

### Task 18 — Diagnose a mask fault (Official Extra Challenge)

**Goal:** diagnose a fault that a configuration check finds faster than any ping.

**Official steps**

1. **E.1:** After restoring the baseline, change **only** PC-B's mask to **255.255.255.252** in **IP Configuration**. The resulting /30 makes its configured gateway fall outside its local subnet. Run `ipconfig`, then the server, gateway and remote-host tests above, and **record the observed outcomes**.
   - *Optional packet inspection:* **Simulation > Edit Filters > ARP** and **ICMP**; run a ping; **Capture/Forward**; click an **Event List Info** square > **OSI Model**. Return to **Realtime** afterwards. (Task 14 covers this in detail.)
2. **E.2:** Correct PC-B's mask to **255.255.255.0** and repeat the gateway and remote-host tests.
3. **E.3:** Add the third fault record to your Word document and state the **smallest evidence-supported repair**.

**Working (Verified):** /30 → blocks of 4; 10.50.20.10 is in **10.50.20.8–10.50.20.11** (usable .9–.10). Gateway .1 and server .20 are outside.

| Test | Linux, gateway refused (Verified) | Linux, gateway forced in (Verified) | Packet Tracer (record yours) |
| --- | --- | --- | --- |
| `ipconfig` / settings | /30; Linux rejects the gateway | /30 with off-subnet gateway | |
| `ping 10.50.20.20` | Fail (Network is unreachable) | Reply | |
| `ping 10.50.20.1` | Fail | Reply | |
| `ping 10.50.10.10` | Fail | Reply | |

- **Hint 1:** If every ping works in Packet Tracer, the fault still exists. `ipconfig` shows it.
- **Hint 2:** The smallest repair changes one value.

---

### Task 19 — Mini-project: a test plan and fault hunt for your Lab 9 network

**Goal:** apply the full method to the segmented network you built in Lab 9.

**Skill you gain:** you can write a complete test plan, including negative tests, and use it to find and record faults. This is the same evidence an AS1-style design explanation needs.

1. Open your working **Lab 9 Task 17** file (two VLANs, 2911 router). Save a copy.
2. **Test plan:** write at least **12** testable claims, covering:
   - every layer from slide 6;
   - at least one claim per VLAN;
   - both directions between VLANs;
   - at least one **negative** test that is expected to fail (for example, PC1 → PC3 with routing removed, or a ping to an unused address).
3. Run the plan on the working network and record the **baseline**.
4. **Fault hunt.** Ask a classmate to introduce **three** faults one at a time without telling you what they are. Working alone? Copy the file and introduce them yourself from this list, then wait a day before diagnosing:
   - a wrong access VLAN;
   - a shut router interface;
   - a wrong gateway;
   - a wrong mask;
   - a router-facing port in the wrong VLAN.
5. For each fault, write a full fault record. Use `diagnose.py` (Task 11) as a second opinion and `retest.py` (Task 12) for the regression check.
6. Write a 150-word reflection: which test in your plan found faults fastest, and which test you would add.

**Expected result:** a 12+ row test plan with a baseline column, three fault records, and three retest comparisons with no regressions.

- **Hint 1:** Lecture 9 section 12's fault-to-check table is a good source of claims.
- **Hint 2:** A negative test that unexpectedly **passes** is also a finding.

---

### Task 20 — Assessment-style practice: testing and diagnosis

**This is practice only, not a real exam question.** The module exam is two hours with short-answer and essay-style questions; the report covers data storage and networking (module guide). Check the real AS1 brief on Canvas. The marks below are invented for planning.

**Rules:** 25 minutes, closed book, write it yourself.

**(a)** Explain the difference between a configuration check and a traffic test, giving one example and one limitation of each. *(4 marks)*

**(b)** Explain why network faults should be diagnosed from the bottom layer upwards. *(3 marks)*

**(c)** A user's PC can ping a server on its own LAN but cannot reach any other network. Describe, in order, the checks you would make and what each would show. *(5 marks)*

**(d)** Using a fault of your choice, write a complete fault record. Explain why retesting must include regression checks, with an example of a repair that could cause a regression. *(8 marks; aim for 250–350 words)*

**Self-marking checklist**

| Part | A good answer includes | Expected | Actual |
| --- | --- | --- | --- |
| (a) | Settings vs real delivery; e.g. `ipconfig` / `ping`; configuration does not prove delivery; ping does not prove the service | 4 points | |
| (b) | Higher layers depend on lower ones; skipping makes failures ambiguous; one low-level fault causes many symptoms | 3 points | |
| (c) | `ipconfig` (gateway, mask) → ping gateway → router `show ip interface brief` / `show ip route` → remote host's settings | 5 points | |
| (d) | Symptom, evidence, root cause, smallest repair, retest; regression example (e.g. readdressing a router to match one PC) | 8 points | |
| Time | Within 25 minutes | Yes | |

- **Hint 1:** Use one of the official lab faults as your example in (d).
- **Hint 2:** Lecture sections 8, 12, 15 and 16.

---

## Tracker

| Task | Name | Done | Notes / score |
| --- | --- | --- | --- |
| 1 | Write testable claims | ☐ | /6 |
| 2 | Dependency order | ☐ | /8 |
| 3 | Configuration or traffic? | ☐ | /7 |
| 4 | Read the host configuration | ☐ | /6 |
| 5 | Choose the next test | ☐ | /5 |
| 6 | Fix the troubleshooting log | ☐ | /5 |
| 7 | Fix the fault records | ☐ | /2 |
| 8 | Three mystery faults | ☐ | /3 |
| 9 | Repair with a regression | ☐ | /4 |
| 10 | The branch printer | ☐ | /3 |
| 11 | `diagnose.py` | ☐ | |
| 12 | `retest.py` | ☐ | |
| 13 | Own-computer ping sequence | ☐ | |
| 14 | Simulation mode: mask fault | ☐ | |
| 15 | Real Linux network (optional) | ☐ | |
| 16 | **Official Task 1**: Baseline | ☐ | |
| 17 | **Official Task 2**: Two faults | ☐ | |
| 18 | **Official Extra Challenge**: Mask fault | ☐ | |
| 19 | Mini-project: test plan and fault hunt | ☐ | |
| 20 | Assessment-style practice | ☐ | /20 |

## Reflection

1. Which fault took you longest to diagnose, and which single check would have found it fastest?
2. Did writing the expected result first ever stop you from misreading a result? Give an example.
3. In Task 18, how did Packet Tracer handle the off-subnet gateway, and what does that teach you about relying only on ping?
4. How would you use a baseline and regression checks to prove that a firewall rule works, both for allowed and blocked traffic?

---

## Answer key

**(Verified)** = real Linux namespaces build, or Python 3.13. **(Expected)** = Packet Tracer, Cisco IOS or Windows; not run here.

### Task 1

- a. PC-A `ping 10.50.10.1` → replies.
- b. Router `show ip route` → `C 10.50.10.0/24` and `C 10.50.20.0/24`.
- c. PC-A `ping 10.50.20.10` **and** PC-B `ping 10.50.10.10` → both reply.
- d. PC-A browser `http://10.50.20.20` → "Practice page".
- e. PC-B `ipconfig` → 10.50.20.10, 255.255.255.0, 10.50.20.1.
- f. PC-B `ping 10.50.20.20` → replies.

### Task 2

1. Link light / `show interfaces status` (layer 1)
2. `show vlan brief` (layer 2)
3. `ping 10.50.20.20` from PC-B (layer 2: local switching)
4. `ipconfig` on PC-B (layer 3)
5. `ping 10.50.20.1` (layer 3)
6. `show ip interface brief` (layer 4)
7. `show ip route` (layer 4)
8. Browser (layer 5)

Steps 3 and 4 can reasonably swap, since slide 8 says to read the configuration before pinging. Explain your choice.

### Task 3

**Configuration checks:**

- `ipconfig` cannot prove delivery.
- `show vlan brief` cannot prove that the cable is connected or that traffic flows.
- `show ip route` cannot prove that the remote host replies.

**Traffic tests:**

- `ping` cannot prove the service works.
- The browser does not by itself show which layer failed.
- `tracert` can be blocked by devices along the path.
- Loopback cannot prove the cable, switch or gateway work.

### Task 4 (Verified with Python)

- **a.** The gateway does not match the design. Remote traffic and replies fail.
- **b.** /30: 10 ÷ 4 = 2 r 2, so the block starts at 8. The range is **10.50.20.8–10.50.20.11** (usable .9–.10). The gateway and server are outside it, so the host treats its own LAN as remote.
- **c.** APIPA: DHCP failed.
- **d.** Correct.
- **e.** No gateway. Local traffic works; nothing remote does.
- **f.** /29: 10 ÷ 8 = 1 r 2, so the block starts at 8. The range is **10.50.20.8–10.50.20.15** (usable .9–.14). The gateway is outside it.

### Task 5

- **A.** Check the DHCP server, the client's link and its switch-port VLAN. Do not type a static address to hide the fault.
- **B.** Router `show ip route`, then the remote host's settings, especially its gateway (the return path).
- **C.** Check the service is on, at the right address and port, and that the URL is right.
- **D.** Check the link and switch port (`show interfaces status`, `show vlan brief`) and the mask. An own-IP ping never tests the cable (Verified).
- **E.** The router interface for that VLAN (`show ip interface brief`) or its switch-facing port VLAN (`show vlan brief`).

### Task 6

**The five mistakes:**

1. No expected results were written down.
2. Sam started at the application (layer 5), and the browser test on PC-A does not test PC-B anyway.
3. Several changes were made at once (gateway, mask, router reboot).
4. The own-IP ping does not prove the cable.
5. Only the failed test was repeated: no regression check (for example, PC-B → server) and no recorded state. The mask change to /16 is also wrong in itself.

**Corrected log:**

1. Expected results written first.
2. Link and `show interfaces status`.
3. `ipconfig` compared with the design.
4. PC-B → server.
5. PC-B → gateway.
6. Router checks.
7. Smallest repair.
8. Retest the failed ping.
9. Regression tests.
10. Record the state.

### Task 7

**Record 1:**

- **Symptom:** PC-B cannot reach PC-A.
- **Evidence:** PC-B → server replies; PC-B → 10.50.20.1 fails; `show ip interface brief`: G0/1 administratively down.
- **Root cause:** G0/1 is shut down.
- **Repair:** `no shutdown` on G0/1. Changing PC-B's address is wrong: it breaks a correct PC (official rule).

**Record 2:**

- **Symptom:** PC-B cannot reach the gateway or PC-A.
- **Evidence:** `ipconfig` shows 255.255.255.252; the design says 255.255.255.0; the gateway is outside the /30.
- **Root cause:** PC-B's mask is wrong.
- **Repair:** set the mask to 255.255.255.0 **only**.

### Task 8 (Verified)

- **Mystery 1:** PC-B's cable is unplugged (link down). This is a **layer 1** fault. Check: link light and `show interfaces status` (`notconnect`). Repair: reconnect.
- **Mystery 2:** The web service is stopped on the server. This is a **layer 5** fault. Every ping works; only HTTP fails. Repair: HTTP **On**.
- **Mystery 3:** PC-B's port is in the wrong broadcast domain, like a wrong VLAN. This is a **layer 2** fault. Check: `show vlan brief`. Repair: move the port back.

Mysteries 1 and 3 both fail every PC-B test. The **link state** tells them apart: Mystery 1's interface had no carrier (`NO-CARRIER`), while Mystery 3's link was up but in the wrong segment.

### Task 9 (Verified)

1. PC-B's gateway (.254) now exists.
2. The server still uses 10.50.20.1, which no longer exists, so its replies to PC-A have no exit.
3. Set PC-B's gateway back to 10.50.20.1 and leave the router alone.
4. The server's ARP cache still held the router's MAC address for 10.50.20.1. The router accepted frames to its MAC, so the fault stayed hidden until the cache expired.

### Task 10

- **a.** The printer's own link, port VLAN or address.
- **b.** The printer's **gateway**, which is missing or wrong: it can answer locally but cannot reply to another network.
- **c.** The printing service (layer 5).

### Task 11 (Verified)

- Mystery 2 case → "LAYER 5 (service)".
- Case B → "LAYER 4 (routes and return path)".

Step 5 model, inside `config_checks` after `mine` is set:

```python
    if addr in (mine.network_address, mine.broadcast_address):
        found.append(f"address {addr} is the network or broadcast address of {mine}")
```

### Task 12 (Verified)

The simple files give one REGRESSION (the server ping) and the verdict "NOT finished". The Fault 2 comparison shows only FIXED and OK lines.

### Task 13 (Expected)

The results are your own. With the link off, loopback and own IP still work (as in the Verified Linux output); the gateway fails. Windows may show "Media disconnected" in `ipconfig` and drop the address.

### Task 14 (Expected)

- **With /24:** the first event is an ARP request for 10.50.20.20.
- **With /30:** PC-B no longer treats .20 as local. Record exactly what Packet Tracer does with the off-subnet gateway.

### Task 15 (Verified)

The outputs are as shown, and in lecture section 17. During Fault 2, `ip -n rtr route` lists only `10.50.10.0/24 dev g00`.

### Tasks 16–18 (Expected; matching Linux results Verified)

Use the test plans and expected-results tables.

**Smallest repair for the Extra Challenge:** set PC-B's mask to 255.255.255.0. Evidence: `ipconfig` shows /30 against the /24 design, and the gateway lies outside 10.50.20.8–.11.

### Tasks 19–20 (model points)

Task 19 is your own work: check it against the expected result. For Task 20, see the self-marking checklist and lecture sections 7, 8, 12, 15 and 16.
