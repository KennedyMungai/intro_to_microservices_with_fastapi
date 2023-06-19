"""The main script for the app"""
import os

from dotenv import find_dotenv, load_dotenv
from fastapi import FastAPI
from redis_om import get_redis_connection

load_dotenv(find_dotenv())

REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")

app = FastAPI(
    title="Inventory Microservice",
    description="The microservice that deals with the inventory system"
)

redis = get_redis_connection(
    host='redis-10746.c8.us-east-1-2.ec2.cloud.redislabs.com',
    port=10746,
    password = REDIS_PASSWORD,
    decode_responses=True
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
