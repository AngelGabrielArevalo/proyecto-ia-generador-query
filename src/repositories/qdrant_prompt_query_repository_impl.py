import os
import uuid
from typing import List
from qdrant_client import QdrantClient
from qdrant_client.http import models
from src.domains.entities.prompt_query_entity import PromptQuery
from src.domains.repositories.prompt_query_repository import PromptQueryRepository


class QdrantPromptQueryRepositoryImpl(PromptQueryRepository):
    def __init__(self):
        self.__host = os.getenv("QDRANT_HOST", "localhost")
        self.__puerto = int(os.getenv("QDRANT_PORT", "6333"))
        self.__nombreColeccion = "prompt_queries"

        self.__clienteQdrant = QdrantClient(
            host=self.__host,
            port=self.__puerto,
            check_compatibility=False,
        )

        self.__crearColeccionSiNoExiste()

    def __crearColeccionSiNoExiste(self) -> None:
        """Verifica si la colección existe y la crea si no."""
        coleccionesExistentes = self.__clienteQdrant.get_collections()
        nombresColecciones = [c.name for c in coleccionesExistentes.collections]

        if self.__nombreColeccion not in nombresColecciones:
            try:
                self.__clienteQdrant.recreate_collection(
                    collection_name=self.__nombreColeccion,
                    vectors_config=models.VectorParams(size=384, distance=models.Distance.COSINE),
                )
                print(f"Colección '{self.__nombreColeccion}' creada correctamente.")
            except Exception as e:
                print(f"Error creando colección: {e}")

    def crearVarios(self, promptsQuery: List[PromptQuery]) -> None:
        """Inserta varios vectores en Qdrant en un solo llamado."""
        try:
            vectores: List[models.PointStruct] = []
            for promptQuery in promptsQuery:
                uuidGenerado = str(uuid.uuid4())
                promptQuery.setId(uuidGenerado)  
                vector = models.PointStruct(
                    id=promptQuery.getId(), # type: ignore
                    vector=promptQuery.getEmbedding(), # type: ignore
                    payload={
                        "prompt": promptQuery.getPrompt(),
                        "query": promptQuery.getQuery(),
                    },
                )
                vectores.append(vector)

            self.__guardarVectores(vectores)
            print(f"{len(vectores)} vectores insertados en Qdrant.")
        except Exception as e:
            print(f"Error al insertar vectores: {e}")

    def __guardarVectores(self, vectores: List[models.PointStruct]) -> None:
        """Guarda o actualiza múltiples vectores en la colección."""
        self.__clienteQdrant.upsert(
            collection_name=self.__nombreColeccion,
            points=vectores,
        )

    def obtenerSimilares(
        self, promptEmbedding: List[float], cantidad: int
    ) -> List[PromptQuery]:
        """Busca vectores similares en la colección y los devuelve como PromptQuery."""
        try:
            vectoresEncontrados = self.__buscarVectores(promptEmbedding, cantidad)
            print(f"Resultado crudo de búsqueda: {vectoresEncontrados}")
        except Exception as e:
            print(f"Error buscando similares: {e}")
            return []

        return self.__mapearAPromptQuery(vectoresEncontrados)

    def __buscarVectores(
        self, embeddingConsulta: List[float], cantidad: int
    ) -> List[models.ScoredPoint]:
        """Llama a Qdrant para buscar vectores similares."""
        return self.__clienteQdrant.search(
            collection_name=self.__nombreColeccion,
            query_vector=embeddingConsulta,
            limit=cantidad,
        )

    def __mapearAPromptQuery(self, vectores: List[models.ScoredPoint]) -> List[PromptQuery]:
        """Mapea resultados de Qdrant a instancias de PromptQuery."""
        promptsQuery: List[PromptQuery] = []

        for vector in vectores:
            payload = vector.payload or {}

            entidad = PromptQuery(
                id=str(vector.id),
                prompt=payload.get("prompt", ""),
                query=payload.get("query", ""),
                embedding=None  # Podés omitirlo o poner None
            )
            promptsQuery.append(entidad)

        return promptsQuery

