from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URI = os.getenv("MONGO_URI")

def connect_to_mongo():
    client = AsyncIOMotorClient(MONGO_URI)
    return client["hrone"]
