from pydantic import BaseModel
class Prod(BaseModel):
    id:int
    name:str
    desc:str
    price:float