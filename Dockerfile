# Development Dockerfile with nodemon for auto-reload
FROM python:3.11-slim-bullseye

WORKDIR /app

COPY ./requirements.txt requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
RUN mkdir /config

ADD driver.json .
ADD intg-stormaudio ./intg-stormaudio

# Network configuration
ENV UC_DISABLE_MDNS_PUBLISH="false"
ENV UC_MDNS_LOCAL_HOSTNAME=""
ENV UC_INTEGRATION_INTERFACE="0.0.0.0"
ENV UC_INTEGRATION_HTTP_PORT="9090"

# Configuration path
ENV UC_CONFIG_HOME="/config"

CMD ["python3", "-u", "intg-stormaudio/driver.py"]