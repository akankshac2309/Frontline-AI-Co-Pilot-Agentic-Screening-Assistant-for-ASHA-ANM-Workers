import sys
import os

# Allow access to parent folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from agents.tb_agent import assess_tb_risk

st.title("AI Co-Pilot for TB Screening")

st.write("Assist frontline health workers in identifying possible TB cases.")

symptoms = st.text_input("Enter patient symptoms")

if st.button("Analyze"):

    if symptoms.strip() == "":
        st.warning("Please enter symptoms.")
    else:
        result = assess_tb_risk(symptoms)

        st.subheader("Screening Report")

        st.write("**Risk Level:**", result["risk"])
        st.write("**Reason:**", result["reason"])

        st.write("### Relevant Guidelines")
        for g in result["guidelines"]:
            st.write("-", g)

        st.write("**Recommended Action:**", result["recommendation"])
        st.write("**Escalation:**", result["escalation"])
        st.write("**Confidence:**", result["confidence"])