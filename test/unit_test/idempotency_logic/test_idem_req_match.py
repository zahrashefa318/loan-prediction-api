from services.hash_request import hash_request
from services.idem_check import idem_check
from services.return_cached_data import return_hashed_req
from db.idempo_tbl import Idem_tbl
from datetime import datetime, timedelta
from routes.predict import payload_structure

def test_idem_req_match(mock_db):
    idem="test_idem"
    data={
        "income": 5000,
        "savings": 2000,
        "expenses": 1500,
        "family_size": 3,
        "years_employed": 5,
        "age": 30,
        "rent": 800,
        "debt": 1000
    }
    
    payload=payload_structure(**data)
    hashed_data=hash_request(payload)
    print (hashed_data)
    record=Idem_tbl(idem_key=idem,hashed_req=hashed_data,cached_res=999,expiry_date=datetime.utcnow()-timedelta(hours=3))
    mock_db.add(record)
    mock_db.commit()
    assert idem_check(idem,mock_db) == True
    assert return_hashed_req(idem,mock_db)== hashed_data