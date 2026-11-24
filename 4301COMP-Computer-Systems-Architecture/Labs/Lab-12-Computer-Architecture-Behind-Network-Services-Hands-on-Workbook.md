# Lab 12 — Computer Architecture Behind Network Services Hands-on Workbook (20 Tasks)

**Module:** 4301COMP Computer Systems Architecture

**Session:** Teaching Week 06, Session B · **Matching lecture:** `../Lectures/Lecture-12-Computer-Architecture-Behind-Network-Services.md`

---

## How to use this lab

**What this lab is for.** You will watch a real browser and a real (tiny) web server working as **processes** on your own computer, link network connections to **PIDs**, prove that the **kernel buffers** data, read the **machine instructions** a CPU runs for network code, and trace one request through every hardware and software component. You will finish by evaluating a prototype network and prioritising improvements.

**Where the official tasks are.**

| Official lab sheet (TW06 Session B) | This workbook |
| --- | --- |
| Task 1 — Observe a browser as a network process | Task 16 |
| Task 2 — Trace the request through hardware and software | Task 17 |
| Extra Challenge — Inspect the network adapter path | Task 18 |

In the timetabled lab, **do Tasks 16–18 first**. This is a practice lab, not your AS1 submission (official sheet).

**Tools**

| Tool | Used in | Notes |
| --- | --- | --- |
| Windows Task Manager, Resource Monitor | Tasks 11, 16 | **Do not** change process settings or elevate privileges (official) |
| Command Prompt (not as administrator) | Tasks 11, 16 | `netstat -ano` |
| PowerShell (normal user) | Task 14 | Read-only commands |
| Device Manager, `msinfo32` | Task 18 | **Read-only**: never update, disable or change anything (official) |
| Microsoft Word | Tasks 16–18 | `TW06B_YourStudentID.docx` |
| Python 3 | Tasks 11–12 | **Optional, your choice.** Built-in modules only |
| Compiler Explorer (godbolt.org) | Task 13 | Free website; nothing to install |
| A Linux system (VM or WSL) | Task 15 | **Optional** |

**Rules:**

- Record only what you can actually see. If a tool is restricted or a PID does not match, **write what you tried and what you observed** instead of fabricating evidence (official).
- Crop screenshots to remove passwords, private information and unrelated activity (official).

**Labels:**

- **Verified** = run before being written here (Linux, Python 3.13, `strace`, `ss`, gcc 13.3).
- **Expected** = not run here (Windows tools, Compiler Explorer).

---

## Part A — Warm-up: who does what? (Tasks 1–5)

### Task 1 — Match the component to its job

**Goal:** know each component's role (slides 5–10).

Match each component (1–8) to one job (A–H).

| # | Component |  | Job |
| --- | --- | --- | --- |
| 1 | Server process | A | Copies a received frame into RAM without the CPU |
| 2 | System call | B | Chooses which runnable thread gets the CPU |
| 3 | NIC | C | Holds a connection's data until the program reads it |
| 4 | DMA | D | Receives the signal and checks the frame |
| 5 | Interrupt | E | The program, with its PID, threads, memory and sockets |
| 6 | Socket buffer | F | Executes instructions through fetch-decode-execute |
| 7 | Scheduler | G | Tells the CPU that new data is waiting |
| 8 | CPU | H | A controlled request for a kernel operation |

**Expected result:** eight unique matches.

- **Hint 1:** Two of them are hardware, one is a signal, the rest are software.
- **Hint 2:** Lecture sections 6–11.

---

### Task 2 — Put the request in order

**Goal:** trace the worked path (slide 11).

Put these server-side stages in order, from frame arrival to the response leaving.

- a) The scheduler context-switches the server thread onto a core
- b) The NIC receives the frame and copies it to RAM by DMA
- c) The server calls `send()` with the response
- d) The kernel's TCP/IP stack places the data in the socket buffer and marks the thread ready
- e) An interrupt makes the CPU run the driver
- f) The server's `recv()` copies the request into its own memory
- g) The CPU executes the server's instructions to build the response
- h) The driver and NIC transmit the response frames

**Expected result:** one order beginning with b and ending with h.

- **Hint 1:** The thread cannot run until it is ready.
- **Hint 2:** Lecture section 12's table.

---

### Task 3 — Predict the process state

**Goal:** apply slide 9.

The tiny web server is running. Give its state (**blocked**, **ready** or **running**) at each moment.

1. Waiting in `accept()` with no visitors.
2. A request has arrived and the kernel has woken the thread, but another program is using the only free core.
3. Building the HTTP response.
4. Has sent the response and called `accept()` again.
5. Using its full time slice on a huge calculation, then made to wait so other threads can run.

**Expected result:** blocked, ready, running, blocked, ready.

- **Hint 1:** "Ready" means "could run, but has not been given a core".
- **Hint 2:** Being pre-empted moves a thread to ready, not to blocked.

---

### Task 4 — Read a real system-call trace

**Goal:** connect slide 6 to real output.

This is the real `strace` output for the tiny server handling one request (Verified):

