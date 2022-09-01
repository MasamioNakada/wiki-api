from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func
from session import Base
from datetime import datetime
from pytz import timezone

class Message(Base):
    __tablename = "unac-sentiment"
    id  = Column(Integer, primary_key=True, index=True)
    group_name = Column(String)
    message = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=datetime.now(tz=timezone('America/Lima')))
