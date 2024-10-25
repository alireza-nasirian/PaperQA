from langchain.text_splitter import CharacterTextSplitter

def split_text(text, chunk_size=1000, chunk_overlap=200):
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=chunk_size,
                                          chunk_overlap=chunk_overlap, length_function=len)
    return text_splitter.split_text(text)
