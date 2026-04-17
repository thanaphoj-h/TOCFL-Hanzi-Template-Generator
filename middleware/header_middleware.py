from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, HTTPException, status
from uuid import UUID
from datetime import datetime

from config import Config


class HeaderMiddleware(BaseHTTPMiddleware):

    def __init__(self, app, config: Config):
        super().__init__(app)
        self.excluded_paths = config.get("middleware.excluded_paths", [])

    async def dispatch(self, request: Request, call_next):

        if any(request.url.path.startswith(p) for p in self.excluded_paths):
            return await call_next(request)

        try:

            request_api_key = request.headers.get("request-api-key")
            request_app_id = request.headers.get("request-app-id")
            request_uuid = request.headers.get("request-uuid")
            request_datetime = request.headers.get("request-datetime")

            if not request_api_key or not request_app_id or not request_uuid or not request_datetime:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Missing required headers")

            try:
                parsed_request_uuid = UUID(request_uuid)
            except ValueError:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid request header UUID format")
            
            try:
                parsed_request_datetime = datetime.fromisoformat(request_datetime)
            except ValueError:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid request header datetime format")

            request.state.headers = {
                "request_api_key": request_api_key,
                "request_app_id": request_app_id,
                "request_uuid": parsed_request_uuid,
                "request_datetime": parsed_request_datetime
            }
        except HTTPException:
            raise
        except Exception as ex:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(ex))
    
        return await call_next(request)