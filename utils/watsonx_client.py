from dotenv import load_dotenv
import os
from ibm_watsonx_ai.credentials import Credentials
from ibm_watsonx_ai.foundation_models.schema import TextGenParameters
from ibm_watsonx_ai.foundation_models import ModelInference

load_dotenv()

API_KEY = os.getenv("API_KEY")
PROJECT_ID = os.getenv("PROJECT_ID")
URL = os.getenv("URL")
MODEL_ID = "ibm/granite-3-8b-instruct"

credentials = Credentials(
    api_key=API_KEY,
    url=URL
)

parameters = TextGenParameters(
    decoding_method="greedy",
    max_new_tokens=300
)

model = ModelInference(
    model_id=MODEL_ID,
    project_id=PROJECT_ID,
    credentials=credentials,
    params=parameters
)

def generate(prompt: str) -> str:
    response = model.generate_text(prompt)
    return response
