# Composers

[![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Docker](https://img.shields.io/badge/Docker-0db7ed?logo=docker&logoColor=white)](https://www.docker.com/)
[![Python 3.12](https://img.shields.io/badge/Python_3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3120/)

SQLite database of clasical music composers and works. Simple instalation via Docker Image. Written in Python using `SQLalchemy` module for database engine and `sqlite3` packege that implements the SQLite interface.

## RUnning and testing the container

Run the database app:

```bash
dockestop $(docker ps -q) && docker rm $(docker ps -a -q) # kill all containers
docker build -t classical_music_db .
docker run -p 5000:5000 classical_music_db
```

And ASK things:

```bash
$ curl -X POST -F 'query=SELECT * FROM composers;' http://localhost:5000/query
{"result":[[1,"Beethoven","German","Classical"],[2,"Bach","German","Baroque"]]}
```


# TODO

* relational diagram
* features
* instalation guide via docker