from pydantic import BaseModel

class Local_User(BaseModel):
    email:str
    password:str