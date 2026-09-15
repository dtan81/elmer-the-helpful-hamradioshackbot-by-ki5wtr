---
name: shack-time
description: Report UTC and America/Denver local time. Use when the operator asks the time, Zulu, UTC, MDT, MST, or when a net starts.
user-invocable: true
---

# Shack time

When the operator asks what time it is, Zulu, or local:

Run:

```bash
date -u +"UTC %Y-%m-%d %H:%M:%S Z"
TZ=America/Denver date +"%Z %Y-%m-%d %H:%M:%S %Z"
```
