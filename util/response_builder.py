from fastapi import Request
from datetime import datetime
from typing import Type, TypeVar
from util.app_datetime_provider import AppDatetimeProvider
from models.response.base_response import BaseResponse
from models.response.error_response import ErrorResponse
from models.response.metadata_response import MetadataResponse

T = TypeVar("T", bound=BaseResponse)

class ResponseBuilder:

    @staticmethod
    def build_metadata(request: Request, status:int) -> MetadataResponse:
        return MetadataResponse(
            status=status,
            request_uuid=request.state.headers["request_uuid"],
            request_datetime=request.state.headers["request_datetime"]
        )
    
    @staticmethod
    def build_error(code: int, status: int, message: str) -> ErrorResponse:
        return ErrorResponse(
            code = code,
            status = status,    # HTTP STATUS
            message = message
        )

    @staticmethod
    def build_error_response(request: Request, code: int, status: int, message: str) -> BaseResponse:

        error_response = ResponseBuilder.build_error(request, code=code, status=status, message=message)
        metadata_response = ResponseBuilder.build_metadata(request, status)
        return BaseResponse(data=None, error=[error_response], metadata=metadata_response)
    
    
    @staticmethod
    def build_success_response(request: Request, response_cls: Type[T], data, status: int) -> T:
        
        metadata_response = ResponseBuilder.build_metadata(request, status)
        return response_cls(data=data, error=None, metadata=metadata_response)
