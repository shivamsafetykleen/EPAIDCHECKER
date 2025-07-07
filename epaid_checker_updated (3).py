
import streamlit as st
import requests
import re

# -------------------------------
# Configuration
# -------------------------------
st.set_page_config(page_title="EPA ID Checker", layout="centered")

# -------------------------------
# Branding and Header
# -------------------------------
st.markdown(
    "<h1 style='color:#e4002b;'>EPA ID Checker</h1>",
    unsafe_allow_html=True
)

# -------------------------------
# State and Generator Type Logic
# -------------------------------
state_epa_requirements = {
    "California": {"VSQG": "No", "SQG": "Yes", "LQG": "Yes"},
    "Texas": {"VSQG": "Yes", "SQG": "Yes", "LQG": "Yes"},
    "New York": {"VSQG": "No", "SQG": "Yes", "LQG": "Yes"},
    "Florida": {"VSQG": "No", "SQG": "Yes", "LQG": "Yes"},
    "Illinois": {"VSQG": "Yes", "SQG": "Yes", "LQG": "Yes"},
    # Add more states as needed
}

epa_links = {
    "California": "https://www.dtsc.ca.gov/database/CalEPAID/",
    "Texas": "https://www.tceq.texas.gov/permitting/waste_permits/ihw/epa_id.html",
    "New York": "https://www.dec.ny.gov/chemical/8786.html",
    "Florida": "https://floridadep.gov/waste/permitting-compliance-assistance/content/epa-id-numbers",
    "Illinois": "https://www.epa.illinois.gov/topics/waste-management/rcra/epa-id/index"
}

# -------------------------------
# State Selection
# -------------------------------
state_input = st.text_input("Enter State Name")
matching_states = [state for state in state_epa_requirements if state_input.lower() in state.lower()]
selected_state = st.selectbox("Select a State", matching_states) if matching_states else None

# -------------------------------
# Generator Type Selection
# -------------------------------
generator_type = st.radio("Select Generator Category", ["VSQG", "SQG", "LQG"])

# -------------------------------
# Display EPA ID Requirement
# -------------------------------
if selected_state and generator_type:
    fed_required = "Yes" if generator_type in ["SQG", "LQG"] else "No"
    state_required = state_epa_requirements[selected_state][generator_type]
    st.markdown(f"**Federal EPA ID Required:** {fed_required}")
    st.markdown(f"**{selected_state} EPA ID Required:** {state_required}")

    if selected_state in epa_links:
        st.markdown(f"[Visit {selected_state} EPA Site]({epa_links[selected_state]})")

# -------------------------------
# Real-Time EPA ID Validation
# -------------------------------
st.markdown("---")
st.subheader("Check EPA ID Status (Real-Time)")

handler_id = st.text_input("Enter EPA ID (Handler ID)")
username = st.text_input("RCRAInfo Username")
password = st.text_input("RCRAInfo Password", type="password")

def validate_epa_id_real_time(handler_id, username, password):
    url = "https://rcrainfo.epa.gov/rcrainfoweb/modules/public/handler/search"
    payload = {
        "handlerId": handler_id,
        "includeInactiveSites": True
    }
    try:
        response = requests.post(url, json=payload, auth=(username, password))
        if response.status_code == 200:
            data = response.json()
            if data and "handlers" in data and data["handlers"]:
                return data["handlers"][0]
            else:
                return {"message": "EPA ID not found or inactive."}
        else:
            return {"error": f"Request failed with status code {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

if st.button("Check EPA ID"):
    if handler_id and username and password:
        result = validate_epa_id_real_time(handler_id, username, password)
        if "error" in result:
            st.error(result["error"])
        elif "message" in result:
            st.warning(result["message"])
        else:
            st.success("EPA ID is active.")
            st.json(result)
    else:
        st.warning("Please enter all fields.")

# -------------------------------
# Footer
# -------------------------------
st.markdown(
    "<div style='position: fixed; bottom: 10px; right: 10px; font-size: 12px; color: gray;'>Created by Shivam</div>",
    unsafe_allow_html=True
)
