from src.repositories.sentence_transformer_embedding_repository_impl import SentenceTransformerEmbeddingRepositoryImpl
from src.repositories.qdrant_prompt_query_repository_impl import QdrantPromptQueryRepositoryImpl
from src.domains.entities.prompt_query_entity import PromptQuery  # 👈 Importás la clase, no List[PromptQuery]

def main():
    texto = "Hola mundo"
    
    # Generar embedding
    embedding_repo = SentenceTransformerEmbeddingRepositoryImpl()
    embedding = embedding_repo.generarEmbedding(texto)
    print(f"Se genero embedding")

    # Crear repo Qdrant
    qdrant_repo = QdrantPromptQueryRepositoryImpl()

    # Crear una instancia PromptQuery
    ejemplo = PromptQuery(
        prompt=texto,
        query="SELECT * FROM tabla WHERE saludo = 'hola mundo'",
        embedding=embedding,
    )

    # Llamar crearVarios con lista
    qdrant_repo.crearVarios([ejemplo])  # 👈 Pasás lista de 1 elemento
    print("Guardado el ejemplo.")

    # Buscar similares con el mismo embedding
    similares = qdrant_repo.obtenerSimilares(embedding, 3)
    print("Similares encontrados:")
    for s in similares:
        print(f"- id: {s.getId()}, prompt: {s.getPrompt()}, query: {s.getQuery()}")

if __name__ == "__main__":
    main()
