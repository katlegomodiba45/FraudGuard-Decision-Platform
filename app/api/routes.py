from fastapi import APIRouter
from app.api.schemas import TransactionRequest, ScoreResponse
from app.services.features import build_features
from app.services.model import score_transaction
from app.services.decision import decide, risk_level
from app.services.monitoring import log_decision

router = APIRouter(tags=["Scoring"])

@router.post("/score", response_model=ScoreResponse, summary="Score a transaction for fraud")
def score_endpoint(transaction: TransactionRequest):
    """
    Full fraud pipeline in 1 call:
    1. Build features from raw transaction
    2. Score it with the model (0.0 - 1.0)
    3. Decide APPROVE / REVIEW / BLOCK
    4. Log the decision for audit
    """
    # 1. Features
    features = build_features(transaction)

    # 2. Model score
    score = score_transaction(features)

    # 3. Decision + Risk
    decision, reason = decide(score)
    level = risk_level(score)

    # 4. Audit log - this creates decisions.csv
    log_decision(transaction.amount, score, decision)

    return {
        "fraud_score": score,
        "decision": decision,
        "risk_level": level,
        "reason": reason,
    }