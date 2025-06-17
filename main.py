import os 
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

def main():
    if not len(sys.argv) > 1:
        sys.exit(1)

    if not isinstance(sys.argv[0], str):
        sys.exit("not a string")
    
    user_prompt = " ".join(sys.argv[1:])

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    client = genai.Client(api_key=api_key)
    generate_content(client, messages)


def generate_content(client, messages):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()