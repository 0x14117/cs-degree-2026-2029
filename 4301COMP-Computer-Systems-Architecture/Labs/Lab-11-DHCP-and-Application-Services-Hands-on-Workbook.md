# Lab 11 — DHCP and Application Services Hands-on Workbook (20 Tasks)

**Module:** 4301COMP Computer Systems Architecture

**Session:** Teaching Week 06, Session A · **Matching lecture:** `../Lectures/Lecture-11-DHCP-and-Application-Services.md`

---

## How to use this lab

**What this lab is for.** You will:

- build the official visitor-information kiosk network, with the router as the only DHCP server;
- watch the four DORA messages and an HTTP exchange;
- diagnose an HTTP fault using evidence;
- work out exactly what a DHCP pool hands out;
- tell apart the different ways a service can fail.

**Where the official tasks are.**

| Official lab sheet (TW06 Session A) | This workbook |
| --- | --- |
| Task 1 — Build a visitor information network | Task 16 |
| Task 2 — Add and test the information service | Task 17 |
| Extra Challenge — Diagnose an HTTP fault | Task 18 |

In the timetabled lab, **do Tasks 16–18 first**.

**Tools**

| Tool | Used in | Notes |
| --- | --- | --- |
| Cisco Packet Tracer 9.0 | Tasks 15–19 | Named on the official sheet |
| Microsoft Word | Tasks 16–18 | For `TW06A_YourStudentID.docx` |
| Windows Command Prompt / PowerShell | Tasks 13–14 | Your own computer; read-only commands |
| Python 3 | Tasks 11, 13 | **Optional, your choice.** Built-in modules only |
| A Linux system with `sudo` (VM or WSL) | Task 12 | **Optional.** Only if you already have one |

**Rules:**

- Predict before you test.
- Test configuration before application behaviour (slide 12).
- Change only the setting the evidence supports (slide 14).
- Capture evidence that proves the claim (slide 15).

**Labels:**

- **Verified** = run before being written here. The kiosk network was rebuilt as a real Linux network with a real DHCP server and web server, captured with `tcpdump`; Python 3.13.
- **Expected** = not run here (Packet Tracer, Cisco IOS, Windows).

---

## Part A — Warm-up: predict and calculate (Tasks 1–5)

### Task 1 — Who sends what, to where?

**Goal:** describe each DORA message precisely.

Complete the table for a kiosk client getting an address from the router (172.20.5.1).

| Message | Sent by | Source IP | Destination IP | Broadcast or not? | Key content |
| --- | --- | --- | --- | --- | --- |
| Discover | | | | | |
| Offer | | | | | |
| Request | | | | | |
| Acknowledge | | | | | |

Then answer: why is the **Request** still sent to everyone, when the client already knows which server it wants?

**Expected result:** the client sends from 0.0.0.0 to 255.255.255.255 (Verified capture in lecture section 6.2).

- **Hint 1:** In this Linux capture, the server's Offer and Ack were also broadcast, because the client set the "broadcast" flag. Some clients ask for unicast replies instead.
- **Hint 2:** Option 54 names the chosen server.

---

### Task 2 — What does the pool really hand out?

**Goal:** calculate IOS pools exactly (slide 6).

For each configuration, give the range of addresses handed out and the count. Show your working.

**a)**

```text
ip dhcp excluded-address 172.20.5.1 172.20.5.99
ip dhcp excluded-address 172.20.5.125 172.20.5.254
ip dhcp pool VISITORS
 network 172.20.5.0 255.255.255.0
```

**b)**

```text
ip dhcp excluded-address 192.168.10.1 192.168.10.49
ip dhcp pool STAFF
 network 192.168.10.0 255.255.255.0
```

**c)**

```text
ip dhcp excluded-address 10.1.1.1 10.1.1.20
ip dhcp excluded-address 10.1.1.201 10.1.1.254
ip dhcp pool LAB
 network 10.1.1.0 255.255.255.0
```

**d)**

```text
ip dhcp excluded-address 172.16.8.1 172.16.8.255
ip dhcp pool CAMPUS
 network 172.16.8.0 255.255.252.0
```

**e)**

```text
ip dhcp excluded-address 192.168.50.1
ip dhcp pool SMALL
 network 192.168.50.0 255.255.255.128
```

**Expected result:** 25, 205, 180, 767 and 125 addresses (Verified with `pool_policy.py`).

- **Hint 1:** Handed out = usable hosts in the network − excluded addresses.
- **Hint 2:** In d, a /22 covers 172.16.8.0–172.16.11.255. Is 172.16.9.0 a usable host?

---

### Task 3 — Static or dynamic?

**Goal:** apply slide 7's roles.

For each device in a visitor centre, choose **static**, **DHCP pool** or **DHCP reservation**, and give a reason.

1. The router's LAN interface
2. The information server
3. A visitor's phone
4. A network printer used by staff
5. A staff laptop that moves between offices
6. A digital sign that a monitoring system checks every minute by IP address

**Expected result:** infrastructure static, or reserved where it must stay on DHCP; visitors in the pool.

- **Hint 1:** Does anything else need to know the device's address in advance?
- **Hint 2:** A reservation gives a fixed address but still uses DHCP.

---

### Task 4 — Is a relay needed?

**Goal:** apply slide 8.

Say **relay needed** or **not needed**, with a reason.

| # | Situation |
| --- | --- |
| a | The router is the DHCP server; clients are on the router's G0/0 LAN (the official lab) |
| b | The DHCP server is 172.20.5.10; clients are on 172.20.6.0/24 behind the router |
| c | The DHCP server and clients are in the same VLAN on one switch |
| d | Clients are in VLAN 120; the DHCP server is in VLAN 110; a router connects the VLANs |
| e | Clients are on the same LAN as the server, but the clients' gateway is wrong |

**Expected result:** relay needed only in b and d.

- **Hint 1:** Do the client and server share a broadcast domain?
- **Hint 2:** For e: does a broadcast use the gateway at all?

---

### Task 5 — Interpret the symptom

**Goal:** apply slide 13 and name the next test, not a guess.

