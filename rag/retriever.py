from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load FAISS vector database
vectorstore = FAISS.load_local(
    "rag/vector_db",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

print("TB Guideline Retriever Ready!")

while True:
    query = input("\nEnter patient symptoms: ")

    if query.lower() == "exit":
        break

    results = retriever.invoke(query)

    print("\nRelevant guideline:")
    for r in results:
        print("-", r.page_content)