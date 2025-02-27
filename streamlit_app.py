import streamlit as st

# Centering the title using Markdown and HTML
st.markdown("<h1 style='text-align: center;'>Power BI Dashboard in Streamlit</h1>", unsafe_allow_html=True)

# Replace with your Power BI embed URL
power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiOTYxN2M2ZmQtNjNhMy00YzhhLTlmNWQtMjNkYzM5ZWY2NjcwIiwidCI6ImE4ZDNlMTJhLWE0ZjktNDdjMy1iN2JkLTBmMThmNTBjNDcxMyIsImMiOjN9"

st.components.v1.iframe(power_bi_url, width=900, height=600)
