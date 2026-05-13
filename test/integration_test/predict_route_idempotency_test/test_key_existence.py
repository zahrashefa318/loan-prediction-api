def test_key_existence(client, valid_token,override_env):
    token=valid_token
    response=client.post(url="/predict",
                         headers={
                             "Authorization":f"Bearer {token}"
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
    assert response.status_code == 422