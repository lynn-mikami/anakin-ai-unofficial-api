from anakin_ai import AnakinAI
import os
import json

api_key = os.getenv("ANAKIN_AI_API_KEY")
if not api_key:
    raise ValueError("Please set the ANAKIN_AI_API_KEY environment variable")

client = AnakinAI(api_key)

QUICK_APP_ID = "28991"

def test_quick_app_stream():
    print("Testing Quick App with streaming:")
    inputs = {
        "Input": "Generate a marketing slogan for a cloud service that emphasizes reliability, performance, and efficiency."
    }
    try:
        for chunk in client.run_quick_app(QUICK_APP_ID, inputs, stream=True):
            print(chunk, end='', flush=True)
        print("\n\nStreaming completed.")
    except Exception as e:
        print(f"Quick App Error: {e}")

def test_quick_app_no_stream():
    print("\nTesting Quick App without streaming:")
    inputs = {
        "Input": "Write a brief product description for a high-performance cloud service."
    }
    try:
        result = client.run_quick_app(QUICK_APP_ID, inputs, stream=False)
        print("Quick App Result:", json.dumps(result, indent=2))
    except Exception as e:
        print(f"Quick App Error: {e}")

if __name__ == "__main__":
    test_quick_app_stream()
    test_quick_app_no_stream()