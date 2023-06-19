"""The products routing logic"""
from fastapi import APIRouter


products_router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@products_router.get(
    "/",
    name='Get All Products',
    description="Returns all the products from the database"
)
async def get_all_products_endpoint():
    """An endpoint to retrieve all the products from the database

    Returns:
        _type_: _description_
    """
    return []
