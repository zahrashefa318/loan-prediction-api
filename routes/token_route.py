from fastapi import APIRouter
from services.token_generator import token_generator
route=APIRouter()
@route.get('/token')
def token():
    token=token_generator()
    return {'token':token}
