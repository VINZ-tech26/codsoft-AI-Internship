import json
import os

memory_file = "memory.json"

# Load memory if file exists
if os.path.exists(memory_file):
    with open(memory_file, "r") as f:
        memory = json.load(f)
else:
    memory = {}

def save_memory():
    with open(memory_file, "w") as f:
        json.dump(memory, f)


def get_response(user_input):

    user_input = user_input.lower()

    # Greeting
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"

    # Reset memory
    elif "reset memory" in user_input:
        memory.clear()
        save_memory()
        return "Memory cleared! I forgot everything."

    # Store name
    elif "my name is" in user_input:
        name = user_input.replace("my name is", "").strip()
        memory["name"] = name
        save_memory()
        return f"Nice to meet you {name.title()}!"

    # Ask name
    elif "what is my name" in user_input:
        if "name" in memory:
            return f"Your name is {memory['name'].title()}."
        else:
            return "You haven't told me your name yet."

    # Ask likes (important: check first)
    elif "what do i like" in user_input:
        if "like" in memory:
            return f"You like {memory['like']}."
        else:
            return "You haven't told me what you like yet."

    # Store likes
    elif "i like" in user_input:
        like = user_input.replace("i like", "").strip()

        if like == "":
            return "Tell me what you like."

        memory["like"] = like
        save_memory()
        return f"Cool! I remember that you like {like}."

    # Identity
    elif "who are you" in user_input:
        return "I am your Smart AI Chatbot built using Python."

    # Health
    elif "how are you" in user_input:
        return "I'm doing great! Thanks for asking."

    # Exit
    elif "bye" in user_input:
        return "Goodbye! Have a great day."

    # Default response
    else:
        return "Interesting! Tell me more about that."