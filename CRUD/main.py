from fastapi import FastAPI, Depends
import db_model
from db import engine, session
from models import Prod
from sqlalchemy.orm import Session

app = FastAPI()
db_model.Base.metadata.create_all(bind=engine)
def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def start():
    return 'Server started'

@app.post('/add_prod')
def add_prod(prod:Prod, db:Session=Depends(get_db)):
    db.add(db_model.Prod(**prod.model_dump()))
    db.commit()
    return 'Prod added'
