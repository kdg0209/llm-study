import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser

OPENAI_KEY = os.getenv('OPENAI_KEY')
LLM = ChatOpenAI(model_name="gpt-4o-mini", openai_api_key=OPENAI_KEY)
PARSER = StrOutputParser()

messages = [
    HumanMessagePromptTemplate.from_template("{contents}")
]

prompt_template = ChatPromptTemplate.from_messages(messages)

chain = prompt_template | LLM | PARSER

response = chain.invoke({
    "contents": "내일 수영하러 가야지"
})

print(response) # 좋은 계획이에요! 수영은 훌륭한 운동이죠. 어떤 스타일을 수영할 예정이신가요?

response = chain.invoke({
    "contents": "내일 뭐한다고 했지?"
})

print(response) # 내일 일정이 어떻게 되는지 잘 모르겠어요. 혹시 이전에 계획한 일이 있다면 그것을 떠올려보는 게 도움이 될 수 있을 것 같아요. 아니면 일정 앱이나 다이어리를 확인해보세요!

# 위 예제 코드에 대한 문제는 대화의 연속성이 없는 것을 확인할 수 있습니다.