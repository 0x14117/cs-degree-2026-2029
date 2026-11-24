# Lab 8 — DHCP, Web Services and VLAN Routing Hands-on Workbook (20 Tasks)

**Module:** 4301COMP Computer Systems Architecture

**Session:** Teaching Week 04, Session B · **Matching lecture:** `../Lectures/Lecture-08-DHCP-Web-Services-and-VLAN-Routing.md`

---

## How to use this lab

**What this lab is for.** You will run a DHCP server and a web server in Packet Tracer, break DHCP and fix it, model DORA and VLANs in code, read real DNS and HTTP exchanges, check HTTPS certificates, and configure VLANs with Cisco IOS commands.

**Where the official tasks are.** The official sheet is titled *DHCP and HTTP on a Single Practice LAN*.

| Official lab sheet (TW04 Session B) | This workbook |
| --- | --- |
| Task 1 — Build the practice LAN | Task 16 |
| Task 2 — Configure DHCP and HTTP | Task 17 |
| Extra Challenge — Diagnose one service fault | Task 18 |

In the timetabled lab, **do Tasks 16–18 first**. Note that this week the official sheet **does** use the **router CLI** (for the router interface only).

**Tools**

| Tool | Used in | Notes |
| --- | --- | --- |
| Cisco Packet Tracer 9.0 | Tasks 10, 16–19 | Named on the official sheet; Logical workspace |
| Microsoft Word, Snipping Tool | Tasks 16–18 | For `TW04B_YourStudentID.docx` |
| Command Prompt on your own Windows PC | Tasks 12–14 | Read-only commands; **never** run `ipconfig /release` on your real PC |
| A web browser | Task 14 | To inspect a real certificate |
| Python 3 | Tasks 11, 13, 15 | **Optional, your choice.** Built-in modules only |

**Rules:** predict before you check; record exactly what you see (including failures); use hints only after a real attempt.

**Labels:** **Verified** = run before being written here (Linux: a real local DNS server queried with `dig`, a real web server queried with `curl`, real HTTPS certificate checks, Python 3.13). **Expected** = not run here (Packet Tracer, Cisco IOS, Windows).

**Safety (from the official sheet).** All network configuration in Tasks 16–19 is **inside the simulation**, not Windows. Do not release or renew your real network adapter, and do not run a DHCP server on a real network: a second DHCP server on a shared network can break other people's connections.

---

## Part A — Warm-up: recognise and predict (Tasks 1–5)

### Task 1 — DORA in order

**Goal:** order the DHCP messages and identify who sends each.

Put these in order, and for each say **who sends it** (client or server) and whether it is a **broadcast** in the basic exchange:

- REQUEST for 192.168.88.100
- OFFER of 192.168.88.100, mask, gateway, DNS, lease
- DISCOVER
- ACKNOWLEDGE

Then list the **five** settings slide 6 says the server provides.

**Expected result:** D, O, R, A; the client sends D and R, both broadcast.

- **Hint 1:** The client has no address at the start.
- **Hint 2:** The Request is broadcast so that other servers know their offers were not chosen.

---

### Task 2 — Pool arithmetic

**Goal:** work out DHCP pool ranges and spot problems.

All networks are /24. For each, give the **first** and **last** pool address and say whether the pool fits inside the network and avoids the listed static addresses.

| # | Start | Max users | Static addresses to avoid | Last address | OK? |
| --- | --- | --- | --- | --- | --- |
| a | 192.168.88.100 | 20 | .1 (router), .10 (server) | | |
| b | 10.10.5.50 | 100 | .1, .10 | | |
| c | 192.168.1.2 | 253 | .1 (router), .10 (server) | | |
| d | 172.16.0.200 | 60 | .1 | | |

**Expected result:** a and b are fine; c and d have problems (Verified).

- **Hint 1:** Last = start + users − 1.
- **Hint 2:** A /24 ends at .255, and .255 is the broadcast address.

---

### Task 3 — Which DNS record?

**Goal:** choose the record type (A, AAAA, CNAME, MX, PTR).

1. `www.uni.test` → 192.168.88.10
2. Which server receives email for `uni.test`?
3. `intranet.uni.test` is another name for `portal.uni.test`
4. What name belongs to 192.168.88.10?
5. `portal.uni.test` → 2001:db8::20
6. A security analyst sees a suspicious IP address in a log and wants its hostname.

**Expected result:** six record types, one of them used twice.

- **Hint 1:** IPv4 → A; IPv6 → AAAA (four As for an address four times longer).
- **Hint 2:** Address → name is the reverse direction.

---

### Task 4 — Read an HTTP exchange

**Goal:** pick out the parts of a real HTTP request and response.

Real `curl -v` output from the checking machine (Verified):

```text
> GET / HTTP/1.1
> Host: 127.0.0.1:8080
> User-Agent: curl/8.5.0
> Accept: */*
> 
< HTTP/1.0 200 OK
< Server: SimpleHTTP/0.6 Python/3.13.18
< Date: (removed)
< Content-type: text/html
< Content-Length: 72
< Last-Modified: (removed)
< 
<html><body><h1>Visitor Information</h1><p>Sam Archer</p></body></html>
```

1. What is the **method** and the **path**?
2. Which header names the **site** wanted?
3. What is the **status code**, and what does it mean?
4. What type of content came back, and how many bytes?
5. Which server software answered?
6. Which transport protocol and port carried this exchange? (Look at the `Host` line.)

**Expected result:** six short answers.

- **Hint 1:** The lines starting `>` were sent by the client; `<` by the server.
- **Hint 2:** HTTP runs over TCP.

---

### Task 5 — Who hears the broadcast?

**Goal:** predict VLAN behaviour.

One 2960 switch:

