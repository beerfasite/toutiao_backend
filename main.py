from fastapi import FastAPI
from routers import news


# 创建 FastAPI 实例
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World888"}


#挂载路由/注册路由
app.include_router(news.router)
