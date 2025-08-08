from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv 

load_dotenv()

model = ChatGroq(
    model ="gemma2-9b-it"
)

messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content = "Tell me about python")
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)
