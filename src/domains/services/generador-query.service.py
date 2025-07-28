from abc import ABC, abstractmethod

class GeneradorQueryService(ABC):
    @abstractmethod
    def agregarEjemplo(self, promptsQuery: List[PromptQuery]) -> None:
        pass
    
    @abstractmethod
    def generarQuery(self, prompt: str) -> str:
        pass