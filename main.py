import os
import json
import argparse

from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from call_function import available_functions

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
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output"
    )
    args = parser.parse_args()
    messages=[
    {
        "role": "system",
        "content": system_prompt
    },
    {
        "role": "user",
        "content": args.user_prompt,
    }
]

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        temperature=0,
        tools=available_functions
    )
    if not response.usage:
        raise RuntimeError("failed API request, please try again")
    
    message = response.choices[0].message
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
        print("Response:")
    
    if message.tool_calls:
        for tool_call in message.tool_calls:
            function_args = json.loads(tool_call.function.arguments or "{}")
            function_name = tool_call.function.name
            print(f"{function_name}({function_args})")
    else:
        print(message.content)

if __name__ == "__main__":
    main()
