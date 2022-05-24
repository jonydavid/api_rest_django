# API Pizzeria

Django API utilizando autenticacion JWT y Basic Auth.

### Installing

Clone

```
https://github.com/jonydavid/api_rest_django.git
```

crear entorno virtual e instalar requerimientos

```
py -m venv env
pip install -r requirements.txt
```

## Run

En orden de ejecución :

```
cd api_rest_django
```

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Despues de ejecutar puede visualizar los endpoint en http://127.0.0.1:8000/doc/ Swagger UI
Incluye Archivo de Colección de Postman
Para Realizar las consultas es necesario generar el token de acceso, o utilizar el Basic Auth:

## API Info

<details>
    <summary><ins>Generar Access Token</ins></summary>
        - POST `http://127.0.0.1:8000/token/`
        - Parametro username, password
</details>

<details>
    <summary><ins>Crear Ingredientes</ins></summary>
        - POST `http://127.0.0.1:8000/api/crear_ingrediente`
        ```json
        {
            "nombre":"Tomate",
            "categoria":"Premium"
        }
        ```
</details>

<details>
    <summary><ins>Ver Ingredientes</ins></summary>
        - GET `http://127.0.0.1:8000/api/get_ingredientes`
</details>

<details>
    <summary><ins>Modificar Ingredientes</ins></summary>
        - PUT `http://127.0.0.1:8000/api/put_ingrediente`
        ```json
        {
            "id":1,
            "nombre":"Locote",
            "categoria":"Premium"
        }
        ```
</details>

<details>
    <summary><ins>Eliminar Ingredientes</ins></summary>
        - DELETE `http://127.0.0.1:8000/api/delete_ingrediente`
        ```json
        {
            "id":1
        }
        ```
</details>

<details>
    <summary><ins>Crear Ingredientes</ins></summary>
        - POS `http://127.0.0.1:8000/api/crear_ingrediente`
        ```json
        {
            "nombre":"Tomate",
            "categoria":"Premium"
        }
        ```
</details>

<details>
    <summary><ins>Crear Pizza</ins></summary>
        - POST `http://127.0.0.1:8000/api/crear_pizza`
        - Parametro 
        ```json
        {
            "nombre":"Muzzarela Free",
            "precio":18000,
            "estado":"INACTIVO",
            "ingrediente":[1]
        }
        ```
</details>

<details>
    <summary><ins>Ver Pizzas</ins></summary>
        - GET `http://127.0.0.1:8000/api/get_pizzas`
</details>

<details>
    <summary><ins>Ver Detalle de Pizzas</ins></summary>
        - GET `http://127.0.0.1:8000/api/detalle_pizzas`
        ```json
        {
         "id":1
        }
        ```
</details>

<details>
    <summary><ins>Modificar las Pizzas</ins></summary>
        - PUT `http://127.0.0.1:8000/api/put_pizzas`
        ```json
        {
            "id":"1",
            "nombre":"Katupiri",
            "precio":25000,
            "estado":"ACTIVO"
        }
        ```
</details>

<details>
    <summary><ins>Agregar Ingrediente las Pizzas</ins></summary>
        - POST `http://127.0.0.1:8000/api/add_ingrediente`
        ```json
        {
            "id":1,
            "ingrediente":1
        }
        ```
</details>

<details>
    <summary><ins>Quitar Ingrediente las Pizzas</ins></summary>
        - POST `http://127.0.0.1:8000/api/remove_ingrediente`
        ```json
        {
            "id":1,
            "ingrediente":1
        }
        ```
</details>
