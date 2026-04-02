from fastapi import APIRouter
from core.logging import get_logger

router = APIRouter(prefix="/health", tags=["health"])
log = get_logger(__name__)

def init():
    @router.get("/")
    def health_check():
        try:
            log.info("Health Check: OK")
            return { "status": "ok" }
        except Exception as err:
            log.exception("Health Check: ERROR")
            return { "status": "ERROR" }
    return router