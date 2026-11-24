# Lab 4 — Ethernet, Switching and Network Models Hands-on Workbook (20 Tasks)

**Module:** 4301COMP Computer Systems Architecture

**Session:** Teaching Week 02, Session B · **Matching lecture:** `../Lectures/Lecture-04-Ethernet-Switching-and-Network-Models.md`

---

## How to use this lab

**What this lab is for.** You will extend your Packet Tracer LAN to two switches, look at real MAC addresses and ARP tables, watch a switch learn (in a simulator you can run), and practise the calculations and layer-mapping that the lecture introduced.

**Where the official tasks are.**

| Official lab sheet (TW02 Session B) | This workbook |
| --- | --- |
| Task 1 — Continue and expand the previous LAN · Task 2 — Add a second switch | Task 16 |
| Task 3 — Test the expanded LAN · Task 4 — Observe IP and MAC addresses | Task 17 |
| Task 5 — Simple subnet-mask experiment · Extra Challenge — Broken inter-switch link | Task 18 |

You need your saved **TW02A_YourStudentID.pkt** from Lab 3. In the timetabled lab, **do Tasks 16–18 first**.

**Tools**

| Tool | Used in | Notes |
| --- | --- | --- |
| Cisco Packet Tracer 9.0 | Tasks 14, 16–19 | Named on the official lab sheet |
| Snipping Tool (Windows key + Shift + S) | Task 17 | Named on the official lab sheet |
| Command Prompt on your own Windows PC | Tasks 12–13 | Every command here only reads information |
| Python 3 | Tasks 11, 15 | **Optional, your choice.** Free from python.org; built-in modules only |
| A web browser | Task 12 | For the IEEE MAC address (OUI) lookup |

**Rules:** predict before you check; show your working; use hints only after a real attempt; record what you actually see.

**Labels:** **Verified** = run or calculated before being written here. **Expected** = not run here. Packet Tracer and Windows could not be run when this lab was written, so their results are **Expected**.

---

## Part A — Warm-up: recognise and predict (Tasks 1–5)

### Task 1 — Bits, bytes and transfer times

**Goal:** convert file sizes and link speeds into transfer times.

Ignore overheads. 1 MB = 10⁶ bytes; 1 byte = 8 bits; 1 Mb/s = 10⁶ bits per second.

| # | File size | Link speed | Time |
| --- | --- | --- | --- |
| a | 100 MB | 100 Mb/s | |
| b | 100 MB | 1 Gb/s | |
| c | 5,000 MB (5 GB) | 1 Gb/s | |
| d | 700 MB | 80 Mb/s | |
| e | 1 MB | 10 Mb/s | |

Then: f. Your broadband is advertised as "80 Mb/s". Why does a 700 MB download not finish in under 9 seconds?

**Expected result:** 8 s, 0.8 s, 40 s, 70 s, 0.8 s (Verified).

- **Hint 1:** Multiply bytes by 8 first.
- **Hint 2:** 700 MB = 5,600 Mb.

---

### Task 2 — Choose the medium

**Goal:** match transmission media to requirements (slides 5 and 11–17).

For each, choose **twisted-pair copper**, **coaxial**, **optical fibre** or **wireless**, and give one reason.

1. Connecting two buildings 2 km apart at 10 Gb/s.
2. Cabling 30 desktop PCs to a switch in the same office.
3. A café that wants customers' phones online.
4. A factory floor next to large electric motors (lots of electromagnetic interference).
5. A house in an area with existing cable-TV infrastructure but no fibre.
6. A link where the organisation is very worried about someone tapping the line.

**Expected result:** six choices, each with a reason from the lecture.

- **Hint 1:** Ethernet over copper is normally limited to about 100 m.
- **Hint 2:** Fibre carries light, not electricity.

---

### Task 3 — Circuit, message or packet?

**Goal:** recognise switching methods and service types.

| # | Description | Answer |
| --- | --- | --- |
| a | A traditional landline phone call | |
| b | Streaming a video over the internet | |
| c | An old system where each node stored a whole telegram before passing it on | |
| d | Packets of one connection all follow the same route and arrive in order, but share links with other traffic | |
| e | Each packet is routed independently and may arrive out of order | |
| f | A path is reserved, so capacity is wasted during silences | |

**Expected result:** a circuit · b packet · c message · d virtual circuit · e datagram · f circuit.

- **Hint 1:** Slide 21 for circuit; slide 22 for message.
- **Hint 2:** Slides 28–30 for virtual circuit versus datagram.

---

### Task 4 — Which layer?

**Goal:** place protocols, addresses and devices in the OSI model.

Give the OSI layer number (1–7) for each:

| Item | Layer | Item | Layer |
| --- | --- | --- | --- |
| IP address | | HTTP | |
| MAC address | | Switch | |
| TCP | | Router | |
| UDP | | Hub | |
| Ethernet frame | | DNS | |
| Fibre-optic cable | | Encryption/compression (where separated) | |
| Routing | | Managing a dialogue between devices | |

Then name the **TCP/IP** layer for: IP, TCP, Ethernet, HTTP.

**Expected result:** 14 OSI answers; four TCP/IP answers.

- **Hint 1:** Addresses: MAC → 2, IP → 3. Devices: hub → 1, switch → 2, router → 3.
- **Hint 2:** Slide 33 maps OSI 5–7 to Application.

---

### Task 5 — Predict the MAC table

**Goal:** predict how a switch learns and decides.

