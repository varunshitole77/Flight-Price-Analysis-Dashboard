import streamlit as st

st.title("Power BI Dashboard in Streamlit")

# Replace with your Power BI embed URL
power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiOTYxN2M2ZmQtNjNhMy00YzhhLTlmNWQtMjNkYzM5ZWY2NjcwIiwidCI6ImE4ZDNlMTJhLWE0ZjktNDdjMy1iN2JkLTBmMThmNTBjNDcxMyIsImMiOjN9"

st.components.v1.iframe(power_bi_url, width=900, height=600)
