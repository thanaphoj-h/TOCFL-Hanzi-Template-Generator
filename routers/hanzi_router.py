from fastapi import APIRouter, status, Request

from models.request.hanzi_request import HanziRequest
from models.response.hanzi_response import HanziResponse
from services.hanzi_service import HanziService
from util.response_builder import ResponseBuilder

router = APIRouter()

@router.post("/hanzi", response_model=HanziResponse)
def read_hanzi(header_request: Request, request: HanziRequest):

    response = HanziService.process_hanzi(request)

    return ResponseBuilder.build_success_response(
        response_cls=HanziResponse,
        request=header_request,
        data=response,
        status=status.HTTP_200_OK
    )

