# NovaCart

NovaCart is a demo commerce platform with a layered FastAPI backend, PostgreSQL persistence, token auth, and a React frontend served by the same app.

## Architecture

- `app/domain`: entities, exceptions, repository contracts, pricing and recommendation rules
- `app/application`: DTOs and business services
- `app/infrastructure`: SQLAlchemy models, session setup, and repository implementations
- `app/presentation/api`: routers, request schemas, dependency container
- `app/presentation/web`: frontend route delivery
- `frontend`: React UI shell plus styling
- `alembic`: database migrations and seed data

## Business Logic

- Product catalog with filtering, sorting, featured items, and related recommendations
- User registration, login, and token-based authenticated sessions
- Per-user cart with inventory checks, shipping methods, coupon support, and price breakdowns
- Checkout with tax and shipping calculations persisted to PostgreSQL
- Product reviews that recalculate average ratings
- Admin dashboard with inventory metrics and order status updates

## Run

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
docker compose up -d postgres
alembic upgrade head
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000`.

The frontend uses React from CDN scripts in `frontend/index.html`, so browser internet access is needed for the UI runtime.

Seeded credentials after `alembic upgrade head`:

- Admin: `admin@novacart.local` / `Admin123!`
- Demo user: `demo@novacart.local` / `Demo123!`

## API Endpoints

- `GET /api/health`
- `GET /api/metrics`
- `POST /api/auth/register`
- `POST /api/auth/login`
- `GET /api/auth/me`
- `GET /api/products`
- `GET /api/products/featured`
- `GET /api/products/categories`
- `GET /api/products/{product_id}`
- `GET /api/products/{product_id}/reviews`
- `POST /api/products/{product_id}/reviews`
- `GET /api/cart`
- `POST /api/cart/items`
- `PUT /api/cart/items/{product_id}`
- `DELETE /api/cart/items/{product_id}`
- `POST /api/cart/clear`
- `POST /api/cart/coupon`
- `DELETE /api/cart/coupon`
- `POST /api/cart/shipping`
- `GET /api/orders`
- `POST /api/orders`
- `GET /api/orders/{order_id}`
- `PUT /api/orders/{order_id}/status`
- `GET /api/admin/dashboard`
- `POST /api/admin/products`
- `PUT /api/admin/products/{product_id}`
- `DELETE /api/admin/products/{product_id}`