| Port | VLAN | Device |
| --- | --- | --- |
| Fa0/1 | 10 (HR) | HR-PC1 |
| Fa0/3 | 10 (HR) | HR-PC2 |
| Fa0/2 | 20 (IT) | IT-PC1 |
| Fa0/4 | 20 (IT) | IT-PC2 |
| Fa0/5 | 30 (Students) | ST-PC1 |
| Fa0/6 | 30 (Students) | ST-PC2 |

1. HR-PC1 sends a DHCP Discover (broadcast). Which devices receive it?
2. ST-PC1 sends an ARP request (broadcast). Which devices receive it?
3. How many broadcast domains does this switch have?
4. Can IT-PC1 reach HR-PC1 with no router? Why?

**Expected result:** each broadcast reaches only the other PC in the same VLAN; 3 broadcast domains (Verified with `vlan_sim.py`).

- **Hint 1:** Slide 14: a VLAN is a separate Layer-2 broadcast domain.
- **Hint 2:** Slide 14 also says what traffic between VLANs requires.

---

## Part B — Find and fix (Tasks 6–10)

### Task 6 — Fix the DHCP pool

**Goal:** correct a broken DHCP pool for 192.168.88.0/24 (router .1, server .10).

Sam Archer set up:

| Field | Sam's value |
| --- | --- |
| Pool 1 | Gateway 192.168.88.254, Start 192.168.88.1, Mask 255.255.255.0, Max users 300 |
| Pool 2 | Gateway 192.168.88.1, Start 192.168.88.100, Mask 255.255.255.0, Max users 20 |
| DHCP service | Off |

Find **five** problems and give the corrected configuration (it should match the official lab).

**Expected result:** one pool, start .100, 20 users, gateway .1, service On.

- **Hint 1:** The official sheet says not to create a second pool for the same subnet.
- **Hint 2:** A /24 has only 254 host addresses, and .1 is already the router.

---

### Task 7 — What does this client's result mean?

**Goal:** interpret client IP results after DHCP (official pool: .100–.119, gateway .1).

| Client | Result of `ipconfig` | Valid? | Most likely meaning |
| --- | --- | --- | --- |
| Client-1 | 192.168.88.100 / 255.255.255.0 / 192.168.88.1 | | |
| Client-2 | 169.254.31.7 / 255.255.0.0 / (none) | | |
| Client-3 | 0.0.0.0 | | |
| Client-4 | 192.168.88.120 / 255.255.255.0 / 192.168.88.1 | | |
| Client-5 | 192.168.88.101 / 255.255.255.0 / 192.168.88.254 | | |
| Client-6 | 192.168.88.10 / 255.255.255.0 / 192.168.88.1 | | |

**Expected result:** only one row is fully valid.

- **Hint 1:** The official sheet lists three results that are **not** valid.
- **Hint 2:** Compare each address with the pool range and the static addresses.

---

### Task 8 — Misread DNS answers

**Goal:** correct wrong interpretations of real `dig` output.

Real output from the local DNS server on the checking machine (Verified):

```text
$ dig @127.0.0.53 www.uni.test A
;; ->>HEADER<<- opcode: QUERY, status: NOERROR
www.uni.test.		0	IN	A	192.168.88.10
$ dig @127.0.0.53 portal.uni.test AAAA
;; ->>HEADER<<- opcode: QUERY, status: NOERROR
portal.uni.test.	0	IN	AAAA	2001:db8::20
$ dig @127.0.0.53 intranet.uni.test A
;; ->>HEADER<<- opcode: QUERY, status: NOERROR
intranet.uni.test.	0	IN	CNAME	portal.uni.test.
portal.uni.test.	0	IN	A	192.168.88.20
$ dig @127.0.0.53 uni.test MX
;; ->>HEADER<<- opcode: QUERY, status: NOERROR
uni.test.		0	IN	MX	10 mail.uni.test.
$ dig @127.0.0.53 -x 192.168.88.10
;; ->>HEADER<<- opcode: QUERY, status: NOERROR
10.88.168.192.in-addr.arpa. 0	IN	PTR	www.uni.test.
$ dig @127.0.0.53 nothere.uni.test A
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN
```

Sam wrote these notes. Each is wrong. Correct them.

1. "intranet.uni.test has its own IP address, 192.168.88.20, separate from portal."
2. "The MX record says mail for uni.test goes to IP address 10."
3. "The PTR query looked up the name 10.88.168.192."
4. "NXDOMAIN means the DNS server is broken."
5. "The 0 in each line is an error code."

**Expected result:** five corrections.

- **Hint 1:** In an MX record, the number before the name is a preference.
- **Hint 2:** Each answer line is: name, TTL, class, type, value.

---

### Task 9 — Read the HTTPS errors

**Goal:** explain what certificate validation protects against.

Real results from the checking machine (Verified):

```text
$ curl --cacert cert.pem https://www.uni.test:8443/
<html><body><h1>Visitor Information</h1><p>Sam Archer</p></body></html>
(exit code 0)
$ curl https://www.uni.test:8443/            # certificate not trusted
curl: (60) SSL certificate problem: self-signed certificate
More details here: https://curl.se/docs/sslcerts.html

curl failed to verify the legitimacy of the server and therefore could not
establish a secure connection to it. To learn more about this situation and
how to fix it, please visit the web page mentioned above.
(exit code 60)
$ curl --cacert cert.pem https://evil.test:8443/   # wrong name
curl: (60) SSL: no alternative certificate subject name matches target host name 'evil.test'
More details here: https://curl.se/docs/sslcerts.html

curl failed to verify the legitimacy of the server and therefore could not
establish a secure connection to it. To learn more about this situation and
how to fix it, please visit the web page mentioned above.
(exit code 60)
```

1. Why did the first request succeed?
2. What does "self-signed certificate" mean, and why did `curl` refuse?
3. In the third test the encryption would have worked. Why did `curl` still refuse?
4. What would a web browser show the user in cases 2 and 3?
5. Slide 19 says HTTPS does **not** prove website **content** is trustworthy. Give an example.

**Expected result:** five answers linked to slide 19.

