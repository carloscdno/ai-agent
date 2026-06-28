import os
import argparse

from dotenv import load_dotenv
from google import genai
from google.genai import types




def main() -> None:
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    client = genai.Client(api_key=api_key)
    parser = argparse.ArgumentParser(
        description="Agent that accepts a task and works on it based on a set of predefined functions"
    )
    parser.add_argument(
        "user_prompt",
        type=str,
        help="User prompt"
    )
    args = parser.parse_args()
    messages: list[types.Content] = [
    types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
    ]
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages
    )
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()
