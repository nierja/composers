FROM python:3.12-slim
WORKDIR /app
COPY . /app
RUN rm classical_music.db
RUN pip install sqlalchemy flask
RUN python db_engine.py
CMD ["python", "db_app.py"]