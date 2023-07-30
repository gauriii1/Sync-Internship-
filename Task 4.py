import re


def clean_text(text):
    # Function to clean the text from special characters and convert to lowercase
    cleaned_text = re.sub(r'[^\w\s]', '', text).lower()
    return cleaned_text


def get_response(user_input):
    user_input = clean_text(user_input)

    # Basic rule-based responses
    if 'hello' in user_input:
        return "Hello there!"
    elif 'how are you' in user_input:
        return "I'm just a chatbot. But thanks for asking!"
    elif 'bye' in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand. Can you please rephrase?"


def main():
    print("Chatbot: Hi there! How can I help you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response = get_response(user_input)
        print("Chatbot:", response)


if __name__ == "__main__":
    main()

