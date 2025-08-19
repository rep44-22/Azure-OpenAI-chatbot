from langchain_openai import AzureChatOpenAI
from dotenv import load_dotenv
#import os
from langchain.prompts import ChatPromptTemplate
load_dotenv()

llm = AzureChatOpenAI(
    azure_deployment="gpt-35-turbo",  # or your deployment
    api_version="2025-01-01-preview",  # or your api version
)

user_input=input("You: ")
prompt=ChatPromptTemplate(
    [
        ("system",("You are a helpful AI assisstant. Please assist the user")),
        ("human", user_input),

    ]
)

response=llm.invoke(prompt.format(user_input=user_input))
print(response.content)