```text
socket(AF_INET, SOCK_STREAM|SOCK_CLOEXEC, IPPROTO_IP) = 3
setsockopt(3, SOL_SOCKET, SO_REUSEADDR, [1], 4) = 0
bind(3, {sa_family=AF_INET, sin_port=htons(8080), sin_addr=inet_addr("127.0.0.1")}, 16) = 0
listen(3, 5)                      = 0
accept4(3, {sa_family=AF_INET, sin_port=htons(55970), sin_addr=inet_addr("127.0.0.1")}, [16], SOCK_CLOEXEC) = 4
recvfrom(4, "GET / HTTP/1.1\r\nHost: 127.0.0.1:"..., 4096, 0, NULL, NULL) = 77
sendto(4, "HTTP/1.0 200 OK\r\nContent-Type: t"..., 110, 0, NULL, 0) = 110
close(4)                          = 0
close(3)                          = 0
+++ exited with 0 +++
```

1. Which call created the socket, and what number did the kernel return?
2. Which call **waited** for a visitor? What did it return, and why is this a different number?
3. How many bytes was the request? The response?
4. Which two calls cross the user/kernel boundary to move the actual HTTP data?
5. Why does `close` appear twice?

**Expected result:** descriptor 3 for listening, 4 for the connection; 77 and 110 bytes.

- **Hint 1:** The number after `=` is the return value.
- **Hint 2:** One socket listens; another is created for each connection.

---

### Task 5 — Assign the responsibility

**Goal:** answer slide 13's knowledge check, plus three more.

1. Which buffer can temporarily hold data from an arriving packet?
2. Who selects a runnable thread to receive CPU time?
3. How does an application request a protected kernel service?
4. Which hardware executes the instructions that generate a response?
5. Which software knows how to talk to one particular model of network card?
6. Where does a new connection wait if the server has not yet called `accept()`?
7. Which Windows tool shows the PID that owns each connection?
8. Write **three sentences** explaining how the components in 1–4 work together for one request (event → components → purpose).

**Expected result:** short answers plus a connected explanation (slide 12).

- **Hint 1:** Lecture section 14's table.
- **Hint 2:** Section 13.2's strong paragraph is a model.

---

## Part B — Find and fix (Tasks 6–10)

### Task 6 — Fix the myths

**Goal:** correct common misunderstandings.

Each statement is wrong. Rewrite it correctly and give the evidence from the lecture.

1. "The browser sends data by writing directly to the network card."
2. "If the web server is busy, incoming requests are lost."
3. "Every packet causes exactly one interrupt."
4. "A web server waiting for visitors uses a lot of CPU."
5. "The first browser process in Task Manager owns all of the browser's connections."
6. "If `msinfo32` shows no IRQ for the adapter, it does not use interrupts."

**Expected result:** six corrected statements with evidence.

- **Hint 1:** Statement 6 is answered on the official lab sheet itself.
- **Hint 2:** Lecture sections 6, 8, 9 and 10.

---

### Task 7 — Turn definitions into an explanation

**Goal:** apply slide 12's key rule.

Sam Archer wrote:

> "A process is a program in execution. A system call is a request to the OS. A NIC is a network card. An interrupt is a signal. The CPU uses fetch-decode-execute."

Rewrite it as **one connected paragraph** (100–150 words) about a specific event: *the kiosk server receiving a visitor's GET request.* Use slide 12's three steps.

**Expected result:** your paragraph names the event, the component at each stage, and why each action is needed.

- **Hint 1:** Use linking words: "because", "so that", "when", "which then".
- **Hint 2:** Check every component in Sam's list appears in your paragraph, in the order it acts.

---

### Task 8 — Fix the evidence column

**Goal:** apply the official Task 2 rule: cite a screenshot only when it supports the statement.

A student's trace table:

| Stage | Component | Evidence |
| --- | --- | --- |
| Sending | Browser process | Task Manager screenshot: msedge.exe PID 6120 |
| Sending | System call | Screenshot of `send()` being called |
| Sending | Kernel network stack | `netstat -ano` row: TCP 192.168.1.20:52114 → 151.101.x.x:443 ESTABLISHED, PID 6120 |
| Receiving | NIC | Device Manager: adapter name |
| Receiving | Interrupt | `msinfo32` IRQ screenshot proves an interrupt for every packet |
| Receiving | Buffer | Task Manager working set shows the packet in the buffer |
| Processing | Scheduler | Task Manager shows the scheduler choosing msedge.exe |
| Processing | CPU | Task Manager CPU time increased after refresh |

Find the rows where the evidence does **not** support the statement, and rewrite them using "conceptual – not directly visible" or "not available with this student account" where appropriate.

**Expected result:** four rows corrected (system call, interrupt, buffer, scheduler).

- **Hint 1:** Can Task Manager or `netstat` show an individual system call?
- **Hint 2:** The official sheet: "these tools do not show every system call or packet interrupt."

---

### Task 9 — Read who owns the connection

**Goal:** interpret real connection-to-process evidence.

The tiny server was **stopped** (so it could not run), then a client connected. Linux's `ss -tnp`, the equivalent of `netstat -ano`, showed (Verified):

