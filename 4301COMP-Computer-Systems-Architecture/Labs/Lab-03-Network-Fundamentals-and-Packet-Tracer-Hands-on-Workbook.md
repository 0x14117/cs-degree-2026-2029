# Lab 3 — Network Fundamentals and Packet Tracer Hands-on Workbook (20 Tasks)

**Module:** 4301COMP Computer Systems Architecture

**Session:** Teaching Week 02, Session A · **Matching lecture:** `../Lectures/Lecture-03-Network-Fundamentals-and-Packet-Tracer.md`

---

## How to use this lab

**What this lab is for.** You will build a real (simulated) LAN in Cisco Packet Tracer, test it with `ping`, break it on purpose and fix it, then practise the same diagnosis on your own computer. You will also check parity and subnet calculations with two short scripts.

**Where the official tasks are.**

| Official lab sheet (TW02 Session A) | This workbook |
| --- | --- |
| Tutorial — Logging in to Cisco Packet Tracer, and Task 1 — Build and configure a small LAN | Task 16 |
| Task 2 — Testing network reachability with ping | Task 17 |
| Task 3 — Basic troubleshooting and fault diagnosis | Task 18 |

In the timetabled lab, **do Tasks 16, 17 and 18 first**. Several later tasks reuse the network you build in Task 16.

**Tools**

| Tool | Used in | Notes |
| --- | --- | --- |
| Cisco Packet Tracer 9.0 | Tasks 10, 15–19 | Named on the official lab sheet. Log in with your Cisco Networking Academy / Skills For All account |
| Snipping Tool (Windows key + Shift + S) | Tasks 17–18 | Named on the official lab sheet |
| Command Prompt on your own Windows PC | Tasks 11–12 | Built in; every command here only reads information |
| Python 3 | Tasks 13–14 | **Optional, your choice.** Free from python.org. Uses only built-in modules |
| Pen and paper | Everywhere | Work out every answer before checking it |

**Rules:** predict before you check; show your working; use hints only after a real attempt; record what you actually see, including failures.

**Labels:** **Verified** = run or calculated before being written here. **Expected** = not run here. Packet Tracer could not be run when this lab was written, so **every Packet Tracer result is Expected**: record your own.

**Safety.** Only `ping` and `tracert` devices on your own network or well-known public test addresses. Do not scan or probe networks you do not own or have permission to test.

---

## Part A — Warm-up: recognise and predict (Tasks 1–5)

### Task 1 — LAN, MAN or WAN?

**Goal:** classify networks by geographical area.

| # | Network | LAN, MAN or WAN? |
| --- | --- | --- |
| a | The four PCs and switch you build in Packet Tracer | |
| b | Your home Wi-Fi | |
| c | A council network joining libraries across Liverpool | |
| d | A supermarket chain joining 400 stores across the UK | |
| e | A data centre with 5,000 servers in one building | |
| f | The internet | |
| g | A university network joining buildings on one campus | |
| h | A cable linking two hospitals in the same city | |

**Expected result:** 4 LAN, 2 MAN, 2 WAN.

- **Hint 1:** Area, not number of devices.
- **Hint 2:** One building or one campus is local.

---

### Task 2 — Topology spotting and mesh maths

**Goal:** recognise topologies and calculate full-mesh links.

1. Name the topology for each description:
   a. Every PC is cabled to one switch.
   b. Four core routers each have a direct link to every other core router.
   c. All PCs are clipped onto one long coaxial cable.
   d. Each node is connected to exactly two neighbours in a closed loop.
   e. A router connects to three floor switches; each switch connects to the PCs on its floor.
2. Calculate the number of links for a full mesh of **3, 4, 6 and 10** nodes. Show the working.
3. A full mesh of 10 offices needs how many **more** links than a star of the same 10 offices joined to one central site? (A star of *n* end nodes needs *n* links.)

**Expected result:** 3, 6, 15 and 45 links; 35 more links (Verified).

- **Hint 1:** links = n × (n − 1) ÷ 2.
- **Hint 2:** 45 − 10 = ?

---

### Task 3 — Which device?

**Goal:** choose the right device for each job (slide 19).

| # | Job | Device | Layer |
| --- | --- | --- | --- |
| a | Connect 20 PCs in one office so frames go only to the right PC | | |
| b | Connect the office network to the internet | | |
| c | Let laptops join the office LAN without cables | | |
| d | An old device that sends every bit to every port | | |
| e | Join two LAN segments and filter frames between them | | |
| f | Connect the 192.168.10.0/24 network to the 192.168.20.0/24 network | | |

**Expected result:** six devices, with layers 1, 2 or 3.

- **Hint 1:** Frames and MAC addresses → layer 2. IP packets between networks → layer 3.
- **Hint 2:** Two different IP networks always need the same kind of device.

---

### Task 4 — Add the parity bit

**Goal:** add even and odd parity bits by hand.

Put the parity bit on the **left**.

| Data | Number of 1s | Even parity: sent bits | Odd parity: sent bits |
| --- | --- | --- | --- |
| 1010101 | | | |
| 1110000 | | | |
| 0000001 | | | |
| 0110110 | | | |
| 1111110 | | | |
| 0000000 | | | |