- **Hint 1:** `--cacert cert.pem` told `curl` to trust that one certificate.
- **Hint 2:** The certificate was issued for `www.uni.test`.

---

### Task 10 — Fix the IOS commands

**Goal:** correct a broken Cisco IOS session.

Sam typed this on a 2960 switch to put Fa0/1 in VLAN 10 (HR) and Fa0/2 in VLAN 20 (IT). **Six** lines are wrong or missing.

```text
Switch> configure terminal
Switch(config)# vlan 10
Switch(config-vlan)# name HR
Switch(config-vlan)# exit
Switch(config)# interface fa0/1
Switch(config-if)# swichport mode access
Switch(config-if)# switchport vlan access 10
Switch(config-if)# exit
Switch(config)# Switch(config)# interface fa0/2
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 20
Switch(config-if)# end
Switch# show vlans
```

1. List the six problems.
2. Write the corrected session (compare with slide 16).
3. **Optional, Packet Tracer:** type your corrected commands on a 2960 and run `show vlan brief`. Record which ports appear under VLAN 10 and VLAN 20.

**Expected result:** a session matching slide 16 (Expected in Packet Tracer).

- **Hint 1:** Look at the first prompt: which mode is Sam in?
- **Hint 2:** Was VLAN 20 ever created?

---

## Part C — Build (Tasks 11–15)

### Task 11 — Model DHCP

**Goal:** explore DORA, leases, reservations and pool exhaustion.

**Skill you gain:** you can model a network service's behaviour in code and use it to predict real faults such as an exhausted pool.

1. Save as `dhcp_sim.py`:

```python
# dhcp_sim.py - a model of a DHCP server handing out leases with DORA:
#   Discover (client broadcast) -> Offer (server) -> Request (client) -> Acknowledge (server)
#
# Pool settings match the official TW04B lab: start 192.168.88.100, 20 users,
# so addresses .100 to .119; gateway 192.168.88.1.
#
# Usage: python dhcp_sim.py

import ipaddress

GATEWAY = "192.168.88.1"
MASK = "255.255.255.0"
DNS = "0.0.0.0"


class DhcpServer:
    def __init__(self, start, max_users, lease_time, reservations=None):
        first = ipaddress.ip_address(start)
        self.pool = [str(first + i) for i in range(max_users)]
        self.leases = {}                       # MAC -> (address, expires_at)
        self.reservations = reservations or {} # MAC -> fixed address
        self.lease_time = lease_time
        self.on = True

    def free_address(self, now):
        used = {addr for addr, expires in self.leases.values() if expires > now}
        used |= set(self.reservations.values())
        for addr in self.pool:
            if addr not in used:
                return addr
        return None

    def dora(self, mac, now):
        print(f"  D  {mac} broadcasts DHCPDISCOVER (source 0.0.0.0, destination 255.255.255.255)")
        if not self.on:
            print("     ...no reply. The client gives up and uses 169.254.x.x (APIPA): not valid here.")
            return None
        if mac in self.reservations:
            offer = self.reservations[mac]
        elif mac in self.leases and self.leases[mac][1] > now:
            offer = self.leases[mac][0]          # renew the same address
        else:
            offer = self.free_address(now)
        if offer is None:
            print("     ...pool exhausted: no OFFER. The client falls back to 169.254.x.x.")
            return None
        print(f"  O  server offers {offer}, mask {MASK}, gateway {GATEWAY}, DNS {DNS}, lease {self.lease_time} h")
        print(f"  R  {mac} broadcasts DHCPREQUEST for {offer}")
        self.leases[mac] = (offer, now + self.lease_time)
        print(f"  A  server sends DHCPACK: {offer} leased until hour {now + self.lease_time}")
        return offer


if __name__ == "__main__":
    server = DhcpServer("192.168.88.100", max_users=20, lease_time=24,
                        reservations={"00:0A:00:00:00:99": "192.168.88.110"})

    print("Client-1 joins at hour 0:")
    server.dora("00:0A:00:00:00:01", now=0)
    print("Client-2 joins at hour 0:")
    server.dora("00:0A:00:00:00:02", now=0)
    print("Printer with a reservation joins:")
    server.dora("00:0A:00:00:00:99", now=0)
    print("Client-1 renews at hour 12 (same address expected):")
    server.dora("00:0A:00:00:00:01", now=12)

    print("\nDHCP service switched Off; Client-3 asks at hour 13:")
    server.on = False
    server.dora("00:0A:00:00:00:03", now=13)
```

2. Run `python dhcp_sim.py`. *What it does:* prints a simulation; it does not touch any real network. Actual output (Verified):

```text
Client-1 joins at hour 0:
  D  00:0A:00:00:00:01 broadcasts DHCPDISCOVER (source 0.0.0.0, destination 255.255.255.255)
  O  server offers 192.168.88.100, mask 255.255.255.0, gateway 192.168.88.1, DNS 0.0.0.0, lease 24 h
  R  00:0A:00:00:00:01 broadcasts DHCPREQUEST for 192.168.88.100
  A  server sends DHCPACK: 192.168.88.100 leased until hour 24
Client-2 joins at hour 0:
  D  00:0A:00:00:00:02 broadcasts DHCPDISCOVER (source 0.0.0.0, destination 255.255.255.255)
  O  server offers 192.168.88.101, mask 255.255.255.0, gateway 192.168.88.1, DNS 0.0.0.0, lease 24 h
  R  00:0A:00:00:00:02 broadcasts DHCPREQUEST for 192.168.88.101
  A  server sends DHCPACK: 192.168.88.101 leased until hour 24
Printer with a reservation joins:
  D  00:0A:00:00:00:99 broadcasts DHCPDISCOVER (source 0.0.0.0, destination 255.255.255.255)
  O  server offers 192.168.88.110, mask 255.255.255.0, gateway 192.168.88.1, DNS 0.0.0.0, lease 24 h
  R  00:0A:00:00:00:99 broadcasts DHCPREQUEST for 192.168.88.110
  A  server sends DHCPACK: 192.168.88.110 leased until hour 24
Client-1 renews at hour 12 (same address expected):
  D  00:0A:00:00:00:01 broadcasts DHCPDISCOVER (source 0.0.0.0, destination 255.255.255.255)
  O  server offers 192.168.88.100, mask 255.255.255.0, gateway 192.168.88.1, DNS 0.0.0.0, lease 24 h
  R  00:0A:00:00:00:01 broadcasts DHCPREQUEST for 192.168.88.100
  A  server sends DHCPACK: 192.168.88.100 leased until hour 36

DHCP service switched Off; Client-3 asks at hour 13:
  D  00:0A:00:00:00:03 broadcasts DHCPDISCOVER (source 0.0.0.0, destination 255.255.255.255)
     ...no reply. The client gives up and uses 169.254.x.x (APIPA): not valid here.
```