```text
State Recv-Q Send-Q Local Address:Port  Peer Address:Port Process  
ESTAB 0  0  127.0.0.1:34160  127.0.0.1:8080  users:(("curl",pid=2525,fd=5))
ESTAB 77  0  127.0.0.1:8080  127.0.0.1:34160  
LISTEN 1  5  127.0.0.1:8080  0.0.0.0:*  users:(("python3",pid=2519,fd=3))
```

A student concluded:

1. "The `curl` process (PID 2525) is the server."
2. "The second ESTAB row has no process, so the connection is broken."
3. "The 77 in Recv-Q means 77 connections are waiting."
4. "LISTEN 1 means one byte is waiting."

Correct each conclusion.

**Expected result:** four corrections. The un-owned row is a connection the kernel accepted on the server's behalf, not yet taken by `accept()`.

- **Hint 1:** Look at which side uses port 8080.
- **Hint 2:** Recv-Q means bytes for an ESTAB socket, and queued connections for a LISTEN socket.

---

### Task 10 — Fix the improvement plan

**Goal:** apply slides 14–15.

For the kiosk prototype (requirement: up to 60 visitors on busy days; the information page must stay available), Sam proposed:

1. "Buy a faster router, because faster is better."
2. "Add a firewall, because security is important."
3. "Enlarge the DHCP pool."
4. "Use HTTPS."

Rewrite the plan so that **each** item names:

- the limitation it fixes;
- the improvement;
- why it has this priority.

Put the items in a justified order.

**Expected result:** the pool first (hard failure above 25 visitors, Verified in Lecture 11); then separation or filtering, and a second server or backup for availability, with reasons; HTTPS justified by a stated risk.

- **Hint 1:** Slide 15's decision rule.
- **Hint 2:** Which limitation stops most users from using the service **at all**?

---

## Part C — Build and observe (Tasks 11–15)

### Task 11 — Watch your own server as a process

**Goal:** see a network service's PID, threads and connections on your own computer.

**Skill you gain:** you can identify which process owns a listening port or connection. This is basic triage in support and security work.

1. Save as `tiny_server.py`:

```python
# tiny_server.py - a minimal web server that narrates each operating-system request it makes.
# Every socket method below is a thin wrapper around a SYSTEM CALL into the kernel.
# Run it, then open http://127.0.0.1:8080 in a browser (or use curl). Stop with Ctrl+C.
#
# Usage: python tiny_server.py            (serves forever)
#        python tiny_server.py 2          (serves 2 requests, then exits)

import os
import socket
import sys
import threading
import time

PAGE = b"<html><body><h1>Tiny server</h1></body></html>"
start = time.perf_counter()


def log(step, detail=""):
    t = (time.perf_counter() - start) * 1000
    print(f"[{t:9.1f} ms] PID {os.getpid()} threads {threading.active_count()}  {step:<28} {detail}", flush=True)


def main(limit=None):
    log("start", "the OS has created this process")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # system call: socket
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    log("socket()", "kernel created a TCP socket")
    s.bind(("127.0.0.1", 8080))                                  # system call: bind
    log("bind()", "claimed port 8080")
    s.listen(5)                                                  # system call: listen
    log("listen()", "kernel will queue up to 5 waiting connections")
    served = 0
    while limit is None or served < limit:
        log("accept() ...", "BLOCKED: waiting, using no CPU")
        conn, addr = s.accept()                                  # system call: accept (blocks)
        log("accept() returned", f"client {addr[0]}:{addr[1]} - thread is runnable again")
        request = conn.recv(4096)                                # system call: recv (copies from kernel buffer)
        first = request.split(b"\r\n", 1)[0].decode(errors="replace")
        log("recv()", f"{len(request)} bytes from the kernel buffer: {first!r}")
        reply = (b"HTTP/1.0 200 OK\r\nContent-Type: text/html\r\nContent-Length: "
                 + str(len(PAGE)).encode() + b"\r\n\r\n" + PAGE)
        conn.sendall(reply)                                      # system call: send (copies into kernel buffer)
        log("send()", f"{len(reply)} bytes handed to the kernel to transmit")
        conn.close()                                             # system call: close
        log("close()", "connection finished")
        served += 1
    s.close()
    log("exit", f"served {served} request(s)")


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else None)
```

2. In a Command Prompt: `python tiny_server.py`. *What it does:* starts a web server **on your own computer only** (127.0.0.1:8080) and prints each system call it makes. Note the PID it prints.
3. In a browser, open `http://127.0.0.1:8080` and refresh twice. Watch the log.
4. In a second Command Prompt: `netstat -ano | findstr 8080`. *What it does:* lists connections involving port 8080 with their PIDs. Find the **LISTENING** row: does its PID match the log?
5. In **Task Manager > Details**, find that PID (python.exe). Record Threads, CPU time and Working set.
6. Stop the server with **Ctrl+C**.

Real output on Linux, two requests from `curl` (Verified):

