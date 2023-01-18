from fastapi import FastAPI
from di.service_provider import ServiceProvider
import api.controllers.log_controller as log_controller


def create_app():
    service_provider = ServiceProvider()    

    app = FastAPI()
    app.container = service_provider
    app.include_router(log_controller.router)
    return app

app = create_app()  