A switch has PC1–PC4 on ports Fa0/1–Fa0/4 and an **empty** MAC table. Frames arrive in this order:

1. PC1 → broadcast
2. PC3 → PC1
3. PC1 → PC3
4. PC2 → PC4
5. PC4 → PC2

For each frame, write: what the switch **learns**, whether it **forwards** or **floods**, which **ports** it sends out of, and how many **entries** the table has afterwards.

**Expected result:** frames 1 and 4 are flooded; 2, 3 and 5 are forwarded; the table ends with 4 entries (Verified with `switch_sim.py`).

- **Hint 1:** The switch always learns the **source** first.
- **Hint 2:** In frame 4, has the switch ever seen PC4 send anything?

---

## Part B — Find and fix (Tasks 6–10)

### Task 6 — Fix the OSI table

**Goal:** correct a classmate's layer table.

Sam Archer's table has **five** errors. Find and fix them.

| Layer | Name | Sam's description |
| --- | --- | --- |
| 7 | Application | The user interface of a program |
| 6 | Presentation | Data formatting, encryption, compression |
| 5 | Session | Physical transmission of bits |
| 4 | Transport | TCP: no delivery guarantee; UDP: reliable, ordered |
| 3 | Network | MAC addressing |
| 2 | Data link | MAC addressing, error detection |
| 1 | Physical | Routing between networks |

**Expected result:** five corrected rows.

- **Hint 1:** Compare with slide 32 line by line.
- **Hint 2:** TCP and UDP have been swapped.

---

### Task 7 — Valid MAC addresses?

**Goal:** recognise well-formed MAC addresses and special ones.

Hexadecimal digits are 0–9 and A–F. For each, say **valid** or **invalid** (and why), and mark any special address.

1. `00:1A:2B:3C:4D:5E`
2. `00-1A-2B-3C-4D-5E`
3. `00:1A:2B:3C:4D`
4. `00:1G:2B:3C:4D:5E`
5. `FF:FF:FF:FF:FF:FF`
6. `192.168.10.11`
7. `02:fc:00:00:00:01`

**Expected result:** 4 valid (one broadcast, one locally administered), 3 invalid.

- **Hint 1:** A MAC address has exactly 12 hex digits (6 pairs).
- **Hint 2:** Item 6 is a different kind of address altogether.

---

### Task 8 — /25 or not?

**Goal:** apply the 255.255.255.128 mask correctly.

All masks are **255.255.255.128**. Same subnet: yes or no?

| # | A | B | Same subnet? |
| --- | --- | --- | --- |
| a | 192.168.10.11 | 192.168.10.130 | |
| b | 192.168.10.11 | 192.168.10.14 | |
| c | 192.168.10.127 | 192.168.10.128 | |
| d | 192.168.10.14 | 192.168.10.100 | |
| e | 192.168.10.129 | 192.168.10.254 | |
| f | 192.168.10.100 | 192.168.10.200 | |

Then: g. Which two addresses in 192.168.10.128/25 must **not** be given to a PC?

