# Lab 7 — TCP/IP, Addressing and Subnetting Hands-on Workbook (20 Tasks)

**Module:** 4301COMP Computer Systems Architecture

**Session:** Teaching Week 04, Session A · **Matching lecture:** `../Lectures/Lecture-07-TCP-IP-Addressing-and-Subnetting.md`

---

## How to use this lab

**What this lab is for.** You will connect two networks with a router in Packet Tracer, work out addresses in binary, see how a router chooses a route, watch TCP and UDP exchanges, find listening ports on your own PC, and practise diagnosing gateway problems.

**Where the official tasks are.**

| Official lab sheet (TW04 Session A) | This workbook |
| --- | --- |
| Task 1 — Build and configure two /24 IPv4 networks | Task 16 |
| Task 2 — Interpret the IPv4 addressing | Task 17 |

The official sheet has no Extra Challenge this week. Task 18 is a **supplementary** test of the routed network you build.

**Official rule for this week:** in Packet Tracer, configure everything through the **graphical interface (GUI)**: **do not use the Router CLI**.

In the timetabled lab, **do Tasks 16–17 first**.

**Tools**

| Tool | Used in | Notes |
| --- | --- | --- |
| Cisco Packet Tracer 9.0 | Tasks 10, 14, 16–19 | Named on the official sheet; Logical workspace; GUI only |
| Microsoft Word | Task 17 | For `TW04A_YourStudentID.docx` |
| Command Prompt on your own Windows PC | Task 13 | Read-only commands |
| Python 3 | Tasks 11, 12, 15 | **Optional, your choice.** Built-in modules only |

**Rules:** predict before you check; show binary working where asked; use hints only after a real attempt; record what you actually see.

**Labels:** **Verified** = run or calculated before being written here (Linux, Python 3.13, `tcpdump`). **Expected** = not run here (Packet Tracer and Windows).

---

## Part A — Warm-up: recognise and predict (Tasks 1–5)

### Task 1 — Which layer, which protocol?

**Goal:** place protocols in the TCP/IP model.

Give the TCP/IP layer (Application, Transport, Internet, Link) for each:

| HTTP | TCP | IPv4 | Ethernet | DNS | UDP | ICMP (ping) | SSH | Wi-Fi | SMTP | IPv6 | HTTPS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | | | | | |

**Expected result:** 5 Application, 2 Transport, 3 Internet, 2 Link.

- **Hint 1:** Slide 6 lists examples for each layer.
- **Hint 2:** ping uses ICMP, which slide 6 places beside IPv4.

---

### Task 2 — TCP or UDP?

**Goal:** choose the right transport for each application, with a reason.

1. Downloading a 2 GB game update.
2. A live football stream.
3. A DNS lookup for `www.ljmu.ac.uk`.
4. Submitting coursework to Canvas.
5. A multiplayer shooter sending player positions 60 times a second.
6. Sending an email.

**Expected result:** 3 TCP, 3 UDP, each with "correctness" or "timeliness" in the reason.

- **Hint 1:** Slide 11: TCP when correctness matters; UDP when timeliness and low overhead matter.
- **Hint 2:** A late player position is useless; a missing byte in a game update breaks it.

---

### Task 3 — Port numbers

**Goal:** recall the well-known ports on slide 12.

| Service | Port | Transport |
| --- | --- | --- |
| SSH | | |
| HTTPS | | |
| DNS | | |
| Telnet | | |
| HTTP | | |
| SMTP (server to server) | | |
| SMTP submission | | |
| FTP | | |

Then: which of these services sends passwords in **plain text** and should not be used on untrusted networks?

**Expected result:** eight ports; Telnet (and FTP and plain HTTP are also unencrypted).

- **Hint 1:** The "secure" ones are 22 and 443.
- **Hint 2:** DNS is the only one listed with two transports.

---

### Task 4 — Binary drill

**Goal:** convert between decimal, binary, masks and prefixes by hand.

Use the place values 128 64 32 16 8 4 2 1.

| # | Convert | Answer |
| --- | --- | --- |
| a | 192 → binary | |
| b | 70 → binary | |
| c | 10 → binary | |
| d | 255 → binary | |
| e | `00010100` → decimal | |
| f | `11000000` → decimal | |
| g | 255.255.255.0 → prefix | |
| h | /26 → mask | |
| i | /16 → mask | |
| j | 255.255.255.128 → prefix | |

**Expected result:** all ten match the answer key (Verified with Python).

- **Hint 1:** Count the 1-bits in a mask to get the prefix.
- **Hint 2:** /26 = 24 + 2, so the last octet is `11000000`.

---

### Task 5 — Network, broadcast, hosts

**Goal:** work out the key addresses for a network.

| Address/prefix | Network address | Broadcast address | First host | Last host | Usable hosts |
| --- | --- | --- | --- | --- | --- |
| 10.70.10.11/24 | | | | | |
| 10.70.20.12/24 | | | | | |
| 192.168.20.34/24 | | | | | |
| 172.20.5.5/16 | | | | | |
| 10.70.10.200/26 | | | | | |

**Expected result:** matches `ipv4_tool.py` (Task 11), Verified.

