#!/usr/bin/env python3
"""
LM Studio Demo: Espresso Horoscope AI
A simple FastAPI app demonstrating LM Studio integration
"""

import os
import requests
import json
from datetime import datetime
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional

# LM Studio configuration
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "http://localhost:1234/v1")
MODEL_NAME = "openai/gpt-oss-20b"

app = FastAPI(
    title="LM Studio Espresso Horoscope Demo",
    description="Demonstrating LM Studio's local AI capabilities through mystical espresso horoscope generation",
    version="1.0.0"
)

class HoroscopeRequest(BaseModel):
    birth_date: str  # MMDD format
    shot_data: Optional[dict] = None

class HoroscopeResponse(BaseModel):
    birth_date: str
    zodiac_sign: str
    zodiac_icon: str
    title: str
    style_name: str
    reading: str
    shot_metrics: dict
    generated_at: str

def get_zodiac_sign(birth_date: str) -> tuple:
    """Get zodiac sign and icon from birth date (MMDD format)"""
    month = int(birth_date[:2])
    day = int(birth_date[2:])
    
    zodiac_signs = [
        ("Capricorn", "🐐", (12, 22), (1, 19)),
        ("Aquarius", "🐬", (1, 20), (2, 18)),
        ("Pisces", "🐟", (2, 19), (3, 20)),
        ("Aries", "🐏", (3, 21), (4, 19)),
        ("Taurus", "🐂", (4, 20), (5, 20)),
        ("Gemini", "👯‍♂️", (5, 21), (6, 20)),
        ("Cancer", "🦀", (6, 21), (7, 22)),
        ("Leo", "🦁", (7, 23), (8, 22)),
        ("Virgo", "🦋", (8, 23), (9, 22)),
        ("Libra", "🦢", (9, 23), (10, 22)),
        ("Scorpio", "🦂", (10, 23), (11, 21)),
        ("Sagittarius", "🏹", (11, 22), (12, 21))
    ]
    
    for sign, icon, (start_month, start_day), (end_month, end_day) in zodiac_signs:
        if (month == start_month and day >= start_day) or (month == end_month and day <= end_day):
            return sign, icon
    
    return "Unknown", "❓"

def generate_sample_shot_data() -> dict:
    """Generate sample espresso shot data"""
    import random
    return {
        "brew_ratio": round(random.uniform(1.2, 2.5), 2),
        "shot_time": random.randint(20, 35),
        "peak_pressure": round(random.uniform(8.5, 12.0), 1),
        "temp_avg": round(random.uniform(90.0, 94.0), 1),
        "channeling": round(random.uniform(0.0, 0.1), 3)
    }

