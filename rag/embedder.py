from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load guideline file
with open("data/tb_guidelines.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split guidelines into chunks
texts = text.split("\n\n")

print("Guideline chunks:")
for t in texts:
    print("-", t)

# Create embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create FAISS database
vectorstore = FAISS.from_texts(texts, embeddings)

# Save database
vectorstore.save_local("rag/vector_db")

print("\nVector database created!")