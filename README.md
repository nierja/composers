# Composers

[![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![Docker](https://img.shields.io/badge/Docker-0db7ed?logo=docker&logoColor=white)](https://www.docker.com/)
[![Python 3.12](https://img.shields.io/badge/Python_3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3120/)

SQLite database of classical music composers and their works. Simple installation via **Docker** Image. Written in Python using `SQLalchemy` module for database engine and `sqlite3` package that implements the SQLite interface.

### Running the database app

```bash
docker build -t classical_music_db .
docker run -p 8080:5000 classical_music_db
```

### Executing SQL queries:

Now that the app runs, you can execute queries:

```bash
# Give me all composers and data about them
$ curl -X POST -F 'query=SELECT * FROM composers;' http://localhost:8080/query

{   
    # pretty printed!
    # normally looks ugly!
    "result":
        [
            [1,"Ludwig van Beethoven","German","Classical/Romantic"],
            [2,"Johann Sebastian Bach","German","Baroque"],
            ...
        ]
}
```
