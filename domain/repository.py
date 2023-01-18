from domain.repository_configuration import RepositoryConfiguration
import logging

class Repository:
    def __init__(self, configuration: RepositoryConfiguration) -> None:
        self.configuration = configuration

    def log(self, message: str) -> None:
        if(self.configuration.print_as_warning):
            logging.warning(message)
        else:
            logging.info(message)