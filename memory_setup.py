import os
import warnings
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory

# Suppress LangChain deprecation warnings for cleaner output
warnings.filterwarnings('ignore', category=UserWarning)

load_dotenv(find_dotenv())

# Ensure API keys are set
if not os.getenv("OPENAI_API_KEY"):
    print("Warning: OPENAI_API_KEY not found in environment.")

llm_model = "gpt-3.5-turbo"
chat_llm = ChatOpenAI(temperature=0.7, model=llm_model)

# Initialize memory
# We use ConversationBufferMemory to store the raw conversation history
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)