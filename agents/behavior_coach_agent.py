from utils.watsonx_client import generate

def run_behavior_coach(diagnosis_summary: str) -> str:
    prompt = f"""
Given the diagnosis summary:
{diagnosis_summary}

Create a daily health plan as a simple bulleted list.
Include actionable checklist items for:
- Diet
- Exercise
- Sleep
- Stress reduction

For example:
* **Diet:** Eat 3 servings of vegetables and drink 8 glasses of water.
* **Exercise:** Go for a 30-minute brisk walk.
* **Sleep:** Aim for 7-8 hours of sleep, avoiding screens 1 hour before bed.
* **Stress:** Practice 5 minutes of deep breathing exercises.
"""
    return generate(prompt)