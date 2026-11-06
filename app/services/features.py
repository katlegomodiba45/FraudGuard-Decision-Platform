def build_features(transaction) -> dict:
    return {
        "amount": float(transaction.amount),
        "country": transaction.country,
        "velocity_1h": int(transaction.velocity_1h),
    }