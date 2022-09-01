from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func
from datetime import datetime
from pytz import timezone

Base  = declarative_base()

class Message(Base):
    __tablename = "unac-sentiment"
    id  = Column(Integer, primary_key=True, index=True)
    group_name = Column(String)
    message = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=datetime.now(tz=timezone('America/Lima')))