- **Hint 1:** Network = host bits 0; broadcast = host bits 1.
- **Hint 2:** /26 blocks start at .0, .64, .128, .192.

---

## Part B — Find and fix (Tasks 6–10)

### Task 6 — Fix the handshake description

**Goal:** correct a wrong account of the TCP handshake.

Sam Archer wrote:

> "TCP starts with the server sending SYN to the client. The client replies with ACK, and the server finishes with SYN-ACK. The first message also carries the data. Sequence numbers are always zero at the start. UDP uses the same handshake but faster."

Find **five** errors and rewrite the paragraph.

**Expected result:** a correct paragraph matching slide 10.

- **Hint 1:** Who starts a connection: client or server?
- **Hint 2:** In the Verified capture (lecture section 9.2), the client's first sequence number was 2895998211.

---

### Task 7 — Read the real capture

**Goal:** interpret a real `tcpdump` capture line by line.

Real capture from the checking machine (Verified, times and options removed):

```text
127.0.0.1.57924 > 127.0.0.1.5050: Flags [S],  seq 2895998211, length 0
127.0.0.1.5050 > 127.0.0.1.57924: Flags [S.], seq 1942035680, ack 2895998212, length 0
127.0.0.1.57924 > 127.0.0.1.5050: Flags [.],  ack 1942035681, length 0
127.0.0.1.57924 > 127.0.0.1.5050: Flags [P.], seq 2895998212:2895998215, ack 1942035681, length 3
```

1. Which port is the server and which is the client's ephemeral port? How can you tell?
2. Label the three handshake packets.
3. Show the arithmetic that proves each `ack` value is correct.
4. How many bytes of data does packet 4 carry? Show it from the sequence numbers.
5. If the third packet were never sent (a "half-open" connection), what attack would that resemble?

**Expected result:** answers consistent with lecture section 9.2.

- **Hint 1:** The side that sends the first SYN is the client.
- **Hint 2:** 2895998215 − 2895998212 = ?

---

### Task 8 — Fix the gateway mistakes

**Goal:** find wrong default-gateway settings and predict their effect.

The network is the official Lab 7 network (router Gi0/0 = 10.70.10.1, Gi0/1 = 10.70.20.1). Sam configured:

| PC | IP / mask | Default gateway |
| --- | --- | --- |
| PC1 | 10.70.10.11 /24 | 10.70.20.1 |
| PC2 | 10.70.10.12 /24 | 10.70.10.12 |
| PC3 | 10.70.20.11 /24 | 10.70.20.1 |
| PC4 | 10.70.20.12 /24 | (blank) |

1. Which three gateway settings are wrong, and why?
2. Predict: PC1 → PC2? PC1 → PC3? PC3 → PC4? PC3 → PC1? PC4 → PC1?
3. Fix the table.

**Expected result:** three faulty rows; only same-network pings work until they are fixed (Expected in Packet Tracer; reasoning from lecture section 17).

- **Hint 1:** A gateway must be an address **on the PC's own network**, and it must be the **router's** address, not the PC's own.
- **Hint 2:** Even if a request gets through, the **reply** needs the other PC's gateway.

---

### Task 9 — Fix the addressing claims

**Goal:** correct common CIDR, class and NAT misunderstandings.

Each statement is false. Correct it.

1. "10.70.10.0/24 is a class A network, so its mask must be 255.0.0.0."
2. "172.32.1.1 is a private address."
3. "NAT is a firewall, so a home network behind NAT is fully protected."
4. "A router uses the first route in its table that matches."
5. "When a packet crosses a router, its destination IP address changes to the router's address."
6. "A /26 network has 64 usable hosts."

**Expected result:** six corrections with slide references.

- **Hint 1:** Slides 16, 17, 18 and 19.
- **Hint 2:** 2⁶ − 2 = ?

---

### Task 10 — The ping that only works one way

**Goal:** diagnose a classic routed-network fault.

Start from your working Task 16 file (use a **copy**). On **PC3**, delete the default gateway (leave it blank).

1. Predict: will PC1 → PC3 work? Will PC1 → PC2 still work? Will PC3 → PC4 work?
2. Test all three and record the results.
3. Use Packet Tracer **Simulation** mode (filter: ICMP) to watch PC1 → PC3. Where does the packet journey stop?
4. Explain why "PC1 can't reach PC3" is really "PC3 can't reply to PC1".
5. Restore PC3's gateway and re-test.

**Expected result:** PC1 → PC3 fails; same-network pings still work. In Simulation mode, the echo request reaches PC3 but PC3 has no route back (Expected).

- **Hint 1:** PC3 receives the request from 10.70.10.11. Is that on PC3's network?
- **Hint 2:** Without a gateway, PC3 has nowhere to send non-local replies.

---

## Part C — Build (Tasks 11–15)

### Task 11 — An IPv4 calculator that shows its working

**Goal:** check Tasks 4 and 5 with a tool that prints the binary.

**Skill you gain:** you can calculate and explain any IPv4 network's addresses in binary, a core skill for configuring networks and firewall rules.

1. Save as `ipv4_tool.py`:

