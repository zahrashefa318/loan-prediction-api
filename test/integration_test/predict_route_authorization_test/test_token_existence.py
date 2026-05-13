def test_token_existence(client):
    response=client.post(url="/predict",
                         headers={
                             "Idempotency-Key":"test_idem"
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
                         })
    assert response.status_code in [401,403]
    assert response.json()["detail"] == "Not authenticated"