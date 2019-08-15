# Dockerizing-Test-Driven-DRF-API-
### Requirements
* Docker(Linux, MacOS or Windows)
* Docker Compose
### Run
In the root directory you have to open cmd and run following commands <br/>
$ docker-compose run web python django-rest-practice/manage.py migrate <br/>
$ docker-compose up <br/>

And access API endpoints on http://localhost:8000/app/projects/

### Endpoints
GET /       http://localhost:8000/app/projects/ <br/>
POST /      http://localhost:8000/app/projects/ <br/>
GET :id/    https://localhsot:8000/app/projects/id/ <br/>
PUT :id/    https://localhsot:8000/app/projects/id/ <br/>
DELETE :id/ https://localhsot:8000/app/projects/1/ <br/>

### RUN tests
to run tests run the following commands on CMD <br/>
$ docker-compose run web python django-rest-practice/manage.py dumpdata > testdata.json <br/>
$ docker-compose run web pytest django-rest-practice/tests <br/>
