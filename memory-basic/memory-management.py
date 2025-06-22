import os
from dotenv import load_dotenv
import langchain
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, trim_messages
from langchain_core.output_parsers import StrOutputParser

langchain.debug = True

OPENAI_KEY = os.getenv('OPENAI_KEY')
LLM = ChatOpenAI(model_name="gpt-4o-mini", openai_api_key=OPENAI_KEY)
PARSER = StrOutputParser()

messages = [
    SystemMessage(content="사용자의 질문에 2문장 이내로 짧게 대답해."),
    HumanMessage(content="오늘은 피자를 먹어야지"),
    AIMessage(content="정말 맛있겠구나!! 음료는 뭘 마실거야?"),
    HumanMessage(content="내일은 월요일이니... 출근을 해야지...?"),
    AIMessage(content="출근이라니 정말 힘들겠구나ㅠㅠ"),
    HumanMessage(content="주말에는 영화를 보러갈거야!"),
    AIMessage(content="주말이 벌써부터 기다려지겠는걸? 보려고 생각해둔 영화가 있어?"),
]

# strategy를 `first`로 사용하여 과거 대화 남기고 최근 대화 삭제하기
# strategy를 `last`로 사용하여 최근 대화 남기고 과거 대화 삭제하기
# strategy를 `last`로 사용하여 최근 대화 남기고 과거 대화 삭제할 때 system message가 삭제되는데, `include_system=True`를 사용하여 system message가 삭제 안되도록 해야함
# HumanMessage로 부터 시작하기 위해서는 `` 설정 추가 필요
trimmer = trim_messages(max_tokens=150, 
                        token_counter=LLM,
                        strategy="last",
                        include_system=True,
                        start_on="human")

chain = trimmer | LLM | PARSER
output = chain.invoke(messages + [
    HumanMessage(content="오늘 무엇을 먹는다고 했지?")
])

print(output) 
# 오늘의 메뉴는 무엇인지 기억이 나지 않네요. 어떤 음식을 드실 예정인가요?
# 이러한 응답을 받는 이유는 max_tokens이 150으로 설정되어 있어. 메시지 내용이 삭제되었기 때문

trimmer = trim_messages(max_tokens=200, 
                        token_counter=LLM,
                        strategy="last",
                        include_system=True,
                        start_on="human")

chain = trimmer | LLM | PARSER
output = chain.invoke(messages + [
    HumanMessage(content="오늘 무엇을 먹는다고 했지?")
])

print(output) 
# 오늘은 피자를 먹기로 했어! 맛있게 먹길 바래!
# max_tokens을 200으로 설정한다면 메시지 내용이 삭제되지 않았기 때문에 사용자에 대한 질문에 답변을 할 수 있게됨