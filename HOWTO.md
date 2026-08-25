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

### 3. Configure Telegram

Create a bot with [@botFather](https://t.me/botfather) and copy the token.

Add this section:

```json
"channels": {
  "telegram": {
    "enabled": true,
    "botToken": "YOUR_BOT_TOKEN_HERE"
  }
}

```

Restart the gateway:

```bash
openclaw gateway restart
```

### 4. Embeddings Configuration

By default OpenClaw uses OpenAI for embeddings. 

Option A: Get a low-cost OpenAI key -- embeddings are very cheap.
Option B: Run local embeddings with Ollama (`nomic-embed-text`).

### 5. Agent Files (Elmer Personality)

The following files control Elmer's behavior:

- `IDENTITY.md` -- Name, emoji, basic identity
- `SOUL.md` -- Core personality and rules
- `USER.md` -- Information about you (the owner)
- `TOOLS.md`  -- Local environment notes (SSH hosts, cameras, etc.)
- `AGENTS.md`  -- Workspace rules and memory handling

Edit these files to customize Elmer.

## Next Steps

- Memory management (`memory/YYYY-MM-DD.md`) and `MEMORY.md`)
- Adding custom skills
- Heartbeat and scheduled tasks
-(am radio specific workflows (DX, POTA, awards tracking)

