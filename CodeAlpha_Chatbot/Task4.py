def simple_chatbot():
    responses = {
        "hello": ["Hi there! 👋", "Hello! How can I help you?", "Hey! What's up?"],
        "hi": ["Hello! 👋", "Hi! How are you?", "Hey! Nice to see you!"],
        "how are you": ["I'm doing great, thanks for asking! 😊", "I'm fine, how about you?"],
        "what is your name": ["I'm ChatBot, your helpful assistant! 🤖", "You can call me ChatBot!"],
        "bye": ["Goodbye! Have a great day! 👋", "See you later!", "Bye! Thanks for chatting!"],
        "goodbye": ["Goodbye! Come back soon! 👋", "It was nice talking to you!"],
        "thanks": ["You're welcome! 😊", "Happy to help!", "Anytime!"],
        "thank you": ["You're welcome! 😊", "My pleasure!", "Happy to help!"],
        "help": ["I can chat with you about various topics. Try saying hello, how are you, bye, etc.", 
                 "What would you like to know?"],
    }
    
    default_replies = [
        "That's interesting! 🤔",
        "I understand. Tell me more!",
        "Interesting point! Can you elaborate?",
        "I'm not sure about that, but I'm learning! 😊",
        "That sounds good!",
    ]
    
    print("=" * 60)
    print("Welcome to ChatBot! 🤖")
    print("=" * 60)
    print("Type 'quit' or 'exit' to end the conversation.\n")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if not user_input:
            continue
        
        if user_input in ["quit", "exit"]:
            print("ChatBot: Goodbye! Have a wonderful day! 👋")
            break
        
        response_found = False
        for keyword, reply_list in responses.items():
            if keyword in user_input:
                import random
                reply = random.choice(reply_list)
                print(f"ChatBot: {reply}\n")
                response_found = True
                break
        
        if not response_found:
            import random
            reply = random.choice(default_replies)
            print(f"ChatBot: {reply}\n")

if __name__ == "__main__":
    simple_chatbot()