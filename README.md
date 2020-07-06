# BKR Python Challenge

Agustin Bassi - [jagustinbassi@gmail.com](mailto:jagustinbassi@gmail.com) -Julio 2020

![Coverage](https://img.shields.io/azure-devops/coverage/danielpalme/ReportGenerator/3.svg)



## 


## Tabla de contenido


* [Introducción al proyecto](#introduccion-al-proyecto)
* [Implementacion del proyecto](#implementación-del-proyecto)
* [Instalacion de dependencias](#instalación-de-dependencias)
* [Correr la aplicación](#correr-la-aplicación)
* [Probar la aplicación](#probar-la-aplicación)
* [Recursos disponibles](#recursos-disponibles)
* [Testing unitario](#testing-unitario)
* [TODOs](#todos)
* [Licencia](#licencia)

## 


## Introduccion al proyecto

El propósito de este proyecto es realizar una REST API capaz de realizar operaciones CRUD sobre Users y States. La aplicación debe aceptar peticiones HTTP con “Content-Type: application/json” únicamente. Así mismo, la tabla de States debe crearse automáticamente a partir del archivo states.csv ubicado en data/states.csv.

El modelo User se describe en la siguiente tabla.


<table>
  <tr>
   <td><strong>Column</strong>
   </td>
   <td><strong>Type</strong>
   </td>
  </tr>
  <tr>
   <td>id
   </td>
   <td>int sequence ( PK )
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td>string
   </td>
  </tr>
  <tr>
   <td>age
   </td>
   <td>int
   </td>
  </tr>
  <tr>
   <td>state
   </td>
   <td>int (FK states)
   </td>
  </tr>
  <tr>
   <td>updated_at
   </td>
   <td>datetime
   </td>
  </tr>
  <tr>
   <td>created_at
   </td>
   <td>datetime
   </td>
  </tr>
</table>


El modelo State se describe en la siguiente tabla.


<table>
  <tr>
   <td><strong>Column</strong>
   </td>
   <td><strong>Type</strong>
   </td>
  </tr>
  <tr>
   <td>id
   </td>
   <td>int sequence ( PK )
   </td>
  </tr>
  <tr>
   <td>name
   </td>
   <td>string
   </td>
  </tr>
  <tr>
   <td>code
   </td>
   <td>int
   </td>
  </tr>
  <tr>
   <td>updated_at
   </td>
   <td>datetime
   </td>
  </tr>
  <tr>
   <td>created_at
   </td>
   <td>datetime
   </td>
  </tr>
</table>



## 


## Implementación del proyecto

El proyecto fue realizado en Python utilizando las siguientes tecnologías/herramientas:



*   **Gitflow**: Metodología de control de versiones basado en branches especificas.
*   **Virutal Environment**: Instalación de las dependencias de la aplicación en un entorno aislado, durante la fase de desarrollo.
*   **Flask**: Framework de desarrollo web para la creación del backend.
*   **SQLAlchemy**: ORM por excelencia en Python para el acceso a distintas bases de datos a partir de clases de Python. Se utilizó Flask-SQLAlchemy para acceder a la DB y sqlalchemy_utils para crear automáticamente la base de datos.
*   **Ecosistema Docker (docker, Dockerfile, Docker-Compose)**: a partir del Dockerfile en el raíz del proyecto se puede compilar la imagen que corre la REST API hecha en Flask, con todas sus dependencias y código fuente dentro. Con Docker-Compose se puede ejecutar la aplicación con un único comando, creando además un servidor de base de datos PostgreSQL.
*   **Unittest**: Framework provisto en la librería standard de Python para realizar testing unitario del código.
*   **Pytest**: Framework para realizar además de testing de software, reporte de coverage (cobertura de código) en distintos formatos, entre ellos HTML.

A diferencia de otros proyectos de internet, en este proyecto no necesita operarse con la base de datos directamente, sino que, al iniciar la aplicación, ésta chequea que exista la base de datos (siempre y cuando haya conexión con el servidor), y en caso de no existir la crea automáticamente, así como también las tablas necesarias.

Durante la fase de desarrollo del proyecto se utilizó un entorno virtual de python con la variable de entorno FLASK_ENV=development. Esto permitió recargar el código automáticamente a medida que se realizaban cambios.

Cuando el código estuvo finalizado, se procedió a generar el archivo requirements.txt a partir de las dependencias del proyecto dentro del entorno virtual, luego se agregó la funcionalidad para compilar la imagen del serivio “api” dentro del archivo docker-compose.yml (build: .). Con la compilación de la imagen de esta manera, el código fuente quedó dentro de la imagen del servicio api.

 \
Es interesante notar que mediante el archivo .dockerignore se puede realizar la copia de todo el proyecto e ignorar archivos/directorios específicos dentro del contexto de Docker.


### 


### Estructura de directorios {#estructura-de-directorios}

La estructura de todo el proyecto se describe en de la siguiente forma.

```sh
├── data
│   ├── db_postgres [error opening dir]
│   └── states.csv
├── docker-compose.yml
├── Dockerfile
├── htmlcov
├── manage.py
├── README.md
├── run.py
├── src
│   ├── app.py
│   ├── config.py
│   ├── __init__.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── state_model.py
│   │   └── user_model.py
│   ├── requirements.txt
│   ├── shared
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   └── utils.py
│   ├── tests
│   │   ├── __init__.py
│   │   ├── test_state_views.py
│   │   └── test_user_views.py
│   └── views
│       ├── __init__.py
│       ├── state_views.py
│       └── user_views.py
└── uwsgi.ini
```

## 


## Instalación de dependencias

Para correr este proyecto se necesitan las siguientes dependencias:



*   [Python 3+](https://www.python.org/) (sólo necesario para modo desarrollo o testing).
*   [Docker](https://docs.docker.com/get-docker/).
*   [Docker compose](https://docs.docker.com/compose/install/).

Una vez instaladas las dependencias se puede correr la aplicación.


## 


## Correr la aplicación

La aplicación funciona sobre Docker-Compose, de esta manera se puede correr la misma en cualquier sistema operativo. El primer paso será compilar la imagen del servicio “api” a partir del archivo Dockerfile. Ejecutar el siguiente comando.


```
docker-compose build api
```


El siguiente paso es ejecutar la aplicación con el comando a continuación.


```
docker-compose up
```


_Nota: Si es la primera vez que se ejecuta la aplicación, puede haber errores en la ejecución del servicio “api” ya que puede darse el caso que el servicio “db” no haya creado la base de datos de manera correcta. Esto suele darse en varios escenarios trabajando con bases de datos, por eso, si se presenta tal problema ejecutar la aplicación en dos tramos, primero levantando el servicio de la base de datos._


```
docker-compose up -d db
```


Y unos segundos despues ejecutar el comando:


```
docker-compose up 
```


Es necesario notar que esto sólo ocurrirá la primera vez que se ejecute la aplicación.


### 


### Correr la aplicación con Python y Virtual Env {#correr-la-aplicación-con-python-y-virtual-env}

Si se desea agregar funcionalidad al código (modo desarrollo) o testear el codigo (modo testing) es conveniente realizar la operación utilizando un entorno virtual de python. Para ello crear el entorno virtual y activarlo con el siguiente comando.


```
python3 -m venv "$PWD"/.venv
source "$PWD"/.venv/bin/activate
```


Luego instalar las dependencias de python con el comando a continuación.


```
pip install -r src/requirements.txt
```


Ya que la aplicación debe conectarse con la base de datos para operar, primero será necesario ejecutar el servidor de base de datos con el siguiente comando.


```
docker-compose up -d db
```


A continuación exportar las variables de entorno que necesita la aplicación de python para comunicarse con la base de datos.


```
export DATABASE_URL=postgresql://bkr-user:bkr-pass@localhost:5432/bkr-db
export DATABASE_TEST_URL=postgresql://bkr-user:bkr-pass@localhost:5432/bkr-test-db
```


_Nota: es necesario que las configuraciones del usuario, contraseña y puerto de la base de datos en el archivo docker-compose.yml se correspondan con los datos exportados en los comandos anteriores como variables de entorno._

Finalmente correr la aplicación simplemente ejecutando el siguiente comando.


```
python run.py
```



## 


## Probar la aplicación

Para probar la aplicación se requiere de un cliente web como Postman.  Si el entorno donde se probará la aplicación es basado en Unix (Linux o MacOS) se puede utilizar la herramienta curl para realizar las pruebas de cada recurso.

Si se quiere más información sobre los recursos de la aplicación, en la sección Recursos disponibles se encuentran todos los detalles necesarios.

A continuación se detallan los comandos necesarios para realizar las pruebas con cada uno de los modelos.


### Usuarios {#usuarios}

Obtener todos los usuarios


<table>
  <tr>
   <td><strong>URI</strong>
   </td>
   <td><a href="http://localhost:5000/api/v1/users/">http://localhost:5000/api/v1/users/</a>
   </td>
  </tr>
  <tr>
   <td><strong>METHOD</strong>
   </td>
   <td>GET
   </td>
  </tr>
  <tr>
   <td><strong>Request Headers</strong>
   </td>
   <td>-
   </td>
  </tr>
  <tr>
   <td><strong>Request Body</strong>
   </td>
   <td>-
   </td>
  </tr>
</table>


Obtener o eliminar un usuario en particular.


<table>
  <tr>
   <td><strong>URI</strong>
   </td>
   <td><a href="http://localhost:5000/api/v1/users/id/">http://localhost:5000/api/v1/users/id/</a>
   </td>
  </tr>
  <tr>
   <td><strong>METHOD</strong>
   </td>
   <td>GET, DELETE
   </td>
  </tr>
  <tr>
   <td><strong>Request Headers</strong>
   </td>
   <td>-
   </td>
  </tr>
  <tr>
   <td><strong>Request Body</strong>
   </td>
   <td>-
   </td>
  </tr>
</table>


Crear o actualizar un usuario en particular


<table>
  <tr>
   <td><strong>URI</strong>
   </td>
   <td><a href="http://localhost:5000/api/v1/users/id/">http://localhost:5000/api/v1/users/id/</a>
   </td>
  </tr>
  <tr>
   <td><strong>METHOD</strong>
   </td>
   <td>POST, PUT
   </td>
  </tr>
  <tr>
   <td><strong>Request Headers</strong>
   </td>
   <td>“content-type”: “application/json”
   </td>
  </tr>
  <tr>
   <td><strong>Request Body</strong>
   </td>
   <td>{ “name”: “John Doe”, “age” : 30, “state_code” : 1}
   </td>
  </tr>
</table>



### Estados {#estados}

Obtener todos los estados


<table>
  <tr>
   <td><strong>URI</strong>
   </td>
   <td><a href="http://localhost:5000/api/v1/states/">http://localhost:5000/api/v1/states/</a>
   </td>
  </tr>
  <tr>
   <td><strong>METHOD</strong>
   </td>
   <td>GET
   </td>
  </tr>
  <tr>
   <td><strong>Request Headers</strong>
   </td>
   <td>-
   </td>
  </tr>
  <tr>
   <td><strong>Request Body</strong>
   </td>
   <td>-
   </td>
  </tr>
</table>


Obtener o eliminar un estado en particular.


<table>
  <tr>
   <td><strong>URI</strong>
   </td>
   <td><a href="http://localhost:5000/api/v1/states/id/">http://localhost:5000/api/v1/states/id/</a>
   </td>
  </tr>
  <tr>
   <td><strong>METHOD</strong>
   </td>
   <td>GET, DELETE
   </td>
  </tr>
  <tr>
   <td><strong>Request Headers</strong>
   </td>
   <td>-
   </td>
  </tr>
  <tr>
   <td><strong>Request Body</strong>
   </td>
   <td>-
   </td>
  </tr>
</table>


Crear o actualizar un estado en particular


<table>
  <tr>
   <td><strong>URI</strong>
   </td>
   <td><a href="http://localhost:5000/api/v1/states/id/">http://localhost:5000/api/v1/states/id/</a>
   </td>
  </tr>
  <tr>
   <td><strong>METHOD</strong>
   </td>
   <td>POST, PUT
   </td>
  </tr>
  <tr>
   <td><strong>Request Headers</strong>
   </td>
   <td>“content-type”: “application/json”
   </td>
  </tr>
  <tr>
   <td><strong>Request Body</strong>
   </td>
   <td>{ “name”: “Province”, “code” : 30 }
   </td>
  </tr>
</table>



## 


## Recursos disponibles

La aplicación presenta los siguientes recursos HTTP para realizar operaciones CRUD sobre cada uno de los datos.


### Recursos de Usuarios {#recursos-de-usuarios}


<table>
  <tr>
   <td><strong>Atributo</strong>
   </td>
   <td><strong>Valor</strong>
   </td>
  </tr>
  <tr>
   <td><strong>URI</strong>
   </td>
   <td><a href="http://localhost:5000/api/v1/users/">http://localhost:5000/api/v1/users/</a>
   </td>
  </tr>
  <tr>
   <td><strong>METHOD</strong>
   </td>
   <td>GET
   </td>
  </tr>
  <tr>
   <td><strong>Details</strong>
   </td>
   <td>Obtener todos los usuarios en la DB
   </td>
  </tr>
  <tr>
   <td><strong>Request Headers</strong>
   </td>
   <td>-
   </td>
  </tr>
  <tr>
   <td><strong>Request Body</strong>
   </td>
   <td>-
   </td>
  </tr>
  <tr>
   <td><strong>Response Body</strong>
   </td>
   <td>JSON con todos los usuarios
   </td>
  </tr>
  <tr>
   <td><strong>Response Status</strong>
   </td>
   <td>200
   </td>
  </tr>
</table>



<table>
  <tr>
   <td><strong>Atributo</strong>
   </td>
   <td><strong>Valor</strong>
   </td>
  </tr>
  <tr>
   <td><strong>URI</strong>
   </td>
   <td><a href="http://localhost:5000/api/v1/users/id/">http://localhost:5000/api/v1/users/id/</a>
   </td>
  </tr>
  <tr>
   <td><strong>METHOD</strong>
   </td>
   <td>GET, POST, PUT, DELETE
   </td>
  </tr>
  <tr>
   <td><strong>Details</strong>
   </td>
   <td>Obtener el detalle del usuario “id”.
   </td>
  </tr>
  <tr>
   <td><strong>Request Headers</strong>
   </td>
   <td>“Content-Type”: “application/json” (solo necesario en POST y PUT)
   </td>
  </tr>
  <tr>
   <td><strong>Request Body</strong>
   </td>
   <td>JSON con los datos del usuario a crear (POST, PUT), vacio para GET, DELETE.
   </td>
  </tr>
  <tr>
   <td><strong>Response Body</strong>
   </td>
   <td>JSON con todos los usuarios
   </td>
  </tr>
  <tr>
   <td><strong>Response Status</strong>
   </td>
   <td>200 = GET o PUT con exito
<p>
201 = POST con exito
<p>
204 = DELETE con exito
<p>
400 = POST o PUT con request body invalido
<p>
404 = No encontrado
   </td>
  </tr>
</table>



### Recursos de Estados {#recursos-de-estados}


<table>
  <tr>
   <td><strong>Atributo</strong>
   </td>
   <td><strong>Valor</strong>
   </td>
  </tr>
  <tr>
   <td><strong>URI</strong>
   </td>
   <td><a href="http://localhost:5000/api/v1/states/">http://localhost:5000/api/v1/states/</a>
   </td>
  </tr>
  <tr>
   <td><strong>METHOD</strong>
   </td>
   <td>GET
   </td>
  </tr>
  <tr>
   <td><strong>Details</strong>
   </td>
   <td>Obtener todos los estados en la DB
   </td>
  </tr>
  <tr>
   <td><strong>Request Headers</strong>
   </td>
   <td>-
   </td>
  </tr>
  <tr>
   <td><strong>Request Body</strong>
   </td>
   <td>-
   </td>
  </tr>
  <tr>
   <td><strong>Response Body</strong>
   </td>
   <td>JSON con todos los estados
   </td>
  </tr>
  <tr>
   <td><strong>Response Status</strong>
   </td>
   <td>200
   </td>
  </tr>
</table>



<table>
  <tr>
   <td><strong>Atributo</strong>
   </td>
   <td><strong>Valor</strong>
   </td>
  </tr>
  <tr>
   <td><strong>URI</strong>
   </td>
   <td><a href="http://localhost:5000/api/v1/states/id/">http://localhost:5000/api/v1/states/id/</a>
   </td>
  </tr>
  <tr>
   <td><strong>METHOD</strong>
   </td>
   <td>GET, POST, PUT, DELETE
   </td>
  </tr>
  <tr>
   <td><strong>Details</strong>
   </td>
   <td>Obtener el detalle del estado “id”.
   </td>
  </tr>
  <tr>
   <td><strong>Request Headers</strong>
   </td>
   <td>“Content-Type”: “application/json” (solo necesario en POST y PUT)
   </td>
  </tr>
  <tr>
   <td><strong>Request Body</strong>
   </td>
   <td>JSON con los datos del estado a crear (POST, PUT), vacio para GET, DELETE.
   </td>
  </tr>
  <tr>
   <td><strong>Response Body</strong>
   </td>
   <td>JSON con todos los estados
   </td>
  </tr>
  <tr>
   <td><strong>Response Status</strong>
   </td>
   <td>200 = GET o PUT con exito
<p>
201 = POST con exito
<p>
204 = DELETE con exito
<p>
400 = POST o PUT con request body invalido
<p>
404 = No encontrado
   </td>
  </tr>
</table>



## 


## Testing unitario

Para todas los endpoints HTTP de la aplicación (usuarios y estados) se crearon sus correspondientes test cases, con el objetivo de intentar probar todos los posibles casos. Para ello sobre cada test se crearon sus casos de éxito (es decir con datos/argumentos que la aplicación espera), así como también datos/argumentos erroneos, con el proposito de chequear los mensajes de error.

Todos los test cases se realizaron con el framework unittest provisto en la libreria standard de python. Así mismo, se utilizó al cliente de test de Flask para poder realizar las peticiones HTTP, creando la aplicación con el flag Testing=True.

Para realizar el testing unitario es necesario crear un entorno virtual e instalar las dependencias, tal como se detalla en la sección Correr la aplicación con “Python y Virtual Environment”.

Una vez que se instalaron las dependencias, simplemente sobre el raíz del proyecto ejecutar el siguiente comando.


```
python -m unittest -v
```


Debería verse una salida como la que se muestra a continuación.


```
ok
test_create_state_ok (src.tests.test_state_views.StateTest) ... ok
test_delete_state_not_found (src.tests.test_state_views.StateTest) ... ok
test_delete_state_ok (src.tests.test_state_views.StateTest) ... ok
test_get_all_states (src.tests.test_state_views.StateTest) ... ok
test_get_state_not_found (src.tests.test_state_views.StateTest) ... ok
test_get_state_ok (src.tests.test_state_views.StateTest) ... ok
test_update_state_bad_request (src.tests.test_state_views.StateTest) ... ok
test_update_state_not_found (src.tests.test_state_views.StateTest) ... ok
test_update_state_ok (src.tests.test_state_views.StateTest) ... ok
test_create_user_bad_request (src.tests.test_user_views.UsersTest) ... ok
test_create_user_ok (src.tests.test_user_views.UsersTest) ... ok
test_delete_user_not_found (src.tests.test_user_views.UsersTest) ... ok
test_delete_user_ok (src.tests.test_user_views.UsersTest) ... ok
test_get_all_users (src.tests.test_user_views.UsersTest) ... ok
test_get_user_not_found (src.tests.test_user_views.UsersTest) ... ok
test_get_user_ok (src.tests.test_user_views.UsersTest) ... ok
test_update_user_bad_request (src.tests.test_user_views.UsersTest) ... ok
test_update_user_not_found (src.tests.test_user_views.UsersTest) ... ok
test_update_user_ok (src.tests.test_user_views.UsersTest) ... ok

----------------------------------------------------------------------
Ran 20 tests in 4.092s
```



### Coverage {#coverage}

A partir de los test cases generados se puede crear un reporte de coverage, que indica qué porcentaje del código pudo ser probado de manera automática. Debido a que este reporte se genera automáticamente no se suele agregar en un repositorio, pero dadas las circunstancias de este proyecto se decidió agregarlo con el objetivo de mostrar el reporte sin necesidad de correr la aplicación en un entorno virtual.

El reporte se encuentra dentro de la carpeta htmlcov/, y para poder visualizar el mismo, abrir el archivo index.html desde un navegador web.

Para generar el reporte de código, a partir del entorno virtual de Python creado previamente, instalar las siguientes dependencias.


```
pip install pytest pytest-html pytest-cov
```


A continuación generar el reporte con el siguiente comando.


```
pytest --cov=src --ignore=data --cov-report html
```


La ejecución del comando anterior reemplazará el contenido del directorio htmlcov/ o bien lo creará en caso que no exista. 

Abrir el archivo htmlcov/index.html  para visualizar el reporte.


## 


## TODOs



*   Subir proyecto a un repositorio publico.
*   Agregar login para acceder a la API.
*   Utilizar HTTPS.
*   Utilizar un entrypoint en el servicio API para iniciar la aplicación de Flask una vez que la base de datos esté operativa.


## 


## Licencia

Copyright Agustin Bassi - 2020
