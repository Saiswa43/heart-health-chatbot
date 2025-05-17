from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
from langchain_community.llms import LlamaCpp
from langchain.chains import RetrievalQA
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser
import os
from dotenv import load_dotenv

# Load from .env file
load_dotenv()
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
os.environ['HUGGINGFACEHUB_API_TOKEN'] = hf_token

# Load and preprocess document
def load_and_index_docs():
    loader = PyPDFDirectoryLoader("data/")
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
    chunks = text_splitter.split_documents(docs)

    embeddings = SentenceTransformerEmbeddings(model_name="NeuML/pubmedbert-base-embeddings")
    vectorstore = Chroma.from_documents(chunks, embeddings)

    return vectorstore

# Load LlamaCpp model
def load_llm():
    llm = LlamaCpp(
        model_path="models/BioMistral-7B.Q4_K_M.gguf",
        temperature=0.2,
        max_tokens=2048,
        top_p=1
    )
    return llm

# Build RAG chain
def build_rag_chain(vectorstore, llm):
    from prompt_template import template
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
    prompt = ChatPromptTemplate.from_template(template)

    rag_chain = (
        {"context": retriever, "query": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    return rag_chain
