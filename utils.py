#from langchain.text_splitter import CharacterTextSplitter
from langchain_text_splitters import CharacterTextSplitter
#from langchain.document_loaders import TextLoader
from langchain_community.document_loaders import TextLoader
#from langchain.vectorstores import FAISS
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA


def load_data():
    loader = TextLoader("data.txt", encoding="utf-8")
    documents = loader.load()

    text_splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = text_splitter.split_documents(documents)
    return docs


def create_chain(docs):
    # ✅ Embeddings
    embeddings = HuggingFaceEmbeddings()

    vectorstore = FAISS.from_documents(docs, embeddings)

    # ✅ LLM (Groq)
    llm = ChatGroq(
        model="openai/gpt-oss-120b"
    )

    # ✅ QA Chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever()
    )

    return qa_chain
