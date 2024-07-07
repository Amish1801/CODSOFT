# This is the Chatbot response function.
def chatbot_response(user_input):
    user_input = user_input.lower()
    
    if "hello" in user_input or "hi" in user_input or "hey" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm a bot, so I don't have feelings, but I'm here to help you!"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "name" in user_input:
        return "I'm a simple rule-based chatbot made for your assistance."
    elif "who made you" in user_input or "who created you" in user_input:
        return "I was created by Amish using Python to demonstrate how rule-based chatbots work for his Internship project at Codsoft."
    elif "what is the time" in user_input:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    elif "what is the date" in user_input:
        from datetime import datetime
        return f"Today's date is {datetime.now().strftime('%Y-%m-%d')}."
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! If you have any other questions, feel free to ask."
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"

# Main loop to interact with the user
if __name__ == "__main__":
    print("Welcome to the Rule-Based Chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)