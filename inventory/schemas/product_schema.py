"""The schemas for the Products"""
from pydantic import BaseModel


class ProductDisplay(BaseModel):
    """The product Display Schema

    Args:
        BaseModel (Pydantic Model): The base model for all models
    """
    pk: str
    name: str
    price: float
    quantity: int

    class Config:
        """The config subclass for the ProductDisplay Schema"""
        orm_mode = True


class ProductCreate(BaseModel):
    """The schema used to create a product

    Args:
        BaseModel (Pydantic Model): The base model
    """
    name: str
    price: float
    quantity: int
