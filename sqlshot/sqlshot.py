from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

# Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

# SQL Prompt
prompt = PromptTemplate.from_template(
    """
You are an expert SQL developer.

Convert the user's natural language question into SQL.

Table name: users

Examples:

Input: Get all users
Output: SELECT * FROM users;

Input: Get active users
Output: SELECT * FROM users WHERE active = 1;

Input: Get inactive users
Output: SELECT * FROM users WHERE active = 0;

Input: Get users whose age is greater than 25
Output: SELECT * FROM users WHERE age > 25;

Input: {input}

Output:
"""
)

# Create LangChain chain
chain = prompt | llm


# User interaction
while True:

    user_input = input("Enter your question: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    response = chain.invoke({
        "input": user_input
    })

    # Handle Gemini response content
    if isinstance(response.content, list):
        text = "".join(
            block["text"]
            for block in response.content
            if block.get("type") == "text"
        )
    else:
        text = response.content

    print("\nGenerated SQL:")
    print(text)
    print("-" * 50)