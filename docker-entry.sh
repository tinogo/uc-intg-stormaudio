#!/bin/bash
# Docker entrypoint script

cd /usr/src/app
pip install --no-cache-dir -q -r requirements.txt
python -m uc_intg_stormaudio