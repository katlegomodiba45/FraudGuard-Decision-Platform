import streamlit as st
import requests

st.set_page_config(page_title="FraudGuard Dashboard", page_icon="🛡️", layout="centered")

st.title("FraudGuard Dashboard")
st.markdown("Test transactions live against the FraudGuard API")

amount = st.slider("Amount (R)", min_value=10, max_value=15000, value=500, step=10)
hour = st.slider("Hour of day", min_value=0, max_value=23, value=12)
velocity = st.slider("Velocity (transactions in last 1h)", min_value=0, max_value=15, value=1)
amount_vs_avg = st.slider("Amount vs User Average", min_value=0.5, max_value=8.0, value=1.0, step=0.1)

if st.button("Score Transaction", type="primary"):
    payload = {
        "amount": amount,
        "hour": hour,
        "velocity_1h": velocity,
        "amount_vs_avg": amount_vs_avg
    }

    try:
        response = requests.post("http://localhost:8000/score", json=payload, timeout=5)
        response.raise_for_status()
        result = response.json()

        st.success("Transaction scored successfully")
        st.metric("Fraud Score", f"{result['fraud_score']:.4f}")
        st.metric("Decision", result["decision"])
        
        with st.expander("Full Response"):
            st.json(result)

    except requests.exceptions.ConnectionError:
        st.error("Cannot connect to the API. Make sure the FastAPI server is running on port 8000.")
    except Exception as e:
        st.error(f"Error: {e}")