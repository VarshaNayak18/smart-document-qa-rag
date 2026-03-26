from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,     # size of each chunk
        chunk_overlap=50    # overlap between chunks
    )

    chunks = text_splitter.split_documents(documents)
    return chunks