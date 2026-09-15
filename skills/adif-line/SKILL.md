---
name: adif-line
description: Build one ADIF QSO record from fields the operator provides. Use when they ask for ADIF, a log line, or export a contact.
user-invocable: true
---

# One ADIF record

Need at least: their call, other station call, band or freq, mode, date, time.

Use only values they gave. If date/time missing, use shack-time (UTC) and say you used now. Do not invent RST, name, or grid.

Template:

<qso_date:8>YYYYMMDD <time_on:4>HHMM <call:N>THEIRCALL <band:N>20m <mode:N>SSB <rst_sent:2>59 <rst_rcvd:2>59 <eor>

Adjust the :N length to the real field length. One record only unless they ask for more.

Do not upload to QRZ, Club Log, or LoTW unless they have a separate skill for that.