| # | Symptom | Most likely area | Next test |
| --- | --- | --- | --- |
| a | PC2 shows 169.254.33.9 | | |
| b | PC1 has 172.20.5.101, but `ping 172.20.5.1` fails | | |
| c | `ping 172.20.5.10` succeeds, the page fails | | |
| d | PC3 shows 172.20.5.10 (the server's address!) | | |
| e | PC1 shows 192.168.1.100, gateway 192.168.1.1 | | |
| f | Ping succeeds; a port check of 172.20.5.10:80 says REFUSED | | |

**Expected result:** six specific next tests.

- **Hint 1:** For d: which IOS command shows what the pool can hand out?
- **Hint 2:** For e: which DHCP server could give a 192.168.1.x address here? (Official lab Task 1.)

---

## Part B — Find and fix (Tasks 6–10)

### Task 6 — Fix the DHCP configuration

**Goal:** correct a broken router session.

Sam Archer typed this to set up the kiosk. **Five** problems stop it meeting the design (gateway .1, server .10, pool .100–.124).

```text
Router> configure terminal
Router(config)# interface g0/0
Router(config-if)# ip address 172.20.5.1 255.255.255.0
Router(config-if)# exit
Router(config)# ip dhcp excluded-address 172.20.5.1 172.20.5.9
Router(config)# ip dhcp pool VISITORS
Router(dhcp-config)# network 172.20.5.0 255.255.255.0
Router(dhcp-config)# default-router 172.20.6.1
Router(dhcp-config)# end
```

What `pool_policy.py` says about Sam's pool lines (Verified):

```text
Pool network : 172.20.5.0/24
Handed out   : 172.20.5.10-172.20.5.254  (245 addresses)
PROBLEM: default-router 172.20.6.1 is outside 172.20.5.0/24
PROBLEM: Service-Server 172.20.5.10 is INSIDE the pool: a client could be given it
```

List the five problems and write the corrected session.

**Expected result:** a corrected session that matches official lab step 1.2.

- **Hint 1:** Two problems are not in the pool lines at all: look at the prompts and the interface.
- **Hint 2:** How many `excluded-address` lines does the official design need?

---

### Task 7 — Fix the relayed network

**Goal:** diagnose a relay design that "nearly works".

A second visitor network, 172.20.6.0/24, was added behind the router. The DHCP server is at 172.20.5.10 and a relay runs on the router. On the real Linux build, the client's first attempt gave (Verified):

```text
-> DISCOVER  from 0.0.0.0 (MAC ca:f2:14:93:fe:3e) to 255.255.255.255, xid 0x0169299e
<- OFFER     from 172.20.6.1: address 172.20.6.113, mask 255.255.255.0, router 172.20.5.1, lease 3600 s
-> REQUEST   broadcast: 'I accept 172.20.6.113 from server 172.20.5.10'
<- ACK       from 172.20.6.1: lease confirmed for 172.20.6.113
```

1. Did the relay work? How can you tell?
2. What is wrong with the lease, and what will the client fail to do?
3. What is the smallest fix, and on which device?
4. What is the Cisco IOS command that enables the relay, and on which interface?
5. Someone suggests also adding a relay on the router's **172.20.5.1** interface "to be safe". Why is that not justified?

**Expected result:** the router option must be 172.20.6.1 for the 172.20.6.0/24 pool.

- **Hint 1:** Compare the client's address with the "router" in the Offer.
- **Hint 2:** Slide 8's last line.

---

### Task 8 — Read the real failures

**Goal:** identify faults from real evidence.

These are **real results** from the rebuilt kiosk network (Verified). For each one, say which link in the dependency chain is broken and the next check.

**Evidence 1:** a new client's DHCP attempt, after 25 clients already had leases:

```text
-> DISCOVER  from 0.0.0.0 (MAC 02:00:00:00:00:17) to 255.255.255.255, xid ...
   (none)    no OFFER within 10 seconds: no DHCP server reachable, or the pool is full
```

The server's log said `no address available`.

**Evidence 2:**

```text
curl: (7) Failed to connect to 172.20.5.10 port 80 after 0 ms: Couldn't connect to server
```

`ping 172.20.5.10` replied.

**Evidence 3:**

```text
curl: (7) Failed to connect to 172.20.5.10 port 80 after 3064 ms: Couldn't connect to server
```

**Evidence 4:** captured on PC1 while loading the page:

```text
IP 172.20.5.116.58668 > 172.20.5.10.80: Flags [S], seq 3142006468, length 0
IP 172.20.5.10.80 > 172.20.5.116.58668: Flags [R.], seq 0, ack 3142006469, length 0
```

**Evidence 5:** a client on 172.20.6.0/24 with the DHCP server at 172.20.5.10 and **no relay**:

```text
-> DISCOVER  from 0.0.0.0 (MAC ca:f2:14:93:fe:3e) to 255.255.255.255, xid 0x0cb499a3
   (none)    no OFFER within 10 seconds: no DHCP server reachable, or the pool is full
```

Evidences 2 and 3 show the same `curl` error. What tells them apart?

**Expected result:**

- 1: pool exhausted;
- 2 and 4: service off (refused, RST);
- 3: no path (time taken, no reply);
- 5: broadcast not forwarded.

- **Hint 1:** "after 0 ms" versus "after 3064 ms".
- **Hint 2:** `[R.]` is a TCP reset.

---

### Task 9 — Fix weak evidence

**Goal:** apply slide 15.

Each item is a screenshot caption from a student's Word document. Rewrite each so that the evidence **proves** the claim. Say what extra screenshot or output is needed.

1. "PC2 got an IP from DHCP." *(Screenshot: `ipconfig` on PC2.)*
2. "HTTP fault proven." *(Screenshot: a browser showing an error.)*
3. "Fixed." *(Screenshot: the Visitor Information page.)*
4. "DORA works." *(Screenshot: the Event List with ten coloured squares, none selected.)*

**Expected result:** each caption names the device, the command or service, what the result shows, and how it rules out an unrelated explanation.

- **Hint 1:** Could the address in 1 have been typed by hand?
- **Hint 2:** In 2, was it a **fresh** request? Is the path proven to work?

---

### Task 10 — Fix the repairs

**Goal:** apply slide 14: change only what the evidence supports.

For each repair, say whether it is justified. If not, give the right one.

| # | Evidence | Repair someone made |
| --- | --- | --- |
| a | Ping to the server succeeds; the page fails; HTTP is Off | Changed PC3's gateway to 172.20.5.10 |
| b | PC1 shows 169.254.x.x; the router pool is correct; Server-PT DHCP is Off; PC1's link is red | Gave PC1 a static address 172.20.5.150 |
| c | Two PCs get addresses in 192.168.0.x | Turned Server-PT **Services > DHCP** Off, then renewed the PCs |
| d | The server ping fails from PC1; PC1's gateway ping succeeds | Changed the router's DHCP pool |
| e | The page fails only from PC2; `ipconfig` shows PC2 with a static 172.20.5.10 | Set PC2 back to DHCP |

**Expected result:** a and d are not justified; c and e are; b hides the real fault.

- **Hint 1:** Official lab: "Do not change the router configuration to repair a local server-connectivity fault."
- **Hint 2:** In b, what does the red link tell you?

---

## Part C — Build (Tasks 11–15)

### Task 11 — Calculate a pool from IOS configuration

**Goal:** automate slide 6's policy check.

**Skill you gain:** you can read device configuration with a script and check it against a design. Configuration auditing tools do the same thing at scale.

1. Save as `pool_policy.py`:

```python
# pool_policy.py - work out which addresses a Cisco IOS DHCP pool will really hand out.
# IOS hands out every address in the pool's "network" EXCEPT the excluded ranges
# (and never the network or broadcast address). This script applies the same rule,
# then checks the result against the static infrastructure addresses (slides 6, 7 and 16).
#
# Usage: python pool_policy.py

import ipaddress

# Paste the relevant lines from the router configuration here.
CONFIG = """
ip dhcp excluded-address 172.20.5.1 172.20.5.99
ip dhcp excluded-address 172.20.5.125 172.20.5.254
ip dhcp pool VISITORS
 network 172.20.5.0 255.255.255.0
 default-router 172.20.5.1
"""

# Addresses that must never be handed out (gateway, server, printers, ...).
STATIC = {"Router G0/0 (gateway)": "172.20.5.1", "Service-Server": "172.20.5.10"}


def pool_from_config(text):
    excluded, network, gateway = [], None, None
    for line in text.strip().splitlines():
        words = line.split()
        if words[:3] == ["ip", "dhcp", "excluded-address"]:
            first = ipaddress.ip_address(words[3])
            last = ipaddress.ip_address(words[4]) if len(words) > 4 else first
            excluded.append((first, last))
        elif words[:1] == ["network"]:
            network = ipaddress.ip_network(f"{words[1]}/{words[2]}")
        elif words[:1] == ["default-router"]:
            gateway = ipaddress.ip_address(words[1])
    usable = [a for a in network.hosts() if not any(f <= a <= l for f, l in excluded)]
    return network, gateway, usable


def ranges(addresses):
    """Turn a sorted list of addresses into readable first-last ranges."""
    out, start, prev = [], None, None
    for a in addresses:
        if start is None:
            start = prev = a
        elif int(a) == int(prev) + 1:
            prev = a
        else:
            out.append(f"{start}-{prev}" if start != prev else str(start))
            start = prev = a
    if start is not None:
        out.append(f"{start}-{prev}" if start != prev else str(start))
    return ", ".join(out) or "(none)"


def check(text, static):
    network, gateway, usable = pool_from_config(text)
    print(f"Pool network : {network}")
    print(f"Handed out   : {ranges(usable)}  ({len(usable)} addresses)")
    problems = []
    if gateway is None:
        problems.append("no default-router: clients will get no gateway")
    elif gateway not in network:
        problems.append(f"default-router {gateway} is outside {network}")
    for name, addr in static.items():
        if ipaddress.ip_address(addr) in usable:
            problems.append(f"{name} {addr} is INSIDE the pool: a client could be given it")
    print("\n".join("PROBLEM: " + p for p in problems) if problems else "No conflicts with static addresses.")
    return len(usable), problems


if __name__ == "__main__":
    check(CONFIG, STATIC)
```

2. Run `python pool_policy.py`. *What it does:* reads the configuration text in the script and prints the pool and any conflicts; it does not connect to any device. Actual output (Verified):

```text
Pool network : 172.20.5.0/24
Handed out   : 172.20.5.100-172.20.5.124  (25 addresses)
No conflicts with static addresses.
```

3. Check your Task 2 answers by pasting each configuration into `CONFIG`.
4. Paste Sam's lines from Task 6 and confirm the two problems it finds.
5. **Extend:** add a check that warns if the pool has **fewer than** a required number of addresses (for example, 30 visitors).

**Expected result:** Task 2 answers confirmed. Sam's pool hands out 245 addresses, including the server's (Verified).

- **Hint 1:** `STATIC` is a dictionary of name → address.
- **Hint 2:** For step 5, add a `needed` parameter and compare it with `len(usable)`.

---

### Task 12 — See DORA with your own DHCP client (optional, Linux)

**Goal:** build the four DHCP messages yourself and watch the answers.

**Skill you gain:** you can construct and read real protocol packets byte by byte. This is how protocol analysis and many security tools work.

**Only with a Linux system and `sudo`.** Do this inside a test network such as the one from Lab 10 Task 15. Do **not** run it on a university or public network: a DHCP request takes an address from that network's pool.

1. Save as `dora_client.py`:

```python
# dora_client.py - a tiny DHCP client that shows the four DORA messages one by one.
# It builds real DHCP packets (RFC 2131), broadcasts them and prints what comes back.
# Linux only, needs root (it uses client port 68 and binds to one interface).
#
# Usage: sudo python3 dora_client.py eth0                 (uses the interface's own MAC)
#        sudo python3 dora_client.py eth0 02:00:00:00:00:07   (pretend to be another client)
# It only asks for a lease and prints it; it does not change the interface's address.

import random
import socket
import struct
import sys

MSG = {1: "DISCOVER", 2: "OFFER", 3: "REQUEST", 5: "ACK", 6: "NAK"}
MAGIC = b"\x63\x82\x53\x63"                       # marks the start of DHCP options


def mac_of(ifname):
    return open(f"/sys/class/net/{ifname}/address").read().strip()


def build(msg_type, xid, mac, extra=b""):
    """BOOTP header (236 bytes) + magic cookie + options."""
    chaddr = bytes.fromhex(mac.replace(":", "")) + b"\x00" * 10
    header = struct.pack("!BBBBIHH4s4s4s4s16s64s128s",
                         1, 1, 6, 0,              # op=request, Ethernet, MAC length 6, hops 0
                         xid, 0, 0x8000,          # transaction ID, seconds, BROADCAST flag
                         b"\0" * 4, b"\0" * 4, b"\0" * 4, b"\0" * 4,   # ciaddr yiaddr siaddr giaddr
                         chaddr, b"\0" * 64, b"\0" * 128)
    opts = bytes([53, 1, msg_type]) + extra + bytes([55, 3, 1, 3, 6]) + b"\xff"  # 55 = ask for mask, router, DNS
    return header + MAGIC + opts


def parse(data):
    xid = struct.unpack("!I", data[4:8])[0]
    yiaddr = socket.inet_ntoa(data[16:20])
    opts, i = {}, 240
    while i < len(data) and data[i] != 255:
        if data[i] == 0:
            i += 1
            continue
        code, length = data[i], data[i + 1]
        opts[code] = data[i + 2:i + 2 + length]
        i += 2 + length
    return xid, yiaddr, opts


def show(direction, kind, details):
    print(f"{direction} {kind:<9} {details}")


def wait_for(sock, xid, wanted):
    while True:
        try:
            data, (src, _port) = sock.recvfrom(1500)
        except socket.timeout:
            return None
        rxid, yiaddr, opts = parse(data)
        if rxid == xid and opts.get(53, b"\0")[0] in wanted:
            return src, yiaddr, opts


def main():
    ifname = sys.argv[1]
    mac = sys.argv[2] if len(sys.argv) > 2 else mac_of(ifname)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, ifname.encode())
    s.bind(("0.0.0.0", 68))
    s.settimeout(10)
    xid = random.getrandbits(32)

    # D - the client has no address, so it broadcasts from 0.0.0.0 to 255.255.255.255
    s.sendto(build(1, xid, mac), ("255.255.255.255", 67))
    show("->", "DISCOVER", f"from 0.0.0.0 (MAC {mac}) to 255.255.255.255, xid {xid:#010x}")
    got = wait_for(s, xid, {2})
    if got is None:
        show("  ", "(none)", "no OFFER within 10 seconds: no DHCP server reachable, or the pool is full")
        return
    src, offered, opts = got
    server_id = opts[54]
    show("<-", "OFFER", f"from {src}: address {offered}, mask {socket.inet_ntoa(opts[1])}, "
                        f"router {socket.inet_ntoa(opts[3])}, lease {struct.unpack('!I', opts[51])[0]} s")

    # R - still no address: broadcast, naming the chosen server (option 54) and address (option 50)
    extra = bytes([50, 4]) + socket.inet_aton(offered) + bytes([54, 4]) + server_id
    s.sendto(build(3, xid, mac, extra), ("255.255.255.255", 67))
    show("->", "REQUEST", f"broadcast: 'I accept {offered} from server {socket.inet_ntoa(server_id)}'")

    # A - the server confirms (ACK) or refuses (NAK)
    got = wait_for(s, xid, {5, 6})
    if got is None:
        show("  ", "(none)", "no ACK received")
        return
    src, yiaddr, opts = got
    show("<-", MSG[opts[53][0]], f"from {src}: lease confirmed for {yiaddr}" if opts[53][0] == 5 else "request refused")


if __name__ == "__main__":
    main()
```

2. On a test LAN with a DHCP server, run `sudo python3 dora_client.py eth0`. *What it does:* broadcasts a Discover, waits for an Offer, sends a Request and waits for an Ack. It prints each step but does **not** change the interface's address. Actual output on the kiosk build (Verified):

```text
-> DISCOVER  from 0.0.0.0 (MAC ea:aa:8e:8c:d1:0a) to 255.255.255.255, xid 0x1e18afc4
<- OFFER     from 172.20.5.1: address 172.20.5.107, mask 255.255.255.0, router 172.20.5.1, lease 3600 s
-> REQUEST   broadcast: 'I accept 172.20.5.107 from server 172.20.5.1'
<- ACK       from 172.20.5.1: lease confirmed for 172.20.5.107
```

3. Run it with a made-up MAC address (`sudo python3 dora_client.py eth0 02:00:00:00:00:01`). Does the server offer a different address?
4. Read `build()`: which bytes make it a **Discover** rather than a **Request**?

**Expected result:** a full DORA exchange; a different address for a different MAC (Verified).

- **Hint 1:** Option 53 holds the message type: 1 = Discover, 3 = Request.
- **Hint 2:** The flags value `0x8000` asks the server to broadcast its replies.

---

### Task 13 — Tell service failures apart

**Goal:** distinguish OPEN, REFUSED and TIMEOUT on your own computer.

**Skill you gain:** you can test whether a service port is reachable and read what a failure means. This is a daily task in support, operations and security work.

1. Save `port_check.py`:

```python
# port_check.py - is a TCP service reachable? Tells apart three different failures.
# A ping only proves the host answers ICMP. A service needs its port to accept a TCP connection.
#   OPEN     - the three-way handshake completed: something is listening on that port
#   REFUSED  - the host answered at once with a reset (RST): the host is up but nothing listens
#   TIMEOUT  - no answer at all: no path to the host, the host is down, or a firewall drops it
#
# Usage: python port_check.py 172.20.5.10 80
#        python port_check.py 127.0.0.1 8000

import socket
import sys
import time


def check(host, port, timeout=3.0):
    start = time.monotonic()
    try:
        with socket.create_connection((host, port), timeout=timeout):
            result = "OPEN"
    except ConnectionRefusedError:
        result = "REFUSED"
    except (socket.timeout, TimeoutError):
        result = "TIMEOUT"
    except OSError as e:                 # e.g. "No route to host", "Network is unreachable"
        result = f"UNREACHABLE ({e.strerror})"
    return result, (time.monotonic() - start) * 1000


MEANING = {
    "OPEN": "service is listening: test the page itself next",
    "REFUSED": "host reached, but no service on this port: check the service is ON and the port/URL",
    "TIMEOUT": "no reply: check the path first (gateway, VLAN, link), then any firewall",
}

if __name__ == "__main__":
    host, port = sys.argv[1], int(sys.argv[2])
    result, ms = check(host, port)
    meaning = MEANING.get(result.split()[0], "no path to the host: check address, gateway, link and VLAN")
    print(f"{host}:{port}  {result}  after {ms:.0f} ms  -> {meaning}")
```

2. In one Command Prompt window, start a small web server **on your own computer only**: `python -m http.server 8000 --bind 127.0.0.1`. *What it does:* serves the files in the current folder at `http://127.0.0.1:8000`. It is reachable only from your own computer. Stop it later with **Ctrl+C**.
3. In a second window: `python port_check.py 127.0.0.1 8000`.
4. Stop the server with Ctrl+C and run the check again.
5. **PowerShell alternative** (Expected): `Test-NetConnection 127.0.0.1 -Port 8000`. Compare `TcpTestSucceeded` with your script's result.

Actual output on Linux (Verified):

```text
127.0.0.1:8000  OPEN  after 4 ms  -> service is listening: test the page itself next
127.0.0.1:8000  REFUSED  after 5 ms  -> host reached, but no service on this port: check the service is ON and the port/URL
```

The same tool on the kiosk network, covering every failure type (Verified):

```text
# HTTP service on
172.20.5.10:80  OPEN  after 3 ms  -> service is listening: test the page itself next
# HTTP service switched off (server still on the network)
172.20.5.10:80  REFUSED  after 5 ms  -> host reached, but no service on this port: check the service is ON and the port/URL
# wrong port in the URL
172.20.5.10:8080  REFUSED  after 5 ms  -> host reached, but no service on this port: check the service is ON and the port/URL
# server's cable unplugged
172.20.5.10:80  TIMEOUT  after 3008 ms  -> no reply: check the path first (gateway, VLAN, link), then any firewall
# remote address with no route from PC1 (another network, no gateway set)
10.99.0.5:80  UNREACHABLE (Network is unreachable)  after 7 ms  -> no path to the host: check address, gateway, link and VLAN
# repaired, retested
172.20.5.10:80  OPEN  after 4 ms  -> service is listening: test the page itself next
```

**Expected result:** OPEN while the server runs; REFUSED after it stops.

- **Hint 1:** REFUSED comes back instantly; TIMEOUT takes the full 3 seconds.
- **Hint 2:** Only test your own computer or networks you are permitted to test.

---

### Task 14 — Read your own DHCP lease

**Goal:** find real DHCP evidence on your own computer.

**Skill you gain:** you can read a client's lease details. This is the first check when a device "has no internet".

On **your own Windows computer** (Expected; read-only):

1. `ipconfig /all` *(shows the full settings of every adapter)*. For your active adapter, record:
   - **DHCP Enabled**;
   - **IPv4 Address**;
   - **Subnet Mask**;
   - **Default Gateway**;
   - **DHCP Server**;
   - **Lease Obtained** and **Lease Expires**.
2. Work out the lease length.
3. Is your DHCP server the same device as your gateway? (At home it usually is: the router.)
4. Answer from the evidence: was this address leased or typed by hand? How do you know?

Do **not** run `ipconfig /release` on your own computer for this task: it disconnects you. The official lab uses `/release` and `/renew` only on simulated PC2.

**Expected result:** a completed table; the lease length in hours.

- **Hint 1:** "DHCP Enabled . . . : No" means a static address.
- **Hint 2:** Lease Expires − Lease Obtained = lease length.

---

### Task 15 — Add a second visitor network with a relay (Packet Tracer)

**Goal:** build slide 8's relay scenario.

**Skill you gain:** you can configure DHCP across a routing boundary with `ip helper-address`, as in most campus and office networks.

Use a **copy** of your Task 17 file (Expected; IOS not run here):

1. Add a second 2960 switch and one PC (**PC4**). Connect the router's **G0/1** to the new switch's Fa0/24, and PC4 to Fa0/1.
2. Router:

   ```text
   configure terminal
   interface g0/1
   ip address 172.20.6.1 255.255.255.0
   no shutdown
   exit
   ip dhcp excluded-address 172.20.6.1 172.20.6.99
   ip dhcp excluded-address 172.20.6.125 172.20.6.254
   ip dhcp pool VISITORS2
   network 172.20.6.0 255.255.255.0
   default-router 172.20.6.1
   end
   ```

   Here the router serves both networks itself, so **no relay is needed**. Set PC4 to DHCP and confirm an address in .100–.124.
3. Now make the **server** the DHCP server for the new network instead:
   - Remove the router's pool: `configure terminal`, `no ip dhcp pool VISITORS2`.
   - On **Service-Server > Services > DHCP**, turn it **On** and create a pool with:
     - default gateway 172.20.6.1;
     - start address 172.20.6.100;
     - mask 255.255.255.0;
     - maximum users 25.
   - Then **Add**. Leave the factory **serverPool** in place, but check that it does not serve the kiosk LAN (see the hint).
4. Renew PC4. Predict, then observe: does it get an address?
5. Router: `interface g0/1`, then `ip helper-address 172.20.5.10`. Renew PC4 again.

**Expected result:**

- Step 2: works (router-served).
- Step 4: fails (169.254, no relay).
- Step 5: PC4 gets 172.20.6.100 or similar from the server.

- **Hint 1:** If the kiosk PCs start getting addresses from the server's serverPool, you have created two competing servers (lecture section 10). Turn serverPool's addressing off, or delete it if your version allows.
- **Hint 2:** Simulation mode with the DHCP filter shows the relayed packets between the router and the server.

---

## Part D — Official tasks and integration (Tasks 16–20)

### Task 16 — Build a visitor information network (Official Task 1)

**Goal:** build the kiosk network with the router as the only DHCP server.

**Official steps**

1. **1.1:** Open Cisco Packet Tracer 9.0. Add:
   - one **1941** router;
   - one **2960-24TT** switch;
   - one **Server-PT**;
   - three **PC-PT** devices.

   Name them **Router**, **Switch**, **Service-Server** and **PC1–PC3** (**Config > Global Settings > Display Name**). With **Copper Straight-Through**, connect:
   - PC1–PC3 **FastEthernet0** → switch **Fa0/1**, **Fa0/2**, **Fa0/3**;
   - Service-Server Fa0 → **Fa0/4**;
   - Router **G0/0** → **Fa0/24**.
2. **1.2:** **Router > CLI**. Answer **no** to the dialog and press Enter again. Type each line, without the prompts:

   ```text
   enable
   configure terminal
   interface g0/0
   ip address 172.20.5.1 255.255.255.0
   no shutdown
   exit
   ip dhcp excluded-address 172.20.5.1 172.20.5.99
   ip dhcp excluded-address 172.20.5.125 172.20.5.254
   ip dhcp pool VISITORS
   network 172.20.5.0 255.255.255.0
   default-router 172.20.5.1
   exit
   end
   show ip interface brief
   show ip route
   show ip dhcp pool
   ```

   **Expected:**
   - G0/0 **up/up** with a connected route for 172.20.5.0/24.
   - **VISITORS** shows **25** available addresses (.100–.124).
   - The excluded ranges protect the gateway, the server and all addresses outside the pool.
   - No relay is needed: the router and the clients share the local network.
   - Wait for green links. Repeat a first ping that loses a reply.
3. **1.3:** **Service-Server > Desktop > IP Configuration > Static**: 172.20.5.10, 255.255.255.0, gateway 172.20.5.1. Leave DNS unused; this activity tests HTTP by numeric IP.
4. **1.4:** **Service-Server > Services > DHCP**: make sure the Service is **Off**. Do not use the built-in **serverPool** or create another pool. The router is the only DHCP server.
5. **1.5:** On each PC: **Desktop > IP Configuration > DHCP**, and wait for "DHCP request successful". Then run `ipconfig`.
   - **Expected:** each PC has a **different** address in .100–.124, mask 255.255.255.0 and gateway 172.20.5.1. A blank, **0.0.0.0** or **169.254.x.x** address is not a valid result.
   - **If it fails:**
     1. Return to Realtime.
     2. Check the green links and Router G0/0.
     3. Run `show ip dhcp pool` and confirm the server's DHCP is still Off.
     4. On the client, choose **Static** then **DHCP** to retry.
   - Then, at `Router#`: `show ip dhcp binding`. You should see one lease per PC.
6. **1.6:** Save as **TW06A_YourStudentID.pkt**. Create **TW06A_YourStudentID.docx** and paste the router's `show ip dhcp pool` / `show ip dhcp binding` output and one PC `ipconfig`.

**Test plan**

| Test | Expected | Actual |
| --- | --- | --- |
| `show ip interface brief` | G0/0 172.20.5.1 up/up | |
| `show ip dhcp pool` | VISITORS, 25 addresses available (before leases) | |
| PC1–PC3 `ipconfig` | Three different addresses in .100–.124, gateway .1 | |
| `show ip dhcp binding` | Three bindings, one per PC MAC | |
| Server DHCP service | Off | |

- **Hint 1:** IOS normally leases the lowest free addresses first (.100, .101, .102) (Expected). The Linux server in the lecture chose differently (Verified); both are inside the pool.
- **Hint 2:** Task 5e and Task 10c cover the competing-server fault.

---

### Task 17 — Add and test the information service (Official Task 2)

**Goal:** publish the page, test it in order, and watch DORA and HTTP in Simulation mode.

**Official steps**

1. **2.1:** **Service-Server > Services > HTTP**: **On**. Select **index.html > Edit** and replace its content with `<html><body><h1>Visitor Information</h1><p>YourStudentID</p></body></html>` (use your own ID). Click **Save**. This page lives in the simulated server.
2. **2.2:** **PC1 > Command Prompt**:
   - `ping 172.20.5.1`: expect replies, which proves the gateway is reachable.
   - `ping 172.20.5.10`: expect replies, which proves local-subnet connectivity to the server.

   If the gateway ping fails, check the client configuration, cable/link and router interface. If the server ping fails, check the client configuration, cable/link and the server's static settings. **Do not change the router configuration to repair a local server-connectivity fault.**
3. **2.3:** **PC1 > Web Browser**: `http://172.20.5.10`, **Go**. Expect "Visitor Information" and your ID. If the ping succeeds but the page fails, check the **HTTP switch**, the saved **index.html** and the URL. Do not alter correct addressing.
4. **2.4:** **Simulation > Edit Filters**:
   1. Clear everything with **Show All/None**.
   2. Select **DHCP**, **ARP**, **TCP** and **HTTP**.
   3. On **PC2 > Command Prompt**, run `ipconfig /release` then `ipconfig /renew`. If either command is unsupported, or no full DHCP exchange appears, use **IP Configuration > Static** then **DHCP** instead.
   4. Click **Capture/Forward** until an address is assigned. Identify the **Discover**, **Offer**, **Request** and **Acknowledge**.
   5. Open **PC2 > Web Browser** at `http://172.20.5.10`, advance the events, and inspect the **TCP/HTTP** events.

   These operations affect only simulated PC2.
5. **2.5:** Capture the filtered event list and the working page, then return to **Realtime**.

**Evidence table** (with a one-line explanation for each, as slide 15 asks)

| Evidence | What it proves | Actual |
| --- | --- | --- |
| PC1 ping 172.20.5.1 | | |
| PC1 ping 172.20.5.10 | | |
| PC1 browser page | | |
| Four DHCP events for PC2 | | |
| TCP SYN, SYN-ACK, ACK and HTTP GET/200 for PC2 | | |

- **Hint 1:** Compare your Simulation events with the real captures in lecture sections 6.2 and 11.
- **Hint 2:** Click an event > **Inbound/Outbound PDU Details** to see the DHCP message type or TCP flags.

---

### Task 18 — Diagnose an HTTP fault (Official Extra Challenge)

**Goal:** prove that a fault is in the service, not the network, and repair only that.

**Official steps**

1. **E.1:** Return to **Realtime**. **File > Save As** `TW06A_Fault_YourStudentID.pkt`. Turn **Service-Server > Services > HTTP > Off**.
   - **PC3 > Command Prompt**: `ping 172.20.5.10`. It should still reply.
   - Open a **fresh** Web Browser request to `http://172.20.5.10/index.html` and click **Go**. Record the failure to obtain a **new** response, not a previously displayed page. Close and reopen the simulated browser if needed.
2. **E.2:** Turn **HTTP > On**. Repeat the same browser request and expect the saved heading and ID. Keep all correct IP settings. Save the repaired file.
3. **E.3:** Capture the failed and successful browser results. Paste both into **TW06A_YourStudentID.docx**, state why changing the gateway would not have been justified, and save.

**What the same fault looks like on a real network (Verified):**

```text
ping 172.20.5.10                -> 2 packets transmitted, 2 received, 0% packet loss
curl http://172.20.5.10/index.html -> curl: (7) Failed to connect to 172.20.5.10 port 80 after 0 ms
port_check.py 172.20.5.10 80    -> REFUSED  (the server answered with a TCP reset)
```

**Fault record**

| Part | Your entry |
| --- | --- |
| Symptom | |
| Evidence (configuration + traffic) | |
| Root cause | |
| Repair (one setting) | |
| Retest + regression (ping still replies) | |
| Why changing the gateway was not justified | |

- **Hint 1:** PC3 and the server are on the **same** subnet. Does PC3 even use its gateway to reach the server?
- **Hint 2:** Lecture section 12.1's table.

---

### Task 19 — Mini-project: a library visitor service

**Goal:** design, build and evidence a small service network from requirements.

**Skill you gain:** you can turn requirements into an address policy, build it and prove it works with evidence that supports each claim.

**Brief.** A library needs:

- a **public** network for up to **40** visitor devices;
- a **staff** network with 8 PCs, a printer and a catalogue web server;
- the catalogue page reachable from **both** networks;
- **one** DHCP server, the router, for both networks;
- in a second version, the DHCP service moved to a server on the staff network.

Steps:

1. **Address policy:** a subnet, gateway and static range for each network, and a pool large enough for its clients. Use `pool_policy.py` to check each pool and the static addresses.
2. **Build** it in Packet Tracer, with the router serving both pools.
3. **Test plan (at least 10 claims)**, following slide 12's order:
   - DHCP leases on both networks;
   - gateway pings;
   - the server by IP from both networks;
   - the service (port 80);
   - the page from both networks.
4. **Version 2:** move DHCP to a server on the staff network. Add `ip helper-address` **only** where it is needed, and justify each one.
5. **Evidence:** for each test plan row, a screenshot with a one-sentence explanation (slide 15).

**Test plan (start)**

| # | Claim | Test | Expected | Actual |
| --- | --- | --- | --- | --- |
| 1 | A public client gets a lease | `ipconfig` + `show ip dhcp binding` | Address in the public pool | |
| 2 | The catalogue service listens | Server HTTP On; browser from a staff PC | Page loads | |
| | | | | |

- **Hint 1:** 40 visitors need a pool of **at least** 40. Leave room to grow.
- **Hint 2:** In version 2, which network's clients are now remote from the DHCP server?

---

### Task 20 — Assessment-style practice: DHCP and services

**This is practice only, not a real exam question.** The module exam is two hours with short-answer and essay-style questions; the report covers data storage and networking (module guide). Check the real AS1 brief on Canvas. Marks are invented for planning.

**Rules:** 25 minutes, closed book, write it yourself.

**(a)** Describe the four messages of the DHCP exchange and explain why the first one is a broadcast. *(4 marks)*

**(b)** A DHCP pool is configured with `network 172.20.5.0 255.255.255.0` and excluded addresses 172.20.5.1–99 and 172.20.5.125–254. State which addresses are handed out and explain why servers should be outside this range. *(4 marks)*

**(c)** Explain when a DHCP relay is needed and what it does. *(4 marks)*

**(d)** Users can ping a web server but cannot load its page. Explain how you would diagnose this using an ordered set of tests, what evidence you would collect, and why changing IP settings would not be justified. *(8 marks; aim for 250–350 words)*

**Self-marking checklist**

| Part | A good answer includes | Expected | Actual |
| --- | --- | --- | --- |
| (a) | D/O/R/A roles; no address yet; does not know the server; Request names the server | 4 points | |
| (b) | .100–.124, 25 addresses; static infrastructure outside to avoid duplicates; predictable addresses | 4 points | |
| (c) | Broadcasts stop at routers; relay forwards as unicast to a remote server; the server picks a pool from the relay address; not needed on the same LAN | 4 points | |
| (d) | Slide 12 order; ping proves the path; check the service is on and listening (refused vs timeout); fresh request; one change; retest + regression; evidence with explanations | 8 points | |
| Time | Within 25 minutes | Yes | |

- **Hint 1:** Use the official Extra Challenge in (d).
- **Hint 2:** Lecture sections 6, 7, 9, 12 and 13.

---

## Tracker

| Task | Name | Done | Notes / score |
| --- | --- | --- | --- |
| 1 | Who sends what, to where? | ☐ | /4 |
| 2 | What does the pool hand out? | ☐ | /5 |
| 3 | Static or dynamic? | ☐ | /6 |
| 4 | Is a relay needed? | ☐ | /5 |
| 5 | Interpret the symptom | ☐ | /6 |
| 6 | Fix the DHCP configuration | ☐ | /5 |
| 7 | Fix the relayed network | ☐ | /5 |
| 8 | Read the real failures | ☐ | /5 |
| 9 | Fix weak evidence | ☐ | /4 |
| 10 | Fix the repairs | ☐ | /5 |
| 11 | `pool_policy.py` | ☐ | |
| 12 | Own DHCP client (optional) | ☐ | |
| 13 | `port_check.py` | ☐ | |
| 14 | Your own DHCP lease | ☐ | |
| 15 | Second network with relay | ☐ | |
| 16 | **Official Task 1**: Visitor network | ☐ | |
| 17 | **Official Task 2**: Information service | ☐ | |
| 18 | **Official Extra Challenge**: HTTP fault | ☐ | |
| 19 | Mini-project: library | ☐ | |
| 20 | Assessment-style practice | ☐ | /20 |

## Reflection

1. In Simulation mode, which DORA message surprised you most, and why?
2. How did you make sure your Extra Challenge screenshot showed a **fresh** failure, not a cached page?
3. Which do you find more useful when a page fails: the ping result or the port check result? Why?
4. Where in a real organisation would a DHCP relay be needed, and what goes wrong if its pool has the wrong gateway?

---

## Answer key

**(Verified)** = real Linux build (dnsmasq, Python 3.13, `tcpdump`, `curl`). **(Expected)** = Packet Tracer, Cisco IOS or Windows; not run here.

### Task 1 (Verified)

| Message | Sent by | Source → destination |
| --- | --- | --- |
| Discover | Client | 0.0.0.0 → 255.255.255.255 |
| Offer | Server | 172.20.5.1 → 255.255.255.255 (broadcast because the client set the flag) |
| Request | Client | 0.0.0.0 → 255.255.255.255, naming the server (option 54) and the address (option 50) |
| Ack | Server | 172.20.5.1 → 255.255.255.255 |

The Request is still broadcast because the client has no confirmed address yet, and because it tells any other server that offered an address that its offer was declined.

### Task 2 (Verified)

**a)** .100–.124 = **25** (254 − 99 − 130).

