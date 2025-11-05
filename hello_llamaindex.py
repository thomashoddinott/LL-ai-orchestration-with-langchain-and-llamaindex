from dotenv import load_dotenv
import os
from llama_index.core import Document, VectorStoreIndex

# Load .env file
load_dotenv()

# Get your key
api_key = os.getenv("LOCAL_LLM_API_KEY") or os.getenv("OPENAI_API_KEY")

documents = [
    Document(text="Abraham Lincoln was the 16th president of the United States."),
    Document(text="Abraham Shakespeare was a Florida lottery winner in 2006."),
    Document(text="William Shakespeare married Anne Hathaway."),
]


index = VectorStoreIndex(documents)
query_engine = index.as_query_engine()
print(query_engine.query("Who was Shakespeare's wife?"))  # use vector store
print(query_engine.query("Where is Flordia?"))  # use model
