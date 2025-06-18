import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser

OPENAI_KEY = os.getenv('OPENAI_KEY')

llm = ChatOpenAI(model_name="gpt-4o-mini", openai_api_key=OPENAI_KEY)
parser = StrOutputParser()

messages = [
    SystemMessage(content="사용자가 입력한 문장을 영어로 번역해"),
    HumanMessage(content="나는 LLM과 LangChain을 공부하고 있어")
]

chain = llm | parser
result = chain.invoke(messages) # LLM의 결과를 반환
output = parser.invoke(result)  # LLM의 결과를 parser를 통해 변환

print(output)