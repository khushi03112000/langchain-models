from langchain_openai import OpenAI   
from dotenv import load_dotenv  ## this is to load environment variables from .env file - load_dotenv is the function that does that
load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

result = llm.invoke("What is the capital of India")

print(result)
