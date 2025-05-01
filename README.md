# Langbase API Integration

A simple Python script that demonstrates how to interact with the Langbase API to use the concise-summarizer-agent.

## What is this?

This project provides a basic implementation for sending text to the Langbase API's concise-summarizer-agent and receiving summarized responses. It demonstrates proper API authentication using environment variables for secure API key management.

## Setup

1. Clone this repository
2. Install dependencies:
   ```
   pip install requests python-dotenv
   ```
3. Create a `.env` file in the project root with your Langbase API key:
   ```
   LANGBASE_API_KEY=your_api_key_here
   ```

## How to Run

1. Ensure your `.env` file contains a valid Langbase API key
2. Run the script:
   ```
   python runme.py
   ```
3. The script will send a sample text to the summarizer agent and print the response

## Security Notes

- The API key is stored in a `.env` file which is excluded from version control via `.gitignore`
- Environment variables are used to securely access the API key at runtime
- Never hardcode API keys or include them in client-side code