# FraudGuard-Decision-Platform

Real-time fraud decision platform: ingestion -> features -> ML scoring -> decision -> monitoring.

## Tech Stack
Python 3.11+ | FastAPI | Pandas + Parquet | scikit-learn + XGBoost | Pydantic | Streamlit | Docker

## Run API
pip install -r requirements.txt
uvicorn app.main:app --reload

## Run Dashboard
streamlit run dashboard/app.py

## Tests
pytest