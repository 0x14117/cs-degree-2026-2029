# Lab 9 — Network Segmentation and Layer 3 Connectivity Hands-on Workbook (20 Tasks)

**Module:** 4301COMP Computer Systems Architecture

**Session:** Teaching Week 05, Session A · **Matching lecture:** `../Lectures/Lecture-09-Network-Segmentation-and-Layer-3-Connectivity.md`

---

## How to use this lab

**What this lab is for.** You will segment a switch into two VLANs, route between them with a router, break an access port on purpose and diagnose it, compare the three inter-VLAN routing methods, write and check an address plan, and practise choosing the right verification command.

**Where the official tasks are.**

| Official lab sheet (TW05 Session A) | This workbook |
| --- | --- |
| Task 1 — Create two isolated practice VLANs | Task 16 |
| Task 2 — Route through two physical router links | Task 17 |
| Task 3 — Extra Challenge: diagnose an access-port fault | Task 18 |

In the timetabled lab, **do Tasks 16–18 first**. Tasks 13 and 14 rebuild the same network with the other two routing methods.

**Tools**

| Tool | Used in | Notes |
| --- | --- | --- |
| Cisco Packet Tracer 9.0 | Tasks 10, 13–19 | Named on the official sheet; Logical workspace; switch and router CLI |
| Microsoft Word | Tasks 17–18 | For `TW05A_YourStudentID.docx` |
| Python 3 | Tasks 11–12 | **Optional, your choice.** Built-in modules only |

**Rules:** predict before you check; when a test fails, **fix only the inconsistent setting and repeat the test** (official sheet); record what you actually see.

**Labels:** **Verified** = run before being written here (Python models of the official network, Python 3.13). **Expected** = not run here (Packet Tracer and Cisco IOS).

**IOS reminder:** type only the command, never the prompt (`Switch(config)#`). A first ping can lose a reply while ARP resolves; repeat it before diagnosing a fault.

---

## Part A — Warm-up: recognise and predict (Tasks 1–5)

### Task 1 — Local or routed?

**Goal:** apply slide 7's rule.

For each host, say **local** (ARP for the destination) or **routed** (ARP for the gateway).

