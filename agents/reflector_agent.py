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
    last_few_logs = logs[-5:] if logs else []

    prompt = f"""
You are an AI health reflection agent.

CURRENT SESSION:
- Symptoms Summary: {symptoms}
- Diagnosis Output: {diagnosis}
- User Feedback: "{feedback}"

RECENT HISTORY (last {len(last_few_logs)} sessions, as JSON):
{json.dumps(last_few_logs, indent=2)}

Your task is to provide a concise, 2-3 point summary based on the feedback.
Use bullet points.

Format your response exactly like this:
**Reflection:**
* [Your 1-sentence reflection on the user's feedback]

**Suggestions:**
* [Your 1st concrete suggestion for improvement]
* [Your 2nd concrete suggestion (if any)]
"""

    return generate(prompt)
