from pydantic import BaseModel, Field
from typing import Literal
from models.request.base_request import BaseRequest


class PageMarginConfig(BaseModel):
    top: int = Field(36, gt=0, le=72)
    right: int = Field(36, gt=0, le=72)
    bottom: int = Field(36, gt=0, le=72)
    left: int = Field(36, gt=0, le=72)

class PageConfig(BaseModel):
    type: Literal["A4", "A5"] = Field("A4")
    margin: PageMarginConfig = PageMarginConfig()

class HanziConfig(BaseModel):
    cols: int = Field(..., gt=0)
    rows: int = Field(..., gt=0)
    trace: int = Field(..., ge=0)

class HanziRequestItem(BaseModel):
    words: str = Field(...)
    page_config: PageConfig = PageConfig()
    hanzi_config: HanziConfig = Field(...)

class HanziRequest(BaseRequest[HanziRequestItem]):
    pass