from app.core.config import settings

def decide(score: float) -> tuple[str, str]:
    """Returns (decision, reason) — single source of truth."""
    block_at = getattr(settings, "decision_threshold", 0.75)
    review_at = getattr(settings, "review_threshold", 0.45)

    if score >= block_at:
        return "BLOCK", f"Score {score:.2f} >= block threshold {block_at}"
    if score >= review_at:
        return "REVIEW", f"Score {score:.2f} >= review threshold {review_at}"
    return "APPROVE", f"Score {score:.2f} below thresholds - low risk"

def make_decision(score: float) -> str:
    """Backwards-compatible wrapper for routes.py / tests."""
    decision, _ = decide(score)
    return decision

def risk_level(score: float) -> str:
    if score >= 0.75:
        return "HIGH"
    if score >= 0.45:
        return "MEDIUM"
    return "LOW"