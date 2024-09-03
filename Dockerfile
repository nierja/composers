FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN rm classical_music.db
RUN pip install sqlalchemy flask
RUN python src/db_create_and_insert.py
CMD ["python", "src/db_app.py"]