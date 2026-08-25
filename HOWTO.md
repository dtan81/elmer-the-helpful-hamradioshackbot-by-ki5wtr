# How to Set Up Elmer

Elmer is a friendly, ham-radio-focused AI agent running on OpenClaw. This guide covers setting up the full stack on a Raspberry Pi (tested on Pi 5).

## Ham Radio Skills

Elmer includes five specialized ham radio skills that are loaded automatically:

### 1. ham-dx
- Monitor DX clusters, rare stations, and DXpeditions
- Examples:
  - "Any rare DX on 20m right now?"
  - "What entities are needed on 10 meters?"
  - "Show me current DX spots for Asia"

### 2. ham-license
- License privileges, band plans, power limits, and exam questions by country and class
- Examples:
  - "What are my privileges on 40m as an Extra?"
  - "Show me the 20m band plan for the US"
  - "What frequency can I use for digital modes?"

### 3. ham-propagation
- Real-time HF/VHF band conditions, solar indices, MUF, grayline, and operating recommendations
- Examples:
  - "How is propagation on 15m right now?"
  - "Is10 meters open to Europe?"
  - "What's the current solar flux and A-index?"

### 4. ham-satellite
- Amateur satellite passes, Doppler shifts, modes, and operating tips
- Examples:
  - "When is the next ISS pass over my grid?"
  - "What satellites are available on 2m?"
  - "Any good FM satellite passes tonight?"

### 5. ham-station
- Personal station assistant for KI5WTR - HF, digital, POTA , EmComm, light contesting, and APRS workflows
- Examples:
  - "What bands are good for POTA today?"
  - "Help me plan a 40m digital setup"
  - "Any upcoming contests this weekend?"

These skills can be used together. For example, you can ask about propagation and then immediately follow up with DX spots on the same band.
