"""The orders route file"""
from math import ceil

import requests
from fastapi import APIRouter, Request, status
from fastapi.background import BackgroundTasks
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
async def create_order_endpoint(
    _request: Request,
    _background_tasks: BackgroundTasks
):
    """The endpoint to make an order

    Args:
        _request (Request): No idea

    Returns:
        _type_: Something
    """
    _body = await _request.json()
    _req = requests.get('http://localhost:8100/products/%s' %
                        _body['id'], timeout=10000)
    _product = _req.json()

    _order = Order(
        product_id=_body['id'],
        price=_product['price'],
        fee=ceil(_product['price'] * 0.2),
        total=ceil(_product['price'] * 1.2),
        quantity=_body['quantity'],
        status='pending'
    )

    _order.save()

    order_completed(_order)

    return _order


def order_completed(_order: Order):
    """A function called when the order is completed

    Args:
        _order (Order): The order
    """
    _order.status = 'completed'
    _order.save()
