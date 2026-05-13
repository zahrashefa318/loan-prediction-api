def test_data_validation(client,valid_token,override_env):
    payload={
        "income":"not_a_number",
        "savings":5000,
        "expenses":2000,
        "family_size":4,
        "years_employed":5,
        "age":30,
        "rent":1000,
        "debt":2000
    }
    headers={"Authorization":f"Bearer {valid_token}","Idempotency-Key":"test_idem_key"}
    res=client.post(url="/predict",json=payload,headers=headers)
    assert res.status_code == 422