import json
from utils.watsonx_client import generate

LOG_FILE = "data/user_logs.json"

def read_logs():
    try:
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def run_reflector(symptoms: str, diagnosis: str, feedback: str) -> str:
    logs = read_logs()
    # Note: Logs are still JSON, but the *current* data is text.
    last_few_logs = logs[-5:] if logs else [] 

    prompt = f"""
You are an AI health reflection agent.

CURRENT SESSION:
- Symptoms Summary: {symptoms}
- Diagnosis Output: {diagnosis}
- User Feedback: "{feedback}"

RECENT HISTORY (last {len(last_few_logs)} sessions, as JSON):
{json.dumps(last_few_logs, indent=2)}

Your task:
1. Reflect on how the session went based on the user's feedback.
2. Suggest one concrete way the system could improve its prompts, response handling, or personalization.

Format your response clearly:
**Reflection:** [Your reflection here]
**Suggestion:** [Your suggestion here]
"""

    return generate(prompt)