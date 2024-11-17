# Proyecto Educativo Django - Aplicación de Tienda Online

Este proyecto educativo tiene como objetivo enseñar los conceptos fundamentales de Django mediante la creación de una aplicación web simple que simula una tienda online. A lo largo del proyecto, aprenderás a trabajar con entornos virtuales, modelos, vistas, templates y el principio DRY.

---

## Índice

1. [Introducción](#1-introducción)
2. [Objetivos de Aprendizaje](#2-objetivos-de-aprendizaje)
3. [Requisitos Previos](#3-requisitos-previos)
4. [Configuración del Entorno](#4-configuración-del-entorno)
5. [Estructura del Proyecto](#5-estructura-del-proyecto)
6. [Desarrollo Paso a Paso](#6-desarrollo-paso-a-paso)
    - [Crear y Configurar el Proyecto](#crear-y-configurar-el-proyecto)
    - [Crear Modelos](#crear-modelos)
    - [Definir Vistas](#definir-vistas)
    - [Configurar URLs](#configurar-urls)
    - [Crear Templates](#crear-templates)
7. [Aplicación del Principio DRY](#7-aplicación-del-principio-dry)
8. [Probar el Proyecto](#8-probar-el-proyecto)
9. [Conclusión](#9-conclusión)

---

## 1. Introducción

Este proyecto se centra en el desarrollo de una aplicación Django que gestiona productos de una tienda online. Utiliza las herramientas y conceptos fundamentales de Django, como entornos virtuales, arquitectura MVC y templates, para construir una aplicación web funcional y bien estructurada.

---

## 2. Objetivos de Aprendizaje

- Aislar dependencias utilizando entornos virtuales.
- Implementar el patrón MVC en Django.
- Configurar modelos, vistas y URLs para estructurar una aplicación.
- Utilizar templates para renderizar vistas dinámicas.
- Aplicar el principio DRY para evitar redundancias en el código.

---

## 3. Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.8 o superior.
- pip (gestor de paquetes de Python).
- Un editor de código, preferiblemente [Visual Studio Code](https://code.visualstudio.com/).

---

## 4. Configuración del Entorno

1. **Crear un entorno virtual:**
   ```bash
   python -m venv venv
   ```
2. **Activar el entorno virtual:**
   - En Windows:
     ```bash
     venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
3. **Instalar Django:**
   ```bash
   pip install django
   ```

---

## 5. Estructura del Proyecto

El proyecto tendrá la siguiente estructura inicial:

```
my_project/
├── core/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│       ├── base.html
│       ├── index.html
│       └── productos.html
├── my_project/
│   ├── settings.py
│   ├── urls.py
├── db.sqlite3
├── manage.py
```

---

## 6. Desarrollo Paso a Paso

### Crear y Configurar el Proyecto

1. Crea un proyecto Django:
   ```bash
   django-admin startproject my_project
   cd my_project
   ```
2. Crea una aplicación dentro del proyecto:
   ```bash
   python manage.py startapp core
   ```
3. Registra la aplicación en `settings.py`:
   ```python
   INSTALLED_APPS = [
       ...
       'core',
   ]
   ```

---

### Crear Modelos

1. Define el modelo `Producto` en `core/models.py`:
   ```python
   from django.db import models

   class Producto(models.Model):
       nombre = models.CharField(max_length=100)
       precio = models.DecimalField(max_digits=10, decimal_places=2)
       descripcion = models.TextField()

       def __str__(self):
           return self.nombre
   ```
2. Aplica las migraciones:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

---

### Definir Vistas

1. Agrega vistas en `core/views.py`:
   ```python
   from django.shortcuts import render
   from .models import Producto

   def index(request):
       return render(request, 'index.html')

   def productos(request):
       productos = Producto.objects.all()
       return render(request, 'productos.html', {'productos': productos})
   ```

---

### Configurar URLs

1. Crea un archivo `core/urls.py`:
   ```python
   from django.urls import path
   from . import views

   urlpatterns = [
       path('', views.index, name='index'),
       path('productos/', views.productos, name='productos'),
   ]
   ```
2. Conecta las URLs de la aplicación al proyecto en `my_project/urls.py`:
   ```python
   from django.contrib import admin
   from django.urls import include, path

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('core.urls')),
   ]
   ```

---

### Crear Templates

1. Crea un archivo base `base.html`:
   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>{% block title %}Tienda Online{% endblock %}</title>
   </head>
   <body>
       {% block content %}{% endblock %}
   </body>
   </html>
   ```

2. Crea `index.html`:
   ```html
   {% extends 'base.html' %}

   {% block title %}Inicio{% endblock %}

   {% block content %}
       <h1>Bienvenido a la Tienda Online</h1>
       <a href="/productos/">Ver Productos</a>
   {% endblock %}
   ```

3. Crea `productos.html`:
   ```html
   {% extends 'base.html' %}

   {% block title %}Productos{% endblock %}

   {% block content %}
       <h1>Listado de Productos</h1>
       <ul>
           {% for producto in productos %}
               <li>{{ producto.nombre }} - ${{ producto.precio }}</li>
           {% endfor %}
       </ul>
   {% endblock %}
   ```

---

## 7. Aplicación del Principio DRY

El principio DRY (Don't Repeat Yourself) se aplica utilizando `base.html` como plantilla base para reducir la redundancia de código en los templates.

---

## 8. Probar el Proyecto

1. **Ejecuta el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```
2. **Accede en el navegador:**
   - Página de inicio: `http://127.0.0.1:8000/`
   - Página de productos: `http://127.0.0.1:8000/productos/`

---

## 9. Conclusión

Este proyecto cubre conceptos clave de Django como entornos virtuales, el patrón MVC, templates dinámicos y el principio DRY. Sirve como una base sólida para proyectos más complejos. ¡Explora y experimenta con más funcionalidades para seguir aprendiendo Django!

---

