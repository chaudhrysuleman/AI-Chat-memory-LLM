from chat_logic import get_chat_response
from memory_setup import memory

def main():
    print("--- Starting Chat with Memory ---\n")
    
    # Message 1
    print("User: Hello, how are you? my name is Muhammad")
    response = get_chat_response("Hello, how are you? my name is Muhammad")
    print(f"AI:   {response}\n")
    
    # Message 2 (Tests memory of name)
    print("User: What is my name?")
    response = get_chat_response("What is my name?")
    print(f"AI:   {response}\n")
    
    # Message 3 (General query)
    print("User: What is the weather like today?")
    response = get_chat_response("What is the weather like today?") 
    print(f"AI:   {response}\n")
    
    print("--- Final Memory State ---")
    print(memory.load_memory_variables({}))

if __name__ == "__main__":
    main()
