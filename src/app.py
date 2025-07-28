from src.repositories.sentence_transformer_embedding_repository_impl import SentenceTransformerEmbeddingRepositoryImpl

def main():
    repo = SentenceTransformerEmbeddingRepositoryImpl()
    texto = "Hola mundo"
    embedding = repo.generarEmbedding(texto)
    print(f"Embedding para '{texto}':\n{embedding}")

if __name__ == "__main__":
    main()
