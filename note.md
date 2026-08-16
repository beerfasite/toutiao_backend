# 总体接口实现

---

1. 模块化路由 → API 接口规范文档  
2. 定义模型类 → 数据库表（数据库设计文档）  
3. 在 crud 文件夹里面创建文件，封装操作数据库的方法  
4. 在路由处理函数里面调用 crud 封装好的方法，响应结果  

# 新闻模块    

---

## 新闻定义模型类别  
基类继承 DeclarativeBase + 数据库表模型类  

## 新闻分类模块化路由
创建 APIRouter 实例  
prefix 路由前缀（API 接口规范文档）  
tags 分组 标签  

    router = APIRouter(prefix="/api/news", tags=["news"])


## 新闻crud  



