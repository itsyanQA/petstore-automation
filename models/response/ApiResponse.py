from pydantic import BaseModel


class ApiResponse(BaseModel):
    code: int
    type: str
    message: str
