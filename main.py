from utils.logger import append_log
from agents.intake_agent import run_symptoms_intake
from agents.diagnosis_agent import run_diagnosis
from agents.behavior_coach_agent import run_behavior_coach
from agents.planner_agent import run_planner_agent
from agents.reflector_agent import run_reflector

if __name__ == "__main__":
    print("🚀 Welcome to HealthMate AI - Powered by Watsonx\n")
    
    # --- Input Section ---
    symptom_description = input("🧑‍⚕️ Please describe your symptoms (e.g., 'fever and cough'): ")
    duration = input("⏳ How long have you had these symptoms (e.g., '3 days'): ")
    severity = ""
    while severity not in ["mild", "moderate", "severe"]:
        severity = input("🌡️ How severe are the symptoms (mild, moderate, severe): ").lower()
    # -------------------------

    print("\n🤖 Step 1: Intake Agent processing user input...")
    symptoms_text = run_symptoms_intake(symptom_description, duration, severity)
    print(f"✅ Symptoms Summary:\n{symptoms_text}\n") # Changed from JSON

    print("🩺 Step 2: Diagnosis Agent analyzing symptoms...")
    diagnosis_text = run_diagnosis(symptoms_text)
    print(f"✅ Diagnosis Suggestion:\n{diagnosis_text}\n")

    print("🧠 Step 3: Behavior Coach creating a daily plan...")
    plan_text = run_behavior_coach(diagnosis_text)
    print(f"✅ Daily Health Plan:\n{plan_text}\n")

    print("📅 Step 4: Planner Agent scheduling activities...")
    schedule_text = run_planner_agent(plan_text)
    print(f"✅ Schedule:\n{schedule_text}\n")

    user_feedback = input("💬 (Optional) Any feedback after following advice? ")

    print("🔁 Step 5: Reflector Agent reviewing feedback...")
    reflection_text = run_reflector(symptoms_text, diagnosis_text, user_feedback)
    print(f"✅ Reflection:\n{reflection_text}\n")

    # Log the entire interaction
    log_entry = {
        "symptom_description": symptom_description,
        "duration": duration,
        "severity": severity,
        "symptoms": symptoms_text, # Changed from JSON
        "diagnosis": diagnosis_text,
        "plan": plan_text,
        "schedule": schedule_text,
        "reflection": reflection_text,
        "feedback": user_feedback
    }

    append_log(log_entry)
