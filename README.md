# Chat Memory LLM

This project demonstrates how to implement **Conversational Memory** using [LangChain](https://github.com/langchain-ai/langchain). It enables the LLM (GPT-3.5-turbo) to remember context from previous interactions, such as the user's name or prior questions.

## How it Works

1.  **Memory Initialization**: We use `ConversationBufferMemory` to store the history of messages.
2.  **Prompt Injection**: A `MessagesPlaceholder` with the key `chat_history` is added to the prompt template.
3.  **Chain Execution**:
    *   Before invoking the LLM, the current `chat_history` is loaded from memory.
    *   The LLM generates a response considering this history.
    *   The new `input` and `output` are saved back to memory.

## Tech Stack

*   **LLM**: OpenAI `gpt-3.5-turbo`.
*   **Memory**: LangChain `ConversationBufferMemory`.

## Project Structure

*   `main.py`: Runs a sample conversation loop.
*   `chat_logic.py`: Contains the `get_chat_response` function and memory management logic.
*   `memory_setup.py`: Handles configuration and API keys.

## Setup

1.  **Environment Variables**:
    Create a `.env` file in the root directory and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_openai_api_key_here
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r chat-memory-llm/requirements.txt
    ```

## How to Run

Execute the main script:
```bash
python chat-memory-llm/main.py
```

## Example Output

```text
User: Hello, how are you? my name is Muhammad
AI:   Hello Muhammad! I'm here to help you.

User: What is my name?
AI:   Your name is Muhammad.
```
# AI-Chat-memory-LLM
