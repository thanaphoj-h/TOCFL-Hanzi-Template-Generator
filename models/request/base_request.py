from pydantic import BaseModel, Field
from typing import List, TypeVar, Generic
from models.request.metadata_request import MetadataRequest

T = TypeVar("T")

class BaseRequest(BaseModel, Generic[T]):
    data: List[T] = Field(..., min_length=1)
    metadata: MetadataRequest = Field(...)