**Expected result:** 3 yes, 3 no (Verified with Python's `ipaddress`).

- **Hint 1:** Lower half .0–.127; upper half .128–.255.
- **Hint 2:** The first and last address of each half are special.

---

### Task 9 — Count the domains

**Goal:** count collision and broadcast domains correctly.

Sam's answers are below. Check each; correct any that are wrong.

| Network | Sam's collision domains | Sam's broadcast domains |
| --- | --- | --- |
| a. One hub with 4 PCs | 4 | 1 |
| b. One switch with 4 PCs | 4 | 4 |
| c. Two switches joined by one link, 2 PCs on each | 4 | 1 |
| d. A router with two interfaces, each to a switch with 3 PCs | 8 | 1 |

**Expected result:** every row contains at least one error.

- **Hint 1:** Each link that ends on a switch or router port is one collision domain; a hub makes everything one.
- **Hint 2:** Switches pass broadcasts on; only routers stop them.

---

### Task 10 — Fix the reasoning

**Goal:** correct wrong explanations.

Each statement is wrong. Correct it in one or two sentences.

1. "A switch sends every frame to every port, just like a hub."
2. "PC1 and PC3 are on different switches, so they need a router."
3. "IP guarantees that every packet arrives, because it is a reliable protocol."
4. "A virtual circuit reserves bandwidth just like a phone call."
5. "My MAC address is how websites on the internet find my computer."
6. "Changing the mask to 255.255.255.128 changed the IP addresses, so the ping failed."

**Expected result:** six corrected statements.

- **Hint 1:** Lecture sections 9, 10, 14 and 17.
- **Hint 2:** For 2: are they on the same IP network?

---

## Part C — Build (Tasks 11–15)

### Task 11 — Run the switch-learning simulator

**Goal:** watch a switch learn MAC addresses, then extend the model.

**Skill you gain:** you can model a network device's decision rules in code and use the model to predict its behaviour.

1. Save as `switch_sim.py`:

```python
# switch_sim.py - how an Ethernet switch learns MAC addresses.
#
# For every frame that arrives, the switch:
#   1. LEARNS: records "source MAC is reachable on the port it came in on".
#   2. FORWARDS: if it knows the destination's port, sends the frame only there;
#      if not (or if it is the broadcast address), FLOODS it out of every other port.
#
# Usage: edit FRAMES at the bottom, then run:  python switch_sim.py

BROADCAST = "FF:FF:FF:FF:FF:FF"


class Switch:
    def __init__(self, name, ports):
        self.name = name
        self.ports = ports          # e.g. ["Fa0/1", "Fa0/2", ...]
        self.mac_table = {}         # MAC address -> port (the "MAC" or "CAM" table)

    def receive(self, in_port, src, dst):
        # 1. Learn where the sender is.
        self.mac_table[src] = in_port

        # 2. Decide where the frame goes.
        if dst != BROADCAST and dst in self.mac_table:
            out = [self.mac_table[dst]]
            action = "forward"
        else:
            out = [p for p in self.ports if p != in_port]
            action = "flood"

        if out == [in_port]:        # destination is on the same port it came from
            out, action = [], "filter (drop)"
        return action, out


if __name__ == "__main__":
    MAC = {"PC1": "00:0A:00:00:00:01", "PC2": "00:0A:00:00:00:02",
           "PC3": "00:0A:00:00:00:03", "PC4": "00:0A:00:00:00:04"}
    PORT = {"PC1": "Fa0/1", "PC2": "Fa0/2", "PC3": "Fa0/3", "PC4": "Fa0/4"}

    sw = Switch("Switch0", ["Fa0/1", "Fa0/2", "Fa0/3", "Fa0/4"])

    # Each frame: (sender, receiver). "ALL" means the broadcast address.
    FRAMES = [("PC1", "ALL"),    # e.g. an ARP request: "who has 192.168.10.13?"
              ("PC3", "PC1"),    # the reply
              ("PC1", "PC3"),
              ("PC2", "PC4"),
              ("PC4", "PC2")]

    for n, (src, dst) in enumerate(FRAMES, start=1):
        dst_mac = BROADCAST if dst == "ALL" else MAC[dst]
        action, out = sw.receive(PORT[src], MAC[src], dst_mac)
        print(f"Frame {n}: {src} -> {dst:<3} | {action:<7} out of {', '.join(out) or '-'}")
        print(f"         MAC table now: {len(sw.mac_table)} entries "
              f"{sorted(sw.mac_table.items(), key=lambda kv: kv[1])}")
```

2. Run `python switch_sim.py`. *What it does:* prints the switch's decisions; it reads and changes no files. Actual output (Verified, Python 3.13):

```text
Frame 1: PC1 -> ALL | flood   out of Fa0/2, Fa0/3, Fa0/4
         MAC table now: 1 entries [('00:0A:00:00:00:01', 'Fa0/1')]
Frame 2: PC3 -> PC1 | forward out of Fa0/1
         MAC table now: 2 entries [('00:0A:00:00:00:01', 'Fa0/1'), ('00:0A:00:00:00:03', 'Fa0/3')]
Frame 3: PC1 -> PC3 | forward out of Fa0/3
         MAC table now: 2 entries [('00:0A:00:00:00:01', 'Fa0/1'), ('00:0A:00:00:00:03', 'Fa0/3')]
Frame 4: PC2 -> PC4 | flood   out of Fa0/1, Fa0/3, Fa0/4
         MAC table now: 3 entries [('00:0A:00:00:00:01', 'Fa0/1'), ('00:0A:00:00:00:02', 'Fa0/2'), ('00:0A:00:00:00:03', 'Fa0/3')]
Frame 5: PC4 -> PC2 | forward out of Fa0/2
         MAC table now: 4 entries [('00:0A:00:00:00:01', 'Fa0/1'), ('00:0A:00:00:00:02', 'Fa0/2'), ('00:0A:00:00:00:03', 'Fa0/3'), ('00:0A:00:00:00:04', 'Fa0/4')]
```

3. Compare with your Task 5 predictions.
4. **Extend it:** add a sixth frame, **PC1 → PC4**. Predict, then run. Is it forwarded or flooded?
5. **Extend it:** a hub is a switch that never learns. Change one line so the switch behaves like a hub (every frame flooded). Which line?

**Expected result:** frame 6 is forwarded out of Fa0/4 only (Verified).

- **Hint 1:** After frame 5, which ports does the table know?
- **Hint 2:** For step 5, look at the `if` condition that chooses "forward".

---

### Task 12 — Find your real MAC address and its manufacturer

**Goal:** read the MAC addresses on your own computer and look up who made the network card.

**Skill you gain:** you can identify a device's manufacturer from its MAC address, a technique used in asset discovery and digital forensics.

On your own Windows PC (Expected; not run here):

1. Command Prompt: `getmac /v`. *What it does:* lists each network adapter and its MAC ("Physical Address"). Read-only.
2. Or `ipconfig /all` and find **Physical Address** for your Wi-Fi or Ethernet adapter.
3. Write down the **first six hex digits** (the OUI).
4. Look them up in the IEEE public registry: search for "IEEE OUI lookup" or use <https://regauth.standards.ieee.org/standards-ra-web/pub/view.html#registries>. Record the manufacturer.
5. Does the manufacturer match your laptop's network card (Task 11 of Lab 1)?

**Linux example (Verified on the checking machine, `ip link show eth0`):**

```text
4: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1400 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
    link/ether 02:fc:00:00:00:01 brd ff:ff:ff:ff:ff:ff
```

`link/ether` is the MAC address and `brd ff:ff:ff:ff:ff:ff` is the broadcast MAC. This address starts with `02`, which marks it as **locally administered** (typical of virtual machines), so an OUI lookup would find no manufacturer.

**Privacy note:** do not post your MAC address publicly. Many phones and laptops now use a **random** MAC for each Wi-Fi network for privacy; if your lookup finds nothing, that may be why.

**Expected result:** a manufacturer name, or a clear reason why there is none.

- **Hint 1:** Use the address of the adapter that is actually connected.
- **Hint 2:** If the second hex digit is 2, 6, A or E, the address is locally administered.

---

### Task 13 — Look at your ARP table

**Goal:** see the IP-to-MAC mappings your computer has learned.

**Skill you gain:** you can read an ARP table, which is a first check when investigating suspected ARP spoofing.

On your own Windows PC (Expected):

1. `ping` your default gateway (from Lab 3, Task 11) so your PC has to use ARP.
2. Run `arp -a`. *What it does:* shows the ARP cache. Read-only.
3. Find the line for your gateway's IP address. Record its **Physical Address** (MAC) and **Type** (dynamic or static).
4. Find any entry ending in `.255` or starting `224.`/`239.` with MAC `ff-ff-ff-ff-ff-ff` or `01-00-5e-…`: these are broadcast and multicast entries, not real devices.
5. If two different IP addresses show the **same** MAC address, note it. On a home network that can be normal (for example a router with two addresses), but on a LAN it can also be a sign of ARP spoofing.

**Linux example (Verified, `ip neigh`):**

```text
192.0.2.1 dev eth0 lladdr 02:fc:00:00:00:05 REACHABLE
```

**Expected result:** your gateway's MAC address recorded.

- **Hint 1:** If the gateway is missing from the table, ping it again first.
- **Hint 2:** "dynamic" means it was learned by ARP; it will expire if unused.

---

### Task 14 — Watch encapsulation in Packet Tracer Simulation mode

**Goal:** see ARP and ICMP frames move through the two-switch LAN, layer by layer.

**Skill you gain:** you can use Packet Tracer's Simulation mode to inspect a PDU's headers at each OSI layer.

Use your Task 16 network (Expected; Packet Tracer was not run here):

1. Click **Simulation** (bottom-right, next to Realtime).
2. In the **Event List Filters**, click **Edit Filters** and keep only **ARP** and **ICMP** ticked.
3. From PC1's Command Prompt, `ping 192.168.10.13` (PC3). (If PC1 already knows PC3's MAC, run `arp -d` on PC1 first to clear its cache.)
4. Click **Capture/Forward** (or **Play**) step by step. Watch the envelopes move.
5. Click an envelope in the event list to open its **PDU Information**. On the **OSI Model** tab, note which layers are shown. On the **Outbound PDU Details** tab, find the Ethernet **source and destination MAC** and the IP **source and destination** addresses.
6. Fill in:

