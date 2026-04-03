from fastapi import FastAPI
from pydantic import BaseModel

from app.calculator import multiply, resta, sum

app = FastAPI()


class OperationInput(BaseModel):
    a: int
    b: int


@app.post("/suma")
def suma_endpoint(data: OperationInput) -> dict[str, int]:
    return {"resultado": sum(data.a, data.b)}


@app.post("/resta")
def resta_endpoint(data: OperationInput) -> dict[str, int]:
    return {"resultado": resta(data.a, data.b)}


@app.post("/multiplicacion")
def multiplicacion_endpoint(data: OperationInput) -> dict[str, int]:
    return {"resultado": multiply(data.a, data.b)}