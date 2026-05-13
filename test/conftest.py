import pytest
from fastapi.testclient import TestClient
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from db.idempo_tbl import Idem_tbl
from db.schema import Base,get_db
import jwt
from datetime import datetime, timedelta

@pytest.fixture   # Fixtures provide setup + cleanup automatically. Those things that are going to be used frequently by any test.
def client(mock_db):
    def override_db():
        return mock_db
    app.dependency_overrides[get_db]=override_db
    client=TestClient(app)
    yield client
    app.dependency_overrides.clear()

@pytest.fixture
def mock_db():
    # SETUP
    mocked_db=create_engine("sqlite://",connect_args={"check_same_thread":False},poolclass=StaticPool) # check_same_thread : false means: Hey SQLite! Allow other threads to use this connection too.
    mocked_sessionLocal=sessionmaker(bind=mocked_db)
    Base.metadata.create_all(bind=mocked_db)
    session=mocked_sessionLocal()
    # TEST RUNS HERE
    yield session    # yeild pauses the execution and saves the state then resume it later.
    # CLEANUP
    session.close()

@pytest.fixture
def valid_token():
    iat=datetime.utcnow()
    exp=datetime.utcnow() + timedelta(minutes=30)
    payload={
        
        "sub":"test_user",
        "iat":iat,
        "exp":exp
    }
    token=jwt.encode(payload,"test_secret",algorithm="HS256")
    return token

@pytest.fixture
def override_env(monkeypatch):
    monkeypatch.setenv("JWT_SECRET","test_secret")
    monkeypatch.setenv("JWT_ALGORITHM","HS256")
    
    