| Event | Protocol | Destination MAC | Destination IP | Which switches does it pass? |
| --- | --- | --- | --- | --- |
| 1st | ARP request | | | |
| 2nd | ARP reply | | | |
| 3rd | ICMP echo request | | | |

**Expected result:** the ARP request has destination MAC `FFFF.FFFF.FFFF` and reaches every PC; the ICMP packets carry PC3's real MAC and cross the inter-switch link.

- **Hint 1:** Packet Tracer writes MAC addresses as three groups of four hex digits, e.g. `0001.4361.A2B5`.
- **Hint 2:** An ARP request is a layer-2 broadcast, so both switches flood it.

---

### Task 15 — Build: compare message and packet switching delays

**Goal:** use a model to see why packet switching delivers messages sooner.

**Skill you gain:** you can turn a formula into code and use it to compare designs.

1. Save as `switching_delay.py`:

```python
# switching_delay.py - why packet switching delivers a message sooner than
# message switching. Simple model: ignores headers, queuing and propagation.
#
# message switching: each of the N links must receive the WHOLE message
#                    before passing it on      -> delay = N * L / R
# packet switching:  split into P packets; links work on different packets
#                    at the same time (a pipeline) -> delay = (N + P - 1) * (L / P) / R
#
# Usage: python switching_delay.py

def message_switching(L, R, N):
    """L = message size in bits, R = link rate in bits/s, N = number of links."""
    return N * L / R


def packet_switching(L, R, N, P):
    """Same, but the message is split into P equal packets."""
    return (N + P - 1) * (L / P) / R


if __name__ == "__main__":
    L = 1_000_000      # 1 Mbit message
    R = 1_000_000      # 1 Mb/s links
    N = 3              # 3 links (sender -> node -> node -> receiver)

    print(f"Message switching:            {message_switching(L, R, N):.2f} s")
    for P in (1, 10, 100):
        print(f"Packet switching, {P:>3} packets: {packet_switching(L, R, N, P):.2f} s")
```

2. Run it. Actual output (Verified, Python 3.13):

```text
Message switching:            3.00 s
Packet switching,   1 packets: 3.00 s
Packet switching,  10 packets: 1.20 s
Packet switching, 100 packets: 1.02 s
```

3. Work out by hand the message-switching and 8-packet delays for an **8 Mbit** message over **4 links** of **2 Mb/s**. Then add a line to the script to check.
4. What happens to the delay as P becomes very large? Why would real networks **not** use tiny packets?

**Expected result:** 16 s for message switching; 5.5 s with 8 packets (Verified).

- **Hint 1:** Message: 4 × 8 ÷ 2. Packets: (4 + 8 − 1) × (8 ÷ 8) ÷ 2.
- **Hint 2:** Every packet also carries a header that the model ignores.

---

## Part D — Official tasks and integration (Tasks 16–20)

