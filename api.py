from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

import util.config as gConfig
from router import predict

config = gConfig.Config()

app = FastAPI(
    title="탈모 확률 예측 API",
)

# CORS 미들웨어 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 출처 허용 (프로덕션에서는 구체적인 출처를 지정하는 것이 좋습니다)
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메소드 허용
    allow_headers=["*"],  # 모든 HTTP 헤더 허용
)

@app.get("/")
async def root():
    return {"asdf": "asdf"}

# 라우터 포함
app.include_router(predict.router)

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=config.api_port, reload=True)
