"""The main app for the microservice"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.orders_route import orders_router

app = FastAPI(
    title="Payment",
    description="The payment microservice"
)


origins = [
    'https://localhost:5173',
    'http://localhost:5173'
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
    description="The root endpoint for the payment microservice",
    tags=["Root"]
)
async def root():
    """The root endpoint for the payment microservice

    Returns:
        _type_: _description_
    """
    return {"message": "Payment Microservice"}

app.include_router(orders_router)