def call_lm_studio(prompt: str) -> str:
    """Call LM Studio API to generate AI content"""
    try:
        response = requests.post(f"{OPENAI_BASE_URL}/chat/completions", json={
            "model": MODEL_NAME,
            "messages": [
                {
                    "role": "system", 
                    "content": "You are a cosmic coffee oracle. Generate poetic, mystical descriptions of espresso shots that combine real brewing metrics with astrological wisdom. Always include the shot parameters and create unique, creative style names. Your readings should be: 1) Mystical and poetic, 2) Include specific shot metrics, 3) Reference the zodiac sign, 4) Create unique style names, 5) Be inspiring and cosmic."
                },
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 200,
            "temperature": 0.8
        }, timeout=30)
        
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"LM Studio API error: {response.status_code}"
            
    except requests.exceptions.RequestException as e:
        return f"Error connecting to LM Studio: {str(e)}"

@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the demo interface"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>LM Studio Espresso Horoscope Demo</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; }
            .container { background: rgba(255,255,255,0.1); padding: 30px; border-radius: 15px; backdrop-filter: blur(10px); }
            h1 { text-align: center; margin-bottom: 30px; }
            .form-group { margin: 20px 0; }
            label { display: block; margin-bottom: 5px; font-weight: bold; }
            input { width: 100%; padding: 10px; border: none; border-radius: 5px; font-size: 16px; }
            button { background: #ff6b6b; color: white; padding: 12px 24px; border: none; border-radius: 5px; font-size: 16px; cursor: pointer; width: 100%; }
            button:hover { background: #ff5252; }
            .result { margin-top: 30px; padding: 20px; background: rgba(255,255,255,0.1); border-radius: 10px; }
            .loading { text-align: center; color: #ffd700; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>☕ LM Studio Espresso Horoscope Demo</h1>
            <p>Enter your birth date (MMDD format) to generate a mystical espresso horoscope powered by LM Studio's local AI!</p>
            
            <form onsubmit="generateHoroscope(event)">
                <div class="form-group">
                    <label for="birthDate">Birth Date (MMDD):</label>
                    <input type="text" id="birthDate" placeholder="e.g., 0611 for June 11th" maxlength="4" required>
                </div>
                <button type="submit">Generate My Espresso Horoscope</button>
            </form>
            
            <div id="result" class="result" style="display: none;">
                <div id="content"></div>
            </div>
        </div>
        
        <script>
            async function generateHoroscope(event) {
                event.preventDefault();
                const birthDate = document.getElementById('birthDate').value;
                const resultDiv = document.getElementById('result');
                const contentDiv = document.getElementById('content');
                
                resultDiv.style.display = 'block';
                contentDiv.innerHTML = '<div class="loading">🔮 Generating your cosmic reading...</div>';
                
                try {
                    const response = await fetch(`/generate_horoscope?birth_date=${birthDate}`);
                    const data = await response.json();
                    
                    contentDiv.innerHTML = `
                        <h2>${data.zodiac_icon} ${data.zodiac_sign} • ${data.title}</h2>
                        <h3>${data.style_name}</h3>
                        <div style="white-space: pre-line; line-height: 1.6;">${data.reading}</div>
                        <hr style="margin: 20px 0;">
                        <h4>📊 Shot Metrics:</h4>
                        <ul>
                            <li>Brew Ratio: ${data.shot_metrics.brew_ratio}:1</li>
                            <li>Shot Time: ${data.shot_metrics.shot_time}s</li>
                            <li>Peak Pressure: ${data.shot_metrics.peak_pressure} bar</li>
                            <li>Temperature: ${data.shot_metrics.temp_avg}°C</li>
                            <li>Channeling: ${data.shot_metrics.channeling}</li>
                        </ul>
                        <p><em>Generated at: ${data.generated_at}</em></p>
                    `;
                } catch (error) {
                    contentDiv.innerHTML = `<div style="color: #ff6b6b;">Error: ${error.message}</div>`;
                }
            }
        </script>
    </body>
    </html>
    """

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "lm-studio-espresso-demo"}

@app.get("/generate_horoscope")
async def generate_horoscope(birth_date: str):
    """Generate a horoscope using LM Studio"""
    if len(birth_date) != 4 or not birth_date.isdigit():
        raise HTTPException(status_code=400, detail="Birth date must be in MMDD format (e.g., 0611)")
    
    # Get zodiac sign
    zodiac_sign, zodiac_icon = get_zodiac_sign(birth_date)
    
    # Generate sample shot data
    shot_data = generate_sample_shot_data()
    
    # Create prompt for LM Studio
    prompt = f"""Generate a horoscope reading for a {zodiac_sign} (birth date {birth_date}) with these shot parameters:
    - Brew Ratio: {shot_data['brew_ratio']}:1
    - Shot Time: {shot_data['shot_time']} seconds
    - Peak Pressure: {shot_data['peak_pressure']} bar
    - Temperature: {shot_data['temp_avg']}°C
    - Channeling: {shot_data['channeling']}
    
    Create a unique style name and cosmic reading that combines the shot metrics with {zodiac_sign} astrological traits."""
    
    # Call LM Studio
    ai_reading = call_lm_studio(prompt)
    
    # Extract title and style name from the reading
    lines = ai_reading.split('\n')
    title = "Cosmic Espresso"  # Default
    style_name = "Mystical Brew"  # Default
    
    for line in lines:
        if "**" in line and "☕️" in line:
            title = line.replace("**", "").replace("☕️", "").strip()
        elif "*" in line and "–" in line:
            style_name = line.replace("*", "").replace("–", "").strip()
    
    return HoroscopeResponse(
        birth_date=birth_date,
        zodiac_sign=zodiac_sign,
        zodiac_icon=zodiac_icon,
        title=title,
        style_name=style_name,
        reading=ai_reading,
        shot_metrics=shot_data,
        generated_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

@app.get("/test_lm_studio")
async def test_lm_studio():
    """Test LM Studio connection"""
    try:
        response = requests.get(f"{OPENAI_BASE_URL}/models", timeout=10)
        if response.status_code == 200:
            models = response.json()
            return {
                "status": "connected",
                "models": [model["id"] for model in models.get("data", [])],
                "target_model": MODEL_NAME
            }
        else:
            return {"status": "error", "message": f"HTTP {response.status_code}"}
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": str(e)}

@app.get("/batch_generate")
async def batch_generate_horoscopes():
    """Generate multiple horoscopes to showcase LM Studio's batch processing capabilities"""
    birth_dates = ["0611", "1007", "0321", "0723", "1225"]  # Different zodiac signs
    results = []
    
    for birth_date in birth_dates:
        try:
            zodiac_sign, zodiac_icon = get_zodiac_sign(birth_date)
            shot_data = generate_sample_shot_data()
            
            prompt = f"""Generate a horoscope reading for a {zodiac_sign} (birth date {birth_date}) with these shot parameters:
            - Brew Ratio: {shot_data['brew_ratio']}:1
            - Shot Time: {shot_data['shot_time']} seconds
            - Peak Pressure: {shot_data['peak_pressure']} bar
            - Temperature: {shot_data['temp_avg']}°C
            - Channeling: {shot_data['channeling']}
            
            Create a unique style name and cosmic reading that combines the shot metrics with {zodiac_sign} astrological traits."""
            
            ai_reading = call_lm_studio(prompt)
            
            results.append({
                "birth_date": birth_date,
                "zodiac_sign": zodiac_sign,
                "zodiac_icon": zodiac_icon,
                "reading": ai_reading,
                "shot_metrics": shot_data
            })
        except Exception as e:
            results.append({
                "birth_date": birth_date,
                "error": str(e)
            })
    
    return {
        "batch_results": results,
        "total_generated": len([r for r in results if "error" not in r]),
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

@app.get("/creative_variations")
async def creative_variations(birth_date: str, count: int = 3):
    """Generate multiple creative variations for the same birth date to showcase LM Studio's creativity"""
    if len(birth_date) != 4 or not birth_date.isdigit():
        raise HTTPException(status_code=400, detail="Birth date must be in MMDD format")
    
    if count > 5:
        count = 5  # Limit to prevent abuse
    
    zodiac_sign, zodiac_icon = get_zodiac_sign(birth_date)
    shot_data = generate_sample_shot_data()
    
    variations = []
    for i in range(count):
        prompt = f"""Generate a UNIQUE and CREATIVE horoscope reading for a {zodiac_sign} (birth date {birth_date}) with these shot parameters:
        - Brew Ratio: {shot_data['brew_ratio']}:1
        - Shot Time: {shot_data['shot_time']} seconds
        - Peak Pressure: {shot_data['peak_pressure']} bar
        - Temperature: {shot_data['temp_avg']}°C
        - Channeling: {shot_data['channeling']}
        
        Make this variation #{i+1} completely different from the others. Use a different writing style, different metaphors, and a unique creative approach. Create a unique style name and cosmic reading that combines the shot metrics with {zodiac_sign} astrological traits."""
        
        ai_reading = call_lm_studio(prompt)
        variations.append({
            "variation": i + 1,
            "reading": ai_reading,
            "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
    
    return {
        "birth_date": birth_date,
        "zodiac_sign": zodiac_sign,
        "zodiac_icon": zodiac_icon,
        "shot_metrics": shot_data,
        "variations": variations,
        "total_variations": len(variations)
    }

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting LM Studio Espresso Horoscope Demo...")
    print("📱 Open your browser to: http://localhost:8000")
    print("🔍 Health check: http://localhost:8000/health")
    print("🧪 Test LM Studio: http://localhost:8000/test_lm_studio")
    print("⏹️  Press Ctrl+C to stop")
    
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
