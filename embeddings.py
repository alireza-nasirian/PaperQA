from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

def create_embeddings(text_chunks):
    embeddings = OpenAIEmbeddings()
    return FAISS.from_texts(text_chunks, embeddings)
