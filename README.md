# Dockerizing-Test-Driven-DRF-API-
### Requirements
* Docker(Linux, MacOS or Windows)
* Docker Compose
### Run
In the root directory you have to open cmd and run following commands\n
$ docker-compose run web python django-rest-practice/manage.py migrate\n
$ docker-compose up\n

And access API endpoints on http://localhost:8000/app/projects/

### Endpoints
GET /       http://localhost:8000/app/projects/ \n
POST /      http:://localhost:8000/app/projects/ \n
GET :id/    https://localhsot:8000/app/projects/id/ \n
PUT :id/    https://localhsot:8000/app/projects/id/ \n
DELETE :id/ https://localhsot:8000/app/projects/1/ \n

### RUN tests
to run tests run the following commands on CMD \n
$ docker-compose run web pytest django-rest-practice/tests \n
