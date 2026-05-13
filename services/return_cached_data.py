from db.schema import SessionLocal
from db.idempo_tbl import Idem_tbl
from .idem_check import idem_check

def cached_response(idem,mocked_db):
    session= mocked_db or SessionLocal()
  
    try:
        record=session.query(Idem_tbl).filter(Idem_tbl.idem_key==idem).first()
        if record:
            return record.cached_res
        else:
            return None
    finally:
        if mocked_db is None:
            session.close()

def return_hashed_req(idem,mocked_db):
    session= mocked_db or SessionLocal()
    try:
        record=session.query(Idem_tbl).filter(Idem_tbl.idem_key==idem).first()
        if record:
            return record.hashed_req
        else:
            None
    finally:
        if mocked_db is None:
            session.close()

