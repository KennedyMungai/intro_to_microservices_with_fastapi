"""The inventory models"""
from database.db import redis
from redis_om import HashModel


class Product(HashModel):
    """The model for the Product.

    Args:
        HashModel (_type_): The HashModel class from redis_om
    """
    name: str
    price: float
    quantity: int

    class Meta:
        """The meta subclass for the redis inventory"""
        database = redis
