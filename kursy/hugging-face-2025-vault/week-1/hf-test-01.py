# MK: 2025-02-16
# Ten skrypt zadziałał! 

from huggingface_hub import login, HfApi
from dotenv import load_dotenv
import os

load_dotenv()

# Logowanie (wymagane do push_to_hub)
login(token=os.getenv("API_TOKEN_HF"))

# Inicjalizacja API
api = HfApi()

# Wyszukiwanie modeli
models = api.list_models(filter="text-classification")

# Pobranie konkretnego modelu
api.snapshot_download(repo_id="bert-base-uncased")
