---
name: freq-band
description: Map a frequency in MHz to amateur band and wavelength. Use when the operator asks what band a frequency is, wavelength, or 14.230 / 146.52 etc.
user-invocable: true
---

# Frequency to band

When given a frequency, treat MHz unless they say kHz or Hz.

US amateur ranges (approx, for identification only — not a privilege check):

160m  1.800–2.000
80m   3.500–4.000
60m   5.330–5.406 (channels)
40m   7.000–7.300
30m   10.100–10.150
20m   14.000–14.350
17m   18.068–18.168
15m   21.000–21.450
12m   24.890–24.990
10m   28.000–29.700
6m    50.000–54.000
2m    144.000–148.000
1.25m 222.000–225.000
70cm  420.000–450.000
33cm  902.000–928.000
23cm  1240–1300

Wavelength meters ≈ 300 / freq_MHz.

Reply: band, range, wavelength. Example: 14.230 → 20m, USB-typical, ~21 m.

If it is outside these ranges, say so. Do not invent a band. Do not say they are allowed to transmit — that is ham-license.
