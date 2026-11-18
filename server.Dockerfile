FROM python:3.14-slim-trixie

WORKDIR /app

COPY server.py .

CMD ["python3", "-u", "server.py"]