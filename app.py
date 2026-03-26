from dotenv import load_dotenv
load_dotenv()

from src.loader import load_pdf
from src.splitter import split_documents

# Load PDF
docs = load_pdf("data/sample.pdf")

# Split into chunks
chunks = split_documents(docs)

print("Number of chunks:", len(chunks))

print("\nFirst chunk:\n")
print(chunks[0].page_content)