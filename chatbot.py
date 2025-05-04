def chatbot():
    print("Hello! I'm your customer service assistant.")
    
    while True:
        user_input = input("You: ").lower()  # Get user input and convert it to lowercase
        
        if 'hello' in user_input or 'hi' in user_input:
            print("Bot: Hi! How can I help you today?")
        
        elif 'bye' in user_input or 'goodbye' in user_input:
            print("Bot: Goodbye! Have a great day!")
            break
        
        elif 'hours' in user_input:
            print("Bot: Our working hours are from 9 AM to 5 PM, Monday to Friday.")
        
        elif 'order' in user_input:
            print("Bot: Please provide your order number to check the status.")
        
        elif 'help' in user_input:
            print("Bot: I can assist you with account inquiries or order status. What do you need help with?")
        
        else:
            print("Bot: Sorry, I didn't understand that. Can you ask something else?")

# Start the chatbot
chatbot()
