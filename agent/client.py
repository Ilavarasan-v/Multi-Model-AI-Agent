# agent/client.py
# Creates and exports the Groq client instance.
# Every module that needs to talk to Groq imports `client` from here.

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("Groq_API_Key"))