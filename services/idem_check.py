from db.schema import SessionLocal
from db.idempo_tbl import Idem_tbl



def idem_check(idem,mocked_db):
    session=mocked_db or SessionLocal()
    record=session.query(Idem_tbl).filter(Idem_tbl.idem_key==idem).first()
    return record is not None