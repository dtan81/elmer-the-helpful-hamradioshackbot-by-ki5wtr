# How to Set Up Elmer — The Helpful Ham Radio Shack Bot

Elmer is a friendly, knowledgeable AI agent purpose-built for the ham radio shack. This guide provides a complete, one-stop path to deploy Elmer on a Raspberry Pi 5 with OpenClaw, Telegram, and Grok (xAI) — or your preferred model provider.

## Prerequisites

- Raspberry Pi 5 (or Pi 4) running Raspberry Pi OS (64-bit recommended)
- Internet connection for initial setup
- xAI API key (for Grok models) — or OpenAI / local Ollama
- Telegram account (for bot interface — recommended)

## 1. Install Raspberry Pi OS & Basic System

```bash
# Update system
sudo apt update && sudo apt full-upgrade -y
sudo apt install -y git curl jq
```

## 2. Install OpenClaw

Follow the official OpenClaw installation for Raspberry Pi:

```bash
curl -fsSL https://get.openclaw.ai | sh
```

Verify:

```bash
openclaw status
```

## 3. Run the OpenClaw Setup Wizard

```bash
openclaw setup
```

Follow the interactive prompts to configure your instance, default model provider, and basic gateway settings.

## 4. Configure xAI (Grok) as Primary Provider

Edit the main config:

```bash
sudo nano /home/ki5wtr/.openclaw/openclaw.json
```

Add your xAI API key under the `models` section (example):

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

## 5. Configure Telegram Bot (Detailed)

1. Open Telegram → search **@BotFather**
2. Send `/newbot` and follow the prompts
   - Bot name example: `Elmer - KI5WTR Assistant`
   - Username example: `elmer_ki5wtr_bot`
3. Copy the **API token** BotFather provides
4. Edit OpenClaw config:

```bash
sudo nano /home/ki5wtr/.openclaw/openclaw.json
```

Add under `channels`:

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

## 6. Embeddings (Optional but Recommended)

Default uses OpenAI. For fully local operation:

- Install Ollama + `nomic-embed-text` model
- Update config to use local embeddings

## 7. Agent Personality Files

Place these files in your OpenClaw workspace (they are already included in this repository):

- `IDENTITY.md`
- `SOUL.md`
- `USER.md`
- `TOOLS.md`
- `AGENTS.md`
- `MEMORY.md` + daily memory files

## 8. Ham Radio Skills

The following specialized skills are included and automatically loaded:

### ham-dx
DX clusters, rare stations, DXpeditions.

### ham-license
**License privileges, band plans, power limits, exam questions, and FCC Part 97 compliance.**  
This skill is the primary resource for staying within current FCC regulations.

### ham-propagation
Real-time band conditions, solar indices, MUF, grayline.

### ham-satellite
Satellite passes, Doppler, operating tips.

### ham-station
Personal station assistant (HF, digital, POTA, EmComm, APRS, contests).

## 9. FCC Compliance & Regulatory Notes

Elmer is designed to help you operate **legally and responsibly**.

- Always verify current privileges with the `ham-license` skill before transmitting.
- The `ham-license` skill references current FCC Part 97 rules and ARRL band charts.
- Never rely solely on AI output for regulatory decisions — cross-check with official FCC or ARRL sources when in doubt.
- Elmer will refuse requests that would encourage operation outside authorized privileges.

## 10. Final Verification

```bash
openclaw status
openclaw gateway restart
```

Send a test message via Telegram:
- “What’s the current SFI and Kp?”
- “Show me my Extra class privileges on 40m”
- “Any rare DX on 20m right now?”

You now have a fully functional, regulation-aware Elmer instance running on your Pi 5.

---

**Repository Contents**
This repo is the complete one-stop resource for Elmer:
- Full setup instructions (this file)
- All personality and configuration files
- The five core ham radio skills (including FCC compliance via `ham-license`)
- Ready for deployment or further customization

73 de Elmer 📻
