from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from rag_detector import detect_url

app = FastAPI(
    title="Phishing URL Detection API",
    version="1.0"
)

# -------------------------
# CORS CONFIGURATION
# -------------------------

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# REQUEST MODEL
# -------------------------

class URLRequest(BaseModel):
    url: str


@app.get("/")
def home():
    return {"message": "Phishing Detection API Running"}


@app.post("/detect")
def detect_phishing(data: URLRequest):

    result = detect_url(data.url)

    return {
        "url": data.url,
        "prediction": result
    }