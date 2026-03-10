# from fastapi import FastAPI
# from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware
# from llm_detector import detect_phishing
#
# app = FastAPI()
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
#
# class URLRequest(BaseModel):
#     url: str
#
#
# @app.post("/detect")
# def detect(data: URLRequest):
#
#     result = detect_phishing(data.url)
#
#     return {
#         "url": data.url,
#         "prediction": result["prediction"],
#         "reason": result["reason"]
#     }

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from llm_detector import detect_phishing

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


@app.post("/detect")
def detect(data: URLRequest):

    try:

        result = detect_phishing(data.url)

        return {
            "url": data.url,
            "prediction": result.get("prediction"),
            "reason": result.get("reason")
        }

    except Exception as e:

        return {
            "url": data.url,
            "prediction": "ERROR",
            "reason": str(e)
        }