```python
# ipv4_tool.py - explain an IPv4 address and prefix, showing the binary.
# Uses only Python's built-in ipaddress module.
# Usage: python ipv4_tool.py 10.70.10.11/24

import ipaddress
import sys


def dotted_binary(address):
    """192.168.1.10 -> 11000000.10101000.00000001.00001010"""
    return ".".join(format(int(octet), "08b") for octet in str(address).split("."))


def historical_class(address):
    first = int(str(address).split(".")[0])
    if first == 127:
        return "loopback (not a class)"
    if first < 128:
        return "A"
    if first < 192:
        return "B"
    if first < 224:
        return "C"
    if first < 240:
        return "D (multicast)"
    return "E (reserved)"


def explain(text):
    iface = ipaddress.ip_interface(text)
    net = iface.network
    hosts = net.num_addresses - 2 if net.prefixlen <= 30 else 0
    first_host = net.network_address + 1
    last_host = net.broadcast_address - 1
    print(f"Address        {str(iface.ip):<16} {dotted_binary(iface.ip)}")
    print(f"Mask (/{net.prefixlen:<2})     {str(net.netmask):<16} {dotted_binary(net.netmask)}")
    print(f"Network        {str(net.network_address):<16} {dotted_binary(net.network_address)}")
    print(f"Broadcast      {str(net.broadcast_address):<16} {dotted_binary(net.broadcast_address)}")
    print(f"Host range     {first_host} - {last_host}  ({hosts:,} usable hosts)")
    print(f"Private?       {'yes' if iface.ip.is_private else 'no'}")
    print(f"Old class      {historical_class(iface.ip)} (historical only; CIDR is used today)")


if __name__ == "__main__":
    for arg in (sys.argv[1:] or ["10.70.10.11/24"]):
        explain(arg)
        print()
```

2. Run `python ipv4_tool.py 10.70.10.11/24 10.70.20.12/24 192.168.20.34/24`. *What it does:* prints calculations only. Actual output (Verified):

```text
Address        10.70.10.11      00001010.01000110.00001010.00001011
Mask (/24)     255.255.255.0    11111111.11111111.11111111.00000000
Network        10.70.10.0       00001010.01000110.00001010.00000000
Broadcast      10.70.10.255     00001010.01000110.00001010.11111111
Host range     10.70.10.1 - 10.70.10.254  (254 usable hosts)
Private?       yes
Old class      A (historical only; CIDR is used today)

Address        10.70.20.12      00001010.01000110.00010100.00001100
Mask (/24)     255.255.255.0    11111111.11111111.11111111.00000000
Network        10.70.20.0       00001010.01000110.00010100.00000000
Broadcast      10.70.20.255     00001010.01000110.00010100.11111111
Host range     10.70.20.1 - 10.70.20.254  (254 usable hosts)
Private?       yes
Old class      A (historical only; CIDR is used today)

Address        192.168.20.34    11000000.10101000.00010100.00100010
Mask (/24)     255.255.255.0    11111111.11111111.11111111.00000000
Network        192.168.20.0     11000000.10101000.00010100.00000000
Broadcast      192.168.20.255   11000000.10101000.00010100.11111111
Host range     192.168.20.1 - 192.168.20.254  (254 usable hosts)
Private?       yes
Old class      C (historical only; CIDR is used today)
```

3. Run it for every row of Task 5 and check your answers.
4. **Extend:** add a line that prints the **wildcard mask** (the mask with every bit flipped, e.g. 0.0.0.255 for /24). Firewall and router rules often use it. Hint: `net.hostmask`.

**Expected result:** your Task 5 answers match; the /24 wildcard mask is `0.0.0.255` (Verified).

- **Hint 1:** Run it with several arguments at once.
- **Hint 2:** `print(f"Wildcard       {net.hostmask}")` inside `explain`.

---

### Task 12 — How a router chooses: longest-prefix match

**Goal:** model the "most specific matching route" rule from slide 16.

**Skill you gain:** you can predict which route a router or firewall rule will apply to a given address.

1. Save as `route_lookup.py`:

```python
# route_lookup.py - how a router (or a PC) chooses where to send a packet.
# Rule (slide 16): of all the routes that MATCH the destination, choose the
# MOST SPECIFIC one, i.e. the one with the longest prefix.
# 0.0.0.0/0 matches everything, so it is the "default route" (default gateway).
#
# Usage: python route_lookup.py

import ipaddress

ROUTES = [  # (destination prefix, where to send it)
    ("10.70.10.0/24", "deliver directly on GigabitEthernet0/0"),
    ("10.70.20.0/24", "deliver directly on GigabitEthernet0/1"),
    ("10.70.0.0/16",  "send to router 10.70.99.2"),
    ("0.0.0.0/0",     "default route: send to ISP 203.0.113.1"),
]


def lookup(destination):
    dest = ipaddress.ip_address(destination)
    matches = [(ipaddress.ip_network(prefix), action) for prefix, action in ROUTES
               if dest in ipaddress.ip_network(prefix)]
    best = max(matches, key=lambda m: m[0].prefixlen)   # longest prefix wins
    return [str(m[0]) for m in matches], best


if __name__ == "__main__":
    for d in ["10.70.20.12", "10.70.10.11", "10.70.55.5", "8.8.8.8"]:
        matched, (net, action) = lookup(d)
        print(f"{d:<12} matches {', '.join(matched):<45} -> /{net.prefixlen}: {action}")
```

