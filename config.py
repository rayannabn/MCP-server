"""
Configuration and environment setup
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY environment variable is not set. "
        "Please set it or create a .env file with your API key."
    )

# Application Configuration
APP_NAME = "AI Calculator"
APP_VERSION = "1.0"
MODEL = "gpt-4o-mini"
