from pydantic import BaseModel, Field
from typing import List
from models.response.base_response import BaseResponse

class HanziResponseItem(BaseModel):
    words: List[str] = Field(...)
    words_count: int = Field(..., ge=0)

class HanziResponse(BaseResponse[HanziResponseItem]):
    pass