2. Run it. Actual output (Verified):

```text
10.70.20.12  matches 10.70.20.0/24, 10.70.0.0/16, 0.0.0.0/0        -> /24: deliver directly on GigabitEthernet0/1
10.70.10.11  matches 10.70.10.0/24, 10.70.0.0/16, 0.0.0.0/0        -> /24: deliver directly on GigabitEthernet0/0
10.70.55.5   matches 10.70.0.0/16, 0.0.0.0/0                       -> /16: send to router 10.70.99.2
8.8.8.8      matches 0.0.0.0/0                                     -> /0: default route: send to ISP 203.0.113.1
```

3. Before running each, predict which route these destinations use: `10.70.20.200`, `10.71.0.1`, `10.70.99.2`.
4. **Extend:** add a route `("10.70.20.128/25", "send to firewall 10.70.20.254")`. Which of `10.70.20.12` and `10.70.20.200` now change route, and why?

**Expected result:** step 3: /24 via Gi0/1; default route; /16 router. Step 4: only 10.70.20.200 changes (it is in .128–.255) (Verified).

- **Hint 1:** List every route that matches, then pick the longest prefix.
- **Hint 2:** 10.71.0.1 is not inside 10.70.0.0/16.

---

### Task 13 — Find the listening ports on your own PC

**Goal:** see which programs on your computer are waiting for network connections.

**Skill you gain:** you can list open ports and link each one to the process (PID) that opened it, a standard step in a security check.

On your own Windows PC (Expected; read-only):

1. Command Prompt: `netstat -ano | findstr LISTENING`. *What it does:* lists every TCP port in the LISTENING state, with the owning PID.
2. Pick three lines. For each, note the **local address and port** and the **PID**.
3. Find each PID in Task Manager > Details (or `tasklist /FI "PID eq <PID>"`). Which program is it?
4. Which ports listen on `0.0.0.0` (every interface) and which only on `127.0.0.1` (this PC only)? Why does that difference matter for security?
5. Run `netstat -ano | findstr ESTABLISHED` while a web page is loading. What remote port do most connections use?

**Linux comparison (Verified):** while a test server was listening, `ss -tln` showed `LISTEN 0 128 127.0.0.1:5050 0.0.0.0:*`.

**Expected result:** a table of three ports, their PIDs and programs; most established web connections go to remote port 443 (Expected).

- **Hint 1:** Port 135 and 445 belong to Windows services; that is normal on Windows.
- **Hint 2:** `127.0.0.1` listeners cannot be reached from other computers.

---

### Task 14 — Watch a TCP handshake in Packet Tracer

**Goal:** see SYN, SYN-ACK and ACK in Simulation mode.

**Skill you gain:** you can identify a TCP handshake in a packet capture, the starting point for analysing any connection.

Use a **copy** of your Task 16 network (Expected; Packet Tracer was not run here):

1. Add a **Server-PT** to **Switch-B**. Give it 10.70.20.100 /24, gateway 10.70.20.1. In **Services > HTTP**, make sure HTTP is **On**.
2. Switch to **Simulation** mode. **Edit Filters**: tick only **TCP** and **HTTP**.
3. On **PC1**, open **Desktop > Web Browser**, type `10.70.20.100`, click **Go**.
4. Step through with **Capture/Forward**. Click each TCP event and, in **PDU Information**, find the TCP **flags** and the source and destination **ports**.
5. Record the first three TCP packets:

| # | From → To | Flags | Source port | Destination port |
| --- | --- | --- | --- | --- |
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

6. Compare with the Verified Linux capture in Task 7. What is the same, and what is different?

**Expected result:** SYN (PC1 → server, destination port 80), SYN+ACK (server → PC1), ACK (PC1 → server), then HTTP.

- **Hint 1:** The server's port is 80 for HTTP.
- **Hint 2:** PC1's source port will be a large ephemeral number.

---

### Task 15 — The same exchange over TCP and UDP

**Goal:** run a tiny TCP and UDP client/server on your own PC and see the difference.

**Skill you gain:** you can write and run a minimal network client and server, and check its listening port with `netstat`.

1. Save as `tcp_udp_demo.py`:

