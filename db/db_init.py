from .schema import Base,engine
from .idempo_tbl import Idem_tbl
Base.metadata.create_all(bind=engine)