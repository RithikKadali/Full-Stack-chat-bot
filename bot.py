# Import the os module to access environment variables
import os

# Import load_dotenv to load variables from a .env file
from dotenv import load_dotenv

# Import ChatOpenAI for interacting with OpenAI-compatible chat models
from langchain_openai import ChatOpenAI

# Import message types used by LangChain
from langchain_core.messages import HumanMessage, SystemMessage


# Load environment variables from the .env file into the system
load_dotenv()

# Get the OpenRouter API key from environment variables
api_key = os.getenv("OPENROUTER_API_KEY")

# If the API key is not found, raise an error
if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env")


# Initialize the language model
llm = ChatOpenAI(
    model="openai/gpt-3.5-turbo",     # Model name (via OpenRouter)
    api_key=api_key,                  # API key for authentication
    base_url="https://openrouter.ai/api/v1",  # OpenRouter endpoint
)

# Display a startup message
print("🤖 Chatbot started (type 'exit' to quit)\n")


# Initialize conversation history with a system message
messages = [
    SystemMessage(content="You are a helpful AI assistant.")
]

# Start an infinite chat loop
while True:
    # Take user input from the console
    user_input = input("You: ")

    # Exit the loop if the user types 'exit' or 'quit'
    if user_input.lower() in ["exit", "quit"]:
        break

    # Add the user's message to the conversation history
    messages.append(HumanMessage(content=user_input))

    # Send the full conversation to the model and get a response
    response = llm.invoke(messages)

    # Print the AI's response
    print("Bot:", response.content)

    # Add the AI's response back into the conversation history
    messages.append(response)