```python
# tcp_udp_demo.py - the same tiny exchange over TCP and over UDP, on your own
# computer only (127.0.0.1, the loopback address). Nothing leaves your PC.
#
# Usage:  python tcp_udp_demo.py           run both demos
#         python tcp_udp_demo.py hold      also keep a TCP server listening on
#                                          port 5050 for 30 s, so you can find
#                                          it with:  netstat -ano | findstr 5050

import socket
import sys
import threading
import time

HOST = "127.0.0.1"


def tcp_demo(port=5050):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # TCP
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, port))
    server.listen(1)                                              # wait for a SYN

    def serve():
        conn, addr = server.accept()      # handshake has completed here
        data = conn.recv(1024)
        conn.sendall(b"HELLO " + data)
        conn.close()                      # FIN

    t = threading.Thread(target=serve)
    t.start()
    client = socket.create_connection((HOST, port))   # sends SYN, gets SYN-ACK, sends ACK
    client.sendall(b"Sam")
    reply = client.recv(1024)
    my_port = client.getsockname()[1]
    client.close()
    t.join()
    server.close()
    print(f"TCP: client used ephemeral port {my_port}, server port {port}, reply {reply!r}")


def udp_demo(port=5051):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     # UDP: no listen/accept
    server.bind((HOST, port))
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client.sendto(b"Sam", (HOST, port))                          # no handshake at all
    data, addr = server.recvfrom(1024)
    server.sendto(b"HELLO " + data, addr)
    reply, _ = client.recvfrom(1024)
    print(f"UDP: client used ephemeral port {addr[1]}, server port {port}, reply {reply!r}")
    client.close()
    server.close()


def hold(port=5050, seconds=30):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, port))
    server.listen(1)
    print(f"Listening on {HOST}:{port} for {seconds} s. Look for it with netstat now.", flush=True)
    time.sleep(seconds)
    server.close()


if __name__ == "__main__":
    tcp_demo()
    udp_demo()
    if len(sys.argv) > 1 and sys.argv[1] == "hold":
        hold()
```

2. Run `python tcp_udp_demo.py`. *What it does:* opens connections **only to your own computer** (127.0.0.1); nothing leaves your PC. Actual output (Verified, port numbers hidden):

```text
TCP: client used ephemeral port <n>, server port 5050, reply b'HELLO Sam'
UDP: client used ephemeral port <n>, server port 5051, reply b'HELLO Sam'
```

3. Run `python tcp_udp_demo.py hold`, and **while it waits**, run `netstat -ano | findstr 5050` in another window. Record the line. Whose PID is it?
4. In the code, find the lines that correspond to: listening for a SYN; completing the handshake; sending a FIN. Why does the UDP part have no equivalent lines?
5. Compare with the Verified captures in lecture sections 9.2 and 10.2: 10 packets for TCP, 2 for UDP.

**Expected result:** two "HELLO Sam" replies; in step 3, a LISTENING line for `127.0.0.1:5050` whose PID is your `python.exe` (Expected on Windows).

- **Hint 1:** `listen()`, `accept()` and `create_connection()` are where the handshake happens.
- **Hint 2:** UDP has no connection, so there is nothing to set up or close.

---

## Part D — Official tasks and integration (Tasks 16–20)

### Task 16 — Build and configure two /24 IPv4 networks (Official Task 1)

**Goal:** connect two networks with a router, using the GUI only.

**Skill you gain:** you can build a routed network in Packet Tracer and configure router interfaces and PC gateways.

**Official steps** (Logical workspace; GUI only; **do not use the Router CLI**)

1. Add one **2911** router, two **2960-24TT** switches and four **PC-PT** devices. Name them **Router**, **Switch-A**, **Switch-B** and **PC1–PC4**.
2. Using **Copper Straight-Through** cables, connect **PC1** and **PC2** to **Switch-A**, **PC3** and **PC4** to **Switch-B**, **Switch-A** to **Router GigabitEthernet0/0**, and **Switch-B** to **Router GigabitEthernet0/1**.
3. Use **10.70.10.0/24** for the first network and **10.70.20.0/24** for the second. A /24 mask is **255.255.255.0**.
4. Configure each PC (**Desktop > IP Configuration > Static**):

   | PC | IP address | Subnet mask | Default gateway |
   | --- | --- | --- | --- |
   | PC1 | 10.70.10.11 | 255.255.255.0 | 10.70.10.1 |
   | PC2 | 10.70.10.12 | 255.255.255.0 | 10.70.10.1 |
   | PC3 | 10.70.20.11 | 255.255.255.0 | 10.70.20.1 |
   | PC4 | 10.70.20.12 | 255.255.255.0 | 10.70.20.1 |

5. Configure the router (**Router > Config**): select **GigabitEthernet0/0**, set **Port Status** to **On**, enter **10.70.10.1** / **255.255.255.0**. Then **GigabitEthernet0/1**: **On**, **10.70.20.1** / **255.255.255.0**.
6. Check that the links are **green**. Review each PC's IP address, mask and gateway under **Desktop > IP Configuration**.
7. **File > Save As** > **TW04A_YourStudentID.pkt**.

**Why Port Status On? (Extra):** router interfaces start **administratively down** (switched off) until configured; switch ports and PC ports start on.

**Test plan**

| Check | Expected | Actual |
| --- | --- | --- |
| Devices named as specified | Router, Switch-A, Switch-B, PC1–PC4 | |
| Switch-A → Gi0/0, Switch-B → Gi0/1 | Yes | |
| All links green (router links may take longer) | Yes | |
| Four PCs: address, mask, gateway as in the table | Yes | |
| Router Gi0/0 = 10.70.10.1/24 On; Gi0/1 = 10.70.20.1/24 On | Yes | |
| Saved as `TW04A_<your ID>.pkt` | Yes | |

- **Hint 1:** If a router link stays red, check that Port Status is ticked On.
- **Hint 2:** Hover over the router to see both interface addresses.

---

### Task 17 — Interpret the IPv4 addressing (Official Task 2)

**Goal:** explain the addressing of the network you built.

