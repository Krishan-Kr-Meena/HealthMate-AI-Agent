from utils.watsonx_client import generate

def run_planner_agent(daily_plan_text: str) -> str:
    prompt = f"""
Take the following daily health plan and convert it into a simple schedule with suggested times.

Daily Plan:
{daily_plan_text}

Format the output as a simple list. For example:
* 08:00 AM - Eat healthy breakfast (from Diet plan)
* 09:00 AM - Walk for 30 minutes (from Exercise plan)
* 10:00 PM - Begin winding down for sleep (from Sleep plan)
"""
    return generate(prompt)
