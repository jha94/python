from pydantic import BaseModel

class user_type(BaseModel):
    email:str
    password:str