### Task 16 — Continue the LAN and add a second switch (Official Tasks 1 and 2)

**Goal:** turn the one-switch LAN into a two-switch LAN.

**Skill you gain:** you can extend a working network in Packet Tracer without breaking it, and know which cable type joins two switches.

**Official Task 1: continue and expand the previous LAN**

1. Launch Cisco Packet Tracer 9.0. **File > Open** your saved **TW02A_YourStudentID.pkt**. Confirm that the workspace shows **Switch0** connected to **PC1–PC4**.
2. On each PC, **Desktop > IP Configuration**, confirm: PC1 = 192.168.10.11, PC2 = 192.168.10.12, PC3 = 192.168.10.13, PC4 = 192.168.10.14; Subnet Mask = 255.255.255.0; Default Gateway = blank.
3. **File > Save As…** **TW02B_YourStudentID.pkt**.

*Official expected result:* the file opens with Switch0 and all four PCs correctly configured on the same IP network with mask 255.255.255.0, and is saved as TW02B_YourStudentID.pkt.

**Official Task 2: add a second switch**

4. **Network Devices > Switches > 2960-24TT**; place **Switch1**.
5. Keep PC1 and PC2 on Switch0. With the **Delete** tool (X icon), delete the cables from **PC3** and **PC4** to Switch0. Press **Escape**.
6. **Connections > Copper Straight-Through**: PC3 **FastEthernet0** → Switch1 **FastEthernet0/1**; PC4 **FastEthernet0** → Switch1 **FastEthernet0/2**.
7. **Connections > Copper Cross-Over** (dashed line): Switch0 **GigabitEthernet0/1** → Switch1 **GigabitEthernet0/1**. No configuration is needed on either switch. Links may start amber; **wait until they turn green**.

*Official expected result:* the new and reconnected link indicators become green, confirming the physical connections are active.

**Why cross-over between switches? (Extra)** A straight-through cable connects devices of different kinds (PC to switch); a cross-over cable swaps the send and receive pairs so two devices of the **same** kind (switch to switch) can talk. Many modern devices detect this automatically (**auto-MDIX**), but the official lab uses the cross-over cable.

**Test plan**

| Check | Expected | Actual |
| --- | --- | --- |
| Opened file shows Switch0 + PC1–PC4 | Yes | |
| IP settings confirmed on all four PCs | As listed | |
| Saved as TW02B file | `TW02B_<your ID>.pkt` | |
| PC3, PC4 on Switch1 Fa0/1, Fa0/2 | Yes | |
| Switch0 Gi0/1 ↔ Switch1 Gi0/1 with cross-over | Green both ends | |

- **Hint 1:** Hover over a cable end to see which port it uses.
- **Hint 2:** If the inter-switch link stays red, check you used the Gigabit ports on both switches.

---

### Task 17 — Test the expanded LAN and observe addresses (Official Tasks 3 and 4)

**Goal:** prove the two-switch LAN works and record the two kinds of address.

**Official Task 3: test the expanded LAN**

1. **PC1 > Desktop > Command Prompt**. Run separately: `ping 192.168.10.12`, `ping 192.168.10.13`, `ping 192.168.10.14`.

   *Official expected result:* each destination becomes reachable with `Reply from…` messages. The first attempt may occasionally time out while the devices establish the information needed for communication; if so, wait and repeat. PC1 and PC2 communicate locally via Switch0, while traffic between PC1 and PC3/PC4 crosses the inter-switch link, **without requiring IP address changes**.

2. Answer the official review questions in your notes:
   1. Did adding the second switch require changing the IP addresses on any of the PCs?
   2. Complete the path taken by frames between devices: PC1 → ______ → ______ → PC3
   3. Are PC1 and PC3 still part of the same local IP network?
3. **Screenshot:** arrange the workspace so both switches and all four PCs are visible, with PC1's Command Prompt showing successful pings. Capture one screenshot (Windows key + Shift + S).

**Official Task 4: observe IP and MAC addresses**

4. **PC1 > Config** tab > **FastEthernet0**. Record the **MAC Address** and **IP Address**. Repeat for **PC3**.

   | Device | IP address | MAC address |
   | --- | --- | --- |
   | PC1 | | |
   | PC3 | | |

   *Official explanation:* an IP address is a **logical Layer 3** address used to identify a device or interface on an IP network. A MAC address is a **48-bit Layer 2** address associated with a network interface and used for Ethernet frame delivery on the local network.

5. **Supplementary:** on PC1, run `arp -a` after the pings. Does PC3's MAC address in the ARP table match what you recorded from PC3's Config tab?

**Test plan**

| Check | Expected | Actual |
| --- | --- | --- |
| PC1 → PC2 | Replies (via Switch0 only) | |
| PC1 → PC3 | Replies (via Switch0 and Switch1) | |
| PC1 → PC4 | Replies | |
| Review questions answered | 3 answers | |
| Screenshot shows both switches, all PCs, successful pings | Yes | |
| MAC and IP recorded for PC1 and PC3 | Yes | |
| ARP table on PC1 matches PC3's MAC | Yes | |

- **Hint 1:** The path question is about switches.
- **Hint 2:** Did the network part of any address change?

---

### Task 18 — Subnet-mask experiment and broken link (Official Task 5 and Extra Challenge)

**Goal:** see a mask change and a link failure stop communication, and explain both.

**Official Task 5: simple subnet-mask experiment**

