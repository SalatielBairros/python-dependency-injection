from dependency_injector import containers, providers
from domain.repository import Repository
from di.di_helper import get_config
from domain.repository_configuration import RepositoryConfiguration
from domain.service import Service
from os import path
from os import environ as env

class ServiceProvider(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=["api.controllers.log_controller"])
    
    config = get_config()
    
    repository_configuration = providers.Singleton(RepositoryConfiguration, print_as_warning=config.printAsWarning)
    repository = providers.Singleton(Repository, configuration=repository_configuration)
    service = providers.Factory(Service, repository=repository)