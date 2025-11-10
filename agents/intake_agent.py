from utils.watsonx_client import generate

def run_symptoms_intake(symptom_description: str, duration: str, severity: str) -> str:
    prompt = f"""
You are a health assistant.
A user has provided the following information:
- Symptoms description: "{symptom_description}"
- Duration: "{duration}"
- Severity: "{severity}"

Your task is to summarize this information into a single, clear paragraph.
Start by restating the user's condition.

Example output:
"You are experiencing {symptom_description} which has lasted for {duration}, and you've described it as {severity}."
"""
    return generate(prompt)