3. **Extend:** at the end of the file, make 20 new clients (MACs `BB:00` to `BB:13`) all ask at hour 0 on a **fresh** server with the same reservation. How many get an address? Why not 20?
4. **Extend:** after those, ask for a new client at hour 25. What happens and why?
5. The model renews by repeating DORA. What does a real client do instead (lecture section 7.3)?

**Expected result:** step 3: 19 clients get addresses, because the reserved .110 is taken out of the 20-address pool; step 4: an address is offered again because the 24-hour leases have expired (Verified).

- **Hint 1:** `for i in range(20): server.dora(f"BB:{i:02X}", now=0)`.
- **Hint 2:** Look at how `free_address` treats reservations.

---

### Task 12 — DHCP and DNS on your own PC

**Goal:** see the DHCP lease and DNS answers your real computer uses.

**Skill you gain:** you can read a host's DHCP lease details and query DNS records yourself, both routine checks when troubleshooting or investigating.

On your own Windows PC (Expected; all read-only):

1. `ipconfig /all`. Record for your active adapter: **DHCP Enabled**, **IPv4 Address**, **DHCP Server**, **DNS Servers**, **Lease Obtained**, **Lease Expires**. How long is your lease?
2. DNS queries with `nslookup`:

   ```text
   nslookup www.ljmu.ac.uk
   nslookup -type=AAAA www.ljmu.ac.uk
   nslookup -type=MX ljmu.ac.uk
   nslookup 8.8.8.8
   ```

   *What they do:* ask your DNS server for an A record, an AAAA record, MX records and a PTR (reverse) record. Record each answer. If you see "Non-authoritative answer", that means it came from a resolver's **cache**, not the authoritative server.
3. View (do **not** edit) your hosts file: `type C:\Windows\System32\drivers\etc\hosts`. Lines starting `#` are comments. Are there any active entries?

**Linux comparison (Verified):** a local DNS server answered `dig` queries for every record type (see Task 8).

**Expected result:** your lease details and four DNS answers. An empty hosts file (only comments) is normal.

- **Hint 1:** The MX answer may list several servers with different preference numbers.
- **Hint 2:** If `nslookup 8.8.8.8` returns `dns.google`, that is a PTR record.

---

### Task 13 — Run a real web server on your PC

**Goal:** serve a page and watch the HTTP exchange from both ends.

**Skill you gain:** you can run a web server, send it requests with `curl`, and read its access log, which is basic web-server administration and investigation.

1. Make a folder `site` with a file `index.html` containing: `<html><body><h1>Visitor Information</h1><p>Sam Archer</p></body></html>`.
2. In that folder, run `python -m http.server 8000 --bind 127.0.0.1`. *What it does:* serves the files in that folder to **your PC only** (127.0.0.1) until you press Ctrl + C.
3. In a browser, open `http://127.0.0.1:8000`. Look at the server window: one line appears per request. That is an **access log**.
4. In a second Command Prompt: `curl -v http://127.0.0.1:8000/` (`curl` is built into Windows 10 and 11). Compare with Task 4.
5. Request a page that does not exist: `curl -v http://127.0.0.1:8000/missing.html`. Record the status code.
6. `netstat -ano | findstr 8000` while it runs: which PID owns the listening port?
7. Stop the server with **Ctrl + C**.

**Expected result:** status 200 for `/`, **404** for `/missing.html` (both Verified on Linux), a LISTENING line on 127.0.0.1:8000 (Expected on Windows).

- **Hint 1:** If port 8000 is in use, choose another such as 8081.
- **Hint 2:** The access log shows the client address, time, request line and status code.

---

### Task 14 — Inspect a real certificate

**Goal:** check the certificate behind a real HTTPS site.

**Skill you gain:** you can inspect a website's certificate (who it was issued to, who issued it and when it expires), a basic phishing and misconfiguration check.

On your own PC (Expected):

1. Open `https://canvas.ljmu.ac.uk` (or another site you use). Click the icon to the left of the address > **Connection is secure** > **Certificate is valid** (wording varies by browser).
2. Record: **Issued to** (common name, and any other names under "Subject Alternative Name"), **Issued by**, **Valid from / to**.
3. Command Prompt: `curl -vI https://www.ljmu.ac.uk`. *What it does:* fetches only the headers and shows the TLS handshake details. Find the TLS version and the certificate's subject and issuer in the output.
4. Answer: why would a certificate for `canvas-ljmu-login.com` on a page that looks exactly like Canvas **not** make it safe?

**Verified comparison:** on the checking machine, a self-signed certificate was rejected ("self-signed certificate") and a certificate for the wrong name was rejected ("no alternative certificate subject name matches") (Task 9).

**Expected result:** a table of four certificate facts and one sentence on phishing.

- **Hint 1:** The site's name must appear in the certificate's names.
- **Hint 2:** Slide 19: a valid certificate authenticates the **server's name**, not its honesty.

---

### Task 15 — Model VLANs

**Goal:** confirm that VLANs separate broadcast domains.

