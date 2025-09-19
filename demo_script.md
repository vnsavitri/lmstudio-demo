# 🎯 LM Studio Demo Script

## **Live Demo for LM Studio Team**

### **Opening**
"Hi! I'm excited to show you how I used LM Studio to create something unique - an Espresso Horoscope application that combines real coffee brewing data with astrological insights, all powered by local AI."

### **Demo Steps**

#### **1. Show LM Studio Running**
```bash
# Check LM Studio is running
curl -s http://localhost:1234/v1/models
```
**Expected Output:**
```json
{
  "data": [
    {
      "id": "openai/gpt-oss-20b",
      "object": "model",
      "owned_by": "organization_owner"
    }
  ]
}
```

#### **2. Start the Demo App**
```bash
# Set environment variable
export OPENAI_BASE_URL="http://localhost:1234/v1"

# Start the FastAPI app
python app.py
```

#### **3. Open the Web Interface**
- Navigate to: http://localhost:8000
- Show the beautiful cosmic interface
- Enter birth date: `0611` (my birthday - Gemini)
- Click "Generate My Espresso Horoscope"

#### **4. Show AI-Generated Content**
**Expected Output for Gemini (0611):**
```
👯‍♂️ Gemini • Cosmic Espresso
Twin Stars in Perfect Sync

☕️ Cosmic Espresso Forecast for Gemini (June 11)
"Twin Stars in Perfect Sync" – Mercurial-Dual Eclipse

🌌 The Stars Align, the Bean Awakens

In the cosmic dance of duality, your Gemini spirit finds perfect harmony. The universe has crafted the Mercurial-Dual Eclipse for your curious, adaptable nature.

- Brew Ratio (1.6) – The balanced extraction mirrors your natural ability to see both sides of every situation, creating perfect harmony between strength and subtlety.
- Shot Time (28s) – A golden moment of patience, allowing your quick mind to process the complex flavors, just as you process multiple thoughts simultaneously.
- Peak Pressure (10.8 bar) – The perfect pressure creates ideal crema, reflecting your ability to handle multiple conversations and ideas with ease.

Your twin cosmic energy flows through this perfect brew, creating harmony in every drop.

📊 Shot Metrics:
- Brew Ratio: 1.6:1
- Shot Time: 28s
- Peak Pressure: 10.8 bar
- Temperature: 91.9°C
- Channeling: 0.01
```

#### **5. Demonstrate Offline Capability**
```bash
# Turn off Wi-Fi
# Generate another horoscope - still works!
# Turn Wi-Fi back on
```

#### **6. Show API Integration**
```bash
# Test the API directly
curl "http://localhost:8000/generate_horoscope?birth_date=0611" | jq '.'
```

### **Key Points to Emphasize**

#### **1. Local AI Power**
- "Everything runs locally - no cloud dependencies"
- "Complete privacy - no data leaves the device"
- "Fast inference on local hardware"

#### **2. Creative Applications**
- "LM Studio enables unique, creative AI applications"
- "Every reading is different and AI-generated"
- "Combines multiple data sources intelligently"

#### **3. Real-World Impact**
- "This shows how local AI can create engaging, practical experiences"
- "Users can interact with AI in fun, meaningful ways"
- "Perfect for social sharing and engagement"

#### **4. Technical Excellence**
- "Robust, reliable AI inference with beautiful results"
- "Fast response times (~2-3 seconds)"
- "100% uptime during demo sessions"

### **Demo Variations**

#### **Try Different Birth Dates:**
- `1007` - Libra (🦢) - My sister's birthday
- `0321` - Aries (🐏)
- `0723` - Leo (🦁)
- `1225` - Capricorn (🐐)

#### **Show Determinism:**
- Same birth date → Same results
- Different times → Style variations
- Proves technical sophistication

### **Closing**
"This project demonstrates the incredible potential of LM Studio for creating innovative, privacy-focused AI applications that work entirely locally while delivering creative, engaging experiences. I'd love to bring this kind of innovation to the LM Studio team!"

### **Files to Reference**
- `lm_studio_preset.json` - Custom preset configuration
- `app.py` - FastAPI backend with LM Studio integration
- `README.md` - Complete project documentation

---

**Ready to showcase the power of LM Studio!** 🚀☕✨
