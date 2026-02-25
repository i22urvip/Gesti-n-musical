# Gestión de Catálogo Musical (Orquesta)

Una aplicación web desarrollada en **Django** para gestionar el catálogo de obras y compositores de una orquesta. Este proyecto permite mantener un registro detallado del repertorio musical, con control de acceso y roles de usuario.

##  Características Principales

* **Catálogo de Obras:** Visualización detallada del repertorio (título, duración, instrumentos, partitura).
* **Gestión de Compositores (CRUD):** Creación, lectura y asociación de compositores a sus respectivas obras.
* **Sistema de Usuarios:** * Registro e inicio de sesión de usuarios.
   Formularios de registro personalizados y limpios.
* **Seguridad y Roles:** * Rutas protegidas para usuarios registrados.
  * Permisos exclusivos de Administrador (ej. borrado definitivo de compositores).
* **Base de Datos en la Nube:** Conectado a PostgreSQL a través de Neon.tech.

##  Tecnologías Utilizadas

* **Backend:** Python 3.12, Django 6.0
* **Base de Datos:** PostgreSQL (Neon)
* **Frontend:** HTML5, CSS3, Bootstrap 5 (Tarjetas, Formularios, Alertas)
* **Entorno:** GitHub Codespaces