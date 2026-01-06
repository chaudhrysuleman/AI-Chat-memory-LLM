from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from memory_setup import chat_llm, memory



# Define prompt with history placeholder
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}")
])

# Create LCEL chain
chain = prompt | chat_llm

def get_chat_response(user_input):
    """
    Process a user input through the LLM chain with memory.
    
    1. Load current history from memory.
    2. Invoke the chain with input + history.
    3. Save the new interaction back to memory.
    """
    # Load history
    history = memory.load_memory_variables({})["chat_history"]
    
    # Invoke chain
    response = chain.invoke({
        "input": user_input,
        "chat_history": history
    })
    
    # Save context
    memory.save_context({"input": user_input}, {"output": response.content})
    
    return response.content
