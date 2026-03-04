from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load embeddings model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load vector database
vectorstore = FAISS.load_local(
    "rag/vector_db",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 2})


def assess_tb_risk(symptoms):
    results = retriever.invoke(symptoms)

    guidelines = [r.page_content for r in results]

    risk_level = "LOW"
    reason = "No strong TB indicators found."

    if "14 days" in symptoms or "weeks" in symptoms:
        risk_level = "HIGH"
        reason = "Patient has prolonged cough which matches TB screening criteria."

    recommendation = "Refer patient for sputum test at nearest health center."
    escalation = "Notify ANM or doctor for further evaluation."

    return {
        "risk": risk_level,
        "reason": reason,
        "guidelines": guidelines,
        "recommendation": recommendation,
        "escalation": escalation,
        "confidence": 0.82
    }