# Lab 13 — Wireless Networks Hands-on Workbook (20 Tasks)

**Module:** 4301COMP Computer Systems Architecture

**Session:** Teaching Week 08, Session A · **Matching lecture:** `../Lectures/Lecture-13-Wireless-Networks.md`

---

## How to use this lab

**What this lab is for.** You will:

- encode and decode bits with NRZ and Manchester;
- generate and recover ASK, FSK and PSK signals;
- calculate wavelengths and data-rate limits;
- read the details of your own Wi-Fi connection;
- build a secured, multi-cell WLAN in Packet Tracer;
- answer the official guided worksheet.

**Where the official tasks are.** This week's official sheet is a **guided lecture worksheet** with 12 questions. It is ungraded and needs no wireless adapter, Packet Tracer, internet access or administrator rights (official sheet).

| Official worksheet (TW08 Session A) | This workbook |
| --- | --- |
| Section 1, questions 1–4: Wireless communication | Task 16 |
| Section 2, questions 5–8: Wireless LANs and security | Task 17 |
| Section 3, questions 9–12: Encoding and signal transmission | Task 18 |

The official sheet says to answer **using only the Week 08 Session A lecture slides**, in your own words.

**Tools**

| Tool | Used in | Notes |
| --- | --- | --- |
| Pen and paper | Tasks 1–10 | Draw waveforms by hand first |
| Python 3 | Tasks 11–13 | **Optional, your choice.** Built-in modules only |
| Windows Command Prompt | Task 14 | Read-only `netsh wlan show` commands on your own laptop |
| Cisco Packet Tracer 9.0 | Tasks 15, 19 | Optional build tasks |

**Rule:** always **state the convention** you use for NRZ, Manchester, ASK and BPSK (slides 9, 10, 26 and 27).

**Labels:**

- **Verified** = run before being written here (Python 3.13).
- **Expected** = not run here (Windows `netsh`, Packet Tracer).

---

## Part A — Warm-up: encode, decode, calculate (Tasks 1–5)

### Task 1 — Benefit or challenge?

**Goal:** sort the statements using slides 5–6.

Label each statement **B** (benefit) or **C** (challenge). For each challenge, add one effect a user would notice.

1. Users can carry laptops between rooms and stay connected.
2. A microwave oven near the router slows the connection.
3. Signals can be received from the car park.
4. Hundreds of phones in a lecture theatre compete for airtime.
5. No need to drill through a listed building's walls.
6. A video call stutters because frames are being retransmitted.
7. A pop-up event network was working within an hour.
8. The signal is weak behind a concrete stairwell.

**Expected result:** 3 benefits, 5 challenges.

- **Hint 1:** Slide 5 lists benefits; slide 6 lists challenges.
- **Hint 2:** "Signals extend beyond the building" is a challenge, because of security.

---

### Task 2 — Encode by hand

**Goal:** draw NRZ-L and Manchester correctly.

**Conventions:**

- NRZ-L: **1 = high, 0 = low**.
- Manchester: **IEEE**, so 0 = high-to-low and 1 = low-to-high.

For each bit string:

1. Write the Manchester signal as half-bit pairs (`10` = high then low).
2. Write the NRZ-L signal the same way.
3. Count the transitions in each.
4. Give the longest flat stretch, in bit periods.

| Bits | NRZ-L pairs | Manchester pairs | NRZ transitions | Manchester transitions |
| --- | --- | --- | --- | --- |
| 10110010 | | | | |
| 00001111 | | | | |
| 01010101 | | | | |

**Expected result:** Manchester always has a mid-bit change. For 01010101, Manchester has **fewer** transitions than for 00001111 (Verified).

- **Hint 1:** In Manchester, a boundary transition appears only between two **equal** bits.
- **Hint 2:** Check with `line_codes.py` (Task 11).

---

### Task 3 — Decode Manchester

**Goal:** read a received Manchester signal.

A receiver records these half-bit levels (1 = high, 0 = low):

```text
01 10 10 01 01 10
```

1. Decode it using the **IEEE** convention.
2. Decode it using the **G. E. Thomas** convention.
3. What is the relationship between the two answers?
4. A second signal arrives: `01 11 10`. What can you say about the second bit?

**Expected result:** IEEE 100110, Thomas 011001; the second signal is invalid (Verified).

- **Hint 1:** Only the **direction** of the mid-bit change matters.
- **Hint 2:** `11` has no mid-bit change.

---

### Task 4 — Name the modulation

**Goal:** recognise ASK, FSK and PSK.

For each description, name the method and the property that carries the data.

1. "The wave is tall for some bits and short for others, but always at the same frequency."
2. "The wave's peaks are closer together for 1 than for 0."
3. "For some bits the wave starts going down instead of up; the size and spacing never change."
4. Slide 27's BPSK for **0110**: at which bit boundaries does the phase flip?
5. Slide 26's ASK convention: is a short wave a 0 or a 1?

**Expected result:** ASK, FSK, PSK; flips at the 0→1 and 1→0 boundaries only; 1.

- **Hint 1:** Look at the lecture figure in section 16.2.
- **Hint 2:** Two consecutive 1s keep the same phase (slide 27).

---

### Task 5 — Waves by numbers

**Goal:** use T = 1/f and λ = c/f (slide 23), with c = 3 × 10⁸ m/s.

