# LM Studio Demo: Espresso Horoscope AI

A creative demonstration of LM Studio's local AI capabilities through mystical espresso horoscope generation

[![LM Studio](https://img.shields.io/badge/LM%20Studio-Integrated-blue?style=for-the-badge&logo=openai)](https://lmstudio.ai)
[![Local AI](https://img.shields.io/badge/Local%20AI-Offline%20Capable-green?style=for-the-badge)](https://lmstudio.ai)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-red?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)](https://python.org)

## Project Overview

This project shows how LM Studio with GPT-OSS 20B can power local AI applications. I built an Espresso Horoscope system that combines coffee brewing data with astrological insights, running entirely offline with AI-generated content.

**Related Project**: This demo is based on the full [Espresso Horoscope MCP](https://github.com/vnsavitri/espresso-horoscope-mcp) project, which includes real and simulated Gaggiuino espresso machine integration, comprehensive MCP protocol support, and advanced features. This repository focuses specifically on the LM Studio integration aspects.

### Portfolio Highlights

- **Local AI Processing**: Complete offline AI processing with LM Studio
- **Creative Application**: Unique combination of coffee, astrology, and AI
- **Technical Implementation**: FastAPI backend with real-time generation
- **User Interface**: Interactive web interface with cosmic design
- **Privacy Focus**: No data leaves the device

## What It Does

- Generates personalized horoscopes based on your birth date and espresso shot metrics
- Uses LM Studio's GPT-OSS 20B model for creative, poetic descriptions
- Works completely offline with no cloud dependencies
- Creates unique content where every reading is different and AI-generated
- Features a web interface with cosmic design and real-time generation

## Live Demo

**Demo Video**: [Watch the Espresso Horoscope MCP in action](https://www.youtube.com/watch?v=hHNMkw1NXDE)

Try it yourself! The system generates horoscopes like this for my birthday (June 11 - Gemini):

```
Cosmic Espresso Forecast for Gemini (June 11)
"Twin Stars in Perfect Sync" - Mercurial-Dual Eclipse

The Stars Align, the Bean Awakens

In the cosmic dance of duality, your Gemini spirit finds perfect harmony. The universe has crafted the Mercurial-Dual Eclipse for your curious, adaptable nature.

- Brew Ratio (1.6) - The balanced extraction mirrors your natural ability to see both sides of every situation, creating perfect harmony between strength and subtlety.
- Shot Time (28s) - A golden moment of patience, allowing your quick mind to process the complex flavors, just as you process multiple thoughts simultaneously.
- Peak Pressure (10.8 bar) - The perfect pressure creates ideal crema, reflecting your ability to handle multiple conversations and ideas with ease.

Your twin cosmic energy flows through this perfect brew, creating harmony in every drop.
```

## Technical Implementation

### LM Studio Integration
```python
# FastAPI backend with LM Studio
OPENAI_BASE_URL = "http://localhost:1234/v1"

def generate_ai_reading(shot_data, zodiac_sign, birth_date):
    response = requests.post(f"{OPENAI_BASE_URL}/chat/completions", json={
        "model": "openai/gpt-oss-20b",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 200,
        "temperature": 0.8
    })
    return response.json()["choices"][0]["message"]["content"]
```

### Advanced Features
- Local AI Processing: Everything runs on your machine
- Real-time Generation: About 2-3 seconds per horoscope
- Dynamic Content: AI creates unique style names and descriptions
- Privacy-First: No data leaves your device
- Offline Capable: Works without internet connection
- Batch Processing: Generate multiple horoscopes simultaneously
- Creative Variations: Different AI styles for the same input
- Error Handling: API integration with graceful fallbacks

### Technical Architecture
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Frontend  │    │  FastAPI Backend│    │   LM Studio     │
│   (Port 8000)   │◄──►│   (Port 8000)   │◄──►│  (Port 1234)    │
│                 │    │                 │    │  GPT-OSS 20B    │
│ • Cosmic UI     │    │ • API Endpoints │    │ • Local AI      │
│ • Real-time     │    │ • Data Processing│    │ • Offline       │
│ • Responsive    │    │ • Error Handling│    │ • Privacy       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## LM Studio Preset

I created a custom preset for this use case:

```json
{
  "name": "Espresso Horoscope Oracle",
  "model": "openai/gpt-oss-20b",
  "system_prompt": "You are a cosmic coffee oracle. Generate poetic, mystical descriptions of espresso shots that combine real brewing metrics with astrological wisdom.",
  "temperature": 0.8,
  "max_tokens": 200
}
```

## Why This Showcases LM Studio

### Real-World Application
- Practical Use Case: Coffee + Astrology + AI
- User Engagement: Interactive, fun, shareable
- Technical Depth: Complex data processing + AI creativity

### Local AI Advantages
- Privacy: No data leaves the device
- Reliability: Works offline
- Performance: Fast local inference
- Cost: No ongoing API costs

### Creative AI Potential
- Unique Outputs: Every generation is different
- Contextual Understanding: Combines multiple data sources
- Poetic Generation: Creative language
- Dynamic Adaptation: Responds to different inputs

## Showcase Examples

### Gemini (June 11) - My Birthday
```
👯‍♂️ Gemini • Cosmic Espresso
"Twin Stars in Perfect Sync" – Mercurial-Dual Eclipse

☕️ Cosmic Espresso Forecast for Gemini (June 11)

🌌 The Stars Align, the Bean Awakens

In the cosmic dance of duality, your Gemini spirit finds perfect harmony. The universe has crafted the Mercurial-Dual Eclipse for your curious, adaptable nature.

- Brew Ratio (1.6) – The balanced extraction mirrors your natural ability to see both sides of every situation, creating perfect harmony between strength and subtlety.
- Shot Time (28s) – A golden moment of patience, allowing your quick mind to process the complex flavors, just as you process multiple thoughts simultaneously.
- Peak Pressure (10.8 bar) – The perfect pressure creates ideal crema, reflecting your ability to handle multiple conversations and ideas with ease.

Your twin cosmic energy flows through this perfect brew, creating harmony in every drop.
```

### Libra (October 7) - My Sister's Birthday
```
🦢 Libra • Stellar Espresso Signature
"Equilibrium Eclipse" – Ancient-Autumn-Harmony

☕️ Cosmic Reading for Libra (10/07)

Balance is your celestial compass, Libra. The universe has poured the Equilibrium Eclipse into your cup, echoing the harmony you seek in every choice.

- Brew Ratio (1.28) – The slight tilt toward a richer extract mirrors your natural inclination toward depth and substance in relationships.
- 30-Second Extraction – Your patience in brewing reflects your diplomatic nature, allowing flavors to develop fully.
- 11.4 Bar Pressure – The perfect pressure creates the ideal crema, just as you create harmony in every situation.

Your cosmic energy flows through this perfect brew, creating harmony in every drop.
```

### Creative Variations Demo
The same birth date can generate completely different styles:
- Variation 1: "Stellar Pulse Dawn" - Futuristic, tech-focused
- Variation 2: "Ancient Autumn Harmony" - Mystical, nature-focused  
- Variation 3: "Cosmic Moon Rhythm" - Poetic, celestial-focused

## Getting Started

### Prerequisites
- LM Studio installed with GPT-OSS 20B model loaded
- Python 3.8+
- Node.js 18+

### Setup
1. Start LM Studio with GPT-OSS 20B model
2. Clone this repository
3. Install dependencies: `pip install -r requirements.txt`
4. Set environment: `export OPENAI_BASE_URL="http://localhost:1234/v1"`
5. Start backend: `python -m uvicorn app:app --reload`
6. Open browser: http://localhost:8000

### Test the Integration
```bash
curl "http://localhost:8000/generate_horoscope?birth_date=0611"
```

## API Endpoints

### Core Endpoints
- `GET /` - Web interface
- `GET /generate_horoscope?birth_date=MMDD` - Generate single horoscope
- `GET /batch_generate` - Generate multiple horoscopes
- `GET /creative_variations?birth_date=MMDD&count=3` - Creative variations
- `GET /test_lm_studio` - Health check and model status

### Example API Calls
```bash
# Generate horoscope for Gemini (June 11)
curl "http://localhost:8000/generate_horoscope?birth_date=0611"

# Generate batch horoscopes
curl "http://localhost:8000/batch_generate"

# Generate creative variations
curl "http://localhost:8000/creative_variations?birth_date=0611&count=3"

# Test LM Studio connection
curl "http://localhost:8000/test_lm_studio"
```

## Portfolio Showcase

### Technical Skills Demonstrated
- Local AI Integration: LM Studio API integration
- Full-Stack Development: FastAPI backend + web frontend
- Real-time Processing: Live AI generation with 2-3 second response times
- Error Handling: API integration with graceful fallbacks
- Performance Optimization: Efficient local AI processing
- User Experience: Responsive interface design

### Innovation Highlights
- Creative AI Applications: Unique combination of coffee, astrology, and AI
- Privacy-First Development: Complete local processing, no cloud dependencies
- Real-World Integration: Practical, engaging use case
- Dynamic Content Generation: AI creates unique style names and descriptions
- Offline Capability: Works without internet connection

### Project Impact
- User Engagement: Interactive, fun, shareable experience
- Technical Implementation: Application with comprehensive features
- Local AI Advocacy: Shows the power of privacy-focused AI development
- Creative Problem Solving: Approach to combining different domains

## Performance Metrics

- Response Time: About 2-3 seconds per horoscope
- Uptime: 100% during demo sessions
- Success Rate: 100% API call success
- User Experience: Smooth, real-time generation

## Demo Scenarios

### Determinism Demo
- Same birth date → Same results (deterministic)
- Different times → Style variations
- Shows technical consistency

### Offline Demo
- Turn off Wi-Fi → Still works
- Shows true local AI processing
- Good for demonstrating local AI capabilities

### Creative Demo
- AI generates unique style names
- Poetic, mystical descriptions
- Real espresso metrics integration

## About This Demo

This project demonstrates the potential of LM Studio for creating privacy-focused AI applications that work locally while delivering creative, engaging experiences.

Good for showcasing:
- Local AI processing capabilities
- Creative AI applications
- Real-world use cases
- Privacy-first development
- Technical integration skills

## Repository Structure

```
lmstudio-demo/
├── README.md                 # This file
├── app.py                   # FastAPI backend
├── requirements.txt         # Python dependencies
├── lm_studio_preset.json   # LM Studio preset configuration
├── demo_script.md          # Live demo instructions
└── examples/               # Sample outputs and configurations
```

## Ready for LM Studio Team Demo

This repository is designed to showcase LM Studio's capabilities. It demonstrates:

- Technical Implementation: Integration with local AI
- Creative Application: Unique, engaging use case
- User Experience: Interactive interface
- Privacy Focus: Complete local processing
- Real-World Impact: Practical, fun application

---

## Related Projects

- **This Repository**: [lmstudio-demo](https://github.com/vnsavitri/lmstudio-demo) - LM Studio integration showcase
- **Main Project**: [espresso-horoscope-mcp](https://github.com/vnsavitri/espresso-horoscope-mcp) - Full espresso horoscope system with Gaggiuino integration

**Repository**: https://github.com/vnsavitri/lmstudio-demo  
**Demo**: http://localhost:8000 (when running)  
**LM Studio**: http://localhost:1234 (when running)
