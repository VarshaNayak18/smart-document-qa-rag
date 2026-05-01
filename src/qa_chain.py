from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

def create_qa_chain(vectorstore):
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        api_key=os.getenv("GROQ_API_KEY")
    )

    retriever = vectorstore.as_retriever()

    def qa_function(query):
        docs = retriever.get_relevant_documents(query)
        
        context = "\n\n".join([doc.page_content for doc in docs])

        prompt = f"""
        Answer the question based only on the context below.

        Context:
        {context}

        Question:
        {query}
        """

        response = llm.invoke(prompt)
        return response.content

    return qa_function