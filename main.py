from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import news,users,favorite
from utils.exception_handlers import register_exception_handlers

# 创建 FastAPI 实例
app = FastAPI()


#注册异常处理器
register_exception_handlers(app)


#允许的来源
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]

#允许的源，前端源，开发阶段允许所有源
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        #允许的源，前端源，开发阶段允许所有源
    allow_credentials=True,     #允许携带cookie
    allow_methods=["*"],        #允许的请求方法
    allow_headers=["*"],        #允许的请求头
)



@app.get("/")
async def root():
    return {"message": "Hello World888"}


#挂载路由/注册路由
app.include_router(news.router)
app.include_router(users.router)
app.include_router(favorite.router)
