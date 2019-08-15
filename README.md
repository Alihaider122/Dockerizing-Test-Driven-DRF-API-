# Dockerizing-Test-Driven-DRF-API-
### Requirements
* Docker(Linux, MacOS or Windows)
* Docker Compose
### Run
In the root directory you have to open cmd and run following commands
$ docker-compose run web python django-rest-practice/manage.py migrate
$ docker-compose up

And access API endpoints on http://localhost:8000/app/projects/

### Endpoints
GET /       http://localhost:8000/app/projects/
POST /      http:://localhost:8000/app/projects/
GET :id/    https://localhsot:8000/app/projects/id/
PUT :id/    https://localhsot:8000/app/projects/id/
DELETE :id/ https://localhsot:8000/app/projects/1/

### RUN tests
to run tests run the following commands on CMD
$ docker-compose run web pytest django-rest-practice/tests
