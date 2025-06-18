import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

OPENAI_KEY = os.getenv('OPENAI_KEY')

llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_KEY)

messages = [
    ("system", "사용자가 입력한 문장을 영어로 번역해"),
    ("human", "오늘은 피자를 먹어야지!")
]

result = llm.invoke(messages)

print("hello")
print(result.content)