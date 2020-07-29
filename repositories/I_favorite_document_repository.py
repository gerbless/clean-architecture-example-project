from abc import ABC, abstractmethod

from entities.favorite_document import FavoriteDocument


class IFavoriteDocumentRepository(ABC):

    @abstractmethod
    def add(self, document: FavoriteDocument): pass

    @abstractmethod
    def get_id(self, uid: int): pass

    @abstractmethod
    def delete(self, uid: int): pass

    @abstractmethod
    def get_all(self): pass