**Expected result:** all twelve answers match the answer key (Verified with `parity.py`).

- **Hint 1:** Even parity: add 1 only if the count is odd.
- **Hint 2:** The even and odd parity bits for the same data are always opposites.

---

### Task 5 — Same network or not?

**Goal:** use a /24 subnet mask to predict whether two devices can talk directly.

All masks are 255.255.255.0.

| # | Address A | Address B | Same network? |
| --- | --- | --- | --- |
| a | 192.168.10.11 | 192.168.10.14 | |
| b | 192.168.10.11 | 192.168.20.14 | |
| c | 192.168.1.10 | 192.168.1.20 | |
| d | 192.168.1.10 | 192.168.2.10 | |
| e | 10.0.0.5 | 10.0.0.250 | |
| f | 172.16.4.1 | 172.16.5.1 | |
| g | 192.168.10.200 | 192.168.10.2 | |
| h | 192.168.100.1 | 192.168.10.1 | |

**Expected result:** 4 yes, 4 no (Verified with Python's `ipaddress` module).

- **Hint 1:** Compare the whole of the first three octets, digit by digit.
- **Hint 2:** Row h is a trap: 100 ≠ 10.

---

## Part B — Find and fix (Tasks 6–10)

### Task 6 — Which bytes were damaged?

**Goal:** check received data for parity errors and see the limit of parity.

Even parity is in use. Each received byte includes its parity bit.

| # | Received | Number of 1s | Pass or error? |
| --- | --- | --- | --- |
| a | 01000001 | | |
| b | 11100011 | | |
| c | 00110110 | | |
| d | 10000000 | | |
| e | 11111111 | | |
| f | 01100110 | | |

Then: byte **f** was actually sent as `00100111`. How many bits changed, and why did parity not notice?

**Expected result:** 2 errors detected (Verified). Byte f passed even though it was damaged.

- **Hint 1:** Count every 1, including the parity bit.
- **Hint 2:** Compare f with `00100111` bit by bit.

---

### Task 7 — Fix the IP plan

**Goal:** find invalid or conflicting IP settings before they cause faults.

Sam Archer planned a LAN on 192.168.10.0/24 (no router). **Five rows contain a problem.** Find and fix each one.

| Device | IP address | Subnet mask |
| --- | --- | --- |
| PC1 | 192.168.10.11 | 255.255.255.0 |
| PC2 | 192.168.10.256 | 255.255.255.0 |
| PC3 | 192.168.10.13 | 255.255.255.0 |
| PC4 | 192.168.10.13 | 255.255.255.0 |
| PC5 | 192.168.10.0 | 255.255.255.0 |
| PC6 | 192.168.11.16 | 255.255.255.0 |
| Printer | 192.168.10.20 | 255.0.255.0 |

**Expected result:** five fixed rows, each with a one-line reason.

- **Hint 1:** Check each octet is 0–255, that no address is used twice, and that no host uses the network or broadcast address.
- **Hint 2:** A mask's 255s must all come before its 0s.

---

### Task 8 — Read the ping results

**Goal:** interpret ping output without jumping to conclusions.

For each situation, say what the result **proves**, what it does **not** prove, and your next diagnostic step.

1. `ping 192.168.10.12` from PC1: four lines of `Reply from 192.168.10.12: bytes=32 time<1ms TTL=128`.
2. `ping 192.168.10.14` from PC1: four lines of `Request timed out.`
3. `ping 127.0.0.1` on your laptop: four replies. `ping 192.168.10.12` from the same laptop: timed out.
4. A real result from the Linux machine used to check this lab (Verified):

   ```text
   $ ping -c 2 -W 2 8.8.8.8
   PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
   From 21.4.102.23 icmp_seq=1 Destination Port Unreachable
   From 21.4.102.23 icmp_seq=2 Destination Port Unreachable

   --- 8.8.8.8 ping statistics ---
   2 packets transmitted, 0 received, +2 errors, 100% packet loss, time 1030ms
   ```

   Is Google's public DNS server (8.8.8.8) down?

**Expected result:** four answers that separate "proves" from "suggests".

- **Hint 1:** Slide 27: no reply does not by itself prove the host is down.
- **Hint 2:** In item 4, the error message comes **from 21.4.102.23**, not from 8.8.8.8. What does that tell you?

---

### Task 9 — Fix the false statements

**Goal:** correct misunderstandings about topologies and devices.

Each statement is **false**. Correct it in one sentence.

1. "A star topology has no single point of failure."
2. "A hub sends each frame only to the port where the destination is."
3. "A router is needed to connect two PCs on the same subnet."
4. "Modern office LANs use a shared coaxial bus."
5. "If one PC's cable breaks in a star network, every PC loses its connection."
6. "Parity can correct the bit that was damaged."

**Expected result:** six corrected sentences.

- **Hint 1:** Re-read lecture sections 9 and 10.
- **Hint 2:** For 5, what does slide 11 say about adding or removing one end device?

---

### Task 10 — Packet Tracer fault hunt (two new faults)

**Goal:** diagnose faults that are not in the official task.

**Skill you gain:** you can diagnose a configuration fault from evidence rather than guessing.

Start from your saved, working Task 16 network (use a **copy**).

**Fault D: duplicate address.** Set PC4's IP address to **192.168.10.13** (the same as PC3).
1. Predict what will happen when PC1 pings 192.168.10.13.
2. Ping it several times and record exactly what you see.
3. Use `ipconfig` on PC3 and PC4. What do you notice?
4. Fix it.

**Fault E: the fault that isn't.** Set PC4's subnet mask to **255.255.0.0** (keep the address 192.168.10.14).
5. Predict: will PC4 and PC1 still be able to ping each other? Use the subnet rule from lecture section 14.
6. Test it and record the result.
7. Explain why, and why it is still a mistake worth fixing.

**Expected result:** Fault D gives unreliable or confusing results; Fault E still works (the network calculation is Verified; the Packet Tracer results are Expected).

- **Hint 1:** For E, with mask 255.255.0.0, PC4's network is 192.168.0.0/16. Is 192.168.10.11 inside it?
- **Hint 2:** For E, PC1 still uses /24. Is 192.168.10.14 inside PC1's network?

---

## Part C — Build (Tasks 11–15)

### Task 11 — Your own computer's IP configuration

**Goal:** find and interpret the real IP settings of the computer you use every day.

**Skill you gain:** you can read `ipconfig` output and identify your IPv4 address, subnet mask, default gateway and MAC address.

On your own Windows PC (Expected; not run here):

1. Open Command Prompt and run `ipconfig`. *What it does:* shows the IP settings of each network adapter. It only reads information.
2. Find your active adapter (Wi-Fi or Ethernet). Record its **IPv4 Address**, **Subnet Mask** and **Default Gateway**.
3. Run `ipconfig /all` (also read-only). Find the **Physical Address**: that is the adapter's **MAC address**. Also note whether **DHCP Enabled** says Yes.
4. Answer: (a) Is your IPv4 address private? Which range? (b) What is your network address? (c) How many usable host addresses does your network have, if the mask is 255.255.255.0?

**Linux alternative (Verified on the checking machine).** `ip -4 addr` shows the same information:

```text
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    inet 127.0.0.1/8 scope host lo
4: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc pfifo_fast state UP group default qlen 1000
    inet 192.0.2.2/24 brd 192.0.2.255 scope global eth0
```

Here `eth0` has address 192.0.2.2 with a /24 mask (255.255.255.0) and broadcast address 192.0.2.255, and `lo` is the loopback interface. `ip route` showed `default via 192.0.2.1`, so the default gateway is 192.0.2.1.

**Expected result:** a table of your four values. **Do not post your public IP address or MAC address online**; keep them in your private notes.

- **Hint 1:** Home networks almost always use 192.168.x.x or 10.x.x.x.
- **Hint 2:** For a /24, the network address is the first three octets followed by .0.

---

### Task 12 — Ping and trace from your own computer

**Goal:** test reachability step by step, outwards from your own machine.

**Skill you gain:** you can use `ping` and `tracert` to locate where a connection stops.

On your own Windows PC (Expected):

1. `ping 127.0.0.1`: tests your own network software.
2. `ping` your own IPv4 address from Task 11.
3. `ping` your default gateway.
4. `ping www.ljmu.ac.uk`. Record whether you get replies. (If you get none, remember slide 27.)
5. `tracert www.ljmu.ac.uk`. *What it does:* lists each router on the path, with three round-trip times each. Lines of `* * *` mean that router did not answer the test, which is common and not always a fault. Press **Ctrl + C** to stop it early.
6. Copy your results into this table:

| Test | Reply? | Time | What it proves |
| --- | --- | --- | --- |
| 127.0.0.1 | | | |
| Own address | | | |
| Default gateway | | | |
| www.ljmu.ac.uk | | | |
| tracert: number of hops | | — | |

A real loopback test from the Linux checking machine (Verified):

```text
$ ping -c 4 127.0.0.1
64 bytes from 127.0.0.1: icmp_seq=1 ttl=64 time=0.028 ms
...
4 packets transmitted, 4 received, 0% packet loss, time 3050ms
```

**Expected result:** replies from at least the first three tests on a working home network.

- **Hint 1:** Linux/macOS use `ping -c 4` (otherwise ping never stops) and `traceroute`.
- **Hint 2:** If the gateway replies but the website does not, the problem (or the filtering) is beyond your router.

---

### Task 13 — Build a parity checker

**Goal:** turn the parity rule into a program and use it to check Tasks 4 and 6.

**Skill you gain:** you can implement a simple integrity check in code and test it with good and damaged data.

1. Save as `parity.py`:

```python
# parity.py - add and check a parity bit, like a sender and receiver would.
# Usage: python parity.py


def count_ones(bits):
    """How many 1s are in a string such as '1000001'."""
    return bits.count("1")


def add_parity(bits, mode="even"):
    """Return the bits with a parity bit added on the left."""
    ones = count_ones(bits)
    if mode == "even":
        parity = "0" if ones % 2 == 0 else "1"   # make the total even
    else:
        parity = "1" if ones % 2 == 0 else "0"   # make the total odd
    return parity + bits


def check(received, mode="even"):
    """True if the received bits (parity bit included) pass the check."""
    ones = count_ones(received)
    return ones % 2 == 0 if mode == "even" else ones % 2 == 1


def flip(bits, position):
    """Simulate noise: change one bit (position 0 = leftmost)."""
    new = "1" if bits[position] == "0" else "0"
    return bits[:position] + new + bits[position + 1:]


if __name__ == "__main__":
    for data in ["1000001", "1100011", "0000000", "1111111"]:
        print(f"{data}: even -> {add_parity(data, 'even')}, odd -> {add_parity(data, 'odd')}")

    sent = add_parity("1000001", "even")          # sender adds parity
    one_error = flip(sent, 3)                     # one bit corrupted
    two_errors = flip(flip(sent, 3), 5)           # two bits corrupted
    print("sent          ", sent, "passes check:", check(sent))
    print("1 bit flipped ", one_error, "passes check:", check(one_error))
    print("2 bits flipped", two_errors, "passes check:", check(two_errors))
```

2. Run `python parity.py`. *What it does:* prints calculations only; it reads and changes no files. Actual output (Verified, Python 3.13):

```text
1000001: even -> 01000001, odd -> 11000001
1100011: even -> 01100011, odd -> 11100011
0000000: even -> 00000000, odd -> 10000000
1111111: even -> 11111111, odd -> 01111111
sent           01000001 passes check: True
1 bit flipped  01010001 passes check: False
2 bits flipped 01010101 passes check: True
```

3. **Extend it:** add a loop that checks the six received bytes from Task 6 and prints "pass" or "error" for each.
4. **Extend it:** use `flip()` to show that flipping **three** bits **is** detected.

**Expected result:** your Task 6 loop reports errors for b and d only (Verified).

- **Hint 1:** `for received in ["01000001", "11100011", ...]:` then `print(received, check(received))`.
- **Hint 2:** `flip(flip(flip(sent, 1), 3), 5)` flips three bits.

---

### Task 14 — Build a subnet checker

**Goal:** check Task 5 and Task 7 with code.

**Skill you gain:** you can use Python's built-in `ipaddress` module to calculate networks, which network and security engineers use to check address plans and firewall rules.

1. Save as `subnet_check.py`:

```python
# subnet_check.py - are two IPv4 addresses in the same network (subnet)?
# Uses Python's built-in ipaddress module, so nothing needs installing.
# Usage: python subnet_check.py

import ipaddress


def describe(address, mask):
    """Show the network an address belongs to, for a given subnet mask."""
    iface = ipaddress.ip_interface(f"{address}/{mask}")
    net = iface.network
    return net, net.network_address, net.broadcast_address


def same_network(ip1, ip2, mask="255.255.255.0"):
    """True if both addresses fall in the same network for this mask."""
    return describe(ip1, mask)[0] == describe(ip2, mask)[0]


if __name__ == "__main__":
    mask = "255.255.255.0"
    tests = [
        ("192.168.10.11", "192.168.10.14"),   # PC1 and PC4 in the official lab
        ("192.168.10.11", "192.168.20.14"),   # PC4 after fault Option B
        ("192.168.1.10", "192.168.1.20"),     # slide 26 example
        ("192.168.1.10", "192.168.2.10"),     # slide 26 example
    ]
    for a, b in tests:
        verdict = "same network: can talk directly" if same_network(a, b, mask) \
            else "different networks: needs a router"
        print(f"{a:<15} {b:<15} {verdict}")

    net, first, last = describe("192.168.10.11", mask)
    print(f"\nNetwork {net}: network address {first}, broadcast address {last}, "
          f"{net.num_addresses - 2} usable host addresses")
```

2. Run it. Actual output (Verified, Python 3.13):

```text
192.168.10.11   192.168.10.14   same network: can talk directly
192.168.10.11   192.168.20.14   different networks: needs a router
192.168.1.10    192.168.1.20    same network: can talk directly
192.168.1.10    192.168.2.10    different networks: needs a router

Network 192.168.10.0/24: network address 192.168.10.0, broadcast address 192.168.10.255, 254 usable host addresses
```

3. **Extend it:** add all eight pairs from Task 5 to `tests` and check your answers.
4. **Extend it:** add a function `is_valid_host(address, mask)` that returns `False` for the network address, the broadcast address or an address outside the network. Test it on PC5 (`192.168.10.0`) and PC6 (`192.168.11.16`) from Task 7, using network 192.168.10.0/24.
5. Try `describe("192.168.10.256", mask)`. What happens? Why is that useful?

**Expected result:** step 3 gives 4 yes, 4 no; step 5 raises a `ValueError` because 256 is not a valid octet (Verified).

- **Hint 1:** `ipaddress.ip_address("192.168.10.0") in ipaddress.ip_network("192.168.10.0/24")` is `True`.
- **Hint 2:** Compare with `net.network_address` and `net.broadcast_address` as well.

---

### Task 15 — Extend the LAN: a hierarchical network

**Goal:** turn the single-switch star into a two-switch hierarchical network.

**Skill you gain:** you can extend a network in Packet Tracer and prove it works with a ping test plan.

Use a **copy** of your Task 16 file (Expected; Packet Tracer was not run here).

1. Add a second **2960-24TT** switch and two more PCs, **PC5** (192.168.10.15/24) and **PC6** (192.168.10.16/24), connected to the new switch.
2. Connect the two switches together. Use **Copper Cross-Over** cable between the two switches (switch-to-switch). If the link stays red, delete it and try the **Automatically Choose Connection Type** tool instead.
3. Wait for the link lights to go green.
4. Run the test plan:

| From | To | Expected | Actual |
| --- | --- | --- | --- |
| PC1 | PC5 | Replies | |
| PC6 | PC4 | Replies | |
| PC5 | PC6 | Replies | |

5. Delete the switch-to-switch cable. Which pings fail now, and which still work? What single point of failure does this show?

**Expected result:** all pings succeed with the link up; with it down, only PCs on the same switch can reach each other.

- **Hint 1:** All six PCs are still in 192.168.10.0/24, so no router is needed.
- **Hint 2:** The inter-switch cable is now carrying all traffic between the two groups.

---

## Part D — Official tasks and integration (Tasks 16–20)

### Task 16 — Log in and build a small LAN (Official Tutorial and Official Task 1)

**Goal:** build and configure a four-PC LAN in Packet Tracer.

**Skill you gain:** you can build, address and save a working LAN in Cisco Packet Tracer.

**Official Tutorial: logging in to Cisco Packet Tracer**

1. If the Cisco Packet Tracer shortcut is missing from your desktop or Start menu, perform a **Workspace Refresh** or open **Appventix** to launch or restore the application shortcut.
2. Launch **Cisco Packet Tracer 9.0**.
3. At the login screen, select **Cisco Networking Academy / Skills For All** login and sign in using your student credentials.
4. Once authenticated, confirm the application opens to the main workspace, ready for building topologies.

**Official Task 1: build and configure a small LAN**

1. Open Cisco Packet Tracer 9.0 and verify the version via **Help > About**.
2. Add devices from the bottom-left Device Selection Box:
   - **Network Devices > Switches > 2960-24TT**: click the workspace to place the switch.
   - **End Devices > PC-PT**: click four times to place four PCs.
3. Rename each PC: click it > **Config** tab > set **Display Name** to **PC1**, **PC2**, **PC3** and **PC4**.
4. Cable each PC to the switch: **Connections** (lightning icon) > **Copper Straight-Through** > click the PC and select **FastEthernet0** > click the switch and select the port:
   - PC1 FastEthernet0 → Switch **FastEthernet0/1**
   - PC2 FastEthernet0 → Switch **FastEthernet0/2**
   - PC3 FastEthernet0 → Switch **FastEthernet0/3**
   - PC4 FastEthernet0 → Switch **FastEthernet0/4**

   Wait until the port link lights turn from **amber** to **solid green**.
5. Configure static IP addresses: click each PC > **Desktop** > **IP Configuration** > **Static**:

   | PC | IP address | Subnet mask | Default gateway |
   | --- | --- | --- | --- |
   | PC1 | 192.168.10.11 | 255.255.255.0 | Leave blank |
   | PC2 | 192.168.10.12 | 255.255.255.0 | Leave blank |
   | PC3 | 192.168.10.13 | 255.255.255.0 | Leave blank |
   | PC4 | 192.168.10.14 | 255.255.255.0 | Leave blank |

6. Verify: on each PC, **Desktop** > **Command Prompt** > type `ipconfig` and press Enter.
7. Save: **File > Save As** > `TW02A_YourStudentID.pkt`.

**Why amber then green? (Extra)** Amber means the switch port is still starting up and checking the link; green means it is ready to forward frames. This usually takes up to about half a minute in Packet Tracer.

**Test plan**

| Check | Expected | Actual |
| --- | --- | --- |
| Version shown in Help > About | 9.0.x | |
| Four PCs named PC1–PC4 | Yes | |
| Each PC on the stated switch port | Fa0/1–Fa0/4 | |
| All link lights green | Yes | |
| `ipconfig` on each PC matches the table | Yes | |
| File saved with the correct name | `TW02A_<your ID>.pkt` | |

- **Hint 1:** Hovering over a device in Packet Tracer shows its interfaces and addresses.
- **Hint 2:** If a light stays red, check you chose **Straight-Through** and the right ports.

---

### Task 17 — Testing network reachability with ping (Official Task 2)

**Goal:** prove the LAN works and capture evidence.

**Official steps**

1. Open **PC1** > **Desktop** > **Command Prompt**.
2. Test connectivity from PC1 to each other PC:
   - `ping 192.168.10.12` (PC2)
   - `ping 192.168.10.13` (PC3)
   - `ping 192.168.10.14` (PC4)
3. Understand the output: a successful response reads **`Reply from 192.168.10.x: bytes=32 time<1ms`**, indicating active communication. If you see **`Request timed out`** or **`Destination host unreachable`**, check that the IP addresses and physical links are correctly configured.
4. Capture evidence: use **Snipping Tool** (or Windows key + Shift + S) to take a screenshot showing your labelled topology with green link lights **and** the Command Prompt window with successful ping replies.

**Note (Expected):** the very first ping to a device sometimes shows one `Request timed out.` followed by replies. This is normal in Packet Tracer: the first packet waits while PC1 finds the other PC's MAC address (a process called **ARP**, which you will meet in the next session). Record it if it happens.

**Test plan**

| Test | Expected | Actual (replies out of 4) |
| --- | --- | --- |
| PC1 → PC2 | Replies | |
| PC1 → PC3 | Replies | |
| PC1 → PC4 | Replies | |
| Screenshot shows topology, green lights and replies | Yes | |

- **Hint 1:** If all pings fail, check PC1 first with `ipconfig`.
- **Hint 2:** If only one fails, check that PC's address and cable.

---

### Task 18 — Basic troubleshooting and fault diagnosis (Official Task 3)

**Goal:** create a fault, diagnose it from evidence and repair it.

**Official steps**

1. **Save a backup copy** of your working topology first.
2. Simulate a connectivity fault on **PC4** using one of these:
   - **Option A (physical fault):** use the **Delete** tool (X icon) to delete the cable between PC4 and the switch.
   - **Option B (incorrect IP network):** PC4 > **Desktop** > **IP Configuration** > change the IP address to **192.168.20.14**, mask **255.255.255.0**.
   - **Option C (interface off):** PC4 > **Config** tab > **FastEthernet0** > untick **Port Status: On**.
3. Diagnose:
   - Inspect the cabling and link lights (green = active physical connection; red or off = link/interface down).
   - Run `ipconfig` on PC4 to check whether its address matches the local network (192.168.10.x).
   - Run `ping 192.168.10.11` from PC4 and observe errors such as timeout or unreachable.
4. Repair (A: reconnect the cable; B: set 192.168.10.14 / 255.255.255.0; C: turn Port Status back on), re-test with ping, and capture screenshots of the **failed test**, the **configuration window** and the **successful re-test**.

**Supplementary:** do all three options, one at a time, restoring the backup in between. That lets you compare how each fault looks.

**Diagnosis record**

| Option | Link lights | `ipconfig` on PC4 | `ping 192.168.10.11` from PC4 | Fault found at which step of the lecture 16.2 flowchart? |
| --- | --- | --- | --- | --- |
| A | | | | |
| B | | | | |
| C | | | | |

**Expected result:** A and C show a link problem at the first step; B shows green lights and a correct-looking `ipconfig`, but the address is on 192.168.**20**.x, a different network.

- **Hint 1:** Option B is the hardest to see, because nothing looks "broken" physically.
- **Hint 2:** Use your subnet checker (Task 14) to confirm Option B.

---

### Task 19 — Mini-project: a small office network

**Goal:** design, build and prove a small network from a brief.

**Skill you gain:** you can turn requirements into a topology, an address plan and a test plan, which is how real network changes are planned.

**Brief.** A small office has **6 PCs and 1 network printer** on one floor, plus **3 PCs** in a back room. Everything must be on one network, **192.168.50.0/24**, with no internet for now.

1. Choose and justify a topology (two sentences).
2. Write an **address plan** table: device, port, IP address, mask. Use addresses from .11 upwards for PCs and .50 for the printer. Do not use .0 or .255.
3. Build it in Packet Tracer (the printer is under **End Devices**).
4. Write and run a **test plan** of at least six pings, including one from the back room to the printer.
5. Identify one **single point of failure** and say how you would remove it.
6. Save as `TW02A_MiniProject.pkt` and screenshot the topology and two successful pings.

**Test plan (add your own rows)**

| From | To | Expected | Actual |
| --- | --- | --- | --- |
| Back-room PC | Printer | Replies | |
| Office PC | Back-room PC | Replies | |
| | | | |

**Expected result:** every test passes; every address is unique and inside 192.168.50.1–254.

- **Hint 1:** Two switches joined by one cable (like Task 15) suits two rooms.
- **Hint 2:** Run the address plan through your `subnet_check.py` before building.

---

### Task 20 — Assessment-style practice: networks and diagnosis

**This is practice only, not a real exam question.** The module exam is two hours with short-answer and essay-style questions, and the report covers data storage and networking (module guide). Marks are invented for planning.

**Rules:** 25 minutes, closed book, write it yourself.

**(a)** Distinguish a LAN from a WAN, with one example of each. *(2 marks)*

**(b)** Compare the star and full-mesh topologies in terms of resilience and cost. Calculate the number of links in a full mesh of 6 devices. *(4 marks)*

**(c)** Using even parity, add the parity bit to `0110110`. Explain one limitation of parity. *(3 marks)*

**(d)** PC1 (192.168.10.11/24) cannot ping PC4. Describe, step by step, how you would diagnose the fault, explaining what each test would show for (i) a disconnected cable and (ii) PC4 configured as 192.168.20.14/24. Explain why "no reply" on its own does not prove PC4 is switched off. *(11 marks; aim for 250–350 words)*

**Self-marking checklist**

| Part | A good answer includes | Expected | Actual |
| --- | --- | --- | --- |
| (a) | Geographical area; correct examples | 2 points | |
| (b) | Star: central single point of failure, cheap; mesh: many paths, resilient, n(n − 1)/2 links; 6 × 5 ÷ 2 = 15 | 4 points | |
| (c) | 00110110 (four 1s already even, so 0); cannot detect two-bit errors or correct errors | 3 points | |
| (d) | Bottom-up order; link lights; `ipconfig`; subnet comparison; ping loopback/own/neighbour; (i) lights off/red; (ii) lights green, 192.168.20 ≠ 192.168.10, needs router; firewalls/ICMP filtering/policy can block replies | 11 points | |
| Time | Within 25 minutes | Yes | |

- **Hint 1:** Plan (d) as the flowchart in lecture section 16.2.
- **Hint 2:** Name each test, then say what result you would expect for each fault.

---

## Tracker

| Task | Name | Done | Notes / score |
| --- | --- | --- | --- |
| 1 | LAN, MAN or WAN? | ☐ | /8 |
| 2 | Topology spotting and mesh maths | ☐ | |
| 3 | Which device? | ☐ | /6 |
| 4 | Add the parity bit | ☐ | /12 |
| 5 | Same network or not? | ☐ | /8 |
| 6 | Which bytes were damaged? | ☐ | /6 |
| 7 | Fix the IP plan | ☐ | /5 |
| 8 | Read the ping results | ☐ | /4 |
| 9 | Fix the false statements | ☐ | /6 |
| 10 | Packet Tracer fault hunt | ☐ | |
| 11 | Your own IP configuration | ☐ | |
| 12 | Ping and trace from your own computer | ☐ | |
| 13 | Parity checker | ☐ | |
| 14 | Subnet checker | ☐ | |
| 15 | Hierarchical LAN | ☐ | |
| 16 | **Official Tutorial + Task 1** — Build a small LAN | ☐ | |
| 17 | **Official Task 2** — Ping | ☐ | |
| 18 | **Official Task 3** — Troubleshooting | ☐ | |
| 19 | Mini-project: small office | ☐ | |
| 20 | Assessment-style practice | ☐ | /20 |

## Reflection

1. Which of the three official faults (A, B, C) was hardest to spot, and why?
2. What did your own `tracert` show? Did any hops show `* * *`, and does that mean they were broken?
3. Why might an organisation deliberately block `ping` replies on some devices?
4. Explain in two sentences why the four PCs in Task 16 do not need a default gateway.

---

## Answer key

**(Verified)** = calculated with Python 3.13 (`parity.py`, `subnet_check.py`, `ipaddress`) or run on the Linux checking machine. **(Expected)** = Packet Tracer or your own computer; not run here.

### Task 1

a LAN · b LAN · c MAN · d WAN · e LAN · f WAN · g LAN · h MAN. (4 LAN, 2 MAN, 2 WAN.)

### Task 2

1. a star · b full mesh · c bus · d ring · e hierarchical.
2. 3 × 2 ÷ 2 = **3** · 4 × 3 ÷ 2 = **6** · 6 × 5 ÷ 2 = **15** · 10 × 9 ÷ 2 = **45** (Verified).
3. 45 − 10 = **35** more links.

### Task 3

a switch (2) · b router (3) · c access point (2) · d hub (1) · e bridge (2) · f router (3).

### Task 4 (Verified)

| Data | 1s | Even | Odd |
| --- | --- | --- | --- |
| 1010101 | 4 | 01010101 | 11010101 |
| 1110000 | 3 | 11110000 | 01110000 |
| 0000001 | 1 | 10000001 | 00000001 |
| 0110110 | 4 | 00110110 | 10110110 |
| 1111110 | 6 | 01111110 | 11111110 |
| 0000000 | 0 | 00000000 | 10000000 |

### Task 5 (Verified)

a yes · b **no** · c yes · d **no** · e yes · f **no** · g yes · h **no**.

### Task 6 (Verified)

| # | 1s | Result |
| --- | --- | --- |
| a | 2 | Pass |
| b | 5 | **Error** |
| c | 4 | Pass |
| d | 1 | **Error** |
| e | 8 | Pass |
| f | 4 | Pass |

Byte f: sent `00100111`, received `01100110`. Two bits changed (second and last), so the count of 1s stayed even and parity could not notice.

### Task 7

| Device | Problem | Fix |
| --- | --- | --- |
| PC2 | 256 is not a valid octet (0–255) | e.g. 192.168.10.12 |
| PC4 | Duplicate of PC3's address | e.g. 192.168.10.14 |
| PC5 | 192.168.10.0 is the network address | e.g. 192.168.10.15 |
| PC6 | 192.168.11.x is a different network; no router | e.g. 192.168.10.16 |
| Printer | 255.0.255.0 is not a valid mask (Verified) | 255.255.255.0 |

PC1 and PC3 are correct.

### Task 8

1. **Proves** PC1 and PC2 can exchange ICMP over the LAN right now. Does not prove every service on PC2 works. Next: test the other PCs.
2. **Suggests** a problem between PC1 and PC4 but does not prove PC4 is off. Next: check PC4's link light, then `ipconfig` on PC4.
3. **Proves** the laptop's own network software works. The failure suggests the laptop is not on the same network as 192.168.10.12 (or a firewall blocks it). Next: `ipconfig` to compare networks.
4. **No.** The replies came from 21.4.102.23, a device on the path that **refused** the requests. 8.8.8.8 was never reached, so you cannot tell whether it is up. (It is a major public service and was running.) This shows filtering, not a down host (Verified output).

### Task 9

1. The central switch is a single point of failure.
2. A hub repeats every bit to **every** other port; a switch sends frames only to the right port.
3. A **switch** connects PCs on the same subnet; a router is only needed between different networks.
4. Modern LANs use **switches** in a star or hierarchical layout; shared coaxial bus is historical.
5. Only that one PC loses its connection; the others are unaffected.
6. Parity can only **detect** an odd number of errors; it cannot tell which bit is wrong, so the data is re-sent.

### Task 10

- **Fault D (Expected):** results become unreliable: replies may come from either PC, or one PC may report an address conflict. Duplicate addresses cause faults that come and go, which are hard to diagnose. Fix: give PC4 192.168.10.14.
- **Fault E (network calculation Verified; Packet Tracer result Expected):** pings **still work**. PC4's network with /16 is 192.168.0.0/16, which **contains** 192.168.10.11, so PC4 treats PC1 as local; PC1 (/24) also sees 192.168.10.14 as local. It is still wrong: PC4 now believes thousands of addresses (192.168.0.0–192.168.255.255) are local, so traffic to, say, 192.168.20.5 would never be sent to a router. Inconsistent masks cause hard-to-find faults later.

### Task 11 (Expected)

Your values. Typical: IPv4 192.168.1.x, mask 255.255.255.0, gateway 192.168.1.1 or 192.168.1.254, DHCP Enabled: Yes. Network address = first three octets + .0; 254 usable hosts for a /24.

### Task 12 (Expected)

Loopback should always reply. Own address and gateway normally reply on a working network. The website may or may not reply: many sites block ICMP. In `tracert`, `* * *` lines usually mean that router does not answer the test, not that it is broken, as long as later hops still respond.

### Task 13 (Verified)

```python
for received in ["01000001", "11100011", "00110110", "10000000", "11111111", "01100110"]:
    print(received, "pass" if check(received) else "error")
```

Output: pass, **error**, pass, **error**, pass, pass. Three flipped bits: `flip(flip(flip(sent, 1), 3), 5)` gives `00010101`, which has three 1s and **fails** the even check, so it is detected.

### Task 14 (Verified)

Step 3: a yes, b no, c yes, d no, e yes, f no, g yes, h no.

Step 4, model function:

```python
def is_valid_host(address, mask):
    net, first, last = describe(address, mask)
    addr = ipaddress.ip_address(address)
    return addr != first and addr != last

home = ipaddress.ip_network("192.168.10.0/24")
for a in ["192.168.10.0", "192.168.11.16", "192.168.10.14"]:
    inside = ipaddress.ip_address(a) in home
    print(a, "valid host here" if inside and is_valid_host(a, "255.255.255.0") else "NOT valid here")
```

Output: `192.168.10.0 NOT valid here`, `192.168.11.16 NOT valid here`, `192.168.10.14 valid host here`.

Step 5: `ValueError: '192.168.10.256/255.255.255.0' does not appear to be an IPv4 or IPv6 interface`. Useful because the program refuses invalid input instead of silently accepting a bad plan.

### Task 15 (Expected)

All pings succeed with the inter-switch link up. With it deleted, PC1–PC4 can still reach each other and PC5–PC6 can reach each other, but no ping crosses between the groups. The inter-switch cable is a single point of failure; a second link (with a protocol that prevents loops, covered later) would remove it.

### Tasks 16–18 (Expected)

Use the test plans. Model diagnosis record for Task 18:

| Option | Link lights | `ipconfig` on PC4 | Ping from PC4 | Flowchart step |
| --- | --- | --- | --- | --- |
| A | None/red (cable gone) | 192.168.10.14, looks correct | Fails | Step 1: physical |
| B | Green | 192.168.20.14 | Fails | Step 3: different network |
| C | Red | 192.168.10.14 | Fails | Step 1: interface off |

### Task 19 (model plan)

Topology: hierarchical (two switches, one per room, joined by one link). Example plan: office PCs 192.168.50.11–16, printer 192.168.50.50, back-room PCs 192.168.50.21–23, all mask 255.255.255.0, no gateway. Single point of failure: the inter-switch link (or either switch); remove it with a second link or a redundant switch.

### Task 20 (model points)

(a) LAN: small area, e.g. one office; WAN: large area, e.g. the internet. (b) Star: cheap, easy to add devices, central switch is a single point of failure; full mesh: every device linked to every other, very resilient, expensive; 6 × 5 ÷ 2 = **15** links. (c) `00110110`; parity cannot detect an even number of errors or correct any error. (d) Follow lecture section 16.2: (i) disconnected cable: link lights off/red at step 1; `ipconfig` may look normal; ping fails; (ii) 192.168.20.14: lights green, `ipconfig` shows 192.168.**20**.14, which is a different network from 192.168.10.x, so with no router the packets cannot be delivered. "No reply" alone does not prove PC4 is off: a firewall, ICMP filtering, policy or a routing problem can also stop replies.
