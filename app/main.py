from fastapi import FastAPI
from pydantic import BaseModel

from app.calculator import add, subtract, multiply

app = FastAPI()


class Numbers(BaseModel):
    a: float
    b: float


@app.get("/")
def read_root():
    return {"message": "Calculator API is running"}


@app.post("/sum")
def sum_numbers(data: Numbers):
    return {"result": add(data.a, data.b)}


@app.post("/subtract")
def subtract_numbers(data: Numbers):
    return {"result": subtract(data.a, data.b)}


@app.post("/multiply")
def multiply_numbers(data: Numbers):
    return {"result": multiply(data.a, data.b)}