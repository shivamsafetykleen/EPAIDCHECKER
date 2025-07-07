import streamlit as st
import re

# Full EPA links dictionary for all 50 U.S. states
epa_links = {'Alabama': 'https://www.adem.alabama.gov/', 'Alaska': 'https://dec.alaska.gov/', 'Arizona': 'https://azdeq.gov/', 'Arkansas': 'https://www.adeq.state.ar.us/', 'California': 'https://www.dtsc.ca.gov/database/CalEPAID/', 'Colorado': 'https://cdphe.colorado.gov/', 'Connecticut': 'https://portal.ct.gov/DEEP', 'Delaware': 'https://dnrec.alpha.delaware.gov/', 'Florida': 'https://floridadep.gov/', 'Georgia': 'https://epd.georgia.gov/', 'Hawaii': 'https://health.hawaii.gov/shwb/', 'Idaho': 'https://www.deq.idaho.gov/', 'Illinois': 'https://www.epa.illinois.gov/', 'Indiana': 'https://www.in.gov/idem/', 'Iowa': 'https://www.iowadnr.gov/', 'Kansas': 'https://www.kdhe.ks.gov/', 'Kentucky': 'https://eec.ky.gov/', 'Louisiana': 'https://deq.louisiana.gov/', 'Maine': 'https://www.maine.gov/dep/', 'Maryland': 'https://mde.maryland.gov/', 'Massachusetts': 'https://www.mass.gov/orgs/massachusetts-department-of-environmental-protection', 'Michigan': 'https://www.michigan.gov/egle', 'Minnesota': 'https://www.pca.state.mn.us/', 'Mississippi': 'https://www.mdeq.ms.gov/', 'Missouri': 'https://dnr.mo.gov/', 'Montana': 'https://deq.mt.gov/', 'Nebraska': 'https://deq.ne.gov/', 'Nevada': 'https://ndep.nv.gov/', 'New Hampshire': 'https://www.des.nh.gov/', 'New Jersey': 'https://www.nj.gov/dep/', 'New Mexico': 'https://www.env.nm.gov/', 'New York': 'https://www.dec.ny.gov/', 'North Carolina': 'https://deq.nc.gov/', 'North Dakota': 'https://deq.nd.gov/', 'Ohio': 'https://epa.ohio.gov/', 'Oklahoma': 'https://www.deq.ok.gov/', 'Oregon': 'https://www.oregon.gov/deq/', 'Pennsylvania': 'https://www.dep.pa.gov/', 'Rhode Island': 'https://dem.ri.gov/', 'South Carolina': 'https://www.scdhec.gov/', 'South Dakota': 'https://denr.sd.gov/', 'Tennessee': 'https://www.tn.gov/environment.html', 'Texas': 'https://www.tceq.texas.gov/', 'Utah': 'https://deq.utah.gov/', 'Vermont': 'https://dec.vermont.gov/', 'Virginia': 'https://www.deq.virginia.gov/', 'Washington': 'https://ecology.wa.gov/', 'West Virginia': 'https://dep.wv.gov/', 'Wisconsin': 'https://dnr.wisconsin.gov/', 'Wyoming': 'https://deq.wyoming.gov/'}

# Sample state list from the dictionary
state_list = list(epa_links.keys())

# Sample comments for demonstration
comment_text = '''
This facility is not permitted to handle hazardous waste.
All operations must comply with state regulations.
The facility is allowed to process non-hazardous waste.
'''

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
    st.markdown(f"[Visit {selected_state} EPA Site]({epa_links[selected_state]})")