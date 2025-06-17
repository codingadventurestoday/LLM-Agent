import os 
from dotenv import load_dotenv
from google import genai
import sys

def main():
    if not len(sys.argv) > 1:
        sys.exit(1)

    if not isinstance(sys.argv[0], str):
        sys.exit("not a string")
    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=sys.argv[0]
    )

    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()