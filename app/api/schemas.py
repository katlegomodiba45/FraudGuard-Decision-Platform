from pydantic import BaseModel

class TransactionRequest(BaseModel):
    amount: float
    country: str = "ZA"
    velocity_1h: int = 1
    user_id: str = "user_1"
    hour: int = 12
    amount_vs_avg: float = 1.0

class ScoreResponse(BaseModel):
    fraud_score: float
    decision: str
    risk_level: str
    reason: str