- **Stage A, valid host IP:** PC4 > **IP Configuration** > IP **192.168.10.130**, mask **255.255.255.0**, gateway blank. From PC1: `ping 192.168.10.130`. Confirm successful replies.
- **Stage B, modified mask:** PC1: keep 192.168.10.11, change the mask to **255.255.255.128**. PC4: keep 192.168.10.130, change the mask to **255.255.255.128**. Gateways blank. From PC1: `ping 192.168.10.130` again. Observe the failure (`Request timed out` or `Destination host unreachable`) caused by the hosts being in **separate logical subnets without a router**.
- **Stage C, restore:** PC1 back to **192.168.10.11 / 255.255.255.0**; PC4 back to **192.168.10.14 / 255.255.255.0**; gateways blank. `ping 192.168.10.14` from PC1 to verify.

*Official expected result:* pings succeed with mask 255.255.255.0; after both are changed to 255.255.255.128, communication fails because they are in different subnets and no router is present; after restoring, it succeeds again.

**Official Extra Challenge: broken inter-switch link**

1. Confirm working pings from PC1 to PC2 (192.168.10.12) and PC3 (192.168.10.13).
2. With the **Delete** tool, delete **only** the cross-over cable between Switch0 Gi0/1 and Switch1 Gi0/1. Press Escape.
3. From PC1, ping PC2 and note the result; then ping PC3 and note the result.
4. Reconnect Switch0 Gi0/1 ↔ Switch1 Gi0/1 with a **Copper Cross-Over** cable. Wait for green, then re-verify PC1 → PC3.

*Official expected result:* ping to PC2 succeeds (same switch); ping to PC3 fails (link broken); reconnecting restores full connectivity.

**Your explanation (write it):** using the /25 table in lecture section 17, show which subnet each PC was in during Stage B. Then explain, using the switch-learning rules, why PC2 is still reachable when the link is broken.

**Record**

| Stage | PC1 address/mask | PC4 address/mask | Same subnet? (your working) | Ping result |
| --- | --- | --- | --- | --- |
| A | 192.168.10.11 /24 | 192.168.10.130 /24 | | |
| B | 192.168.10.11 /25 | 192.168.10.130 /25 | | |
| C | 192.168.10.11 /24 | 192.168.10.14 /24 | | |
| Link broken: PC1 → PC2 | — | — | — | |
| Link broken: PC1 → PC3 | — | — | — | |

- **Hint 1:** /25: .0–.127 and .128–.255.
- **Hint 2:** PC1 and PC2 hang off the same switch; the broken cable is not on their path.

---

### Task 19 — Mini-project: a layer-by-layer evidence report

**Goal:** collect real evidence for each layer of the model from your own computer.

**Skill you gain:** you can use standard tools to gather evidence at each network layer and present it in a structured technical table, which is the basis of a network investigation.

On your own computer (Expected), fill this table with **real values you observed** (keep private details such as your public IP out of anything you share):

| TCP/IP layer (OSI layers) | Question | Tool | Your evidence |
| --- | --- | --- | --- |
| Application (5–7) | What IP address does www.ljmu.ac.uk resolve to? | `nslookup www.ljmu.ac.uk` | |
| Transport (4) | Which protocol does a web page use underneath? | Reasoning (HTTP/HTTPS run over TCP) | |
| Internet (3) | What is your IP address and gateway? How many hops to www.ljmu.ac.uk? | `ipconfig`, `tracert` | |
| Network access (1–2) | What is your MAC address? What is your gateway's MAC? Wired or wireless? Link speed? | `getmac /v`, `arp -a`, Settings > Network | |

Then write 150–200 words explaining how one web request moves **down** the layers on your PC and back **up** on the server, using the word **encapsulation**.

**Test plan**

| Check | Expected | Actual |
| --- | --- | --- |
| Every row has a real observed value | Yes | |
| Each value has a unit or format (e.g. Mb/s, dotted decimal, hex) | Yes | |
| Explanation uses the layer names correctly | Yes | |
| No public IP or full MAC published | Yes | |

- **Hint 1:** `nslookup` asks DNS, an application-layer service, which answers with an IP address.
- **Hint 2:** Your link speed appears in Settings > Network & internet > (your connection) > Properties.

---

### Task 20 — Assessment-style practice: switching and models

**This is practice only, not a real exam question.** The module exam is two hours with short-answer and essay-style questions; the report covers data storage and networking (module guide). The slides state that **AS1 is handed out on 6 October 2026**: check the real brief on Canvas for its requirements. Marks below are invented for planning.

**Rules:** 25 minutes, closed book, write it yourself.

**(a)** Explain the difference between a MAC address and an IP address. *(3 marks)*

**(b)** Explain how a switch builds its MAC table and what it does with a frame for an unknown destination. *(4 marks)*

**(c)** Compare circuit switching and packet switching, giving one advantage of each. *(4 marks)*

**(d)** Describe the OSI and TCP/IP models and explain how they correspond. Use sending a web page as an example, naming the PDU and the address used at the transport, network and data-link layers. *(9 marks; aim for 250–350 words)*

**Self-marking checklist**

| Part | A good answer includes | Expected | Actual |
| --- | --- | --- | --- |
| (a) | MAC: 48-bit, layer 2, local delivery, set by manufacturer; IP: 32-bit (IPv4), layer 3, logical, across networks | 3 points | |
| (b) | Learns source MAC + port for every frame; forwards known; floods unknown/broadcast except arrival port | 4 points | |
| (c) | Circuit: reserved path, predictable, wasteful, set-up can fail; packet: shared links, efficient for bursty data, variable delay | 4 points | |
| (d) | All 7 OSI layers named; 4 TCP/IP layers and mapping; segment/port, packet/IP address, frame/MAC; encapsulation; why two models exist | 9 points | |
| Time | Within 25 minutes | Yes | |

