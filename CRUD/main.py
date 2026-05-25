from fastapi import FastAPI, Depends
import db_models
from db import engine, session
from models import Prod
from sqlalchemy.orm import Session

app = FastAPI()
db_models.Base.metadata.create_all(bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def start():
    return 'Server started'

@app.post('/add_prods')
def add_prods(prod:Prod, db:Session=Depends(get_db)):
    db.add(db_models.Prod(**prod.model_dump()))
    db.commit()
    return 'Prod added'
