---
name: winlink
description: Check or send KI5WTR Winlink over CMS telnet via Pat. Use when asked to check Winlink, WL2K, CMS, winlink email, or send a Winlink message.
---

Read STATION.md for station facts. Password is only in Pat config.

## Check
Run /home/ki5wtr/bin/winlink-check.sh
Summarize From, Subject, Date. If it prints (empty), say inbox empty.
On error, show the error. Never invent messages.

## Send
Only if the operator clearly asks to send. Show the draft and wait for yes.
Do not send on a vague "handle my email."
RF/DigiRig Winlink only if they say RF.