```text
[      0.0 ms] PID 2402 threads 1  start                        the OS has created this process
[      0.1 ms] PID 2402 threads 1  socket()                     kernel created a TCP socket
[      0.1 ms] PID 2402 threads 1  bind()                       claimed port 8080
[      0.1 ms] PID 2402 threads 1  listen()                     kernel will queue up to 5 waiting connections
[      0.1 ms] PID 2402 threads 1  accept() ...                 BLOCKED: waiting, using no CPU
[    712.1 ms] PID 2402 threads 1  accept() returned            client 127.0.0.1:44276 - thread is runnable again
[    712.2 ms] PID 2402 threads 1  recv()                       77 bytes from the kernel buffer: 'GET / HTTP/1.1'
[    712.2 ms] PID 2402 threads 1  send()                       110 bytes handed to the kernel to transmit
[    712.2 ms] PID 2402 threads 1  close()                      connection finished
[    712.2 ms] PID 2402 threads 1  accept() ...                 BLOCKED: waiting, using no CPU
[   1024.7 ms] PID 2402 threads 1  accept() returned            client 127.0.0.1:44282 - thread is runnable again
[   1024.8 ms] PID 2402 threads 1  recv()                       77 bytes from the kernel buffer: 'GET / HTTP/1.1'
[   1024.9 ms] PID 2402 threads 1  send()                       110 bytes handed to the kernel to transmit
[   1024.9 ms] PID 2402 threads 1  close()                      connection finished
[   1024.9 ms] PID 2402 threads 1  exit                         served 2 request(s)
```

**Expected result:** the `netstat` LISTENING PID matches the server's printed PID. The CPU time barely changes, because the server is blocked almost all the time.

- **Hint 1:** If port 8080 is in use, change both 8080s in the script to 8090.
- **Hint 2:** The time gap before each "accept() returned" is time spent **blocked**.

---

### Task 12 — Prove the kernel buffers data

**Goal:** see slide 8 happen.

**Skill you gain:** you can show, with a reproducible experiment, how the OS decouples network timing from program timing. This is the basis for understanding back-pressure and denial-of-service.

1. Save as `buffer_demo.py`:

```python
# buffer_demo.py - show that the KERNEL buffers network data while the application is not reading.
# The "server" accepts a connection, then deliberately does nothing for a few seconds
# (as if it were not scheduled on the CPU). The client sends five messages straight away.
# The messages wait in the kernel's receive buffer; when the server finally calls recv(),
# they are all already there.
#
# Usage: python buffer_demo.py

import socket
import threading
import time

PAUSE = 3          # seconds the server "is not running"
start = time.perf_counter()


def t():
    return f"{(time.perf_counter() - start):5.2f} s"


def server(ready):
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("127.0.0.1", 8081))
    s.listen(1)
    ready.set()
    conn, _ = s.accept()
    print(f"{t()}  server: connection accepted, now NOT reading for {PAUSE} s")
    time.sleep(PAUSE)                                    # the server is blocked/not scheduled
    print(f"{t()}  server: calls recv() for the first time")
    data = b""
    conn.settimeout(0.5)
    try:
        while True:
            chunk = conn.recv(4096)
            if not chunk:
                break
            data += chunk
    except socket.timeout:
        pass
    print(f"{t()}  server: received {len(data)} bytes in one go: {data.decode()!r}")
    conn.close()
    s.close()


ready = threading.Event()
th = threading.Thread(target=server, args=(ready,))
th.start()
ready.wait()
c = socket.create_connection(("127.0.0.1", 8081))
for i in range(1, 6):
    c.sendall(f"msg{i};".encode())
    print(f"{t()}  client: sent msg{i} (send() returned at once - the kernel holds the data)")
c.close()
th.join()
```

2. Run `python buffer_demo.py`. *What it does:* runs a client and a server inside one program on 127.0.0.1; nothing leaves your computer. Actual output (Verified):

```text
 0.01 s  server: connection accepted, now NOT reading for 3 s
 0.01 s  client: sent msg1 (send() returned at once - the kernel holds the data)
 0.01 s  client: sent msg2 (send() returned at once - the kernel holds the data)
 0.01 s  client: sent msg3 (send() returned at once - the kernel holds the data)
 0.01 s  client: sent msg4 (send() returned at once - the kernel holds the data)
 0.01 s  client: sent msg5 (send() returned at once - the kernel holds the data)
 3.01 s  server: calls recv() for the first time
 3.01 s  server: received 25 bytes in one go: 'msg1;msg2;msg3;msg4;msg5;'
```

3. Change `PAUSE` to 6 and run again. Does the client still finish at once?
4. **Extend:** replace the `for` loop with one big send, `c.sendall(b"x" * 20_000_000)` (20 MB). Keep `PAUSE = 3`, and print the time just before and just after the send. Does the client finish at once now? Explain using "buffers are finite" (slide 8). (Try 2 MB first: on many systems it still fits in the buffers.)

**Expected result:** steps 2–3: the client finishes almost instantly. Step 4 with 20 MB: `sendall()` does not return until **after** the server starts reading. 2 MB fitted in the buffers on the test machine (Verified).

- **Hint 1:** Each `send()` returns as soon as the kernel has accepted the data, not when the server reads it.
- **Hint 2:** For step 4, print the time just before and just after `sendall()`.

---

### Task 13 — Read the CPU's instructions for network code

**Goal:** connect slide 10 to real machine code.

**Skill you gain:** you can read basic x86-64 assembly and relate it to the fetch-decode-execute cycle and to performance. This is a foundation for reverse engineering and exploit analysis.

