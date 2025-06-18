import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import SystemMessagePromptTemplate,  HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser

OPENAI_KEY = os.getenv('OPENAI_KEY')
LLM = ChatOpenAI(model_name="gpt-4o-mini", openai_api_key=OPENAI_KEY)
PARSER = StrOutputParser()

# 메시지 템플릿 설정
messages = [
    SystemMessagePromptTemplate.from_template("사용자가 입력한 문장을 {language}로 번역해"),
    HumanMessagePromptTemplate.from_template("{text}")
]

prompt_template = ChatPromptTemplate.from_messages(messages)

# Pipeline 구성
chain = prompt_template | LLM | PARSER

response = chain.invoke({
    "language": "영어",
    "text": "나는 파이썬 프로그래밍 언어를 활용하여 LLM과 LangChain을 공부하고 있어"
})

print(response)