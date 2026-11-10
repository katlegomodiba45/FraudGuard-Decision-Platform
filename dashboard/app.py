import streamlit as st
import requests

st.set_page_config(page_title="FraudGuard", layout="centered")
st.title("FraudGuard - Transaction Check")
st.write("Check if a transaction looks fraudulent.")

amount = st.number_input("Amount (R)", min_value=0.0, value=500.0)
hour = st.slider("Hour of day", 0, 23, 12)
velocity_1h = st.number_input("Transactions in last 1 hour", min_value=0, value=1)
amount_vs_avg = st.number_input("Amount vs your average (e.g. 1.0 = normal, 5.0 = 5x bigger)", min_value=0.0, value=1.0)

if st.button("Check Transaction"):
    payload = {
        "amount": amount,
        "hour": hour,
        "velocity_1h": velocity_1h,
        "amount_vs_avg": amount_vs_avg
    }
    try:
        response = requests.post("https://fraudguard-api.onrender.com/score", json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()
        score = result.get("fraud_score", 0)
        decision = result.get("decision", "UNKNOWN")
        st.metric("Fraud Score", f"{score:.2f}")
        if decision == "BLOCK":
            st.error(f"Decision: {decision} - Block this transaction")
        elif decision == "REVIEW":
            st.warning(f"Decision: {decision} - Send for manual review")
        else:
            st.success(f"Decision: {decision} - Allow transaction")
        st.json(result)
    except Exception as e:
        st.error(f"API error: {e}")