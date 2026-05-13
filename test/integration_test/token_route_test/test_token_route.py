def test_token_route(client):
    res=client.get("/token")
    assert res.status_code == 200
    assert res.json()["token"] is not None
    assert  isinstance(res.json()["token"] ,str)
    