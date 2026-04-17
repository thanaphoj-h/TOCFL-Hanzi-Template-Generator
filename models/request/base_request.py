from pydantic import BaseModel, Field
from typing import List, TypeVar, Generic

T = TypeVar("T")

class BaseRequest(BaseModel, Generic[T]):
    data: List[T] = Field(..., min_length=1)
