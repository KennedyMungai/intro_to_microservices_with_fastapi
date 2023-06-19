"""The orders route file"""
from fastapi import APIRouter, status


orders_router = APIRouter(
    prefix="/orders", 
    tags=["Orders"]
    )