**Official steps**

1. For **10.70.10.0/24**, write down the **network address**, **broadcast address** and **valid host range**.
2. For **10.70.20.0/24**, the same.
3. Explain why **PC1 and PC2** are on the same local network, while **PC1 and PC3** are on different networks.
4. State the default gateway used by **PC1** and by **PC3**.
5. Explain why a host needs a **default gateway** when the destination is outside its local /24 network.
6. Take one screenshot of the completed topology and one screenshot of the IP Configuration window for one PC on **each** network. Paste them into **TW04A_YourStudentID.docx**.

**Supplementary:** for step 3, include the binary AND working for the third octet (lecture section 13.3).

**Test plan**

| Check | Expected | Actual |
| --- | --- | --- |
| Both networks: network, broadcast, host range | Correct values (see Task 5) | |
| Same/different network explanation uses the prefix | Yes | |
| Gateways stated | 10.70.10.1 and 10.70.20.1 | |
| Gateway explanation mentions routing to other networks and the gateway's MAC | Yes | |
| Three screenshots in the document | Yes | |

- **Hint 1:** Use `ipv4_tool.py` to check your values, but write the reasoning yourself.
- **Hint 2:** Lecture section 17.

---

### Task 18 — Test the routed network (supplementary)

**Goal:** prove traffic crosses the router, and see MAC addresses change at the router (slide 19).

Use your Task 16 network (Expected):

1. From **PC1**, `ping 10.70.10.1` (its gateway), then `ping 10.70.20.11` (PC3).
2. From **PC1**, `tracert 10.70.20.11`. How many hops? What is the first hop's address?
3. **Simulation** mode, filter **ICMP**. Ping PC1 → PC3 again. Click the ICMP packet **before** the router and **after** the router. In each, record the Ethernet **source and destination MAC** and the IP **source and destination**.

| Point | Src MAC | Dst MAC | Src IP | Dst IP |
| --- | --- | --- | --- | --- |
| PC1 → Router | | | | |
| Router → PC3 | | | | |

4. Which addresses changed at the router, and which stayed the same?

**Test plan**

| Test | Expected | Actual |
| --- | --- | --- |
| PC1 → 10.70.10.1 | Replies | |
| PC1 → PC3 | Replies (first may time out during ARP) | |
| tracert PC1 → PC3 | 2 hops: 10.70.10.1, then 10.70.20.11 | |
| MACs change at router, IPs stay the same | Yes | |

- **Hint 1:** The router's Gi0/0 MAC appears as the destination on the first leg and Gi0/1's MAC as the source on the second.
- **Hint 2:** Lecture section 17.2.

---

### Task 19 — Mini-project: an address plan for three departments

**Goal:** design, build and test a small routed network from a brief.

**Skill you gain:** you can produce an IP address plan and prove it works, which is how real networks are designed and documented.

**Brief.** A company has three departments, **Sales (20 PCs)**, **Finance (8 PCs)** and **IT (5 PCs + 1 server)**. Each department needs its own network. Use networks taken from **10.80.0.0/16**, one **/24** per department, and one router with **three** Gigabit interfaces (the 2911 has Gi0/0, Gi0/1 and Gi0/2).

1. **Address plan table:** department, network, mask, gateway (router interface), first and last usable host, broadcast.
2. **Build** a reduced version in Packet Tracer: one router, three switches, **two PCs per department** and the IT server (GUI only).
3. **Test plan:** at least six pings, including every department to every other department, and one `tracert`.
4. **Explain** in 100 words why each department being on its own network is useful for **security**.
5. **Extension:** Finance only needs 8 PCs. Which smaller prefix would still fit them, and how many hosts would it allow?

**Test plan**

| From | To | Expected | Actual |
| --- | --- | --- | --- |
| Sales PC | Finance PC | Replies | |
| Finance PC | IT server | Replies | |
| IT PC | Sales PC | Replies | |
| | | | |

- **Hint 1:** For example Sales 10.80.10.0/24, Finance 10.80.20.0/24, IT 10.80.30.0/24, gateways .1.
- **Hint 2:** For the extension, 2⁴ − 2 = 14 hosts.

---

### Task 20 — Assessment-style practice: TCP/IP and addressing

**This is practice only, not a real exam question.** The module exam is two hours with short-answer and essay-style questions; the report covers data storage and networking (module guide). Check the real AS1 brief on Canvas. Marks are invented for planning.

**Rules:** 25 minutes, closed book, no calculator, write it yourself.

**(a)** Compare TCP and UDP, giving one suitable application for each. *(4 marks)*

**(b)** Describe the TCP three-way handshake. *(3 marks)*

**(c)** For 10.70.20.12/24, give the network address, broadcast address and number of usable hosts, showing the mask in binary. *(4 marks)*

**(d)** PC1 (10.70.10.11/24) sends a packet to PC3 (10.70.20.11/24) through a router. Explain how PC1 decides the destination is remote, what the default gateway does, which addresses in the frame and packet change at the router and which stay the same, and why PC3 also needs a correct gateway. *(9 marks; aim for 250–350 words)*

**Self-marking checklist**

