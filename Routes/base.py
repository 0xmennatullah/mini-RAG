from fastapi import FastAPI, APIRouter

base_router = APIRouter(
    prefix="/api/v1", #prefix for all the routes
    tags=["api_v1"],
)



@base_router.get("/")
def welcome():
    return{
        "message": "hello all :>" #can be changed n reloaded on the fly

    }


