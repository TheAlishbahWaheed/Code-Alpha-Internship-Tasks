from datetime import datetime

def chatbot():
    print("🤖 Chatbot: Hello! I'm your Python chatbot.")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower().strip()

        # Greetings
        if any(word in user for word in ["hello", "hi", "hey"]):
            print("🤖 Chatbot: Hello! How can I help you today?")

        # How are you
        elif "how are you" in user:
            print("🤖 Chatbot: I'm doing great! Thanks for asking.")

        # Name
        elif "your name" in user:
            print("🤖 Chatbot: My name is SmartBot.")

        # Time
        elif "time" in user:
            current_time = datetime.now().strftime("%I:%M %p")
            print(f"🤖 Chatbot: The current time is {current_time}.")

        # Date
        elif "date" in user:
            current_date = datetime.now().strftime("%d-%m-%Y")
            print(f"🤖 Chatbot: Today's date is {current_date}.")

        # Help
        elif "help" in user:
            print("🤖 Chatbot: I can tell time, date, do calculations, and chat with you.")

        # Calculator
        elif user.startswith("calculate"):
            try:
                expression = user.replace("calculate", "").strip()
                result = eval(expression)
                print(f"🤖 Chatbot: The answer is {result}")
            except:
                print("🤖 Chatbot: Please enter a valid expression.")

        # Weather (dummy response)
        elif "weather" in user:
            print("🤖 Chatbot: Sorry, I cannot check live weather without internet access.")

        # Thanks
        elif "thank" in user:
            print("🤖 Chatbot: You're welcome!")

        # Goodbye
        elif user in ["bye", "exit", "quit"]:
            print("🤖 Chatbot: Goodbye! Have a nice day.")
            break

        # Unknown input
        else:
            print("🤖 Chatbot: I didn't understand that. Type 'help' to see what I can do.")

chatbot()