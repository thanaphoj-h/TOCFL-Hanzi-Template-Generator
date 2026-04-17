import os
from fastapi import FastAPI

from config import Config
from util.app_datetime_provider import AppDatetimeProvider
from util.logging import setup_logging, get_logger

from middleware.header_middleware import HeaderMiddleware

from routers.health_routers import router as health_routers
from routers.hanzi_router import router as hanzi_router

# Load Config
config = Config.load_yml("config.yml")

# Setup Logging
setup_logging(config)
log = get_logger(__name__)

# Create FastAPI App
app = FastAPI(title="TOCFL Hanzi Generator")

app.add_middleware(HeaderMiddleware, config=config)

app.include_router(health_routers)
app.include_router(hanzi_router)

# BASE_DIR = os.path.dirname(__file__)
log.info(f"Now: {AppDatetimeProvider.now_str()}")