| Part | A good answer includes | Expected | Actual |
| --- | --- | --- | --- |
| (a) | Connection-oriented vs connectionless; reliable/ordered vs no guarantee; overhead; e.g. HTTPS vs live video | 4 points | |
| (b) | SYN with initial sequence number; SYN-ACK with own number and ack; ACK; then data | 3 points | |
| (c) | 10.70.20.0; 10.70.20.255; 254; 11111111.11111111.11111111.00000000 | 4 points | |
| (d) | Mask comparison/AND; gateway on own network; frame to gateway's MAC; IP destination unchanged; router routing table, new frame; MACs change per hop; return path needs PC3's gateway | 9 points | |
| Time | Within 25 minutes | Yes | |

- **Hint 1:** Draw the two networks and the router before writing (d).
- **Hint 2:** Lecture sections 9, 13 and 17.

---

## Tracker

| Task | Name | Done | Notes / score |
| --- | --- | --- | --- |
| 1 | Which layer, which protocol? | ☐ | /12 |
| 2 | TCP or UDP? | ☐ | /6 |
| 3 | Port numbers | ☐ | /9 |
| 4 | Binary drill | ☐ | /10 |
| 5 | Network, broadcast, hosts | ☐ | /25 |
| 6 | Fix the handshake description | ☐ | /5 |
| 7 | Read the real capture | ☐ | /5 |
| 8 | Fix the gateway mistakes | ☐ | |
| 9 | Fix the addressing claims | ☐ | /6 |
| 10 | The ping that only works one way | ☐ | |
| 11 | IPv4 calculator | ☐ | |
| 12 | Longest-prefix match | ☐ | |
| 13 | Listening ports on your PC | ☐ | |
| 14 | TCP handshake in Packet Tracer | ☐ | |
| 15 | TCP and UDP demo | ☐ | |
| 16 | **Official Task 1** — Two /24 networks and a router | ☐ | |
| 17 | **Official Task 2** — Interpret the addressing | ☐ | |
| 18 | Test the routed network (supplementary) | ☐ | |
| 19 | Mini-project: three departments | ☐ | |
| 20 | Assessment-style practice | ☐ | /20 |

## Reflection

1. Before this lab, what did you think the default gateway did? What do you think now?
2. Which programs on your PC were listening on ports, and did any surprise you?
3. Why is it useful that MAC addresses change at each hop but IP addresses do not?
4. Which binary conversion do you still find slow, and how will you practise it?

---

## Answer key

**(Verified)** = calculated with Python 3.13 (`ipaddress`, `ipv4_tool.py`, `route_lookup.py`) or captured with `tcpdump` on the Linux checking machine. **(Expected)** = Packet Tracer or Windows; not run here.

### Task 1

Application: HTTP, DNS, SSH, SMTP, HTTPS. Transport: TCP, UDP. Internet: IPv4, ICMP, IPv6. Link: Ethernet, Wi-Fi.

### Task 2

TCP: 1 (update must be exact), 4 (coursework must arrive complete), 6 (email). UDP: 2 (late video frames are useless), 3 (small, fast query; retried if lost), 5 (latest position matters more than old ones).

### Task 3

SSH 22 TCP · HTTPS 443 TCP · DNS 53 UDP/TCP · Telnet 23 TCP · HTTP 80 TCP · SMTP 25 TCP · SMTP submission 587 TCP · FTP 21 TCP. Plaintext: **Telnet** (also FTP and HTTP are unencrypted).

### Task 4 (Verified)

a `11000000` · b `01000110` · c `00001010` · d `11111111` · e 20 · f 192 · g /24 · h 255.255.255.192 · i 255.255.0.0 · j /25.

### Task 5 (Verified)

| Address/prefix | Network | Broadcast | First host | Last host | Hosts |
| --- | --- | --- | --- | --- | --- |
| 10.70.10.11/24 | 10.70.10.0 | 10.70.10.255 | 10.70.10.1 | 10.70.10.254 | 254 |
| 10.70.20.12/24 | 10.70.20.0 | 10.70.20.255 | 10.70.20.1 | 10.70.20.254 | 254 |
| 192.168.20.34/24 | 192.168.20.0 | 192.168.20.255 | 192.168.20.1 | 192.168.20.254 | 254 |
| 172.20.5.5/16 | 172.20.0.0 | 172.20.255.255 | 172.20.0.1 | 172.20.255.254 | 65,534 |
| 10.70.10.200/26 | 10.70.10.192 | 10.70.10.255 | 10.70.10.193 | 10.70.10.254 | 62 |

### Task 6

Errors: (1) the **client** sends the first SYN, not the server; (2) the server replies **SYN-ACK** (second), (3) and the client finishes with **ACK** (third); (4) the handshake carries **no data**: data follows once it is complete; (5) initial sequence numbers are **not zero** (chosen by each side; e.g. 2895998211 in the capture), and **UDP has no handshake** at all. Corrected: "The client sends SYN with its initial sequence number; the server replies SYN-ACK with its own sequence number and an acknowledgement of the client's number + 1; the client sends ACK of the server's number + 1. Data transfer then begins. UDP is connectionless and has no handshake."

### Task 7 (Verified)