1. Go to **godbolt.org** (Compiler Explorer) and choose **C** with **x86-64 gcc**. Paste:

   ```c
   unsigned int sum_bytes(const unsigned char *buf, int len)
   {
       unsigned int total = 0;
       for (int i = 0; i < len; i++)
           total += buf[i];
       return total;
   }
   ```

2. In the compiler options box, type `-O1`. Find the **loop**: the instructions between the label and the conditional jump back to it.
3. Fill in an FDE table for each loop instruction: what is fetched, what the control unit decodes, what the ALU or memory does.
4. Change the options to `-O0`, then `-O3`. Count the instructions in the loop each time. What is different about `-O3`?

Real gcc 13.3 `-O1` output (Verified):

```text
0000000000000000 <sum_bytes>:
   0:	f3 0f 1e fa          	endbr64
   4:	85 f6                	test   %esi,%esi
   6:	7e 1f                	jle    27 <sum_bytes+0x27>
   8:	48 89 f8             	mov    %rdi,%rax
   b:	48 63 f6             	movslq %esi,%rsi
   e:	48 01 f7             	add    %rsi,%rdi
  11:	ba 00 00 00 00       	mov    $0x0,%edx
  16:	0f b6 08             	movzbl (%rax),%ecx
  19:	01 ca                	add    %ecx,%edx
  1b:	48 83 c0 01          	add    $0x1,%rax
  1f:	48 39 f8             	cmp    %rdi,%rax
  22:	75 f2                	jne    16 <sum_bytes+0x16>
  24:	89 d0                	mov    %edx,%eax
  26:	c3                   	ret
  27:	ba 00 00 00 00       	mov    $0x0,%edx
  2c:	eb f6                	jmp    24 <sum_bytes+0x24>
```

**Expected result:**

- `-O1`: a 5-instruction loop. Total instructions = 9 + 5n, so 7,509 for 1,500 bytes (Verified).
- `-O0`: an 11-instruction loop that keeps the variables in memory, not registers (Verified).
- `-O3`: many more instructions, using `xmm` registers that add 16 bytes at a time (SIMD) (Verified).

Compiler Explorer may use a different gcc version, so the details can vary.

- **Hint 1:** `jne` jumps back while the comparison is "not equal".
- **Hint 2:** Registers are faster than memory: more memory accesses per byte means a slower loop.

---

### Task 14 — Link connections to processes with PowerShell

**Goal:** produce a connection-to-process list that `netstat -ano` cannot give you in one step.

**Skill you gain:** you can produce an evidence table of which program is talking to which remote address. Analysts use this to spot unexpected programs talking to the internet.

In **PowerShell (normal user)** (Expected; read-only):

```powershell
Get-NetTCPConnection -State Established |
  Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, OwningProcess,
    @{Name='Process'; Expression={(Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue).ProcessName}} |
  Sort-Object Process | Format-Table -AutoSize
```

*What it does:* lists your established TCP connections and adds the name of the process that owns each one. It changes nothing.

1. Run it with a browser open. Which processes have connections? Which remote ports (443, 80) do they use?
2. Pick one browser row: does the PID match one in Task Manager **Details**?
3. Is there any process you do not recognise? Search its name **before** drawing conclusions. Many system processes make legitimate connections.

**Expected result:** a table of established connections with process names; browser connections mostly to port 443.

- **Hint 1:** QUIC (HTTP/3) uses **UDP**, so some browser traffic will not appear in a TCP list (official lab Task 1 note).
- **Hint 2:** `Get-NetUDPEndpoint` lists UDP endpoints.

---

### Task 15 — Count real interrupts and system calls (optional, Linux)

**Goal:** observe slide 7's interrupts and slide 6's system calls directly.

**Skill you gain:** you can measure kernel activity with `/proc` counters and `strace`, the standard Linux tools for performance and security analysis.

**Only with a Linux system.** Both parts are read-only.

1. Save as `irq_watch.sh`:

```bash
#!/bin/bash
# irq_watch.sh - count NIC interrupts, received packets and NET_RX soft-interrupts around one web request.
NIC=eth0
DEV=$(basename $(readlink -f /sys/class/net/$NIC/device))           # e.g. virtio7
irq() { grep -E "$DEV-input" /proc/interrupts | awk '{s=0; for(i=2;i<NF-2;i++) s+=$i; print s}'; }
pk()  { cat /sys/class/net/$NIC/statistics/rx_packets; }
sirq(){ grep NET_RX /proc/softirqs | awk '{s=0; for(i=2;i<=NF;i++) s+=$i; print s}'; }
i1=$(irq); p1=$(pk); s1=$(sirq)
curl -s -o /dev/null "$1"
i2=$(irq); p2=$(pk); s2=$(sirq)
echo "driver: $(basename $(readlink /sys/class/net/$NIC/device/driver))   device: $DEV"
echo "packets received:           $((p2-p1))"
echo "NIC receive interrupts:     $((i2-i1))"
echo "NET_RX soft-interrupt runs: $((s2-s1))"
```

