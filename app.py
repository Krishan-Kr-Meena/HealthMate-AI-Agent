import streamlit as st
from agents.intake_agent import run_symptoms_intake
from agents.diagnosis_agent import run_diagnosis
from agents.behavior_coach_agent import run_behavior_coach
from agents.planner_agent import run_planner_agent
from agents.reflector_agent import run_reflector
from utils.logger import append_log

st.set_page_config(page_title="HealthMate AI", layout="centered")
st.title("🏥 HealthMate AI")
st.markdown("An AI-powered health assistant for basic triage and wellness guidance.")

# Session state
if "pipeline_run" not in st.session_state:
    st.session_state.pipeline_run = False
if "feedback_given" not in st.session_state:
    st.session_state.feedback_given = False
if "data" not in st.session_state:
    st.session_state.data = {}

# Step 1: User Input
# Only show input if the pipeline hasn't run
if not st.session_state.pipeline_run:
    st.subheader("1. Enter Your Symptoms")
    symptom_description = st.text_area("🧑 Describe your main symptoms:", height=100)

    col1, col2 = st.columns(2)
    with col1:
        duration = st.text_input("⏳ Duration:", placeholder="e.g., 3 days")
    with col2:
        severity = st.selectbox(
            "🌡️ Severity:",
            ["", "mild", "moderate", "severe"],
            format_func=lambda x: "Select Severity" if x == "" else x.capitalize()
        )


    if st.button("🚀 Run HealthMate AI"):
        # Validate all inputs
        if not symptom_description.strip():
            st.warning("Please describe your symptoms.")
        elif not duration.strip():
            st.warning("Please enter the duration.")
        elif not severity.strip():
            st.warning("Please select the severity.")
        else:
            with st.spinner("🤖 Processing..."):
                # All agents now use plain text
                symptoms_text = run_symptoms_intake(symptom_description, duration, severity)
                diagnosis_text = run_diagnosis(symptoms_text)
                plan_text = run_behavior_coach(diagnosis_text)
                schedule_text = run_planner_agent(plan_text)

                st.session_state.data = {
                    "symptom_description": symptom_description,
                    "duration": duration,
                    "severity": severity,
                    "symptoms": symptoms_text,
                    "diagnosis": diagnosis_text,
                    "plan": plan_text,
                    "schedule": schedule_text
                }

                st.session_state.pipeline_run = True
                st.session_state.feedback_given = False
                st.rerun() # <-- FIX 1: Changed to st.rerun()

# Step 2: Show Plan and Ask for Feedback
if st.session_state.pipeline_run and not st.session_state.feedback_given:
    st.subheader("🩺 Symptoms Summary")
    st.markdown(st.session_state.data["symptoms"])

    st.subheader("📋 Diagnosis Suggestions")
    st.markdown(st.session_state.data["diagnosis"])

    st.subheader("🧘 Health Plan")
    st.markdown(st.session_state.data["plan"])

    st.subheader("🕒 Daily Schedule")
    st.markdown(st.session_state.data["schedule"])

    st.info("💬 Please review the plan and schedule above and share your feedback.")

    feedback = st.text_input("Your feedback (required to continue):", key="feedback_box")
    if st.button("Submit Feedback"):
        if not feedback.strip():
            st.warning("Please provide feedback before proceeding.")
        else:
            st.session_state.data["feedback"] = feedback
            st.session_state.feedback_given = True
            st.rerun() # <-- FIX 2: Changed to st.rerun()

# Step 3: Reflector
if st.session_state.feedback_given:
    st.subheader("🔍 Reflection & Suggestions")
    
    # Check if reflection is already generated
    if "reflection" not in st.session_state.data:
        with st.spinner("🔄 Reflecting..."):
            reflection_text = run_reflector(
                st.session_state.data["symptoms"],
                st.session_state.data["diagnosis"],
                st.session_state.data["feedback"]
            )
            st.session_state.data["reflection"] = reflection_text
            append_log(st.session_state.data)
    
    st.markdown(st.session_state.data["reflection"])
    st.success("✅ All done!")
    
    # --- NEW BUTTON ---
    # Add a button to reset the session state and start over
    if st.button("🔄 Check Another Symptom"):
        st.session_state.pipeline_run = False
        st.session_state.feedback_given = False
        st.session_state.data = {}
        st.rerun() # <-- FIX 3: Changed to st.rerun()

# Footer
st.markdown("---")
st.caption("⚠️ This assistant is for educational purposes only and does not replace professional medical advice.")
