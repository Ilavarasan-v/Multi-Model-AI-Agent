# 🧠 Multi-Model AI Agent

> Upload any image. Ask anything. Get structured JSON output — dynamically shaped to your specific image and question.

---

## 📌 What is this?

A **multimodal AI agent** that accepts any image + any question and returns clean, structured JSON output. 
No predefined categories. 
No fixed fields. The agent figures out the best JSON structure by itself based on what it sees.

---

## 🎯 How it Works

```
You upload an image + type a question
        ↓
Agent looks at both together
        ↓
Decides what information is relevant
        ↓
Decides the best JSON structure for THIS specific image + question
        ↓
Returns clean structured output in your browser
```

---

## 💡 Example Outputs

**Receipt photo + "am I overspending on food?"**
```json
{
  "verdict": "overspending",
  "total_spent": 3847,
  "biggest_category": "food",
  "food_percentage": 68,
  "tip": "Your restaurant spending alone exceeds your stated food budget."
}
```

**Whiteboard photo + "summarize this meeting"**
```json
{
  "topic": "Q2 sprint planning",
  "key_decisions": ["Ship auth by April 25", "Drop dark mode to v2"],
  "action_items": ["Deepak: API spec by Friday", "Priya: design review Monday"],
  "open_questions": ["Which cloud provider for prod?"]
}
```

**Product photo + "should I buy this for travel?"**
```json
{
  "buy": true,
  "score": 8,
  "best_for": "carry-on travel under 5 days",
  "concerns": ["No laptop compartment visible", "Zipper looks fragile"],
  "verdict": "Good choice if you pack light."
}
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Llama 4 Scout** | Multimodal reasoning model (early fusion) |
| **Groq API** | Runs Llama 4 Scout at 460+ tokens/sec |
| **Streamlit** | Turns Python into a web UI |
| **Python** | Core language |

---

## 📁 Project Structure

```
Multi-Model-AI-Agent/
├── .gitignore
├── .env.example          ← API key template
├── requirements.txt
├── app.py                ← Streamlit UI (run this)
└── agent/
    ├── __init__.py
    ├── client.py         ← Groq client singleton
    ├── image.py          ← base64 image loader
    ├── prompt.py         ← system prompt + message assembler
    ├── llm.py            ← API caller + JSON parser
    └── agent.py          ← orchestrator
```

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/Ilavarasan-v/Multi-Model-AI-Agent.git
cd Multi-Model-AI-Agent
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your API key
```bash
cp .env.example .env
```
Edit `.env` and add your key:
```
GROQ_API_KEY=your_key_here
```
Get a free key at 👉 [console.groq.com](https://console.groq.com) — no credit card needed.

### 5. Run the app
```bash
streamlit run app.py
```
Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🖼️ Supported Image Formats

| Format | MIME Type |
|--------|-----------|
| `.jpg` / `.jpeg` | image/jpeg |
| `.png` | image/png |
| `.webp` | image/webp |
| `.gif` | image/gif |

> ⚠️ Max image size: **4MB** — compress larger images before uploading.

---

## ⚙️ Architecture

```
User (uploads image + types question)
        ↓
app.py — Streamlit UI
        ↓
agent/agent.py — Orchestrator
    ↓               ↓
agent/image.py   agent/prompt.py
(base64 encode)  (build messages)
        ↓
agent/llm.py — Calls Groq API
        ↓
agent/client.py — Groq client
        ↓
Returns JSON → displayed in browser
```

---

## 🔒 Security

- API key is stored in `.env` — never committed to version control
- `.env` is listed in `.gitignore`
- `.env.example` is provided as a safe template

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 🙋‍♂️ Author

**Ilavarasan V**  
[@Ilavarasan-v](https://github.com/Ilavarasan-v)

---

> Built with  using Groq + LLaMA 4 Scout + Streamlit

## 🙋‍♂️ Sample output

<img width="1719" height="880" alt="Screenshot 2026-04-22 105901" src="https://github.com/user-attachments/assets/b2c8cad3-bd59-4e08-8030-6b70314861fc" />
<img width="1924" height="1084" alt="Screenshot 2026-04-22 111457" src="https://github.com/user-attachments/assets/dea1528b-d242-468b-a99f-b97a70bbd0e8" />
<img width="1924" height="1084" alt="Screenshot 2026-04-22 113132" src="https://github.com/user-attachments/assets/5332219b-bdc6-43aa-88ef-6b4b3013099f" />


