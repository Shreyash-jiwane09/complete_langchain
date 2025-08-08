from langchain_community.embeddings import OllamaEmbeddings



embeddings=(
    OllamaEmbeddings(model="gemma:2b")  ##by default it ues llama2
)

query = "Delhi is the capital of India"
documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]
query_embed=embeddings.embed_query(query)
doc_embed=embeddings.embed_documents(documents)

print("Query embedding:", query_embed)
print("Document embeddings:", doc_embed)
