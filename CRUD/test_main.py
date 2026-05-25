import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import db_models
from db import engine
from main import app, get_db

TEST_DATABASE_URL = "sqlite:///./test_db.db"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
session = sessionmaker(autoflush=False, bind=engine)

@pytest.fixture(scope="function", autouse=True)
def setup_db():
    db_models.Base.metadata.create_all(bind=engine)
    yield
    db_models.Base.metadata.drop_all(bind=engine)

def override_get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

def test_start_endpoint():
    response = client.get("/")
    assert response.status_code==200
    assert response.json()=='Server started'

def test_add_prod_endpoint():
    payload = {
        "id": 1,
        "name": "Gaming Laptop",
        "desc": "High performance gaming laptop",
        "float": 1299.99
    }
    response = client.post("/add_prods", json=payload)
    assert response.status_code==200
    assert response.json() == 'Prod added'

def test_add_prod_fail():
    payload = {
        "id": 89,
        "name": "Gaming Laptop",
        "desc": "High performance gaming laptop",
        "float": '1299.99'
    }
    response = client.post('/add_prods', json=payload)
    assert response.status_code==422

        