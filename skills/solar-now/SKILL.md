---
name: solar-now
description: Fetch current solar indices (SFI, A, K, sunspots) from hamqsl XML. Use when the operator asks solar conditions, SFI, K-index, or a short band snapshot.
user-invocable: true
---

# Solar now

Run:

python3 {baseDir}/scripts/solar.py

Report those fields only. If the script prints FETCH_FAILED or PARSE_FAILED, say the source is down. Do not invent SFI, A, or K.

Keep it short. Do not give TX advice unless they also ask ham-license or ham-propagation.
