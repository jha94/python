from fastapi import FastAPI
from models import Product
app = FastAPI()

@app.get('/')
def greeting():
    return "Good morning"

products = [
    Product(id=1, name="Laptop", desc="Best Machine", price=350000, quantity=1),
    Product(id=2, name="Book", desc="Best non machine", price=700, quantity=1)
]

@app.get('/list')
def list_products():
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