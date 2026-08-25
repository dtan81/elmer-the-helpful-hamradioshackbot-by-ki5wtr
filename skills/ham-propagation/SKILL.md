---
name: ham-propagation
description: Real-time HF/VHF band conditions, solar indices, MUF, grayline, and operating recommendations for amateur radio.
---

# Ham Radio Propagation

Use this skill whenever the user asks about band conditions, propagation, solar weather, MUF, K-index, SFI, grayline, openings, or “what bands are open.”

Rules:
- Always fetch the latest data. Never invent current numbers.
- Prefer these sources (in order): NOAA SWPC, N0NBH, hamqsl.com, PSKReporter, DXMaps, QRZ propagation tools, spaceweather.com.
- Report the time of the data in UTC.
- Ask for the user’s grid square or approximate location if unknown and it matters for path recommendations.
- Give practical advice: best bands right now, mode suggestions (CW/SSB/FT8), power notes, and time-of-day considerations.

Typical workflow:
1. Get current solar indices (SFI, A-index, K-index, X-ray flux, sunspot number).
2. Check band-by-band conditions (160m–6m and optionally 2m).
3. Note any special conditions (grayline, TEP, aurora, sporadic-E, etc.).
4. Recommend specific bands/modes for the user’s goals (DX, local, digital, etc.).
5. Keep the response concise and operator-friendly.