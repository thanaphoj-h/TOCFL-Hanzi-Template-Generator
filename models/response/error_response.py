from pydantic import BaseModel

class ErrorItem(BaseModel):
    code: int
    status: int
    message: str