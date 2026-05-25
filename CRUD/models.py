from pydantic import BaseModel
class Prod(BaseModel):
    id:int
    name:str
    desc:str
    float:float