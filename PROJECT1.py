print("Welcome to ChatBot!")
print("Type 'bye' to exit.")

while True:
    user = input("You: ")
    user = user.lower()

    if user == "hi":
        print("Bot: Hello!")

    elif user == "how are you":
        print("Bot: I am fine.")

    elif user == "name":
        print("Bot: I am a rule-based chatbot.")

    elif user == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I don't understand.")
