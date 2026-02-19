print("🤖 Mini AI Assistant Started!")
print("Type 'pause' to stop.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("AI: Goodbye! 👋")
        break

    elif "hello" in user_input:
        print("AI: Hi there! How can I help you today?")

    elif "your name" in user_input:
        print("AI: I am your first Python AI program 😎")

    elif "java" in user_input:
        print("AI: Ah! A Java developer entering Python world 🚀")

    elif "ai" in user_input:
        print("AI: AI is the future. And you are just getting started!")

    elif "weather" in user_input:
        print("AI: I can't check live weather yet, but soon I will!")

    else:
        print("AI: Interesting... tell me more!")
