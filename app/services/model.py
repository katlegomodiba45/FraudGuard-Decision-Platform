from typing import Dict

def score_transaction(features: Dict) -> float:
    """
    Score a transaction for fraud risk.
    Returns a probability between 0 and 1.
    """
    score = 0.08  # base risk

    amount = float(features.get("amount", 0))
    hour = int(features.get("hour", 12))
    velocity_1h = float(features.get("velocity_1h", 0))
    amount_vs_avg = float(features.get("amount_vs_avg", 1.0))

    # Amount risk
    if amount > 5000:
        score += 0.35
    elif amount > 2000:
        score += 0.22
    elif amount > 800:
        score += 0.12

    # Night time risk
    if hour >= 22 or hour <= 5:
        score += 0.18

    # High velocity
    if velocity_1h >= 5:
        score += 0.25
    elif velocity_1h >= 3:
        score += 0.15

    # Amount much higher than user average
    if amount_vs_avg >= 4.0:
        score += 0.28
    elif amount_vs_avg >= 2.5:
        score += 0.16

    return round(max(0.0, min(0.99, score)), 4)