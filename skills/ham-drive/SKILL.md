---
name: ham-drive
description: Build a phone-friendly VHF/UHF road-trip radio card from a route or city. Use when the user says drive mode, road trip, mobile, highway repeaters, travel radio plan, or /drive.
user-invocable: true
metadata:
 openclaw:
 emoji: "🚗"
 requires:
 bins: ["curl"]
author: Dominic Tanner (KI5WTR / dtan81)
---

# ham-drive — road-trip radio copilot

Build a one-screen mobile plan. Do not write essays. Do not key a radio. Do not invent CTCSS/DCS tones, offsets, or talkgroups. If a lookup is weak, say UNKNOWN and give simplex instead.

## Inputs to collect (ask only what is missing)

- Start and end (city, highway, or grid). Optional waypoints.
- Vehicle radio — HT vs mobile, bands (default 2m + 70cm FM).
- Modes they actually have — FM always; DMR / Fusion / D-Star only if they said so.
- License class if known from memory.
- Date/time of departure if given; else assume departing soon.

Prefer station memory (callsign, class, typical HT/mobile) over re-asking.

## Research order

1. Resolve the route into 3–6 waypoints (start, major cities / passes / summits, end).
2. For each waypoint look up open analog FM repeaters (2m first, then 70cm) from RepeaterBook or another live directory. Search `site:repeaterbook.com` plus city/state.
3. Prefer repeaters marked open / on-air, with a published tone, on a high site or known wide-area machine.
4. Skip closed, off-air, coordination-unknown, and tourist machines with no tone listed unless they are the only option.
5. Note mountain passes, long desert stretches, and canyons as "simplex or APRS only" segments.
6. US APRS voice/data calling is 144.390 MHz (North America). National 2m simplex calling is 146.520. 70cm simplex calling is 446.000.
7. If ham-aprs or aprs.fi is available, mention 1–2 digis/igates near the route. Do not dump a map.
8. Optional weather one-liner if storms or winter passes are relevant (lightning, snow, high wind).

Never fabricate a tone. Never recommend transmitting outside the user's license privileges.

## Output format (strict)

Use this shape. Keep the whole reply short enough to read at a stoplight.

```
🚗 DRIVE — [start] → [end]
Radio [HT/mobile] · [bands] · [FM/DMR/...]

NATIONAL
- 2m call 146.520
- 70cm call 446.000
- APRS 144.390 (NA)

[SEGMENT 1 — place / highway]
- 146.xxx − 123.0 CALL city (note)
- 447.xxx + 100.0 CALL city
- Simplex if none: 146.520

[SEGMENT 2 — ...]

DEAD ZONES
- [pass/canyon/desert] — expect nothing; drop a voice mail on 146.52 or beacon APRS

WATCH
- [weather / fire / winter pass / event traffic]

73
```

Rules for the list
- Max 3 repeaters per segment.
- Frequency, offset or +/−, tone, callsign, city. One short note only (wide coverage, linked, EchoLink, etc).
- Sort by "would actually hit from a car" not by database distance.
- If DMR was requested, add one talkgroup line per segment only when the source lists it. Otherwise say "FM only for this card."

## Follow-ups you should offer (one line)

After the card, offer at most one of
- CHIRP-style memory list (freq, duplex, offset, tone, name)
- "next 80 miles only" refresh
- APRS buddy overlay if they have a watchlist

## Safety

- No auto-transmit. No DTMF strings unless the user asked for a specific machine's documented code and you found it on the trustee/RepeaterBook page.
- Do not tell them to talk on 146.52 in a city if a busy repeater is the better play — list both.
- If they are driving, remind them once that programming the radio happens parked.

**Credit:** Created by Dominic Tanner (KI5WTR / dtan81)
