"""The consumers service file"""
from database.db import redis
from models.db_models import Product

key = 'order_completed'
group = 'inventory_group'


