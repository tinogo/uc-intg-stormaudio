FROM python:3.11-slim-bullseye
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN uv pip install --no-cache-dir -r requirements.txt --system
RUN mkdir /config

ADD driver.json .
ADD uc_intg_stormaudio ./uc_intg_stormaudio

# Network configuration
ENV UC_DISABLE_MDNS_PUBLISH="false"
ENV UC_MDNS_LOCAL_HOSTNAME=""
ENV UC_INTEGRATION_INTERFACE="0.0.0.0"
ENV UC_INTEGRATION_HTTP_PORT="9090"

# Configuration path
ENV UC_CONFIG_HOME="/config"

CMD ["python3", "-m", "uc_intg_stormaudio"]