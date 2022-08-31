from tokenize import group
from typing import Optional
from pydantic import BaseModel, Field

class Whatsresq(BaseModel):
    app : Optional[str] 
    sender : str
    message : str
    group_name : Optional[str]
    phone: Optional[str]


