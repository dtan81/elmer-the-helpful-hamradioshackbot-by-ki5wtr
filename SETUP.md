# Elmer Setup Guide – Replicate This Instance

> **To follow this guide, clone the repo and open `SETUP.md`.**
>
> See example output in the [README](README.md#example-output).

**Last Updated:** 2026-09-06  
**Tested with:** OpenClaw 2026.9.2

**Goal:** Step-by-step instructions to build an Elmer instance identical to the KI5WTR configuration on a Raspberry Pi 5 (16 GB).

### Known Working Configuration

- **OpenClaw Version:** 2026.9.2
- **Hardware:** Raspberry Pi 5 (16 GB)
- **Node.js:** 26.x
- **Primary Channel:** Telegram (long polling)
- **Remote Access:** Tailscale

### 1. Hardware Used
- Raspberry Pi 5 (16 GB RAM)
- Storage: High-quality microSD card or NVMe SSD (recommended for reliability)
- Networking: Wired Ethernet preferred, with Tailscale for secure remote access
- Power supply: Official 27W USB-C PD supply

### 2. Base System Preparation
1. Install the latest 64-bit Raspberry Pi OS.
2. Perform a full system update and reboot.
3. (Optional) Create a dedicated non-root user and enable SSH with key authentication.

### 3. OpenClaw Installation
1. Install Node.js 26 (recommended version).
2. Install OpenClaw globally:
   ```bash
   npm install -g openclaw@latest --allow-scripts=openclaw
   ```
3. Run the onboarding wizard:
   ```bash
   openclaw onboard --install-daemon
   ```
4. Verify the gateway is running:
   ```bash
   openclaw status
   ```

### 4. Agent Identity & Personality
Create or copy the following files into your workspace directory:

- `SOUL.md` — Defines core personality, behavior rules, and tone.
- `IDENTITY.md` — Sets the agent’s name, emoji, and basic identity.
- `USER.md` — Contains operator preferences and timezone.
- `MEMORY.md` — Stores long-term facts (station equipment, preferences, community involvement).

These files control how the agent behaves and what it remembers across sessions.

### 5. Workspace & Skills
Enable the ham radio skill set for full functionality:

- `ham-aprs`
- `ham-digital`
- `ham-dx`
- `ham-emcomm`
- `ham-license`
- `ham-pota`
- `ham-propagation`
- `ham-satellite`
- `ham-station`

Skills are loaded from the `plugin-skills` directory. Review each skill’s `SKILL.md` file for configuration options.

### 6. Telegram Configuration
This is one of the most common areas of difficulty.

**Recommended configuration:**

```json
{
  "channels": {
    "telegram": {
      "enabled": true,
      "botToken": "YOUR_BOT_TOKEN",
      "dmPolicy": "pairing",
      "allowFrom": ["YOUR_NUMERIC_TELEGRAM_USER_ID"],
      "groups": {
        "*": {
          "requireMention": true
        }
      }
    }
  }
}
```

**Key points:**
- Use numeric user IDs in `allowFrom`.
- `dmPolicy: "pairing"` is the safest setting for personal use.
- After the first successful DM, the user ID is typically recorded automatically.
- Restart the gateway after making changes to `openclaw.json`.

### 7. OpenClaw Mobile App / Node Pairing (iOS & Android)
This is the second most common source of issues.

**Pairing process:**

1. Ensure the gateway is running and reachable over your network or Tailscale.
2. Use the `/pair` command in Telegram (or another configured channel) to generate a setup code.
3. Enter the code in the OpenClaw mobile app.
4. Approve the pairing request if prompted on the gateway.

**Critical files to preserve during updates:**
- `~/.openclaw/nodes/paired.json`
- `~/.openclaw/state/`

**Strongly recommended:** Create a full backup of `~/.openclaw` before performing any OpenClaw updates.

### 8. Remote Access & Networking
- Install and enable Tailscale as a service.
- Configure the gateway to serve the Control UI over Tailscale.
- Access the Control UI using the Tailscale IP address or DNS name.

### 9. Backup & Maintenance Strategy
Before any OpenClaw update, create a dated backup:

```bash
mkdir -p ~/backups
tar -czf ~/backups/openclaw-preupdate-$(date +%Y-%m-%d).tar.gz -C ~ .openclaw
```

Store backups in a safe location outside the main system when possible.

### 10. Verification & First Run
After completing setup, verify functionality with:

```bash
openclaw channels status
openclaw nodes list
```

Test that:
- Telegram responds correctly
- The mobile app can connect and issue commands
- Skills return expected results (e.g., propagation reports)

### 11. Notes & Gotchas
- Always back up before updating OpenClaw.
- The `openclaw onboard` wizard handles most initial configuration.
- Keep `dmPolicy: "pairing"` and explicit `allowFrom` entries for security.
- Node pairing data lives in `nodes/paired.json` — do not delete this file during updates.