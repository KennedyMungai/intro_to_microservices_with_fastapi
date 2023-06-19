"""The orders route file"""
import requests
from fastapi import APIRouter, Request, status


orders_router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@orders_router.post(
    "/",
    name="Make an Order",
    description="The endpoint to make an order",
    status_code=status.HTTP_201_CREATED
)
async def create_order_endpoint(_request: Request):
    """The endpoint to make an order

    Args:
        _request (Request): No idea

    Returns:
        _type_: Something
    """
    _body = await _request.json()
    _req = requests.get(f'http://localhost:8000/products/%s' % _body['id'], timeout=10000)

    return _req.json()
