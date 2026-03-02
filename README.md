# Tutorial Django 

## Cómo correr el proyecto 

### 1) Crear entorno virtual
```bash
py -m venv .venv
```
### 2) Activar entorno virtual
 ```bash
.venv\Scripts\activate
```
### 3) Instalar dependencias
```bash
pip install django factory_boy
```
### 4) Aplicar migraciones
```bash
py manage.py makemigrations
py manage.py migrate
```
### 5) Cargar productos de prueba
```bash
py manage.py seed_products
```
### 6) Ejecutar servidor
```bash
py manage.py runserver
```
preguntas tutorial

Con DI / DIP

La vista depende de una abstracción (ImageStorage)

Sin DI

La vista depende directamente de ImageLocalStorage
