import streamlit as st
import re

# Sample state list for demonstration
state_list = ["California", "Texas", "New York", "Florida", "Illinois"]

# Sample comments for demonstration
comment_text = """
This facility is not permitted to handle hazardous waste.
All operations must comply with state regulations.
The facility is allowed to process non-hazardous waste.
"""

# EPA links dictionary
epa_links = {
    "California": "https://www.dtsc.ca.gov/database/CalEPAID/",
    "Texas": "https://www.tceq.texas.gov/permitting/waste_permits/ihw/epa_id.html",
    "New York": "https://www.dec.ny.gov/chemical/8786.html",
    "Florida": "https://floridadep.gov/waste/permitting-compliance-assistance/content/epa-id-numbers",
    "Illinois": "https://www.epa.illinois.gov/topics/waste-management/rcra/epa-id/index"
}

# Function to highlight keywords in comments
def highlight_keywords(text):
    keywords = ["not permitted", "allowed", "must", "required", "prohibited"]
    for word in keywords:
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        text = pattern.sub(f"<span style='color:red; font-weight:bold'>{word}</span>", text)
    return text

# Streamlit app
st.title("EPA ID Checker")

# Search bar for state
state_input = st.text_input("Enter State Name")
matching_states = [state for state in state_list if state_input.lower() in state.lower()]
selected_state = st.selectbox("Select a State", matching_states) if matching_states else None

# Display comments with highlighted keywords
st.markdown(highlight_keywords(comment_text), unsafe_allow_html=True)

# Display EPA website link for the selected state
if selected_state in epa_links:
    st.markdown(f"Visit {selected_state} EPA Site")
