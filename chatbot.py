import re

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    responses = {
        r"(hello|hi|hey)": "Hello! Welcome to our Customer Support. How can I help you today?",
        r"(how are you)": "I'm doing great! How can I assist you?",
        r"(help)": """Here are the services I can help you with:
1. Track Order
2. Cancel Order
3. Return Product
4. Offers and Discounts
5. Payment Options
6. Talk to Support
Type the number or the service name to continue.""",
        r"(1|track order)": "Please provide your Order ID to track your order.",
        r"(2|cancel order)": "To cancel your order, please go to 'My Orders' section or type your Order ID here.",
        r"(3|return product)": "You can return the product within 7 days. Type your Order ID to initiate return.",
        r"(4|offers|discounts)": "Use code SAVE10 for 10% off on your first order!",
        r"(5|payment |payment methods)": "We accept UPI, credit/debit cards, and wallets.",
        r"(6|support|talk to support|customer care)": "You can reach our customer care at 1800-111-222.",
        r"(bye|exit|thank you)": "Thank you for using our support service. Have a great day!"
    }

    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response

    return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Chatbot interaction loop
print("Bot: Hello! I'm your virtual assistant. Type 'help' to see what I can do. Type 'exit' to leave.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "bye"]:
        print("Bot: Thank you! Goodbye. 👋")
        break
    print("Bot:", chatbot_response(user_input))
