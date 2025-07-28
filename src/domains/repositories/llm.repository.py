from abc import ABC, abstractmethod
from ast import List

class LlmRepository(ABC):
    @abstractmethod
    def generarTexto(self, prompt: str, tokenMaximos: Optional[int] = None) -> str:
        pass
