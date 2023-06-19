"""The models for the Order data"""
from database.db import redis
from redis_om import HashModel


class Order(HashModel):
    """The model for the orders

    Args:
        HashModel (Redis_om): The base class for the Order class
    """
    product_id: str
    price: float
    fee: float
    total: float
    quantity: int
    status: str     # pending, completed, refunded

    class Meta:
        """The metadata for the order class"""
        database = redis
