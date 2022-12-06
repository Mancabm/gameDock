# gameDock

<h1>Instalación del proyecto</h1>
    <p>1. Clonar el repositorio</p>
    <p>2. Desde la terminal (en la caperta del proyecto) ejecutar pip install -r requirements.txt</p>
    <p>3. Crear un archivo .env dentro de GameDock y añadir los campo SECRET_KEY y PASSWORD generadas de forma
        segura</p>
    <p>4. Descargar postgresql https://www.postgresql.org version 14.6</p>
    <p>5. Seguir guía para instalación en Windows https://www.postgresqltutorial.com/postgresql-getting-started/install-postgresql/ <b>usar puerto 5432</b></p>
    <p>6. Lanzad pgAdmin4</p>
    <p>7. Seguir https://chartio.com/learn/postgresql/create-a-user-with-pgadmin/ para crear un usuario <bu>gamedock<bu> con password <bu>La password metida dentro de .env como PASSWORD</bu></p>
    <p>8. Crear una base de datos llamada <b>gamedock</b> y dar permisos al usuario <b>gamedock</b></p>
    <p>9. Desde la terminal (en la caperta del proyecto) ejecutar python3 manage.py migrate</p>
    <p>10. Si no da errores la instalación se ha completado</p>