Show your working for each.

1. The period of a 2.4 GHz carrier.
2. The wavelength of a 2.4 GHz carrier, in cm.
3. The wavelength of a 5 GHz carrier, in cm.
4. A wave has period 0.5 ns. What is its frequency?
5. The wavelength of a 900 MHz mobile signal.
6. A student measures the "wavelength" on a graph whose horizontal axis is time. What have they actually measured?

**Expected result:** 0.417 ns; 12.5 cm; 6 cm; 2 GHz; 33.3 cm; the period (Verified).

- **Hint 1:** 1 GHz = 10⁹ Hz; 1 ns = 10⁻⁹ s.
- **Hint 2:** Slide 23: wavelength is measured in space.

---

## Part B — Find and fix (Tasks 6–10)

### Task 6 — Fix Sam's encodings

**Goal:** spot encoding errors.

Sam Archer encoded **00110101** and stated: "NRZ-L 1 = high; Manchester IEEE". His half-bit pairs:

```text
NRZ-L:       00 00 10 10 00 10 00 10
Manchester:  01 01 10 10 01 10 01 10
```

1. What did Sam do wrong in the NRZ-L line? What is that kind of signal called?
2. What did Sam do wrong in the Manchester line?
3. Write the correct versions.

**Expected result:**

- NRZ-L: `00 00 11 11 00 11 00 11`.
- Manchester (IEEE): `10 10 01 01 10 01 10 01` (Verified).

- **Hint 1:** NRZ means "non-return-to-zero".
- **Hint 2:** Compare Sam's Manchester line with the G. E. Thomas convention.

---

### Task 7 — Fix the claims

**Goal:** correct misconceptions using the slides.

Each statement is wrong. Correct it and name the slide that shows why.

1. "5 GHz Wi-Fi is faster because 5 is bigger than 2.4."
2. "Our WLAN uses spread spectrum, so we don't need a password."
3. "Infrared Wi-Fi would cover the whole floor through the walls."
4. "In an ad hoc network, the access point forwards traffic between laptops."
5. "Modern switched Ethernet uses CSMA/CD to handle collisions."
6. "The access point is the laptop's default gateway."
7. "Token Ring is a good choice for a new office LAN."

**Expected result:** seven corrections with slide numbers.

- **Hint 1:** Slides 7, 14, 15, 19, 21 and 22.
- **Hint 2:** For 6: what does an AP **bridge** to?

---

### Task 8 — Fix the WLAN design

**Goal:** apply slides 16–18 and 22.

Sam's design for a three-floor library:

- One access point on the ground floor, set to maximum power.
- SSID "Library", **open** (no password) "so visitors can join easily".
- Staff PCs and visitors on the same WLAN and subnet.
- A second AP added later on floor 3 with SSID "Library2" on the **same channel** as the first.

Find **five** problems and propose a fixed design.

**Expected result:** coverage, security, separation, roaming (SSID) and channel problems identified.

- **Hint 1:** Roaming needs overlapping cells with the **same** SSID (slide 18).
- **Hint 2:** Slide 22 for security; Lecture 9 for separating visitors from staff.

---

### Task 9 — The inverted message

**Goal:** see why ASK conventions matter.

A transmitter used **slide 26's convention** (1 = lower amplitude). The received amplitudes for five bits were:

```text
high, low, low, high, low
```

1. Decode the bits using slide 26's convention.
2. A receiver wrongly assumes "1 = higher amplitude". What does it decode?
3. How could two devices make sure they agree on the convention?

**Expected result:** 01101 with the slide's convention; 10010 with the wrong one (Verified with `modulation.py`).

- **Hint 1:** A convention mismatch inverts every bit.
- **Hint 2:** Standards define conventions so that devices from different makers agree.

---

### Task 10 — Which convention was used?

**Goal:** use meaning to work out an unknown convention.

A Manchester signal carrying one ASCII character arrives:

```text
10 01 01 10 10 10 01 01
```

1. Decode it with the IEEE convention and convert it to a character (the ASCII code 0x63 is `c`).
2. Decode it with the Thomas convention. Is the result a printable ASCII character (0x20–0x7E)?
3. Which convention was most likely used?

**Expected result:** IEEE gives 01100011 = 0x63 = `c`; Thomas gives 10011100 = 0x9C, which is not printable (Verified).

- **Hint 1:** Split the 8 bits into two groups of 4 to get the hex digits.
- **Hint 2:** Next session (binary and decimal) practises these conversions.

---

## Part C — Build and observe (Tasks 11–15)

### Task 11 — A line-code tool

**Goal:** encode, draw and decode NRZ-L and Manchester automatically.

**Skill you gain:** you can turn a written protocol rule into working code and use it to check hand calculations. This is how engineers test protocol implementations.

1. Save as `line_codes.py`:

