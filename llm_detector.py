import os
from groq import Groq
from dotenv import load_dotenv

# load environment variables
load_dotenv()

# get api key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# initialize groq client
client = Groq(api_key=GROQ_API_KEY)


def analyze_url(url, context):

    prompt = f"""
You are a cybersecurity expert.

Analyze this URL and determine if it is phishing or safe.

URL: {url}

Similar known examples:
{context}

If the URL imitates brands or contains suspicious
keywords like login, verify, update or bank,
classify it as PHISHING.

Otherwise classify it as SAFE.

Return only:
SAFE or PHISHING
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content.strip()