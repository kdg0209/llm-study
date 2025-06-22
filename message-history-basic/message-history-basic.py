# memory-basic/memory-management.py 파일에서 message를 하드코딩하였는데, 
# history를 사용하여 대화 기록을 관리
import os
from dotenv import load_dotenv
import langchain
import argparse
from langchain_openai import ChatOpenAI
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import HumanMessage, SystemMessage, trim_messages
from langchain_core.output_parsers import StrOutputParser

# langchain.debug = True

parser = argparse.ArgumentParser()
parser.add_argument("--message", "-m", type=str, required=True, help="사용자 메시지")
parser.add_argument("--chat_room", "-c", type=str, required=True, help="채팅방 ID")
args = parser.parse_args()

user_message = args.message
chat_room_id = args.chat_room

OPENAI_KEY = os.getenv('OPENAI_KEY')
LLM = ChatOpenAI(model_name="gpt-4o-mini", openai_api_key=OPENAI_KEY)
PARSER = StrOutputParser()
store = { }
trimmer = trim_messages(max_tokens=1000,     # 최대 1000개의 토큰까지만 메시지를 유지
                        token_counter=LLM,   # LLM 모델을 기반으로 토큰 수 계산
                        strategy="last",     # 마지막 메시지부터 유지하는 전략
                        include_system=True, # 시스템 메시지를 포함하도록 설정
                        start_on="human")    # 대화가 HumanMessage로 시작되도록 설정

chain = trimmer | LLM | PARSER

kdg_default_messages = SystemMessage(content="김동균의 영어 닉네임은 woody를 주로 사용하고 있으며, 깃 허브 링크는 https://github.com/kdg0209입니다. 또한 생일은 02월 09일입니다. 그리고 백엔드 엔지니어이고, Java를 주로 사용하고 있습니다. 현재 관심사는 LLM이며 유데미에서 강의를 통해 공부하고 있습니다.")

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        history = InMemoryChatMessageHistory()
        history.messages.append(SystemMessage(content="사용자의 질문에 2문장 이내로 짧게 대답해."))
        store[session_id] = history
    if session_id == 'kdg':
        history = InMemoryChatMessageHistory()
        history.messages.append(kdg_default_messages)
        store[session_id] = history
    return store[session_id]

with_history = RunnableWithMessageHistory(chain, get_session_history)
config = {"configurable": {"session_id": chat_room_id}}

output = with_history.invoke([HumanMessage(content=user_message)], config=config) 
print(output)
print(store)
print("▶ 히스토리:", store[chat_room_id].messages)