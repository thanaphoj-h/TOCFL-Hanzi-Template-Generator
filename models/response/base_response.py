from pydantic import BaseModel
from typing import Generic, TypeVar, List, Optional
from models.response.error_response import ErrorItem
from models.response.metadata_response import MetadataResponse

T = TypeVar("T")

class BaseResponse(BaseModel, Generic[T]):
    data: Optional[List[T]] = None
    error: Optional[List[ErrorItem]] = None
    metadata: MetadataResponse