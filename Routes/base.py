from fastapi import FastAPI, APIRouter
import os
base_router = APIRouter(
    prefix="/api/v1", #prefix for all the routes
    tags=["api_v1"],
)



@base_router.get("/")
async def welcome():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION")
    return{
        "app name":app_name,
        "app version": app_version  #can be changed n reloaded on the fly
    }