2. Run `bash irq_watch.sh https://www.ljmu.ac.uk/`. *What it does:* reads kernel counters before and after one download. On WSL or some VMs the device name may differ; if it shows nothing, run `cat /proc/interrupts` and look for your network device.

   Actual output (Verified, virtual machine):

   ```text
   driver: virtio_net   device: virtio7
   packets received:           18
   NIC receive interrupts:     12
   NET_RX soft-interrupt runs: 24
   ```

3. Trace the tiny server's system calls: `strace -f -e trace=network,close python3 tiny_server.py 1`, then in another terminal `curl http://127.0.0.1:8080/`. Compare with Task 4.

**Expected result:** fewer interrupts than packets (polling), and the same call sequence as Task 4.

- **Hint 1:** `strace` may need installing (`sudo apt install strace`). If you would rather not install it, use the trace in Task 4.
- **Hint 2:** Other background traffic makes the counts approximate.

---

## Part D — Official tasks and integration (Tasks 16–20)

### Task 16 — Observe a browser as a network process (Official Task 1)

**Goal:** link a real browser connection to its process, using only normal-user tools.

**Official steps**

1. **1.1:** Create **TW06B_YourStudentID.docx**. Press **Ctrl+Shift+Esc** to open **Task Manager** > **Details** (expand the left menu if needed). Right-click a column heading > **Select columns** and tick **PID**, **Threads**, **CPU time** and **Working set (memory)**. If a column is unavailable, record that fact. **Do not alter any process settings.**
2. **1.2:** Open a browser, visit a public university web page and refresh it. Press **Windows+R**, type `resmon` and press **Enter**.
   - If **Resource Monitor** opens, choose **Network**, find a browser process showing activity and record its **PID**.
   - If Windows asks for administrator approval, select **Cancel** and use Task Manager instead. Do not attempt to elevate privileges.
3. **1.3:** In **Task Manager > Details**, find that PID and record the process name, thread count, CPU time and working set. If Resource Monitor is unavailable, choose a browser PID from Task Manager **and say so**. Browsers use multiple processes; do not assume the first browser entry owns the network connection.
4. **1.4:** Open **Command Prompt** normally (**Windows+R** > `cmd` > **Enter**; not as administrator) and run `netstat -ano`.
   - Look for the selected browser PID in the final column. Record the protocol, local and remote endpoints, and the TCP state if shown.
   - Refresh the browser and try once more if necessary.
   - A connection may use another PID or **UDP/QUIC**. If there is no match, record *"no matching browser PID observed"*. UDP entries have no TCP state.
5. **1.5:** Add labelled screenshots of the information you can access: **Task Manager** and, where available, **Resource Monitor** and **netstat**. For a restricted tool or a missing PID match, write what you tried and what you observed. Crop screenshots to avoid passwords, private information or unrelated activity.

**Record**

| Item | Value or "not available" |
| --- | --- |
| Browser process name | |
| PID (and where you found it) | |
| Threads | |
| CPU time | |
| Working set | |
| `netstat -ano` row(s) for that PID | |
| Protocol / state | |
| Limitations encountered | |

- **Hint 1:** `netstat -ano | findstr <PID>` filters the output to one PID.
- **Hint 2:** Task 14 gives the same information with process names in one table.

---

### Task 17 — Trace the request through hardware and software (Official Task 2)

**Goal:** produce the official 10-row trace table, with honest evidence.

**Official steps**

1. **2.1:** In Word, insert a table with **3 columns and 10 rows**, with headings **Stage**, **Component**, **Evidence**. Use the nine remaining rows for:
   - browser process
   - system call
   - kernel network stack
   - driver
   - NIC
   - interrupt/polling
   - buffer
   - scheduler
   - CPU

   For **Stage**, identify the part of the request–response activity (such as sending, receiving or processing). For **Component**, name the item involved.
2. **2.2:** In **Evidence**, cite an actual screenshot **only** when it supports the statement. Otherwise write *"conceptual – not directly visible"* or *"not available with this student account"*. Example of the format (not a network answer): Stage = input; Component = keyboard; Evidence = a character appears on screen.
3. **2.3:** Save **TW06B_YourStudentID.docx** with the table, the available screenshots and any access limitations. Check readability and labels.

**Template**

| Stage | Component | Evidence |
| --- | --- | --- |
| | Browser process | |
| | System call | |
| | Kernel network stack | |
| | Driver | |
| | NIC | |
| | Interrupt/polling | |
| | Buffer | |
| | Scheduler | |
| | CPU | |

- **Hint 1:** Only some rows can have screenshot evidence from normal-user tools. Task 8 shows which.
- **Hint 2:** Lecture section 12's table gives the stage and purpose for each component.

---

### Task 18 — Inspect the network adapter path (Official Extra Challenge)

**Goal:** see the NIC and driver your computer actually uses, read-only.

**Official steps**

