import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# -------- LOAD TXT DOCUMENT --------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOC_PATH = os.path.join(BASE_DIR, "resource.txt")

# Load environment variables
load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")
if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found in .env")



with open(DOC_PATH, "r", encoding="utf-8") as f:
    document_content = f.read()

# -------- INITIALIZE MODEL --------
llm = ChatOpenAI(
    model="openai/gpt-3.5-turbo",
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
)

print("🤖 Chatbot started (type 'exit' to quit)\n")

# -------- SYSTEM MESSAGE WITH DOC --------
messages = [
    SystemMessage(
        content=(
            "You are a helpful AI assistant.\n\n"
            "Use the following document as your knowledge base.\n"
            "Answer questions ONLY using this document when relevant.\n\n"
            "DOCUMENT:\n"
            f"{document_content}"
        )
    )
]

# -------- CHAT LOOP --------
while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    messages.append(HumanMessage(content=user_input))

    response = llm.invoke(messages)

    print("Bot:", response.content)

    messages.append(response)
