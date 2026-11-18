#!/bin/bash
# Docker entrypoint script

cd /usr/src/app
uv sync --locked --no-dev --no-install-project
exec uv run --locked --no-sync python -m uc_intg_stormaudio