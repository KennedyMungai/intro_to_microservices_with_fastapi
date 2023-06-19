"""The products routing logic"""
from fastapi import APIRouter, status
from models.db_models import Product
from schemas.product_schema import ProductCreate, ProductDisplay

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
    return [format_service(pk) for pk in Product.all_pks()]


def format_service(_pk: str) -> ProductDisplay:
    """A function to format the return of an item

    Args:
        pk (str): The Primary Key

    Returns:
        ProductDisplay: The schema
    """
    product = Product.get(_pk)
    return product


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


@products_router.get(
    "/{_pk}",
    name='Get Product',
    description="Returns a product",
    response_model=ProductDisplay
)
async def get_single_product_endpoint(_pk: str):
    """The endpoint to get a single product

    Args:
        pk (str): The Primary Key

    Returns:
        _type_: _description_
    """
    return Product.get(_pk)


@products_router.delete(
    "/{_pk}",
    name='Delete Product',
    description="An endpoint to delete a product",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None
)
async def delete_product_endpoint(_pk: str) -> None:
    """An endpoint to delete a product

    Args:
        pk (str): The Primary Key

    Returns:
        _type_: _description_
    """
    return Product.delete(_pk)
