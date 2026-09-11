# Elmer Setup Guide – Replicate This Instance

> **To follow this guide, clone the repo and open `SETUP.md`.**
>
> See example output in the [README](README.md#example-output).

**Last Updated:** 2026-09-06  
**Tested with:** OpenClaw 2026.9.2

**Goal:** Step-by-step instructions to build an Elmer instance identical to the KI5WTR configuration on a Raspberry Pi 5 (16 GB).

**Prerequisites**

Before starting, make sure you have:

- Raspberry Pi 5 (16 GB RAM recommended)
- High-quality microSD card or NVMe SSD
- Node.js 26 installed
- A Telegram account and bot token (create one at [@BotFather](https://t.me/BotFather))
- Tailscale account (recommended for remote access)
- Basic familiarity with the terminal

**Prerequisites**

Before starting, make sure you have:

- Raspberry Pi 5 (16 GB RAM recommended)
- High-quality microSD card or NVMe SSD
- Node.js 26 installed
- A Telegram account and bot token (create one at [@BotFather](https://t.me/BotFather))
- Tailscale account (recommended for remote access)
- Basic familiarity with the terminal

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

### 3. OpenClaw Installation & Onboarding

1. Install Node.js 26 (required for this setup).

2. Install OpenClaw globally:
   ```bash
   npm install -g openclaw@latest --allow-scripts=openclaw
   ```

3. Run the onboarding wizard with the daemon flag:
   ```bash
   openclaw onboard --install-daemon
   ```

   The wizard will guide you through these steps. Follow the instructions below for each prompt:

   - **Security acknowledgment**  
     Read the risk notice and confirm you understand the implications of running an agent with tools.

   - **Existing config detection** (if present)  
     Choose **Keep** if you want to preserve your current setup, or **Modify** if you’re starting fresh.

   - **Setup mode**  
     Select **QuickStart** (recommended for most users) unless you need full control.

   - **Model / Provider selection**  
     Choose your model provider (e.g. `xai/grok-4.3`). This sets your default model. You can change it later via configuration.

   - **API key / secret input**  
     Paste your API key or select **SecretRef** (recommended) to store it securely.

   - **Workspace path**  
     Accept the default (`~/.openclaw/workspace`) or enter a custom path.

   - **Gateway settings**  
     Use the defaults for port and bind address. Keep **Token** auth enabled.

   - **Channels**  
     Configure your Telegram bot token when prompted (or skip and configure later).

   - **Daemon installation**  
     The `--install-daemon` flag will automatically set this up as a systemd service.

   - **Skills & dependencies**  
     Allow the wizard to install required packages.

   - **Verification**  
     The wizard will run health checks and confirm the gateway is working.

4. After the wizard completes, verify everything is running:
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

Enable the ham radio skill set for full functionality. Each skill below adds specific capabilities:

- `ham-aprs` — APRS tracking, messaging, and digipeater functions
- `ham-digital` — FT8, FT4, and other digital mode support
- `ham-dx` — DX cluster monitoring and rare station alerts
- `ham-emcomm` — Emergency communications and Winlink support
- `ham-license` — License privileges, band plans, and exam help
- `ham-pota` — POTA activation and hunting assistance
- `ham-propagation` — Real-time HF/VHF band conditions and forecasts
- `ham-satellite` — Amateur satellite pass predictions and operating tips
- `ham-station` — General station assistant for HF, digital, and POTA

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

### Troubleshooting & Common Issues

**Node.js version errors**  
Make sure you are on Node 26.x. Run `node -v`. If you’re on an older version, use `nvm install 26 && nvm use 26`.

**`openclaw onboard` fails or hangs**  
Try running it without the `--install-daemon` flag first:
```bash
openclaw onboard
```
Then add the daemon afterward if needed.

**Telegram bot not responding**  
- Double-check your bot token in `openclaw.json`.
- Make sure your numeric user ID is in the `allowFrom` list.
- Restart the gateway after changes: `sudo systemctl restart openclaw`.

**How to get your numeric Telegram user ID**  
1. Start a chat with [@userinfobot](https://t.me/userinfobot) on Telegram.
2. Send any message.
3. The bot will reply with your numeric user ID. Copy that number into your config.

**Gateway won’t start after onboarding**  
Run `openclaw doctor` or `openclaw status --deep` to see detailed errors.

**Skills not loading**  
Make sure the skill folders exist in `plugin-skills/` and that you’ve run `npm install` in the workspace if required by the skill.

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