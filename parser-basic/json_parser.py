import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

class SimilarModel(BaseModel):
    word: str = Field(description="word")
    similar: str = Field(description="similar")

OPENAI_KEY = os.getenv('OPENAI_KEY')
LLM = ChatOpenAI(model_name="gpt-4o-mini", openai_api_key=OPENAI_KEY)
JSON_PARSER = JsonOutputParser(pydantic_object=SimilarModel)

prompt = PromptTemplate(
    template="""
        입력한 단어와 관련있는 유사 단어를 알려주세요 유사 단어 구성시 산업군과 업종이 서로 관련있어야 합니다.
        - 제약사항: {restrictions}
        - 입력단어: {word}
    """,
    input_variables=["word"],
    partial_variables={"restrictions": JSON_PARSER.get_format_instructions()},
)

chain = prompt | LLM | JSON_PARSER
result = chain.invoke({
    "word": "파이썬"
})

print(result) # example out put {'word': '파이썬', 'similar': '자바'}