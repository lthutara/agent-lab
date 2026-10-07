from openai import OpenAI  # pip install openai

#client = OpenAI()  # needs OPENAI_API_KEY env var

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

messages = [{"role": "system", "content": "You are a helpful assistant."}]

print("Chatbot ready. Type 'quit' to exit.")
while True:
    user_input = input("You: ")
    if user_input == "quit":
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        #model="gpt-4o-mini",
        model="deepseek-chat",
        messages=messages,
    )
    print(response)
    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print("Bot:", reply)
