def test_predict_route_model(client,valid_token,override_env):
    res=client.post(url="/predict",
                    headers={
                        "Idempotency-Key":"test_idem",
                        "Authorization":f"Bearer {valid_token}"
                            },
                        json={
                            "income":50000,
                            "savings":20000,
                            "expenses":15000,
                            "family_size":4,
                            "years_employed":5,
                            "age":30,
                            "rent":1000,
                            "debt":2000
                        })
    assert res.status_code==200
    assert "predicted loan" in res.json()
    assert isinstance(res.json()["predicted loan"],float)
    