# AI Agent CLI

A simple command-line AI agent built in Python. It uses an LLM (via OpenRouter)
to understand natural language instructions and perform actions on a codebase,
such as reading files, listing directories, and writing/fixing code.

## Features

- Reads and understands your codebase
- Executes Python files
- Reads, writes, and modifies files
- Uses function calling to let the LLM decide which actions to take

## Requirements

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) installed
- An OpenRouter API key

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/carloscdno/ai-agent.git
   cd ai-agent
   ```

2. Install dependencies with uv:
   ```bash
   uv sync
   ```

3. Add your OpenRouter API key to a `.env` file:
   ```
   OPENROUTER_API_KEY=your_key_here
   ```

## Usage

Run the agent with a prompt describing the task:

```bash
uv run main.py "fix the bug in calculator.py"
```

## Warning

This is a toy/educational project. Be cautious about giving any LLM-based agent
access to your filesystem or ability to execute code. Please always review changes
before trusting them in a real project.

## Acknowledgments

Built as part of the [Boot.dev](https://www.boot.dev) "Build an AI Agent in Python" course.