def test_same_idem(client,valid_token,override_env):
    idem="test_idem"
    res1=client.post(url="/predict",
                     headers={
                         "Idempotency-Key":idem,
                         "Authorization":f"Bearer {valid_token}"
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
    res2=client.post(url="/predict",
                     headers={
                         "Idempotency-Key":idem,
                         "Authorization":f"Bearer {valid_token}"
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
    assert res1.json()== res2.json()