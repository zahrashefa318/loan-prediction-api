from db.idempo_tbl import Idem_tbl
from datetime import datetime, timedelta
from services.expired_keys_deletion import delete_expired_key
def test_expired_idem_deletion(mock_db):
    idem="tes_idem"
    record=Idem_tbl(idem_key=idem,hashed_req="kajsfdhkj",cached_res=87687,expiry_date=datetime.utcnow() - timedelta(days=5))
    mock_db.add(record)
    mock_db.commit()
    assert mock_db.query(Idem_tbl).filter_by(idem_key = idem).first() is not None
    delete_expired_key(mock_db)
    assert mock_db.query(Idem_tbl).filter_by(idem_key = idem).first() is  None
    