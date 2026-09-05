FROM python:3.11-slim-bullseye
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN uv pip install --no-cache-dir -r requirements.txt --system
RUN mkdir /config

COPY driver.json .
COPY uc_intg_stormaudio ./uc_intg_stormaudio

# Configuration path
ENV UC_CONFIG_HOME="/config"

CMD ["python3", "-m", "uc_intg_stormaudio"]