import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate,  HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser

OPENAI_KEY = os.getenv('OPENAI_KEY')
LLM = ChatOpenAI(model_name="gpt-4o-mini", openai_api_key=OPENAI_KEY)
PARSER = StrOutputParser()

# 메시지 템플릿 설정
messages = [
    SystemMessagePromptTemplate.from_template("사용자가 입력한 단어에 대해 설명해줘."),
    HumanMessagePromptTemplate.from_template("{word}")
]

prompt_template = ChatPromptTemplate.from_messages(messages)

# string parser로 변환
chain = prompt_template | LLM | PARSER

response = chain.invoke({
    "word": "따뜻한 아이스 아메리카노"
})

print(response)