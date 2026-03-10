from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def detect_phishing(url):

    prompt = f"""
You are a cybersecurity expert.

Analyze this URL and determine if it is phishing.

URL: {url}

Consider:
- suspicious keywords (login, verify, update, secure)
- impersonation of brands
- unusual domain patterns
- excessive hyphens or numbers

Return only one word:

SAFE
or
PHISHING
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()