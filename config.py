import os
from dotenv import load_dotenv

load_dotenv()
MISTRAL_API_KEY = os.getenv('MISTRAL_API_KEY')
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
LLM_MODEL = "deepseek/deepseek-v3-0324"
# LLM_MODEL = "open-mistral-nemo"