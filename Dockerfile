FROM python:3.14-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

RUN mkdir /config

COPY ./pyproject.toml ./uv.lock ./
RUN uv sync --locked --no-dev --no-install-project
ENV PATH="/app/.venv/bin:$PATH"

COPY driver.json .
COPY uc_intg_stormaudio ./uc_intg_stormaudio

# Configuration path
ENV UC_CONFIG_HOME="/config"

CMD ["python3", "-m", "uc_intg_stormaudio"]