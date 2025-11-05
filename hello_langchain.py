# pip install langchain-openai
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

application_prompt = """Given the following short description
    of a particular topic, write 3 attention-grabbing headlines 
    for a blog post. Reply with only the titles, one on each line,
    with no additional text.
    DESCRIPTION:
    {user_input}
"""
user_input = """AI Orchestration with LangChain and LlamaIndex
    keywords: Generative AI, applications, LLM, chatbot"""


llm = ChatOpenAI(
    api_key="not-needed",  # placeholder to satisfy library
    base_url="http://localhost:1234/v1",  # see chapter 1 video 3
    # see ./screenshots/LM Studio Server - una-cybertron-7b-v2
)

prompt = PromptTemplate(input_variables=["user_input"], template=application_prompt)

chain = prompt | llm | StrOutputParser()
results = chain.stream({"user_input": user_input})
for chunk in results:
    print(chunk, end="")
