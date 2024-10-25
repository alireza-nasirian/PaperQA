import warnings
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain_community.callbacks.manager import get_openai_callback
from document_reader import read_documents_from_directory
from text_processing import split_text
from embeddings import create_embeddings

load_dotenv()
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Load and process documents
train_directory = 'data/'
text = read_documents_from_directory(train_directory)
text_chunks = split_text(text)

# Create embeddings
docsearch = create_embeddings(text_chunks)

# Set up question-answering
llm = OpenAI()
chain = load_qa_chain(llm, chain_type="stuff")

# Main loop for user query
while True:
    query = input("Ask a question about the paper: ")
    if query == "end":
        break
    docs = docsearch.similarity_search(query)
    with get_openai_callback() as cb:
        response = chain.run(input_documents=docs, question=query)
        print("\n" + response)
        print(cb)
