# 🩺 Frontline AI Co-Pilot for ASHA / ANM Workers

An AI-powered healthcare screening assistant designed to help **frontline health workers** quickly assess patient symptoms and identify possible health risks.

The system analyzes patient symptoms and provides **triage suggestions (Low / Medium / High risk)** along with recommended next steps.

---

# 🚀 Features

✔ Symptom-based health screening
✔ Voice and text symptom input
✔ AI-assisted triage classification
✔ Detection for common conditions:

* Tuberculosis
* Diabetes
* Anemia
* Diarrhea / dehydration

✔ Clinical reasoning explanation
✔ Downloadable patient screening report (PDF)

---

# 🧠 Tech Stack

* Python
* Streamlit
* SpeechRecognition
* Groq LLM API
* FAISS Vector Database
* LangChain
* ReportLab

---

# 📂 Project Structure

```
agents/      → AI screening logic
frontend/    → Streamlit web application
rag/         → Guideline retrieval system
data/        → Medical guideline data
```

---

# ⚙️ Installation

Clone the repository

```
git clone https://github.com/akankshac2309/Frontline-AI-Co-Pilot-Agentic-Screening-Assistant-for-ASHA-ANM-Workers.git
```

Install dependencies

```
pip install -r requirements.txt
```

Run the application

```
streamlit run frontend/app.py
```

---

# 🧪 Example Input

```
Patient coughing for three weeks with fever
```

### Output

```
Risk Level: HIGH
Possible tuberculosis infection
Recommendation: Visit nearest health center
```

---

# ⚠ Disclaimer

This tool assists frontline healthcare workers and **does not replace professional medical diagnosis**.

---

# 🌍 Future Improvements

* Multilingual symptom support
* Expanded disease detection
* Integration with ABDM health systems
* AI-based symptom extraction

---
