from fastapi import FastAPI
from app.database import connect_to_mongo
from app.routes import product_routes, order_routes

app = FastAPI()
app.database = connect_to_mongo()

app.include_router(product_routes.router)
app.include_router(order_routes.router)
