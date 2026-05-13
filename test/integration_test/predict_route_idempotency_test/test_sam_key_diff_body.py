def test_same_key_diff_body(client, valid_token, override_env):
    res1=client.post(url="/predict",
                     headers={
                         "Idempotency-Key":"test_idem",
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
                         "Idempotency-Key":"test_idem",
                         "Authorization":f"Bearer {valid_token}"
                     },
                     json={
                            "income": 4000,
                            "savings": 1000,
                            "expenses": 900,
                            "family_size": 8,
                            "years_employed": 5,
                            "age": 40,
                            "rent": 1000,
                            "debt": 11000
                     })
    print(res2.json())
    assert res2.status_code == 409
    assert res2.json()["detail"] == "Idempotency key and request payload mismatch!"
  