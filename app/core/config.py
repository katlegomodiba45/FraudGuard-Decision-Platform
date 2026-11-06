from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FraudGuard"
    decision_threshold: float = 0.75
    review_threshold: float = 0.45

settings = Settings()