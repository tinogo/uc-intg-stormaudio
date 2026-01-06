# Development Dockerfile with nodemon for auto-reload
FROM python:3.11-slim-bullseye

WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

ADD server.py .

CMD ["python3", "-u", "server.py"]