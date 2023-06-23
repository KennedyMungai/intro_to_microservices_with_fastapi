"""The main script for the app"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.consumers_route import consumers_route
from routes.products_route import products_router

app = FastAPI(
    title="Inventory Microservice",
    description="The microservice that deals with the inventory system"
)

origins=[
    'http://localhost:5173',
    'https://localhost:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
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
app.include_router(consumers_route)
