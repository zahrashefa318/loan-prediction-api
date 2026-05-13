from services.authorization_check import is_authorized
from datetime import datetime, timedelta
import jwt

def test_expired_token(client,override_env):
    def create_expired_token():
        payload={
            "sub":"exp_user",
            "iat":datetime.utcnow(),
            "exp":datetime.utcnow() - timedelta(minutes=30)
        }
        token=jwt.encode(payload,"test_secret",algorithm="HS256")
        return token
    response=client.post(url="/predict",
                headers={"Authorization":f"Bearer {create_expired_token()}",
                         "Idempotency-Key":"My_test_123"},
                json={
                            "income": 5000,
                            "savings": 2000,
                            "expenses": 1500,
                            "family_size": 3,
                            "years_employed": 5,
                            "age": 30,
                            "rent": 800,
                            "debt": 1000
        })
    assert response.json()["detail"] == "Token expired"
    assert response.status_code == 401


