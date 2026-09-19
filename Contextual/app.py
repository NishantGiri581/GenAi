from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
)

prompt = PromptTemplate.from_template(
    """
    Answer the user's question clearly and simply.

    Question:
    {question}
    """
)

chain = prompt | llm

while True:
    user_input = input("Enter your question: ")

    if user_input.lower() == "exit":
        break

    response = chain.invoke({
        "question": user_input
    })

    if isinstance(response.content, list):
        text = "".join(
            block["text"]
            for block in response.content
            if block.get("type") == "text"
        )
    else:
        text = response.content

    print("\nAI:", text)