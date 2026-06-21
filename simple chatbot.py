# Simple Chatbot

def chatbot(user_input):
    user_input = user_input.lower()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "I don't understand that."

print("Chatbot: Hello! Type 'bye' to exit.")

while True:
    user = input("You: ")

    response = chatbot(user)
    print("Chatbot:", response)

    if user.lower() == "bye":
        break
