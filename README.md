# Gestión de Catálogo Musical (Orquesta)

Una aplicación web desarrollada en **Django** para gestionar el catálogo de obras y compositores de una orquesta. Este proyecto permite mantener un registro detallado del repertorio musical, con control de acceso y roles de usuario.

## Características Principales

* **Catálogo de Obras:** Visualización detallada del repertorio (título, duración, instrumentos, partitura).
* **Gestión de Compositores (CRUD):** Creación, lectura y asociación de compositores a sus respectivas obras.
* **Sistema de Usuarios:** * Registro e inicio de sesión de usuarios.
* Formularios de registro personalizados y limpios.


* **Seguridad y Roles:** * Rutas protegidas para usuarios registrados.
* Permisos exclusivos de Administrador (ej. borrado definitivo de compositores).


* **Base de Datos en la Nube:** Conectado a PostgreSQL a través de Neon.tech.

## Tecnologías Utilizadas

* **Backend:** Python 3.12, Django 6.0
* **Base de Datos:** PostgreSQL (Neon)
* **Frontend:** HTML5, CSS3, Bootstrap 5 (Tarjetas, Formularios, Alertas)
* **Entorno:** GitHub Codespaces

## Estructura de Directorios y Ficheros

El proyecto "El Rincón del Músico" sigue de forma estricta la arquitectura **MVT (Modelo-Vista-Plantilla)** propia del framework Django. Cada archivo tiene una única responsabilidad para mantener el código limpio y escalable.

A modo de analogía, podemos imaginar el proyecto como un gran restaurante:

```text
Gesti-n-musical/
├── manage.py
├── .env
├── requirements.txt
├── venv/
├── orquesta/
│   ├── settings.py
│   └── urls.py
└── catalogo/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── tests.py
    └── templates/
        └── catalogo/

```

### 1. La Raíz del Proyecto

Contiene los archivos de configuración general y el entorno de ejecución que hacen que todo el sistema funcione.

* **`manage.py`:** Es el script principal de Django y el punto de entrada. Nunca escribimos código dentro de él, pero lo usamos constantemente en la terminal para darle órdenes al sistema (ej. `python manage.py runserver` o `makemigrations`).
* **`.env` :** Archivo de variables de entorno (ignorado en GitHub por seguridad) que almacena credenciales sensibles, como la `SECRET_KEY` de Django y la `DATABASE_URL` para conectarnos a PostgreSQL en Neon.
* **`requirements.txt` :** Un archivo de texto que detalla qué herramientas y librerías extra (Django, psycopg2, python-dotenv...) necesita el proyecto para funcionar en cualquier ordenador.
* **`venv/` :** Directorio generado automáticamente que contiene el Entorno Virtual. Aísla las dependencias de nuestro proyecto para que no interfieran con el sistema operativo local.

### 2. Directorio de Configuración: `orquesta/`

Es el núcleo central que administra el comportamiento global de la aplicación web.

* **`settings.py`:** Aquí configuramos absolutamente todo el proyecto: la conexión a la base de datos, las variables de entorno, los idiomas, y qué aplicaciones ("apps") están instaladas.
* **`urls.py`:** Intercepta las peticiones web entrantes y las redirige. Por ejemplo, si un usuario entra a la web, este archivo le dice: "Pasa por esta puerta y habla con la aplicación Catálogo".

### 3. Aplicación Principal: `catalogo/`

En Django, un proyecto se divide en "apps". Esta carpeta contiene el 90% de nuestro código y representa la lógica de negocio de "El Rincón del Músico".

* **`models.py`:** Define la estructura de la base de datos mediante clases de Python (ORM). Aquí se alojan las entidades `Compositor` y `Obra`, indicando a PostgreSQL qué columnas debe tener cada tabla (nombre, época, duración...).
* **`views.py`:** Es el puente de comunicación. Cuando un usuario pide ver las obras, la *Vista* va a la base de datos (*Modelos*), extrae la información y se la entrega a la página web (*Plantillas*) para que el usuario la visualice.
* **`urls.py`:** Funciona igual que el recepcionista principal, pero dedicado en exclusiva a esta app. Asocia rutas específicas (ej. `/obras/`) con la vista correcta que debe ejecutarse.
* **`templates/catalogo/`:** Directorio que almacena los archivos HTML (como `lista_obras.html`). Es la cara visible de la web, donde aplicamos las clases de Bootstrap 5 para crear la interfaz gráfica (colores burdeos, fondo crema y tarjetas de presentación).
* **`tests.py`:** Archivo dedicado a las pruebas unitarias (Unit Testing). Asegura automáticamente que la lógica no se rompa al hacer cambios, comprobando que, por ejemplo, un Compositor se guarda correctamente en la base de datos.
