from fastapi import FastAPI
from fastapi import Body
from pydantic import BaseModel

app = FastAPI()
orders = []


class Order(BaseModel):
    kind: str
    size: str
    extra_cheese: bool



@app.get("/aaa")
def root() :
    return {"message": "Hello, World!"}


@app.get("/orderlist")
def root() :
    return orders


@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}



#http://127.0.0.1:8000/order_pizza?kind=불고기&size=라지&extra_cheese=false
@app.get("/order_pizza")
def order_pizza(kind : str, size:str , extra_cheese: bool):
    return {
        "kind": kind,
        "size": size,
        "extra_cheese": extra_cheese
        }
    

@app.post("/order_pizza2")
def creat_pizza(kind :str = Body(), 
                size :str = Body() , 
                extra_cheese : bool = Body()):
    return {
        "kind": kind,
        "size": size,
        "extra_cheese": extra_cheese
        }


@app.post("/orders")
def create_order(order : Order):
    orders.append(order)
    return order