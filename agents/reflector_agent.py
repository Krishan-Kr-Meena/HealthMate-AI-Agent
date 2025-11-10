# import json  <- No longer needed
from utils.watsonx_client import generate

# LOG_FILE = "data/user_logs.json"  <- No longer needed

# def read_logs():  <- No longer needed
#     try:
#         with open(LOG_FILE, "r") as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return []

def run_reflector(symptoms: str, diagnosis: str, feedback: str) -> str:
    # logs = read_logs()  <- No longer needed
    # last_few_logs = logs[-5:] if logs else []  <- No longer needed

    prompt = f"""
You are an AI health reflection agent.

CURRENT SESSION:
- Symptoms Summary: {symptoms}
- Diagnosis Output: {diagnosis}
- User Feedback: "{feedback}"

Your task is to provide a concise reflection and 1-2 suggestions based on the user's feedback.
Do not add any extra headers or summaries.
Use simple bullet points.

Format your response exactly like this, including "End of session":

End of session

Reflection:
* [Your 1-sentence reflection on the user's feedback]

Suggestions:
* [Your 1st concrete suggestion for system improvement]
* [Your 2nd concrete suggestion for system improvement (if any)]

End of session
"""

    return generate(prompt)
