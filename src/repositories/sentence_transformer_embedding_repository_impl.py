from sentence_transformers import SentenceTransformer
from typing import List
from src.domains.repositories.embedding_repository import EmbeddingRepository  

class SentenceTransformerEmbeddingRepositoryImpl(EmbeddingRepository):
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def generarEmbedding(self, texto: str) -> List[float]:
        embedding = self.model.encode(texto, convert_to_numpy=True)  # type: ignore
        return embedding.tolist() # type: ignore
