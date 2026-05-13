from db.schema import SessionLocal
from datetime import datetime
from db.idempo_tbl import Idem_tbl

def delete_expired_key(db):
    
        current_time=datetime.utcnow()
        record=db.query(Idem_tbl).all()
        for r in record:
            if r.expiry_date <= current_time:
                db.delete(r)
        db.commit()       
   


    
