import os
from core.logging import setup_logging, get_logger
from fastapi import FastAPI
from config import Config
from routers import health_routers

# Load Config
config = Config.load_yml("config.yml")

# Setup Logging
setup_logging(config)
log = get_logger(__name__)

# Create FastAPI App
app = FastAPI(title="TOCFL Hanzi Generator")

app.include_router(health_routers.init())

BASE_DIR = os.path.dirname(__file__)
log.info(BASE_DIR)