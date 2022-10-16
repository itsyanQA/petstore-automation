from pydantic import BaseModel

from models.response.ApiResponse import ApiResponse


class ApiResponseMetaData(BaseModel):
    api_response: ApiResponse
    status_code: int
