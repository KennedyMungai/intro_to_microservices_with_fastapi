"""The main app for the microservice"""
from fastapi import FastAPI


app = FastAPI(
    title="Payment",
    description="The payment microservice"
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
