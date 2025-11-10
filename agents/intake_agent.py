from utils.watsonx_client import generate

def run_symptoms_intake(user_input: str) -> str:
    prompt = f"""
You are a helpful health assistant. A user says: "{user_input}"
Ask any necessary follow-up questions to clarify their symptoms, duration, and severity.

Then, provide a clear, one-paragraph summary of the user's condition.
For example: "The user is experiencing a severe headache and slight dizziness which started 2 days ago."
"""
    return generate(prompt)