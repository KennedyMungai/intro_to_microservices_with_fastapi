"""The consumers route file"""
from fastapi import APIRouter, Depends


consumers_route = APIRouter(
    prefix="/consumers", 
    tags=["Consumers"]
    )