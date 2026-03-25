#  RAG Chatbot (Context-Aware AI Chatbot)

An AI-powered **Retrieval-Augmented Generation (RAG) Chatbot** built using modern tools like LangChain, Groq, and Streamlit.
This chatbot can answer user queries based on provided data with a clean ChatGPT-like interface.

---

##  Features

*  ChatGPT-like interactive UI (Streamlit)
*  Context-aware answers using RAG
*  Fast responses using Groq API
*  Vector search with FAISS
*  Chat history memory
*  Clear chat option
*  Download chat as text file
*  Typing animation for better UX

---

##  Tech Stack

* **Python**
* **Streamlit** (Frontend UI)
* **LangChain** (RAG Pipeline)
* **Groq API** (LLM)
* **FAISS** (Vector Database)
* **HuggingFace Embeddings**

---

##  Project Structure

```
rag-chatbot/
│── app.py          # Streamlit frontend
│── utils.py        # Backend logic (RAG pipeline)
│── data.txt        # Knowledge base file
│── requirements.txt
```

---

##  Installation

###  Clone Repository

```bash
git clone https://github.com/your-username/rag-chatbot.git
cd rag-chatbot
```

###  Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

###  Install Dependencies

```bash
pip install -r requirements.txt
```

---

##  Setup API Key

Create a `.env` file or add in code:

```
GROQ_API_KEY=your_api_key_here
```

---

##  Run the App

```bash
streamlit run app.py
```

---

##  How It Works

1. Loads data from `data.txt`
2. Splits text into chunks
3. Converts text into embeddings
4. Stores embeddings in FAISS vector database
5. Retrieves relevant context based on user query
6. Sends context + query to LLM (Groq)
7. Returns accurate answer

---



---

##  Future Improvements

*  PDF & multiple file support
*  Voice-based chatbot
* Deployment (Streamlit Cloud)
* Long-term memory

---

## Contributing

Feel free to fork this repo and improve it!

---

##  Contact

If you like this project or want to collaborate:

* LinkedIn: (https://www.linkedin.com/in/ali-raza-53624337b/)


---

## ⭐ Support

If you found this useful, give it a ⭐ on GitHub!

---
