import sys
import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import clist

app = FastAPI(
    title="Your API Title",
    description="Your API Description",
    version="1.0.0",
    docs_url="/docs/",
    redoc_url="/redoc/"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "Internal Server Error"}
    )

@app.get("/")
def read_root():
    return {"message": "Welcome to the New-Problem API!"}

@app.get("/{method}/")
def get_method(handle: str, method: int, resource_id: int):
    try:
        result = clist.Main(handle, method, resource_id).return_item(method)
        return result
    except Exception as e:
        logger.error(f"Error in get_method: {e}")
        return JSONResponse(
            status_code=500,
            content={"message": "Internal Server Error"}
        )