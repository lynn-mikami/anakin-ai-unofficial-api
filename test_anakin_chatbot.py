from anakin_ai import AnakinAI
import os
import json

api_key = os.getenv("ANAKIN_AI_API_KEY")
if not api_key:
    raise ValueError("Please set the ANAKIN_AI_API_KEY environment variable")

client = AnakinAI(api_key)

CHATBOT_APP_ID = "28993"

def test_chatbot_stream():
    print("Testing Chatbot with streaming:")
    content = "What's your name? Are you the clever one?"
    try:
        for chunk in client.chat_with_bot(CHATBOT_APP_ID, content, stream=True):
            print(chunk, end='', flush=True)
        print("\n\nStreaming completed.")
    except Exception as e:
        print(f"Chatbot Error: {e}")

def test_chatbot_no_stream():
    print("\nTesting Chatbot without streaming:")
    content = "Tell me a joke about AI."
    try:
        result = client.chat_with_bot(CHATBOT_APP_ID, content, stream=False)
        print("Chatbot Result:", json.dumps(result, indent=2))
    except Exception as e:
        print(f"Chatbot Error: {e}")

def test_chatbot_conversation():
    print("\nTesting Chatbot conversation:")
    try:
        # First message
        print("User: Hello, who are you?")
        response = client.chat_with_bot(CHATBOT_APP_ID, "Hello, who are you?", stream=False)
        print("Chatbot:", response['content'])

        # Second message
        print("\nUser: What can you do?")
        response = client.chat_with_bot(CHATBOT_APP_ID, "What can you do?", stream=False)
        print("Chatbot:", response['content'])

        # Third message
        print("\nUser: Tell me a fun fact about AI.")
        response = client.chat_with_bot(CHATBOT_APP_ID, "Tell me a fun fact about AI.", stream=False)
        print("Chatbot:", response['content'])

    except Exception as e:
        print(f"Chatbot Conversation Error: {e}")

if __name__ == "__main__":
    test_chatbot_stream()
    test_chatbot_no_stream()
    test_chatbot_conversation()