| # | Host address/prefix | Destination | Local or routed? |
| --- | --- | --- | --- |
| a | 10.10.10.12/24 | 10.10.10.11 | |
| b | 10.10.20.11/24 | 10.10.10.1 | |
| c | 10.10.20.13/24 | 10.10.20.1 | |
| d | 192.168.1.130/25 | 192.168.1.20 | |
| e | 10.10.20.13/24 | 8.8.8.8 | |
| f | 172.16.5.10/24 | 172.16.5.200 | |
| g | 172.16.5.10/26 | 172.16.5.70 | |
| h | 10.10.20.12/**16** | 10.10.10.11 | |

Then: in row h, what goes wrong in the official network, where 10.10.10.11 is in a different VLAN?

**Expected result:** 4 local, 4 routed (Verified with Python).

- **Hint 1:** Use the **host's** mask on both addresses.
- **Hint 2:** /26 blocks: .0–.63, .64–.127, …

---

### Task 2 — Who are my neighbours?

**Goal:** read VLAN membership and predict Layer-2 reachability.

After the official Task 1 commands, the switch has:

| Port | Device | VLAN |
| --- | --- | --- |
| Fa0/1 | PC1 10.10.10.11 | 110 |
| Fa0/2 | PC2 10.10.10.12 | 110 |
| Fa0/3 | PC3 10.10.20.11 | 120 |
| Fa0/4 | PC4 10.10.20.12 | 120 |
| Fa0/5 | PC5 10.10.20.13 | 120 |

1. Which PCs receive PC4's ARP broadcast?
2. Before any router is added, which of these pings work: PC1 → PC2, PC3 → PC5, PC1 → PC3?
3. How many broadcast domains are there?
4. If PC5 were plugged into Fa0/2 instead (still 10.10.20.13), who would its neighbours be, and could it reach PC3?

**Expected result:** 2 broadcast domains; only same-VLAN pings work before routing.

- **Hint 1:** Slide 5: devices share broadcasts with their VLAN only.
- **Hint 2:** For 4, slide 6: a port in the wrong VLAN gives the wrong neighbours.

---

### Task 3 — Pick the routing method

**Goal:** choose an inter-VLAN routing method for each case (slide 14).

| # | Situation | Method | One trade-off |
| --- | --- | --- | --- |
| a | Temporary training room, three small VLANs, router with spare ports | | |
| b | Campus distribution, many VLANs, high traffic | | |
| c | Small branch, one router link to the switch | | |
| d | The official TW05A lab | | |
| e | A school adding a tenth VLAN; the router has only two Gigabit ports | | |

**Expected result:** each of the three methods appears at least once.

- **Hint 1:** Count the router ports each method needs.
- **Hint 2:** Lecture section 9.4's comparison table.

---

### Task 4 — Read an address plan

**Goal:** spot the infrastructure, the pool and any problems.

| VLAN | Subnet | Gateway | Reserved | DHCP pool |
| --- | --- | --- | --- | --- |
| 110 RECEPTION | 10.10.10.0/24 | 10.10.10.1 | .1–.9 | .100–.199 |
| 120 WORKSHOP | 10.10.20.0/24 | 10.10.20.1 | .1–.9 | .100–.199 |

1. A printer for reception needs a fixed address. Choose one and say why.
2. How many DHCP addresses can each VLAN hand out?
3. A third VLAN, 130 GUEST, is needed. Following the same pattern, what subnet and gateway would you give it?
4. Why is it helpful that the VLAN number and the third octet are linked?

**Expected result:** an address in .2–.9; 100 addresses each; 10.10.30.0/24 with gateway 10.10.30.1.

- **Hint 1:** Infrastructure is reserved first.
- **Hint 2:** .100 to .199 inclusive.

---

### Task 5 — Predict `show vlan brief`

**Goal:** predict switch output from commands.

After these commands on a new 2960 (all ports start in VLAN 1):

```text
vlan 110
name RECEPTION
exit
vlan 120
name WORKSHOP
exit
interface range fa0/1 - 2
switchport mode access
switchport access vlan 110
exit
interface range fa0/3 - 5
switchport mode access
switchport access vlan 120
end
```

Predict which ports `show vlan brief` lists under **default** (VLAN 1), **RECEPTION** (110) and **WORKSHOP** (120). (The 2960-24TT has Fa0/1–Fa0/24 and Gi0/1–Gi0/2.)

**Expected result:** 110: Fa0/1–2; 120: Fa0/3–5; VLAN 1: Fa0/6–24 and Gi0/1–2 (Expected).

- **Hint 1:** `interface range fa0/3 - 5` means Fa0/3, Fa0/4 and Fa0/5.
- **Hint 2:** Ports never mentioned stay in VLAN 1.

---

## Part B — Find and fix (Tasks 6–10)

### Task 6 — Fix the switch configuration

**Goal:** correct a broken VLAN session.

Sam Archer typed this to recreate official Tasks 1 and 2.2. **Six** problems stop it working as intended.

```text
Switch> configure terminal
Switch(config)# vlan 110
Switch(config-vlan)# name RECEPTION
Switch(config-vlan)# exit
Switch(config)# interface range fa0/1 - 2
Switch(config-if-range)# switchport access vlan 110
Switch(config-if-range)# exit
Switch(config)# interface range fa0/3 - 5
Switch(config-if-range)# switchport mode access
Switch(config-if-range)# switchport access vlan 210
Switch(config-if-range)# exit
Switch(config)# interface fa0/23
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 120
Switch(config-if)# exit
Switch(config)# interface fa0/24
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 110
Switch(config-if)# end
```

**Expected result:** six problems listed and a corrected session matching the official sheet.

- **Hint 1:** Check the first prompt, and whether every VLAN used was created.
- **Hint 2:** Compare Fa0/23 and Fa0/24 with the router interfaces they serve (G0/0 → VLAN 110).

---

### Task 7 — Fix the router configuration

**Goal:** correct a router session and predict its symptoms.

```text
Router> enable
Router# configure terminal
Router(config)# interface g0/0
Router(config-if)# ip address 10.10.10.1 255.255.0.0
Router(config-if)# exit
Router(config)# interface g0/1
Router(config-if)# ip address 10.10.20.254 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# end
```

The PCs use gateways 10.10.10.1 and 10.10.20.1, as in the official lab.

1. Find **three** problems.
2. For each, say what `show ip interface brief` or `show ip route` would show.
3. Which pings would fail, and why?

**Expected result:** three problems with their evidence.

- **Hint 1:** Router interfaces start administratively down.
- **Hint 2:** The gateway configured on the PCs must be the router's actual address.

---

### Task 8 — Diagnose from evidence

**Goal:** identify a fault from command output, using the official troubleshooting order.

For each case, name the fault, the check that proves it, and the **one** setting to fix.

**Case A.** PC4 cannot ping 10.10.20.1. `show vlan brief` shows Fa0/4 under VLAN 110. PC4 `ipconfig`: 10.10.20.12 / 255.255.255.0 / 10.10.20.1.

**Case B.** No VLAN 120 PC can ping 10.10.20.1, but PC3 → PC4 works. `show ip interface brief`: `GigabitEthernet0/1 10.10.20.1 YES manual administratively down down`.

**Case C.** PC1 → PC3 fails, PC3 → PC4 works, PC3 → 10.10.20.1 works. PC3 `ipconfig`: 10.10.20.11 / 255.255.255.0 / Default Gateway: 0.0.0.0.

**Case D.** PC2 → PC1 works, PC2 → PC3 fails. PC2 `ipconfig`: 10.10.10.12 / 255.255.255.0 / 10.10.20.1.

**Case E.** Every VLAN 120 PC can ping the others but not 10.10.20.1. `show vlan brief`: Fa0/24 under VLAN 110. Router G0/1 up/up.

**Expected result:** five faults, each matching a row of lecture section 12's table (Verified with the Lab 9 model).

- **Hint 1:** Work bottom-up: switch membership → PC settings → router state.
- **Hint 2:** In Case C, think about the **reply**.

---

### Task 9 — Fix the address plan

**Goal:** correct a faulty VLAN address plan.

| VLAN | Subnet | Gateway | Reserved | DHCP pool | Hosts needed |
| --- | --- | --- | --- | --- | --- |
| 110 RECEPTION | 10.10.10.0/24 | 10.10.10.1 | .1–.9 | .1–.50 | 25 |
| 120 WORKSHOP | 10.10.0.0/16 | 10.10.30.1 | 10.10.20.1–.9 | 10.10.20.100–.120 | 40 |
| 130 GUEST | 10.10.30.0/27 | 10.10.30.1 | .1–.5 | .10–.40 | 50 |

1. Find all the problems (there are at least six).
2. Rewrite the plan so it follows lecture section 10's principles.
3. Check your corrected plan with `plan_check.py` (Task 12).

**Expected result:** `plan_check.py` finds 8 problems in Sam's plan (Verified) and none in yours.

- **Hint 1:** A /16 starting 10.10.0.0 contains every 10.10.x.x address.
- **Hint 2:** A /27 has 2⁵ − 2 = 30 usable addresses.

---

### Task 10 — Wrong VLAN, wrong neighbours

**Goal:** see slide 6's warning for yourself, beyond the official challenge.

Use a **copy** of your working Task 17 file (Expected):

1. Move **Fa0/23** (the router's VLAN 110 link) into VLAN 120. Predict, then test: PC1 → 10.10.10.1? PC1 → PC3?
2. Restore it. Now give **PC4** the mask 255.255.0.0 (keep its address and gateway). Predict, then test PC4 → PC1 and PC4 → PC5.
3. Restore it. For each fault, which single command showed you the cause fastest?

**Expected result:** step 1: PC1 cannot reach its gateway or PC3; step 2: PC4 → PC1 fails (PC4 wrongly treats it as local) while PC4 → PC5 works (Verified with the model; Packet Tracer results Expected).

- **Hint 1:** In step 1, G0/0 is now in the wrong broadcast domain for VLAN 110's hosts.
- **Hint 2:** In step 2, apply PC4's new mask to 10.10.10.11.

---

## Part C — Build (Tasks 11–15)

### Task 11 — Trace pings with a segmentation model

**Goal:** model the official network and reproduce its faults.

**Skill you gain:** you can model a network's forwarding decisions (host, switch, router) and use the model to predict and explain faults before touching real equipment.

1. Save as `segment_sim.py`:

```python
# segment_sim.py - trace a ping through a VLAN-segmented network with a router.
#
# It follows the same checks a real host, switch and router make:
#   1. Host: is the destination in my subnet? If yes -> local; if no -> use my gateway.
#   2. Switch: the frame can only reach ports in the SAME VLAN as the sender's port.
#   3. Router: the interface must be up, and the destination must be in a connected network.
#   4. The reply must make the same journey back.
# It models the official TW05A lab (VLAN 110 = 10.10.10.0/24, VLAN 120 = 10.10.20.0/24).
#
# Usage: python segment_sim.py

import ipaddress

# Switch ports and their access VLANs (official lab, Task 2 complete).
PORT_VLAN = {"Fa0/1": 110, "Fa0/2": 110, "Fa0/3": 120, "Fa0/4": 120, "Fa0/5": 120,
             "Fa0/23": 110, "Fa0/24": 120}

# Hosts: port, address/prefix, gateway (None = blank).
HOSTS = {
    "PC1": ("Fa0/1", "10.10.10.11/24", "10.10.10.1"),
    "PC2": ("Fa0/2", "10.10.10.12/24", "10.10.10.1"),
    "PC3": ("Fa0/3", "10.10.20.11/24", "10.10.20.1"),
    "PC4": ("Fa0/4", "10.10.20.12/24", "10.10.20.1"),
    "PC5": ("Fa0/5", "10.10.20.13/24", "10.10.20.1"),
}

# Router interfaces: switch port they plug into, address/prefix, up?
ROUTER = {"G0/0": ("Fa0/23", "10.10.10.1/24", True),
          "G0/1": ("Fa0/24", "10.10.20.1/24", True)}


def who_has(ip, vlan):
    """Which host or router interface owns this IP AND sits in this VLAN? (ARP)"""
    for name, (port, cidr, _gw) in HOSTS.items():
        if ipaddress.ip_interface(cidr).ip == ipaddress.ip_address(ip) and PORT_VLAN[port] == vlan:
            return name
    for name, (port, cidr, up) in ROUTER.items():
        if up and ipaddress.ip_interface(cidr).ip == ipaddress.ip_address(ip) and PORT_VLAN[port] == vlan:
            return "Router " + name
    return None


def one_way(src_name, src_port, src_cidr, src_gw, dst_ip, log):
    """Deliver one packet from a host. Returns the name that receives it, or None."""
    me = ipaddress.ip_interface(src_cidr)
    vlan = PORT_VLAN[src_port]
    if ipaddress.ip_address(dst_ip) in me.network:
        log.append(f"{src_name}: {dst_ip} is local ({me.network}); ARP for it in VLAN {vlan}")
        target = who_has(dst_ip, vlan)
        if target is None:
            log.append(f"   no reply to ARP: nobody with {dst_ip} in VLAN {vlan}")
        return target
    if src_gw is None:
        log.append(f"{src_name}: {dst_ip} is remote but no default gateway is set")
        return None
    log.append(f"{src_name}: {dst_ip} is remote; ARP for gateway {src_gw} in VLAN {vlan}")
    gw = who_has(src_gw, vlan)
    if gw is None or not gw.startswith("Router"):
        log.append(f"   gateway {src_gw} not reachable in VLAN {vlan}")
        return None
    # The router looks for a connected network that contains the destination.
    for iface, (port, cidr, up) in ROUTER.items():
        net = ipaddress.ip_interface(cidr).network
        if up and ipaddress.ip_address(dst_ip) in net:
            out_vlan = PORT_VLAN[port]
            log.append(f"   {gw} routes it out of {iface} ({net}) into VLAN {out_vlan}")
            target = who_has(dst_ip, out_vlan)
            if target is None:
                log.append(f"   no reply to the router's ARP for {dst_ip} in VLAN {out_vlan}")
            return target
    log.append(f"   {gw} has no connected route to {dst_ip}")
    return None


def ping(src, dst_ip):
    log = []
    port, cidr, gw = HOSTS[src]
    target = one_way(src, port, cidr, gw, dst_ip, log)
    ok = False
    if target and not target.startswith("Router"):
        t_port, t_cidr, t_gw = HOSTS[target]
        my_ip = str(ipaddress.ip_interface(cidr).ip)
        log.append(f"{target} received the request; now the reply:")
        back = one_way(target, t_port, t_cidr, t_gw, my_ip, log)
        ok = back == src
    elif target:
        ok = True                     # router interface replies directly
        log.append(f"{target} replies directly")
    print(f"ping {src} -> {dst_ip}: {'SUCCESS' if ok else 'FAIL'}")
    for line in log:
        print("   " + line)
    return ok


if __name__ == "__main__":
    print("== Working network (official Task 2)")
    ping("PC1", "10.10.10.12")
    ping("PC1", "10.10.20.11")

    print("\n== Fault: PC3's port moved to VLAN 110 (official Extra Challenge)")
    PORT_VLAN["Fa0/3"] = 110
    ping("PC3", "10.10.20.1")
    PORT_VLAN["Fa0/3"] = 120          # repair
    ping("PC3", "10.10.20.1")
```

2. Run `python segment_sim.py`. *What it does:* prints simulated ping traces; it does not touch any real network. Actual output (Verified):

```text
== Working network (official Task 2)
ping PC1 -> 10.10.10.12: SUCCESS
   PC1: 10.10.10.12 is local (10.10.10.0/24); ARP for it in VLAN 110
   PC2 received the request; now the reply:
   PC2: 10.10.10.11 is local (10.10.10.0/24); ARP for it in VLAN 110
ping PC1 -> 10.10.20.11: SUCCESS
   PC1: 10.10.20.11 is remote; ARP for gateway 10.10.10.1 in VLAN 110
      Router G0/0 routes it out of G0/1 (10.10.20.0/24) into VLAN 120
   PC3 received the request; now the reply:
   PC3: 10.10.10.11 is remote; ARP for gateway 10.10.20.1 in VLAN 120
      Router G0/1 routes it out of G0/0 (10.10.10.0/24) into VLAN 110

== Fault: PC3's port moved to VLAN 110 (official Extra Challenge)
ping PC3 -> 10.10.20.1: FAIL
   PC3: 10.10.20.1 is local (10.10.20.0/24); ARP for it in VLAN 110
      no reply to ARP: nobody with 10.10.20.1 in VLAN 110
ping PC3 -> 10.10.20.1: SUCCESS
   PC3: 10.10.20.1 is local (10.10.20.0/24); ARP for it in VLAN 120
   Router G0/1 replies directly
```

3. Reproduce each Task 8 case in the model by changing `PORT_VLAN`, `HOSTS` or `ROUTER` before a `ping(...)` line, then restoring it. Example for Case B: `ROUTER["G0/1"] = ("Fa0/24", "10.10.20.1/24", False)`.
4. Use the model to answer: in Case C, does the ping **request** reach PC3? Where exactly does it fail?

**Expected result (Verified):** A fails PC4 → gateway; B fails PC1 → PC3 but PC3 → PC5 works; C fails on the **reply**; D: PC2 → PC1 works, PC2 → PC3 fails; E fails PC3 → gateway.

- **Hint 1:** Each `HOSTS` entry is `(port, "address/prefix", gateway)`; use `None` for no gateway.
- **Hint 2:** The trace lines after "received the request; now the reply" show the return journey.

---

### Task 12 — Check an address plan with code

**Goal:** automate the address-plan rules from slides 9 and 16.

**Skill you gain:** you can validate an address plan automatically, which catches overlaps and pool errors before they cause outages.

1. Save as `plan_check.py`:

```python
# plan_check.py - check a VLAN address plan for the mistakes slide 9 and slide 16 warn about:
# overlapping subnets, gateways outside their subnet, DHCP pools that overlap the
# reserved infrastructure range, and subnets too small for the number of hosts.
#
# Usage: python plan_check.py

import ipaddress

# Each VLAN: subnet, gateway, reserved infrastructure range (first, last),
# DHCP pool (first, last) or None, and how many hosts it must hold.
PLAN = {
    110: {"name": "RECEPTION", "subnet": "10.10.10.0/24", "gateway": "10.10.10.1",
          "reserved": ("10.10.10.1", "10.10.10.9"), "pool": ("10.10.10.100", "10.10.10.199"), "hosts": 25},
    120: {"name": "WORKSHOP", "subnet": "10.10.20.0/24", "gateway": "10.10.20.1",
          "reserved": ("10.10.20.1", "10.10.20.9"), "pool": ("10.10.20.100", "10.10.20.199"), "hosts": 40},
}


def check(plan):
    problems = []
    nets = {v: ipaddress.ip_network(d["subnet"]) for v, d in plan.items()}
    vlans = list(plan)
    for i, a in enumerate(vlans):                       # 1. overlapping subnets
        for b in vlans[i + 1:]:
            if nets[a].overlaps(nets[b]):
                problems.append(f"VLAN {a} {nets[a]} overlaps VLAN {b} {nets[b]}")
    for v, d in plan.items():
        net = nets[v]
        gw = ipaddress.ip_address(d["gateway"])
        if gw not in net or gw in (net.network_address, net.broadcast_address):
            problems.append(f"VLAN {v}: gateway {gw} is not a usable address in {net}")
        r1, r2 = (ipaddress.ip_address(x) for x in d["reserved"])
        if not (r1 <= gw <= r2):
            problems.append(f"VLAN {v}: gateway {gw} is outside the reserved range")
        if d["pool"]:
            p1, p2 = (ipaddress.ip_address(x) for x in d["pool"])
            if not (p1 in net and p2 in net) or p2 >= net.broadcast_address or p1 <= net.network_address:
                problems.append(f"VLAN {v}: pool {p1}-{p2} is not inside the usable range of {net}")
            if p1 <= r2 and r1 <= p2:
                problems.append(f"VLAN {v}: pool {p1}-{p2} overlaps reserved {r1}-{r2}")
            size = int(p2) - int(p1) + 1
            if size < d["hosts"]:
                problems.append(f"VLAN {v}: pool has {size} addresses but {d['hosts']} hosts are needed")
        usable = net.num_addresses - 2
        if usable < d["hosts"]:
            problems.append(f"VLAN {v}: {net} has {usable} usable addresses, needs {d['hosts']}")
    return problems


if __name__ == "__main__":
    for v, d in PLAN.items():
        print(f"VLAN {v} {d['name']:<10} {d['subnet']:<15} gateway {d['gateway']:<11} "
              f"reserved {d['reserved'][0]}-{d['reserved'][1].split('.')[-1]}  "
              f"pool {d['pool'][0]}-{d['pool'][1].split('.')[-1]}")
    found = check(PLAN)
    print("\n" + ("\n".join("PROBLEM: " + p for p in found) if found else "No problems found."))
```

2. Run it. Actual output (Verified):

```text
VLAN 110 RECEPTION  10.10.10.0/24   gateway 10.10.10.1  reserved 10.10.10.1-9  pool 10.10.10.100-199
VLAN 120 WORKSHOP   10.10.20.0/24   gateway 10.10.20.1  reserved 10.10.20.1-9  pool 10.10.20.100-199

No problems found.
```

3. Replace `PLAN` with Sam's plan from Task 9 and run again. How many problems does it find?
4. Enter your corrected plan. It should report **No problems found**.
5. **Extend:** add a check that the **gateway is not inside the DHCP pool**. Test it by putting a pool of .1–.50 back into one VLAN.

**Expected result:** 8 problems for Sam's plan (Verified); none for a correct one.

- **Hint 1:** Each VLAN is a dictionary with `subnet`, `gateway`, `reserved`, `pool` and `hosts`.
- **Hint 2:** For step 5: `if p1 <= gw <= p2:`.

---

### Task 13 — Rebuild with router-on-a-stick

**Goal:** route the same two VLANs over **one** trunk link.

**Skill you gain:** you can configure an 802.1Q trunk and router subinterfaces, the standard way to route many VLANs over one link.

Use a **copy** of your Task 17 file (Expected; IOS was not run here):

1. Delete the cable G0/1 ↔ Fa0/24. Keep G0/0 ↔ Fa0/23.
2. Switch:

   ```text
   configure terminal
   interface fa0/23
   switchport mode trunk
   end
   ```

3. Router (remove the old address from G0/0 first):

   ```text
   configure terminal
   interface g0/0
   no ip address
   no shutdown
   interface g0/0.110
   encapsulation dot1Q 110
   ip address 10.10.10.1 255.255.255.0
   interface g0/0.120
   encapsulation dot1Q 120
   ip address 10.10.20.1 255.255.255.0
   end
   show ip interface brief
   show ip route
   ```

4. Test: PC1 → 10.10.10.1, PC3 → 10.10.20.1, PC1 → PC3.
5. On the switch, `show interfaces trunk`. Which VLANs does it say are allowed and active on Fa0/23?

**Expected result:** all pings work; `show ip route` lists both networks as connected, via **G0/0.110** and **G0/0.120**.

- **Hint 1:** The PCs' gateways do not change.
- **Hint 2:** `encapsulation dot1Q` must come **before** `ip address` on a subinterface.

---

### Task 14 — Rebuild with a Layer-3 switch

**Goal:** route the two VLANs inside a multilayer switch.

**Skill you gain:** you can configure switch virtual interfaces (SVIs) and enable routing on a Layer-3 switch, the approach used in campus networks.

In a **new** file (Expected):

1. Place a **3560-24PS** multilayer switch and five PCs on Fa0/1–Fa0/5 (same addresses and gateways as the official lab). No router.
2. Create VLANs 110 and 120 and assign Fa0/1–2 and Fa0/3–5 as in official Task 1.
3. Then:

   ```text
   configure terminal
   ip routing
   interface vlan 110
   ip address 10.10.10.1 255.255.255.0
   no shutdown
   interface vlan 120
   ip address 10.10.20.1 255.255.255.0
   no shutdown
   end
   show ip route
   ```

4. Test PC1 → PC3 and `tracert 10.10.20.11` from PC1.
5. Compare with Tasks 17 and 13: how many physical links and router ports did each method use?

**Expected result:** `show ip route` shows `C 10.10.10.0/24 … Vlan110` and `C 10.10.20.0/24 … Vlan120`; PC1 → PC3 works with the first hop 10.10.10.1.

- **Hint 1:** An SVI only comes up when at least one port in that VLAN is connected.
- **Hint 2:** Without `ip routing`, the switch will not route between the VLANs.

---

### Task 15 — The right check for the question

**Goal:** practise slide 12: each command answers a different question.

**Skill you gain:** you can choose the fastest command to confirm or rule out each part of a design.

On your working Task 17 network (Expected), run each command and fill in:

| Command | Where | Question it answers | What you saw |
| --- | --- | --- | --- |
| `show vlan brief` | Switch | | |
| `show interfaces status` | Switch | | |
| `show mac address-table` (after some pings) | Switch | | |
| `ipconfig` | PC3 | | |
| `show ip interface brief` | Router | | |
| `show ip route` | Router | | |

Then: in `show mac address-table`, which VLAN and port does the router's **G0/1** MAC appear on? Why?

**Expected result:** six rows completed; G0/1's MAC appears in VLAN 120 on Fa0/24.

- **Hint 1:** The MAC table only fills after traffic has passed.
- **Hint 2:** Lecture section 12's table lists the questions.

---

## Part D — Official tasks and integration (Tasks 16–20)

### Task 16 — Create two isolated practice VLANs (Official Task 1)

**Goal:** create VLANs 110 and 120 and confirm that they are isolated.

**Skill you gain:** you can create VLANs, assign access ports with `interface range`, and verify membership.

**Official steps**

1. **1.1:** Open Cisco Packet Tracer 9.0 (Logical workspace). Add one **2960-24TT** and five **PC-PT** devices, named **PC1–PC5** (Config > Global Settings > Display Name). With **Copper Straight-Through**, connect each PC's **FastEthernet0**: PC1 → **Fa0/1**, PC2 → **Fa0/2**, PC3 → **Fa0/3**, PC4 → **Fa0/4**, PC5 → **Fa0/5**.
2. **1.2:** **Switch > CLI**. If asked about the initial configuration dialog, type **no**, Enter, Enter. Create the VLANs (one command per line, no prompts):

   ```text
   enable
   configure terminal
   vlan 110
   name RECEPTION
   exit
   vlan 120
   name WORKSHOP
   exit
   ```

3. **1.3:** Continue at `Switch(config)#`:

   ```text
   interface range fa0/1 - 2
   switchport mode access
   switchport access vlan 110
   exit
   interface range fa0/3 - 5
   switchport mode access
   switchport access vlan 120
   end
   show vlan brief
   ```

   Expect **Fa0/1–2** in **VLAN 110** and **Fa0/3–5** in **VLAN 120**. No routing exists yet.
4. **1.4:** On each PC, **Desktop > IP Configuration > Static**: PC1 **10.10.10.11**, PC2 **10.10.10.12**, PC3 **10.10.20.11**, PC4 **10.10.20.12**, PC5 **10.10.20.13**; mask **255.255.255.0**; gateways **blank** for now.
5. **1.5:** From **PC1 > Command Prompt**: `ping 10.10.10.12`, then `ping 10.10.20.11`. The local ping should succeed; the remote ping should fail before routing.
6. **1.6:** Wait for green links (or **Fast Forward Time**); repeat a first ping that loses a reply. At `Switch#`: `show vlan brief` and `show interfaces status`. Expect the five endpoint ports **connected** in their VLANs. **File > Save As** `TW05A_YourStudentID.pkt`.

**Test plan**

| Check | Expected | Actual |
| --- | --- | --- |
| `show vlan brief` | Fa0/1–2 VLAN 110 RECEPTION; Fa0/3–5 VLAN 120 WORKSHOP | |
| `show interfaces status` | Fa0/1–5 connected, VLANs 110/110/120/120/120 | |
| PC1 → 10.10.10.12 | Replies | |
| PC1 → 10.10.20.11 | Fails (no routing) | |
| Saved | `TW05A_<your ID>.pkt` | |

- **Hint 1:** In Packet Tracer, the remote ping usually reports "Request timed out" or nothing useful; with no gateway, PC1 has nowhere to send it.
- **Hint 2:** Lecture section 8.2.

---

### Task 17 — Route through two physical router links (Official Task 2)

**Goal:** connect the VLANs with a router and prove every path works.

**Official steps**

1. **2.1:** Place a **2911** router. With **Copper Straight-Through**: router **G0/0** → switch **Fa0/23**; router **G0/1** → switch **Fa0/24** (two separate cables).
2. **2.2:** Switch, at `Switch#`:

   ```text
   configure terminal
   interface fa0/23
   switchport mode access
   switchport access vlan 110
   exit
   interface fa0/24
   switchport mode access
   switchport access vlan 120
   end
   show vlan brief
   ```

   Check that each router-facing port is in the same VLAN as its intended clients.
3. **2.3:** **Router > CLI** (decline the setup dialogue with **no** if offered):

   ```text
   enable
   configure terminal
   interface g0/0
   ip address 10.10.10.1 255.255.255.0
   no shutdown
   exit
   interface g0/1
   ip address 10.10.20.1 255.255.255.0
   no shutdown
   end
   show ip interface brief
   show ip route
   ```

   Use physical interfaces throughout; no trunk or subinterfaces are needed. Each interface is a gateway in one broadcast domain.
4. **2.4:** On every PC keep the address and mask; set the gateway to **10.10.10.1** (PC1, PC2) or **10.10.20.1** (PC3–PC5).
5. **2.5:** On the router run `show ip interface brief` and `show ip route`: both interfaces **up/up**, both /24 networks **connected**. From every PC ping its gateway; then from PC1 ping **10.10.20.11** and **10.10.20.13**.
6. **2.6:** If a ping fails, check switch links and `show vlan brief`, then PC `ipconfig`, then router interface state and connected routes. **Fix only the inconsistent setting and repeat the test.** Use **Place Note (N)** to label the VLANs, subnets and router links. In **TW05A_YourStudentID.docx** record a device/address/mask/gateway table and the switch, router and ping evidence. Save both files.

**Device table for your document**

| Device | Port / interface | VLAN | Address | Mask | Gateway |
| --- | --- | --- | --- | --- | --- |
| PC1 | Fa0/1 | 110 | 10.10.10.11 | 255.255.255.0 | 10.10.10.1 |
| PC2 | Fa0/2 | 110 | | | |
| PC3 | Fa0/3 | 120 | | | |
| PC4 | Fa0/4 | 120 | | | |
| PC5 | Fa0/5 | 120 | | | |
| Router G0/0 | Fa0/23 | 110 | 10.10.10.1 | 255.255.255.0 | — |
| Router G0/1 | Fa0/24 | 120 | | | — |

**Test plan**

| Test | Expected | Actual |
| --- | --- | --- |
| `show ip interface brief` | G0/0 10.10.10.1 up/up; G0/1 10.10.20.1 up/up | |
| `show ip route` | `C 10.10.10.0/24` via G0/0; `C 10.10.20.0/24` via G0/1 | |
| Each PC → its gateway | Replies (5 tests) | |
| PC1 → 10.10.20.11 | Replies | |
| PC1 → 10.10.20.13 | Replies | |

- **Hint 1:** The model in Task 11 traces exactly these pings (Verified).
- **Hint 2:** If only one VLAN fails, check that VLAN's router port with `show vlan brief`.

---

### Task 18 — Diagnose an access-port fault (Official Task 3, Extra Challenge)

**Goal:** create, diagnose and repair a wrong-VLAN access port, then evaluate the design.

**Official steps**

1. **3.1:** Save a copy as **TW05A_Fault_YourStudentID.pkt**. At `Switch#`:

   ```text
   configure terminal
   interface fa0/3
   switchport access vlan 110
   end
   ```

   On **PC3 > Command Prompt**: `ping 10.10.20.1`. Expect failure after moving its port out of the correct broadcast domain.
2. **3.2:** At `Switch#`: `show vlan brief`; on PC3: `ipconfig`. Compare the port VLAN with the unchanged PC subnet. Repair:

   ```text
   configure terminal
   interface fa0/3
   switchport access vlan 120
   end
   ```

   Repeat the gateway ping and `ping 10.10.10.11`. Capture the failure, the corrected membership and the successful retest; save the repaired copy.
3. **3.3:** Explain why the fault occurred. Compare the **port capacity** and **single points of failure** in this design with alternative routing arrangements.

**Model of this fault (Verified):**

```text
ping PC3 -> 10.10.20.1: FAIL
   PC3: 10.10.20.1 is local (10.10.20.0/24); ARP for it in VLAN 110
      no reply to ARP: nobody with 10.10.20.1 in VLAN 110
```

**Test plan**

| Stage | Expected | Actual |
| --- | --- | --- |
| Fa0/3 in VLAN 110: PC3 → 10.10.20.1 | Fails | |
| `show vlan brief` shows Fa0/3 under 110 | Yes | |
| PC3 `ipconfig` unchanged (10.10.20.11/24, gw .20.1) | Yes | |
| After repair: PC3 → 10.10.20.1 | Replies | |
| After repair: PC3 → 10.10.10.11 | Replies | |

- **Hint 1:** The PC's subnet says "workshop"; the port says "reception". Which one decides who hears its ARP?
- **Hint 2:** For 3.3, use lecture section 9.4's table: router ports per VLAN, the shared link in router-on-a-stick, the switch as a single point of failure.

---

### Task 19 — Mini-project: segmenting a growing community centre

**Goal:** extend the community-centre design from slide 10 and justify it (slide 15).

**Skill you gain:** you can design a segmented network from requirements and justify the decisions in terms of security, manageability and scale.

**Brief.** The centre (VLAN 110 Reception, VLAN 120 Workshop) is adding:

- **Guest Wi-Fi** for visitors (up to 60 devices), which must not reach staff devices directly;
- **Staff** office PCs and a printer (15 devices);
- in a year, possibly two more VLANs.

The router has **two** Gigabit ports.

1. **Segmentation:** list the VLANs, with one sentence each on why that group is separate (roles, services or risk).
2. **Address plan:** one non-overlapping subnet per VLAN, gateway, reserved range, DHCP pool (where suitable). Check it with `plan_check.py`.
3. **Routing method:** choose one and justify it against the router's two ports and future growth.
4. **Build** the design in Packet Tracer (two PCs per VLAN is enough) and run a test plan of at least eight pings, including one between every pair of VLANs.
5. **Security note:** write two sentences on what still has to be added at the router before guests are truly kept away from staff devices.

**Test plan (add rows)**

| From | To | Expected | Actual |
| --- | --- | --- | --- |
| Guest PC | Staff PC | Replies for now (no ACL yet) | |
| Staff PC | Reception PC | Replies | |
| | | | |

- **Hint 1:** Four or more VLANs and only two router ports point to one particular method.
- **Hint 2:** Following the VLAN-to-octet pattern, VLAN 130 → 10.10.30.0/24.

---

### Task 20 — Assessment-style practice: segmentation and routing

**This is practice only, not a real exam question.** The module exam is two hours with short-answer and essay-style questions; the report covers data storage and networking (module guide). Check the real AS1 brief on Canvas. Marks are invented for planning.

**Rules:** 25 minutes, closed book, write it yourself.

**(a)** Explain what a VLAN is and give two reasons for segmenting a network. *(3 marks)*

**(b)** Explain how a host decides whether to send a frame directly or to its default gateway. *(3 marks)*

**(c)** Compare separate physical interfaces, router-on-a-stick and Layer-3 switching for inter-VLAN routing. *(6 marks)*

**(d)** A PC in the workshop VLAN suddenly cannot reach its gateway, although its IP settings have not changed. Explain the likely cause, how you would confirm it using switch, PC and router checks, and why VLANs alone do not make the network secure. *(8 marks; aim for 250–350 words)*

**Self-marking checklist**

| Part | A good answer includes | Expected | Actual |
| --- | --- | --- | --- |
| (a) | Separate Layer-2 broadcast domain on one switch; fewer broadcasts, organisation, supports security policy | 3 points | |
| (b) | Compares destination with own address and mask; local → ARP destination; remote → ARP gateway; IP destination unchanged | 3 points | |
| (c) | Ports/links used; scaling; capacity; single points of failure; suitable situations | 6 points | |
| (d) | Access port in wrong VLAN; `show vlan brief`, `ipconfig`, `show ip interface brief`/`show ip route`; fix one setting and retest; VLANs limit Layer 2 only; ACLs/firewalls at the Layer-3 boundary | 8 points | |
| Time | Within 25 minutes | Yes | |

- **Hint 1:** Use the official Extra Challenge as your example in (d).
- **Hint 2:** Lecture sections 7, 9 and 12.

---

## Tracker

| Task | Name | Done | Notes / score |
| --- | --- | --- | --- |
| 1 | Local or routed? | ☐ | /8 |
| 2 | Who are my neighbours? | ☐ | /4 |
| 3 | Pick the routing method | ☐ | /5 |
| 4 | Read an address plan | ☐ | /4 |
| 5 | Predict `show vlan brief` | ☐ | |
| 6 | Fix the switch configuration | ☐ | /6 |
| 7 | Fix the router configuration | ☐ | /3 |
| 8 | Diagnose from evidence | ☐ | /5 |
| 9 | Fix the address plan | ☐ | |
| 10 | Wrong VLAN, wrong neighbours | ☐ | |
| 11 | Segmentation model | ☐ | |
| 12 | Address-plan checker | ☐ | |
| 13 | Router-on-a-stick | ☐ | |
| 14 | Layer-3 switch | ☐ | |
| 15 | The right check for the question | ☐ | |
| 16 | **Official Task 1** — Two isolated VLANs | ☐ | |
| 17 | **Official Task 2** — Two physical router links | ☐ | |
| 18 | **Official Task 3** — Access-port fault | ☐ | |
| 19 | Mini-project: community centre | ☐ | |
| 20 | Assessment-style practice | ☐ | /20 |

## Reflection

1. Which of the three routing methods felt easiest to configure, and which would you choose for your own home lab? Why?
2. In Task 18, the PC's settings were perfect but it still failed. What does that teach you about troubleshooting?
3. Which verification command gave you the most useful information, and why?
4. What would you add to the router to make the Guest VLAN in Task 19 genuinely safe?

---

## Answer key

**(Verified)** = Python 3.13 (`ipaddress`, `segment_sim.py`, `plan_check.py`). **(Expected)** = Packet Tracer and Cisco IOS; not run here.

### Task 1 (Verified)

a local · b routed · c local · d routed · e routed · f local · g routed · h local (**wrongly**). In h, PC4's /16 makes it treat 10.10.10.11 as local, so it ARPs for it in VLAN 120, gets no answer and never uses its gateway: the ping fails.

### Task 2

1. PC3 and PC5. 2. PC1 → PC2 works; PC3 → PC5 works; PC1 → PC3 fails (different VLANs, no router). 3. **Two**. 4. Its neighbours would be PC1 and PC2 (VLAN 110). It could not reach PC3: its ARP stays in VLAN 110, and with no router, nothing connects the VLANs.

### Task 3

a separate physical interfaces (port and cable per VLAN) · b Layer-3 switch (cost/complexity; switch is critical) · c router-on-a-stick (shared link, single point of failure) · d separate physical interfaces (official design) · e router-on-a-stick or a Layer-3 switch (ten VLANs cannot each have a router port).

### Task 4

1. Any of 10.10.10.2–10.10.10.9: inside the reserved range, so DHCP will never hand it out. 2. .100–.199 = **100** each. 3. 10.10.30.0/24, gateway 10.10.30.1 (reserved .1–.9, pool .100–.199). 4. Anyone can work out a device's VLAN from its address (and vice versa), which speeds up troubleshooting and avoids mistakes.

### Task 5 (Expected)

`default` (VLAN 1): Fa0/6–Fa0/24, Gi0/1, Gi0/2 · `RECEPTION` (110): Fa0/1, Fa0/2 · `WORKSHOP` (120): Fa0/3, Fa0/4, Fa0/5.

### Task 6

(1) `configure terminal` at `Switch>`: `enable` missing. (2) VLAN **120 never created** (`vlan 120`, `name WORKSHOP`, `exit`). (3) Fa0/1–2 missing `switchport mode access`. (4) Fa0/3–5 put in VLAN **210** instead of 120. (5) Fa0/23 is in VLAN 120 but serves G0/0 (VLAN 110). (6) Fa0/24 is in VLAN 110 but serves G0/1 (VLAN 120). Corrected: official Task 1.2–1.3 and 2.2.

### Task 7

(1) G0/0 mask 255.255.**0.0** (should be /24): `show ip route` shows 10.10.0.0/16 as connected on G0/0, which overlaps 10.10.20.0/24. (2) G0/0 has **no `no shutdown`**: `show ip interface brief` shows it administratively down, so VLAN 110 hosts cannot reach their gateway. (3) G0/1 is **10.10.20.254**, but the VLAN 120 PCs use gateway 10.10.20.1: their ARP for .1 gets no answer. Result: no inter-VLAN ping works; VLAN 120 PCs cannot reach any gateway; within each VLAN, pings still work.

### Task 8 (each Verified with `segment_sim.py`)

A: PC4's port in the wrong VLAN → `show vlan brief` → `switchport access vlan 120` on Fa0/4. B: G0/1 shut down → `show ip interface brief` → `no shutdown` on G0/1. C: PC3 has no gateway → `ipconfig` on PC3 → set gateway 10.10.20.1 (the request reaches PC3, the reply cannot leave). D: PC2's gateway is 10.10.20.1 (not on its network) → `ipconfig` → set 10.10.10.1. E: router-facing Fa0/24 in VLAN 110 → `show vlan brief` → `switchport access vlan 120` on Fa0/24.

### Task 9 (Verified)

`plan_check.py` reports 8 problems: the /16 overlaps both other subnets (2); VLAN 110's pool .1–.50 overlaps the reserved .1–.9 and its gateway; VLAN 120's gateway 10.10.30.1 is outside its reserved range (and belongs to the Guest pattern); VLAN 120's pool has 21 addresses for 40 hosts; VLAN 130's pool .10–.40 runs past the /27's usable range (.1–.30); VLAN 130's pool has 31 addresses for 50 hosts; the /27 has only 30 usable addresses for 50 hosts. A corrected plan: 110 → 10.10.10.0/24, gw .1, reserved .1–.9, pool .100–.199; 120 → 10.10.20.0/24, gw .1, reserved .1–.9, pool .100–.199; 130 → 10.10.30.0/24, gw .1, reserved .1–.9, pool .100–.199.

### Task 10 (model Verified; Packet Tracer Expected)

Step 1: G0/0 is now in VLAN 120, so VLAN 110's ARP for 10.10.10.1 gets no answer: PC1 cannot reach its gateway or PC3. Step 2: PC4 → PC1 fails (PC4 ARPs for 10.10.10.11 inside VLAN 120); PC4 → PC5 still works. Fastest checks: `show vlan brief` for step 1; `ipconfig` on PC4 for step 2.

### Task 11 (Verified)

As stated in the expected result. Case C: the request **does** reach PC3 ("PC3 received the request"); the reply fails because PC3 has no default gateway for the remote 10.10.10.11.

### Task 12 (Verified)

Step 3: 8 problems (listed in Task 9). Step 5 model addition (inside the `if d["pool"]:` block):

```python
            if p1 <= gw <= p2:
                problems.append(f"VLAN {v}: gateway {gw} is inside the DHCP pool")
```

### Tasks 13–15 (Expected)

Task 13: `show ip route` → `C 10.10.10.0/24 is directly connected, GigabitEthernet0/0.110` and `C 10.10.20.0/24 … GigabitEthernet0/0.120`; `show interfaces trunk` lists Fa0/23 trunking with VLANs including 110 and 120. Task 14: 0 router ports and 0 inter-device links for routing (all inside the 3560), compared with 2 links/2 ports (Task 17) and 1 link/1 port (Task 13). Task 15: questions as in lecture section 12; G0/1's MAC appears in VLAN 120 on Fa0/24 because that access port is in VLAN 120 and G0/1 sent frames through it.

### Tasks 16–18 (Expected)

Use the test plans. Task 18, 3.3 (model): the fault occurred because the switch, not the PC, decides a frame's VLAN; with Fa0/3 in VLAN 110, PC3's ARP for 10.10.20.1 never reached G0/1. This design uses one router port and one switch port per VLAN (the 2911 runs out quickly) and each link is a single point of failure for its VLAN; router-on-a-stick needs one port but makes the trunk a single point of failure for every VLAN; a Layer-3 switch needs no router ports but makes the switch critical.

### Task 19 (model points)

VLANs 110 Reception, 120 Workshop, 130 Guest, 140 Staff, each 10.10.<VLAN-100>.0/24 following the pattern (e.g. 130 → 10.10.30.0/24, 140 → 10.10.40.0/24), gateway .1, reserved .1–.9, pools for Guest and Reception. Method: **router-on-a-stick** (four VLANs, two ports, room for growth) or a Layer-3 switch if budget allows. Security: without ACLs the router will route guests to staff; an ACL (or firewall) must deny Guest → Staff and allow only what guests need (e.g. internet access).

### Task 20 (model points)

(a) Lecture section 6. (b) Section 8. (c) Section 9.4. (d) Sections 7.3, 12 and 15.
