from app.core.config import settings

def decide(score: float) -> tuple[str, str]:
    if score >= settings.decision_threshold:
        return "BLOCK", f"Score {score:.2f} >= block threshold {settings.decision_threshold}"
    if score >= settings.review_threshold:
        return "REVIEW", f"Score {score:.2f} >= review threshold {settings.review_threshold}"
    return "APPROVE", f"Score {score:.2f} below thresholds - low risk"

def make_decision(score: float) -> str:
    decision, _ = decide(score)
    return decision

def risk_level(score: float) -> str:
    if score >= 0.75:
        return "HIGH"
    if score >= 0.45:
        return "MEDIUM"
    return "LOW"