```python
# line_codes.py - encode bits with NRZ-L and Manchester, draw them, count transitions, decode them.
# Conventions MUST be stated (slides 9 and 10). This script uses:
#   NRZ-L:      1 = high level, 0 = low level, for the whole bit period
#   Manchester: IEEE 802.3 convention - 0 = high-to-low in mid-bit, 1 = low-to-high in mid-bit
#               (set CONVENTION = "thomas" for the opposite, G. E. Thomas, convention)
#
# Usage: python line_codes.py 11101000
#        python line_codes.py 1111111100000000

import sys

CONVENTION = "ieee"           # or "thomas"


def nrz_l(bits):
    """Two half-bit samples per bit, so it lines up with Manchester. 1 = high (1), 0 = low (0)."""
    return [int(b) for b in bits for _ in range(2)]


def manchester(bits, convention=CONVENTION):
    out = []
    for b in bits:
        if (b == "1") == (convention == "ieee"):
            out += [0, 1]          # low then high: a rising edge in the middle
        else:
            out += [1, 0]          # high then low: a falling edge in the middle
    return out


def decode_manchester(levels, convention=CONVENTION):
    bits = ""
    for i in range(0, len(levels), 2):
        rising = levels[i] == 0 and levels[i + 1] == 1
        falling = levels[i] == 1 and levels[i + 1] == 0
        if not (rising or falling):
            return None                                  # no mid-bit transition: invalid
        bits += "1" if rising == (convention == "ieee") else "0"
    return bits


def transitions(levels):
    return sum(1 for a, b in zip(levels, levels[1:]) if a != b)


def longest_flat(levels):
    """Longest stretch (in bit periods) with no transition at all."""
    best = run = 1
    for a, b in zip(levels, levels[1:]):
        run = run + 1 if a == b else 1
        best = max(best, run)
    return best / 2


def draw(levels):
    """Draw a waveform with two characters per half-bit: '‾‾' high, '__' low, '|' at a change."""
    top, bottom = "", ""
    for i, v in enumerate(levels):
        edge = i > 0 and levels[i - 1] != v
        top += ("|" if edge else " ") + ("‾‾" if v else "  ")
        bottom += ("|" if edge else " ") + ("  " if v else "__")
    return top, bottom


if __name__ == "__main__":
    bits = sys.argv[1] if len(sys.argv) > 1 else "11101000"
    header = "".join(f" {b}    " for b in bits)
    print(f"bits:        {header}")
    print(f"clock:       {'|‾‾ __' * len(bits)}")
    for name, lv in (("NRZ-L", nrz_l(bits)), (f"Manchester", manchester(bits))):
        top, bottom = draw(lv)
        print(f"{name:<12} {top}")
        print(f"{'':<12} {bottom}")
    for name, lv in (("NRZ-L", nrz_l(bits)), ("Manchester", manchester(bits))):
        print(f"{name:<11} transitions: {transitions(lv):>3}   longest stretch with no transition: "
              f"{longest_flat(lv):g} bit periods")
    m = manchester(bits)
    print(f"Manchester ({CONVENTION} convention) decodes back to: {decode_manchester(m)}")
    print(f"Signal changes per bit: NRZ-L at most 1, Manchester up to 2 -> Manchester needs about twice the bandwidth")
```

2. Run `python line_codes.py 11101000`. *What it does:* prints the clock, the NRZ-L and Manchester waveforms, transition counts and a decode check. Actual output (Verified):

```text
bits:         1     1     1     0     1     0     0     0    
clock:       |‾‾ __|‾‾ __|‾‾ __|‾‾ __|‾‾ __|‾‾ __|‾‾ __|‾‾ __
NRZ-L         ‾‾ ‾‾ ‾‾ ‾‾ ‾‾ ‾‾|     |‾‾ ‾‾|                 
                               |__ __|     |__ __ __ __ __ __
Manchester      |‾‾|  |‾‾|  |‾‾ ‾‾|     |‾‾ ‾‾|  |‾‾|  |‾‾|  
              __|  |__|  |__|     |__ __|     |__|  |__|  |__
NRZ-L       transitions:   3   longest stretch with no transition: 3 bit periods
Manchester  transitions:  12   longest stretch with no transition: 1 bit periods
Manchester (ieee convention) decodes back to: 11101000
Signal changes per bit: NRZ-L at most 1, Manchester up to 2 -> Manchester needs about twice the bandwidth
```

3. Check your Task 2 answers: `python line_codes.py 10110010` and so on.
4. Run `python line_codes.py 1111111100000000`. Compare the longest flat stretches.
5. Set `CONVENTION = "thomas"` and run again. What changes?

**Expected result (step 4, Verified):**

```text
NRZ-L       transitions:   1   longest stretch with no transition: 8 bit periods
Manchester  transitions:  30   longest stretch with no transition: 1 bit periods
Manchester (ieee convention) decodes back to: 1111111100000000
Signal changes per bit: NRZ-L at most 1, Manchester up to 2 -> Manchester needs about twice the bandwidth
```

- **Hint 1:** Each bit is drawn as two half-bit samples.
- **Hint 2:** `decode_manchester` returns `None` for an invalid signal.

---

### Task 12 — Generate and recover ASK, FSK and BPSK

**Goal:** see the three modulation methods and how noise affects them.

**Skill you gain:** you can generate and demodulate digital signals in code. This is the basis of software-defined radio and signal analysis.

1. Save as `modulation.py`:

