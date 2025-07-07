
import streamlit as st
import re

# Sample data for demonstration
states = ["California", "Texas", "New York", "Florida", "Illinois"]
generator_types = ["VSQG", "SQG", "LQG"]

# Sample logic for determining if EPA ID is required
def requires_epa_id(state, generator_type):
    if generator_type == "VSQG":
        return "EPA ID may not be required for VSQG in most states."
    elif generator_type == "SQG":
        return "EPA ID is typically required for SQG."
    elif generator_type == "LQG":
        return "EPA ID is required for LQG."
    else:
        return "Unknown generator type."

# Simulated EPA ID validation (for demonstration)
def is_epa_id_active(epa_id):
    # Simulate check: assume IDs ending in even digit are active
    if epa_id and epa_id[-1].isdigit():
        return int(epa_id[-1]) % 2 == 0
    return False

# Streamlit UI
st.set_page_config(page_title="EPA ID Checker", layout="centered")

st.title("EPA ID Requirement Checker")

# State selection
selected_state = st.selectbox("Select a State", states)

# Generator type selection
selected_generator = st.radio("Select Generator Category", generator_types)

# Display requirement result
if selected_state and selected_generator:
    result = requires_epa_id(selected_state, selected_generator)
    st.markdown(f"### Result:\n{result}")

# EPA ID input and check
st.markdown("---")
epa_id_input = st.text_input("Enter EPA ID to check if it's active")

if epa_id_input:
    if is_epa_id_active(epa_id_input):
        st.success("✅ The EPA ID appears to be active.")
    else:
        st.error("❌ The EPA ID appears to be inactive or invalid.")

# Footer
st.markdown(
    "<div style='position: fixed; bottom: 10px; right: 10px; font-size: 12px; color: gray;'>Created by Shivam</div>",
    unsafe_allow_html=True
)
