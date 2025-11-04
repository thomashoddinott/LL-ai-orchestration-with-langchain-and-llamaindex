import os
from openai import OpenAI # version 1.0+
# if you get openai errors, run pip install --upgrade openai

llm = OpenAI(
    api_key="not-needed", # placeholder to satisfy library
    base_url="http://localhost:1234/v1"  # see chapter 1 video 3
    # see ./screenshots/LM Studio Server - una-cybertron-7b-v2
)

system_prompt = """Given the following short description
    of a particular topic, write 3 attention-grabbing headlines 
    for a blog post. Reply with only the titles, one on each line,
    with no additional text.
    DESCRIPTION:
"""
user_input = """AI Orchestration with LangChain and LlamaIndex
    keywords: Generative AI, applications, LLM, chatbot"""

prompt = system_prompt + user_input
response = llm.completions.create(
    model="gpt-4-1106-preview",
    prompt=prompt,
    max_tokens=500,
    temperature=0.7,
)
print(response.choices[0].text)
# print(response.choices[0].message.content)