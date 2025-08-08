from langchain_groq import ChatGroq
from dotenv import load_dotenv


load_dotenv()

llm = ChatGroq(
    model = "gemma2-9b-it"
)


result = llm.invoke("What is machine learning?")

print(result.content)