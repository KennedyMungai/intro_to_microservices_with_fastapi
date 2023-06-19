"""The products routing logic"""
from fastapi import APIRouter, status

from models.db_models import Product


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
    return Product.all_pks()


@products_router.post(
    "/",
    name='Create Product',
    description="Creates a new product",
    status_code=status.HTTP_201_CREATED
)
async def create_product_endpoint(product: Product):
    """The endpoint to create a product

    Args:
        product (Product): The data needed to create the product

    Returns:
        _type_: _description_
    """
    return product.save()
