from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exception_handlers import http_exception_handler
import uvicorn


import util.config as gConfig
from router import predict

config = gConfig.Config()

app = FastAPI(
    title="탈모 확률 예측 API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_origins=["https://talmoclient.vercel.app", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"msg": "서버체크 ok"}

@app.get("/1")
async def root():
    return {"deploy": "deploy github action test"}

app.include_router(predict.predict)

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=config.api_port, reload=True)
