"""The consumers service file"""
import time

from database.db import redis
from models.db_models import Product

key = 'order_completed'
group = 'inventory_group'


try:
    redis.xgroup_create(key, group)
except:
    print('Group already exists!')


while True:
    try:
        results = redis.xreadgroup(group, key, {key: '>'}, None)
        print(results)
    except Exception as e:
        print(str(e))

    time.sleep(1)
