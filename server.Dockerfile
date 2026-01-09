FROM python:3.11-slim-bullseye
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN uv pip install --no-cache-dir -r requirements.txt --system

ADD server.py .

CMD ["python3", "-u", "server.py"]