from abc import ABC, abstractmethod


class IAwardInterface(ABC):

    def __init__(self):
        self.db = None

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_id(self, id: str):
        pass
