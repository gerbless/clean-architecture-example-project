from abc import ABC, abstractmethod


class ILoginUseCase(ABC):

    @abstractmethod
    def valid_credential(self, email: str, password: str): 
        pass