1. **E.1:** Optional and read-only. Press **Windows+R**, enter `devmgmt.msc` and press **Enter**. Under **Network adapters**, inspect **General** and **Driver** for the active adapter. **Do not update, disable or change anything.** If Windows asks for administrator approval or blocks access, select **Cancel** and use **Windows+R** > `msinfo32` > **Components** > **Network** > **Adapter** instead. Record only the information available to your account.
2. **E.2:** If available, inspect **msinfo32** > **Hardware Resources** > **IRQs** for the adapter or controller. If nothing is listed, record *"not shown"*. This does not prove interrupts are unused: modern devices may not show a simple IRQ mapping. Do not enter BIOS/firmware or change device settings.
3. **E.3:** Include one available, read-only screenshot and **2–3 sentences** explaining how the NIC, driver, buffers and interrupts or polling relate to incoming browser data. State **one limitation** of what you could observe: these tools do not show every system call or packet interrupt.

**Record**

| Item | Value or "not shown" |
| --- | --- |
| Adapter name | |
| Driver provider and version | |
| IRQ(s) listed | |
| Limitation | |

For comparison, the Linux machine used for the lecture reported driver `virtio_net` (a virtual NIC) and separate interrupt lines for its receive and transmit queues (Verified).

- **Hint 1:** Many modern adapters use **MSI/MSI-X** interrupts, which may show as large or negative IRQ numbers, or not at all.
- **Hint 2:** Lecture section 8 explains polling.

---

### Task 19 — Mini-project: evaluate and improve a prototype

**Goal:** apply slides 14–15 to a network you built.

**Skill you gain:** you can evaluate a technical design against requirements and justify a prioritised improvement. This is the reasoning examiners and employers look for.

Choose **one** prototype you built: the Lab 9 segmented network, the Lab 10 routed network with a server, or the Lab 11 kiosk.

1. **Requirements:** write three realistic requirements (for example, number of users, availability of a service, separation of visitors from staff).
2. **Limitations:** find at least **one** limitation in **each** of slide 14's four categories, with evidence (a test result, a pool size, a single device).
3. **Improvements:** for each limitation, propose one improvement from slide 15 (security, reliability, scalability).
4. **Priority:** order the improvements and justify the order with slide 15's decision rule.
5. **Implement the top improvement** in a copy of your Packet Tracer file. Re-run your earlier test plan, plus new tests that prove the improvement. Record regressions (Lecture 10).
6. **Explain** in 150–200 words, using slide 12's event → components → purpose style for at least one technical point.

**Evaluation table**

| Limitation (slide 14 category) | Evidence | Improvement (slide 15 area) | Priority and reason |
| --- | --- | --- | --- |
| | | | |

- **Hint 1:** "Single devices create points of failure": which device, if removed, stops everything?
- **Hint 2:** A justified priority links back to a **stated requirement**.

---

### Task 20 — Assessment-style practice: a request inside the server

**This is practice only, not a real exam question.** The module exam is two hours with short-answer and essay-style questions covering architecture, operating systems and networking (module guide). Marks are invented for planning.

**Rules:** 25 minutes, closed book, write it yourself.

**(a)** Explain what a system call is and give two examples used by a web server. *(3 marks)*

**(b)** Explain the roles of the NIC, driver and interrupts when a packet arrives. *(4 marks)*

**(c)** Explain why kernel buffers are needed and state one cost or risk of buffering. *(3 marks)*

**(d)** Trace an HTTP request from its arrival at a server to the response leaving, explaining how the scheduler, process states and the fetch-decode-execute cycle are involved. Connect the components rather than listing definitions. *(10 marks; aim for 300–400 words)*

**Self-marking checklist**

| Part | A good answer includes | Expected | Actual |
| --- | --- | --- | --- |
| (a) | User mode → controlled kernel operation; validated; e.g. `accept`, `recv`, `send` | 3 points | |
| (b) | NIC receives and checks the frame and uses DMA; interrupt (or polling) alerts the CPU; driver passes the data to the stack | 4 points | |
| (c) | Data arrives while the app is not running; holds data until `recv`; uses memory or can be flooded | 3 points | |
| (d) | Ordered path; blocked → ready → running; context switch; system calls; CPU FDE for response code; send path out; connected explanation | 10 points | |
| Time | Within 25 minutes | Yes | |

- **Hint 1:** Use lecture section 13.2's paragraph as a model, but write your own.
- **Hint 2:** Real evidence such as "the stopped server still had 77 bytes waiting" makes an answer stronger.

---

## Tracker

| Task | Name | Done | Notes / score |
| --- | --- | --- | --- |
| 1 | Match the component | ☐ | /8 |
| 2 | Put the request in order | ☐ | |
| 3 | Predict the process state | ☐ | /5 |
| 4 | Read a real trace | ☐ | /5 |
| 5 | Assign the responsibility | ☐ | /8 |
| 6 | Fix the myths | ☐ | /6 |
| 7 | Definitions to explanation | ☐ | |
| 8 | Fix the evidence column | ☐ | /4 |
| 9 | Who owns the connection | ☐ | /4 |
| 10 | Fix the improvement plan | ☐ | |
| 11 | Your own server as a process | ☐ | |
| 12 | Kernel buffering | ☐ | |
| 13 | CPU instructions | ☐ | |
| 14 | Connections to processes | ☐ | |
| 15 | Interrupts and system calls (optional) | ☐ | |
| 16 | **Official Task 1**: Browser as a process | ☐ | |
| 17 | **Official Task 2**: Trace table | ☐ | |
| 18 | **Official Extra Challenge**: Adapter path | ☐ | |
| 19 | Mini-project: evaluate and improve | ☐ | |
| 20 | Assessment-style practice | ☐ | /20 |

