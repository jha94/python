from fastapi import FastAPI
from models import Product
import db_models
from database import engine

app = FastAPI()

db_models.Base.metadata.create_all(bind=engine)

products = [
    Product(id=1, name='first', desc='first desc'),
    Product(id=2, name='second', desc='second desc')
    ]

@app.get('/')
def welcome():
    return 'Welcome'

@app.get('/list_products')
def get_all_products():
    return products

@app.get('/get_by_id')
def get_by_id(id:int):
    for product in products:
        if(product.id==id):
            return product