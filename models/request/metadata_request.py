from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID
from util.app_datetime_provider import AppDatetimeProvider

class MetadataRequest(BaseModel):
    request_uuid: UUID | None = Field(...)
    request_datetime: datetime = Field(default_factory=AppDatetimeProvider.now, frozen=True)