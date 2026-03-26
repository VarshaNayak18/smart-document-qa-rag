import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("GROQ_API_KEY")

from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=key
)

response = llm.invoke("Explain AI in one line")
print(response.content)