```python
# modulation.py - carry bits on a carrier wave with ASK, BFSK and BPSK, then recover them.
# Conventions are the ones on the TW08A slides:
#   ASK  (slide 26): 1 = LOWER amplitude, 0 = HIGHER amplitude
#   BFSK (slide 25): two carrier frequencies; here 0 = 1 cycle per bit, 1 = 2 cycles per bit
#   BPSK (slide 27): 0 = reference sine wave, 1 = the inverted (180 degree) sine wave
# It then adds random noise and counts how many bits each method gets wrong.
#
# Usage: python modulation.py 0110
#        python modulation.py 0110 noise          (adds the noise experiment)

import math
import random
import sys

N = 40                                   # samples per bit


def ask(bits):
    return [(0.4 if b == "1" else 1.0) * math.sin(2 * math.pi * 2 * n / N) for b in bits for n in range(N)]


def bfsk(bits):
    return [math.sin(2 * math.pi * (2 if b == "1" else 1) * n / N) for b in bits for n in range(N)]


def bpsk(bits):
    return [(-1 if b == "1" else 1) * math.sin(2 * math.pi * 2 * n / N) for b in bits for n in range(N)]


def correlate(seg, ref):
    return sum(s * r for s, r in zip(seg, ref))


def demodulate(kind, samples, nbits):
    out = ""
    for k in range(nbits):
        seg = samples[k * N:(k + 1) * N]
        ref2 = [math.sin(2 * math.pi * 2 * n / N) for n in range(N)]
        ref1 = [math.sin(2 * math.pi * 1 * n / N) for n in range(N)]
        if kind == "ASK":       # how big is the wave? (energy matched to the carrier)
            size = correlate(seg, ref2) / (N / 2)
            out += "1" if size < 0.7 else "0"
        elif kind == "BFSK":    # which frequency matches better?
            out += "1" if abs(correlate(seg, ref2)) > abs(correlate(seg, ref1)) else "0"
        else:                   # BPSK: in phase (+) or inverted (-)?
            out += "1" if correlate(seg, ref2) < 0 else "0"
    return out


def sketch(samples, nbits, rows=7):
    """Very small text plot, 20 columns per bit."""
    cols = [samples[int(i * N / 20)] for i in range(nbits * 20)]
    lines = []
    for r in range(rows):
        level = 1 - 2 * r / (rows - 1)
        lines.append("".join("*" if abs(v - level) < 1 / (rows - 1) else ("." if abs(level) < 1e-9 else " ")
                             for v in cols))
    return lines


if __name__ == "__main__":
    bits = sys.argv[1] if len(sys.argv) > 1 else "0110"
    print("bits:   " + "".join(f"{b:<20}" for b in bits))
    for name, fn in (("ASK", ask), ("BFSK", bfsk), ("BPSK", bpsk)):
        s = fn(bits)
        print(f"\n{name}  (recovered: {demodulate(name, s, len(bits))})")
        for line in sketch(s, len(bits)):
            print("        " + line)
    if "noise" in sys.argv:
        random.seed(4301)
        test = "".join(random.choice("01") for _ in range(2000))
        print(f"\nNoise experiment: {len(test)} random bits, the same random noise added to each method")
        for sigma in (0.5, 1.0, 1.5):
            row = []
            for name, fn in (("ASK", ask), ("BFSK", bfsk), ("BPSK", bpsk)):
                noisy = [v + random.gauss(0, sigma) for v in fn(test)]
                errors = sum(a != b for a, b in zip(test, demodulate(name, noisy, len(test))))
                row.append(f"{name} {errors:>4} errors")
            print(f"  noise level {sigma}:  " + "   ".join(row))
```

2. Run `python modulation.py 0110 noise`. *What it does:* draws each signal in text, recovers the bits, then runs the noise test. Actual output (Verified):

```text
bits:   0                   1                   1                   0                   

ASK  (recovered: 0110)
          **        **                                                **        **      
         *  *      *  *                                              *  *      *  *     
                             ****      ****      ****      ****                         
        *....*....*....*....*....*....*....*....*....*....*....*....*....*....*....*....
                                  ****      ****      ****      ****                    
              *  *      *  *                                              *  *      *  *
               **        **                                                **        ** 

BFSK  (recovered: 0110)
            ***               **        **        **        **          ***             
          **   **            *  *      *  *      *  *      *  *       **   **           
         *       *                                                   *       *          
        *.........*.........*....*....*....*....*....*....*....*....*.........*.........
                   *       *                                                   *       *
                    **   **       *  *      *  *      *  *      *  *            **   ** 
                      ***          **        **        **        **               ***   

BPSK  (recovered: 0110)
          **        **             **        **        **        **   **        **      
         *  *      *  *           *  *      *  *      *  *      *  * *  *      *  *     
                                                                                        
        *....*....*....*....*....*....*....*....*....*....*....*....*....*....*....*....
                                                                                        
              *  *      *  * *  *      *  *      *  *      *  *           *  *      *  *
               **        **   **        **        **        **             **        ** 

Noise experiment: 2000 random bits, the same random noise added to each method
  noise level 0.5:  ASK   10 errors   BFSK    0 errors   BPSK    0 errors
  noise level 1.0:  ASK  198 errors   BFSK    3 errors   BPSK    0 errors
  noise level 1.5:  ASK  398 errors   BFSK   69 errors   BPSK    4 errors
```

3. Run it with `1001`. Where does the BPSK phase flip?
4. **Extend:** change ASK's "1" amplitude from 0.4 to 0.0 (on-off keying) and rerun the noise test. Does ASK improve? Why?

