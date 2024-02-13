# Instructions

**1. Create a Virtual Environment(optional)**

```
python -m venv venv
# Activate it
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

**2. Install Dependencies:**

```
pip install -r requirements.txt
```

**3. Apply migrations:**

```
python manage.py makemigrations
python manage.py migrate
```

**4. Run the Development Server:**

```
python manage.py runserver
```

# API Documentation

### User authentication

**1. Register Endpoint:**

```
POST /register/
```

Body:

```
{
    "username": "user",
    "password1": "password"
    "password2": "password"
    "email": "damon.liren@gmail.com"
}
```

HTML Response: `Registration success!!!`

Authentication Required: No

**2. Log in Endpoint:**

```
POST /login/
```

Body:

```
{
    "username": "user",
    "pass": "password"
}
```

HTML Response:
`Login success! Please see CSRF token in your cookies.`

If you are using Postman to test this project, you have to copy the csrf token from cookies you received after logging in

**3. log out Endpoint:**

```
GET /logout/
```

### RESTful APIs

**1. Items(with query filters)**

List/Create Items

```
GET /api/items/
```

Query Parameters:

stock_status: Filters items by stock status (e.g., In Stock, Out of Stock).

category: Filters items by category ID.

Example: `/api/items/?stock_status=In+Stock&category=1`

Description: Retrieves a list of items, optionally filtered by stock status and category.

Authentication Required: Yes

```
POST /api/items/
```

Body Example:

```
{
  "sku": "ETSY-FOREST",
  "name": "Etsy Bundle Pack",
  "category": 1,
  "tags": [1, 2, 4, 5],
  "stock_status": "In Stock",
  "available_stock": 0,
}
```

Description: Creates a new item.

Authentication Required: Yes

```
GET /api/items/:id
PUT /api/items/:id
DELETE /api/items/:id
```

Description: Get, Update or delete an exist item.

Authentication Required: Yes

**2. Category**

List/Create categories

```
GET /api/categories/
POST /api/categories/
```

Description: Similar to Item

Authentication Required: Yes

```
GET /api/categories/:id
PUT /api/categories/:id
DELETE /api/categories/:id
```

Description: Similar to Item

Authentication Required: Yes

**3. Tag**

List/Create tags

```
GET /api/tags/
POST /api/tags/
```

Description: Similar to Item

Authentication Required: Yes

```
GET /api/tags/:id
PUT /api/tags/:id
DELETE /api/tags/:id
```

Description: Similar to Item

Authentication Required: Yes
