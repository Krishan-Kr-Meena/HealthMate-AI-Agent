from utils.watsonx_client import generate

def run_diagnosis(symptom_summary: str) -> str:
    prompt = f"""
Based on the following symptom summary:
"{symptom_summary}"

List the top 3 possible conditions (this is not a final diagnosis).
Then, provide clear advice on what the user should do next.

Format your response clearly, for example:
**Possible Conditions:**
* Condition 1
* Condition 2
* Condition 3

**Advice:**
[Your advice here]
"""
    return generate(prompt)