**Expected result:** in this model, BPSK made the fewest errors. Moving ASK's two amplitudes further apart reduces its errors.

- **Hint 1:** The demodulator compares each bit period with a clean reference wave (correlation).
- **Hint 2:** The further apart two symbols are, the more noise it takes to confuse them.

---

### Task 13 — Wavelength and data-rate calculator

**Goal:** check slide 7's claim with numbers.

**Skill you gain:** you can estimate a channel's theoretical capacity and explain what really limits wireless speed. Network designers use this reasoning when choosing channel widths.

1. Save as `wireless_calc.py`:

```python
# wireless_calc.py - the numbers behind slides 7 and 23.
#   period       T = 1 / f
#   wavelength   lambda = c / f            (c = speed of light, about 3 x 10^8 m/s)
#   Shannon limit  C = B x log2(1 + S/N)   (the maximum error-free data rate for a channel)
# Notice that the carrier frequency f does NOT appear in the Shannon limit: data rate depends
# on channel BANDWIDTH B and signal-to-noise ratio S/N (slide 7), not on the carrier itself.
#
# Usage: python wireless_calc.py

import math

C = 299_792_458                                 # speed of light, m/s


def period_and_wavelength(f_hz):
    return 1 / f_hz, C / f_hz


def shannon(bandwidth_hz, snr_db):
    snr = 10 ** (snr_db / 10)                   # convert decibels to a plain ratio
    return bandwidth_hz * math.log2(1 + snr)


if __name__ == "__main__":
    print("Carrier          Period T        Wavelength")
    for label, f in (("2.4 GHz", 2.4e9), ("5 GHz", 5e9), ("6 GHz", 6e9), ("FM radio 100 MHz", 100e6)):
        T, lam = period_and_wavelength(f)
        print(f"{label:<16} {T * 1e9:8.4f} ns   {lam * 100:8.2f} cm")

    print("\nShannon limit for different channels (the carrier frequency is not in the formula)")
    print("Bandwidth   SNR     Limit")
    for bw_mhz in (20, 40, 80, 160):
        for snr_db in (10, 25):
            print(f"{bw_mhz:>4} MHz  {snr_db:>3} dB  {shannon(bw_mhz * 1e6, snr_db) / 1e6:8.1f} Mbit/s")

    print("\nSame 20 MHz channel and 25 dB SNR at two carriers:")
    for label in ("2.4 GHz", "5 GHz"):
        print(f"  {label}: {shannon(20e6, 25) / 1e6:.1f} Mbit/s  (identical - bandwidth and SNR decide)")
```

2. Run `python wireless_calc.py`. Actual output (Verified):

```text
Carrier          Period T        Wavelength
2.4 GHz            0.4167 ns      12.49 cm
5 GHz              0.2000 ns       6.00 cm
6 GHz              0.1667 ns       5.00 cm
FM radio 100 MHz  10.0000 ns     299.79 cm

Shannon limit for different channels (the carrier frequency is not in the formula)
Bandwidth   SNR     Limit
  20 MHz   10 dB      69.2 Mbit/s
  20 MHz   25 dB     166.2 Mbit/s
  40 MHz   10 dB     138.4 Mbit/s
  40 MHz   25 dB     332.4 Mbit/s
  80 MHz   10 dB     276.8 Mbit/s
  80 MHz   25 dB     664.8 Mbit/s
 160 MHz   10 dB     553.5 Mbit/s
 160 MHz   25 dB    1329.5 Mbit/s

Same 20 MHz channel and 25 dB SNR at two carriers:
  2.4 GHz: 166.2 Mbit/s  (identical - bandwidth and SNR decide)
  5 GHz: 166.2 Mbit/s  (identical - bandwidth and SNR decide)
```

3. Use it to answer: does doubling the channel width (20 → 40 MHz) or improving the SNR from 10 dB to 25 dB give more capacity?
4. Add a 320 MHz channel (used by Wi-Fi 7) at 25 dB. What is the limit?

**Expected result:** doubling the bandwidth doubles the limit; the SNR gain multiplies it by about 2.4; 320 MHz at 25 dB ≈ 2,659 Mbit/s.

- **Hint 1:** `shannon(320e6, 25)`.
- **Hint 2:** Real Wi-Fi rates are lower because of coding and overhead.

---

### Task 14 — Read your own Wi-Fi connection

**Goal:** connect the lecture to your real wireless link.

**Skill you gain:** you can read a device's wireless connection details. This is the first step in wireless troubleshooting and in checking that a network uses strong security.

On **your own Windows laptop**, connected to Wi-Fi (Expected; read-only, no administrator rights needed):

```text
netsh wlan show interfaces
```

*What it does:* shows the details of your current Wi-Fi connection. It changes nothing.

Record:

| Field | Your value | Lecture link |
| --- | --- | --- |
| SSID | | Network name advertised by the AP (slide 18) |
| BSSID | | The MAC address of the AP's radio, so it identifies **which** AP |
| Radio type | | 802.11ax/ac/n: which Wi-Fi generation (section 10.2) |
| Band and Channel | | 2.4, 5 or 6 GHz (slide 7) |
| Authentication | | WPA2-Personal, WPA3, WPA2-Enterprise (slide 22) |
| Cipher | | e.g. CCMP (AES) |
| Signal | | % strength (slide 6) |
| Receive / Transmit rate (Mbps) | | Not the same as internet speed (slide 7) |

