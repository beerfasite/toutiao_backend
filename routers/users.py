from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from config.db_conf import get_db
from schemas.users import UserRequest, UserAuthResponse, UserInfoResponse
from crud import users
from utils.response import success_response

router = APIRouter(prefix="/api/user",tags=["user"])


@router.post("/register")
async def register(user_data:UserRequest,db:AsyncSession = Depends(get_db)):  #用户信息和db
    #用户注册
    #注册逻辑：验证用户是否存在->创建用户->生成token->响应结果
    existing_user = await users.get_user_by_username(db, user_data.username)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="用户已经存在")
    user = await users.create_user(db,user_data)
    
    token = await users.create_token(db,user.id)

    #     return {
    #     "code": 200,
    #     "message": "注册成功",
    #     "data": {
    #     "token": token,
    #     "userInfo": {
    #       "id": user.id,
    #       "username": user.username,
    #       "bio": user.bio,
    #       "avatar": user.avatar
    #     }
    #   }
    # }
    response_data = UserAuthResponse(token = token,user_info = UserInfoResponse.model_validate(user))
    return success_response(message="注册成功",data=response_data)
