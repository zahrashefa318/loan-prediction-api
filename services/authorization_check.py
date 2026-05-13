import jwt
import os
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends,HTTPException,status
from dotenv import load_dotenv
load_dotenv()
security=HTTPBearer()

def is_authorized(credentials:HTTPAuthorizationCredentials=Depends(security)):
    try:
        JWT_SECRET=os.getenv("JWT_SECRET").strip()
        JWT_ALGORITHM=os.getenv("JWT_ALGORITHM").strip()
        if not JWT_SECRET or not JWT_ALGORITHM:
            raise ValueError("Missing JWT_SECRET and/or JWT_ALGORITHM")
        token=credentials.credentials
        decoded_token=jwt.decode(token,JWT_SECRET, algorithms=[JWT_ALGORITHM])
        print("SECRET:", JWT_SECRET)
        print("ALGO:", JWT_ALGORITHM)
        print("TOKEN:", token)
        print(decoded_token)
        return decoded_token
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Token expired",headers={"WWW-Authenticate": "Bearer"})
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token",headers={"WWW-Authenticate": "Bearer"})


