import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS

from langchain_core.messages import HumanMessage, SystemMessage


# -------- LOAD ENV --------
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# -------- LOAD DOCUMENT --------
with open("resource.txt", "r", encoding="utf-8") as f:
    text = f.read()

# -------- SPLIT DOCUMENT --------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_text(text)

# -------- CREATE EMBEDDINGS --------
embeddings = OpenAIEmbeddings(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

vectorstore = FAISS.from_texts(chunks, embeddings)

# -------- INITIALIZE LLM --------
llm = ChatOpenAI(
    model="openai/gpt-3.5-turbo",
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
)

print("🤖 RAG Chatbot started (type 'exit' to quit)\n")

# -------- CHAT LOOP --------
while True:
    query = input("You: ")

    if query.lower() in ["exit", "quit"]:
        break

    # 🔍 Retrieve relevant chunks
    docs = vectorstore.similarity_search(query, k=3)

    context = "\n\n".join(doc.page_content for doc in docs)

    messages = [
        SystemMessage(
            content=(
                "Answer the question using ONLY the context below.\n\n"
                f"CONTEXT:\n{context}"
            )
        ),
        HumanMessage(content=query)
    ]

    response = llm.invoke(messages)
    print("Bot:", response.content)