**Skill you gain:** you can model how a switch keeps VLANs apart and predict who receives broadcasts.

1. Save as `vlan_sim.py`:

```python
# vlan_sim.py - a switch with VLANs. Each access port belongs to one VLAN.
# A frame can only be flooded or forwarded to ports in the SAME VLAN, so each
# VLAN is a separate Layer-2 broadcast domain (slide 14).
#
# Usage: python vlan_sim.py

BROADCAST = "FF:FF:FF:FF:FF:FF"


class VlanSwitch:
    def __init__(self, port_vlans):
        self.port_vlans = port_vlans      # port -> VLAN number (access ports)
        self.mac_table = {}               # (VLAN, MAC) -> port

    def receive(self, in_port, src, dst):
        vlan = self.port_vlans[in_port]
        self.mac_table[(vlan, src)] = in_port                # learn, per VLAN
        same_vlan = [p for p, v in self.port_vlans.items() if v == vlan and p != in_port]
        if dst != BROADCAST and (vlan, dst) in self.mac_table:
            return vlan, "forward", [self.mac_table[(vlan, dst)]]
        return vlan, "flood", same_vlan                      # only within this VLAN


if __name__ == "__main__":
    # Slide 16's example: Fa0/1 in VLAN 10 (HR), Fa0/2 in VLAN 20 (IT).
    # Two more ports added so each VLAN has two PCs.
    ports = {"Fa0/1": 10, "Fa0/3": 10, "Fa0/2": 20, "Fa0/4": 20}
    who = {"Fa0/1": "HR-PC1", "Fa0/3": "HR-PC2", "Fa0/2": "IT-PC1", "Fa0/4": "IT-PC2"}
    mac = {p: f"00:0A:00:00:00:0{i}" for i, p in enumerate(ports, start=1)}
    sw = VlanSwitch(ports)

    tests = [("Fa0/1", BROADCAST, "HR-PC1 sends a broadcast (e.g. ARP or DHCP Discover)"),
             ("Fa0/2", BROADCAST, "IT-PC1 sends a broadcast"),
             ("Fa0/3", mac["Fa0/1"], "HR-PC2 sends to HR-PC1"),
             ("Fa0/4", mac["Fa0/1"], "IT-PC2 tries to send straight to HR-PC1's MAC")]
    for port, dst, label in tests:
        vlan, action, out = sw.receive(port, mac[port], dst)
        reached = [who[p] for p in out] or ["nobody"]
        print(f"{label}\n   VLAN {vlan}: {action} -> reaches {', '.join(reached)}")
```

2. Run it. Actual output (Verified):

```text
HR-PC1 sends a broadcast (e.g. ARP or DHCP Discover)
   VLAN 10: flood -> reaches HR-PC2
IT-PC1 sends a broadcast
   VLAN 20: flood -> reaches IT-PC2
HR-PC2 sends to HR-PC1
   VLAN 10: forward -> reaches HR-PC1
IT-PC2 tries to send straight to HR-PC1's MAC
   VLAN 20: flood -> reaches IT-PC1
```

3. **Extend:** add VLAN 30 (Students) on Fa0/5 and Fa0/6 (as in Task 5) and send a broadcast from Fa0/5. Who receives it?
4. Why did IT-PC2's frame to HR-PC1's MAC get **flooded** within VLAN 20 instead of delivered?
5. What device would you add so IT can reach HR, and where would you control what is allowed?

**Expected result:** the VLAN 30 broadcast reaches only Fa0/6 (Verified).

- **Hint 1:** Add `"Fa0/5": 30, "Fa0/6": 30` to `ports` (and names to `who`).
- **Hint 2:** The switch learns MACs **per VLAN**: HR-PC1's MAC is unknown inside VLAN 20.

---

## Part D — Official tasks and integration (Tasks 16–20)

### Task 16 — Build the practice LAN (Official Task 1)

**Goal:** build a LAN with a router, a switch, a server and three clients.

**Skill you gain:** you can configure a router interface from the Cisco IOS CLI and verify it with `show` commands.

**Official steps**

1. Open **Cisco Packet Tracer 9.0** from **Start**; sign in with your Cisco learning account if prompted. Work in the **Logical** workspace. All configuration is inside the simulation, not Windows.
2. Use the bottom-left categories (**Network Devices > Routers** or **Switches**; **End Devices > PC** or **Server**). Click a model, then the workspace. Rename via **Config > Global Settings > Display Name**.
3. Add one **1941** router, one **2960-24TT** switch, one **Server-PT** and three **PC-PT**. Name them **Router**, **Switch**, **Service-Server** and **Client-1** to **Client-3**.
4. Cable with **Connections > Copper Straight-Through**: the three PCs' **FastEthernet0** to switch **Fa0/1**, **Fa0/2**, **Fa0/3**; **Service-Server FastEthernet0** to **Fa0/4**; **Router GigabitEthernet0/0** to switch **Fa0/24**.
5. **Router > CLI.** If asked "Would you like to enter the initial configuration dialog?", type **no** and press Enter; press Enter again. Type each command on its own line (do not type the prompts):

   ```text
   enable
   configure terminal
   interface g0/0
   ip address 192.168.88.1 255.255.255.0
   no shutdown
   end
   show ip interface brief
   show ip route
   ```

   **G0/0** should be **up/up** with a **connected** route for **192.168.88.0/24**. Wait for green links (or **Fast Forward Time**). A first ping can lose a reply while ARP resolves; repeat it before diagnosing a fault.
6. **Service-Server > Desktop > IP Configuration > Static:** IP **192.168.88.10**, mask **255.255.255.0**, gateway **192.168.88.1**. Leave DNS unused: this activity tests HTTP by numeric address.
7. **File > Save As** **TW04B_YourStudentID.pkt**. Create **TW04B_YourStudentID.docx** in Word for screenshots and answers.
8. On the server, **Desktop > Command Prompt**, `ping 192.168.88.1`. Capture the labelled topology and the successful ping.