- **Hint 1:** For (d), draw the two columns first, then write.
- **Hint 2:** Lecture sections 15–16.

---

## Tracker

| Task | Name | Done | Notes / score |
| --- | --- | --- | --- |
| 1 | Bits, bytes and transfer times | ☐ | /6 |
| 2 | Choose the medium | ☐ | /6 |
| 3 | Circuit, message or packet? | ☐ | /6 |
| 4 | Which layer? | ☐ | /18 |
| 5 | Predict the MAC table | ☐ | /5 |
| 6 | Fix the OSI table | ☐ | /5 |
| 7 | Valid MAC addresses? | ☐ | /7 |
| 8 | /25 or not? | ☐ | /7 |
| 9 | Count the domains | ☐ | /4 |
| 10 | Fix the reasoning | ☐ | /6 |
| 11 | Switch-learning simulator | ☐ | |
| 12 | Your real MAC and manufacturer | ☐ | |
| 13 | Your ARP table | ☐ | |
| 14 | Packet Tracer Simulation mode | ☐ | |
| 15 | Switching delay model | ☐ | |
| 16 | **Official Tasks 1–2** — Continue LAN, add switch | ☐ | |
| 17 | **Official Tasks 3–4** — Test, observe addresses | ☐ | |
| 18 | **Official Task 5 + Extra Challenge** | ☐ | |
| 19 | Mini-project: layer evidence report | ☐ | |
| 20 | Assessment-style practice | ☐ | /20 |

## Reflection

1. Before this lab, would you have expected PC1 and PC3 to need a router once they were on different switches? What changed your mind?
2. In Task 14, what surprised you about the ARP request?
3. Explain in your own words why changing only the subnet mask broke the ping in Task 18.
4. Which layer of the OSI model do you feel least sure about, and what will you do about it?

---

## Answer key

**(Verified)** = calculated or run with Python 3.13 (`switch_sim.py`, `switching_delay.py`, `ipaddress`) or on the Linux checking machine. **(Expected)** = Packet Tracer or your own computer; not run here.

### Task 1 (Verified)

a 800 Mb ÷ 100 Mb/s = **8 s** · b 800 ÷ 1,000 = **0.8 s** · c 40,000 Mb ÷ 1,000 = **40 s** · d 5,600 ÷ 80 = **70 s** · e 8 ÷ 10 = **0.8 s**.
f: "80 Mb/s" is megabits; 700 MB is 5,600 megabits, so the best case is 70 s, and real downloads also lose capacity to headers, other traffic and the server's speed.

### Task 2 (model answers)

1 Fibre: long distance at high speed. 2 Twisted-pair copper: cheap, short runs, standard for desktops. 3 Wireless: mobility, no cables for customers. 4 Fibre: immune to electromagnetic interference. 5 Coaxial: existing cable-TV infrastructure. 6 Fibre: much harder to tap without detection (and encrypt the data anyway).

### Task 3

a circuit · b packet · c message · d virtual circuit · e datagram · f circuit.

### Task 4

| Item | Layer | Item | Layer |
| --- | --- | --- | --- |
| IP address | 3 | HTTP | 7 |
| MAC address | 2 | Switch | 2 |
| TCP | 4 | Router | 3 |
| UDP | 4 | Hub | 1 |
| Ethernet frame | 2 | DNS | 7 |
| Fibre-optic cable | 1 | Encryption/compression | 6 |
| Routing | 3 | Managing a dialogue | 5 |

TCP/IP: IP → Internet · TCP → Transport · Ethernet → Network access · HTTP → Application.

### Task 5 (Verified)

| Frame | Learns | Action | Out of | Entries |
| --- | --- | --- | --- | --- |
| 1 PC1 → broadcast | PC1 on Fa0/1 | Flood | Fa0/2, Fa0/3, Fa0/4 | 1 |
| 2 PC3 → PC1 | PC3 on Fa0/3 | Forward | Fa0/1 | 2 |
| 3 PC1 → PC3 | (already known) | Forward | Fa0/3 | 2 |
| 4 PC2 → PC4 | PC2 on Fa0/2 | Flood | Fa0/1, Fa0/3, Fa0/4 | 3 |
| 5 PC4 → PC2 | PC4 on Fa0/4 | Forward | Fa0/2 | 4 |

### Task 6

Errors: layer 7 is network **services** used by applications (not the UI); layer 5 manages dialogues/connections (not bits); layer 4 TCP **reliable, ordered**, UDP **no guarantee** (swapped); layer 3 **logical addressing and routing (IP)** (not MAC); layer 1 **transmission of bits** (not routing). Rows 6 and 2 are correct.

### Task 7

1 Valid · 2 Valid (hyphens are also used) · 3 **Invalid**: only 10 hex digits · 4 **Invalid**: G is not a hex digit · 5 Valid: the **broadcast** address · 6 **Invalid**: that is an IPv4 address, not a MAC · 7 Valid: **locally administered** (leading 02). So 4 valid, 3 invalid.

### Task 8 (Verified)

a **no** (.11 lower, .130 upper) · b yes · c **no** (.127 is the lower broadcast; .128 the upper network address) · d yes · e yes · f **no**.
g: **192.168.10.128** (network address) and **192.168.10.255** (broadcast address).

