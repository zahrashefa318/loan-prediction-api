from sqlalchemy import Integer, String,Float,Column,DateTime,Text
from .schema import Base
class Idem_tbl(Base):
    __tablename__="idem_tbl"
    id=Column(Integer, autoincrement=True, primary_key=True)
    idem_key=Column(String,nullable=False,unique=True)
    hashed_req=Column(String,nullable=False)
    cached_res=Column(Float,nullable=False)
    expiry_date=Column(DateTime, nullable=False)

