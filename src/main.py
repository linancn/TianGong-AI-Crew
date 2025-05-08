from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
# import openlit

# from fastapi.staticfiles import StaticFiles

from src.config.config import FASTAPI_AUTH, FASTAPI_BEARER_TOKEN

from src.routers import health_router, research_router

# openlit.init(otlp_endpoint="http://127.0.0.1:4318", disable_metrics=True)

bearer_scheme = HTTPBearer()


def validate_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    if credentials.scheme != "Bearer" or credentials.credentials != FASTAPI_BEARER_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid or missing token")
    return credentials


app = FastAPI(
    title="TianGong AI Crews",
    version="1.0",
    description="TianGong AI Crews API Server",
    dependencies=[Depends(validate_token)] if FASTAPI_AUTH else None,
)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router.router)
app.include_router(research_router.router)
