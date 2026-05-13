from fastapi import APIRouter, Depends, Header , HTTPException,BackgroundTasks
from pydantic import BaseModel
from model.model_loader import load_model
import numpy as np
from sqlalchemy.orm import Session
from services.idem_check import idem_check
from services.return_cached_data import cached_response,return_hashed_req
from db.schema import SessionLocal
from db.idempo_tbl import Idem_tbl
from services.hash_request import hash_request
from services.expired_keys_deletion import delete_expired_key
from services .authorization_check import is_authorized
from db.schema import get_db
from datetime import datetime, timedelta
router=APIRouter()

class payload_structure(BaseModel):
    income:float
    savings:float
    expenses:float
    family_size:int
    years_employed:int
    age:int
    rent:float
    debt:float

model=load_model()
    

@router.post('/predict')
def predict(data:payload_structure,bg:BackgroundTasks,idem:str=Header(...,alias="Idempotency-Key"),user:dict=Depends(is_authorized),db:Session=Depends(get_db)):
    
    try:
        hashed_request=hash_request(data)
        if idem_check(idem,db):
            cached_hashed_req=return_hashed_req(idem,db)
            if hashed_request == cached_hashed_req:
                response=cached_response(idem,db)
                return {'predicted loan':response}
            else :
                raise HTTPException (status_code=409, detail="Idempotency key and request payload mismatch!")
        #extract the features as the same order in the training
        features=np.array([
            data.income,
            data.savings,
            data.expenses,
            data.family_size,
            data.years_employed,
            data.age,
            data.rent,
            data.debt
        ])

        w=model["w"]
        b=model["b"]
        X_mean=model["X_mean"]
        X_std=model["X_std"]
        y_mean=model["Y_mean"]
        y_std=model["Y_std"]

        #normalize the features :
        features=(features - X_mean)/ (X_std +1e-8)
        y_pred=np.dot(features,w)+b #normalized prediction
        y_pred=y_pred * y_std + y_mean #convert back to real value from normalized ones.
        y_pred=np.maximum(0,y_pred) # to avoid negative predictions.

        #save the predicted value in the db for later same requests from same user.
        
        
        expiration_date=datetime.utcnow()+ timedelta(seconds=120)
        record=Idem_tbl(idem_key=idem,hashed_req=hashed_request,cached_res=float(y_pred),expiry_date=expiration_date)
        db.add(record)
        db.commit()
        
            
        bg.add_task(delete_expired_key,db)
        return {'predicted loan':round(float(y_pred),2)}
    except HTTPException:
        raise
    except Exception as e:
        print(e)
        raise
