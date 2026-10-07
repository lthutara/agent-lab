import json
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

MEMORY_FILE = "chat_history.json"   # <-- new

def load_messages():                # <-- new
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE) as f:
            return json.load(f)
    return [{"role": "system", "content": "You are a helpful assistant."}]

def save_messages(messages):        # <-- new
    with open(MEMORY_FILE, "w") as f:
        json.dump(messages, f, indent=2)

messages = load_messages()          # <-- changed: start from file, not empty list

print(f"Loaded {len(messages)} messages. Type 'quit' or 'clear'.")

while True:
    user_input = input("You: ")

    if user_input == "quit":
        break

    if user_input == "clear":       # <-- new: wipe memory
        messages = [{"role": "system", "content": "You are a helpful assistant."}]
        save_messages(messages)
        print("(memory wiped)")
        continue

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
    )

    reply = response.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print("Bot:", reply)

    u = response.usage
    print(f"[tokens: {u.prompt_tokens} in / {u.completion_tokens} out]")

    save_messages(messages)         # <-- new: save after every exchange
