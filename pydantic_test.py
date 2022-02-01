from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel

class Users(BaseModel):
    id : int
    username : str
    password : str
    confirm_password : str
    alias = 'anonymous'
    timestamp : Optional[datetime] = None
    friends : List[int] = []

data = {'id': '1234', 'username': 'wai foong', 'password': 'Password123', 'confirm_password': 'Password123', 'timestamp': '2020-08-03 10:30', 'friends': [1, '2', b'3']}

user = Users(**data)

print(user)