**Test plan**

| Check | Expected | Actual |
| --- | --- | --- |
| Six devices named as specified | Yes | |
| Cabling to Fa0/1–Fa0/4 and Fa0/24 | Yes | |
| `show ip interface brief`: G0/0 192.168.88.1 up/up | Yes | |
| `show ip route`: `C 192.168.88.0/24 … GigabitEthernet0/0` | Yes | |
| Server static 192.168.88.10/24, gateway .1 | Yes | |
| Server → router ping | Replies | |
| Files saved | `.pkt` and `.docx` | |

- **Hint 1:** If G0/0 shows "administratively down", you missed `no shutdown`.
- **Hint 2:** `show ip route` marks connected networks with `C` (and the router's own address with `L`).

---

### Task 17 — Configure DHCP and HTTP (Official Task 2)

**Goal:** make the server hand out addresses and serve a web page.

**Official steps**

1. **Service-Server > Services > DHCP**: Service **On**. If a built-in pool named **serverPool** is shown, select it and edit it with the values below (do **not** create a second pool for the same subnet). If no pool is shown, create one and click **Add**:
   - Pool Name **Practice-LAN** if it can be changed; otherwise keep **serverPool**.
   - Default Gateway **192.168.88.1**, DNS Server **0.0.0.0**, Start IP Address **192.168.88.100**, Subnet Mask **255.255.255.0**, Maximum Number of Users **20**.
   - Click **Save** (editing) or **Add** (new).
   - The intended range is **192.168.88.100–119**, excluding the static gateway **.1** and server **.10**.
   - If a client gets an unexpected address, return here, confirm only one active pool for this subnet with these values, then renew the client.
2. Each **PC > Desktop > IP Configuration > DHCP**. Wait for "DHCP request successful". Then **Command Prompt** > `ipconfig`. Each PC must have a **different** address in **.100–.119**, mask **255.255.255.0**, gateway **192.168.88.1**. A blank, **0.0.0.0** or **169.254.x.x** address is **not** valid. If unsuccessful: back to Realtime, check green links, the server's static address, DHCP On and the saved pool; select Static then DHCP to retry.
3. **Service-Server > Services > HTTP**: HTTP **On**. Select **index.html > Edit**, replace its content with:

   ```html
   <html><body><h1>Visitor Information</h1><p>YourStudentID</p></body></html>
   ```

   substituting your own ID, and **Save**. (This page is inside the simulated server.)
4. **Client-1 > Command Prompt**: `ping 192.168.88.1`, then `ping 192.168.88.10`. Then **Desktop > Web Browser** > `http://192.168.88.10` > **Go**. Expect the heading and your ID. Use the Packet Tracer browser, not Edge/Chrome.
5. Capture one client `ipconfig`, the successful server ping and the page. If HTTP fails after ping succeeds, check **HTTP On**, the saved `index.html` and the `http://` URL. Numeric URLs do not test DNS. All switch ports stay in the default **VLAN 1**, so everything is one Layer-2 broadcast domain; separate VLAN routing is developed in TW05A.

**Supplementary:** switch to **Simulation** mode with the filter set to **DHCP** and click **Static** then **DHCP** on Client-3. Watch the four DORA messages; note which are broadcasts.

**Test plan**

| Check | Expected | Actual |
| --- | --- | --- |
| One pool only; values as listed | Yes | |
| Client-1, 2, 3 addresses | Three different addresses in .100–.119 | |
| Mask and gateway on clients | 255.255.255.0, 192.168.88.1 | |
| Client-1 → router and server pings | Replies | |
| Browser shows "Visitor Information" and your ID | Yes | |
| Simulation shows Discover, Offer, Request, Ack | Yes | |

- **Hint 1:** The first client usually gets .100, the next .101, and so on.
- **Hint 2:** If the browser shows nothing, check HTTP is On **and** that you clicked **Save** on `index.html`.

---

### Task 18 — Diagnose one service fault (Official Extra Challenge)

**Goal:** prove what happens when DHCP is unavailable, then fix it.

**Official steps**

1. Save a copy as **TW04B_Fault_YourStudentID.pkt**. On **Service-Server**, set **Services > DHCP > Off**.
2. **Only in Client-3 > Desktop > Command Prompt**, enter `ipconfig /release` then `ipconfig /renew`. Record the unsuccessful request or absence of a valid lease. If these simulated commands are unavailable, use **Client-3 > IP Configuration > Static**, then **DHCP**. **Do not release or renew the real Windows network adapter.**
3. Turn DHCP back **On**. On Client-3, repeat `ipconfig /renew` (or Static then DHCP). Verify its range, mask and gateway against Task 17, then `ping 192.168.88.10`. **Existing leases on the other clients do not prove that new DHCP requests are working.** Save the repaired copy.
4. Capture the faulty and corrected client configuration and add **one sentence stating the root cause**.

**Record**

| State | Client-3 address | Mask | Gateway | Ping .10 |
| --- | --- | --- | --- | --- |
| DHCP Off, after renew | | | | |
| DHCP On, after renew | | | | |

**Expected result:** with DHCP off, Client-3 has no valid lease (blank, 0.0.0.0 or 169.254.x.x) and cannot reach the server; with DHCP on, it gets an address in .100–.119 and the ping succeeds (Expected). Client-1 and Client-2 keep working throughout because their leases have not expired: that is why the official sheet warns that existing leases prove nothing.

- **Hint 1:** Compare with the "DHCP service switched Off" part of `dhcp_sim.py`'s output.
- **Hint 2:** A good root-cause sentence names the service, its state and the effect.

---

### Task 19 — Mini-project: two VLANs and a router

**Goal:** build the inter-VLAN design from slides 16–17.

**Skill you gain:** you can segment a switch into VLANs with IOS commands and route between them, the basis of every segmented enterprise network.

Build in Packet Tracer (Expected; IOS was not run here):

1. One **2960** switch, one **1941** router, four PCs: **HR-PC1**, **HR-PC2** (VLAN 10) and **IT-PC1**, **IT-PC2** (VLAN 20).
2. On the switch, use slide 16's commands to create VLAN 10 **HR** and VLAN 20 **IT**, and put the PC ports in the right VLANs. Also put **Fa0/23** in VLAN 10 and **Fa0/24** in VLAN 20.
3. Cable router **G0/0** → switch **Fa0/23**, router **G0/1** → switch **Fa0/24**.
4. Router (CLI or GUI): G0/0 **192.168.10.1/24** and G0/1 **192.168.20.1/24**, both `no shutdown`.
5. PCs (static): HR 192.168.10.11 and .12, gateway .10.1; IT 192.168.20.11 and .12, gateway .20.1.
6. `show vlan brief` on the switch; screenshot it.
7. Run the test plan. Then **delete** the router's G0/1 cable and repeat the HR → IT test.

**Test plan**

| Test | Expected | Actual |
| --- | --- | --- |
| HR-PC1 → HR-PC2 | Replies (same VLAN) | |
| IT-PC1 → IT-PC2 | Replies (same VLAN) | |
| HR-PC1 → IT-PC1 | Replies via the router | |
| `tracert` HR-PC1 → IT-PC1 | 192.168.10.1, then 192.168.20.11 | |
| HR-PC1 → IT-PC1 with G0/1 cable removed | Fails | |
| `show vlan brief` | Fa0/1, 0/3, 0/23 in VLAN 10; Fa0/2, 0/4, 0/24 in VLAN 20 (or your ports) | |

Finally, write two sentences: why is this design **segmented but not yet secure** (slide 19)?

- **Hint 1:** Lecture section 17.2 is this exact design.
- **Hint 2:** Nothing on the router yet decides which traffic is **allowed**.

---

### Task 20 — Assessment-style practice: network services

**This is practice only, not a real exam question.** The module exam is two hours with short-answer and essay-style questions; the report covers data storage and networking (module guide). Check the real AS1 brief on Canvas. Marks are invented for planning.

**Rules:** 25 minutes, closed book, write it yourself.

**(a)** Explain the purpose of DHCP and describe the DORA exchange. *(5 marks)*

**(b)** A DHCP pool starts at 192.168.88.100 with 20 users. State the range, and explain why the router (.1) and server (.10) are outside it. *(2 marks)*

**(c)** Explain how a recursive resolver finds the IPv4 address for `www.ljmu.ac.uk`, and state what A, CNAME and MX records are. *(5 marks)*

**(d)** A university separates HR, IT and Students using VLANs. Explain what a VLAN is, how traffic moves between VLANs, and why VLANs alone are not a complete security control. Include the role of HTTPS for the intranet portal. *(8 marks; aim for 250–350 words)*

**Self-marking checklist**

| Part | A good answer includes | Expected | Actual |
| --- | --- | --- | --- |
| (a) | Automatic address, mask, gateway, DNS, lease; fewer errors; Discover (broadcast), Offer, Request, Ack | 5 points | |
| (b) | .100–.119; statics outside the pool avoid duplicate addresses | 2 points | |
| (c) | Client → resolver; root, TLD, authoritative; answer cached; A = IPv4, CNAME = alias, MX = mail server | 5 points | |
| (d) | Separate Layer-2 broadcast domain on one switch; router or Layer-3 switch between VLANs, each interface a gateway; ACLs/firewalls needed; HTTPS = TLS, authenticates server and protects data in transit, not content or endpoints | 8 points | |
| Time | Within 25 minutes | Yes | |

- **Hint 1:** Use slide 18's university scenario as your structure for (d).
- **Hint 2:** Lecture sections 7, 9, 14, 17 and 19.

---

## Tracker

| Task | Name | Done | Notes / score |
| --- | --- | --- | --- |
| 1 | DORA in order | ☐ | /9 |
| 2 | Pool arithmetic | ☐ | /4 |
| 3 | Which DNS record? | ☐ | /6 |
| 4 | Read an HTTP exchange | ☐ | /6 |
| 5 | Who hears the broadcast? | ☐ | /4 |
| 6 | Fix the DHCP pool | ☐ | /5 |
| 7 | What does this result mean? | ☐ | /6 |
| 8 | Misread DNS answers | ☐ | /5 |
| 9 | Read the HTTPS errors | ☐ | /5 |
| 10 | Fix the IOS commands | ☐ | /6 |
| 11 | Model DHCP | ☐ | |
| 12 | DHCP and DNS on your PC | ☐ | |
| 13 | Real web server | ☐ | |
| 14 | Inspect a real certificate | ☐ | |
| 15 | Model VLANs | ☐ | |
| 16 | **Official Task 1** — Build the practice LAN | ☐ | |
| 17 | **Official Task 2** — DHCP and HTTP | ☐ | |
| 18 | **Official Extra Challenge** — Diagnose a DHCP fault | ☐ | |
| 19 | Mini-project: two VLANs and a router | ☐ | |
| 20 | Assessment-style practice | ☐ | /20 |

## Reflection

1. In Task 18, why did Client-1 keep working while DHCP was off? What does that teach you about testing a fix?
2. How long is the DHCP lease on your home or university network, and why might a network choose a short or long lease?
3. What would you check first if a website's name stopped working but its IP address still worked?
4. Explain to a friend, in two sentences, what the padlock in their browser does and does not mean.

---

## Answer key

**(Verified)** = run on the Linux checking machine (dnsmasq + `dig`, Python `http.server` + `curl`, OpenSSL certificate + `curl`, Python 3.13 models). **(Expected)** = Packet Tracer, IOS or Windows; not run here.

### Task 1

1 DISCOVER (client, broadcast) → 2 OFFER (server) → 3 REQUEST (client, broadcast) → 4 ACKNOWLEDGE (server). Settings: IP address, subnet mask, default gateway, DNS server address, lease duration.

### Task 2 (Verified)

a. .100–**.119**: fine. b. 10.10.5.50–**10.10.5.149**: fine, avoids .1 and .10. c. 192.168.1.2–**192.168.1.254**: fits the /24, but **includes .10** (the server's static address), so the server's address could be leased to a client: duplicate address risk. d. 172.16.0.200–**172.16.1.3**: **runs past the end** of 172.16.0.0/24 (and through its broadcast address .255) into another network: invalid.

### Task 3

1 A · 2 MX · 3 CNAME · 4 PTR · 5 AAAA · 6 PTR.

### Task 4 (Verified)

1. GET, path `/`. 2. `Host: 127.0.0.1:8080`. 3. **200 OK**: success. 4. `text/html`, **72** bytes. 5. `SimpleHTTP/0.6 Python/3.13.18`. 6. **TCP**, port **8080** (a test port; normal HTTP uses 80).

### Task 5 (Verified)

1. HR-PC2 only. 2. ST-PC2 only. 3. **Three** (one per VLAN). 4. **No**: they are in different broadcast domains; traffic between VLANs needs a router or Layer-3 switch (slide 14).

### Task 6

Problems: (1) **two pools** for the same subnet; (2) pool 1's start **.1** is the router's address; (3) **300** users is more than a /24 can hold (254 hosts); (4) pool 1's gateway **.254** is not the router; (5) the DHCP service is **Off**. Fix: **one** pool, gateway 192.168.88.1, DNS 0.0.0.0, start 192.168.88.100, mask 255.255.255.0, max users 20, service **On**.

### Task 7

| Client | Valid? | Meaning |
| --- | --- | --- |
| 1 | **Yes** | Correct lease |
| 2 | No | 169.254 (APIPA): no DHCP reply |
| 3 | No | 0.0.0.0: no address obtained |
| 4 | No | .120 is outside the pool: a second pool or wrong pool settings, or a manually typed address |
| 5 | No | Wrong gateway (.254): pool's gateway setting wrong |
| 6 | No | .10 is the **server's** static address: duplicate address (typed by hand, or a pool covering .10) |

### Task 8 (Verified output)

1. `intranet` has **no** address of its own: it is a **CNAME** (alias) for `portal`, and the address belongs to `portal`. 2. **10** is the MX **preference**; mail goes to the **server named** `mail.uni.test`. 3. It looked up the **address** 192.168.88.10, written in reverse form `10.88.168.192.in-addr.arpa`, and got the **name** `www.uni.test`. 4. NXDOMAIN means **the name does not exist**; the server worked correctly. 5. The 0 is the **TTL** (seconds the answer may be cached); this test server sets none.

### Task 9 (Verified output)

1. The client trusted the certificate (`--cacert`) **and** the name `www.uni.test` matched it. 2. Self-signed = issued by itself, not by a certificate authority the client trusts, so the client cannot prove the server's identity and stops. 3. The certificate is for `www.uni.test`, not `evil.test`: the server could not prove it **is** `evil.test`, so continuing could mean talking to an impostor. 4. A full-page warning such as "Your connection is not private" (Expected). 5. A phishing site with a valid certificate for its own look-alike name, or a genuine site showing false information.

### Task 10

Problems: (1) `configure terminal` typed at `Switch>`: `enable` is missing first; (2) `swichport` misspelt; (3) `switchport vlan access 10` has the words in the wrong order (`switchport access vlan 10`); (4) the prompt was typed into a command (`Switch(config)# interface fa0/2`); (5) VLAN **20 was never created** (`vlan 20`, `name IT`, `exit` missing); (6) `show vlans` should be `show vlan brief`. Corrected session = slide 16.

### Task 11 (Verified)

Step 3: **19** clients get addresses; the 20th gets no offer, because the reserved .110 is never handed out dynamically, leaving 19 free addresses. Step 4: at hour 25 all the 24-hour leases have expired, so the new client is offered **192.168.88.100** again. Step 5: a real client renews part-way through its lease with a **Request** to its server and an **Ack**, without a new Discover.

### Task 12 (Expected)

Your values. Typical home networks: lease 24 hours to several days; DHCP server = your router's address.

### Task 13 (Verified on Linux; Windows Expected)

`/` → 200; `/missing.html` → **404**. The access log shows lines such as `127.0.0.1 - - [time] "GET / HTTP/1.1" 200 -`. `netstat` shows 127.0.0.1:8000 LISTENING with your `python.exe` PID.

### Task 14 (Expected)

Your certificate details. Phishing answer: a certificate only proves the site **is** `canvas-ljmu-login.com`; it says nothing about whether that domain belongs to LJMU.

### Task 15 (Verified)

Step 3: the broadcast from Fa0/5 reaches **Fa0/6 only**. Step 4: the switch learns MACs per VLAN; HR-PC1's MAC is known only in VLAN 10, so inside VLAN 20 it is an unknown destination and is flooded within VLAN 20, never reaching HR. Step 5: a **router** (or Layer-3 switch); control what is allowed with **ACLs/firewall rules** on it.

### Tasks 16–18 (Expected)

Use the test plans. Task 16: `show ip interface brief` → `GigabitEthernet0/0 192.168.88.1 YES manual up up`; `show ip route` → `C 192.168.88.0/24 is directly connected, GigabitEthernet0/0` and `L 192.168.88.1/32 …`. Task 18 root cause (model): "Client-3 had no valid address because the DHCP service on Service-Server was switched off, so its renewal request received no reply."

### Task 19 (Expected)

Use the test plan. Segmented but not secure: traffic between HR and IT is now forced through the router, but the router forwards everything because no ACL or firewall rule restricts it (slides 14 and 19).

### Task 20 (model points)

(a) Lecture sections 6–7. (b) 192.168.88.100–119; statics outside to avoid duplicates. (c) Section 9 and 11. (d) Sections 14, 17 and 19.
