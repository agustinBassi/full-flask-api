# Ejercicio BKR

El ejercicio consiste de hacer una api con 2 tablas y armar endpoint REST para consultar,
crear, borrar o actualizar ambas tablas. Los servicios deben responder manejando solo el *Accept: application/json*

- [] Generar tablas `users` y `states`
- [] Importar informacion del archivo `stats.csv` en la tabla `states`
- [] Generar CRUD (REST) de `users`
- [] Generar endpoint (REST) `states`


## Tablas


### Users

Column | Type
------ | ----
id | int sequence ( PK )
name | string
age | int
state | int (FK states)
updated_at | datetime
created_at | datetime

### States
Column | Type
------ | ----
id | int sequence ( PK )
code | int
name | string
updated_at | datetime
created_at | datetime


# TESTs

Todos los test cases juntos desde la raiz con

python -m unittest -v

Para generar el reporte de coverage

pip install pytest
pip install pytest-html

Para correr todos los test cases y generar una carpeta llamada htmlcov

pytest --cov=src --ignore=data --cov-report html

Poner una captura de pantalla en el readme y explicar como generar los tests pero no incluirlos en el codigo (o si).

Aclarar que la DB debe ponerse en test para test y luego poner la otra para produccion

Aclarar que las configuraciones ya estan armadas desde el config.py para que no se necesite hacer mucho desde afuera 

Aclarar lo de correr el compose de esta manera

sudo docker-compose up -d db

La DB no necesita crearse para el test, ya que la APP la genera automaticamente

