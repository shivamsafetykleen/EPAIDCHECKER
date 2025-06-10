
import pandas as pd
import streamlit as st

# Load the reshaped EPA data
df = pd.read_excel('reshaped_epa_data.xlsx', engine='openpyxl')

st.title("EPA ID Requirements Checker")

# Dropdowns
state = st.selectbox("Select State", df['State'].unique())
generator_status = st.selectbox("Select Generator Status", ['VSQG', 'SQG', 'LQG'])

# Filter and display
filtered = df[(df['State'] == state) & (df['Generator Status'] == generator_status)]
if not filtered.empty:
    st.write("**Federal EPA ID Requirement:**", filtered.iloc[0]['Federal EPA ID Requirement'])
    st.write("**State EPA ID Requirement:**", filtered.iloc[0]['State EPA ID Requirement'])
    st.write("**Comments:**", filtered.iloc[0]['Comments'])
else:
    st.warning("No data found for the selected combination.")
