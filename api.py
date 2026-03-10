from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from rag_detector import detect_url

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class URLRequest(BaseModel):
    url: str


@app.get("/")
def home():
    return {"message": "Phishing Detection API Running"}


@app.post("/detect")
def detect(data: URLRequest):

    result = detect_url(data.url)

    return {
        "url": data.url,
        "prediction": result
    }


# This is required for Render
if __name__ == "__main__":
    import uvicorn
    import os

    port = int(os.environ.get("PORT", 10000))

    uvicorn.run(app, host="0.0.0.0", port=port)