**b)** 192.168.10.50–.254 = **205** (254 − 49).

**c)** 10.1.1.21–.200 = **180**.

**d)** The /22 has usable hosts 172.16.8.1–172.16.11.254, which is 1022 addresses. The exclusion removes 255 of them, leaving **767**: 172.16.9.0–172.16.11.254. Note that **172.16.9.0 is a valid host** inside a /22.

**e)** /25 → usable .1–.126. Excluding .1 leaves .2–.126 = **125**.

### Task 3

1. Static (the gateway).
2. Static (clients and links point at it).
3. Pool.
4. Static or reservation (staff print to a fixed address).
5. Pool.
6. Reservation or static (it is monitored by IP address).

### Task 4

| | Verdict |
| --- | --- |
| a | Not needed (official) |
| b | Needed |
| c | Not needed |
| d | Needed: the VLANs are separate broadcast domains |
| e | Not needed: DHCP broadcasts never use the gateway. The wrong gateway is a separate fault |

### Task 5

- **a)** DHCP failed. Check the link and VLAN, then the router pool (`show ip dhcp pool`).
- **b)** Local link, VLAN or mask, or the router G0/0 state. Check `ipconfig` and `show ip interface brief`.
- **c)** The service. Is HTTP on? Is the port reachable? Is the URL right?
- **d)** The pool overlaps the server's static address. Check `show running-config` exclusions or run `pool_policy.py`, then `show ip dhcp binding`.
- **e)** A competing DHCP server (Server-PT's **serverPool**). Check Server-PT **Services > DHCP**.
- **f)** The service is off or on another port. Check the server's HTTP switch.