Then:

1. Move to another room and run it again. What changed?
2. On campus, walk between two areas. Did the **BSSID** change while the **SSID** stayed the same? That is roaming (slide 18).
3. Is your home network using WPA2 or WPA3? If WPA2, does the router's settings page offer WPA3?

**Expected result:** a completed table. Signal and rates fall with distance; the BSSID changes when you roam.

- **Hint 1:** If the command says no wireless interface, you are on a wired connection or a computer without Wi-Fi. Record that.
- **Hint 2:** Do not share your BSSID or home SSID publicly in your write-up. Crop or blur them.

---

### Task 15 — Build a secured multi-cell WLAN (Packet Tracer)

**Goal:** build slides 16–18 and secure them as slide 22 describes.

**Skill you gain:** you can configure access points with WPA2 and connect wireless clients. This is a core task for any network or security technician.

In a **new** Packet Tracer file (Expected):

1. Place one 2960 switch and two **AccessPoint-PT** devices. Connect each AP's **Port 0** to the switch (Copper Straight-Through). Add a **Server-PT** on the switch with static 192.168.50.10/24 and **DHCP On** (pool start 192.168.50.100, gateway 192.168.50.1).
2. On **AP1 > Config > Port 1**:
   - SSID `Lab13`;
   - Channel **1**;
   - Authentication **WPA2-PSK**;
   - a strong passphrase of your own;
   - Encryption **AES**.
3. Do the same on **AP2**, with the **same** SSID and passphrase but Channel **11**.
4. Add two **Laptop-PT** devices. Power each off and replace its wired card with **WPC300N** (drag the module in **Physical**), then power on. In **Desktop > PC Wireless** (or **Config > Wireless0**), connect to `Lab13` with the passphrase. Set IP to **DHCP**.
5. Test: does each laptop get an address? Can they ping each other and the server?
6. Change one laptop's passphrase to a wrong one. What happens?

**Test plan**

| Test | Expected | Actual |
| --- | --- | --- |
| Laptop 1 associates (dashed line to an AP) | Yes | |
| Laptop 1 gets a DHCP address | 192.168.50.10x | |
| Laptop 1 → Laptop 2 ping | Replies | |
| Wrong passphrase | No association | |

- **Hint 1:** If a laptop shows no dashed line, check the SSID spelling and the passphrase.
- **Hint 2:** The APs bridge to the switch, so the server's DHCP reaches wireless clients without a relay (Lecture 11).

---

## Part D — Official worksheet and integration (Tasks 16–20)

### Task 16 — Wireless communication (Official worksheet, questions 1–4)

**Goal:** answer section 1 of the official worksheet in your own words, using only the Week 08 Session A slides.

1. **Q1.** Describe two benefits of using a wireless connection rather than relying entirely on network cables.
2. **Q2.** Describe two conditions that can make a wireless connection less reliable. How might they affect the user's experience?
3. **Q3.** Why must multiple wireless devices share radio spectrum carefully?
4. **Q4.** A student claims that a higher radio carrier frequency always means a faster network. Using the lecture, explain why this claim is not necessarily correct.

**Expected result:** short, clear answers with examples from slides 5–7.

- **Hint 1:** For Q4, slide 7 lists what data rate actually depends on.
- **Hint 2:** Task 13 gives numbers you can mention.

---

### Task 17 — Wireless LANs and security (Official worksheet, questions 5–8)

**Goal:** answer section 2 of the official worksheet.

1. **Q5.** In an infrastructure wireless LAN, what does an access point do for a connected laptop?
2. **Q6.** What is the purpose of using several access points with overlapping coverage? Explain what happens when a user moves between cells.
3. **Q7.** How does an ad hoc wireless network differ from an infrastructure wireless LAN?
4. **Q8.** Why are authentication and encryption important on a radio-based WLAN? Explain how WPA2 or WPA3 relates to this need.

**Expected result:** answers based on slides 16–19 and 22.

- **Hint 1:** For Q6, Task 14's BSSID observation is real evidence of roaming.
- **Hint 2:** For Q8, slide 6's last bullet explains *why*; slide 22 explains *how*.

---

### Task 18 — Encoding and signal transmission (Official worksheet, questions 9–12)

**Goal:** answer section 3 of the official worksheet.

1. **Q9.** What does NRZ encoding do, and why can a long sequence without signal transitions make timing difficult?
2. **Q10.** What happens in the middle of each bit period with Manchester encoding? Why can that help a receiver?
3. **Q11.** Compare infrared and radio transmission. In particular, consider their behaviour around walls and obstacles.
4. **Q12.** For each of these digital modulation methods, identify the signal property that carries the information: binary ASK, BFSK and BPSK.

**Expected result:** answers based on slides 8–11, 21 and 24–27.

- **Hint 1:** Task 11's "longest flat stretch" output illustrates Q9.
- **Hint 2:** Q12 needs one word each.

When finished, save your responses in your own storage. There is no separate submission unless your tutor says so (official sheet).

---

### Task 19 — Mini-project: a wireless design for a small café-bookshop

