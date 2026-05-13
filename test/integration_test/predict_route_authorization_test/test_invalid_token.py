from fastapi import status
def test_invalid_token(client):
    response=client.post(url="/predict",
                         headers={
                             "Idempotency-Key":"test_idem",
                             "Authorization":"Bearer lsakfjlskdhf876876"
                         },
                         json={
                                "income": 5000,
                                "savings": 2000,
                                "expenses": 1500,
                                "family_size": 3,
                                "years_employed": 5,
                                "age": 30,
                                "rent": 800,
                                "debt": 1000
                                            }
                         )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json()["detail"] == "Invalid token"