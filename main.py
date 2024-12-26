from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import clist

# Create the FastAPI app instance
app = FastAPI(
    title="Your API Title",
    description="Your API Description",
    version="1.0.0",
    docs_url="/docs/",
    redoc_url="/redoc/" # URL for ReDoc documentation
)


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    """Root endpoint."""
    return {"message": "Welcome to the Next-Problem API!"}

@app.get("/{method}/")
def get_method(handle:str, method: int, resource_id:int):
    result = clist.Main(handle,method,resource_id).return_item(method)
    return result