"""The main app for the microservice"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Payment",
    description="The payment microservice"
)


origins = []

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