## Reflection

1. Which part of the request's journey was easiest to see with real tools, and which was hardest? Why?
2. What surprised you about how much time a server process spends blocked?
3. How would you explain to a non-technical person why a website can still receive your request while the server program is busy?
4. Which improvement in Task 19 would you defend first in front of a client, and what evidence supports it?

---

## Answer key

**(Verified)** = Linux, Python 3.13, `strace`, `ss`, gcc 13.3, `/proc`. **(Expected)** = Windows tools, Compiler Explorer.

### Task 1

1-E · 2-H · 3-D · 4-A · 5-G · 6-C · 7-B · 8-F

### Task 2

b → e → d → a → f → g → c → h

### Task 3

1. Blocked
2. Ready
3. Running
4. Blocked
5. Ready (pre-empted)

### Task 4 (Verified)

1. `socket()` created the socket and returned **3**.
2. `accept4()` waited for a visitor. It returned **4**, a **new** descriptor for this connection. Descriptor 3 keeps listening.
3. The request was **77** bytes and the response **110** bytes.
4. `recvfrom` and `sendto`.
5. One `close` for the connection (4) and one for the listening socket (3).

### Task 5

1. NIC ring buffer, then the socket receive buffer.
2. The scheduler.
3. A system call.
4. The CPU.
5. The driver.
6. The kernel's accept queue (Verified: `LISTEN 1`).
7. `netstat -ano`, or Resource Monitor's Network tab.
8. Use the event → components → purpose structure.

### Task 6

1. The browser makes system calls; the kernel and driver use the NIC (Verified trace).
2. The kernel buffers requests, up to a limit (Verified: Recv-Q 77 with the server stopped).
3. Drivers often handle several packets per interrupt (Verified: about 12 interrupts for 18 packets).
4. A waiting server is blocked and uses no CPU (Verified: state S; CPU time barely changes).
5. Browsers use many processes; match the PID in `netstat`.
6. The official sheet: "This does not prove interrupts are unused".

### Task 7

Model: lecture section 13.2.

### Task 8

**System call:** "conceptual – not directly visible" (Windows normal-user tools do not show individual calls; `strace` on Linux can).

**Interrupt:** IRQ information shows the device's interrupt line, not an interrupt per packet. Write "IRQ listed: … (does not show each packet's interrupt)" or "not shown".

**Buffer:** "conceptual – not directly visible". The working set is the process's memory, not the kernel's socket buffer.

**Scheduler:** "conceptual – not directly visible". Task Manager shows CPU time, not scheduling decisions.

The browser, kernel-stack (`netstat`), NIC and CPU-time rows are acceptable **if** the screenshots exist.

### Task 9 (Verified)

1. `curl` is the **client**: its local port is 34160 and it connects **to** 8080. The server is `python3`, PID 2519.
2. The connection is complete: the kernel finished the handshake. It has no owning process yet because the stopped server has not called `accept()`.
3. For an ESTAB socket, Recv-Q 77 means **77 bytes** waiting to be read.
4. For a LISTEN socket, Recv-Q 1 means **one connection** waiting in the accept queue.

### Task 10

1. **Pool first.** Limitation: only 25 addresses for 60 visitors (a hard failure). Improvement: enlarge the pool. Highest priority, because most visitors otherwise get nothing.
2. **Availability.** Limitation: one router and one server are single points of failure. Improvement: a backup server or monitored recovery.
3. **Security.** Limitation: visitors share the server's network with no filtering. Improvement: a separate VLAN plus filtering. Its priority depends on the stated risk.
4. **HTTPS.** Justified if visitors enter or receive sensitive information. Otherwise it is lower priority.

"Faster router" has no identified limitation, so it is dropped.

### Task 11 (Verified on Linux; Windows Expected)

The log is as shown. The LISTENING PID matches. The CPU time stays near zero.

### Task 12 (Verified)

- Steps 2–3: the client finishes at about 0.01 s whatever the pause.
- Step 4, real run:

  ```text
   0.01 s  client: starting sendall of 20,000,000 bytes
   0.03 s  server: connection accepted, now NOT reading for 3 s
   3.03 s  server: calls recv() for the first time
   6.07 s  client: sendall returned
   7.23 s  server: received 20000000 bytes
  ```

  The client was held until about 6 s, after the server began reading at 3 s, because the buffers filled. 2 MB was accepted at once, which shows that the buffers are large but **finite**.

### Task 13 (Verified with gcc 13.3)

- `-O1`: 5-instruction loop; 9 + 5n.
- `-O0`: 11-instruction loop with memory operands such as `-0x4(%rbp)`.
- `-O3`: 132 instructions in total, 51 of them SIMD instructions using `xmm` registers (vectorised).

### Task 14 (Expected)

The results are your own. Browser connections are mostly to 443.

### Task 15 (Verified on a VM)

As shown. Fewer interrupts than packets; the same system calls as Task 4.

### Tasks 16–18 (Expected)

The results are your own. Record limitations honestly.

### Tasks 19–20 (model points)

Use the self-marking checklist and lecture sections 6–16.
