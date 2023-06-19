"""The database configuration for the inventory"""
import os

from dotenv import find_dotenv, load_dotenv
from redis_om import get_redis_connection

load_dotenv(find_dotenv())


REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")


redis = get_redis_connection(
    host='redis-10746.c8.us-east-1-2.ec2.cloud.redislabs.com',
    port=10746,
    password=REDIS_PASSWORD,
    decode_responses=True
)
