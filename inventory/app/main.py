"""The main script for the app"""
from fastapi import FastAPI
from routes.products_route import products_router

app = FastAPI(
    title="Inventory Microservice",
    description="The microservice that deals with the inventory system"
)


@app.get(
    "/",
    name="Root",
    description="The root endpoint of the inventory microservice",
    tags=['Inventory Root'],
    response_model=dict[str, str]
)
async def root() -> dict[str, str]:
    """The root endpoint of the inventory microservice

    Returns:
        dict[str, str]: A simple message
    """
    return {"Message": "The inventory microservice is running"}


app.include_router(products_router)
