from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
)

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a professional language translation AI agent.

Your task is to translate the user's input into Spanish.

Rules:
1.⁠ ⁠Detect the language of the user's input automatically.
2.⁠ ⁠Translate it accurately into natural Spanish.
3.⁠ ⁠Preserve the original meaning, tone, and context.
4.⁠ ⁠Do not explain the translation unless the user asks.
5.⁠ ⁠Output only the Spanish translation.
"""),
    ("human", "{input}")
])

chain = prompt | llm

while True:
    user_input = input("Enter your text (or 'exit'): ").strip()
    if user_input.lower() == "exit":
        break
    try:
        response = chain.invoke({"input": user_input})
        text = response.content
        if isinstance(text, list):
            text = "".join(b.get("text", "") for b in text if isinstance(b, dict))
        print(text)
    except Exception as e:
        print(f"Error: {e}")