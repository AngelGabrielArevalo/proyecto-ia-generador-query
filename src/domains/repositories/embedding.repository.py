from abc import ABC, abstractmethod
from ast import List

class EmbeddingRepository(ABC):
    @abstractmethod
    def generarEmbedding(self, texto: str) -> List[float]:
        pass
