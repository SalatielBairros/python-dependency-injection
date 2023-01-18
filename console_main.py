from di.service_provider import ServiceProvider


ServiceProvider.config.override(True)
service = ServiceProvider.service()
service.show_message("Salatiel Bairros")