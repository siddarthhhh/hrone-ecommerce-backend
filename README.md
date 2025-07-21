#  HROne E-Commerce Backend

A FastAPI-based backend system built for the HROne Backend Intern Hiring Task.  
It includes complete product and order management APIs with strict adherence to request/response formats provided in the official task PDF.

---

##  Features Implemented

- **Products**
  - Create new products with name, price, and multiple sizes with quantities.
  - List products with optional filters: `name`, `size`.
  - Supports pagination using `limit` and `offset`.

- **Orders**
  - Create orders for a user by providing product IDs and quantities.
  - List orders by `userID` with pagination.
  - Orders include product details (ID and name) and compute total price.

---

##  Development Workflow

### 1. Planned the Core Features from the Task PDF
I began by analyzing the problem statement and broke it into two core parts:
- **Products API**
- **Orders API**

I ensured that every endpoint closely matches the structure expected by the automatic validation script (request and response schemas).

---

### 2.  Clean Project Structure

Modular layout using FastAPI best practices:
```
app/
├── main.py
├── database.py
├── models/
│   ├── product.py
│   └── order.py
└── routes/
    ├── product_routes.py
    └── order_routes.py
```

---

### 3. MongoDB Atlas Connection via Motor

- Used `motor` (async MongoDB driver) for async DB access.
- Created a reusable connection in `database.py`.
- Connected using a secure **MongoDB Atlas URI** (Free M0 tier).

---

### 4. Data Validation with Pydantic

Defined Pydantic models inside `app/models/`:
- `ProductSchema`, `SizeSchema`
- `OrderSchema`, `OrderItemSchema`

These help ensure strict type-checking, validation, and structured data across APIs.

---

### 5. Built Product APIs (`routes/product_routes.py`)

- **POST `/products`**  
  Accepts name, price, and sizes array. Stores in MongoDB.

- **GET `/products`**  
  Supports optional query filters: `name`, `size`.  
  Also includes pagination: `limit`, `offset`.

---

### 6. Built Order APIs (`routes/order_routes.py`)

- **POST `/orders`**  
  Accepts `userID` and a list of `items` (with `productId` and `qty`).  
  Stores the order in MongoDB.

- **GET `/orders/{user_id}`**  
  Returns all orders of the user.  
  - Includes pagination.
  - Performs a MongoDB `$lookup` to fetch product name for each `productId`.
  - Computes total price of each order.

---

### 7. Tested with Swagger UI (`/docs`)

- Verified every API using the built-in Swagger interface.
- Ensured all:
  - Request payloads match the specs.
  - Response formats match exactly (including nested product name in orders).
  - Filters and pagination work.
  - Proper handling of errors and edge cases.

---

### 8. Deployment

- Deployed the backend to **Railway** (Free Tier).
- Connected it to **MongoDB Atlas** using a secure connection string.
- Environment variable `MONGO_URI` is configured inside Railway for safe database access.

---

## Tech Stack

- **FastAPI** (async Python web framework)
- **MongoDB Atlas** (cloud database)
- **Motor** (async MongoDB driver)
- **Pydantic** (schema validation)
- **Uvicorn** (ASGI server)

---

## 🔗 API Base URL

> 📍 The deployed backend is accessible at:  
`https://hrone-ecommerce-backend-x7ri.onrender.com/`

All endpoints are relative to this root.


