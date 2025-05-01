import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

url = "https://api.langbase.com/nurettin-senyer11123/concise-summarizer-agent-ff2e"
headers = {
    "Authorization": f"Bearer {os.environ.get('LANGBASE_API_KEY')}",
    "Content-Type": "application/json"
}
payload = {"input":"Based on the code I can see, this appears to be a project "
"that interacts with the Langbase API to use a concise-summarizer-agent. "
"The code makes HTTP requests to the Langbase API endpoint with authentication and "
"receives responses from the agent. The main functionality seems to be sending input to a"
" summarization service and processing the response."}

response = requests.post(url, headers=headers, json=payload)

if not response.ok:
    raise Exception(f"Error: {response.text}")

agent_response = response.json()
print("Agent response:", agent_response)
