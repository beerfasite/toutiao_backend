from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, update, true
from models.news import Category, News


#获取新闻类别
async def get_categories(db: AsyncSession, skip: int = 0, limit: int = 100):
    stmt = select(Category).offset(skip).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()



async def get_news_list(db: AsyncSession,category_id:int,skip: int = 0, limit: int = 10):
    #查询指定分类下的所有新闻
    stmt = select(News).where(News.category_id == category_id).offset(skip).limit(limit)
    result = await db.execute(stmt)
    return result.scalars().all()


async def get_news_count(db: AsyncSession, category_id:int):
    #查询指定分类下的新闻数量
    stmt = select(func.count(News.id)).where(News.category_id == category_id)
    result = await db.execute(stmt)
    return result.scalar_one()  #只能有一个结果，否则报错




async def get_news_detail(
        db: AsyncSession,
        news_id: int
):
    #获取新闻详情页面id，title，content，author等等
    stmt = select(News).where(News.id == news_id)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()



async def increase_news_views(
        db: AsyncSession,
        news_id: int,
):
    #增加浏览量
    stmt = update(News).where(News.id == news_id).values(views = News.views + 1)
    result = await db.execute(stmt)
    #更新立刻提交数据库，因此多一条commit
    await db.commit()

    #更新 -> 检查数据库是否真的命中了数据 -> 命中了返回true否则false，浏览量不一定+1
    return result.rowcount > 0 #rowcount检查这一行
