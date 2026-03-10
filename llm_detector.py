from groq import Groq
import os
from dotenv import load_dotenv
import json

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def detect_phishing(url):

    prompt = f"""
You are a cybersecurity expert.

Analyze this URL:

{url}

Determine if it is phishing.

Return ONLY valid JSON in this format:

{{
"prediction": "SAFE or PHISHING",
"reason": "short explanation"
}}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    text = response.choices[0].message.content.strip()

    return json.loads(text)