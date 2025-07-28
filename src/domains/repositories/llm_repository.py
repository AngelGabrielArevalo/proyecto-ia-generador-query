from abc import ABC, abstractmethod
from typing import Optional

class LlmRepository(ABC):
    @abstractmethod
    def generarTexto(self, prompt: str, tokenMaximos: Optional[int] = None) -> str:
        pass
