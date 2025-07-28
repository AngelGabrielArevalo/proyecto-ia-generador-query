from abc import ABC, abstractmethod
from typing import List
from src.domains.entities.prompt_query_entity import PromptQuery


class PromptQueryRepository(ABC):
    @abstractmethod
    def crearVarios(self, promptsQuery: List[PromptQuery]) -> None:
        pass

    @abstractmethod
    def obtenerSimilares(
        self, promptEmbedding: List[float], cantidad: int
    ) -> List[PromptQuery]:
        pass
