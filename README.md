# Web ISPP - FLASK

-A documentar-

## Installation

Este proyecto requiere Python 3.10 para poder ejecutarlo
*Se recomienda utilizar un Entorno virtual*

Instala las dependencias y los requerimientos para ejecutar el servidor
```sh
pip install -r requirements.txt
```
Descarga y importa las bases de datos a tu RDBMS, (Se utilizo MySQL para este proyecto) que se encuentra ubicado en *sql/DBISPPStructure.sql*:
- Se debe utilizar el archivo *sql/Testers.sql* para que el software tenga sus funcionalidades.

Se puede optar por instalar `python-dotenv` para ejecutar el archivo *.dot* o
Utilizar variables de entorno del sistema operativo (ya sea EXPORT o SET)

Las variables a definir son:
> FLASK_APP = entrypoint:app

> FLASK_ENV = development

> FLASK_DEBUG = true

> APP_SETTINGS_MODULE = config.default

> FLASK_RUN_HOST= 0.0.0.0

> FLASK_RUN_PORT= 8000

> MAIL_USERNAME='correo@gmail.com'

> MAIL_PASSWORD='password'

**Es importante editar el MAIL_USERNAME y MAIL_PASSWORD para que se pueda enviar correos. A lo contrario de no hacerlo, pueden llegar errores y el malfuncionamiento del sistema**

Se ejecuta el servidor con:
```sh
flask run
```
