print("🤖 Rule-Based AI Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How can I help you?")

    elif user_input == "how are you":
        print("Bot: I am fine. Thank you for asking!")

    elif user_input == "what is your name":
        print("Bot: I am a Rule-Based AI Chatbot.")

    elif user_input == "who created you":
        print("Bot: I was created using Python programming.")

    elif user_input == "help":
        print("Bot: You can greet me, ask my name, or say bye to exit.")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")