from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model = "gemma2-9b-it")


#detailed way

template = PromptTemplate(
    template = 'Greet the person in 5 language. The name of person is {name}',
    input_variables=['name']

)

#Fill the values of the placeholers

prompt = template.invoke({'name':'shreyash'})

result = model.invoke(prompt)

print(result.content)