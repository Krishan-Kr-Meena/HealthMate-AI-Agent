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

# Session state to preserve steps
if "pipeline_run" not in st.session_state:
    st.session_state.pipeline_run = False
if "feedback_given" not in st.session_state:
    st.session_state.feedback_given = False
if "data" not in st.session_state:
    st.session_state.data = {}

# Step 1: User Input
user_input = st.text_area("🧑 Describe your symptoms:", height=150)

if st.button("🚀 Run HealthMate AI"):
    if not user_input.strip():
        st.warning("Please enter your symptoms.")
    else:
        with st.spinner("🤖 Processing..."):
            # Run the pipeline with new text-based outputs
            symptoms_text = run_symptoms_intake(user_input)
            diagnosis_text = run_diagnosis(symptoms_text)
            plan_text = run_behavior_coach(diagnosis_text)
            schedule_text = run_planner_agent(plan_text)

            st.session_state.data = {
                "user_input": user_input,
                "symptoms": symptoms_text,
                "diagnosis": diagnosis_text,
                "plan": plan_text,
                "schedule": schedule_text
            }

            st.session_state.pipeline_run = True
            st.session_state.feedback_given = False

# Step 2: Show Plan and Ask for Feedback
if st.session_state.pipeline_run and not st.session_state.feedback_given:
    st.subheader("🩺 Symptoms Summary")
    st.markdown(st.session_state.data["symptoms"]) # Changed from st.json

    st.subheader("📋 Diagnosis Suggestions")
    st.markdown(st.session_state.data["diagnosis"]) # Changed from st.json

    st.subheader("🧘 Health Plan")
    st.markdown(st.session_state.data["plan"]) # Changed from st.json

    st.subheader("🕒 Daily Schedule")
    st.markdown(st.session_state.data["schedule"]) # Changed from st.json

    st.info("💬 Please review the plan and schedule above and share your feedback.")

    feedback = st.text_input("Your feedback (required to continue):", key="feedback_box")
    if st.button("Submit Feedback"):
        if not feedback.strip():
            st.warning("Please provide feedback before proceeding.")
        else:
            st.session_state.data["feedback"] = feedback
            st.session_state.feedback_given = True

# Step 3: Reflector
if st.session_state.feedback_given:
    with st.spinner("🔄 Reflecting..."):
        reflection_text = run_reflector(
            st.session_state.data["symptoms"],
            st.session_state.data["diagnosis"],
            st.session_state.data["feedback"]
        )

        st.session_state.data["reflection"] = reflection_text

        # Log the complete interaction
        # Note: The logger will now log plain text for most fields
        append_log(st.session_state.data)

    st.subheader("🔍 Reflection & Suggestions")
    st.markdown(reflection_text) # Changed from st.json

    st.success("✅ All done! You can restart with new input anytime.")

# Footer
st.markdown("---")
st.caption("⚠️ This assistant is for educational purposes only and does not replace professional medical advice.")