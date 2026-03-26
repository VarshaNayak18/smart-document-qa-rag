from dotenv import load_dotenv
load_dotenv()

from src.loader import load_pdf

# Load PDF
docs = load_pdf("data/sample.pdf")

print("Number of pages:", len(docs))

print("\nFirst page content:\n")
print(docs[0].page_content[:500]) 