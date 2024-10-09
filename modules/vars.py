import os

API_ID    = os.environ.get("API_ID", "23917270")
API_HASH  = os.environ.get("API_HASH", "596a4c1d72ba6d00056f8733f6f3e5fb")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
