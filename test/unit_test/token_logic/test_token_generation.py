from services.token_generator import token_generator
def test_token_generation():
    token = token_generator()
    assert token is not None
    assert isinstance(token, str)