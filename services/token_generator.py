import jwt
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
load_dotenv()

def token_generator():
    JWT_SECRET=os.getenv("JWT_SECRET").strip()
    JWT_ALGORITHM=os.getenv("JWT_ALGORITHM").strip()
    if not JWT_SECRET or not JWT_ALGORITHM:
        raise ValueError("JWT secret or algorithm is not available!")
    
    created_time=datetime.utcnow()
    expiration_time=created_time + timedelta(hours=12)
    payload={'sub':'anonymous',
             'exp':int(expiration_time.timestamp())}
    
    token=jwt.encode(payload,JWT_SECRET,algorithm=JWT_ALGORITHM) 
    return token      
             
