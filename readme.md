## GraphQL using Graphene in Django, FastAPI, and Flask

### Description  
This project demonstrates the integration of **GraphQL** using the **Graphene** library in three Python web frameworks:
- **Django**
- **FastAPI**
- **Flask**

For each, it covers:
- Dependencies
- Configuration/Project Setup
- Route Setup

---

## 1. Django + Graphene

### Dependencies `requirements.txt`:

```txt
Django
graphene-django
```

### Project Configuration  

Add `graphene_django` to `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # GraphQL
    'graphene_django',
]
```

### Route Setup  
Add a route in `urls.py`:

```python
from django.urls import path
from graphene_django.views import GraphQLView
from qrfql.schemas import schema

urlpatterns = [
    path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema)),  # GraphiQL UI
]
```

---

## 2. FastAPI + Graphene

### Dependencies `requirements.txt`:

```txt
sqlalchemy
fastapi
uvicorn[standard]
graphene
starlette-graphene3
```

### Project Setup  

Create `main.py`:

```python
from fastapi import FastAPI
from qrfql.schemas import schema
from starlette_graphene3 import GraphQLApp, make_graphiql_handler

app = FastAPI(description="GraphQL API")
app.mount("/graphql", GraphQLApp(schema=schema, on_get=make_graphiql_handler()))

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
```

---

## 3. Flask + Graphene

### Dependencies `requirements.txt`:

```txt
flask
sqlalchemy
graphql-core==2.3.2
flask_graphql
graphene
```

### Project Setup  

Create `app.py`:

```python
from flask import Flask
from flask_graphql import GraphQLView
from qrfql.schemas import schema

app = Flask(__name__)
app.add_url_rule("/graphql", view_func=GraphQLView.as_view("graphql", graphql_schema=schema, graphiql=True))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
```

---