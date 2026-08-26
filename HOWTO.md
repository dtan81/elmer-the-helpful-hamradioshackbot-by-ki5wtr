# How to Set Up Elmer — The Helpful Ham Radio Shack Bot

Elmer is a friendly, knowledgeable AI agent purpose-built for the ham radio shack. This guide provides a complete, one-stop path to deploy Elmer on a Raspberry Pi 5 with OpenClaw, Telegram, and Grok (xAI).

## Prerequisites

- Raspberry Pi 5 (or Pi 4) running Raspberry Pi OS (64-bit recommended)
- Internet connection for initial setup
- xAI API key (for Grok models) — or OpenAI / local Ollama
- Telegram account (recommended for the bot interface)

## 1. Install Raspberry Pi OS & Basic System

```bash
# Update system
sudo apt update && sudo apt full-upgrade -y
sudo apt install -y git curl jq
```

## 2. Install OpenClaw

Run the official OpenClaw installation script:

```bash
curl -fsSL https://get.openclaw.ai | sh
```

Verify the installation:

```bash
openclaw status
```

## 3. Run the OpenClaw Onboarding Wizard

**Important:** Use the correct command:

```bash
openclaw onboard
```

Follow the interactive prompts to configure your instance, choose your default model provider (Grok recommended), and set up the gateway.

## 4. Configure xAI (Grok) as Primary Provider

Edit the main config file:

```bash
sudo nano ~/.openclaw/openclaw.json
```

Add your xAI API key under the models section. Example:

```json
"models": {
  "default": "xai/grok-4.3",
  "providers": {
    "xai": {
      "apiKey": "xai-XXXXXXXXXXXXXXXXXXXXXXXX"
    }
  }
}
```

Alternative providers (OpenAI, local Ollama) can be configured the same way.

## 5. Configure Telegram Bot

1. Open Telegram and search for **@BotFather**
2. Send `/newbot` and follow the prompts
   - Bot name example: `Elmer - KI5WTR Assistant`
   - Username example: `elmer_ki5wtr_bot`
3. Copy the **API token** that BotFather provides
4. Edit the OpenClaw config:

```bash
sudo nano ~/.openclaw/openclaw.json
```

Add the Telegram channel under `channels`:

```json
"channels": {
  "telegram": {
    "enabled": true,
    "token": "123456:ABCDEF1234ghIkl-zyx57W2v1u123ew11"
  }
}
```

5. Restart the gateway:

```bash
openclaw gateway restart
```

6. Test by sending a message to your new bot in Telegram.

## 6. Embeddings (Optional but Recommended for Local Use)

Default uses OpenAI embeddings. For fully local operation:

- Install Ollama
- Pull the `nomic-embed-text` model
- Update the config to point to your local embedding provider

## 7. Agent Personality & Configuration Files

Place these files in your OpenClaw workspace folder (they are included in this repository):

- `IDENTITY.md` — Basic identity
- `SOUL.md` — Core personality and rules
- `USER.md` — Information about you (the operator)
- `TOOLS.md` — Local notes and environment-specific details
- `AGENTS.md` — Workspace rules and memory guidelines
- `MEMORY.md` + daily `memory/YYYY-MM-DD.md` files

These files control how Elmer behaves and remembers context.

## 8. Ham Radio Skills

The following specialized skills are included and automatically available:

- **ham-aprs** — APRS tracking, messaging, digipeaters, tactical use
- **ham-digital** — FT8, FT4, and other digital modes (setup, strategy, logging)
- **ham-dx** — DX clusters, rare stations, DXpeditions, needed entities
- **ham-emcomm** — Emergency communications, nets, Winlink, procedures
- **ham-license** — License privileges, band plans, power limits, exam questions, FCC Part 97 compliance
- **ham-pota** — POTA activations, hunting, park info, logging
- **ham-propagation** — Real-time HF/VHF band conditions, solar indices, MUF, grayline
- **ham-satellite** — Amateur satellite passes, Doppler, modes, operating tips
- **ham-station** — Personal station assistant (HF, digital, POTA, EmComm, APRS, contests)

## 9. FCC Compliance & Regulatory Notes

Elmer is designed to help you operate **legally and responsibly**:

- Always verify current privileges with the `ham-license` skill before transmitting
- The `ham-license` skill references current FCC Part 97 rules and ARRL band charts
- Never rely solely on AI output for regulatory decisions — cross-check with official FCC or ARRL sources when in doubt
- Elmer will refuse requests that would encourage operation outside authorized privileges

## 10. Final Verification

```bash
openclaw status
openclaw gateway restart
```

Send a few test messages via Telegram:

- “What’s the current SFI and Kp?”
- “Show me my Extra class privileges on 40m”
- “Any rare DX on 20m right now?”

You now have a fully functional, regulation-aware Elmer instance running on your Pi 5.

---

**Repository Contents**

This repo is the complete one-stop resource for Elmer:
- Full setup instructions (this file)
- All personality and configuration files
- All nine ham radio skills (including FCC compliance via `ham-license`)
- Ready for deployment or further customization

73 de Elmer 📻
