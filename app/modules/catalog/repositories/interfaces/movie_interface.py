from abc import ABC, abstractmethod


class IMovieInterface(ABC):

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_id(self, id: str):
        pass
