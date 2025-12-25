from fastapi import FastAPI, Depends
from models import Product
from database import session
import database_model
from sqlalchemy.orm import Session

app = FastAPI()

@app.get('/')
def greeting():
    return "Good morning"

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

@app.get('/list')
def list_products(db:Session=Depends(get_db)):
    products = db.query(database_model.product).all()
    return products

@app.get('/get_by_id/{id}')
def get_by_id(id:int):
    for prod in products:
        if prod.id==id:
            return prod
    return "Product not found"


@app.put("/update")
def updated(product:Product):
    for i, prod in enumerate(products):
        if prod.id==product.id:
            products[i] = product
            return "updated successfully"

@app.delete('/delete/{id}')
def delete(id:int):
    for i, prod in enumerate(products):
        if prod.id==id:
            products.pop(i)
            return "deleted successfully"
    return "Please enter valid ID"

@app.post('/add')
def add(product:Product, db:Session=Depends(get_db)):
    db.add(database_model.Product(**product.model_dump()))
    db.commit()
    return "Product added successfully"