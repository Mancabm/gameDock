# gameDock

Instalación del proyecto
-------------
    1. Clonar el repositorio
    2. Desde la terminal (en la caperta del proyecto) ejecutar pip install -r requirements.txt
    3. Descargar postgresql https://www.postgresql.org version 14.6
    4. Seguir guía para instalación en Windows https://www.postgresqltutorial.com/postgresql-getting-started/install-postgresql/ <b>usar puerto 5432</b>
    5. Lanzad pgAdmin4
    6. Seguir https://chartio.com/learn/postgresql/create-a-user-with-pgadmin/ para crear un usuario <bu>gamedock</bu> com password <bu>gameDock</bu>
    7. Crear una base de datos llamada <b>gamedock<b> y dar permisos al usuario <b>gameDock</b>
    8. Desde la terminal (en la caperta del proyecto) ejecutar python3 manage.py migrate
    9. Si no da errores la instalación se ha completado 