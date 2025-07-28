from typing import List, Optional

class PromptQuery:
    def __init__(
        self,
        id: Optional[str] = None,
        prompt: str = "",
        query: str = "",
        embedding: Optional[List[float]] = None,
    ):
        self._id = id
        self._prompt = prompt
        self._query = query
        self._embedding = embedding

    def getId(self) -> Optional[str]:
        return self._id

    def setId(self, valor: Optional[str]) -> None:
        self._id = valor

    def getPrompt(self) -> str:
        return self._prompt

    def setPrompt(self, valor: str) -> None:
        self._prompt = valor

    def getQuery(self) -> str:
        return self._query

    def setQuery(self, valor: str) -> None:
        self._query = valor

    def getEmbedding(self) -> Optional[List[float]]:
        return self._embedding

    def setEmbedding(self, valor: Optional[List[float]]) -> None:
        self._embedding = valor
