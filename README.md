
# 🛒 FastAPI eCommerce Backend

A scalable backend API for an eCommerce application (Flipkart/Amazon-style) built using **FastAPI** and **MongoDB** (with **Motor** for async operations).

---

## 🚀 Features

- ✅ Create Product with sizes & quantity
- ✅ List Products with filters (name, size) and pagination
- ✅ Create Orders with product references and quantity
- ✅ Get Orders with product lookup, quantity, total, and pagination

---

## 🧱 Tech Stack

- **FastAPI** (Python 3.10+)
- **MongoDB Atlas**
- **Motor** (Async MongoDB driver)
- **Pydantic** for validation
- **Uvicorn** for running the server

---

## 📁 Project Structure

```
ecommerce-backend/
├── main.py
├── database.py
├── .env
├── routes/
│   ├── products.py
│   └── orders.py
├── models/
│   ├── product_model.py
│   └── order_model.py
├── schemas/
│   ├── product.py
│   └── order.py
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/ecommerce-backend.git
cd ecommerce-backend
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, install manually:
```bash
pip install fastapi uvicorn motor python-dotenv
```

### 4. Create `.env` file

```env
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/ecommerce?retryWrites=true&w=majority
```

Replace `<username>` and `<password>` with your **MongoDB Atlas** credentials.

---

## ▶️ Running the Server

```bash
uvicorn main:app --reload
```

Visit API docs:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

---

## 📦 API Endpoints

### 🧾 Create Product

**POST** `/products`

```json
{
  "name": "iPhone 15",
  "price": 99999,
  "sizes": [
    { "size": "128GB", "quantity": 10 },
    { "size": "256GB", "quantity": 5 }
  ]
}
```

### 📄 List Products

**GET** `/products?name=iphone&size=128GB&limit=5&offset=0`

Response:
```json
{
  "data": [
    { "id": "abc123", "name": "iPhone 15", "price": 99999 }
  ],
  "page": { "next": 5, "limit": 5, "previous": 0 }
}
```

---

### 🛒 Create Order

**POST** `/orders`

```json
{
  "userId": "user123",
  "items": [
    { "productId": "abc123", "quantity": 2 },
    { "productId": "xyz456", "quantity": 1 }
  ]
}
```

---

### 📦 Get Orders

**GET** `/orders/user123`

Response:
```json
{
  "data": [
    {
      "id": "order123",
      "items": [
        {
          "productDetails": {
            "name": "iPhone 15",
            "id": "abc123"
          },
          "qty": 2
        }
      ],
      "total": 199998.0
    }
  ],
  "page": { "next": 10, "limit": 10, "previous": 0 }
}
```

---

## 🧪 Testing Tools

- [Thunder Client (VSCode)](https://www.thunderclient.com/)
- [Postman](https://www.postman.com/)
- Swagger UI at `http://localhost:8000/docs`