**Goal:** design, justify and partly build a small WLAN.

**Skill you gain:** you can turn wireless theory into a justified design with security and testing, the kind of reasoning used in real site surveys.

**Brief.** A two-room café-bookshop with:

- about 30 customers' devices;
- 3 staff tablets and a card terminal;
- a back office whose stock PC is wired.

The owner wants customers to roam between rooms without reconnecting, and to stay away from staff devices.

1. **Access points:** how many, where, and with what cell overlap? Which channels (2.4 GHz: 1, 6, 11; also consider 5 GHz)?
2. **SSIDs and security:** a staff SSID with WPA3 (or WPA2 if needed) and a separate guest SSID. Justify each using slides 6 and 22.
3. **Separation:** how are guests kept away from staff devices? (Use Lecture 9: separate VLANs and subnets, plus filtering at the router.)
4. **Build** a simplified version in Packet Tracer: two APs, one SSID roaming test, WPA2-PSK, DHCP. Run a test plan of at least 6 rows.
5. **Explain** in 150 words why spread spectrum or "hiding the SSID" is not a substitute for WPA2/WPA3.

**Test plan (start)**

| # | Test | Expected | Actual |
| --- | --- | --- | --- |
| 1 | Laptop joins the guest SSID with the passphrase | Associates; gets a guest address | |
| 2 | Wrong passphrase | No association | |
| | | | |

- **Hint 1:** Neighbouring APs should use different channels.
- **Hint 2:** A guest VLAN and its own subnet make the separation testable.

---

### Task 20 — Assessment-style practice: wireless and signals

**This is practice only, not a real exam question.** The module exam is two hours with short-answer and essay-style questions covering architecture, operating systems and networking (module guide). Marks are invented for planning.

**Rules:** 25 minutes, closed book, write it yourself.

**(a)** Encode **10011010** using NRZ-L (1 = high) and Manchester (IEEE: 0 = high-to-low, 1 = low-to-high). Draw both and state which helps clock recovery, and why. *(5 marks)*

**(b)** Explain the difference between infrastructure and ad hoc wireless networks. *(3 marks)*

**(c)** Explain how ASK, FSK and PSK carry data. *(4 marks)*

**(d)** A company wants Wi-Fi across a three-floor office, with visitors kept away from staff systems. Discuss the design, covering access points and roaming, carrier frequency and data rate, and security. *(8 marks; aim for 250–350 words)*

**Self-marking checklist**

| Part | A good answer includes | Expected | Actual |
| --- | --- | --- | --- |
| (a) | NRZ-L pairs `11 00 00 11 11 00 11 00`; Manchester pairs `01 10 10 01 01 10 01 10`; conventions stated; mid-bit transitions aid clock recovery | 5 points | |
| (b) | AP associates, bridges and authenticates vs direct device-to-device | 3 points | |
| (c) | Amplitude / frequency / phase; conventions; examples | 4 points | |
| (d) | Overlapping cells, same SSID, different channels; data rate depends on bandwidth/SNR/modulation, not just frequency; WPA3/WPA2; separate guest SSID/VLAN; spread spectrum is not security | 8 points | |
| Time | Within 25 minutes | Yes | |

- **Hint 1:** Check (a) with `line_codes.py 10011010`.
- **Hint 2:** Lecture sections 8, 9, 11–14 and 16.

---

## Tracker

| Task | Name | Done | Notes / score |
| --- | --- | --- | --- |
| 1 | Benefit or challenge? | ☐ | /8 |
| 2 | Encode by hand | ☐ | /3 |
| 3 | Decode Manchester | ☐ | /4 |
| 4 | Name the modulation | ☐ | /5 |
| 5 | Waves by numbers | ☐ | /6 |
| 6 | Fix Sam's encodings | ☐ | /2 |
| 7 | Fix the claims | ☐ | /7 |
| 8 | Fix the WLAN design | ☐ | /5 |
| 9 | The inverted message | ☐ | /3 |
| 10 | Which convention? | ☐ | /3 |
| 11 | `line_codes.py` | ☐ | |
| 12 | `modulation.py` | ☐ | |
| 13 | `wireless_calc.py` | ☐ | |
| 14 | Your own Wi-Fi | ☐ | |
| 15 | Packet Tracer WLAN | ☐ | |
| 16 | **Official** worksheet Q1–4 | ☐ | |
| 17 | **Official** worksheet Q5–8 | ☐ | |
| 18 | **Official** worksheet Q9–12 | ☐ | |
| 19 | Mini-project: café-bookshop | ☐ | |
| 20 | Assessment-style practice | ☐ | /20 |

## Reflection

1. Why do you think the slides insist on stating conventions? Where did a convention change your answer in this lab?
2. What did your own `netsh wlan show interfaces` output tell you that surprised you?
3. Which modulation method would you choose for a very noisy environment, and why?
4. In one sentence, explain to a friend why a hidden SSID is not real security.

---

## Answer key

**(Verified)** = Python 3.13 (`line_codes.py`, `modulation.py`, `wireless_calc.py`). **(Expected)** = Windows `netsh`, Packet Tracer.

### Task 1

