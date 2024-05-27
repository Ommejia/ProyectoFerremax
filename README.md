
# Documentación de la API

## Introducción
Este documento describe las APIs disponibles en el proyecto Ferramax, un sistema para gestionar el proceso de ventas de una ferretería. La API permite obtener productos activos, agregar productos a un carrito de compras y realizar el pago del carrito.

## Estructura del Proyecto

El proyecto sigue una estructura Django y está organizado de la siguiente manera:
- `asgi.py`: Configuración de ASGI para el proyecto.
- `settings.py`: Configuración global del proyecto Django.
- `urls.py`: Enrutamiento principal del proyecto.
- `wsgi.py`: Configuración de WSGI para el proyecto.
- `admin.py`: Registro de modelos en el administrador de Django.
- `api.py`: Definición de las vistas de la API.
- `apps.py`: Configuración de la aplicación.
- `models.py`: Definición de los modelos de la base de datos.
- `serializers.py`: Serialización de datos para la API.
- `tests.py`: Pruebas unitarias.
- `views.py`: Definición de las vistas.
- `load_products.py`: Script para cargar productos en la base de datos.
- `manage.py`: Utilidad de línea de comandos de Django.

## Endpoints Disponibles

### 1. Obtener Todos los Productos Activos

- **URL**: `[/api/products/](http://localhost:8000/api/v1/products/)`
- **Método HTTP**: `GET`
- **Descripción**: Retorna una lista de todos los productos activos.
- **Parámetros**:
  - `skip` (opcional): Número de productos a saltar (por defecto es 0).
  - `limit` (opcional): Número máximo de productos a retornar (por defecto es 10).
- **Respuesta**:
  ```json
  [
    {
      "id": 1,
      "name": "Producto 1",
      "description": "Descripción del producto 1",
      "price": 100.0,
      "is_active": true
    },
    ...
  ]
  ```

### 2. Ingresar Productos al Carro de Compras

- **URL**: `/api/cart/`
- **Método HTTP**: `POST`
- **Descripción**: Agrega uno o más productos al carrito de compras.
- **Cuerpo de la Solicitud**:
  ```json
  {
    "product_id": 1,
    "quantity": 2
  }
  ```
- **Respuesta**:
  ```json
  {
    "id": 1,
    "product_id": 1,
    "quantity": 2
  }
  ```

### 3. Pagar el Carro de Compras y Finalizar el Pedido

- **URL**: `/api/checkout/`
- **Método HTTP**: `POST`
- **Descripción**: Finaliza el pedido y limpia el carrito de compras.
- **Respuesta**:
  ```json
  {
    "message": "Checkout completed"
  }
  ```

## Guía de Ejecución

Para ejecutar el proyecto localmente, sigue estos pasos:

1. **Crear y activar un entorno virtual**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows: .\venv\Scripts\activate
    ```

2. **Instalar las dependencias**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Inicializar la base de datos**:
    ```sh
    python manage.py migrate
    ```

4. **Cargar datos de productos**:
    ```sh
    python manage.py load_products
    ```

5. **Ejecutar el servidor**:
    ```sh
    python manage.py runserver
    ```


## Modelo de Datos

### Producto

- **Atributos**:
  - `id` (int): Identificador único del producto.
  - `name` (str): Nombre del producto.
  - `description` (str): Descripción del producto.
  - `price` (float): Precio del producto.
  - `is_active` (bool): Indicador de si el producto está activo.

### Carro de Compras

- **Atributos**:
  - `id` (int): Identificador único del ítem en el carrito.
  - `product_id` (int): Identificador del producto.
  - `quantity` (int): Cantidad de productos.

## Consideraciones

- **Seguridad**: Asegúrate de manejar correctamente la autenticación y autorización en el futuro.
- **Escalabilidad**: Para entornos de producción, considera el uso de una base de datos más robusta y servicios de pago reales.
- **Mantenimiento**: Documenta cualquier cambio significativo en las APIs para facilitar el mantenimiento futuro.

---

Este documento proporciona toda la información necesaria para entender y utilizar las APIs disponibles en el proyecto Ferramax. Si tienes alguna pregunta o necesitas más detalles, no dudes en contactar al equipo de desarrollo.