### Task 6 (Verified with `pool_policy.py` for the pool lines)

1. `configure terminal` was typed at `Router>`: `enable` is missing.
2. `no shutdown` is missing on G0/0.
3. The exclusion ends at .9, so the server (.10) is inside the pool.
4. The second exclusion (.125–.254) is missing. The pool hands out 245 addresses instead of 25.
5. `default-router 172.20.6.1` should be **172.20.5.1**.

The corrected session is official step 1.2.

### Task 7 (Verified)

1. Yes. The client on 172.20.6.0/24 received a lease from the remote server, through the relay (the Offer came via 172.20.6.1).
2. The lease's router is **172.20.5.1**, which is not in the client's network. The client cannot reach anything beyond its own LAN.
3. Change the default router option of the **172.20.6.0/24 pool**, on the DHCP server, to 172.20.6.1. After this fix the Offer showed `router 172.20.6.1` (Verified).
4. `ip helper-address 172.20.5.10` on the router interface facing the **clients** (G0/1, 172.20.6.1).
5. The 172.20.5.0/24 clients share a broadcast domain with the server already (slide 8).

### Task 8 (Verified)

1. The pool is exhausted (25/25).
2. Service off: refused at once (0 ms). The host is up.
3. No path: the request waited about 3 s with no answer (the server's link was down).
4. A SYN answered by a reset `[R.]`: the host is up, but nothing listens on port 80.
5. No relay: the Discover broadcast stopped at the router.

Evidences 2 and 3 are told apart by the **time taken** and by **ping**: the instant refusal comes with a working ping.

### Task 9

Model captions:

1. "PC2 `ipconfig` shows 172.20.5.101 and the router's `show ip dhcp binding` lists PC2's MAC with 172.20.5.101, so the address was leased by the router, not typed by hand."
2. "With HTTP Off, PC3's fresh browser request (browser reopened) fails, while `ping 172.20.5.10` replies: the path works, and the service does not."
3. "After HTTP On, the same request returns the page with my ID, and the server ping still replies (regression check)."
4. "PC2's DHCP events, each selected: Discover (0.0.0.0 → 255.255.255.255), Offer from 172.20.5.1, Request, Ack."

### Task 10

| | Justified? | Why |
| --- | --- | --- |
| a | No | The server is local and the fault is HTTP. Turn HTTP On |
| b | No | It hides a link fault and the address is outside the design. Fix the link, then renew DHCP |
| c | Yes | It removes the competing server |
| d | No | DHCP is not involved: the client has an address and its gateway works. Check the server's settings and link |
| e | Yes | It removes the duplicate static address |

### Task 11 (Verified)

The answers are as in Tasks 2 and 6. Step 5 model:

```python
def enough(usable, needed):
    return [] if len(usable) >= needed else [f"pool has {len(usable)} addresses, {needed} needed"]
```

### Task 12 (Verified on Linux)

The output is as shown. A different MAC address was given a different address. Each of the four messages takes its type from the byte after `53, 1`.

### Task 13 (Verified on Linux; PowerShell Expected)

OPEN, then REFUSED. `Test-NetConnection` shows `TcpTestSucceeded : True`, then `False`.

### Task 14 (Expected)

The values are your own. A home router usually acts as both gateway and DHCP server.

### Task 15 (Expected; matching Linux relay results Verified)

- Step 2: PC4 gets a lease from the router.
- Step 4: 169.254 (no relay).
- Step 5: a lease from the server via `ip helper-address`.

### Tasks 16–18 (Expected)

Use the test plans. Task 18: PC3 reaches the server **directly** on the same subnet without using its gateway, so the gateway cannot be the cause. Ping proves the path, and the refused or failed page proves the service.

### Tasks 19–20 (model points)

Use the self-marking checklist and lecture sections 6–9 and 11–16.
