from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject

from api.request.log_request import LogRequest
from di.service_provider import ServiceProvider
from domain.service import Service


router = APIRouter(prefix="/logs")

@router.post("/write")
@inject
def write_log(request: LogRequest, service: Service = Depends(Provide[ServiceProvider.service])):
    service.show_message(request.text)
    return {
        'message': 'Log written',
        'content': request.text
    }