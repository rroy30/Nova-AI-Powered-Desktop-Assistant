import os

# The name of your AI assistant
ASSISTANT_NAME = "nova"

# Securely retrieve the API key from your system environment variables
# You will need to set 'GROQ_API_KEY' on your computer locally
GROQ_API_KEY = os.getenv("GROQ_API_KEY")