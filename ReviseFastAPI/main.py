from fastapi import FastAPI, Depends
from model import Pydantic_Model
from sqlalchemy.orm import Session
from db import session, engine
from db_model import Sql_Model, Base
app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def greeting(db:Session=Depends(get_db)):
    return db.query(Sql_Model).all()

@app.post('/add')
def add_product(product:Pydantic_Model, db:Session=Depends(get_db)):
    db.add(Sql_Model(**product.model_dump()))
    db.commit()
    return "added successfully"

@app.put('/edit')
def update_product(product:Pydantic_Model, db:Session=Depends(get_db)):
    prod = db.query(Sql_Model).first()
    prod.name = product.name
    db.commit()
    return "updated successfully"

@app.delete('/delete')
def del_product(product:Pydantic_Model, db:Session=Depends(get_db)):
    prod = db.query(Sql_Model).filter(Sql_Model.name==product.name).first()
    if prod:
        db.delete(prod)
        db.commit()
    return "deleted successfully"
    
    
