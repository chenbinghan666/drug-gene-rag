import os
from dotenv import load_dotenv
def load_config():
    load_dotenv()
    config = {
        "ZAI_API_KEY": os.getenv("ZAI_API_KEY"),
        "email": os.getenv("email")
    }
    return config
