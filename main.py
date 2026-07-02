import os
import argparse

from dotenv import load_dotenv
from openai import OpenAI

def main() -> None:
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY environment variable not set")

    client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)
    parser = argparse.ArgumentParser(
        description="Agent that accepts a task and works on it based on a set of predefined functions"
    )
    parser.add_argument(
        "user_prompt",
        type=str,
        help="User prompt"
    )
    args = parser.parse_args()
    messages=[
    {
        "role": "user",
        "content": args.user_prompt,
    }
]

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages
    )
    if not response.usage:
        raise RuntimeError("failed API request, please try again")
    
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")
    print("Response:")
    print(response.choices[0].message.content)
    

if __name__ == "__main__":
    main()
