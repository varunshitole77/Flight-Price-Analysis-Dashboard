import streamlit as st

st.title.center("Flight Price Analysis")

# Replace with your Power BI embed URL
power_bi_url = "https://app.powerbi.com/view?r=eyJrIjoiOTYxN2M2ZmQtNjNhMy00YzhhLTlmNWQtMjNkYzM5ZWY2NjcwIiwidCI6ImE4ZDNlMTJhLWE0ZjktNDdjMy1iN2JkLTBmMThmNTBjNDcxMyIsImMiOjN9"

st.components.v1.iframe(power_bi_url, width=1000, height=1000)