- **Benefits:** 1, 5 and 7.
- **Challenges:**
  - 2: interference, so the connection is slower;
  - 3: signal leakage, so outsiders could listen or try to join;
  - 4: shared airtime, so it feels slow despite a good signal;
  - 6: retransmissions add delay;
  - 8: obstacles weaken the signal, so the connection drops or slows.

### Task 2 (Verified)

| Bits | NRZ-L pairs | Manchester pairs (IEEE) | NRZ transitions | Manchester transitions | Longest flat (NRZ / Manchester) |
| --- | --- | --- | --- | --- | --- |
| 10110010 | 11 00 11 11 00 00 11 00 | 01 10 01 01 10 10 01 10 | 5 | 10 | 2 / 1 |
| 00001111 | 00 00 00 00 11 11 11 11 | 10 10 10 10 01 01 01 01 | 1 | 14 | 4 / 1 |
| 01010101 | 00 11 00 11 00 11 00 11 | 10 01 10 01 10 01 10 01 | 7 | 8 | 1 / 1 |

### Task 3 (Verified)

1. IEEE: **100110**.
2. Thomas: **011001**.
3. Each answer is the other with every bit inverted.
4. `11` has no mid-bit transition, so the second bit is **invalid**.

### Task 4

1. ASK.
2. FSK.
3. PSK.
4. The phase flips at the 0→1 boundary (between bits 1 and 2) and the 1→0 boundary (between bits 3 and 4), but not between the two 1s.
5. 1.

### Task 5 (Verified)

1. T = 1 / (2.4 × 10⁹) = **0.417 ns**.
2. λ = 3 × 10⁸ / 2.4 × 10⁹ = 0.125 m = **12.5 cm**.
3. λ = 3 × 10⁸ / 5 × 10⁹ = 0.06 m = **6 cm**.
4. f = 1 / (0.5 × 10⁻⁹) = **2 GHz**.
5. λ = 3 × 10⁸ / 9 × 10⁸ = **0.333 m** (33.3 cm).
6. They have measured the **period**: a time, not a distance.

### Task 6 (Verified)

1. Sam returned to low in the second half of every 1: that is **return-to-zero (RZ)**, not NRZ. The correct NRZ-L is `00 00 11 11 00 11 00 11`.
2. Sam used the **Thomas** convention while stating IEEE. The correct IEEE Manchester is `10 10 01 01 10 01 10 01`.

### Task 7

1. **Slide 7:** speed depends on bandwidth, SNR, modulation and so on. 5 GHz is often faster because wider channels are available there.
2. **Slides 20 and 22:** spread spectrum is not security. Use WPA2/WPA3.
3. **Slide 21:** infrared does not normally pass through walls.
4. **Slide 19:** ad hoc devices talk directly, with no AP.
5. **Slide 14:** full-duplex switched links have no collisions, and CSMA/CD is not used.
6. **Slide 17:** the AP bridges to the distribution network. The gateway is a router.
7. **Slide 15:** Token Ring is legacy.

### Task 8

1. One AP cannot cover three floors. Add APs per floor with overlapping cells (slide 18).
2. The network is open, so there is no authentication or encryption. Use WPA3/WPA2 (slide 22).
3. Staff and visitors share a subnet. Use separate SSIDs, VLANs and subnets with filtering (Lecture 9).
4. Using a different SSID breaks roaming. Use the **same** SSID across APs (slide 18).
5. Using the same channel causes interference. Use different non-overlapping channels.

Maximum power everywhere also causes overlap and interference; plan the cells instead.

### Task 9 (Verified)

1. **01101**.
2. **10010**: every bit is inverted.
3. Both devices follow the same standard, which defines the convention.

### Task 10 (Verified)

1. IEEE gives **01100011** = 0x63 = `c`.
2. Thomas gives 10011100 = 0x9C, which is **not** printable ASCII.
3. **IEEE** was most likely used.

### Task 11 (Verified)

The output is as shown. With `thomas`, the Manchester pairs invert; the transition counts are unchanged.

### Task 12 (Verified)

- Step 2: output as shown.
- Step 3, for 1001: the phase flips at the 1→0 boundary (between bits 1 and 2) and at the 0→1 boundary (between bits 3 and 4).
- Step 4: with amplitude 0.0 for a 1, the two ASK symbols are further apart, so there are fewer errors. In this model ASK still does worse than BPSK. If you lower the "1" amplitude, also lower the decision threshold in `demodulate()` (`size < 0.7`) to halfway between the two amplitudes.

### Task 13 (Verified)

- 20 MHz, 10 dB → 69.2 Mbit/s; 40 MHz → 138.4 (×2); 20 MHz at 25 dB → 166.2 (×2.4).
- 320 MHz at 25 dB ≈ 2,659 Mbit/s.

### Tasks 14–15 (Expected)

The results are your own. The BSSID changes when you roam; with a wrong passphrase there is no association.

### Tasks 16–18 (official worksheet, model points)

- **Q1–4:** slides 5–7 and lecture sections 6–8.
- **Q5–8:** slides 16–19 and 22, and lecture sections 11–14.
- **Q9–12:** slides 8–11, 21 and 24–27, and lecture sections 9, 14 and 16.
- **Q12:** ASK = amplitude; BFSK = frequency; BPSK = phase.

### Tasks 19–20 (model points)

Use the self-marking checklist. Check Task 20(a) with `line_codes.py 10011010`.
