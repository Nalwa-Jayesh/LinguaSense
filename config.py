import os
from dotenv import load_dotenv

load_dotenv()
MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY')
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
LLM_MODEL = "google/gemma-7b-it"
# LLM_MODEL = "open-mistral-nemo"