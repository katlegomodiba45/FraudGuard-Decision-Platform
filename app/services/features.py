def build_features(transaction) -> dict:
    return {
        "amount": float(transaction.amount),
        "country": transaction.country,
        "velocity_1h": int(transaction.velocity_1h),
        "hour": int(getattr(transaction, "hour", 12)),
        "amount_vs_avg": float(getattr(transaction, "amount_vs_avg", 1.0)),
    }