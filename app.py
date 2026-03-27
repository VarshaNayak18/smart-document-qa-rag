from dotenv import load_dotenv
load_dotenv()

from src.loader import load_pdf
from src.splitter import split_documents
from src.embeddings import create_vector_store

# Load PDF
docs = load_pdf("data/sample.pdf")

# Split
chunks = split_documents(docs)

# Create vector DB
vectorstore = create_vector_store(chunks)

print("Vector store created successfully!")

# Test search
query = "What are APIs?"
results = vectorstore.similarity_search(query, k=2)

print("\nTop results:\n")
for res in results:
    print(res.page_content[:300])
    print("----")