from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID

class MetadataResponse(BaseModel):
    status: int =  Field(...)
    request_uuid: UUID | None = Field(...)
    request_datetime: datetime = Field(...)