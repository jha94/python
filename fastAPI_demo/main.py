from fastapi import FastAPI, Depends
from models import Product
from database import session, engine
import db_models
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
def main():
    return 'Say Hello to FastAPI demo'

@app.get('/products')
def get_all_products(db:Session = Depends(get_db)):
    db_products = db.query(db_models.Product).all()
    return db_products

@app.get('/product/{id}')
def get_products_by_id(id:int, db:Session = Depends(get_db)):
    db_prod = db.query(db_models.Product).filter(db_models.Product.id==id).first()
    if db_prod:
        return db_prod
    return 'Product not found'

@app.post('/product')
def add_product(prod:Product, db:Session = Depends(get_db)):
    db.add(db_models.Product(**prod.model_dump()))
    db.commit()
    return 'Product added successfully'

@app.delete('/delete')
def delete_product(id:int, db:Session = Depends(get_db)):
    db.query(db_models.Product).filter(db_models.Product.id==id).delete()
    db.commit()
    return 'Product deleted successfully'