### Task 9

| Network | Correct collision | Correct broadcast | Sam |
| --- | --- | --- | --- |
| a hub, 4 PCs | **1** | 1 | Collision wrong |
| b switch, 4 PCs | 4 | **1** | Broadcast wrong |
| c two switches | **5** (4 PC links + inter-switch link) | 1 | Collision wrong |
| d router + 2 switches | 8 | **2** | Broadcast wrong |

None of Sam's rows is fully correct: each has one wrong number. (Row d's collision count of 8 is right, but its broadcast count is wrong.)

### Task 10

1. A switch learns MAC addresses and forwards known destinations to one port; it floods only broadcasts and unknown destinations.
2. They are still on the same IP network (192.168.10.0/24); switches pass frames between them, so no router is needed.
3. IP is best-effort and does not acknowledge or retransmit; TCP (above IP) adds reliability.
4. A virtual circuit fixes the route and order but shares the links; only circuit switching reserves capacity.
5. MAC addresses only work on the local network; websites reach you by IP address (routers replace the frame at every hop).
6. The IP addresses did not change; the mask changed which addresses each PC treats as local, putting PC1 and PC4 in different /25 subnets.

### Task 11 (Verified)

Step 4: add `("PC1", "PC4")` to `FRAMES` → `Frame 6: PC1 -> PC4 | forward out of Fa0/4`. Step 5: change `if dst != BROADCAST and dst in self.mac_table:` to `if False:` so every frame is flooded, like a hub.

Two-switch extension (optional, Verified): modelling Switch0 and Switch1 joined by Gi0/1, after the frames PC1 → broadcast, PC3 → PC1, PC1 → PC3 and PC2 → PC4, Switch0's table lists PC3 on **Gi0/1** and Switch1's table lists PC1 and PC2 on **Gi0/1**: each switch sees every remote PC through the inter-switch port. With that link removed, PC1 → PC2 is still delivered but PC1 → PC4 is not.

### Task 12 (Expected)

Your manufacturer. For the Verified Linux example, `02:fc:00:00:00:01` is locally administered, so no manufacturer is registered.

### Task 13 (Expected)

Your gateway's MAC, type "dynamic". Broadcast/multicast entries are not devices.

### Task 14 (Expected)

1st: ARP request, destination MAC `FFFF.FFFF.FFFF` (broadcast), destination IP 192.168.10.13 (the address being asked about), flooded by both switches to every PC. 2nd: ARP reply from PC3, unicast to PC1's MAC, crosses Switch1 → Switch0. 3rd: ICMP echo request, destination MAC = PC3's MAC, destination IP 192.168.10.13, crosses Switch0 → Switch1.

### Task 15 (Verified)

Message switching: 4 × 8 Mbit ÷ 2 Mb/s = **16 s**. Eight 1-Mbit packets: (4 + 8 − 1) × (1 ÷ 2) = 11 × 0.5 = **5.5 s**. Check line: `print(message_switching(8_000_000, 2_000_000, 4), packet_switching(8_000_000, 2_000_000, 4, 8))` prints `16.0 5.5`. As P grows, the delay approaches L/R (4 s here; 4.012 s with 1,000 packets, Verified), but each real packet carries a header, so very small packets waste capacity.

### Tasks 16–17 (Expected)

Review questions: (1) **No**: no IP address changed. (2) PC1 → **Switch0** → **Switch1** → PC3. (3) **Yes**: both are in 192.168.10.0/24. MAC addresses: your own (Packet Tracer assigns them); IPs 192.168.10.11 and 192.168.10.13.

### Task 18 (network calculations Verified; Packet Tracer results Expected)

| Stage | Same subnet? | Ping |
| --- | --- | --- |
| A | Yes: both in 192.168.10.0/24 | Replies |
| B | **No**: PC1 in 192.168.10.0/25 (.0–.127), PC4 in 192.168.10.128/25 (.128–.255) | Fails |
| C | Yes: both in 192.168.10.0/24 | Replies |
| Link broken: PC2 | — | Replies: PC1 and PC2 are both on Switch0 |
| Link broken: PC3 | — | Fails: the only path to Switch1 is gone |

### Task 19 (Expected)

Your values. Model explanation points: the browser's HTTP request (application) is placed in a TCP segment with port numbers (transport), then an IP packet with source and destination IP addresses (internet), then an Ethernet or Wi-Fi frame with MAC addresses and an FCS (network access), then sent as bits. Each router removes and rebuilds the frame for the next link; the server reverses the process going up.

### Task 20 (model points)

(a) MAC: 48-bit layer-2 hardware address for local frame delivery; IP: 32-bit (IPv4) logical layer-3 address used across networks via routers. (b) For each frame, record source MAC → arrival port; forward known destinations out of one port; flood unknown or broadcast frames out of all other ports; filter frames whose destination is on the arrival port. (c) Circuit: reserved path gives predictable quality, but capacity is wasted and set-up can fail; packet: links shared efficiently, good for bursty traffic, but delay and loss vary. (d) Name OSI 7–1 and TCP/IP's four layers with the mapping (Application = 5–7, Transport = 4, Internet = 3, Network access = 1–2); transport → segment with port numbers; network → packet with IP addresses; data link → frame with MAC addresses; describe encapsulation down and up; OSI used for teaching/troubleshooting, TCP/IP for the real protocols.
