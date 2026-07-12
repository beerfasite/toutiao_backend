from fastapi import APIRouter

#创建apirouter实例
#prefix路由前缀
#tags分组标签
router = APIRouter(prefix="/api/news",tags = ["news"])

@router.get("/categories")
async def get_categories():
    return {"msg":"获取分类成功"}

