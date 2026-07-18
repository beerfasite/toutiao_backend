from fastapi.responses import  JSONResponse
from fastapi.encoders import jsonable_encoder

def success_response(message:str = "success",data = None):
    content = {
        "message":message,
        "data":data,
        "code":200
    }

    #目标：把任何FastAPI，Pydantic或者ORM对象，都要正常响应->code,message,data
    return JSONResponse(content = jsonable_encoder(content))
