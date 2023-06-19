"""The orders route file"""
import requests
from fastapi import APIRouter, Request, status
from models.db_models import Order

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
    _req = requests.get('http://localhost:8100/products/%s' % _body['id'], timeout=10000)
    _product = _req.json()
    
    _order = Order(
        product_id = _body['id'],
        price = _product['price'],
        fee = _product['price'] * 0.2,
        total = _product['price'] * 1.2,
        quantity = _body['quantity'],
        status='pending'
    )
    
    _order.save()

    return _order