1. Server port **5050**; client ephemeral port **57924**. The client sends the first SYN, and 57924 is a high, temporary number.
2. Packet 1 SYN, packet 2 SYN-ACK, packet 3 ACK.
3. 2895998211 + 1 = **2895998212** (server's ack); 1942035680 + 1 = **1942035681** (client's ack).
4. 2895998215 − 2895998212 = **3** bytes ("Sam"); `length 3` agrees.
5. A **SYN flood** leaves many such half-open connections.

### Task 8

1. PC1's gateway 10.70.20.1 is on the **other** network (it must be 10.70.10.1). PC2's gateway is **its own address** (must be 10.70.10.1). PC4 has **no** gateway (must be 10.70.20.1). PC3 is correct.
2. PC1 → PC2: **works** (same network, no gateway needed). PC1 → PC3: **fails** (PC1 cannot reach a gateway on another network). PC3 → PC4: **works** (same network). PC3 → PC1: the request reaches PC1, but PC1's reply fails because its gateway is wrong, so **fails**. PC4 → PC1: **fails** (PC4 has no gateway). (Reasoning from slide 19; Packet Tracer results Expected.)
3. All gateways: PC1, PC2 → 10.70.10.1; PC3, PC4 → 10.70.20.1.

### Task 9

1. Classes are historical; 10.70.10.0/**24** has mask 255.255.255.0 because CIDR says so (slides 16, 18). 2. 172.16.0.0/12 ends at 172.31.255.255, so 172.32.1.1 is **public** (slide 17). 3. NAT is **not a firewall by itself** (slide 17). 4. Routers choose the **most specific** (longest-prefix) match (slide 16). 5. The IP destination **stays the same**; the **MAC** addresses change (slide 19). 6. /26 has 2⁶ − 2 = **62** usable hosts.

### Task 10 (Expected; reasoning from slide 19)

PC1 → PC3 fails; PC1 → PC2 and PC3 → PC4 still work. In Simulation mode the echo request crosses the router and reaches PC3, but PC3 cannot send the reply: 10.70.10.11 is not on its network and it has no gateway. So the fault is on the **return** path.

### Task 11 (Verified)

Output matches Task 5. Wildcard line: `print(f"Wildcard       {net.hostmask}")` prints `0.0.0.255` for /24 and `0.0.0.63` for /26.

### Task 12 (Verified)

Step 3: `10.70.20.200` → /24 Gi0/1; `10.71.0.1` → default route (not in 10.70.0.0/16); `10.70.99.2` → /16 router. Step 4: after adding `10.70.20.128/25`, only **10.70.20.200** changes to the firewall route, because /25 is more specific than /24 and .200 is in .128–.255; 10.70.20.12 is not inside that /25, so it still uses /24.

### Task 13 (Expected)

Your values. `0.0.0.0` listeners accept connections from any interface (other computers can reach them, firewall permitting); `127.0.0.1` listeners only from this PC. Most established browsing connections use remote port **443** (HTTPS).

### Task 14 (Expected)

1: PC1 → server, SYN, source port (ephemeral, e.g. 1025+), destination port 80. 2: server → PC1, SYN+ACK, 80 → PC1's port. 3: PC1 → server, ACK. Same pattern as the Linux capture; differences: real addresses instead of loopback, port 80 instead of 5050, and Packet Tracer's own numbering of sequence numbers.

### Task 15 (Verified; Windows netstat Expected)

Output: two `b'HELLO Sam'` replies. Handshake lines: `server.listen(1)` (waits for SYN), `create_connection(...)` with `server.accept()` (handshake completes), `conn.close()`/`client.close()` (FIN). UDP uses `sendto`/`recvfrom` with no connection, so there is nothing to open or close. On the checking machine, `ss -tln` during `hold` showed `LISTEN … 127.0.0.1:5050` (Verified).

### Tasks 16–18 (Expected)

Use the test plans. Task 18: tracert shows 2 hops (10.70.10.1, then 10.70.20.11). Before the router: src MAC = PC1, dst MAC = router Gi0/0, src IP 10.70.10.11, dst IP 10.70.20.11. After: src MAC = router Gi0/1, dst MAC = PC3, same IPs.

### Task 19 (model plan)

| Department | Network | Gateway | Hosts | Broadcast |
| --- | --- | --- | --- | --- |
| Sales | 10.80.10.0/24 | 10.80.10.1 (Gi0/0) | .2–.254 for PCs | 10.80.10.255 |
| Finance | 10.80.20.0/24 | 10.80.20.1 (Gi0/1) | .2–.254 | 10.80.20.255 |
| IT | 10.80.30.0/24 | 10.80.30.1 (Gi0/2) | .2–.254 | 10.80.30.255 |

Security: traffic between departments must pass through the router, where it can be filtered and logged; a compromised Sales PC cannot directly reach Finance devices at layer 2; broadcasts stay within each department. Extension: /28 gives 14 usable hosts, enough for 8 PCs (Verified: 2⁴ − 2 = 14).

### Task 20 (model points)

(a) Lecture section 10.1. (b) Section 9.1. (c) 10.70.20.0, 10.70.20.255, 254, mask `11111111.11111111.11111111.00000000`. (d) Sections 13.3 and 17.
