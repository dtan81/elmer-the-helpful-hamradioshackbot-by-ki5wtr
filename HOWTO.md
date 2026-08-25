# How to Set Up Elmer

Elmer is a friendly, ham-radio-focused AI agent running on OpenClaw. This guide covers setting up the full stack on a Raspberry Pi (tested on Pi 5).

## Prerequisites

- Raspberry Pi 4 or 5 (or any Debian-based Linux device)
- OpenClaw installed and running
- xAI API key (for Grok models)
- Telegram Bot Token (recommended)

## 1. Run the OpenClaw Setup Wizard

Launch the interactive setup wizard to configure your instance:

```bash
openclaw setup
```

Follow the prompts to set your default model provider, API keys, and basic gateway settings.

## 2. Configure xAI as the Provider

Edit the main config file:

```bash
sudo nano /home/ki5wtr/.openclaw/openclaw.json
```

Ensure the xAI provider is configured under the `models` section with your API key.

## 3. Configure Telegram (Detailed)

1. Open Telegram and search for [@BotFather](https://t.me/botfather).
2. Start a chat and send `/newbot`.
3. Follow the prompts to name your bot (e.g., "Elmer - KI5WTR Assistant") and choose a username (e.g., `elmer_ki5wtr_bot`).
4. Copy the bot token provided by BotFather.
5. Edit the OpenClaw config:

```bash
sudo nano /home/ki5wtr/.openclaw/openclaw.json
```

Add or update the Telegram channel section:

```json
"channels": {
  "telegram": {
    "enabled": true,
    "token": "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"
  }
}
```

6. Restart the gateway to apply changes:

```bash
openclaw gateway restart
```

Verify the bot is active by sending a message to it in Telegram.

## 4. Embeddings Configuration

The default is OpenAI. Option B: use local Ollama (nomic-embed-text).

## 5. Agent Files (Elmer Personality)

- `IDENTITY.md`
- `SOUL.md`
- `USER.md`
- `TOOLS.md`
- `AGENTS.md`
- `MEMORY.md` and daily memory files

## 6. Ham Radio Skills

The five specialized ham radio skills are automatically loaded:

### ham-dx
- DX clusters, rare stations, DXpeditions
- Examples: "Any rare DX on 20m?", "Needed DX on 10m?"

### ham-license
- License privileges, band plans, power limits, exam questions
- Examples: "What are my privileges on 40m as Extra?", "Show me the 20m band plan"

### ham-propagation
- RF conditions, solar indices, MUF, grayline, operating recommendations
- Examples: "How is propagation on 15m?", "Is 10m open to Europe?"

### ham-satellite
- Satellite passes, Doppler, modes, operating tips
- Examples: "When is the next ISS pass?", "GOOD FM satellite passes?"

### ham-station
- Ki5WTR personal station assistant (HF, digital, POTA , EmComm, APRS)
- Examples: "Pota bands today?", "Help me plan 40m digital setup", "Contests this weekend?"
