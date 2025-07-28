from abc import ABC, abstractmethod
from typing import List
from src.domains.entities import PromptQuery


class PromptQueryRepository(ABC):
    @abstractmethod
    def crear(self, promptQuery: PromptQuery) -> None:
        pass

    @abstractmethod
    def obtenerSimilares(
        self, queryEmbedding: List[float], cantidadSimilares: int
    ) -> List[PromptQuery]:
        pass
