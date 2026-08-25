# How to Set Up Elmer

Elmer is a friendly, ham-radio-focused AI agent running on OpenClaw. This guide covers setting up the full stack on a Raspberry Pi (tested on Pi 5).

## Prerequisites

- Raspberry Pi 4 or 5 (or any Debian-based Linux device)
- OpenClaw installed and running
- xAI API key (for Grok models)
- Telegram Bot Token (recommended)

## 1. Install OpenClaw

Follow the official installation instructions: 
https://docs.openclaw.ai

Verify it's running:

```bash
openclaw status
```

## 2. Configure xAI as the Provider

Edit the main config file:

```bash
sudo nano /home/ki5wtr/.openclaw/openclaw.json
```

Add the xAI provider section under `models`:

```json
"underf the models section"
```

## 3. Configure Telegram

Create a bot with [@BotFather](https://t.me/botfather) and add the token under the `channels.telegram` section, then restart the gateway.

## 4. Embeddings Configuration

The default is OpenAI. Option B: use local Ollama (nomic-embed-text).

## 5. Agent Files (Elmer Personality)

- `IDENTITY.md`
- `SOML.md`
- `USER.md`
- `TOOLS.md`
- `AGENTS.md`
- `IDENTITY.md`
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
