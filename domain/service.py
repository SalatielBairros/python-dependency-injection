from domain.repository import Repository


class Service:
    def __init__(self, repository: Repository):
        self.__repository__ = repository

    def show_message(self, message: str):
        self.__repository__.log(message)